"""SQLite repository for MaintenancePlan aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from mfm.database.mappers.maintenance_mapper import MaintenanceMapper
from mfm.database.models.maintenance_plan_model import MaintenancePlanModel
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteMaintenancePlanRepository(MaintenancePlanRepository):
    """SQLAlchemy-backed repository for MaintenancePlan aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, plan: MaintenancePlan) -> None:
        self._session.add(MaintenanceMapper.to_orm_plan(plan))
        self._session.flush()

    def get_by_id(self, plan_id: UUID) -> MaintenancePlan | None:
        orm = self._session.scalar(
            select(MaintenancePlanModel)
            .options(selectinload(MaintenancePlanModel.requirements))
            .where(MaintenancePlanModel.id == plan_id)
        )
        if orm is None:
            return None
        return MaintenanceMapper.to_domain_plan(orm)

    def update(self, plan: MaintenancePlan) -> None:
        existing = self._session.scalar(
            select(MaintenancePlanModel)
            .options(selectinload(MaintenancePlanModel.requirements))
            .where(MaintenancePlanModel.id == plan.id.value)
        )
        if existing is None:
            raise ValueError(f"Maintenance plan {plan.id.value} does not exist")

        self._session.merge(MaintenanceMapper.to_orm_plan(plan))
        self._session.flush()

    def delete(self, plan_id: UUID) -> None:
        orm = self._session.get(MaintenancePlanModel, plan_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, plan_id: UUID) -> bool:
        return self._session.get(MaintenancePlanModel, plan_id) is not None

    def list(self) -> list[MaintenancePlan]:
        orm_entities = self._session.scalars(
            select(MaintenancePlanModel).options(
                selectinload(MaintenancePlanModel.requirements)
            )
        ).unique().all()
        return [MaintenanceMapper.to_domain_plan(orm) for orm in orm_entities]

    def get_by_target(self, target: MaintenanceTarget) -> list[MaintenancePlan]:
        orm_entities = self._session.scalars(
            select(MaintenancePlanModel)
            .options(selectinload(MaintenancePlanModel.requirements))
            .where(
                MaintenancePlanModel.target_type == target.target_type,
                MaintenancePlanModel.target_id == target.target_id,
            )
        ).unique().all()
        return [MaintenanceMapper.to_domain_plan(orm) for orm in orm_entities]
