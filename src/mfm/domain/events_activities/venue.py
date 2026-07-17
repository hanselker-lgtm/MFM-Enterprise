"""Venue entity for events and activities."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Venue:
    """Physical venue where events and activities occur."""

    name: str
    address: str
    capacity: int
    venue_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.name = str(self.name).strip()
        if not self.name:
            raise ValueError("venue name cannot be empty")

        self.address = str(self.address).strip()
        if not self.address:
            raise ValueError("venue address cannot be empty")

        if not isinstance(self.capacity, int) or self.capacity <= 0:
            raise ValueError("venue capacity must be positive integer")

        if not isinstance(self.venue_id, UUID):
            self.venue_id = UUID(str(self.venue_id))
