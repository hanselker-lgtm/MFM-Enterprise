from __future__ import annotations

from datetime import date
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus
from mfm.infrastructure.persistence.sqlite.sqlite_asset_repository import SQLiteAssetRepository
from mfm.repositories.unit_of_work import UnitOfWork


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _create_uow(session: Session) -> UnitOfWork:
    return UnitOfWork(session)


def _create_asset(number: str = "ASSET-R-001") -> Asset:
    return Asset(
        asset_number=AssetNumber(number),
        name="Repository Asset",
        description="Generic repository test asset",
        category=AssetCategory.EQUIPMENT,
        status=AssetStatus.ACTIVE,
        owner_id=uuid4(),
        location=AssetLocation("Warehouse Alpha"),
        acquisition_date=date(2022, 1, 1),
    )


def test_asset_repository_add_and_get_by_id() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("ASSET-R-ADD")
        repo.add(asset)
        uow.commit()

        loaded = repo.get_by_id(asset.id.value)
        assert loaded is not None
        assert isinstance(loaded, Asset)
        assert loaded == asset
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_get_by_asset_number() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("asset-r-number")
        repo.add(asset)
        uow.commit()

        loaded = repo.get_by_asset_number("ASSET-R-NUMBER")
        assert loaded is not None
        assert loaded.id == asset.id
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_update() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("ASSET-R-UPDATE")
        repo.add(asset)
        uow.commit()

        asset.rename("Updated Asset")
        asset.change_location("Warehouse Beta")
        asset.change_owner(None)
        asset.deactivate()

        repo.update(asset)
        uow.commit()

        updated = repo.get_by_id(asset.id.value)
        assert updated is not None
        assert updated.name == "Updated Asset"
        assert updated.location == AssetLocation("Warehouse Beta")
        assert updated.owner_id is None
        assert updated.status is AssetStatus.INACTIVE
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_delete() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("ASSET-R-DELETE")
        repo.add(asset)
        uow.commit()

        repo.delete(asset.id.value)
        uow.commit()

        assert repo.get_by_id(asset.id.value) is None
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_exists() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("ASSET-R-EXISTS")
        repo.add(asset)
        uow.commit()

        assert repo.exists(asset.id.value) is True

        repo.delete(asset.id.value)
        uow.commit()

        assert repo.exists(asset.id.value) is False
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_list() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        first = _create_asset("ASSET-R-LIST-1")
        second = _create_asset("ASSET-R-LIST-2")
        second.change_location("Harbor East")

        repo.add(first)
        repo.add(second)
        uow.commit()

        items = repo.list()

        assert all(isinstance(item, Asset) for item in items)
        assert any(item.id == first.id for item in items)
        assert any(item.id == second.id for item in items)
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_search() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        first = _create_asset("ASSET-R-SEARCH-1")
        first.rename("Harbor Crane")
        first.change_location("Pier A")

        second = _create_asset("ASSET-R-SEARCH-2")
        second.rename("Office Desk")
        second.change_location("Head Office")

        repo.add(first)
        repo.add(second)
        uow.commit()

        hits = repo.search("Pier")

        assert all(isinstance(item, Asset) for item in hits)
        assert any(item.id == first.id for item in hits)
        assert all(item.id != second.id for item in hits)
    finally:
        session.close()
        engine.dispose()


def test_asset_repository_mapper_roundtrip() -> None:
    engine, session = _create_session()
    try:
        uow = _create_uow(session)
        repo = SQLiteAssetRepository(uow)

        asset = _create_asset("ASSET-R-ROUNDTRIP")
        asset.dispose(date(2026, 1, 1))
        repo.add(asset)
        uow.commit()

        reloaded = repo.get_by_id(asset.id.value)
        assert reloaded is not None
        assert reloaded == asset
        assert reloaded.status is AssetStatus.DISPOSED
        assert reloaded.retired_date == date(2026, 1, 1)
    finally:
        session.close()
        engine.dispose()
