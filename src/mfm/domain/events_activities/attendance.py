"""Attendance entity for activities."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Attendance:
    """Represents one attendance record."""

    event_id: UUID
    activity_id: UUID
    member_id: UUID
    attended_at: datetime
    present: bool = True
    attendance_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.event_id, UUID):
            self.event_id = UUID(str(self.event_id))
        if not isinstance(self.activity_id, UUID):
            self.activity_id = UUID(str(self.activity_id))
        if not isinstance(self.member_id, UUID):
            self.member_id = UUID(str(self.member_id))

        if not isinstance(self.attended_at, datetime) or self.attended_at.tzinfo is None:
            raise ValueError("attended_at must be timezone-aware datetime")

        if not isinstance(self.present, bool):
            raise ValueError("present must be bool")

        if not isinstance(self.attendance_id, UUID):
            self.attendance_id = UUID(str(self.attendance_id))
