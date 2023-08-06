from enum import IntEnum


class OMEMOTrust(IntEnum):
    UNTRUSTED = 0
    VERIFIED = 1
    UNDECIDED = 2
    BLIND = 3
