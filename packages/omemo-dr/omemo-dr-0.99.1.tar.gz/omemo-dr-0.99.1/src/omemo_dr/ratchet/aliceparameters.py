from __future__ import annotations

from ..ecc.ec import ECPublicKey
from ..ecc.eckeypair import ECKeyPair
from ..identitykey import IdentityKey
from ..identitykeypair import IdentityKeyPair


class AliceParameters:
    def __init__(
        self,
        our_identity_key: IdentityKeyPair,
        our_base_key: ECKeyPair,
        their_identity_key: IdentityKey,
        their_signed_pre_key: ECPublicKey,
        their_ratchet_key: ECPublicKey,
        their_one_time_pre_key: ECPublicKey | None,
    ) -> None:
        self.our_base_key = our_base_key
        self.our_identity_key = our_identity_key
        self.their_signed_pre_key = their_signed_pre_key
        self.their_ratchet_key = their_ratchet_key
        self.their_identity_key = their_identity_key
        self.their_one_time_pre_key = their_one_time_pre_key

    def get_our_identity_key(self) -> IdentityKeyPair:
        return self.our_identity_key

    def get_our_base_key(self) -> ECKeyPair:
        return self.our_base_key

    def get_their_identity_key(self) -> IdentityKey:
        return self.their_identity_key

    def get_their_signed_pre_key(self) -> ECPublicKey:
        return self.their_signed_pre_key

    def get_their_one_time_pre_key(self) -> ECPublicKey | None:
        return self.their_one_time_pre_key

    def get_their_ratchet_key(self) -> ECPublicKey:
        return self.their_ratchet_key
