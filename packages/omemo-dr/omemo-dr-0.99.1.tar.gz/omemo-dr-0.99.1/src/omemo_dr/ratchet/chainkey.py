from __future__ import annotations

import hashlib
import hmac

from ..kdf.derivedmessagesecrets import DerivedMessageSecrets
from ..kdf.hkdf import HKDF
from ..kdf.messagekeys import MessageKeys


class ChainKey:
    MESSAGE_KEY_SEED = bytearray([0x01])
    CHAIN_KEY_SEED = bytearray([0x02])

    def __init__(self, kdf: HKDF, key: bytes, index: int) -> None:
        self.kdf = kdf
        self.key = key
        self.index = index

    def get_key(self) -> bytes:
        return self.key

    def get_index(self) -> int:
        return self.index

    def get_next_chain_key(self) -> ChainKey:
        nextKey = self.get_base_material(self.__class__.CHAIN_KEY_SEED)
        return ChainKey(self.kdf, nextKey, self.index + 1)

    def get_message_keys(self) -> MessageKeys:
        if self.kdf.session_version <= 3:
            domain_separator = "WhisperMessageKeys"
        else:
            domain_separator = "OMEMO Message Key Material"

        input_key_material = self.get_base_material(self.__class__.MESSAGE_KEY_SEED)
        key_material_bytes = self.kdf.derive_secrets(
            input_key_material,
            bytearray(domain_separator.encode()),
            DerivedMessageSecrets.SIZE,
        )
        key_material = DerivedMessageSecrets(key_material_bytes)
        return MessageKeys(
            key_material.get_cipher_key(),
            key_material.get_mac_key(),
            key_material.get_iv(),
            self.index,
        )

    def get_base_material(self, seedBytes: bytes) -> bytes:
        mac = hmac.new(bytes(self.key), digestmod=hashlib.sha256)
        mac.update(bytes(seedBytes))
        return mac.digest()
