from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

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
from mfm.domain.procurement.exceptions import InvalidSupplierReferenceError
from mfm.domain.procurement.identifiers import PurchaseOrderId
from mfm.domain.procurement.identifiers import PurchaseOrderLineId
from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import PurchaseReceiptId
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine


def _utc_dt(year: int, month: int, day: int, hour: int = 8) -> datetime:
    return datetime(year, month, day, hour, tzinfo=UTC)


def _money(amount: str | int, currency: Currency = Currency.DKK) -> Money:
    return Money(amount=Decimal(str(amount)), currency=currency)


def _line(
    *,
    description: str = "Marine paint",
    quantity: str | int = "5",
    unit_price: Money | None = None,
    inventory_item_reference: str | None = "INV-PAINT-001",
) -> PurchaseOrderLine:
    return PurchaseOrderLine(
        description_snapshot=description,
        quantity=quantity,
        unit_price=unit_price or _money("10.00"),
        inventory_item_reference=inventory_item_reference,
    )


def _order(*, lines: list[PurchaseOrderLine] | None = None) -> PurchaseOrder:
    return PurchaseOrder(
        id=PurchaseOrderId.new(),
        purchase_order_number=PurchaseOrderNumber("PO-1001"),
        supplier_reference=SupplierReference("SUP-42"),
        currency=Currency.DKK,
        created_at=_utc_dt(2026, 7, 15),
        supplier_name_snapshot="Maritime Supplies A/S",
        supplier_contact_snapshot="contact@supplies.example",
        notes="Initial procurement order",
        requested_by_reference="ORG-1",
        lines=lines or [],
    )


def test_reference_value_objects_validate_and_are_immutable() -> None:
    order_id = PurchaseOrderId.new()
    line_id = PurchaseOrderLineId.new()
    receipt_id = PurchaseReceiptId.new()
    order_number = PurchaseOrderNumber(" PO-1001 ")
    supplier_reference = SupplierReference(" SUP-42 ")

    assert isinstance(order_id.value, UUID)
    assert isinstance(line_id.value, UUID)
    assert isinstance(receipt_id.value, UUID)
    assert order_number.value == "PO-1001"
    assert supplier_reference.value == "SUP-42"

    with pytest.raises(FrozenInstanceError):
        order_number.value = "PO-1002"  # type: ignore[misc]


@pytest.mark.parametrize(
    "factory, expected",
    [
        (lambda: PurchaseOrderNumber(" "), InvalidPurchaseOrderReferenceError),
        (lambda: SupplierReference(" "), InvalidSupplierReferenceError),
    ],
)
def test_reference_value_objects_reject_blank_values(factory, expected) -> None:
    with pytest.raises(expected):
        factory()


def test_purchase_order_creation_emits_created_event_and_starts_draft() -> None:
    order = _order()
    events = order.pull_events()

    assert order.status is PurchaseOrderStatus.DRAFT
    assert order.order_total == _money(0)
    assert any(isinstance(event, PurchaseOrderCreated) for event in events)


def test_purchase_order_line_validation_and_totals() -> None:
    line = _line(quantity="3", unit_price=_money("12.50"))

    assert line.line_total == _money("37.50")
    assert line.outstanding_quantity == Decimal("3")

    with pytest.raises(InvalidPurchaseOrderLineError):
        _line(quantity=0)


def test_currency_mismatch_is_rejected_on_line_addition() -> None:
    order = _order()
    order.pull_events()
    line = _line(unit_price=_money("10.00", Currency.EUR))

    with pytest.raises(InvalidPurchaseOrderLineError):
        order.add_line(line)


def test_draft_amendments_add_update_remove_lines_emit_events() -> None:
    order = _order()
    order.pull_events()
    first = _line(description="Paint A", quantity=2)

    order.add_line(first)
    order.update_line(first.id, quantity=3, line_note="Updated note")
    order.remove_line(first.id)
    events = order.pull_events()

    assert order.lines == []
    assert any(isinstance(event, PurchaseOrderAmended) for event in events)
    assert order.order_total == _money(0)


def test_valid_lifecycle_transitions_emit_events() -> None:
    order = _order(lines=[_line()])
    order.pull_events()

    order.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    order.approve(approved_at=_utc_dt(2026, 7, 15, 10), approved_by_reference="ORG-APPROVER")
    order.place(ordered_at=_utc_dt(2026, 7, 15, 11), external_order_reference="EXT-PO-77")
    events = order.pull_events()

    assert order.status is PurchaseOrderStatus.ORDERED
    assert order.approved_by_reference == "ORG-APPROVER"
    assert order.external_order_reference == "EXT-PO-77"
    assert any(isinstance(event, PurchaseOrderSubmitted) for event in events)
    assert any(isinstance(event, PurchaseOrderApproved) for event in events)
    assert any(isinstance(event, PurchaseOrderOrdered) for event in events)


def test_forbidden_lifecycle_transitions_are_rejected() -> None:
    draft_order = _order(lines=[_line()])
    draft_order.pull_events()

    with pytest.raises(InvalidPurchaseOrderLifecycleError):
        draft_order.approve(
            approved_at=_utc_dt(2026, 7, 15, 10),
            approved_by_reference="APPROVER",
        )

    submitted_order = _order(lines=[_line()])
    submitted_order.pull_events()
    submitted_order.submit(submitted_at=_utc_dt(2026, 7, 15, 9))

    with pytest.raises(InvalidPurchaseOrderLifecycleError):
        submitted_order.place(ordered_at=_utc_dt(2026, 7, 15, 11))


