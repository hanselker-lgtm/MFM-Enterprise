"""Asset number value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.asset.exceptions import InvalidAssetNumberError


@dataclass(frozen=True, slots=True)
class AssetNumber(ValueObject):
    """Canonical asset number value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidAssetNumberError("asset_number must be a string")

        normalized = self.value.strip().upper()
        if not normalized:
            raise InvalidAssetNumberError("asset_number cannot be empty")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
