from __future__ import annotations

from typing import cast
from typing import Optional
from typing import Union

import google.protobuf.message

from ..ecc.curve import Curve
from ..ecc.djbec import CurvePublicKey
from ..ecc.ec import ECPublicKey
from ..ecc.eckeypair import ECKeyPair
from ..identitykeypair import IdentityKey
from ..identitykeypair import IdentityKeyPair
from ..kdf.hkdf import HKDF
from ..kdf.messagekeys import MessageKeys
from ..ratchet.chainkey import ChainKey
from ..ratchet.rootkey import RootKey
from . import storageprotos_pb2 as storageprotos


class SessionState:
    def __init__(
        self, session: Optional[Union[SessionState, SessionStructureProto]] = None
    ) -> None:
        if session is None:
            self.session_structure = cast(
                SessionStructureProto, storageprotos.SessionStructure()
            )

        elif isinstance(session, SessionState):
            self.session_structure = cast(
                SessionStructureProto, storageprotos.SessionStructure()
            )
            self.session_structure.CopyFrom(session.get_structure())

        else:
            self.session_structure = session

    def get_structure(self) -> SessionStructureProto:
        return self.session_structure

    def get_alice_base_key(self) -> bytes:
        return self.session_structure.aliceBaseKey

    def set_alice_base_key(self, alice_base_key: bytes) -> None:
        self.session_structure.aliceBaseKey = alice_base_key

    def set_session_version(self, version: int) -> None:
        self.session_structure.sessionVersion = version

    def get_session_version(self) -> int:
        session_version = self.session_structure.sessionVersion
        return 2 if session_version == 0 else session_version

    def set_remote_identity_key(self, identity_key: IdentityKey) -> None:
        self.session_structure.remoteIdentityPublic = identity_key.serialize()

    def set_local_identity_key(self, identity_key: IdentityKey) -> None:
        self.session_structure.localIdentityPublic = identity_key.serialize()

    def get_remote_identity_key(self) -> IdentityKey:
        assert self.session_structure.remoteIdentityPublic is not None
        return IdentityKey(self.session_structure.remoteIdentityPublic, 0)

    def get_local_identity_key(self) -> IdentityKey:
        return IdentityKey(self.session_structure.localIdentityPublic, 0)

    def get_previous_counter(self) -> int:
        return self.session_structure.previousCounter

    def set_previous_counter(self, previous_counter: int) -> None:
        self.session_structure.previousCounter = previous_counter

    def get_root_key(self) -> RootKey:
        return RootKey(HKDF(self.get_session_version()), self.session_structure.rootKey)

    def set_root_key(self, root_key: RootKey) -> None:
        self.session_structure.rootKey = root_key.get_key_bytes()

    def get_sender_ratchet_key(self) -> CurvePublicKey:
        key = Curve.decode_point(
            bytearray(self.session_structure.senderChain.senderRatchetKey), 0
        )
        assert isinstance(key, CurvePublicKey)
        return key

    def get_sender_ratchet_key_pair(self) -> ECKeyPair:
        public_key = self.get_sender_ratchet_key()
        private_key = Curve.decode_private_point(
            self.session_structure.senderChain.senderRatchetKeyPrivate
        )

        return ECKeyPair(public_key, private_key)

    def has_receiver_chain(
        self, ec_publick_key_sender_ephemeral: CurvePublicKey
    ) -> bool:
        return self.get_receiver_chain(ec_publick_key_sender_ephemeral) is not None

    def has_sender_chain(self) -> bool:
        return self.session_structure.HasField("senderChain")

    def get_receiver_chain(
        self, ec_publick_key_sender_ephemeral: CurvePublicKey
    ) -> Optional[tuple[ChainStructureProto, int]]:
        receiver_chains = self.session_structure.receiverChains
        index = 0
        for receiver_chain in receiver_chains:
            chain_sender_ratchet_key = Curve.decode_point(
                bytearray(receiver_chain.senderRatchetKey), 0
            )
            if chain_sender_ratchet_key == ec_publick_key_sender_ephemeral:
                return (receiver_chain, index)

            index += 1

    def get_receiver_chain_key(
        self, ec_public_key_sender_ephemeral: CurvePublicKey
    ) -> ChainKey:
        receiver_chain_and_index = self.get_receiver_chain(
            ec_public_key_sender_ephemeral
        )
        assert receiver_chain_and_index is not None
        receiver_chain = receiver_chain_and_index[0]
        assert receiver_chain is not None

        return ChainKey(
            HKDF(self.get_session_version()),
            receiver_chain.chainKey.key,
            receiver_chain.chainKey.index,
        )

    def add_receiver_chain(
        self, ec_publick_key_sender_ratchet_key: CurvePublicKey, chain_key: ChainKey
    ) -> None:
        sender_ratchet_key = ec_publick_key_sender_ratchet_key

        chain = cast(
            ChainStructureProto,
            storageprotos.SessionStructure.Chain(),  # pyright: ignore
        )
        chain.senderRatchetKey = sender_ratchet_key.serialize()
        chain.chainKey.key = chain_key.get_key()
        chain.chainKey.index = chain_key.get_index()

        self.session_structure.receiverChains.extend([chain])

        if len(self.session_structure.receiverChains) > 5:
            del self.session_structure.receiverChains[0]

    def set_sender_chain(
        self, ec_key_pair_sender_ratchet_key_pair: ECKeyPair, chain_key: ChainKey
    ) -> None:
        sender_ratchet_key_pair = ec_key_pair_sender_ratchet_key_pair

        self.session_structure.senderChain.senderRatchetKey = (
            sender_ratchet_key_pair.get_public_key().serialize()
        )
        self.session_structure.senderChain.senderRatchetKeyPrivate = (
            sender_ratchet_key_pair.get_private_key().serialize()
        )
        self.session_structure.senderChain.chainKey.key = chain_key.key
        self.session_structure.senderChain.chainKey.index = chain_key.index

    def get_sender_chain_key(self) -> ChainKey:
        chain_key_structure = self.session_structure.senderChain.chainKey
        return ChainKey(
            HKDF(self.get_session_version()),
            chain_key_structure.key,
            chain_key_structure.index,
        )

    def set_sender_chain_key(self, chain_key_next_chain_key: ChainKey) -> None:
        next_chain_key = chain_key_next_chain_key

        self.session_structure.senderChain.chainKey.key = next_chain_key.get_key()
        self.session_structure.senderChain.chainKey.index = next_chain_key.get_index()

    def has_message_keys(
        self, ec_publick_key_sender_ephemeral: CurvePublicKey, counter: int
    ) -> bool:
        sender_ephemeral = ec_publick_key_sender_ephemeral
        chain_and_index = self.get_receiver_chain(sender_ephemeral)
        assert chain_and_index is not None
        chain = chain_and_index[0]

        message_key_list = chain.messageKeys
        for message_key in message_key_list:
            if message_key.index == counter:
                return True

        return False

    def remove_message_keys(
        self, ec_public_key_sender_ephemeral: CurvePublicKey, counter: int
    ) -> MessageKeys:
        sender_ephemeral = ec_public_key_sender_ephemeral
        chain_and_index = self.get_receiver_chain(sender_ephemeral)
        assert chain_and_index is not None
        chain = chain_and_index[0]
        assert chain is not None

        message_key_list = chain.messageKeys
        result = None

        for i in range(0, len(message_key_list)):
            message_key = message_key_list[i]
            if message_key.index == counter:
                result = MessageKeys(
                    message_key.cipherKey,
                    message_key.macKey,
                    message_key.iv,
                    message_key.index,
                )
                del message_key_list[i]
                break

        assert result is not None

        self.session_structure.receiverChains[chain_and_index[1]].CopyFrom(chain)

        return result

    def set_message_keys(
        self, ec_public_key_sender_ephemeral: CurvePublicKey, message_keys: MessageKeys
    ) -> None:
        sender_ephemeral = ec_public_key_sender_ephemeral
        chain_and_index = self.get_receiver_chain(sender_ephemeral)
        assert chain_and_index is not None
        chain = chain_and_index[0]
        message_key_structure = chain.messageKeys.add()  # pyright: ignore
        message_key_structure.cipherKey = message_keys.get_cipher_key()
        message_key_structure.macKey = message_keys.get_mac_key()
        message_key_structure.index = message_keys.get_counter()
        message_key_structure.iv = message_keys.get_iv()

        self.session_structure.receiverChains[chain_and_index[1]].CopyFrom(chain)

    def set_receiver_chain_key(
        self, ec_public_key_sender_ephemeral: CurvePublicKey, chain_key: ChainKey
    ) -> None:
        sender_ephemeral = ec_public_key_sender_ephemeral
        chain_and_index = self.get_receiver_chain(sender_ephemeral)
        assert chain_and_index is not None
        chain = chain_and_index[0]
        chain.chainKey.key = chain_key.get_key()
        chain.chainKey.index = chain_key.get_index()

        self.session_structure.receiverChains[chain_and_index[1]].CopyFrom(chain)

    def set_pending_key_exchange(
        self,
        sequence: int,
        our_base_key: ECKeyPair,
        our_ratchet_key: ECKeyPair,
        our_identity_key: IdentityKeyPair,
    ) -> None:
        structure = cast(
            PendingKeyExchangeStructureProto,
            self.session_structure.pending_key_exchange(),  # pyright: ignore
        )
        structure.sequence = sequence
        structure.localBaseKey = our_base_key.get_public_key().serialize()
        structure.localBaseKeyPrivate = our_base_key.get_private_key().serialize()
        structure.localRatchetKey = our_ratchet_key.get_public_key().serialize()
        structure.localRatchetKeyPrivate = our_ratchet_key.get_private_key().serialize()
        structure.localIdentityKey = our_identity_key.get_public_key().serialize()
        structure.localIdentityKeyPrivate = (
            our_identity_key.get_private_key().serialize()
        )

        self.session_structure.pendingKeyExchange.MergeFrom(structure)

    def get_pending_key_exchange_sequence(self) -> int:
        return self.session_structure.pendingKeyExchange.sequence

    def get_pending_key_exchange_base_key(self) -> ECKeyPair:
        public_key = Curve.decode_point(
            bytearray(self.session_structure.pendingKeyExchange.localBaseKey), 0
        )
        private_key = Curve.decode_private_point(
            self.session_structure.pendingKeyExchange.localBaseKeyPrivate
        )
        return ECKeyPair(public_key, private_key)

    def get_pending_key_exchange_ratchet_key(self) -> ECKeyPair:
        public_key = Curve.decode_point(
            bytearray(self.session_structure.pendingKeyExchange.localRatchetKey), 0
        )
        private_key = Curve.decode_private_point(
            self.session_structure.pendingKeyExchange.localRatchetKeyPrivate
        )
        return ECKeyPair(public_key, private_key)

    def get_pending_key_exchange_identity_key(self) -> IdentityKeyPair:
        public_key = IdentityKey(
            bytearray(self.session_structure.pendingKeyExchange.localIdentityKey), 0
        )

        private_key = Curve.decode_private_point(
            self.session_structure.pendingKeyExchange.localIdentityKeyPrivate
        )
        return IdentityKeyPair.new(public_key, private_key)

    def has_pending_key_exchange(self) -> bool:
        return self.session_structure.HasField("pendingKeyExchange")

    def set_unacknowledged_pre_key_message(
        self, pre_key_id: int, signed_pre_key_id: int, base_key: CurvePublicKey
    ) -> None:
        self.session_structure.pendingPreKey.signedPreKeyId = signed_pre_key_id
        self.session_structure.pendingPreKey.baseKey = base_key.serialize()
        self.session_structure.pendingPreKey.preKeyId = pre_key_id

    def has_unacknowledged_pre_key_message(self) -> bool:
        return self.session_structure.HasField("pendingPreKey")

    def get_unacknowledged_pre_key_message_items(
        self,
    ) -> UnacknowledgedPreKeyMessageItems:
        pre_key_id = None
        if self.session_structure.pendingPreKey.HasField("preKeyId"):
            pre_key_id = self.session_structure.pendingPreKey.preKeyId

        assert pre_key_id is not None
        return SessionState.UnacknowledgedPreKeyMessageItems(
            pre_key_id,
            self.session_structure.pendingPreKey.signedPreKeyId,
            Curve.decode_point(
                bytearray(self.session_structure.pendingPreKey.baseKey), 0
            ),
        )

    def clear_unacknowledged_pre_key_message(self) -> None:
        self.session_structure.ClearField("pendingPreKey")

    def set_remote_registration_id(self, registration_id: int) -> None:
        self.session_structure.remoteRegistrationId = registration_id

    def get_remote_registration_id(self) -> int:
        return self.session_structure.remoteRegistrationId

    def set_local_registration_id(self, registration_id: int) -> None:
        self.session_structure.localRegistrationId = registration_id

    def get_local_registration_id(self) -> int:
        return self.session_structure.localRegistrationId

    def serialize(self) -> bytes:
        return self.session_structure.SerializeToString()

    class UnacknowledgedPreKeyMessageItems:
        def __init__(
            self, pre_key_id: int, signed_pre_key_id: int, base_key: ECPublicKey
        ) -> None:
            self.pre_key_id = pre_key_id
            self.signed_pre_key_id = signed_pre_key_id
            self.base_key = base_key

        def get_pre_key_id(self) -> int:
            return self.pre_key_id

        def get_signed_pre_key_id(self) -> int:
            return self.signed_pre_key_id

        def get_base_key(self) -> ECPublicKey:
            return self.base_key


