"""Asset location value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.asset.exceptions import InvalidAssetLocationError


@dataclass(frozen=True, slots=True)
class AssetLocation(ValueObject):
    """Canonical location value object for an asset."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidAssetLocationError("location must be a string")

        normalized = self.value.strip()
        if not normalized:
            raise InvalidAssetLocationError("location cannot be empty")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
