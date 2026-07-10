"""Volunteer availability value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.organization.exceptions import InvalidVolunteerAvailabilityError


@dataclass(frozen=True, slots=True)
class VolunteerAvailability(ValueObject):
    """Structured availability for scheduling volunteers."""

    is_available: bool
    max_hours_per_week: int
    preferred_days: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.is_available, bool):
            raise InvalidVolunteerAvailabilityError("is_available must be bool")

        if not isinstance(self.max_hours_per_week, int) or self.max_hours_per_week < 0:
            raise InvalidVolunteerAvailabilityError(
                "max_hours_per_week must be a non-negative integer"
            )

        if not isinstance(self.preferred_days, tuple):
            raise InvalidVolunteerAvailabilityError("preferred_days must be a tuple")

        normalized_days: list[str] = []
        for day in self.preferred_days:
            if not isinstance(day, str) or not day.strip():
                raise InvalidVolunteerAvailabilityError(
                    "preferred_days values must be non-empty strings"
                )
            normalized_days.append(day.strip().upper())

        deduplicated = tuple(dict.fromkeys(normalized_days))
        object.__setattr__(self, "preferred_days", deduplicated)
