"""Create WorkOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.maintenance.create_maintenance_plan import (
    ApplicationException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_maintenance_plan import WorkOrderResponse
from mfm.application.maintenance.create_maintenance_plan import to_work_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository
from mfm.repositories.work_order_repository import WorkOrderRepository


@dataclass(frozen=True, slots=True)
class CreateWorkOrderRequest:
    maintenance_plan_id: UUID
    maintenance_requirement_id: UUID
    title: str
    description: str
    planned_date: date | None = None

    def validate(self) -> None:
        if not isinstance(self.maintenance_plan_id, UUID):
            raise ValidationException("maintenance_plan_id must be UUID")
        if not isinstance(self.maintenance_requirement_id, UUID):
            raise ValidationException("maintenance_requirement_id must be UUID")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationException("title must be a non-empty string")
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValidationException("description must be a non-empty string")
        if self.planned_date is not None and not isinstance(self.planned_date, date):
            raise ValidationException("planned_date must be date or None")


@dataclass(frozen=True, slots=True)
class CreateWorkOrderResponse:
    work_order: WorkOrderResponse


class CreateWorkOrderUseCase:
    """Create work order from existing maintenance requirement context."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateWorkOrderRequest) -> CreateWorkOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                plan_repository: MaintenancePlanRepository = uow.maintenance_plan_repository
                work_order_repository: WorkOrderRepository = uow.work_order_repository

                plan = plan_repository.get_by_id(request.maintenance_plan_id)
                if plan is None:
                    raise BusinessRuleViolation(
                        f"Maintenance plan {request.maintenance_plan_id} does not exist"
                    )

                requirement = plan.get_requirement(request.maintenance_requirement_id)
                if requirement is None:
                    raise BusinessRuleViolation(
                        f"Maintenance requirement {request.maintenance_requirement_id} does not exist"
                    )

                work_order = WorkOrder(
                    maintenance_target=plan.maintenance_target,
                    maintenance_requirement_id=requirement.id,
                    title=request.title,
                    description=request.description,
                    planned_date=request.planned_date,
                )
                work_order_repository.add(work_order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create work order failed") from exc

        return CreateWorkOrderResponse(work_order=to_work_order_response(work_order))
