"""Inventory stock location value object."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.common.value_object import ValueObject
from mfm.domain.inventory.exceptions import InvalidStockLocationError


@dataclass(frozen=True, slots=True)
class StockLocation(ValueObject):
    """Stable inventory-owned stock location with optional vessel reference."""

    location_key: str
    location_name: str
    vessel_id: UUID | None = None

    def __post_init__(self) -> None:
        for field_name in ("location_key", "location_name"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise InvalidStockLocationError(
                    f"{field_name} must be a non-empty string"
                )
            object.__setattr__(self, field_name, value.strip())

        if self.vessel_id is None:
            return

        if isinstance(self.vessel_id, str):
            try:
                object.__setattr__(self, "vessel_id", UUID(self.vessel_id))
            except Exception as exc:
                raise InvalidStockLocationError("vessel_id must be UUID") from exc
            return

        if not isinstance(self.vessel_id, UUID):
            raise InvalidStockLocationError("vessel_id must be UUID")