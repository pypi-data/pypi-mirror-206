from __future__ import annotations

from .djbec import DjbECPrivateKey
from .ec import ECPublicKey


class ECKeyPair:
    def __init__(self, public_key: ECPublicKey, private_key: DjbECPrivateKey) -> None:
        self._public_key = public_key
        self._private_key = private_key

    def get_private_key(self) -> DjbECPrivateKey:
        return self._private_key

    def get_public_key(self) -> ECPublicKey:
        return self._public_key
