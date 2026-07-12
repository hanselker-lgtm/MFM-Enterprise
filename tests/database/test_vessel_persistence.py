from __future__ import annotations

import json
import weakref
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.mappers.vessel_mapper import VesselMapper
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel
from mfm.database.models.vessel_model import VesselModel
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Vessel._clear_registry_for_tests()


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return engine, session


def _create_asset(session: Session, asset_number: str = "ASSET-V-001") -> AssetModel:
    owner = ContactModel(
        id=uuid4(),
        contact_number=f"C-{asset_number}",
        status=ContactStatus.ACTIVE,
    )
    session.add(owner)
    session.flush()

    asset = AssetModel(
        asset_number=asset_number,
        name="Test Vessel Asset",
        description="Asset for vessel persistence tests",
        category=AssetCategory.OTHER,
        status=AssetStatus.ACTIVE,
        owner_id=owner.id,
    )
    asset.location = AssetLocationModel(value="Dock A")
    session.add(asset)
    session.flush()
    return asset


def test_vessel_model_create_update_delete() -> None:
    _, session = _create_session()
    asset = _create_asset(session, "ASSET-V-010")

    vessel = VesselModel(
        asset_id=asset.id,
        registration="OY-PERSIST-010",
        name="Persistence One",
        shipyard="Aalborg",
        build_year=2010,
        construction_material=VesselMaterial.STEEL,
        status=VesselStatus.ACTIVE,
    )
    vessel.dimensions = VesselDimensionsModel(length=30.0, beam=6.0, draft=2.2)

    session.add(vessel)
    session.commit()

    loaded = session.get(VesselModel, vessel.id)
    assert loaded is not None
    assert loaded.registration == "OY-PERSIST-010"
    assert loaded.dimensions.length == 30.0

    loaded.name = "Persistence Updated"
    loaded.status = VesselStatus.LAID_UP
    loaded.dimensions.beam = 6.5
    session.commit()

    updated = session.get(VesselModel, vessel.id)
    assert updated is not None
    assert updated.name == "Persistence Updated"
    assert updated.status is VesselStatus.LAID_UP
    assert updated.dimensions.beam == 6.5

    dimensions_id = updated.dimensions.id
    session.delete(updated)
    session.commit()

    assert session.get(VesselModel, vessel.id) is None
    assert session.get(VesselDimensionsModel, dimensions_id) is None


def test_vessel_relation_to_asset_model() -> None:
    _, session = _create_session()
    asset = _create_asset(session, "ASSET-V-011")

    vessel = VesselModel(
        asset_id=asset.id,
        registration="OY-PERSIST-011",
        name="Relation Vessel",
        shipyard="Esbjerg",
        build_year=2016,
        construction_material=VesselMaterial.ALUMINUM,
        status=VesselStatus.ACTIVE,
    )
    vessel.dimensions = VesselDimensionsModel(length=22.0, beam=5.0, draft=1.8)

    session.add(vessel)
    session.commit()

    loaded = session.get(VesselModel, vessel.id)
    assert loaded is not None
    assert loaded.asset is not None
    assert loaded.asset.id == asset.id
    assert loaded.asset.vessel is not None
    assert loaded.asset.vessel.id == loaded.id


def test_vessel_mapper_roundtrip_through_persistence() -> None:
    _, session = _create_session()
    asset = _create_asset(session, "ASSET-V-012")

    domain_vessel = Vessel(
        asset_id=asset.id,
        registration=VesselRegistration("OY-PERSIST-012"),
        name="Mapper Through DB",
        shipyard="Odense",
        build_year=2020,
        construction_material=VesselMaterial.COMPOSITE,
        length=18.4,
        beam=4.6,
        draft=1.4,
        status=VesselStatus.ACTIVE,
    )

    orm = VesselMapper.to_orm_vessel(domain_vessel)
    session.add(orm)
    session.commit()

    loaded = session.get(VesselModel, orm.id)
    assert loaded is not None

    restored = VesselMapper.to_domain_vessel(loaded)
    assert restored.id == domain_vessel.id
    assert restored.asset_id == domain_vessel.asset_id
    assert restored.registration == domain_vessel.registration
    assert restored.length == domain_vessel.length
    assert restored.beam == domain_vessel.beam
    assert restored.draft == domain_vessel.draft


def test_vessel_persistence_serialization_payload() -> None:
    _, session = _create_session()
    asset = _create_asset(session, "ASSET-V-013")

    vessel = VesselModel(
        asset_id=asset.id,
        registration="OY-PERSIST-013",
        name="Serializable Vessel",
        shipyard="Nakskov",
        build_year=2018,
        construction_material=VesselMaterial.FIBERGLASS,
        status=VesselStatus.RESTORATION,
    )
    vessel.dimensions = VesselDimensionsModel(length=12.2, beam=3.6, draft=1.1)
    session.add(vessel)
    session.commit()

    loaded = session.get(VesselModel, vessel.id)
    assert loaded is not None

    payload = {
        "id": str(loaded.id),
        "asset_id": str(loaded.asset_id),
        "registration": loaded.registration,
        "name": loaded.name,
        "shipyard": loaded.shipyard,
        "build_year": loaded.build_year,
        "construction_material": loaded.construction_material.value,
        "status": loaded.status.value,
        "dimensions": {
            "length": loaded.dimensions.length,
            "beam": loaded.dimensions.beam,
            "draft": loaded.dimensions.draft,
        },
    }

    serialized = json.dumps(payload)
    deserialized = json.loads(serialized)

    assert deserialized["registration"] == "OY-PERSIST-013"
    assert deserialized["dimensions"]["length"] == 12.2
    assert deserialized["construction_material"] == "FIBERGLASS"
