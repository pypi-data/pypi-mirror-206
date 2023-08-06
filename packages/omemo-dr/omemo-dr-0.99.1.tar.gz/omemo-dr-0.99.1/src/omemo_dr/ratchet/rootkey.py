from __future__ import annotations

from ..ecc.curve import Curve
from ..ecc.djbec import CurvePublicKey
from ..ecc.eckeypair import ECKeyPair
from ..kdf.derivedrootsecrets import DerivedRootSecrets
from ..kdf.hkdf import HKDF
from .chainkey import ChainKey


class RootKey:
    def __init__(self, kdf: HKDF, key: bytes) -> None:
        self.kdf = kdf
        self.key = key

    def get_key_bytes(self) -> bytes:
        return self.key

    def create_chain(
        self,
        ec_public_key_their_ratchet_key: CurvePublicKey,
        ec_key_pair_our_ratchet_key: ECKeyPair,
    ) -> tuple[RootKey, ChainKey]:
        if self.kdf.session_version <= 3:
            domain_separator = "WhisperRatchet"
        else:
            domain_separator = "OMEMO Root Chain"

        shared_secret = Curve.calculate_agreement(
            ec_public_key_their_ratchet_key,
            ec_key_pair_our_ratchet_key.get_private_key(),
        )

        derived_secret_bytes = self.kdf.derive_secrets(
            shared_secret,
            domain_separator.encode(),
            DerivedRootSecrets.SIZE,
            salt=self.key,
        )

        derived_secrets = DerivedRootSecrets(derived_secret_bytes)
        new_root_key = RootKey(self.kdf, derived_secrets.get_root_key())
        new_chain_key = ChainKey(self.kdf, derived_secrets.get_chain_key(), 0)
        return (new_root_key, new_chain_key)