def test_receipt_recording_updates_status_and_preserves_history() -> None:
    order = _order(lines=[_line(quantity=5), _line(description="Filter", quantity=2, unit_price=_money("15.00"))])
    order.pull_events()
    order.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    order.approve(approved_at=_utc_dt(2026, 7, 15, 10), approved_by_reference="APPROVER")
    order.place(ordered_at=_utc_dt(2026, 7, 15, 11), external_order_reference="EXT-1")
    order.pull_events()

    receipt_one = order.record_receipt(
        receipt_reference="RCPT-1",
        received_at=_utc_dt(2026, 7, 16, 8),
        lines=[PurchaseReceiptLine(order.lines[0].id, 2)],
    )
    receipt_two = order.record_receipt(
        receipt_reference="RCPT-2",
        received_at=_utc_dt(2026, 7, 17, 8),
        lines=[
            PurchaseReceiptLine(order.lines[0].id, 3),
            PurchaseReceiptLine(order.lines[1].id, 2),
        ],
    )
    events = order.pull_events()

    assert receipt_one.id != receipt_two.id
    assert order.status is PurchaseOrderStatus.RECEIVED
    assert order.lines[0].received_quantity == Decimal("5")
    assert order.lines[1].received_quantity == Decimal("2")
    assert len(order.receipts) == 2
    assert any(isinstance(event, PurchaseReceiptRecorded) for event in events)


def test_receipt_cannot_exceed_outstanding_quantity() -> None:
    order = _order(lines=[_line(quantity=3)])
    order.pull_events()
    order.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    order.approve(approved_at=_utc_dt(2026, 7, 15, 10), approved_by_reference="APPROVER")
    order.place(ordered_at=_utc_dt(2026, 7, 15, 11))

    with pytest.raises(InvalidPurchaseReceiptError):
        order.record_receipt(
            receipt_reference="RCPT-OVER",
            received_at=_utc_dt(2026, 7, 16, 8),
            lines=[PurchaseReceiptLine(order.lines[0].id, 4)],
        )


def test_cancel_is_allowed_before_received_and_rejected_after_received() -> None:
    cancellable = _order(lines=[_line()])
    cancellable.pull_events()
    cancellable.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    cancellable.pull_events()
    cancellable.cancel(
        cancelled_at=_utc_dt(2026, 7, 15, 12),
        cancelled_by_reference="ORG-ADMIN",
        cancellation_reason="Scope changed",
    )
    cancel_events = cancellable.pull_events()

    assert cancellable.status is PurchaseOrderStatus.CANCELLED
    assert any(isinstance(event, PurchaseOrderCancelled) for event in cancel_events)

    received = _order(lines=[_line()])
    received.pull_events()
    received.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    received.approve(approved_at=_utc_dt(2026, 7, 15, 10), approved_by_reference="APPROVER")
    received.place(ordered_at=_utc_dt(2026, 7, 15, 11))
    received.record_receipt(
        receipt_reference="RCPT-FULL",
        received_at=_utc_dt(2026, 7, 16, 8),
        lines=[PurchaseReceiptLine(received.lines[0].id, 5)],
    )

    with pytest.raises(InvalidPurchaseOrderLifecycleError):
        received.cancel(cancelled_at=_utc_dt(2026, 7, 16, 12))


def test_restoration_reconstructs_state_and_emits_no_false_events() -> None:
    order = _order(lines=[_line(quantity=4), _line(description="Filter", quantity=2, unit_price=_money("15.00"))])
    order.pull_events()
    order.submit(submitted_at=_utc_dt(2026, 7, 15, 9))
    order.approve(approved_at=_utc_dt(2026, 7, 15, 10), approved_by_reference="APPROVER")
    order.place(ordered_at=_utc_dt(2026, 7, 15, 11))
    order.record_receipt(
        receipt_reference="RCPT-RESTORE",
        received_at=_utc_dt(2026, 7, 16, 8),
        lines=[PurchaseReceiptLine(order.lines[0].id, 4)],
    )
    order.record_receipt(
        receipt_reference="RCPT-RESTORE-2",
        received_at=_utc_dt(2026, 7, 17, 8),
        lines=[PurchaseReceiptLine(order.lines[1].id, 2)],
    )
    order.pull_events()

    restored = PurchaseOrder.from_dict(order.to_dict())

    assert restored.pull_events() == []
    assert restored.status is PurchaseOrderStatus.RECEIVED
    assert restored.order_total == order.order_total
    assert restored.received_total == order.received_total
    assert restored.lines[0].received_quantity == Decimal("4")
    assert restored.lines[1].received_quantity == Decimal("2")
    assert len(restored.receipts) == 2


def test_inventory_boundary_uses_opaque_item_reference_only() -> None:
    line = _line(inventory_item_reference="INV-OPAQUE-123")

    assert line.inventory_item_reference == "INV-OPAQUE-123"
    assert isinstance(line.inventory_item_reference, str)
