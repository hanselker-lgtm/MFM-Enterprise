"""SQLite repository for Vessel aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.vessel_mapper import VesselMapper
from mfm.database.models.vessel_model import VesselModel
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.repositories.unit_of_work import UnitOfWork
from mfm.repositories.vessel_repository import VesselRepository


class SQLiteVesselRepository(VesselRepository):
    """SQLAlchemy-backed repository for Vessel aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, vessel: Vessel) -> None:
        if self._session.scalar(
            select(VesselModel).where(
                VesselModel.registration == vessel.registration.value
            )
        ) is not None:
            raise ValueError(f"Registration {vessel.registration.value} already exists")

        self._session.add(VesselMapper.to_orm_vessel(vessel))
        self._session.flush()

    def get_by_id(self, vessel_id: UUID) -> Vessel | None:
        orm = self._session.scalar(
            select(VesselModel)
            .options(joinedload(VesselModel.dimensions))
            .where(VesselModel.id == vessel_id)
        )
        if orm is None:
            return None
        return VesselMapper.to_domain_vessel(orm)

    def get_by_registration(self, registration: str) -> Vessel | None:
        normalized = VesselRegistration(registration).value
        orm = self._session.scalar(
            select(VesselModel)
            .options(joinedload(VesselModel.dimensions))
            .where(VesselModel.registration == normalized)
        )
        if orm is None:
            return None
        return VesselMapper.to_domain_vessel(orm)

    def update(self, vessel: Vessel) -> None:
        orm = self._session.scalar(
            select(VesselModel)
            .options(joinedload(VesselModel.dimensions))
            .where(VesselModel.id == vessel.id.value)
        )
        if orm is None:
            raise ValueError(f"Vessel {vessel.id.value} does not exist")

        if orm.registration != vessel.registration.value:
            duplicate = self._session.scalar(
                select(VesselModel).where(
                    VesselModel.registration == vessel.registration.value,
                    VesselModel.id != vessel.id.value,
                )
            )
            if duplicate is not None:
                raise ValueError(
                    f"Registration {vessel.registration.value} already exists"
                )

        orm.asset_id = vessel.asset_id
        orm.registration = vessel.registration.value
        orm.name = vessel.name
        orm.shipyard = vessel.shipyard
        orm.build_year = vessel.build_year
        orm.construction_material = vessel.construction_material
        orm.status = vessel.status

        if orm.dimensions is None:
            raise ValueError(f"Vessel {vessel.id.value} has no dimensions row")

        orm.dimensions.length = vessel.length
        orm.dimensions.beam = vessel.beam
        orm.dimensions.draft = vessel.draft
        self._session.flush()

    def delete(self, vessel_id: UUID) -> None:
        orm = self._session.get(VesselModel, vessel_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, vessel_id: UUID) -> bool:
        return self._session.get(VesselModel, vessel_id) is not None

    def list(self) -> list[Vessel]:
        orm_entities = self._session.scalars(
            select(VesselModel).options(joinedload(VesselModel.dimensions))
        ).unique().all()
        return [VesselMapper.to_domain_vessel(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Vessel]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(VesselModel)
            .options(joinedload(VesselModel.dimensions))
            .where(
                or_(
                    VesselModel.registration.ilike(query),
                    VesselModel.name.ilike(query),
                    VesselModel.shipyard.ilike(query),
                )
            )
        ).unique().all()
        return [VesselMapper.to_domain_vessel(orm) for orm in orm_entities]
