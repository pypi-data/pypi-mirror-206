from __future__ import annotations

from typing import cast

import google.protobuf.message

from ..ecc.curve import Curve
from ..ecc.eckeypair import ECKeyPair
from .storageprotos_pb2 import PreKeyRecordStructure


class PreKeyRecord:
    def __init__(self, structure: PreKeyRecordStructureProto) -> None:
        self._structure = structure

    @classmethod
    def new(
        cls,
        _id: int,
        ec_key_pair: ECKeyPair,
    ) -> PreKeyRecord:
        structure = cast(PreKeyRecordStructureProto, PreKeyRecordStructure())
        structure.id = _id
        structure.publicKey = ec_key_pair.get_public_key().serialize()
        structure.privateKey = ec_key_pair.get_private_key().serialize()
        return cls(structure)

    @classmethod
    def from_bytes(cls, serialized: bytes) -> PreKeyRecord:
        record = cast(PreKeyRecordStructureProto, PreKeyRecordStructure())
        record.ParseFromString(serialized)
        return cls(record)

    def get_id(self) -> int:
        return self._structure.id

    def get_key_pair(self):
        public_key = Curve.decode_point(bytearray(self._structure.publicKey), 0)
        private_key = Curve.decode_private_point(bytearray(self._structure.privateKey))
        return ECKeyPair(public_key, private_key)

    def serialize(self) -> bytes:
        return self._structure.SerializeToString()


class PreKeyRecordStructureProto(google.protobuf.message.Message):
    id: int
    publicKey: bytes
    privateKey: bytes
