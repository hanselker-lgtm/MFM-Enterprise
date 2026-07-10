from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import date
from typing import Any
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.asset.create_asset import AssetCreatedEvent
from mfm.application.asset.create_asset import BusinessRuleViolation
from mfm.application.asset.create_asset import CreateAssetRequest
from mfm.application.asset.create_asset import CreateAssetUseCase
from mfm.application.asset.create_asset import RepositoryException
from mfm.application.asset.create_asset import ValidationException
from mfm.application.asset.dispose_asset import AssetDisposedEvent
from mfm.application.asset.dispose_asset import DisposeAssetRequest
from mfm.application.asset.dispose_asset import DisposeAssetUseCase
from mfm.application.asset.relocate_asset import AssetRelocatedEvent
from mfm.application.asset.relocate_asset import RelocateAssetRequest
from mfm.application.asset.relocate_asset import RelocateAssetUseCase
from mfm.application.asset.retire_asset import AssetRetiredEvent
from mfm.application.asset.retire_asset import RetireAssetRequest
from mfm.application.asset.retire_asset import RetireAssetUseCase
from mfm.application.asset.transfer_asset import AssetTransferredEvent
from mfm.application.asset.transfer_asset import TransferAssetRequest
from mfm.application.asset.transfer_asset import TransferAssetUseCase
from mfm.application.asset.update_asset import AssetUpdatedEvent
from mfm.application.asset.update_asset import UpdateAssetRequest
from mfm.application.asset.update_asset import UpdateAssetUseCase
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.events.event_handler import EventHandler
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def handle(self, event: DomainEvent) -> None:
        self.events.append(event)


class InMemoryAssetRepository:
    def __init__(
        self,
        store: dict[UUID, Asset],
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def add(self, asset: Asset) -> None:
        if self._fail_on_add:
            raise RuntimeError("asset add failed")
        self._store[asset.id.value] = asset

    def get_by_id(self, asset_id: UUID) -> Asset | None:
        return self._store.get(asset_id)

    def get_by_asset_number(self, asset_number: str) -> Asset | None:
        normalized = AssetNumber(asset_number).value
        return next(
            (
                item
                for item in self._store.values()
                if item.asset_number.value == normalized
            ),
            None,
        )

    def update(self, asset: Asset) -> None:
        if self._fail_on_update:
            raise RuntimeError("asset update failed")
        self._store[asset.id.value] = asset

    def delete(self, asset_id: UUID) -> None:
        self._store.pop(asset_id, None)

    def exists(self, asset_id: UUID) -> bool:
        return asset_id in self._store

    def list(self) -> list[Asset]:
        return list(self._store.values())

    def search(self, text: str) -> list[Asset]:
        lowered = text.casefold()
        return [
            item
            for item in self._store.values()
            if lowered in item.asset_number.value.casefold()
            or lowered in item.name.casefold()
            or lowered in item.description.casefold()
            or lowered in item.location.value.casefold()
        ]


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity: Any) -> None:
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_asset_add: bool = False,
        fail_asset_update: bool = False,
    ) -> None:
        super().__init__()
        self.fail_asset_add = fail_asset_add
        self.fail_asset_update = fail_asset_update

        self.assets: dict[UUID, Asset] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self._snapshot = deepcopy(self.assets)

        self.asset_repository = InMemoryAssetRepository(
            self.assets,
            fail_on_add=self.fail_asset_add,
            fail_on_update=self.fail_asset_update,
        )

        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = _NoopRepo()
        self.invoice_repository = _NoopRepo()
        self.payment_repository = _NoopRepo()
        self.journal_repository = _NoopRepo()

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self.assets = self._snapshot

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


@pytest.fixture(autouse=True)
def clear_asset_registry() -> None:
    Asset._clear_registry_for_tests()


@pytest.fixture()
def dispatcher() -> DomainEventDispatcher:
    return DomainEventDispatcher()


def _event_collector(dispatcher: DomainEventDispatcher, event_type: type[DomainEvent]) -> EventCollector:
    collector = EventCollector()
    dispatcher.register(event_type, collector)
    return collector


def _seed_asset(uow: FakeUnitOfWork, *, number: str = "ASSET-APP-001") -> Asset:
    asset = Asset(
        asset_number=AssetNumber(number),
        name="Seed Asset",
        description="Seed",
        category=AssetCategory.EQUIPMENT,
        owner_id=uuid4(),
        location=AssetLocation("Warehouse A"),
        acquisition_date=date(2024, 1, 1),
    )
    uow.assets[asset.id.value] = asset
    return asset


def test_create_asset() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetCreatedEvent)
    use_case = CreateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        CreateAssetRequest(
            asset_number="ASSET-APP-100",
            name="Application Asset",
            description="Created through use case",
            category=AssetCategory.TOOL,
            owner_id=uuid4(),
            location="Workshop",
            acquisition_date=date(2025, 1, 1),
        )
    )

    assert uow.commits == 1
    assert response.asset_id in uow.assets
    assert response.status is AssetStatus.ACTIVE
    assert len(collector.events) == 1


