from __future__ import annotations

from typing import cast
from typing import Optional

import google.protobuf.message

from . import storageprotos_pb2 as storageprotos
from .sessionstate import SessionState
from .sessionstate import SessionStructureProto


class SessionRecord:
    ARCHIVED_STATES_MAX_LENGTH = 40

    def __init__(
        self,
        session_state: Optional[SessionState] = None,
        serialized: Optional[bytes] = None,
    ) -> None:
        self.previous_states: list[SessionState] = []
        if session_state:
            self.session_state = session_state
            self.fresh = False

        elif serialized:
            record = cast(RecordStructureProto, storageprotos.RecordStructure())
            record.ParseFromString(serialized)
            self.session_state = SessionState(record.currentSession)
            self.fresh = False
            for previous_structure in record.previousSessions:
                self.previous_states.append(SessionState(previous_structure))

        else:
            self.fresh = True
            self.session_state = SessionState()

    def has_session_state(self, version: int, alice_base_key: bytes) -> bool:
        if (
            self.session_state.get_session_version() == version
            and alice_base_key == self.session_state.get_alice_base_key()
        ):
            return True

        for state in self.previous_states:
            if (
                state.get_session_version() == version
                and alice_base_key == state.get_alice_base_key()
            ):
                return True

        return False

    def get_session_state(self) -> SessionState:
        return self.session_state

    def get_previous_session_states(self) -> list[SessionState]:
        return self.previous_states

    def is_fresh(self) -> bool:
        return self.fresh

    def archive_current_state(self) -> None:
        self.promote_state(SessionState())

    def promote_state(self, promoted_state: SessionState) -> None:
        self.previous_states.insert(0, self.session_state)
        self.session_state = promoted_state
        if len(self.previous_states) > self.__class__.ARCHIVED_STATES_MAX_LENGTH:
            self.previous_states.pop()

    def set_state(self, session_state: SessionState) -> None:
        self.session_state = session_state

    def serialize(self) -> bytes:
        previous_structures = [
            previous_state.get_structure() for previous_state in self.previous_states
        ]
        record = cast(RecordStructureProto, storageprotos.RecordStructure())
        record.currentSession.MergeFrom(self.session_state.get_structure())
        record.previousSessions.extend(previous_structures)

        return record.SerializeToString()


class RecordStructureProto(google.protobuf.message.Message):
    currentSession: SessionStructureProto
    previousSessions: list[SessionStructureProto]
