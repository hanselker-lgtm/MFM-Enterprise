"""Purchase receipt records for procurement domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Mapping

from mfm.domain.procurement.exceptions import InvalidPurchaseReceiptError
from mfm.domain.procurement.identifiers import PurchaseOrderLineId
from mfm.domain.procurement.identifiers import PurchaseReceiptId


def _normalize_positive_quantity(value: Decimal | str | int, field_name: str) -> Decimal:
    if isinstance(value, bool) or isinstance(value, float):
        raise InvalidPurchaseReceiptError(f"{field_name} must not be float")
    try:
        decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
    except Exception as exc:
        raise InvalidPurchaseReceiptError(f"{field_name} must be a valid decimal") from exc
    if decimal_value <= Decimal("0"):
        raise InvalidPurchaseReceiptError(f"{field_name} must be greater than zero")
    return decimal_value


@dataclass(slots=True)
class PurchaseReceiptLine:
    """Quantity received for a single purchase order line."""

    purchase_order_line_id: PurchaseOrderLineId
    quantity: Decimal | str | int

    def __post_init__(self) -> None:
        if not isinstance(self.purchase_order_line_id, PurchaseOrderLineId):
            self.purchase_order_line_id = PurchaseOrderLineId(self.purchase_order_line_id)
        self.quantity = _normalize_positive_quantity(self.quantity, "quantity")

    def to_dict(self) -> dict[str, str]:
        return {
            "purchase_order_line_id": str(self.purchase_order_line_id.value),
            "quantity": str(self.quantity),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PurchaseReceiptLine":
        if not isinstance(data, Mapping):
            raise InvalidPurchaseReceiptError("data must be a mapping")
        return cls(
            purchase_order_line_id=PurchaseOrderLineId(data["purchase_order_line_id"]),
            quantity=data["quantity"],
        )


@dataclass(slots=True)
class PurchaseReceipt:
    """Immutable receipt history record."""

    receipt_reference: str
    received_at: datetime
    lines: list[PurchaseReceiptLine]
    id: PurchaseReceiptId = field(default_factory=PurchaseReceiptId.new)

    def __post_init__(self) -> None:
        if not isinstance(self.id, PurchaseReceiptId):
            self.id = PurchaseReceiptId(self.id)

        if not isinstance(self.receipt_reference, str) or not self.receipt_reference.strip():
            raise InvalidPurchaseReceiptError("receipt_reference must be a non-empty string")
        self.receipt_reference = self.receipt_reference.strip()

        if not isinstance(self.received_at, datetime):
            raise InvalidPurchaseReceiptError("received_at must be datetime")
        if self.received_at.tzinfo is None or self.received_at.utcoffset() is None:
            raise InvalidPurchaseReceiptError(
                "received_at must be timezone-aware datetime"
            )
        self.received_at = self.received_at.astimezone(UTC)

        if not isinstance(self.lines, list) or len(self.lines) == 0:
            raise InvalidPurchaseReceiptError("lines must be a non-empty list")
        self.lines = [line if isinstance(line, PurchaseReceiptLine) else PurchaseReceiptLine.from_dict(line) for line in self.lines]

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id.value),
            "receipt_reference": self.receipt_reference,
            "received_at": self.received_at.isoformat(),
            "lines": [line.to_dict() for line in self.lines],
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PurchaseReceipt":
        if not isinstance(data, Mapping):
            raise InvalidPurchaseReceiptError("data must be a mapping")
        return cls(
            id=PurchaseReceiptId(data["id"]),
            receipt_reference=str(data["receipt_reference"]),
            received_at=datetime.fromisoformat(str(data["received_at"])),
            lines=[PurchaseReceiptLine.from_dict(item) for item in data["lines"]],
        )
