from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from mfm.database.mappers.purchase_order_mapper import PurchaseOrderMapper
from mfm.database.models.base_model import BaseModel
from mfm.database.models.purchase_order_line_model import PurchaseOrderLineModel
from mfm.database.models.purchase_order_model import PurchaseOrderModel
from mfm.database.models.purchase_receipt_line_model import PurchaseReceiptLineModel
from mfm.database.models.purchase_receipt_model import PurchaseReceiptModel
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
from mfm.domain.procurement.exceptions import InvalidPurchaseReceiptError
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    connection = engine.connect()
    BaseModel.metadata.create_all(connection)
    session = Session(bind=connection)
    session.info["test_connection"] = connection
    session.info["test_engine"] = engine
    return session


def _close_session(session: Session) -> None:
    connection = session.info.pop("test_connection", None)
    engine = session.info.pop("test_engine", None)
    session.close()
    if isinstance(connection, Connection):
        connection.close()
    if isinstance(engine, Engine):
        engine.dispose()


def _aware(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int = 0,
    *,
    offset_hours: int = 0,
) -> datetime:
    local_tz = timezone(timedelta(hours=offset_hours))
    return datetime(year, month, day, hour, minute, tzinfo=local_tz)


def _line(
    *,
    line_id: UUID,
    description: str,
    quantity: Decimal,
    unit_price: Decimal,
    inventory_item_reference: str | None,
    expected_delivery_at: datetime | None,
    line_note: str | None,
) -> PurchaseOrderLine:
    return PurchaseOrderLine(
        id=line_id,
        description_snapshot=description,
        quantity=quantity,
        unit_price=Money(amount=unit_price, currency=Currency.DKK),
        inventory_item_reference=inventory_item_reference,
        expected_delivery_at=expected_delivery_at,
        line_note=line_note,
    )


def _order(*, order_id: UUID, order_number: str) -> PurchaseOrder:
    order = PurchaseOrder(
        id=order_id,
        purchase_order_number=order_number,
        supplier_reference="SUP-001",
        currency=Currency.DKK,
        created_at=_aware(2028, 1, 5, 10, 30, offset_hours=1),
        supplier_name_snapshot="Northern Marine Supplies",
        supplier_contact_snapshot="accounts@nms.example",
        notes="Quarterly consumables",
        requested_by_reference="user-req-1",
    )
    order.pull_events()

    order.add_line(
        _line(
            line_id=UUID("00000000-0000-0000-0000-00000000C101"),
            description="Deck paint red",
            quantity=Decimal("12.500"),
            unit_price=Decimal("199.95"),
            inventory_item_reference="INV-PAINT-RED",
            expected_delivery_at=_aware(2028, 1, 20, 8, 0, offset_hours=2),
            line_note="Port-side storage",
        )
    )
    order.add_line(
        _line(
            line_id=UUID("00000000-0000-0000-0000-00000000C102"),
            description="Hydraulic oil",
            quantity=Decimal("3.000"),
            unit_price=Decimal("750.10"),
            inventory_item_reference="INV-HYD-OIL",
            expected_delivery_at=None,
            line_note=None,
        )
    )
    return order


def _persist_and_reload(session: Session, order: PurchaseOrder) -> PurchaseOrder:
    orm = PurchaseOrderMapper.to_orm_purchase_order(order)
    session.add(orm)
    session.commit()
    session.expunge_all()

    loaded = session.get(PurchaseOrderModel, order.id.value)
    assert loaded is not None
    return PurchaseOrderMapper.to_domain_purchase_order(loaded)


def test_purchase_order_creation_roundtrip_preserves_identity_and_snapshots(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-create-roundtrip")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C001"),
            order_number="PO-2028-001",
        )

        restored = _persist_and_reload(session, order)

        assert restored.id == order.id
        assert restored.purchase_order_number == order.purchase_order_number
        assert restored.supplier_reference == order.supplier_reference
        assert restored.supplier_name_snapshot == "Northern Marine Supplies"
        assert restored.supplier_contact_snapshot == "accounts@nms.example"
        assert restored.notes == "Quarterly consumables"
        assert restored.requested_by_reference == "user-req-1"
        assert restored.status is PurchaseOrderStatus.DRAFT
    finally:
        _close_session(session)


