"""Vessel dimensions value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.fleet.exceptions import InvalidVesselDimensionsError


@dataclass(frozen=True, slots=True)
class VesselDimensions(ValueObject):
    """Dimensions value object for vessels."""

    length: float
    beam: float
    draft: float

    def __post_init__(self) -> None:
        if self.length <= 0:
            raise InvalidVesselDimensionsError("length must be positive")
        if self.beam <= 0:
            raise InvalidVesselDimensionsError("beam must be positive")
        if self.draft <= 0:
            raise InvalidVesselDimensionsError("draft must be positive")
