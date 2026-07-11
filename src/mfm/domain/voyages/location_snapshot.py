"""Historical location snapshot value object for voyages."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.voyages.exceptions import InvalidVoyageLocationError


@dataclass(frozen=True, slots=True)
class LocationSnapshot(ValueObject):
    """Historical location reference and readable snapshot."""

    name_snapshot: str
    location_external_id: str | None = None
    locality_snapshot: str | None = None
    country_snapshot: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name_snapshot, str) or not self.name_snapshot.strip():
            raise InvalidVoyageLocationError("name_snapshot must be a non-empty string")
        object.__setattr__(self, "name_snapshot", self.name_snapshot.strip())

        for field_name in (
            "location_external_id",
            "locality_snapshot",
            "country_snapshot",
        ):
            value = getattr(self, field_name)
            if value is None:
                continue
            if not isinstance(value, str):
                raise InvalidVoyageLocationError(
                    f"{field_name} must be string or None"
                )
            object.__setattr__(self, field_name, value.strip() or None)
