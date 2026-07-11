"""Get Maintenance history use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.maintenance.create_maintenance_plan import (
    ApplicationException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenancePlanResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenanceRecordResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_maintenance_plan import parse_target_type
from mfm.application.maintenance.create_maintenance_plan import to_plan_response
from mfm.application.maintenance.create_maintenance_plan import to_record_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository
from mfm.repositories.work_order_repository import WorkOrderRepository


@dataclass(frozen=True, slots=True)
class GetMaintenanceHistoryRequest:
    target_type: str
    target_id: UUID

    def validate(self) -> None:
        if not isinstance(self.target_type, str) or not self.target_type.strip():
            raise ValidationException("target_type must be a non-empty string")
        if not isinstance(self.target_id, UUID):
            raise ValidationException("target_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetMaintenanceHistoryResponse:
    target_type: str
    target_id: UUID
    plans: tuple[MaintenancePlanResponse, ...]
    records: tuple[MaintenanceRecordResponse, ...]


class GetMaintenanceHistoryUseCase:
    """Load persistent maintenance history for one maintenance target."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: GetMaintenanceHistoryRequest,
    ) -> GetMaintenanceHistoryResponse:
        request.validate()

        target = MaintenanceTarget(
            target_type=parse_target_type(request.target_type),
            target_id=request.target_id,
        )

        try:
            with self._unit_of_work as uow:
                plan_repository: MaintenancePlanRepository = uow.maintenance_plan_repository
                work_order_repository: WorkOrderRepository = uow.work_order_repository

                plans = plan_repository.get_by_target(target)
                work_orders = work_order_repository.list()

                records = [
                    work_order.maintenance_record
                    for work_order in work_orders
                    if work_order.maintenance_record is not None
                    and work_order.maintenance_target == target
                ]
                records.sort(key=lambda item: item.completed_at)
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get maintenance history failed") from exc

        return GetMaintenanceHistoryResponse(
            target_type=target.target_type.value,
            target_id=target.target_id,
            plans=tuple(to_plan_response(plan) for plan in plans),
            records=tuple(to_record_response(record) for record in records),
        )