def test_line_roundtrip_preserves_quantity_money_and_inventory_reference(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-line-roundtrip")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C002"),
            order_number="PO-2028-002",
        )

        restored = _persist_and_reload(session, order)

        assert len(restored.lines) == 2
        assert restored.lines[0].quantity == Decimal("12.500")
        assert restored.lines[0].unit_price.amount == Decimal("199.95")
        assert restored.lines[0].unit_price.currency is Currency.DKK
        assert restored.lines[0].inventory_item_reference == "INV-PAINT-RED"
        assert restored.lines[1].quantity == Decimal("3.000")
        assert restored.lines[1].unit_price.amount == Decimal("750.10")
        assert restored.order_total.amount == Decimal("4749.68")
        assert restored.order_total.currency is Currency.DKK
    finally:
        _close_session(session)


def test_supplier_and_inventory_references_remain_opaque_identifiers(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-opaque-references")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C003"),
            order_number="PO-2028-003",
        )

        restored = _persist_and_reload(session, order)

        assert restored.supplier_reference.value == "SUP-001"
        assert restored.lines[0].inventory_item_reference == "INV-PAINT-RED"
        assert not hasattr(restored, "supplier")
    finally:
        _close_session(session)


def test_lifecycle_roundtrip_preserves_status_transitions_and_timestamps(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-lifecycle-roundtrip")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C004"),
            order_number="PO-2028-004",
        )
        order.submit(submitted_at=_aware(2028, 1, 7, 9, 0, offset_hours=1))
        order.approve(
            approved_at=_aware(2028, 1, 8, 11, 30, offset_hours=1),
            approved_by_reference="manager-1",
        )
        order.place(
            ordered_at=_aware(2028, 1, 9, 14, 45, offset_hours=1),
            external_order_reference="SUP-ORDER-77",
        )

        restored = _persist_and_reload(session, order)

        assert restored.status is PurchaseOrderStatus.ORDERED
        assert restored.approved_by_reference == "manager-1"
        assert restored.external_order_reference == "SUP-ORDER-77"
        assert restored.approved_at is not None and restored.approved_at.tzinfo is UTC
        assert restored.ordered_at is not None and restored.ordered_at.tzinfo is UTC
    finally:
        _close_session(session)


def test_receipt_history_roundtrip_preserves_append_only_historical_truth(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-receipt-history")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C005"),
            order_number="PO-2028-005",
        )
        line_one_id = order.lines[0].id
        line_two_id = order.lines[1].id

        order.submit(submitted_at=_aware(2028, 2, 1, 9, 0, offset_hours=1))
        order.approve(
            approved_at=_aware(2028, 2, 2, 10, 0, offset_hours=1),
            approved_by_reference="manager-2",
        )
        order.place(ordered_at=_aware(2028, 2, 3, 11, 0, offset_hours=1))
        order.record_receipt(
            receipt_reference="RCPT-1",
            received_at=_aware(2028, 2, 5, 8, 0, offset_hours=1),
            lines=[
                PurchaseReceiptLine(
                    purchase_order_line_id=line_one_id,
                    quantity=Decimal("2.500"),
                )
            ],
        )
        order.record_receipt(
            receipt_reference="RCPT-2",
            received_at=_aware(2028, 2, 6, 8, 0, offset_hours=1),
            lines=[
                PurchaseReceiptLine(
                    purchase_order_line_id=line_one_id,
                    quantity=Decimal("10.000"),
                ),
                PurchaseReceiptLine(
                    purchase_order_line_id=line_two_id,
                    quantity=Decimal("3.000"),
                ),
            ],
        )

        restored = _persist_and_reload(session, order)

        assert restored.status is PurchaseOrderStatus.RECEIVED
        assert [receipt.receipt_reference for receipt in restored.receipts] == [
            "RCPT-1",
            "RCPT-2",
        ]
        assert restored.lines[0].received_quantity == Decimal("12.500")
        assert restored.lines[1].received_quantity == Decimal("3.000")
        assert restored.received_total.amount == Decimal("4749.68")
    finally:
        _close_session(session)


def test_mapper_restoration_emits_no_false_domain_events(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-restoration-events")
    try:
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000C006"),
            order_number="PO-2028-006",
        )
        order.submit(submitted_at=_aware(2028, 3, 1, 8, 0, offset_hours=1))
        order.approve(
            approved_at=_aware(2028, 3, 2, 8, 0, offset_hours=1),
            approved_by_reference="manager-3",
        )
        order.place(ordered_at=_aware(2028, 3, 3, 8, 0, offset_hours=1))
        order.record_receipt(
            receipt_reference="RCPT-3",
            received_at=_aware(2028, 3, 5, 8, 0, offset_hours=1),
            lines=[
                PurchaseReceiptLine(
                    purchase_order_line_id=order.lines[0].id,
                    quantity=Decimal("12.500"),
                ),
                PurchaseReceiptLine(
                    purchase_order_line_id=order.lines[1].id,
                    quantity=Decimal("3.000"),
                ),
            ],
        )
        order.pull_events()

        restored = _persist_and_reload(session, order)

        assert restored.pull_events() == []
    finally:
        _close_session(session)


