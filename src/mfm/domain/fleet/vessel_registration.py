"""Vessel registration value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.fleet.exceptions import InvalidVesselRegistrationError


@dataclass(frozen=True, slots=True)
class VesselRegistration(ValueObject):
    """Canonical vessel registration value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidVesselRegistrationError("registration must be a string")

        normalized = self.value.strip().upper()
        if not normalized:
            raise InvalidVesselRegistrationError("registration cannot be empty")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
