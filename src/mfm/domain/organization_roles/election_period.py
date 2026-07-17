"""Election period entity for organization roles capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class ElectionPeriod:
    """Election period for board/committee governance cycles."""

    name: str
    starts_on: date
    ends_on: date
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(self.starts_on, date):
            raise ValueError("starts_on must be date")
        if not isinstance(self.ends_on, date):
            raise ValueError("ends_on must be date")
        if self.ends_on < self.starts_on:
            raise ValueError("ends_on cannot be before starts_on")

        self.name = self.name.strip()

    def includes(self, at_date: date) -> bool:
        if not isinstance(at_date, date):
            raise ValueError("at_date must be date")
        return self.starts_on <= at_date <= self.ends_on
