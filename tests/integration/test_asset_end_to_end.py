from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.application.asset.create_asset import AssetCreatedEvent
from mfm.application.asset.create_asset import CreateAssetUseCase
from mfm.application.asset.dispose_asset import AssetDisposedEvent
from mfm.application.asset.dispose_asset import DisposeAssetUseCase
from mfm.application.asset.relocate_asset import AssetRelocatedEvent
from mfm.application.asset.relocate_asset import RelocateAssetUseCase
from mfm.application.asset.retire_asset import AssetRetiredEvent
from mfm.application.asset.retire_asset import RetireAssetUseCase
from mfm.application.asset.transfer_asset import AssetTransferredEvent
from mfm.application.asset.transfer_asset import TransferAssetUseCase
from mfm.application.asset.update_asset import AssetUpdatedEvent
from mfm.application.asset.update_asset import UpdateAssetUseCase
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.events.event_handler import EventHandler
from mfm.application.features.asset.create_asset_feature import CreateAssetFeature
from mfm.application.features.asset.create_asset_feature import CreateAssetRequest
from mfm.application.features.asset.dispose_asset_feature import DisposeAssetFeature
from mfm.application.features.asset.dispose_asset_feature import DisposeAssetRequest
from mfm.application.features.asset.relocate_asset_feature import RelocateAssetFeature
from mfm.application.features.asset.relocate_asset_feature import RelocateAssetRequest
from mfm.application.features.asset.retire_asset_feature import RetireAssetFeature
from mfm.application.features.asset.retire_asset_feature import RetireAssetRequest
from mfm.application.features.asset.transfer_ownership_feature import TransferOwnershipFeature
from mfm.application.features.asset.transfer_ownership_feature import TransferOwnershipRequest
from mfm.application.features.asset.update_asset_feature import UpdateAssetFeature
from mfm.application.features.asset.update_asset_feature import UpdateAssetRequest
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.asset.exceptions import InvalidAssetStatusTransitionError
from mfm.infrastructure.persistence.sqlite.sqlite_asset_repository import SQLiteAssetRepository
from mfm.repositories.unit_of_work import UnitOfWork


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def handle(self, event: DomainEvent) -> None:
        self.events.append(event)


class SqliteAssetApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.asset_repository = SQLiteAssetRepository(self._persistence_uow)

        # Required by abstract contract, unused by these workflows.
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
class FeatureStack:
    create_asset: CreateAssetFeature
    update_asset: UpdateAssetFeature
    transfer_ownership: TransferOwnershipFeature
    relocate_asset: RelocateAssetFeature
    retire_asset: RetireAssetFeature
    dispose_asset: DisposeAssetFeature


@pytest.fixture(autouse=True)
def clear_asset_registry() -> None:
    Asset._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "asset-006.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


def _register_event_collectors(dispatcher: DomainEventDispatcher) -> EventCollector:
    collector = EventCollector()
    dispatcher.register(AssetCreatedEvent, collector)
    dispatcher.register(AssetUpdatedEvent, collector)
    dispatcher.register(AssetTransferredEvent, collector)
    dispatcher.register(AssetRelocatedEvent, collector)
    dispatcher.register(AssetRetiredEvent, collector)
    dispatcher.register(AssetDisposedEvent, collector)
    return collector


