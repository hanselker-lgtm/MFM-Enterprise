from __future__ import annotations

from uuid import uuid4

import pytest

from mfm.database.mappers.vessel_mapper import VesselMapper
from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel
from mfm.database.models.vessel_model import VesselModel
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Vessel._clear_registry_for_tests()


def test_vessel_mapper_roundtrip() -> None:
    vessel = Vessel(
        asset_id=uuid4(),
        registration=VesselRegistration("OY-MAP-001"),
        name="Mapper Vessel",
        shipyard="Lindoe",
        build_year=2014,
        construction_material=VesselMaterial.STEEL,
        length=41.2,
        beam=8.3,
        draft=3.1,
        status=VesselStatus.ACTIVE,
    )

    orm = VesselMapper.to_orm_vessel(vessel)

    assert isinstance(orm, VesselModel)
    assert orm.id == vessel.id.value
    assert orm.registration == "OY-MAP-001"
    assert isinstance(orm.dimensions, VesselDimensionsModel)
    assert orm.dimensions.length == 41.2

    restored = VesselMapper.to_domain_vessel(orm)

    assert restored.id == vessel.id
    assert restored.asset_id == vessel.asset_id
    assert restored.registration == vessel.registration
    assert restored.name == vessel.name
    assert restored.shipyard == vessel.shipyard
    assert restored.build_year == vessel.build_year
    assert restored.construction_material is vessel.construction_material
    assert restored.length == vessel.length
    assert restored.beam == vessel.beam
    assert restored.draft == vessel.draft
    assert restored.status is vessel.status
