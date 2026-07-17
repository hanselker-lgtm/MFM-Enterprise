"""Communication preference entity for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from uuid import UUID
from uuid import uuid4


class PreferenceFrequency(str, Enum):
    """Delivery frequency for non-urgent communication."""

    IMMEDIATE = "IMMEDIATE"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


@dataclass(slots=True)
class CommunicationPreference:
    """Preference profile for a contact."""

    preferred_method_id: UUID
    allow_marketing: bool = False
    frequency: PreferenceFrequency = PreferenceFrequency.IMMEDIATE
    quiet_hours: tuple[int, int] | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.preferred_method_id, UUID):
            raise ValueError("preferred_method_id must be UUID")
        if not isinstance(self.allow_marketing, bool):
            raise ValueError("allow_marketing must be bool")
        if not isinstance(self.frequency, PreferenceFrequency):
            self.frequency = PreferenceFrequency(str(self.frequency).upper())

        if self.quiet_hours is not None:
            if len(self.quiet_hours) != 2:
                raise ValueError("quiet_hours must have start and end")
            start, end = self.quiet_hours
            if not isinstance(start, int) or not isinstance(end, int):
                raise ValueError("quiet_hours values must be integers")
            if not (0 <= start <= 23 and 0 <= end <= 23):
                raise ValueError("quiet_hours values must be in range 0-23")
