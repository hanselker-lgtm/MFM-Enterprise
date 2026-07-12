"""Historical inventory stock movement entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal

from mfm.domain.inventory.exceptions import InvalidInventoryQuantityError
from mfm.domain.inventory.exceptions import InvalidStockMovementError
from mfm.domain.inventory.identifiers import StockMovementId
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement_type import StockMovementType


@dataclass(frozen=True, slots=True)
class StockMovement:
    """Append-only historical stock movement."""

    movement_type: StockMovementType
    quantity: Decimal
    location: StockLocation
    occurred_at: datetime
    id: StockMovementId = field(default_factory=StockMovementId.new)
    external_reference: str | None = None
    note: str | None = None
    reason: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, StockMovementId):
            object.__setattr__(self, "id", StockMovementId(self.id))

        if not isinstance(self.movement_type, StockMovementType):
            try:
                normalized_type = StockMovementType(str(self.movement_type).upper())
            except Exception as exc:
                raise InvalidStockMovementError("movement_type is invalid") from exc
            object.__setattr__(self, "movement_type", normalized_type)

        if not isinstance(self.quantity, Decimal):
            raise InvalidInventoryQuantityError("quantity must be Decimal")
        if self.quantity <= Decimal("0"):
            raise InvalidInventoryQuantityError("quantity must be positive")

        if not isinstance(self.location, StockLocation):
            raise InvalidStockMovementError("location must be StockLocation")

        if not isinstance(self.occurred_at, datetime):
            raise InvalidStockMovementError("occurred_at must be datetime")
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise InvalidStockMovementError("occurred_at must be timezone-aware datetime")
        object.__setattr__(self, "occurred_at", self.occurred_at.astimezone(UTC))

        for field_name in ("external_reference", "note", "reason"):
            value = getattr(self, field_name)
            if value is None:
                continue
            if not isinstance(value, str):
                raise InvalidStockMovementError(f"{field_name} must be string or None")
            object.__setattr__(self, field_name, value.strip() or None)