from __future__ import annotations

from ..ecc.djbec import CurvePublicKey
from ..ecc.djbec import EdPublicKey
from ..ecc.ec import ECPublicKey
from ..identitykey import IdentityKey


class PreKeyBundle:
    def __init__(
        self,
        registration_id: int,
        device_id: int,
        pre_key_id: int,
        ec_public_key_pre_key_public: ECPublicKey,
        signed_pre_key_id: int,
        ec_public_key_signed_pre_key_public: ECPublicKey,
        signed_pre_key_signature: bytes,
        identity_key: IdentityKey,
    ) -> None:
        self.registration_id = registration_id
        self.device_id = device_id
        self.pre_key_id = pre_key_id
        self.pre_key_public = ec_public_key_pre_key_public
        self.signed_pre_key_id = signed_pre_key_id
        self.signed_pre_key_public = ec_public_key_signed_pre_key_public
        self.signed_pre_key_signature = signed_pre_key_signature
        self.identity_key = identity_key

    def get_device_id(self) -> int:
        return self.device_id

    def get_pre_key_id(self) -> int:
        return self.pre_key_id

    def get_pre_key(self) -> ECPublicKey:
        return self.pre_key_public

    def get_signed_pre_key_id(self) -> int:
        return self.signed_pre_key_id

    def get_signed_pre_key(self) -> ECPublicKey:
        return self.signed_pre_key_public

    def get_signed_pre_key_signature(self) -> bytes:
        return self.signed_pre_key_signature

    def get_identity_key(self) -> IdentityKey:
        return self.identity_key

    def get_registration_id(self) -> int:
        return self.registration_id

    def get_session_version(self) -> int:
        public_key = self.identity_key.get_public_key()
        if isinstance(public_key, CurvePublicKey):
            return 3

        elif isinstance(public_key, EdPublicKey):
            return 4

        else:
            breakpoint()
            raise AssertionError("Unknown session version")