class MessageKeyStructureProto(google.protobuf.message.Message):
    index: int
    cipherKey: bytes
    macKey: bytes
    iv: bytes


class ChainKeyStructureProto(google.protobuf.message.Message):
    index: int
    key: bytes


class ChainStructureProto(google.protobuf.message.Message):
    senderRatchetKey: bytes
    senderRatchetKeyPrivate: bytes
    chainKey: ChainKeyStructureProto
    messageKeys: list[MessageKeyStructureProto]


class PendingKeyExchangeStructureProto(google.protobuf.message.Message):
    sequence: int
    localBaseKey: bytes
    localBaseKeyPrivate: bytes
    localRatchetKey: bytes
    localRatchetKeyPrivate: bytes
    localIdentityKey: bytes
    localIdentityKeyPrivate: bytes


class PendingPreKeyStructureProto(google.protobuf.message.Message):
    preKeyId: int
    signedPreKeyId: int
    baseKey: bytes


class SessionStructureProto(google.protobuf.message.Message):
    sessionVersion: int
    localIdentityPublic: bytes
    remoteIdentityPublic: bytes
    rootKey: bytes
    previousCounter: int
    senderChain: ChainStructureProto
    receiverChains: list[ChainStructureProto]
    pendingKeyExchange: PendingKeyExchangeStructureProto
    pendingPreKey: PendingPreKeyStructureProto
    remoteRegistrationId: int
    localRegistrationId: int
    needsRefresh: bool
    aliceBaseKey: bytes
