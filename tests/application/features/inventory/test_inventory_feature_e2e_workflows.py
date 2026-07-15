from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.inventory_item_model  # noqa: F401
import mfm.database.models.inventory_stock_movement_model  # noqa: F401
import mfm.database.models.inventory_stock_position_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.features.inventory.adjust_stock_feature import AdjustStockFeature
from mfm.application.features.inventory.adjust_stock_feature import AdjustStockRequest
from mfm.application.features.inventory.create_inventory_item_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    CreateInventoryItemFeature,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    CreateInventoryItemRequest,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    StockLocationInput,
)
from mfm.application.features.inventory.deactivate_inventory_item_feature import (
    DeactivateInventoryItemFeature,
)
from mfm.application.features.inventory.deactivate_inventory_item_feature import (
    DeactivateInventoryItemRequest,
)
from mfm.application.features.inventory.get_inventory_item_feature import GetInventoryItemFeature
from mfm.application.features.inventory.get_inventory_item_feature import GetInventoryItemRequest
from mfm.application.features.inventory.issue_stock_feature import IssueStockFeature
from mfm.application.features.inventory.issue_stock_feature import IssueStockRequest
from mfm.application.features.inventory.list_inventory_items_feature import (
    ListInventoryItemsFeature,
)
from mfm.application.features.inventory.list_inventory_items_feature import (
    ListInventoryItemsRequest,
)
from mfm.application.features.inventory.list_low_stock_items_feature import (
    ListLowStockItemsFeature,
)
from mfm.application.features.inventory.list_low_stock_items_feature import (
    ListLowStockItemsRequest,
)
from mfm.application.features.inventory.reactivate_inventory_item_feature import (
    ReactivateInventoryItemFeature,
)
from mfm.application.features.inventory.reactivate_inventory_item_feature import (
    ReactivateInventoryItemRequest,
)
from mfm.application.features.inventory.receive_stock_feature import ReceiveStockFeature
from mfm.application.features.inventory.receive_stock_feature import ReceiveStockRequest
from mfm.application.inventory.adjust_stock import AdjustStockUseCase
from mfm.application.inventory.create_inventory_item import CreateInventoryItemUseCase
from mfm.application.inventory.deactivate_inventory_item import DeactivateInventoryItemUseCase
from mfm.application.inventory.get_inventory_item import GetInventoryItemUseCase
from mfm.application.inventory.issue_stock import IssueStockUseCase
from mfm.application.inventory.list_inventory_items import ListInventoryItemsUseCase
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsUseCase
from mfm.application.inventory.reactivate_inventory_item import ReactivateInventoryItemUseCase
from mfm.application.inventory.receive_stock import ReceiveStockUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.sqlite.sqlite_inventory_repository import (
    SQLiteInventoryRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteInventoryApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.inventory_repository = SQLiteInventoryRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class InventoryFeatureStack:
    create: CreateInventoryItemFeature
    get: GetInventoryItemFeature
    list_items: ListInventoryItemsFeature
    receive: ReceiveStockFeature
    issue: IssueStockFeature
    adjust: AdjustStockFeature
    deactivate: DeactivateInventoryItemFeature
    reactivate: ReactivateInventoryItemFeature
    list_low_stock: ListLowStockItemsFeature


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "inventory_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_feature_stack(session: Session) -> InventoryFeatureStack:
    uow = SQLiteInventoryApplicationUnitOfWork(session)

    return InventoryFeatureStack(
        create=CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow)),
        get=GetInventoryItemFeature(service=GetInventoryItemUseCase(unit_of_work=uow)),
        list_items=ListInventoryItemsFeature(
            service=ListInventoryItemsUseCase(unit_of_work=uow)
        ),
        receive=ReceiveStockFeature(service=ReceiveStockUseCase(unit_of_work=uow)),
        issue=IssueStockFeature(service=IssueStockUseCase(unit_of_work=uow)),
        adjust=AdjustStockFeature(service=AdjustStockUseCase(unit_of_work=uow)),
        deactivate=DeactivateInventoryItemFeature(
            service=DeactivateInventoryItemUseCase(unit_of_work=uow)
        ),
        reactivate=ReactivateInventoryItemFeature(
            service=ReactivateInventoryItemUseCase(unit_of_work=uow)
        ),
        list_low_stock=ListLowStockItemsFeature(
            service=ListLowStockItemsUseCase(unit_of_work=uow)
        ),
    )


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _location(
    key: str,
    name: str,
    *,
    vessel_id: UUID | None = None,
) -> StockLocationInput:
    return StockLocationInput(location_key=key, location_name=name, vessel_id=vessel_id)


