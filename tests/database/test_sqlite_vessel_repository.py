from __future__ import annotations

from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_dimensions import VesselDimensions
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus
from mfm.infrastructure.persistence.sqlite.sqlite_vessel_repository import (
    SQLiteVesselRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Vessel._clear_registry_for_tests()


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _create_uow(session: Session) -> UnitOfWork:
    return UnitOfWork(session)


def _create_asset(session: Session, asset_number: str) -> UUID:
    owner = ContactModel(
        id=uuid4(),
        contact_number=f"C-{asset_number}",
        status=ContactStatus.ACTIVE,
    )
    session.add(owner)
    session.flush()

    asset = AssetModel(
        asset_number=asset_number,
        name=f"Asset {asset_number}",
        description="Asset for vessel repository tests",
        category=AssetCategory.OTHER,
        status=AssetStatus.ACTIVE,
        owner_id=owner.id,
    )
    asset.location = AssetLocationModel(value="Dock")
    session.add(asset)
    session.flush()
    return asset.id


def _create_vessel(asset_id: UUID, registration: str = "OY-REP-001") -> Vessel:
    return Vessel(
        asset_id=asset_id,
        registration=VesselRegistration(registration),
        name="Repository Vessel",
        shipyard="Odense",
        build_year=2011,
        construction_material=VesselMaterial.STEEL,
        length=25.0,
        beam=6.1,
        draft=2.0,
        status=VesselStatus.ACTIVE,
    )


def test_vessel_repository_add() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-ADD")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-ADD")
    repo.add(vessel)
    uow.commit()

    loaded = repo.get_by_id(vessel.id.value)
    assert loaded is not None
    assert isinstance(loaded, Vessel)
    assert loaded.registration == VesselRegistration("OY-REP-ADD")


def test_vessel_repository_get_by_id() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-ID")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-ID")
    repo.add(vessel)
    uow.commit()

    loaded = repo.get_by_id(vessel.id.value)
    assert loaded is not None
    assert loaded.id == vessel.id


def test_vessel_repository_get_by_registration() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-REG")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "oy-rep-reg")
    repo.add(vessel)
    uow.commit()

    loaded = repo.get_by_registration("OY-REP-REG")
    assert loaded is not None
    assert loaded.id == vessel.id


def test_vessel_repository_update() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-UPD")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-UPD")
    repo.add(vessel)
    uow.commit()

    vessel.rename("Updated Vessel")
    vessel.update_dimensions(vessel_dimensions := vessel_dimensions_factory())
    vessel.change_status(VesselStatus.LAID_UP)

    repo.update(vessel)
    uow.commit()

    loaded = repo.get_by_id(vessel.id.value)
    assert loaded is not None
    assert loaded.name == "Updated Vessel"
    assert loaded.length == vessel_dimensions.length
    assert loaded.beam == vessel_dimensions.beam
    assert loaded.draft == vessel_dimensions.draft
    assert loaded.status is VesselStatus.LAID_UP


def vessel_dimensions_factory():
    return VesselDimensions(length=33.3, beam=7.4, draft=2.8)


def test_vessel_repository_delete() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-DEL")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-DEL")
    repo.add(vessel)
    uow.commit()

    repo.delete(vessel.id.value)
    uow.commit()

    assert repo.get_by_id(vessel.id.value) is None


def test_vessel_repository_exists() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-EXS")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-EXS")
    repo.add(vessel)
    uow.commit()

    assert repo.exists(vessel.id.value) is True

    repo.delete(vessel.id.value)
    uow.commit()

    assert repo.exists(vessel.id.value) is False


def test_vessel_repository_list() -> None:
    _, session = _create_session()
    asset_id_1 = _create_asset(session, "ASSET-VR-LST1")
    asset_id_2 = _create_asset(session, "ASSET-VR-LST2")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    first = _create_vessel(asset_id_1, "OY-REP-LST1")
    second = _create_vessel(asset_id_2, "OY-REP-LST2")

    repo.add(first)
    repo.add(second)
    uow.commit()

    items = repo.list()
    assert all(isinstance(item, Vessel) for item in items)
    assert any(item.id == first.id for item in items)
    assert any(item.id == second.id for item in items)


def test_vessel_repository_search() -> None:
    _, session = _create_session()
    asset_id_1 = _create_asset(session, "ASSET-VR-SR1")
    asset_id_2 = _create_asset(session, "ASSET-VR-SR2")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    first = _create_vessel(asset_id_1, "OY-HARBOR-001")
    first.rename("Harbor Queen")

    second = _create_vessel(asset_id_2, "OY-RIVER-001")
    second.rename("River Star")

    repo.add(first)
    repo.add(second)
    uow.commit()

    hits = repo.search("Harbor")
    assert all(isinstance(item, Vessel) for item in hits)
    assert any(item.id == first.id for item in hits)
    assert all(item.id != second.id for item in hits)


def test_vessel_repository_mapper_database_roundtrip_and_asset_id_preserved() -> None:
    _, session = _create_session()
    asset_id = _create_asset(session, "ASSET-VR-RT")
    uow = _create_uow(session)
    repo = SQLiteVesselRepository(uow)

    vessel = _create_vessel(asset_id, "OY-REP-RT")
    repo.add(vessel)
    uow.commit()

    reloaded = repo.get_by_registration("OY-REP-RT")
    assert reloaded is not None
    assert reloaded == vessel
    assert reloaded.asset_id == asset_id
