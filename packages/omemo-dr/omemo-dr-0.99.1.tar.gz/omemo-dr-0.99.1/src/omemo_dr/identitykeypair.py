from __future__ import annotations

from typing import cast

import google.protobuf.message

from .ecc.curve import Curve
from .ecc.djbec import DjbECPrivateKey
from .identitykey import IdentityKey
from .state.storageprotos_pb2 import IdentityKeyPairStructure


class IdentityKeyPair:
    def __init__(self, structure: IdentityKeyPairStructureProto) -> None:
        self._structure = structure

    @classmethod
    def new(
        cls,
        identity_key_public_key: IdentityKey,
        ec_private_key: DjbECPrivateKey,
    ) -> IdentityKeyPair:
        structure = cast(IdentityKeyPairStructureProto, IdentityKeyPairStructure())

        structure.publicKey = identity_key_public_key.serialize()
        structure.privateKey = ec_private_key.serialize()

        return cls(structure)

    @classmethod
    def from_bytes(cls, serialized: bytes) -> IdentityKeyPair:
        structure = cast(IdentityKeyPairStructureProto, IdentityKeyPairStructure())
        structure.ParseFromString(serialized)
        return cls(structure)

    def get_public_key(self) -> IdentityKey:
        return IdentityKey(bytearray(self._structure.publicKey), offset=0)

    def get_private_key(self) -> DjbECPrivateKey:
        return Curve.decode_private_point(bytearray(self._structure.privateKey))

    def serialize(self) -> bytes:
        return self._structure.SerializeToString()


class IdentityKeyPairStructureProto(google.protobuf.message.Message):
    publicKey: bytes
    privateKey: bytes
