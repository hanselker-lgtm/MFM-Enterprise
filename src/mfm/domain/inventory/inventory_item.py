"""InventoryItem aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.inventory.events import InventoryItemCreated
from mfm.domain.inventory.events import InventoryItemDeactivated
from mfm.domain.inventory.events import InventoryItemReactivated
from mfm.domain.inventory.events import StockAdjusted
from mfm.domain.inventory.events import StockIssued
from mfm.domain.inventory.events import StockReceived
from mfm.domain.inventory.exceptions import InsufficientStockError
from mfm.domain.inventory.exceptions import InvalidInventoryAdjustmentError
from mfm.domain.inventory.exceptions import InvalidInventoryItemError
from mfm.domain.inventory.exceptions import InvalidInventoryLifecycleError
from mfm.domain.inventory.exceptions import InvalidInventoryQuantityError
from mfm.domain.inventory.exceptions import InvalidInventoryReferenceError
from mfm.domain.inventory.identifiers import InventoryItemId
from mfm.domain.inventory.inventory_item_status import InventoryItemStatus
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement import StockMovement
from mfm.domain.inventory.stock_movement_type import StockMovementType
from mfm.domain.inventory.stock_position import StockPosition
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure


@dataclass(slots=True)
class InventoryItem(AggregateRoot):
    """Aggregate root for generic inventory item stock management."""

    item_reference: str
    name: str
    unit_of_measure: UnitOfMeasure
    id: InventoryItemId = field(default_factory=InventoryItemId.new)
    status: InventoryItemStatus = InventoryItemStatus.ACTIVE
    description: str | None = None
    minimum_stock_level: Decimal | str | int | None = None
    _positions: dict[str, StockPosition] = field(default_factory=dict, init=False, repr=False)
    _movements: list[StockMovement] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, InventoryItemId):
            self.id = InventoryItemId(self.id)

        self.item_reference = self._normalize_reference(self.item_reference)
        self.name = self._normalize_text(self.name, "name")

        if not isinstance(self.unit_of_measure, UnitOfMeasure):
            raise InvalidInventoryItemError("unit_of_measure must be UnitOfMeasure")

        if not isinstance(self.status, InventoryItemStatus):
            try:
                self.status = InventoryItemStatus(str(self.status).upper())
            except Exception as exc:
                raise InvalidInventoryLifecycleError("status is invalid") from exc

        self.description = self._normalize_optional_text(self.description, "description")

        if self.minimum_stock_level is not None:
            normalized_minimum = self.unit_of_measure.normalize_quantity(
                self.minimum_stock_level
            )
            if normalized_minimum < Decimal("0"):
                raise InvalidInventoryQuantityError(
                    "minimum_stock_level cannot be negative"
                )
            self.minimum_stock_level = normalized_minimum

        self.add_event(
            InventoryItemCreated(
                inventory_item_id=self.id.value,
                item_reference=self.item_reference,
            )
        )

    @property
    def positions(self) -> tuple[StockPosition, ...]:
        return tuple(
            self._positions[key]
            for key in sorted(self._positions)
        )

    @property
    def movements(self) -> tuple[StockMovement, ...]:
        return tuple(self._movements)

    @property
    def total_quantity(self) -> Decimal:
        total = sum((position.quantity for position in self._positions.values()), Decimal("0"))
        return self.unit_of_measure.normalize_quantity(total)

    @property
    def low_stock(self) -> bool:
        return self.minimum_stock_level is not None and self.total_quantity < self.minimum_stock_level

    def quantity_at(self, location: StockLocation) -> Decimal:
        position = self._positions.get(location.location_key)
        if position is None:
            return self.unit_of_measure.normalize_quantity(Decimal("0"))
        return position.quantity

    def receive_stock(
        self,
        *,
        location: StockLocation,
        quantity: Decimal | str | int,
        occurred_at: datetime,
        external_reference: str | None = None,
        note: str | None = None,
    ) -> StockMovement:
        self._require_active()
        validated_location = self._require_location(location)
        normalized_quantity = self._normalize_positive_quantity(quantity)
        normalized_occurred_at = self._normalize_aware_datetime(occurred_at, "occurred_at")

        position = self._positions.get(validated_location.location_key)
        if position is None:
            position = StockPosition(
                location=validated_location,
                quantity=self.unit_of_measure.normalize_quantity(Decimal("0")),
            )
            self._positions[validated_location.location_key] = position
        position.increase(normalized_quantity)

        movement = StockMovement(
            movement_type=StockMovementType.RECEIPT,
            quantity=normalized_quantity,
            location=validated_location,
            occurred_at=normalized_occurred_at,
            external_reference=self._normalize_optional_text(
                external_reference,
                "external_reference",
            ),
            note=self._normalize_optional_text(note, "note"),
        )
        self._movements.append(movement)
        self.add_event(
            StockReceived(
                inventory_item_id=self.id.value,
                stock_movement_id=movement.id.value,
                location_key=validated_location.location_key,
                quantity=normalized_quantity,
                occurred_at=normalized_occurred_at,
            )
        )
        return movement

    def issue_stock(
        self,
        *,
        location: StockLocation,
        quantity: Decimal | str | int,
        occurred_at: datetime,
        external_reference: str | None = None,
        note: str | None = None,
    ) -> StockMovement:
        self._require_active()
        validated_location = self._require_location(location)
        normalized_quantity = self._normalize_positive_quantity(quantity)
        normalized_occurred_at = self._normalize_aware_datetime(occurred_at, "occurred_at")

        position = self._positions.get(validated_location.location_key)
        if position is None or position.quantity < normalized_quantity:
            raise InsufficientStockError("insufficient stock at location")

        position.decrease(normalized_quantity)

        movement = StockMovement(
            movement_type=StockMovementType.ISSUE,
            quantity=normalized_quantity,
            location=validated_location,
            occurred_at=normalized_occurred_at,
            external_reference=self._normalize_optional_text(
                external_reference,
                "external_reference",
            ),
            note=self._normalize_optional_text(note, "note"),
        )
        self._movements.append(movement)
        self.add_event(
            StockIssued(
                inventory_item_id=self.id.value,
                stock_movement_id=movement.id.value,
                location_key=validated_location.location_key,
                quantity=normalized_quantity,
                occurred_at=normalized_occurred_at,
            )
        )
        return movement

    def adjust_stock_to_count(
        self,
        *,
        location: StockLocation,
        counted_quantity: Decimal | str | int,
        reason: str,
        occurred_at: datetime,
        note: str | None = None,
    ) -> StockMovement:
        self._require_active()
        validated_location = self._require_location(location)
        normalized_counted_quantity = self.unit_of_measure.normalize_quantity(counted_quantity)
        if normalized_counted_quantity < Decimal("0"):
            raise InvalidInventoryQuantityError("counted_quantity cannot be negative")
        normalized_reason = self._normalize_text(reason, "reason")
        normalized_occurred_at = self._normalize_aware_datetime(occurred_at, "occurred_at")

        current_quantity = self.quantity_at(validated_location)
        if normalized_counted_quantity == current_quantity:
            raise InvalidInventoryAdjustmentError(
                "counted_quantity must differ from current quantity"
            )

        delta = normalized_counted_quantity - current_quantity
        movement_type = (
            StockMovementType.ADJUSTMENT_INCREASE
            if delta > Decimal("0")
            else StockMovementType.ADJUSTMENT_DECREASE
        )
        movement_quantity = self.unit_of_measure.normalize_quantity(abs(delta))

        position = self._positions.get(validated_location.location_key)
        if position is None:
            position = StockPosition(
                location=validated_location,
                quantity=self.unit_of_measure.normalize_quantity(Decimal("0")),
            )
            self._positions[validated_location.location_key] = position
        position.set_quantity(normalized_counted_quantity)

        movement = StockMovement(
            movement_type=movement_type,
            quantity=movement_quantity,
            location=validated_location,
            occurred_at=normalized_occurred_at,
            note=self._normalize_optional_text(note, "note"),
            reason=normalized_reason,
        )
        self._movements.append(movement)
        self.add_event(
            StockAdjusted(
                inventory_item_id=self.id.value,
                stock_movement_id=movement.id.value,
                location_key=validated_location.location_key,
                quantity=movement_quantity,
                movement_type=movement_type.value,
                occurred_at=normalized_occurred_at,
            )
        )
        return movement

    def deactivate(self) -> None:
        if self.status is not InventoryItemStatus.ACTIVE:
            raise InvalidInventoryLifecycleError(
                "only active inventory item can be deactivated"
            )
        if self.total_quantity != self.unit_of_measure.normalize_quantity(Decimal("0")):
            raise InvalidInventoryLifecycleError(
                "inventory item with stock cannot be deactivated"
            )
        self.status = InventoryItemStatus.INACTIVE
        self.add_event(InventoryItemDeactivated(inventory_item_id=self.id.value))

    def reactivate(self) -> None:
        if self.status is not InventoryItemStatus.INACTIVE:
            raise InvalidInventoryLifecycleError(
                "only inactive inventory item can be reactivated"
            )
        self.status = InventoryItemStatus.ACTIVE
        self.add_event(InventoryItemReactivated(inventory_item_id=self.id.value))

    def explained_quantity_from_history(self) -> Decimal:
        total = Decimal("0")
        for movement in self._movements:
            if movement.movement_type in {
                StockMovementType.RECEIPT,
                StockMovementType.ADJUSTMENT_INCREASE,
            }:
                total += movement.quantity
            else:
                total -= movement.quantity
        return self.unit_of_measure.normalize_quantity(total)

    def _require_active(self) -> None:
        if self.status is not InventoryItemStatus.ACTIVE:
            raise InvalidInventoryLifecycleError(
                "inactive inventory item cannot change stock"
            )

    @staticmethod
    def _normalize_reference(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidInventoryReferenceError("item_reference must be string")
        normalized = value.strip()
        if not normalized:
            raise InvalidInventoryReferenceError(
                "item_reference must be a non-empty string"
            )
        if any(character in normalized for character in "\r\n\t"):
            raise InvalidInventoryReferenceError(
                "item_reference contains unsupported whitespace"
            )
        return normalized

    @staticmethod
    def _normalize_text(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise InvalidInventoryItemError(f"{field_name} must be string")
        normalized = value.strip()
        if not normalized:
            raise InvalidInventoryItemError(
                f"{field_name} must be a non-empty string"
            )
        return normalized

    @staticmethod
    def _normalize_optional_text(value: str | None, field_name: str) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise InvalidInventoryItemError(f"{field_name} must be string or None")
        normalized = value.strip()
        return normalized or None

    @staticmethod
    def _normalize_aware_datetime(value: datetime, field_name: str) -> datetime:
        if not isinstance(value, datetime):
            raise InvalidInventoryItemError(f"{field_name} must be datetime")
        if value.tzinfo is None or value.utcoffset() is None:
            raise InvalidInventoryItemError(
                f"{field_name} must be timezone-aware datetime"
            )
        return value.astimezone(UTC)

    def _normalize_positive_quantity(self, value: Decimal | str | int) -> Decimal:
        normalized = self.unit_of_measure.normalize_quantity(value)
        if normalized <= Decimal("0"):
            raise InvalidInventoryQuantityError("quantity must be positive")
        return normalized

    @staticmethod
    def _require_location(location: StockLocation) -> StockLocation:
        if not isinstance(location, StockLocation):
            raise InvalidInventoryItemError("location must be StockLocation")
        return location