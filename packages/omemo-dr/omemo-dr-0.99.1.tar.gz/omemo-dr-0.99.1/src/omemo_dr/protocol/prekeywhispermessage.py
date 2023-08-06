from __future__ import annotations

from typing import cast

import google.protobuf.message
from google.protobuf.message import DecodeError

from ..ecc.curve import Curve
from ..ecc.ec import ECPublicKey
from ..exceptions import InvalidKeyException
from ..exceptions import InvalidMessageException
from ..exceptions import InvalidVersionException
from ..identitykey import IdentityKey
from ..util.byteutil import ByteUtil
from . import whisperprotos_pb2 as whisperprotos
from .ciphertextmessage import CiphertextMessage
from .whispermessage import WhisperMessage


class PreKeyWhisperMessage(CiphertextMessage):
    def __init__(
        self,
        serialized: bytes,
        message_version: int,
        registration_id: int,
        pre_key_id: int,
        signed_pre_key_id: int,
        ec_public_base_key: ECPublicKey,
        identity_key: IdentityKey,
        whisper_message: WhisperMessage,
    ) -> None:
        self._serialized = serialized
        self._message_version = message_version
        self._registration_id = registration_id
        self._pre_key_id = pre_key_id
        self._signed_pre_key_id = signed_pre_key_id
        self._ec_public_base_key = ec_public_base_key
        self._identity_key = identity_key
        self._whisper_message = whisper_message

    @classmethod
    def new(
        cls,
        message_version: int,
        registration_id: int,
        pre_key_id: int,
        signed_pre_key_id: int,
        ec_public_base_key: ECPublicKey,
        identity_key: IdentityKey,
        whisper_message: WhisperMessage,
    ) -> PreKeyWhisperMessage:
        prekey_message = cast(
            PreKeyWhisperMessageProto, whisperprotos.PreKeyWhisperMessage()
        )
        prekey_message.signedPreKeyId = signed_pre_key_id
        prekey_message.preKeyId = pre_key_id
        prekey_message.baseKey = ec_public_base_key.serialize()
        prekey_message.identityKey = identity_key.serialize()
        prekey_message.message = whisper_message.serialize()
        prekey_message.registrationId = registration_id

        version_bytes = ByteUtil.ints_to_byte_high_and_low(3, 3)
        message_bytes = prekey_message.SerializeToString()

        serialized = bytes(ByteUtil.combine(version_bytes, message_bytes))

        return cls(
            serialized,
            message_version,
            registration_id,
            pre_key_id,
            signed_pre_key_id,
            ec_public_base_key,
            identity_key,
            whisper_message,
        )

    @classmethod
    def from_bytes(cls, serialized: bytes) -> PreKeyWhisperMessage:
        try:
            version = ByteUtil.high_bits_to_int(serialized[0])
            if version != 3:
                raise InvalidVersionException("Unknown version %s" % version)

            pre_key_whisper_message = cast(
                PreKeyWhisperMessageProto, whisperprotos.PreKeyWhisperMessage()
            )
            pre_key_whisper_message.ParseFromString(serialized[1:])

            if (
                not pre_key_whisper_message.signedPreKeyId
                or not pre_key_whisper_message.baseKey
                or not pre_key_whisper_message.identityKey
                or not pre_key_whisper_message.message
            ):
                raise InvalidMessageException("Incomplete message")

            registration_id = pre_key_whisper_message.registrationId
            pre_key_id = pre_key_whisper_message.preKeyId
            signed_pre_key_id = pre_key_whisper_message.signedPreKeyId

            base_key = Curve.decode_point(bytearray(pre_key_whisper_message.baseKey), 0)

            identity_key = IdentityKey(
                Curve.decode_point(bytearray(pre_key_whisper_message.identityKey), 0)
            )
            message = WhisperMessage.from_bytes(pre_key_whisper_message.message)
        except (InvalidKeyException, DecodeError) as error:
            raise InvalidMessageException(str(error))

        return cls(
            serialized,
            version,
            registration_id,
            pre_key_id,
            signed_pre_key_id,
            base_key,
            identity_key,
            message,
        )

    def get_message_version(self) -> int:
        return self._message_version

    def get_identity_key(self) -> IdentityKey:
        return self._identity_key

    def get_registration_id(self) -> int:
        return self._registration_id

    def get_pre_key_id(self) -> int:
        return self._pre_key_id

    def get_signed_pre_key_id(self) -> int:
        return self._signed_pre_key_id

    def get_base_key(self) -> ECPublicKey:
        return self._ec_public_base_key

    def get_whisper_message(self) -> WhisperMessage:
        return self._whisper_message

    def serialize(self) -> bytes:
        return self._serialized

    def get_type(self) -> int:
        return CiphertextMessage.PREKEY_TYPE


class PreKeyWhisperMessageProto(google.protobuf.message.Message):
    signedPreKeyId: int
    preKeyId: int
    baseKey: bytes
    identityKey: bytes
    message: bytes
    registrationId: int
