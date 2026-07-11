"""Calculate due maintenance use case."""

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
    MaintenanceRequirementResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_maintenance_plan import to_requirement_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository


@dataclass(frozen=True, slots=True)
class CalculateDueMaintenanceRequest:
    maintenance_plan_id: UUID
    as_of_date: date
    running_hours_by_requirement_id: dict[UUID, int] | None = None

    def validate(self) -> None:
        if not isinstance(self.maintenance_plan_id, UUID):
            raise ValidationException("maintenance_plan_id must be UUID")
        if not isinstance(self.as_of_date, date):
            raise ValidationException("as_of_date must be date")
        if self.running_hours_by_requirement_id is None:
            return

        if not isinstance(self.running_hours_by_requirement_id, dict):
            raise ValidationException("running_hours_by_requirement_id must be dict or None")

        for key, value in self.running_hours_by_requirement_id.items():
            if not isinstance(key, UUID):
                raise ValidationException("running hours keys must be UUID")
            if not isinstance(value, int) or value < 0:
                raise ValidationException("running hours values must be non-negative int")


@dataclass(frozen=True, slots=True)
class CalculateDueMaintenanceResponse:
    due_requirements: tuple[MaintenanceRequirementResponse, ...]


class CalculateDueMaintenanceUseCase:
    """Calculate due maintenance using domain-owned due logic."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: CalculateDueMaintenanceRequest,
    ) -> CalculateDueMaintenanceResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: MaintenancePlanRepository = uow.maintenance_plan_repository
                plan = repository.get_by_id(request.maintenance_plan_id)
                if plan is None:
                    raise BusinessRuleViolation(
                        f"Maintenance plan {request.maintenance_plan_id} does not exist"
                    )

                due = plan.calculate_due(
                    as_of_date=request.as_of_date,
                    running_hours_by_requirement_id=request.running_hours_by_requirement_id,
                )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Calculate due maintenance failed") from exc

        return CalculateDueMaintenanceResponse(
            due_requirements=tuple(to_requirement_response(item) for item in due)
        )
