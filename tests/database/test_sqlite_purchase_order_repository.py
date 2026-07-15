from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from pathlib import Path
import weakref
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine
from mfm.infrastructure.persistence.sqlite.sqlite_purchase_order_repository import (
    SQLitePurchaseOrderRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


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
    inventory_item_reference: str | None = None,
) -> PurchaseOrderLine:
    return PurchaseOrderLine(
        id=line_id,
        description_snapshot=description,
        quantity=quantity,
        unit_price=Money(amount=unit_price, currency=Currency.DKK),
        inventory_item_reference=inventory_item_reference,
    )


def _order(
    *,
    order_id: UUID | None = None,
    order_number: str,
    supplier_reference: str = "SUP-001",
) -> PurchaseOrder:
    order = PurchaseOrder(
        id=order_id or uuid4(),
        purchase_order_number=order_number,
        supplier_reference=supplier_reference,
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
            line_id=uuid4(),
            description="Deck paint red",
            quantity=Decimal("12.500"),
            unit_price=Decimal("199.95"),
            inventory_item_reference="INV-PAINT-RED",
        )
    )
    order.add_line(
        _line(
            line_id=uuid4(),
            description="Hydraulic oil",
            quantity=Decimal("3.000"),
            unit_price=Decimal("750.10"),
            inventory_item_reference="INV-HYD-OIL",
        )
    )
    return order


def _progress_to_ordered(order: PurchaseOrder) -> None:
    order.submit(submitted_at=_aware(2028, 2, 1, 9, 0, offset_hours=1))
    order.approve(
        approved_at=_aware(2028, 2, 2, 10, 0, offset_hours=1),
        approved_by_reference="manager-1",
    )
    order.place(
        ordered_at=_aware(2028, 2, 3, 11, 0, offset_hours=1),
        external_order_reference="SUP-ORDER-77",
    )


def test_purchase_order_repository_add_get_by_id_and_missing(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-add-get.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(session))
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E001"),
            order_number="PO-REPO-001",
        )

        repository.add(order)
        session.commit()

        loaded = repository.get_by_id(order.id.value)
        assert loaded is not None
        assert loaded.id == order.id
        assert loaded.purchase_order_number.value == "PO-REPO-001"
        assert loaded.supplier_reference.value == "SUP-001"

        missing = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000E999"))
        assert missing is None
    finally:
        session.close()


def test_purchase_order_repository_get_by_number_and_exists_by_number(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-number.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(session))
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E002"),
            order_number="PO-REPO-002",
        )

        repository.add(order)
        session.commit()

        by_str = repository.get_by_number("PO-REPO-002")
        by_value_object = repository.get_by_number(PurchaseOrderNumber("PO-REPO-002"))
        missing = repository.get_by_number("PO-REPO-NOT-FOUND")

        assert by_str is not None
        assert by_str.id == order.id
        assert by_value_object is not None
        assert by_value_object.id == order.id
        assert missing is None
        assert repository.exists_by_number("PO-REPO-002") is True
        assert repository.exists_by_number(PurchaseOrderNumber("PO-REPO-002")) is True
        assert repository.exists_by_number("PO-REPO-NOT-FOUND") is False
    finally:
        session.close()


def test_purchase_order_repository_update_persists_history_and_status_across_sessions(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-update.sqlite"
    first_session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(first_session))
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E003"),
            order_number="PO-REPO-003",
        )
        repository.add(order)
        first_session.commit()

        loaded = repository.get_by_id(order.id.value)
        assert loaded is not None

        _progress_to_ordered(loaded)
        loaded.record_receipt(
            receipt_reference="RCPT-1",
            received_at=_aware(2028, 2, 5, 8, 0, offset_hours=1),
            lines=[
                PurchaseReceiptLine(
                    purchase_order_line_id=loaded.lines[0].id,
                    quantity=Decimal("2.500"),
                )
            ],
        )

        repository.update(loaded)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(second_session))
        restored = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000E003"))

        assert restored is not None
        assert restored.status is PurchaseOrderStatus.PARTIALLY_RECEIVED
        assert restored.approved_by_reference == "manager-1"
        assert restored.external_order_reference == "SUP-ORDER-77"
        assert restored.approved_at is not None and restored.approved_at.tzinfo is UTC
        assert restored.ordered_at is not None and restored.ordered_at.tzinfo is UTC
        assert len(restored.receipts) == 1
        assert restored.receipts[0].receipt_reference == "RCPT-1"
        assert restored.lines[0].received_quantity == Decimal("2.500")
        assert restored.lines[1].received_quantity == Decimal("0")
    finally:
        second_session.close()


