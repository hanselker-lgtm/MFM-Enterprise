"""Purchase order line entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Mapping

from mfm.domain.finance.money import Money
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderLineError
from mfm.domain.procurement.identifiers import PurchaseOrderLineId


def _normalize_quantity(value: Decimal | str | int, field_name: str) -> Decimal:
    if isinstance(value, bool) or isinstance(value, float):
        raise InvalidPurchaseOrderLineError(f"{field_name} must not be float")
    try:
        decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
    except Exception as exc:
        raise InvalidPurchaseOrderLineError(f"{field_name} must be a valid decimal") from exc
    if decimal_value <= Decimal("0"):
        raise InvalidPurchaseOrderLineError(f"{field_name} must be greater than zero")
    return decimal_value


def _normalize_optional_text(value: str | None, field_name: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise InvalidPurchaseOrderLineError(f"{field_name} must be string or None")
    normalized = value.strip()
    return normalized or None


@dataclass(slots=True)
class PurchaseOrderLine:
    """Line commitment on a purchase order."""

    description_snapshot: str
    quantity: Decimal | str | int
    unit_price: Money
    id: PurchaseOrderLineId = field(default_factory=PurchaseOrderLineId.new)
    inventory_item_reference: str | None = None
    expected_delivery_at: datetime | None = None
    line_note: str | None = None
    received_quantity: Decimal | str | int = Decimal("0")

    def __post_init__(self) -> None:
        if not isinstance(self.id, PurchaseOrderLineId):
            self.id = PurchaseOrderLineId(self.id)

        if not isinstance(self.description_snapshot, str) or not self.description_snapshot.strip():
            raise InvalidPurchaseOrderLineError(
                "description_snapshot must be a non-empty string"
            )
        self.description_snapshot = self.description_snapshot.strip()

        self.quantity = _normalize_quantity(self.quantity, "quantity")

        if not isinstance(self.unit_price, Money):
            raise InvalidPurchaseOrderLineError("unit_price must be Money")

        self.inventory_item_reference = _normalize_optional_text(
            self.inventory_item_reference,
            "inventory_item_reference",
        )
        self.line_note = _normalize_optional_text(self.line_note, "line_note")

        if self.expected_delivery_at is not None:
            if not isinstance(self.expected_delivery_at, datetime):
                raise InvalidPurchaseOrderLineError(
                    "expected_delivery_at must be datetime or None"
                )
            if self.expected_delivery_at.tzinfo is None or self.expected_delivery_at.utcoffset() is None:
                raise InvalidPurchaseOrderLineError(
                    "expected_delivery_at must be timezone-aware datetime"
                )
            self.expected_delivery_at = self.expected_delivery_at.astimezone(UTC)

        self.received_quantity = _normalize_quantity(
            self.received_quantity,
            "received_quantity",
        ) if self.received_quantity != Decimal("0") else Decimal("0")

        if self.received_quantity > self.quantity:
            raise InvalidPurchaseOrderLineError(
                "received_quantity cannot exceed committed quantity"
            )

    @property
    def line_total(self) -> Money:
        return self.unit_price * self.quantity

    @property
    def outstanding_quantity(self) -> Decimal:
        return self.quantity - self.received_quantity

    def record_received_quantity(self, quantity: Decimal | str | int) -> None:
        received = _normalize_quantity(quantity, "quantity")
        if self.received_quantity + received > self.quantity:
            raise InvalidPurchaseOrderLineError(
                "received quantity cannot exceed committed quantity"
            )
        self.received_quantity = self.received_quantity + received

    def amend(
        self,
        *,
        description_snapshot: str | None = None,
        quantity: Decimal | str | int | None = None,
        unit_price: Money | None = None,
        inventory_item_reference: str | None = None,
        expected_delivery_at: datetime | None = None,
        line_note: str | None = None,
    ) -> None:
        if description_snapshot is not None:
            if not isinstance(description_snapshot, str) or not description_snapshot.strip():
                raise InvalidPurchaseOrderLineError(
                    "description_snapshot must be a non-empty string"
                )
            self.description_snapshot = description_snapshot.strip()

        if quantity is not None:
            normalized_quantity = _normalize_quantity(quantity, "quantity")
            if normalized_quantity < self.received_quantity:
                raise InvalidPurchaseOrderLineError(
                    "quantity cannot be less than received_quantity"
                )
            self.quantity = normalized_quantity

        if unit_price is not None:
            if not isinstance(unit_price, Money):
                raise InvalidPurchaseOrderLineError("unit_price must be Money")
            self.unit_price = unit_price

        if inventory_item_reference is not None:
            self.inventory_item_reference = _normalize_optional_text(
                inventory_item_reference,
                "inventory_item_reference",
            )

        if expected_delivery_at is not None:
            if not isinstance(expected_delivery_at, datetime):
                raise InvalidPurchaseOrderLineError(
                    "expected_delivery_at must be datetime or None"
                )
            if expected_delivery_at.tzinfo is None or expected_delivery_at.utcoffset() is None:
                raise InvalidPurchaseOrderLineError(
                    "expected_delivery_at must be timezone-aware datetime"
                )
            self.expected_delivery_at = expected_delivery_at.astimezone(UTC)

        if line_note is not None:
            self.line_note = _normalize_optional_text(line_note, "line_note")

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id.value),
            "description_snapshot": self.description_snapshot,
            "quantity": str(self.quantity),
            "unit_price": self.unit_price.to_dict(),
            "inventory_item_reference": self.inventory_item_reference,
            "expected_delivery_at": (
                self.expected_delivery_at.isoformat() if self.expected_delivery_at is not None else None
            ),
            "line_note": self.line_note,
            "received_quantity": str(self.received_quantity),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PurchaseOrderLine":
        if not isinstance(data, Mapping):
            raise InvalidPurchaseOrderLineError("data must be a mapping")
        return cls(
            id=PurchaseOrderLineId(data["id"]),
            description_snapshot=str(data["description_snapshot"]),
            quantity=data["quantity"],
            unit_price=Money.from_dict(data["unit_price"]),
            inventory_item_reference=data.get("inventory_item_reference"),
            expected_delivery_at=(
                datetime.fromisoformat(str(data["expected_delivery_at"]))
                if data.get("expected_delivery_at") is not None
                else None
            ),
            line_note=data.get("line_note"),
            received_quantity=data.get("received_quantity", Decimal("0")),
        )
