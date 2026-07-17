"""Assignment entity for role assignments."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(slots=True)
class Assignment:
    """Assign a role to an assignee in a time period."""

    role_id: UUID
    assignee_id: UUID
    starts_on: date
    ends_on: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.role_id, UUID):
            raise ValueError("role_id must be UUID")
        if not isinstance(self.assignee_id, UUID):
            raise ValueError("assignee_id must be UUID")
        if not isinstance(self.starts_on, date):
            raise ValueError("starts_on must be date")
        if self.ends_on is not None and not isinstance(self.ends_on, date):
            raise ValueError("ends_on must be date or None")
        if self.ends_on is not None and self.ends_on < self.starts_on:
            raise ValueError("ends_on cannot be before starts_on")

    def overlaps(self, other: "Assignment") -> bool:
        left_end = self.ends_on
        right_end = other.ends_on

        if left_end is None and right_end is None:
            return True
        if left_end is None:
            return right_end >= self.starts_on
        if right_end is None:
            return left_end >= other.starts_on
        return self.starts_on <= right_end and left_end >= other.starts_on