def test_update_asset() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetUpdatedEvent)
    asset = _seed_asset(uow, number="ASSET-APP-101")

    use_case = UpdateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        UpdateAssetRequest(asset_id=asset.id.value, name="Updated Name")
    )

    assert uow.commits == 1
    assert response.name == "Updated Name"
    assert uow.assets[asset.id.value].name == "Updated Name"
    assert len(collector.events) == 1


def test_relocate_asset() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetRelocatedEvent)
    asset = _seed_asset(uow, number="ASSET-APP-102")

    use_case = RelocateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        RelocateAssetRequest(asset_id=asset.id.value, location="Warehouse B")
    )

    assert uow.commits == 1
    assert response.location == "Warehouse B"
    assert uow.assets[asset.id.value].location == AssetLocation("Warehouse B")
    assert len(collector.events) == 1


def test_transfer_ownership() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetTransferredEvent)
    asset = _seed_asset(uow, number="ASSET-APP-103")

    use_case = TransferAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    new_owner = uuid4()

    response = use_case.execute(
        TransferAssetRequest(asset_id=asset.id.value, owner_id=new_owner)
    )

    assert uow.commits == 1
    assert response.owner_id == new_owner
    assert uow.assets[asset.id.value].owner_id == new_owner
    assert len(collector.events) == 1


def test_retire_asset() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetRetiredEvent)
    asset = _seed_asset(uow, number="ASSET-APP-104")

    use_case = RetireAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        RetireAssetRequest(asset_id=asset.id.value, retired_on=date(2026, 1, 1))
    )

    assert uow.commits == 1
    assert response.status is AssetStatus.RETIRED
    assert response.retired_date == date(2026, 1, 1)
    assert len(collector.events) == 1


def test_dispose_asset() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, AssetDisposedEvent)
    asset = _seed_asset(uow, number="ASSET-APP-105")

    use_case = DisposeAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        DisposeAssetRequest(asset_id=asset.id.value, disposed_on=date(2026, 2, 1))
    )

    assert uow.commits == 1
    assert response.status is AssetStatus.DISPOSED
    assert response.retired_date == date(2026, 2, 1)
    assert len(collector.events) == 1


def test_duplicate_asset_number() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    _ = _seed_asset(uow, number="ASSET-APP-DUP")

    use_case = CreateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateAssetRequest(
                asset_number="asset-app-dup",
                name="Duplicate",
                description="Should fail",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )


def test_rollback() -> None:
    uow = FakeUnitOfWork(fail_asset_add=True)
    dispatcher = DomainEventDispatcher()
    use_case = CreateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            CreateAssetRequest(
                asset_number="ASSET-APP-ROLLBACK",
                name="Rollback",
                description="Failing add",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_unit_of_work_commit() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    use_case = CreateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    _ = use_case.execute(
        CreateAssetRequest(
            asset_number="ASSET-APP-COMMIT",
            name="Commit Asset",
            description="Commit check",
            category=AssetCategory.OTHER,
            owner_id=None,
            location="Warehouse",
        )
    )

    assert uow.commits == 1


def test_domain_events() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()

    created = _event_collector(dispatcher, AssetCreatedEvent)
    updated = _event_collector(dispatcher, AssetUpdatedEvent)
    relocated = _event_collector(dispatcher, AssetRelocatedEvent)
    transferred = _event_collector(dispatcher, AssetTransferredEvent)
    retired = _event_collector(dispatcher, AssetRetiredEvent)
    disposed = _event_collector(dispatcher, AssetDisposedEvent)

    create_use_case = CreateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    update_use_case = UpdateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    relocate_use_case = RelocateAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    transfer_use_case = TransferAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    retire_use_case = RetireAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)
    dispose_use_case = DisposeAssetUseCase(unit_of_work=uow, dispatcher=dispatcher)

    create_response = create_use_case.execute(
        CreateAssetRequest(
            asset_number="ASSET-APP-EVENTS",
            name="Events Asset",
            description="Event checks",
            category=AssetCategory.OTHER,
            owner_id=None,
            location="Warehouse",
        )
    )

    _ = update_use_case.execute(
        UpdateAssetRequest(asset_id=create_response.asset_id, name="Events Asset Updated")
    )
    _ = relocate_use_case.execute(
        RelocateAssetRequest(asset_id=create_response.asset_id, location="Warehouse B")
    )
    _ = transfer_use_case.execute(
        TransferAssetRequest(asset_id=create_response.asset_id, owner_id=uuid4())
    )
    _ = retire_use_case.execute(
        RetireAssetRequest(asset_id=create_response.asset_id, retired_on=date(2026, 1, 1))
    )
    _ = dispose_use_case.execute(
        DisposeAssetRequest(asset_id=create_response.asset_id, disposed_on=date(2026, 2, 1))
    )

    assert len(created.events) == 1
    assert len(updated.events) == 1
    assert len(relocated.events) == 1
    assert len(transferred.events) == 1
    assert len(retired.events) == 1
    assert len(disposed.events) == 1