def _create_request(
    *,
    item_reference: str,
    name: str,
    minimum_stock_level: Decimal | str | int | None,
) -> CreateInventoryItemRequest:
    return CreateInventoryItemRequest(
        item_reference=item_reference,
        name=name,
        description=f"{name} description",
        unit_code="LITRE",
        unit_decimal_places=1,
        unit_display_name="litre",
        minimum_stock_level=minimum_stock_level,
    )


def test_e2e_workflow_1_create_retrieve_and_list_inventory_items(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        created = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-001",
                name="Hydraulic Oil",
                minimum_stock_level=Decimal("2.0"),
            )
        )

        loaded = stack.get.execute(
            GetInventoryItemRequest(
                inventory_item_id=created.inventory_item.inventory_item_id,
            )
        )

        assert loaded.inventory_item.inventory_item_id == created.inventory_item.inventory_item_id
        assert loaded.inventory_item.item_reference == "INV-E2E-001"
        assert loaded.inventory_item.name == "Hydraulic Oil"
        assert loaded.inventory_item.unit_code == "LITRE"
        assert loaded.inventory_item.status == "ACTIVE"
        assert loaded.inventory_item.total_quantity == Decimal("0.0")
        assert loaded.inventory_item.movements == ()

        listed = stack.list_items.execute(ListInventoryItemsRequest())
        refs = [item.item_reference for item in listed.items]
        assert "INV-E2E-001" in refs
    finally:
        session.close()


def test_e2e_workflow_2_historical_stock_truth_roundtrip(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        location = _location("STORE-A", "Store A")

        created = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-HISTORY",
                name="Primer Paint",
                minimum_stock_level=Decimal("0.0"),
            )
        )
        item_id = created.inventory_item.inventory_item_id

        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("10.0"),
                occurred_at=_aware_utc(2030, 1, 1, 8),
                note="opening",
            )
        )
        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("5.0"),
                occurred_at=_aware_utc(2030, 1, 2, 8),
                note="receive",
            )
        )
        stack.issue.execute(
            IssueStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("3.0"),
                occurred_at=_aware_utc(2030, 1, 3, 8),
                note="issue",
            )
        )
        adjusted = stack.adjust.execute(
            AdjustStockRequest(
                inventory_item_id=item_id,
                location=location,
                counted_quantity=Decimal("11.0"),
                reason="cycle count",
                occurred_at=_aware_utc(2030, 1, 4, 8),
                note="adjust",
            )
        )

        assert adjusted.inventory_item.total_quantity == Decimal("11.0")
        assert [movement.movement_type for movement in adjusted.inventory_item.movements] == [
            "RECEIPT",
            "RECEIPT",
            "ISSUE",
            "ADJUSTMENT_DECREASE",
        ]
        assert [movement.quantity for movement in adjusted.inventory_item.movements] == [
            Decimal("10.0"),
            Decimal("5.0"),
            Decimal("3.0"),
            Decimal("1.0"),
        ]
    finally:
        session.close()


def test_e2e_workflow_3_insufficient_stock_does_not_persist_invalid_state(
    sqlite_session_factory,
) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        location = _location("STORE-B", "Store B")

        created = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-INSUFFICIENT",
                name="Cleaning Fluid",
                minimum_stock_level=Decimal("0.0"),
            )
        )
        item_id = created.inventory_item.inventory_item_id

        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("2.0"),
                occurred_at=_aware_utc(2030, 2, 1, 8),
            )
        )

        with pytest.raises(BusinessRuleViolation):
            stack.issue.execute(
                IssueStockRequest(
                    inventory_item_id=item_id,
                    location=location,
                    quantity=Decimal("3.0"),
                    occurred_at=_aware_utc(2030, 2, 1, 9),
                )
            )

        loaded = stack.get.execute(GetInventoryItemRequest(inventory_item_id=item_id))
        assert loaded.inventory_item.total_quantity == Decimal("2.0")
        assert [movement.movement_type for movement in loaded.inventory_item.movements] == [
            "RECEIPT",
        ]
    finally:
        session.close()


