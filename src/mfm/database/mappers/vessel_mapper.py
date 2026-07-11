"""Mapper between vessel domain aggregate and persistence models."""

from __future__ import annotations

from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel
from mfm.database.models.vessel_model import VesselModel
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_id import VesselId
from mfm.domain.fleet.vessel_registration import VesselRegistration


class VesselMapper:
    """Map between vessel domain aggregate and SQLAlchemy models."""

    @staticmethod
    def to_orm_vessel(vessel: Vessel) -> VesselModel:
        orm = VesselModel(
            id=vessel.id.value,
            asset_id=vessel.asset_id,
            registration=vessel.registration.value,
            name=vessel.name,
            shipyard=vessel.shipyard,
            build_year=vessel.build_year,
            construction_material=vessel.construction_material,
            status=vessel.status,
        )
        orm.dimensions = VesselDimensionsModel(
            vessel_id=vessel.id.value,
            length=vessel.length,
            beam=vessel.beam,
            draft=vessel.draft,
        )
        return orm

    @staticmethod
    def to_domain_vessel(orm: VesselModel) -> Vessel:
        return Vessel(
            id=VesselId(orm.id),
            asset_id=orm.asset_id,
            registration=VesselRegistration(orm.registration),
            name=orm.name,
            shipyard=orm.shipyard,
            build_year=orm.build_year,
            construction_material=orm.construction_material,
            length=orm.dimensions.length,
            beam=orm.dimensions.beam,
            draft=orm.dimensions.draft,
            status=orm.status,
        )
