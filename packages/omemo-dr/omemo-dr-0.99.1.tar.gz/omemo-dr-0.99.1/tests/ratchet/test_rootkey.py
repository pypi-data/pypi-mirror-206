import unittest

from omemo_dr.ecc.curve import Curve
from omemo_dr.ecc.djbec import CurvePublicKey
from omemo_dr.ecc.eckeypair import ECKeyPair
from omemo_dr.kdf.hkdf import HKDF
from omemo_dr.ratchet.rootkey import RootKey


class RootKeyTest(unittest.TestCase):
    def test_root_key_derivation_v2(self):
        root_key_seed = bytearray(
            [
                0x7B,
                0xA6,
                0xDE,
                0xBC,
                0x2B,
                0xC1,
                0xBB,
                0xF9,
                0x1A,
                0xBB,
                0xC1,
                0x36,
                0x74,
                0x04,
                0x17,
                0x6C,
                0xA6,
                0x23,
                0x09,
                0x5B,
                0x7E,
                0xC6,
                0x6B,
                0x45,
                0xF6,
                0x02,
                0xD9,
                0x35,
                0x38,
                0x94,
                0x2D,
                0xCC,
            ]
        )

        alice_public = bytearray(
            [
                0x05,
                0xEE,
                0x4F,
                0xA6,
                0xCD,
                0xC0,
                0x30,
                0xDF,
                0x49,
                0xEC,
                0xD0,
                0xBA,
                0x6C,
                0xFC,
                0xFF,
                0xB2,
                0x33,
                0xD3,
                0x65,
                0xA2,
                0x7F,
                0xAD,
                0xBE,
                0xFF,
                0x77,
                0xE9,
                0x63,
                0xFC,
                0xB1,
                0x62,
                0x22,
                0xE1,
                0x3A,
            ]
        )

        alice_private = bytearray(
            [
                0x21,
                0x68,
                0x22,
                0xEC,
                0x67,
                0xEB,
                0x38,
                0x04,
                0x9E,
                0xBA,
                0xE7,
                0xB9,
                0x39,
                0xBA,
                0xEA,
                0xEB,
                0xB1,
                0x51,
                0xBB,
                0xB3,
                0x2D,
                0xB8,
                0x0F,
                0xD3,
                0x89,
                0x24,
                0x5A,
                0xC3,
                0x7A,
                0x94,
                0x8E,
                0x50,
            ]
        )

        bob_public = bytearray(
            [
                0x05,
                0xAB,
                0xB8,
                0xEB,
                0x29,
                0xCC,
                0x80,
                0xB4,
                0x71,
                0x09,
                0xA2,
                0x26,
                0x5A,
                0xBE,
                0x97,
                0x98,
                0x48,
                0x54,
                0x06,
                0xE3,
                0x2D,
                0xA2,
                0x68,
                0x93,
                0x4A,
                0x95,
                0x55,
                0xE8,
                0x47,
                0x57,
                0x70,
                0x8A,
                0x30,
            ]
        )

        next_root = bytearray(
            [
                0xB1,
                0x14,
                0xF5,
                0xDE,
                0x28,
                0x01,
                0x19,
                0x85,
                0xE6,
                0xEB,
                0xA2,
                0x5D,
                0x50,
                0xE7,
                0xEC,
                0x41,
                0xA9,
                0xB0,
                0x2F,
                0x56,
                0x93,
                0xC5,
                0xC7,
                0x88,
                0xA6,
                0x3A,
                0x06,
                0xD2,
                0x12,
                0xA2,
                0xF7,
                0x31,
            ]
        )

        next_chain = bytearray(
            [
                0x9D,
                0x7D,
                0x24,
                0x69,
                0xBC,
                0x9A,
                0xE5,
                0x3E,
                0xE9,
                0x80,
                0x5A,
                0xA3,
                0x26,
                0x4D,
                0x24,
                0x99,
                0xA3,
                0xAC,
                0xE8,
                0x0F,
                0x4C,
                0xCA,
                0xE2,
                0xDA,
                0x13,
                0x43,
                0x0C,
                0x5C,
                0x55,
                0xB5,
                0xCA,
                0x5F,
            ]
        )

        alice_public_key = Curve.decode_point(alice_public, 0)
        assert isinstance(alice_public_key, CurvePublicKey)

        alice_private_key = Curve.decode_private_point(alice_private)
        alice_key_pair = ECKeyPair(alice_public_key, alice_private_key)
        bob_public_key = Curve.decode_point(bob_public, 0)
        assert isinstance(bob_public_key, CurvePublicKey)

        root_key = RootKey(HKDF(2), root_key_seed)
        root_key_chain_key_pair = root_key.create_chain(bob_public_key, alice_key_pair)

        next_root_key = root_key_chain_key_pair[0]
        next_chain_key = root_key_chain_key_pair[1]

        self.assertEqual(root_key.get_key_bytes(), root_key_seed)
        self.assertEqual(next_root_key.get_key_bytes(), next_root)
        self.assertEqual(next_chain_key.get_key(), next_chain)
