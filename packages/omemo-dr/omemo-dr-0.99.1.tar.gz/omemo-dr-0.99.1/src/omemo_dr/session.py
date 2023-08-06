from __future__ import annotations

from typing import Any
from typing import Optional

import logging
import time
from collections import defaultdict

from . import exceptions
from .aes import aes_decrypt
from .aes import aes_encrypt
from .aes import get_new_iv
from .aes import get_new_key
from .const import OMEMOTrust
from .ecc.djbec import CurvePublicKey
from .identitykey import IdentityKey
from .identitykeypair import IdentityKeyPair
from .observable import Observable
from .protocol.prekeywhispermessage import PreKeyWhisperMessage
from .protocol.whispermessage import WhisperMessage
from .sessionbuilder import SessionBuilder
from .sessioncipher import SessionCipher
from .state.prekeybundle import PreKeyBundle
from .state.store import Store
from .structs import OMEMOBundle
from .structs import OMEMOConfig
from .structs import OMEMOMessage
from .util.keyhelper import KeyHelper

log = logging.getLogger(__name__)


class OMEMOSession(Observable):
    def __init__(self, own_address: str, storage: Store, config: OMEMOConfig) -> None:
        Observable.__init__(self, log)
        self._device_store: dict[str, set[int]] = defaultdict(set)
        self._group_member_store: dict[str, set[str]] = defaultdict(set)
        self._session_ciphers: dict[str, dict[int, SessionCipher]] = defaultdict(dict)

        self._own_address = own_address
        self._storage = storage
        self._config = config

        if self._storage.needs_init():
            logging.info("Generating OMEMO keys")
            self._own_device_id = self._generate_keys()
        else:
            self._own_device_id = self._storage.get_local_registration_id()

        self.add_device(self._own_address, self._own_device_id)
        logging.info("Our device id: %s", self._own_device_id)

        logging.info("%s PreKeys available", self._storage.get_pre_key_count())

        for address, device in self._storage.get_active_device_tuples():
            logging.info("Load device from storage: %s - %s", address, device)
            self.add_device(address, device)

    def _generate_keys(self) -> int:
        identity_key_pair = KeyHelper.generate_identity_key_pair()
        own_device_id = KeyHelper.get_random_sequence(2147483647)
        self._storage.store_own_identity(own_device_id, identity_key_pair)

        signed_pre_key = KeyHelper.generate_signed_pre_key(
            identity_key_pair, KeyHelper.get_random_sequence(65536)
        )
        self._storage.store_signed_pre_key(signed_pre_key.get_id(), signed_pre_key)

        self._generate_pre_keys(self._config.default_prekey_amount)

        return own_device_id

    def _generate_pre_keys(self, count: int) -> None:
        prekey_id = self._storage.get_current_pre_key_id() or 0
        pre_keys = KeyHelper.generate_pre_keys(prekey_id + 1, count)
        for pre_key in pre_keys:
            self._storage.store_pre_key(pre_key.get_id(), pre_key)

    def build_session(self, address: str, device_id: int, bundle: OMEMOBundle) -> None:
        session = SessionBuilder(self._storage, address, device_id)

        prekey = bundle.pick_prekey()
        otpk = CurvePublicKey(prekey["key"][1:])

        spk = CurvePublicKey(bundle.spk["key"][1:])
        ik = IdentityKey(CurvePublicKey(bundle.ik[1:]))

        prekey_bundle = PreKeyBundle(
            self._own_device_id,
            device_id,
            prekey["id"],
            otpk,
            bundle.spk["id"],
            spk,
            bundle.spk_signature,
            ik,
        )

        session.process_pre_key_bundle(prekey_bundle)
        self._get_session_cipher(address, device_id)

    @property
    def storage(self) -> Any:
        return self._storage

    def get_own_fingerprint(self, *, formatted: bool = False) -> str:
        identity_key = self._storage.get_identity_key_pair().get_public_key()
        return identity_key.get_fingerprint(formatted=formatted)

    def get_bundle(self) -> OMEMOBundle:
        self._check_pre_key_count()

        bundle: dict[str, Any] = {"otpks": []}
        for k in self._storage.load_pending_pre_keys():
            key = k.get_key_pair().get_public_key().serialize()
            bundle["otpks"].append({"key": key, "id": k.get_id()})

        ik_pair = self._storage.get_identity_key_pair()
        bundle["ik"] = ik_pair.get_public_key().serialize()

        self._cycle_signed_pre_key(ik_pair)

        spk = self._storage.load_signed_pre_key(
            self._storage.get_current_signed_pre_key_id()
        )
        bundle["spk_signature"] = spk.get_signature()
        bundle["spk"] = {
            "key": spk.get_key_pair().get_public_key().serialize(),
            "id": spk.get_id(),
        }

        return OMEMOBundle(**bundle)

    def decrypt_message(
        self, omemo_message: OMEMOMessage, address: str
    ) -> tuple[str, str, OMEMOTrust]:
        if omemo_message.sid == self.get_own_device():
            logging.info("Received previously sent message by us")
            raise exceptions.SelfMessage

        try:
            encrypted_key, prekey = omemo_message.keys[self.get_own_device()]
        except KeyError:
            logging.info("Received message not for our device")
            raise exceptions.MessageNotForDevice

        try:
            if prekey:
                key, fingerprint, trust = self._process_pre_key_message(
                    address, omemo_message.sid, encrypted_key
                )
            else:
                key, fingerprint, trust = self._process_message(
                    address, omemo_message.sid, encrypted_key
                )

        except exceptions.DuplicateMessageException:
            logging.info("Received duplicated message")
            raise exceptions.DuplicateMessage

        except Exception as error:
            logging.warning(error)
            raise exceptions.DecryptionFailed

        if omemo_message.payload is None:
            logging.debug("Decrypted Key Exchange Message")
            raise exceptions.KeyExchangeMessage

        try:
            result = aes_decrypt(key, omemo_message.iv, omemo_message.payload)
        except Exception as error:
            logging.warning(error)
            raise exceptions.DecryptionFailed

        logging.debug("Decrypted Message => %s", result)
        return result, fingerprint, trust

    def _get_whisper_message(
        self, address: str, device: int, key: bytes
    ) -> tuple[bytes, bool]:
        cipher = self._get_session_cipher(address, device)
        cipher_key = cipher.encrypt(key)
        prekey = isinstance(cipher_key, PreKeyWhisperMessage)
        return cipher_key.serialize(), prekey

    def encrypt(
        self, address: str, plaintext: str, *, groupchat: bool
    ) -> Optional[OMEMOMessage]:
        try:
            devices_for_encryption = self.get_devices_for_enc(
                address, groupchat=groupchat
            )
        except exceptions.NoDevicesFound:
            logging.warning("No devices for encryption found for: %s", address)
            return

        result = aes_encrypt(plaintext)
        whisper_messages: dict[str, dict[int, tuple[bytes, bool]]] = defaultdict(dict)

        for address_, device in devices_for_encryption:
            count = self._storage.get_unacknowledged_count(address_, device)
            if count >= self._config.unacknowledged_count:
                logging.warning(
                    "Set device inactive %s because of %s unacknowledged messages",
                    device,
                    count,
                )
                self.remove_device(address_, device)

            try:
                whisper_messages[address_][device] = self._get_whisper_message(
                    address_, device, result.key
                )
            except Exception:
                logging.exception("Failed to encrypt")
                continue

        recipients = set(whisper_messages.keys())
        if address != self._own_address:
            recipients -= {self._own_address}
        if not recipients:
            logging.error("Encrypted keys empty")
            return

        encrypted_keys: dict[int, tuple[bytes, bool]] = {}
        for address_ in whisper_messages:
            encrypted_keys.update(whisper_messages[address_])

        logging.debug("Finished encrypting message")
        return OMEMOMessage(
            sid=self.get_own_device(),
            keys=encrypted_keys,
            iv=result.iv,
            payload=result.payload,
        )

    def encrypt_key_transport(
        self, address: str, devices: list[int]
    ) -> Optional[OMEMOMessage]:
        whisper_messages: dict[str, dict[int, tuple[bytes, bool]]] = defaultdict(dict)
        for device in devices:
            try:
                whisper_messages[address][device] = self._get_whisper_message(
                    address, device, get_new_key()
                )
            except Exception:
                logging.exception("Failed to encrypt")
                continue

        if not whisper_messages[address]:
            logging.error("Encrypted keys empty")
            return

        logging.debug("Finished Key Transport message")
        return OMEMOMessage(
            sid=self.get_own_device(),
            keys=whisper_messages[address],
            iv=get_new_iv(),
            payload=None,
        )

    def has_trusted_keys(self, address: str) -> bool:
        inactive = self._storage.get_inactive_sessions_keys(address)
        trusted = self._storage.get_trusted_fingerprints(address)
        return bool(set(trusted) - set(inactive))

    def get_devices_without_sessions(self, address: str) -> list[int]:
        known_devices = self.get_devices(address, without_self=True)
        missing_devices = [
            dev
            for dev in known_devices
            if not self._storage.contains_session(address, dev)
        ]
        if missing_devices:
            logging.info("Missing device sessions for %s: %s", address, missing_devices)
        return missing_devices

    def _get_session_cipher(self, address: str, device_id: int) -> SessionCipher:
        try:
            return self._session_ciphers[address][device_id]
        except KeyError:
            cipher = SessionCipher(
                self._storage,
                address,
                device_id,
            )
            self._session_ciphers[address][device_id] = cipher
            return cipher

    def _process_pre_key_message(
        self, address: str, device: int, key: bytes
    ) -> tuple[bytes, str, OMEMOTrust]:
        logging.info("Process pre key message from %s", address)
        pre_key_message = PreKeyWhisperMessage.from_bytes(key)
        if not pre_key_message.get_pre_key_id():
            raise Exception("Received Pre Key Message without PreKey => %s" % address)

        session_cipher = self._get_session_cipher(address, device)
        key = session_cipher.decrypt_pkmsg(pre_key_message)

        identity_key = pre_key_message.get_identity_key()
        trust = self._get_trust_from_identity_key(address, identity_key)
        fingerprint = identity_key.get_fingerprint()

        self._storage.set_identity_last_seen(address, identity_key)

        self.add_device(address, device)
        self._notify("republish-bundle", self.get_bundle())
        return key, fingerprint, trust

    def _process_message(
        self, address: str, device: int, key: bytes
    ) -> tuple[bytes, str, OMEMOTrust]:
        logging.info("Process message from %s", address)
        message = WhisperMessage.from_bytes(key)

        session_cipher = self._get_session_cipher(address, device)
        key = session_cipher.decrypt_msg(message)

        identity_key = self._get_identity_key_from_device(address, device)
        assert identity_key is not None
        trust = self._get_trust_from_identity_key(address, identity_key)
        fingerprint = identity_key.get_fingerprint()

        self._storage.set_identity_last_seen(address, identity_key)

        self.add_device(address, device)

        return key, fingerprint, trust

    def _get_identity_key_from_device(
        self, address: str, device: int
    ) -> Optional[IdentityKey]:
        session_record = self._storage.load_session(address, device)
        return session_record.get_session_state().get_remote_identity_key()

    def _get_trust_from_identity_key(
        self, address: str, identity_key: IdentityKey
    ) -> OMEMOTrust:
        trust = self._storage.get_trust_for_identity(address, identity_key)
        return OMEMOTrust(trust) if trust is not None else OMEMOTrust.UNDECIDED

    def _check_pre_key_count(self) -> None:
        # Check if enough PreKeys are available
        pre_key_count = self._storage.get_pre_key_count()
        if pre_key_count < self._config.min_prekey_amount:
            missing_count = self._config.default_prekey_amount - pre_key_count
            self._generate_pre_keys(missing_count)
            logging.info("%s PreKeys created", missing_count)

    def _cycle_signed_pre_key(self, ik_pair: IdentityKeyPair) -> None:
        # Publish every spk_cycle_seconds a new SignedPreKey
        # Delete all existing SignedPreKeys that are older
        # then spk_archive_seconds

        # if spk_cycle_seconds is reached, generate a new SignedPreKey
        now = int(time.time())
        timestamp = self._storage.get_signed_pre_key_timestamp(
            self._storage.get_current_signed_pre_key_id()
        )

        if int(timestamp) < now - self._config.spk_cycle_seconds:
            spk = KeyHelper.generate_signed_pre_key(
                ik_pair, self._storage.get_next_signed_pre_key_id()
            )
            self._storage.store_signed_pre_key(spk.get_id(), spk)
            logging.debug("Cycled SignedPreKey")

        # Delete all SignedPreKeys that are older than spk_archive_seconds
        timestamp = now - self._config.spk_archive_seconds
        self._storage.remove_old_signed_pre_keys(timestamp)

    def update_devicelist(self, address: str, devicelist: list[int]) -> None:
        for device in list(devicelist):
            if device == self.get_own_device():
                continue
            count = self._storage.get_unacknowledged_count(address, device)
            if count > self._config.unacknowledged_count:
                logging.warning(
                    "Ignore device because of %s unacknowledged messages: %s %s",
                    count,
                    address,
                    device,
                )
                devicelist.remove(device)

        self._device_store[address] = set(devicelist)
        logging.info("Saved devices for %s", address)
        self._storage.set_active_state(address, devicelist)

    def add_group_member(self, group_address: str, address: str) -> None:
        logging.info("Saved group member %s %s", group_address, address)
        self._group_member_store[group_address].add(address)

    def remove_group_member(self, group_address: str, address: str) -> None:
        logging.info("Removed group member %s %s", group_address, address)
        self._group_member_store[group_address].discard(address)

    def get_group_members(
        self, group_address: str, without_self: bool = True
    ) -> set[str]:
        members = set(self._group_member_store[group_address])
        if without_self:
            members.discard(self._own_address)
        return members

    def add_device(self, address: str, device: int) -> None:
        self._device_store[address].add(device)

    def remove_device(self, address: str, device: int) -> None:
        self._device_store[address].discard(device)
        self._storage.set_inactive(address, device)

    def get_devices(self, address: str, without_self: bool = False) -> set[int]:
        devices = set(self._device_store[address])
        if without_self:
            devices.discard(self.get_own_device())
        return devices

    def get_devices_for_enc(
        self, address: str, *, groupchat: bool
    ) -> set[tuple[str, int]]:
        devices_for_encryption: list[tuple[str, int]] = []

        if groupchat:
            devices_for_encryption = self._get_devices_for_group_encryption(address)
        else:
            devices_for_encryption = self._get_devices_for_encryption(address)

        if not devices_for_encryption:
            raise exceptions.NoDevicesFound

        devices_for_encryption += self._get_own_devices_for_encryption()
        return set(devices_for_encryption)

    def _get_devices_for_group_encryption(self, address: str) -> list[tuple[str, int]]:
        devices_for_encryption: list[tuple[str, int]] = []
        for address_ in self._group_member_store[address]:
            devices_for_encryption += self._get_devices_for_encryption(address_)
        return devices_for_encryption

    def _get_own_devices_for_encryption(self) -> list[tuple[str, int]]:
        devices_for_encryption: list[tuple[str, int]] = []
        own_devices = self.get_devices(self._own_address, without_self=True)
        for device in own_devices:
            if self._storage.is_trusted(self._own_address, device):
                devices_for_encryption.append((self._own_address, device))
        return devices_for_encryption

    def _get_devices_for_encryption(self, address: str) -> list[tuple[str, int]]:
        devices_for_encryption: list[tuple[str, int]] = []
        devices = self.get_devices(address)

        for device in devices:
            if self._storage.is_trusted(address, device):
                devices_for_encryption.append((address, device))
        return devices_for_encryption

    def get_own_device(self) -> int:
        return self._own_device_id

    def is_own_device_published(self) -> bool:
        return self.get_own_device() in self.get_devices(self._own_address)

    def destroy(self) -> None:
        self._unregister_signals()
