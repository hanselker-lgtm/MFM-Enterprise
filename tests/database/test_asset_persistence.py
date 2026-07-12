from __future__ import annotations

from datetime import date
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.mappers.asset_mapper import AssetMapper
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def test_asset_model_create_update_delete() -> None:
    engine, session = _create_session()
    try:
        owner_id = uuid4()
        asset = AssetModel(
            asset_number="ASSET-P-001",
            name="Portable Generator",
            description="Backup power",
            category=AssetCategory.EQUIPMENT,
            status=AssetStatus.ACTIVE,
            owner_id=owner_id,
            acquisition_date=date(2023, 5, 1),
        )
        asset.location = AssetLocationModel(value="Warehouse A")

        session.add(asset)
        session.commit()

        loaded = session.get(AssetModel, asset.id)
        assert loaded is not None
        assert loaded.asset_number == "ASSET-P-001"
        assert loaded.location.value == "Warehouse A"

        loaded.name = "Portable Generator MK2"
        loaded.status = AssetStatus.INACTIVE
        loaded.location.value = "Warehouse B"
        session.commit()

        updated = session.get(AssetModel, asset.id)
        assert updated is not None
        assert updated.name == "Portable Generator MK2"
        assert updated.status is AssetStatus.INACTIVE
        assert updated.location.value == "Warehouse B"

        location_id = updated.location.id
        session.delete(updated)
        session.commit()

        assert session.get(AssetModel, asset.id) is None
        assert session.get(AssetLocationModel, location_id) is None
    finally:
        session.close()
        engine.dispose()


def test_asset_location_relation_persists_and_updates() -> None:
    engine, session = _create_session()
    try:
        asset = AssetModel(
            asset_number="ASSET-P-002",
            name="Head Office",
            description="Main building",
            category=AssetCategory.BUILDING,
            status=AssetStatus.ACTIVE,
        )
        asset.location = AssetLocationModel(value="Campus North")

        session.add(asset)
        session.commit()

        loaded = session.get(AssetModel, asset.id)
        assert loaded is not None
        assert loaded.location.asset_id == loaded.id

        loaded.location.value = "Campus South"
        session.commit()

        reloaded = session.get(AssetModel, asset.id)
        assert reloaded is not None
        assert reloaded.location.value == "Campus South"
    finally:
        session.close()
        engine.dispose()


def test_asset_lifecycle_fields_persist() -> None:
    engine, session = _create_session()
    try:
        asset = AssetModel(
            asset_number="ASSET-P-003",
            name="Legacy Crane",
            description="Harbor crane",
            category=AssetCategory.OTHER,
            status=AssetStatus.ACTIVE,
            acquisition_date=date(2010, 1, 1),
        )
        asset.location = AssetLocationModel(value="Pier 1")

        session.add(asset)
        session.commit()

        loaded = session.get(AssetModel, asset.id)
        assert loaded is not None

        loaded.status = AssetStatus.RETIRED
        loaded.retired_date = date(2025, 12, 31)
        session.commit()

        retired = session.get(AssetModel, asset.id)
        assert retired is not None
        assert retired.status is AssetStatus.RETIRED
        assert retired.retired_date == date(2025, 12, 31)

        retired.status = AssetStatus.DISPOSED
        session.commit()

        disposed = session.get(AssetModel, asset.id)
        assert disposed is not None
        assert disposed.status is AssetStatus.DISPOSED
    finally:
        session.close()
        engine.dispose()


def test_asset_serialization_via_mapper_roundtrip() -> None:
    engine, session = _create_session()
    try:
        domain_asset = Asset(
            asset_number=AssetNumber("ASSET-P-004"),
            name="Serializable Asset",
            description="Serialize through persistence",
            category=AssetCategory.TOOL,
            status=AssetStatus.INACTIVE,
            owner_id=uuid4(),
            location=AssetLocation("Workshop"),
            acquisition_date=date(2022, 3, 15),
        )

        orm = AssetMapper.to_orm_asset(domain_asset)
        session.add(orm)
        session.commit()

        loaded = session.get(AssetModel, orm.id)
        assert loaded is not None

        restored = AssetMapper.to_domain_asset(loaded)
        payload = restored.to_dict()
        serialized_restored = Asset.from_dict(payload)

        assert serialized_restored == restored
        assert serialized_restored.location == AssetLocation("Workshop")
    finally:
        session.close()
        engine.dispose()
