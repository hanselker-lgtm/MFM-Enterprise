"""SQLite repository for Voyage aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.voyage_mapper import VoyageMapper
from mfm.database.models.voyage_model import VoyageModel
from mfm.domain.voyages.voyage import Voyage
from mfm.repositories.unit_of_work import UnitOfWork
from mfm.repositories.voyage_repository import VoyageRepository


class SQLiteVoyageRepository(VoyageRepository):
    """SQLAlchemy-backed repository for Voyage aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, voyage: Voyage) -> None:
        self._session.add(VoyageMapper.to_orm_voyage(voyage))
        self._session.flush()

    def get_by_id(self, voyage_id: UUID) -> Voyage | None:
        orm = self._session.scalar(
            select(VoyageModel).where(VoyageModel.id == voyage_id)
        )
        if orm is None:
            return None
        return VoyageMapper.to_domain_voyage(orm)

    def update(self, voyage: Voyage) -> None:
        existing = self._session.get(VoyageModel, voyage.id.value)
        if existing is None:
            raise ValueError(f"Voyage {voyage.id.value} does not exist")

        self._session.merge(VoyageMapper.to_orm_voyage(voyage))
        self._session.flush()

    def exists(self, voyage_id: UUID) -> bool:
        return self._session.get(VoyageModel, voyage_id) is not None

    def list(self) -> list[Voyage]:
        orm_entities = self._session.scalars(
            select(VoyageModel).order_by(
                VoyageModel.planned_departure_at,
                VoyageModel.created_at,
            )
        ).all()
        return [VoyageMapper.to_domain_voyage(orm) for orm in orm_entities]

    def get_by_vessel(self, vessel_id: UUID) -> list[Voyage]:
        orm_entities = self._session.scalars(
            select(VoyageModel)
            .where(VoyageModel.vessel_id == vessel_id)
            .order_by(
                VoyageModel.planned_departure_at,
                VoyageModel.created_at,
            )
        ).all()
        return [VoyageMapper.to_domain_voyage(orm) for orm in orm_entities]
