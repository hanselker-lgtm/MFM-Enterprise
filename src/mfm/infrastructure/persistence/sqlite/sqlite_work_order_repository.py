"""SQLite repository for WorkOrder aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from mfm.database.mappers.maintenance_mapper import MaintenanceMapper
from mfm.database.models.work_order_model import WorkOrderModel
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.repositories.unit_of_work import UnitOfWork
from mfm.repositories.work_order_repository import WorkOrderRepository


class SQLiteWorkOrderRepository(WorkOrderRepository):
    """SQLAlchemy-backed repository for WorkOrder aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, work_order: WorkOrder) -> None:
        self._session.add(MaintenanceMapper.to_orm_work_order(work_order))
        self._session.flush()

    def get_by_id(self, work_order_id: UUID) -> WorkOrder | None:
        orm = self._session.scalar(
            select(WorkOrderModel)
            .options(selectinload(WorkOrderModel.records))
            .where(WorkOrderModel.id == work_order_id)
        )
        if orm is None:
            return None
        return MaintenanceMapper.to_domain_work_order(orm)

    def update(self, work_order: WorkOrder) -> None:
        existing = self._session.scalar(
            select(WorkOrderModel)
            .options(selectinload(WorkOrderModel.records))
            .where(WorkOrderModel.id == work_order.id.value)
        )
        if existing is None:
            raise ValueError(f"Work order {work_order.id.value} does not exist")

        self._session.merge(MaintenanceMapper.to_orm_work_order(work_order))
        self._session.flush()

    def delete(self, work_order_id: UUID) -> None:
        orm = self._session.get(WorkOrderModel, work_order_id)
        if orm is None:
            return

        if orm.status.value == "COMPLETED" or orm.records:
            raise ValueError(
                "Completed work orders or work orders with maintenance records cannot be deleted"
            )

        self._session.delete(orm)
        self._session.flush()

    def exists(self, work_order_id: UUID) -> bool:
        return self._session.get(WorkOrderModel, work_order_id) is not None

    def list(self) -> list[WorkOrder]:
        orm_entities = self._session.scalars(
            select(WorkOrderModel).options(selectinload(WorkOrderModel.records))
        ).unique().all()
        return [MaintenanceMapper.to_domain_work_order(orm) for orm in orm_entities]

    def get_by_maintenance_requirement_id(
        self,
        maintenance_requirement_id: UUID,
    ) -> list[WorkOrder]:
        orm_entities = self._session.scalars(
            select(WorkOrderModel)
            .options(selectinload(WorkOrderModel.records))
            .where(WorkOrderModel.maintenance_requirement_id == maintenance_requirement_id)
        ).unique().all()
        return [MaintenanceMapper.to_domain_work_order(orm) for orm in orm_entities]