def test_e2e_workflow_4_low_stock_semantics_and_inventory_boundary(
    sqlite_session_factory,
) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        location = _location("STORE-C", "Store C")

        above = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-LOW-ABOVE",
                name="Above Threshold",
                minimum_stock_level=Decimal("2.0"),
            )
        )
        equal = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-LOW-EQUAL",
                name="Equal Threshold",
                minimum_stock_level=Decimal("2.0"),
            )
        )
        below = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-LOW-BELOW",
                name="Below Threshold",
                minimum_stock_level=Decimal("2.0"),
            )
        )

        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=above.inventory_item.inventory_item_id,
                location=location,
                quantity=Decimal("3.0"),
                occurred_at=_aware_utc(2030, 3, 1, 8),
            )
        )
        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=equal.inventory_item.inventory_item_id,
                location=location,
                quantity=Decimal("2.0"),
                occurred_at=_aware_utc(2030, 3, 1, 9),
            )
        )
        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=below.inventory_item.inventory_item_id,
                location=location,
                quantity=Decimal("1.0"),
                occurred_at=_aware_utc(2030, 3, 1, 10),
            )
        )

        low_stock = stack.list_low_stock.execute(ListLowStockItemsRequest())
        refs = [item.item_reference for item in low_stock.items]

        assert refs == ["INV-E2E-LOW-BELOW"]

        # Inventory low-stock query returns inventory state only and no procurement side effects.
        for item in low_stock.items:
            assert not hasattr(item, "supplier_id")
            assert not hasattr(item, "purchase_order_id")
    finally:
        session.close()


def test_e2e_workflow_5_deactivate_and_reactivate(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        created = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-LIFECYCLE",
                name="Lifecycle Item",
                minimum_stock_level=Decimal("0.0"),
            )
        )
        item_id = created.inventory_item.inventory_item_id

        deactivated = stack.deactivate.execute(
            DeactivateInventoryItemRequest(inventory_item_id=item_id)
        )
        assert deactivated.inventory_item.status == "INACTIVE"

        loaded_inactive = stack.get.execute(GetInventoryItemRequest(inventory_item_id=item_id))
        assert loaded_inactive.inventory_item.status == "INACTIVE"

        reactivated = stack.reactivate.execute(
            ReactivateInventoryItemRequest(inventory_item_id=item_id)
        )
        assert reactivated.inventory_item.status == "ACTIVE"

        loaded_active = stack.get.execute(GetInventoryItemRequest(inventory_item_id=item_id))
        assert loaded_active.inventory_item.status == "ACTIVE"
    finally:
        session.close()


def test_e2e_workflow_6_persistence_reopen_preserves_state_and_history(tmp_path: Path) -> None:
    db_path = tmp_path / "inventory_feature_e2e_reopen.sqlite"
    location = _location("STORE-R", "Store Reopen")
    item_id: UUID

    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    SessionFactory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    first_session = SessionFactory()
    try:
        stack = _build_feature_stack(first_session)

        created = stack.create.execute(
            _create_request(
                item_reference="INV-E2E-REOPEN",
                name="Durable Item",
                minimum_stock_level=Decimal("0.0"),
            )
        )
        item_id = created.inventory_item.inventory_item_id

        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("10.0"),
                occurred_at=_aware_utc(2030, 4, 1, 8),
            )
        )
        stack.receive.execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("5.0"),
                occurred_at=_aware_utc(2030, 4, 2, 8),
            )
        )
        stack.issue.execute(
            IssueStockRequest(
                inventory_item_id=item_id,
                location=location,
                quantity=Decimal("3.0"),
                occurred_at=_aware_utc(2030, 4, 3, 8),
            )
        )
        stack.adjust.execute(
            AdjustStockRequest(
                inventory_item_id=item_id,
                location=location,
                counted_quantity=Decimal("11.0"),
                reason="cycle count",
                occurred_at=_aware_utc(2030, 4, 4, 8),
            )
        )
    finally:
        first_session.close()
        engine.dispose()

    reopen_engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(reopen_engine)
    ReopenSessionFactory = sessionmaker(
        bind=reopen_engine,
        expire_on_commit=False,
        class_=Session,
    )

    reopened_session = ReopenSessionFactory()
    try:
        reopened_stack = _build_feature_stack(reopened_session)
        loaded = reopened_stack.get.execute(GetInventoryItemRequest(inventory_item_id=item_id))

        assert loaded.inventory_item.item_reference == "INV-E2E-REOPEN"
        assert loaded.inventory_item.total_quantity == Decimal("11.0")
        assert [movement.movement_type for movement in loaded.inventory_item.movements] == [
            "RECEIPT",
            "RECEIPT",
            "ISSUE",
            "ADJUSTMENT_DECREASE",
        ]
        assert [movement.quantity for movement in loaded.inventory_item.movements] == [
            Decimal("10.0"),
            Decimal("5.0"),
            Decimal("3.0"),
            Decimal("1.0"),
        ]
    finally:
        reopened_session.close()
        reopen_engine.dispose()