def test_timezone_roundtrip_preserves_utc_semantics_for_header_and_lines(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-timezone")
    try:
        order = PurchaseOrder(
            id=UUID("00000000-0000-0000-0000-00000000C007"),
            purchase_order_number="PO-2028-007",
            supplier_reference="SUP-007",
            currency=Currency.DKK,
            created_at=_aware(2028, 4, 1, 8, 0, offset_hours=2),
        )
        order.pull_events()
        order.add_line(
            PurchaseOrderLine(
                id=UUID("00000000-0000-0000-0000-00000000C107"),
                description_snapshot="Rope",
                quantity=Decimal("1.000"),
                unit_price=Money(amount=Decimal("99.99"), currency=Currency.DKK),
                expected_delivery_at=_aware(2028, 4, 3, 10, 0, offset_hours=-3),
            )
        )

        restored = _persist_and_reload(session, order)

        assert restored.created_at.tzinfo is UTC
        assert restored.lines[0].expected_delivery_at is not None
        assert restored.lines[0].expected_delivery_at.tzinfo is UTC
        assert restored.created_at == datetime(2028, 4, 1, 6, 0, tzinfo=UTC)
        assert restored.lines[0].expected_delivery_at == datetime(
            2028,
            4,
            3,
            13,
            0,
            tzinfo=UTC,
        )
    finally:
        _close_session(session)


def test_table_metadata_registers_procurement_persistence_models(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "purchase-order-metadata")
    try:
        inspector = inspect(session.info["test_connection"])
        tables = set(inspector.get_table_names())

        assert "purchase_order" in tables
        assert "purchase_order_line" in tables
        assert "purchase_receipt" in tables
        assert "purchase_receipt_line" in tables
    finally:
        _close_session(session)


def test_invalid_persistence_state_unknown_status_fails_restore() -> None:
    orm = PurchaseOrderModel(
        id=UUID("00000000-0000-0000-0000-00000000C008"),
        purchase_order_number="PO-2028-008",
        supplier_reference="SUP-008",
        status="UNKNOWN",  # type: ignore[arg-type]
        currency=Currency.DKK,
        order_created_at=_aware(2028, 5, 1, 8, 0),
    )

    with pytest.raises((ValueError, TypeError)):
        PurchaseOrderMapper.to_domain_purchase_order(orm)


def test_invalid_persistence_state_receipt_referencing_missing_line_fails_restore() -> None:
    orm = PurchaseOrderModel(
        id=UUID("00000000-0000-0000-0000-00000000C009"),
        purchase_order_number="PO-2028-009",
        supplier_reference="SUP-009",
        status=PurchaseOrderStatus.PARTIALLY_RECEIVED,
        currency=Currency.DKK,
        order_created_at=_aware(2028, 5, 2, 8, 0),
        approved_by_reference="manager",
        approved_at=_aware(2028, 5, 2, 9, 0),
        ordered_at=_aware(2028, 5, 2, 10, 0),
    )
    orm.lines.append(
        PurchaseOrderLineModel(
            id=UUID("00000000-0000-0000-0000-00000000C201"),
            purchase_order_id=orm.id,
            line_order=0,
            description_snapshot="Fallback line",
            quantity=Decimal("2.000"),
            unit_price_amount=Decimal("10.00"),
            unit_price_currency=Currency.DKK,
            received_quantity=Decimal("1.000"),
        )
    )

    receipt = PurchaseReceiptModel(
        id=UUID("00000000-0000-0000-0000-00000000C901"),
        purchase_order_id=orm.id,
        receipt_order=0,
        receipt_reference="RCPT-INVALID",
        received_at=_aware(2028, 5, 3, 8, 0),
    )
    receipt.lines.append(
        PurchaseReceiptLineModel(
            purchase_receipt_id=receipt.id,
            purchase_order_line_id=UUID("00000000-0000-0000-0000-00000000C999"),
            receipt_line_order=0,
            quantity=Decimal("1.000"),
        )
    )
    orm.receipts.append(receipt)

    with pytest.raises(InvalidPurchaseReceiptError):
        PurchaseOrderMapper.to_domain_purchase_order(orm)
