"""Purchase order aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Mapping

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
from mfm.domain.procurement.events import PurchaseOrderAmended
from mfm.domain.procurement.events import PurchaseOrderApproved
from mfm.domain.procurement.events import PurchaseOrderCancelled
from mfm.domain.procurement.events import PurchaseOrderCreated
from mfm.domain.procurement.events import PurchaseOrderOrdered
from mfm.domain.procurement.events import PurchaseOrderSubmitted
from mfm.domain.procurement.events import PurchaseReceiptRecorded
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderError
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderLifecycleError
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderLineError
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderReferenceError
from mfm.domain.procurement.exceptions import InvalidPurchaseReceiptError
from mfm.domain.procurement.exceptions import PurchaseOrderSerializationError
from mfm.domain.procurement.identifiers import PurchaseOrderId
from mfm.domain.procurement.identifiers import PurchaseOrderLineId
from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import PurchaseReceiptId
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.domain.procurement.purchase_receipt import PurchaseReceipt
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine


def _normalize_text(value: str | None, field_name: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise InvalidPurchaseOrderError(f"{field_name} must be string or None")
    normalized = value.strip()
    return normalized or None


def _normalize_datetime(value: datetime, field_name: str) -> datetime:
    if not isinstance(value, datetime):
        raise InvalidPurchaseOrderReferenceError(f"{field_name} must be datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise InvalidPurchaseOrderReferenceError(
            f"{field_name} must be timezone-aware datetime"
        )
    return value.astimezone(UTC)


def _normalize_optional_datetime(value: datetime | None, field_name: str) -> datetime | None:
    if value is None:
        return None
    return _normalize_datetime(value, field_name)


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
class PurchaseOrder(AggregateRoot):
    """Aggregate root for purchasing lifecycle and receipt history."""

    purchase_order_number: PurchaseOrderNumber | str
    supplier_reference: SupplierReference | str
    currency: Currency | str
    created_at: datetime
    id: PurchaseOrderId = field(default_factory=PurchaseOrderId.new)
    status: PurchaseOrderStatus = PurchaseOrderStatus.DRAFT
    lines: list[PurchaseOrderLine] = field(default_factory=list)
    supplier_name_snapshot: str | None = None
    supplier_contact_snapshot: str | None = None
    notes: str | None = None
    requested_by_reference: str | None = None
    approved_by_reference: str | None = None
    approved_at: datetime | None = None
    ordered_at: datetime | None = None
    external_order_reference: str | None = None
    cancelled_at: datetime | None = None
    cancellation_reason: str | None = None
    receipts: list[PurchaseReceipt] = field(default_factory=list)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, PurchaseOrderId):
            self.id = PurchaseOrderId(self.id)

        if not isinstance(self.purchase_order_number, PurchaseOrderNumber):
            self.purchase_order_number = PurchaseOrderNumber(str(self.purchase_order_number))

        if not isinstance(self.supplier_reference, SupplierReference):
            self.supplier_reference = SupplierReference(str(self.supplier_reference))

        if not isinstance(self.currency, Currency):
            self.currency = Currency(str(self.currency).upper())

        self.created_at = _normalize_datetime(self.created_at, "created_at")

        if not isinstance(self.status, PurchaseOrderStatus):
            self.status = PurchaseOrderStatus(str(self.status).upper())

        self.supplier_name_snapshot = _normalize_text(
            self.supplier_name_snapshot,
            "supplier_name_snapshot",
        )
        self.supplier_contact_snapshot = _normalize_text(
            self.supplier_contact_snapshot,
            "supplier_contact_snapshot",
        )
        self.notes = _normalize_text(self.notes, "notes")
        self.requested_by_reference = _normalize_text(
            self.requested_by_reference,
            "requested_by_reference",
        )
        self.approved_by_reference = _normalize_text(
            self.approved_by_reference,
            "approved_by_reference",
        )
        self.external_order_reference = _normalize_text(
            self.external_order_reference,
            "external_order_reference",
        )
        self.cancellation_reason = _normalize_text(
            self.cancellation_reason,
            "cancellation_reason",
        )

        self.approved_at = _normalize_optional_datetime(self.approved_at, "approved_at")
        self.ordered_at = _normalize_optional_datetime(self.ordered_at, "ordered_at")
        self.cancelled_at = _normalize_optional_datetime(self.cancelled_at, "cancelled_at")

        if not isinstance(self.lines, list):
            raise InvalidPurchaseOrderError("lines must be a list")
        if not isinstance(self.receipts, list):
            raise InvalidPurchaseOrderError("receipts must be a list")

        self.lines = [line if isinstance(line, PurchaseOrderLine) else PurchaseOrderLine.from_dict(line) for line in self.lines]
        self.receipts = [receipt if isinstance(receipt, PurchaseReceipt) else PurchaseReceipt.from_dict(receipt) for receipt in self.receipts]

        self._validate_unique_line_ids()
        self._validate_currency_alignment()
        self._validate_receipt_history()
        self._validate_status_invariants()

        self.add_event(
            PurchaseOrderCreated(
                purchase_order_id=self.id.value,
                purchase_order_number=self.purchase_order_number.value,
            )
        )

    def _validate_unique_line_ids(self) -> None:
        seen: set[Any] = set()
        for line in self.lines:
            if line.id.value in seen:
                raise InvalidPurchaseOrderError("duplicate purchase order line id")
            seen.add(line.id.value)

    def _validate_currency_alignment(self) -> None:
        for line in self.lines:
            if line.unit_price.currency != self.currency:
                raise InvalidPurchaseOrderError(
                    "all purchase order lines must match purchase order currency"
                )

    def _line_by_id(self, line_id: PurchaseOrderLineId) -> PurchaseOrderLine:
        identifier = line_id if isinstance(line_id, PurchaseOrderLineId) else PurchaseOrderLineId(line_id)
        for line in self.lines:
            if line.id == identifier:
                return line
        raise InvalidPurchaseOrderError("purchase order line not found")

    def _assert_draft(self) -> None:
        if self.status is not PurchaseOrderStatus.DRAFT:
            raise InvalidPurchaseOrderLifecycleError(
                "only draft purchase order can be amended"
            )

    def _assert_submitted(self) -> None:
        if self.status is not PurchaseOrderStatus.SUBMITTED:
            raise InvalidPurchaseOrderLifecycleError(
                "only submitted purchase order can be approved"
            )

    def _assert_approved(self) -> None:
        if self.status is not PurchaseOrderStatus.APPROVED:
            raise InvalidPurchaseOrderLifecycleError(
                "only approved purchase order can be placed"
            )

    def _assert_receivable(self) -> None:
        if self.status not in {
            PurchaseOrderStatus.ORDERED,
            PurchaseOrderStatus.PARTIALLY_RECEIVED,
        }:
            raise InvalidPurchaseOrderLifecycleError(
                "only ordered or partially received purchase order can record receipts"
            )

    def _assert_cancellable(self) -> None:
        if self.status in {PurchaseOrderStatus.RECEIVED, PurchaseOrderStatus.CANCELLED}:
            raise InvalidPurchaseOrderLifecycleError(
                "received or cancelled purchase order cannot be cancelled"
            )

    def _validate_receipt_history(self) -> None:
        received_by_line: dict[PurchaseOrderLineId, Decimal] = {
            line.id: Decimal("0") for line in self.lines
        }
        for receipt in self.receipts:
            for receipt_line in receipt.lines:
                if receipt_line.purchase_order_line_id not in received_by_line:
                    raise InvalidPurchaseReceiptError("receipt references unknown line")
                received_by_line[receipt_line.purchase_order_line_id] += receipt_line.quantity

        for line in self.lines:
            if received_by_line[line.id] != line.received_quantity:
                raise InvalidPurchaseOrderError(
                    "line received quantity must match receipt history"
                )
            if line.received_quantity > line.quantity:
                raise InvalidPurchaseOrderError(
                    "line received quantity cannot exceed committed quantity"
                )

    def _validate_status_invariants(self) -> None:
        if self.status is PurchaseOrderStatus.DRAFT:
            if any(
                value is not None
                for value in (
                    self.approved_at,
                    self.ordered_at,
                    self.cancelled_at,
                    self.external_order_reference,
                    self.approved_by_reference,
                )
            ):
                raise InvalidPurchaseOrderLifecycleError(
                    "draft purchase order cannot have approval, ordering, or cancellation state"
                )
            if self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "draft purchase order cannot have receipt history"
                )
            return

        if self.status is PurchaseOrderStatus.SUBMITTED:
            if self.approved_at is not None or self.ordered_at is not None:
                raise InvalidPurchaseOrderLifecycleError(
                    "submitted purchase order cannot have approval or ordering state"
                )
            if self.cancelled_at is not None:
                raise InvalidPurchaseOrderLifecycleError(
                    "submitted purchase order cannot have cancellation state"
                )
            if self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "submitted purchase order cannot have receipt history"
                )
            return

        if self.status is PurchaseOrderStatus.APPROVED:
            if self.approved_at is None or self.approved_by_reference is None:
                raise InvalidPurchaseOrderLifecycleError(
                    "approved purchase order requires approval fact"
                )
            if self.ordered_at is not None or self.cancelled_at is not None:
                raise InvalidPurchaseOrderLifecycleError(
                    "approved purchase order cannot have ordering or cancellation state"
                )
            if self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "approved purchase order cannot have receipt history"
                )
            return

        if self.status is PurchaseOrderStatus.ORDERED:
            if self.approved_at is None or self.approved_by_reference is None or self.ordered_at is None:
                raise InvalidPurchaseOrderLifecycleError(
                    "ordered purchase order requires approval and ordering facts"
                )
            if self.cancelled_at is not None:
                raise InvalidPurchaseOrderLifecycleError(
                    "ordered purchase order cannot have cancellation state"
                )
            if any(line.received_quantity != Decimal("0") for line in self.lines):
                raise InvalidPurchaseOrderLifecycleError(
                    "ordered purchase order cannot have received quantities"
                )
            if self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "ordered purchase order cannot have receipt history"
                )
            return

        if self.status is PurchaseOrderStatus.PARTIALLY_RECEIVED:
            if self.approved_at is None or self.approved_by_reference is None or self.ordered_at is None:
                raise InvalidPurchaseOrderLifecycleError(
                    "partially received purchase order requires approval and ordering facts"
                )
            if not self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "partially received purchase order requires receipt history"
                )
            if all(line.received_quantity == Decimal("0") for line in self.lines):
                raise InvalidPurchaseOrderLifecycleError(
                    "partially received purchase order requires received quantities"
                )
            if all(line.outstanding_quantity == Decimal("0") for line in self.lines):
                raise InvalidPurchaseOrderLifecycleError(
                    "partially received purchase order cannot be fully received"
                )
            return

        if self.status is PurchaseOrderStatus.RECEIVED:
            if self.approved_at is None or self.approved_by_reference is None or self.ordered_at is None:
                raise InvalidPurchaseOrderLifecycleError(
                    "received purchase order requires approval and ordering facts"
                )
            if not self.receipts:
                raise InvalidPurchaseOrderLifecycleError(
                    "received purchase order requires receipt history"
                )
            if any(line.outstanding_quantity != Decimal("0") for line in self.lines):
                raise InvalidPurchaseOrderLifecycleError(
                    "received purchase order must be fully received"
                )
            return

        if self.status is PurchaseOrderStatus.CANCELLED:
            if self.cancelled_at is None:
                raise InvalidPurchaseOrderLifecycleError(
                    "cancelled purchase order requires cancelled_at"
                )
            return

        raise InvalidPurchaseOrderLifecycleError("purchase order status is invalid")

    @property
    def order_total(self) -> Money:
        total = Money(amount=Decimal("0"), currency=self.currency)
        for line in self.lines:
            total = total + line.line_total
        return total

    @property
    def received_total(self) -> Money:
        total = Money(amount=Decimal("0"), currency=self.currency)
        for line in self.lines:
            received_line_total = line.unit_price * line.received_quantity
            total = total + received_line_total
        return total

    def add_line(self, line: PurchaseOrderLine) -> None:
        self._assert_draft()
        if not isinstance(line, PurchaseOrderLine):
            raise InvalidPurchaseOrderLineError("line must be PurchaseOrderLine")
        if line.unit_price.currency != self.currency:
            raise InvalidPurchaseOrderLineError(
                "line currency must match purchase order currency"
            )
        if any(existing.id == line.id for existing in self.lines):
            raise InvalidPurchaseOrderLineError("purchase order line id already exists")

        self.lines.append(line)
        self.add_event(
            PurchaseOrderAmended(
                purchase_order_id=self.id.value,
                purchase_order_line_id=line.id.value,
                amendment_kind="LINE_ADDED",
            )
        )

    def update_line(
        self,
        line_id: PurchaseOrderLineId,
        **changes: Any,
    ) -> None:
        self._assert_draft()
        line = self._line_by_id(line_id)

        if "unit_price" in changes:
            unit_price = changes["unit_price"]
            if not isinstance(unit_price, Money):
                raise InvalidPurchaseOrderLineError("unit_price must be Money")
            if unit_price.currency != self.currency:
                raise InvalidPurchaseOrderLineError(
                    "line currency must match purchase order currency"
                )

        line.amend(**changes)
        self.add_event(
            PurchaseOrderAmended(
                purchase_order_id=self.id.value,
                purchase_order_line_id=line.id.value,
                amendment_kind="LINE_UPDATED",
            )
        )

    def remove_line(self, line_id: PurchaseOrderLineId) -> None:
        self._assert_draft()
        identifier = line_id if isinstance(line_id, PurchaseOrderLineId) else PurchaseOrderLineId(line_id)
        for index, line in enumerate(self.lines):
            if line.id == identifier:
                del self.lines[index]
                self.add_event(
                    PurchaseOrderAmended(
                        purchase_order_id=self.id.value,
                        purchase_order_line_id=line.id.value,
                        amendment_kind="LINE_REMOVED",
                    )
                )
                return
        raise InvalidPurchaseOrderLineError("purchase order line not found")

    def amend_draft(
        self,
        *,
        supplier_reference: SupplierReference | str | None = None,
        supplier_name_snapshot: str | None = None,
        supplier_contact_snapshot: str | None = None,
        notes: str | None = None,
        requested_by_reference: str | None = None,
    ) -> None:
        self._assert_draft()
        if supplier_reference is not None:
            self.supplier_reference = (
                supplier_reference
                if isinstance(supplier_reference, SupplierReference)
                else SupplierReference(str(supplier_reference))
            )
        if supplier_name_snapshot is not None:
            self.supplier_name_snapshot = _normalize_text(
                supplier_name_snapshot,
                "supplier_name_snapshot",
            )
        if supplier_contact_snapshot is not None:
            self.supplier_contact_snapshot = _normalize_text(
                supplier_contact_snapshot,
                "supplier_contact_snapshot",
            )
        if notes is not None:
            self.notes = _normalize_text(notes, "notes")
        if requested_by_reference is not None:
            self.requested_by_reference = _normalize_text(
                requested_by_reference,
                "requested_by_reference",
            )
        self.add_event(
            PurchaseOrderAmended(
                purchase_order_id=self.id.value,
                amendment_kind="HEADER_AMENDED",
            )
        )

    def submit(self, *, submitted_at: datetime) -> None:
        self._assert_draft()
        if len(self.lines) == 0:
            raise InvalidPurchaseOrderLifecycleError(
                "draft purchase order must have at least one line before submission"
            )
        submitted_at = _normalize_datetime(submitted_at, "submitted_at")
        self.status = PurchaseOrderStatus.SUBMITTED
        self.add_event(
            PurchaseOrderSubmitted(
                purchase_order_id=self.id.value,
                submitted_at=submitted_at,
            )
        )

    def approve(self, *, approved_at: datetime, approved_by_reference: str) -> None:
        self._assert_submitted()
        approved_by_reference = _normalize_text(approved_by_reference, "approved_by_reference")
        approved_at = _normalize_datetime(approved_at, "approved_at")
        self.status = PurchaseOrderStatus.APPROVED
        self.approved_at = approved_at
        self.approved_by_reference = approved_by_reference
        self.add_event(
            PurchaseOrderApproved(
                purchase_order_id=self.id.value,
                approved_at=approved_at,
                approved_by_reference=approved_by_reference,
            )
        )

    def place(self, *, ordered_at: datetime, external_order_reference: str | None = None) -> None:
        self._assert_approved()
        ordered_at = _normalize_datetime(ordered_at, "ordered_at")
        self.status = PurchaseOrderStatus.ORDERED
        self.ordered_at = ordered_at
        if external_order_reference is not None:
            self.external_order_reference = _normalize_text(
                external_order_reference,
                "external_order_reference",
            )
        self.add_event(
            PurchaseOrderOrdered(
                purchase_order_id=self.id.value,
                ordered_at=ordered_at,
                external_order_reference=self.external_order_reference,
            )
        )

    def record_receipt(
        self,
        *,
        receipt_reference: str,
        received_at: datetime,
        lines: list[PurchaseReceiptLine],
    ) -> PurchaseReceipt:
        self._assert_receivable()
        receipt_reference = _normalize_text(receipt_reference, "receipt_reference")
        received_at = _normalize_datetime(received_at, "received_at")

        if not isinstance(lines, list) or len(lines) == 0:
            raise InvalidPurchaseReceiptError("lines must be a non-empty list")

        receipt_lines: list[PurchaseReceiptLine] = []
        for item in lines:
            receipt_line = item if isinstance(item, PurchaseReceiptLine) else PurchaseReceiptLine.from_dict(item)
            line = self._line_by_id(receipt_line.purchase_order_line_id)
            if receipt_line.quantity > line.outstanding_quantity:
                raise InvalidPurchaseReceiptError(
                    "receipt quantity cannot exceed outstanding quantity"
                )
            receipt_lines.append(receipt_line)

        for receipt_line in receipt_lines:
            self._line_by_id(receipt_line.purchase_order_line_id).record_received_quantity(
                receipt_line.quantity
            )

        receipt = PurchaseReceipt(
            id=PurchaseReceiptId.new(),
            receipt_reference=receipt_reference,
            received_at=received_at,
            lines=receipt_lines,
        )
        self.receipts.append(receipt)

        if all(line.outstanding_quantity == Decimal("0") for line in self.lines):
            self.status = PurchaseOrderStatus.RECEIVED
        else:
            self.status = PurchaseOrderStatus.PARTIALLY_RECEIVED

        self.add_event(
            PurchaseReceiptRecorded(
                purchase_order_id=self.id.value,
                purchase_receipt_id=receipt.id.value,
                received_at=received_at,
            )
        )
        return receipt

    def cancel(
        self,
        *,
        cancelled_at: datetime,
        cancelled_by_reference: str | None = None,
        cancellation_reason: str | None = None,
    ) -> None:
        self._assert_cancellable()
        cancelled_at = _normalize_datetime(cancelled_at, "cancelled_at")
        self.status = PurchaseOrderStatus.CANCELLED
        self.cancelled_at = cancelled_at
        self.cancelled_by_reference = _normalize_text(cancelled_by_reference, "cancelled_by_reference")
        self.cancellation_reason = _normalize_text(cancellation_reason, "cancellation_reason")
        self.add_event(
            PurchaseOrderCancelled(
                purchase_order_id=self.id.value,
                cancelled_at=cancelled_at,
                cancelled_by_reference=self.cancelled_by_reference,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id.value),
            "purchase_order_number": self.purchase_order_number.value,
            "supplier_reference": self.supplier_reference.value,
            "status": self.status.value,
            "currency": self.currency.value,
            "created_at": self.created_at.isoformat(),
            "lines": [line.to_dict() for line in self.lines],
            "supplier_name_snapshot": self.supplier_name_snapshot,
            "supplier_contact_snapshot": self.supplier_contact_snapshot,
            "notes": self.notes,
            "requested_by_reference": self.requested_by_reference,
            "approved_by_reference": self.approved_by_reference,
            "approved_at": self.approved_at.isoformat() if self.approved_at is not None else None,
            "ordered_at": self.ordered_at.isoformat() if self.ordered_at is not None else None,
            "external_order_reference": self.external_order_reference,
            "cancelled_at": self.cancelled_at.isoformat() if self.cancelled_at is not None else None,
            "cancellation_reason": self.cancellation_reason,
            "receipts": [receipt.to_dict() for receipt in self.receipts],
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PurchaseOrder":
        if not isinstance(data, Mapping):
            raise PurchaseOrderSerializationError("data must be a mapping")

        required = {
            "id",
            "purchase_order_number",
            "supplier_reference",
            "status",
            "currency",
            "created_at",
            "lines",
            "supplier_name_snapshot",
            "supplier_contact_snapshot",
            "notes",
            "requested_by_reference",
            "approved_by_reference",
            "approved_at",
            "ordered_at",
            "external_order_reference",
            "cancelled_at",
            "cancellation_reason",
            "receipts",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise PurchaseOrderSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            lines_payload = data["lines"]
            receipts_payload = data["receipts"]
            if not isinstance(lines_payload, list) or not isinstance(receipts_payload, list):
                raise PurchaseOrderSerializationError("lines and receipts must be lists")

            order = cls(
                id=PurchaseOrderId(data["id"]),
                purchase_order_number=PurchaseOrderNumber(str(data["purchase_order_number"])),
                supplier_reference=SupplierReference(str(data["supplier_reference"])),
                status=PurchaseOrderStatus(str(data["status"]).upper()),
                currency=Currency(str(data["currency"]).upper()),
                created_at=datetime.fromisoformat(str(data["created_at"])),
                lines=[PurchaseOrderLine.from_dict(item) for item in lines_payload],
                supplier_name_snapshot=data["supplier_name_snapshot"],
                supplier_contact_snapshot=data["supplier_contact_snapshot"],
                notes=data["notes"],
                requested_by_reference=data["requested_by_reference"],
                approved_by_reference=data["approved_by_reference"],
                approved_at=(
                    datetime.fromisoformat(str(data["approved_at"]))
                    if data.get("approved_at") is not None
                    else None
                ),
                ordered_at=(
                    datetime.fromisoformat(str(data["ordered_at"]))
                    if data.get("ordered_at") is not None
                    else None
                ),
                external_order_reference=data["external_order_reference"],
                cancelled_at=(
                    datetime.fromisoformat(str(data["cancelled_at"]))
                    if data.get("cancelled_at") is not None
                    else None
                ),
                cancellation_reason=data["cancellation_reason"],
                receipts=[PurchaseReceipt.from_dict(item) for item in receipts_payload],
            )
            order.pull_events()
            return order
        except PurchaseOrderSerializationError:
            raise
        except Exception as exc:
            raise PurchaseOrderSerializationError("Invalid serialized purchase order") from exc
