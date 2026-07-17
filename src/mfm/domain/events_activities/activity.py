"""Activity entity within an event."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4

from mfm.domain.events_activities.schedule import Schedule


@dataclass(slots=True)
class Activity:
    """Represents one activity under an event."""

    event_id: UUID
    title: str
    schedule: Schedule
    status: str = "PLANNED"
    description: str | None = None
    activity_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.event_id, UUID):
            self.event_id = UUID(str(self.event_id))

        self.title = str(self.title).strip()
        if not self.title:
            raise ValueError("activity title cannot be empty")

        if self.description is not None:
            self.description = str(self.description).strip() or None

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("activity status cannot be empty")

        if not isinstance(self.schedule, Schedule):
            raise ValueError("schedule must be Schedule")

        if not isinstance(self.activity_id, UUID):
            self.activity_id = UUID(str(self.activity_id))
