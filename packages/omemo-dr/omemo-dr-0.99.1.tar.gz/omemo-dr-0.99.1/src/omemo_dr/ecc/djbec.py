from __future__ import annotations

from typing import Any

import binascii

from .. import curve
from ..util.byteutil import ByteUtil
from .ec import ECPrivateKey
from .ec import ECPublicKey

CURVE25519_KEY_LEN = 33
ED25519_KEY_LEN = 32
DJB_TYPE = 5


class DjbECPublicKey(ECPublicKey):
    def __init__(self, _bytes: bytes) -> None:
        self._public_key = _bytes

    def get_type(self) -> int:
        from .curve import Curve

        return Curve.DJB_TYPE

    def get_bytes(self) -> bytes:
        return self._public_key

    def get_public_key(self) -> bytes:
        return self._public_key

    def __eq__(self, other: Any) -> bool:
        return self._public_key == other.get_public_key()

    def __lt__(self, other: Any) -> bool:
        my_val = int(binascii.hexlify(self._public_key), 16)
        other_val = int(binascii.hexlify(other.get_public_key()), 16)

        return my_val < other_val

    def __cmp__(self, other: Any) -> int:
        my_val = int(binascii.hexlify(self._public_key), 16)
        other_val = int(binascii.hexlify(other.get_public_key()), 16)

        if my_val < other_val:
            return -1
        elif my_val == other_val:
            return 0
        else:
            return 1


class CurvePublicKey(DjbECPublicKey):
    def serialize(self) -> bytes:
        from .curve import Curve

        combined = ByteUtil.combine([Curve.DJB_TYPE], self._public_key)
        return bytes(combined)

    def to_ed(self) -> EdPublicKey:
        return EdPublicKey(curve.convert_curve_to_ed_pubkey(self._public_key))


class EdPublicKey(DjbECPublicKey):
    def to_curve(self) -> CurvePublicKey:
        return CurvePublicKey(curve.convert_ed_to_curve_pubkey(self._public_key))

    def serialize(self) -> bytes:
        return self._public_key


class DjbECPrivateKey(ECPrivateKey):
    def __init__(self, private_key: bytes) -> None:
        self._private_key = private_key

    def get_type(self) -> int:
        from .curve import Curve

        return Curve.DJB_TYPE

    def get_private_key(self) -> bytes:
        return self._private_key

    def serialize(self) -> bytes:
        return self._private_key

    def __eq__(self, other: Any) -> bool:
        return self._private_key == other.get_private_key()
