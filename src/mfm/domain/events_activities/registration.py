"""Registration entity for event participation."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Registration:
    """Represents a participant registration for an event."""

    event_id: UUID
    member_id: UUID
    registered_at: datetime
    status: str = "REGISTERED"
    registration_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.event_id, UUID):
            self.event_id = UUID(str(self.event_id))
        if not isinstance(self.member_id, UUID):
            self.member_id = UUID(str(self.member_id))

        if not isinstance(self.registered_at, datetime) or self.registered_at.tzinfo is None:
            raise ValueError("registered_at must be timezone-aware datetime")

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("registration status cannot be empty")

        if not isinstance(self.registration_id, UUID):
            self.registration_id = UUID(str(self.registration_id))