def test_purchase_order_repository_list_and_filter_methods(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-list.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(session))

        draft = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E004"),
            order_number="PO-REPO-A",
            supplier_reference="SUP-A",
        )
        submitted = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E005"),
            order_number="PO-REPO-B",
            supplier_reference="SUP-A",
        )
        submitted.submit(submitted_at=_aware(2028, 3, 1, 9, 0, offset_hours=1))

        ordered = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E006"),
            order_number="PO-REPO-C",
            supplier_reference="SUP-B",
        )
        _progress_to_ordered(ordered)

        repository.add(submitted)
        repository.add(ordered)
        repository.add(draft)
        session.commit()

        listed = repository.list()
        assert [item.purchase_order_number.value for item in listed] == [
            "PO-REPO-A",
            "PO-REPO-B",
            "PO-REPO-C",
        ]

        submitted_only = repository.list_by_state(PurchaseOrderStatus.SUBMITTED)
        assert [item.purchase_order_number.value for item in submitted_only] == [
            "PO-REPO-B",
        ]

        ordered_only = repository.list_by_state("ORDERED")
        assert [item.purchase_order_number.value for item in ordered_only] == [
            "PO-REPO-C",
        ]

        supplier_a = repository.list_by_supplier_reference("SUP-A")
        assert [item.purchase_order_number.value for item in supplier_a] == [
            "PO-REPO-A",
            "PO-REPO-B",
        ]

        supplier_b = repository.list_by_supplier_reference(
            SupplierReference("SUP-B")
        )
        assert [item.purchase_order_number.value for item in supplier_b] == [
            "PO-REPO-C",
        ]
    finally:
        session.close()


def test_purchase_order_repository_duplicate_number_and_missing_update_raise_value_error(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-errors.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(session))

        first = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E007"),
            order_number="PO-REPO-DUP",
        )
        duplicate = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E008"),
            order_number="PO-REPO-DUP",
        )
        missing = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E009"),
            order_number="PO-REPO-MISSING",
        )

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(duplicate)

        with pytest.raises(ValueError):
            repository.update(missing)
    finally:
        session.close()


def test_purchase_order_repository_defers_transaction_commit_to_unit_of_work(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-rollback.sqlite"
    first_session = _new_session(db_path)
    try:
        uow = UnitOfWork(first_session)
        repository = SQLitePurchaseOrderRepository(uow)
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E010"),
            order_number="PO-REPO-ROLLBACK",
        )

        repository.add(order)
        uow.rollback()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(second_session))
        assert repository.get_by_number("PO-REPO-ROLLBACK") is None
    finally:
        second_session.close()


def test_purchase_order_repository_reload_does_not_emit_false_restoration_events(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-purchase-order-repository-events.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLitePurchaseOrderRepository(UnitOfWork(session))
        order = _order(
            order_id=UUID("00000000-0000-0000-0000-00000000E011"),
            order_number="PO-REPO-EVENTS",
        )
        _progress_to_ordered(order)
        order.record_receipt(
            receipt_reference="RCPT-E1",
            received_at=_aware(2028, 4, 1, 8, 0, offset_hours=1),
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

        repository.add(order)
        session.commit()

        loaded = repository.get_by_id(order.id.value)
        assert loaded is not None
        assert loaded.pull_events() == []
    finally:
        session.close()
