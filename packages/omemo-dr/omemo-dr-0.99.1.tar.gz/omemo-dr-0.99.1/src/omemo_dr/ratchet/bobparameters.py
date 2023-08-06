from __future__ import annotations

from ..ecc.ec import ECPublicKey
from ..ecc.eckeypair import ECKeyPair
from ..identitykey import IdentityKey
from ..identitykeypair import IdentityKeyPair


class BobParameters:
    def __init__(
        self,
        our_identity_key: IdentityKeyPair,
        our_signed_pre_key: ECKeyPair,
        our_ratchet_key: ECKeyPair,
        our_one_time_pre_key: ECKeyPair | None,
        their_identity_key: IdentityKey,
        their_base_key: ECPublicKey,
    ) -> None:
        self.our_identity_key = our_identity_key
        self.our_signed_pre_key = our_signed_pre_key
        self.our_ratchet_key = our_ratchet_key
        self.our_one_time_pre_key = our_one_time_pre_key
        self.their_identity_key = their_identity_key
        self.their_base_key = their_base_key

    def get_our_identity_key(self) -> IdentityKeyPair:
        return self.our_identity_key

    def get_our_signed_pre_key(self) -> ECKeyPair:
        return self.our_signed_pre_key

    def get_our_one_time_pre_key(self) -> ECKeyPair | None:
        return self.our_one_time_pre_key

    def get_their_identity_key(self) -> IdentityKey:
        return self.their_identity_key

    def get_their_base_key(self) -> ECPublicKey:
        return self.their_base_key

    def get_our_ratchet_key(self) -> ECKeyPair:
        return self.our_ratchet_key
