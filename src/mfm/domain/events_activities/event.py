"""Event aggregate root entry for CAP-005."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4

from mfm.domain.events_activities.schedule import Schedule
from mfm.domain.events_activities.venue import Venue


@dataclass(slots=True)
class Event:
    """Represents one planned event."""

    name: str
    venue: Venue
    schedule: Schedule
    status: str = "PLANNED"
    description: str | None = None
    event_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.name = str(self.name).strip()
        if not self.name:
            raise ValueError("event name cannot be empty")

        if self.description is not None:
            self.description = str(self.description).strip() or None

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("event status cannot be empty")

        if not isinstance(self.venue, Venue):
            raise ValueError("venue must be Venue")
        if not isinstance(self.schedule, Schedule):
            raise ValueError("schedule must be Schedule")

        if not isinstance(self.event_id, UUID):
            self.event_id = UUID(str(self.event_id))
