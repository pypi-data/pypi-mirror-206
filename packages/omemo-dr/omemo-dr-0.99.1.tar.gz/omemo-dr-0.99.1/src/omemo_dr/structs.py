from __future__ import annotations

from typing import TypedDict

import random
from dataclasses import dataclass


@dataclass
class OMEMOConfig:
    default_prekey_amount: int
    min_prekey_amount: int
    spk_archive_seconds: int
    spk_cycle_seconds: int
    unacknowledged_count: int


class PreKey(TypedDict):
    key: bytes
    id: int


@dataclass
class OMEMOBundle:
    spk: PreKey
    spk_signature: bytes
    ik: bytes
    otpks: list[PreKey]

    def pick_prekey(self) -> PreKey:
        return random.SystemRandom().choice(self.otpks)


@dataclass
class OMEMOMessage:
    sid: int
    iv: bytes
    keys: dict[int, tuple[bytes, bool]]
    payload: bytes | None