def _build_stack(session: Session, dispatcher: DomainEventDispatcher) -> FeatureStack:
    app_uow = SqliteAssetApplicationUnitOfWork(session)

    return FeatureStack(
        create_asset=CreateAssetFeature(
            service=CreateAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        update_asset=UpdateAssetFeature(
            service=UpdateAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        transfer_ownership=TransferOwnershipFeature(
            service=TransferAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        relocate_asset=RelocateAssetFeature(
            service=RelocateAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        retire_asset=RetireAssetFeature(
            service=RetireAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        dispose_asset=DisposeAssetFeature(
            service=DisposeAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
    )


def _reload_asset(session: Session, asset_id: UUID) -> Asset:
    reload_uow = UnitOfWork(session)
    repository = SQLiteAssetRepository(reload_uow)

    reloaded = repository.get_by_id(asset_id)
    assert reloaded is not None
    return reloaded


def _assert_asset_rows_exist(session: Session, asset_id: UUID) -> None:
    orm_asset = session.scalar(select(AssetModel).where(AssetModel.id == asset_id))
    orm_location = session.scalar(
        select(AssetLocationModel).where(AssetLocationModel.asset_id == asset_id)
    )

    assert orm_asset is not None
    assert orm_location is not None


def test_asset_006_workflow_1_create_persist_reload_verify(sqlite_session: Session) -> None:
    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-E2E-{uuid4().hex[:6].upper()}",
            name="E2E Crane",
            description="Crane for integration workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock A",
            acquisition_date=date(2026, 1, 1),
        )
    )

    assert response.status == "ACTIVE"
    _assert_asset_rows_exist(sqlite_session, response.asset_id)

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_asset(reload_session, response.asset_id)
        assert reloaded.asset_number.value == response.asset_number
        assert reloaded.name == "E2E Crane"
        assert reloaded.status is AssetStatus.ACTIVE
        assert reloaded.location.value == "Dock A"
    finally:
        reload_session.close()

    assert any(isinstance(event, AssetCreatedEvent) for event in collector.events)


def test_asset_006_workflow_2_transfer_ownership_persist_reload_verify(
    sqlite_session: Session,
) -> None:
    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    create_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-E2E-{uuid4().hex[:6].upper()}",
            name="E2E Vessel",
            description="Vessel for transfer workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock B",
            acquisition_date=date(2026, 1, 2),
        )
    )

    new_owner_id = uuid4()
    transfer_response = stack.transfer_ownership.execute(
        TransferOwnershipRequest(
            asset_id=create_response.asset_id,
            owner_id=new_owner_id,
        )
    )

    assert transfer_response.owner_id == new_owner_id

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_asset(reload_session, create_response.asset_id)
        assert reloaded.owner_id == new_owner_id
        assert reloaded.status is AssetStatus.ACTIVE
    finally:
        reload_session.close()

    assert any(isinstance(event, AssetTransferredEvent) for event in collector.events)


def test_asset_006_workflow_3_relocate_asset_persist_reload_verify(
    sqlite_session: Session,
) -> None:
    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    create_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-E2E-{uuid4().hex[:6].upper()}",
            name="E2E Tool",
            description="Tool for relocation workflow",
            category=AssetCategory.TOOL,
            owner_id=None,
            location="Warehouse A",
            acquisition_date=date(2026, 1, 3),
        )
    )

    relocate_response = stack.relocate_asset.execute(
        RelocateAssetRequest(
            asset_id=create_response.asset_id,
            location="Warehouse B",
        )
    )

    assert relocate_response.location == "Warehouse B"

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_asset(reload_session, create_response.asset_id)
        assert reloaded.location.value == "Warehouse B"
    finally:
        reload_session.close()

    assert any(isinstance(event, AssetRelocatedEvent) for event in collector.events)


def test_asset_006_workflow_4_retire_asset_persist_reload_verify_lifecycle_rules(
    sqlite_session: Session,
) -> None:
    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    create_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-E2E-{uuid4().hex[:6].upper()}",
            name="E2E Generator",
            description="Generator for retirement workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Yard",
            acquisition_date=date(2026, 1, 4),
        )
    )

    retired_on = date(2026, 4, 1)
    retire_response = stack.retire_asset.execute(
        RetireAssetRequest(
            asset_id=create_response.asset_id,
            retired_on=retired_on,
        )
    )

    assert retire_response.status == "RETIRED"
    assert retire_response.retired_date == retired_on

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_asset(reload_session, create_response.asset_id)
        assert reloaded.status is AssetStatus.RETIRED
        assert reloaded.retired_date == retired_on

        # Lifecycle rule check: retired assets can be reactivated.
        reloaded.activate()
        reload_uow = UnitOfWork(reload_session)
        repository = SQLiteAssetRepository(reload_uow)
        repository.update(reloaded)
        reload_uow.commit()

        reloaded_again = _reload_asset(reload_session, create_response.asset_id)
        assert reloaded_again.status is AssetStatus.ACTIVE
        assert reloaded_again.retired_date is None
    finally:
        reload_session.close()

    assert any(isinstance(event, AssetRetiredEvent) for event in collector.events)


def test_asset_006_workflow_5_dispose_asset_persist_reload_verify_disposed_cannot_reactivate(
    sqlite_session: Session,
) -> None:
    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    create_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-E2E-{uuid4().hex[:6].upper()}",
            name="E2E Container",
            description="Container for disposal workflow",
            category=AssetCategory.OTHER,
            owner_id=None,
            location="Terminal",
            acquisition_date=date(2026, 1, 5),
        )
    )

    disposed_on = date(2026, 6, 1)
    dispose_response = stack.dispose_asset.execute(
        DisposeAssetRequest(
            asset_id=create_response.asset_id,
            disposed_on=disposed_on,
        )
    )

    assert dispose_response.status == "DISPOSED"
    assert dispose_response.retired_date == disposed_on

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_asset(reload_session, create_response.asset_id)
        assert reloaded.status is AssetStatus.DISPOSED

        with pytest.raises(InvalidAssetStatusTransitionError):
            reloaded.activate()
    finally:
        reload_session.close()

    assert any(isinstance(event, AssetDisposedEvent) for event in collector.events)
