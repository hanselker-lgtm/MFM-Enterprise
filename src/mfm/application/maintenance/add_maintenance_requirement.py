"""Add MaintenanceRequirement use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

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
    RepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_maintenance_plan import to_plan_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType
from mfm.domain.maintenance.maintenance_requirement import MaintenanceRequirement
from mfm.domain.maintenance.maintenance_type import MaintenanceType
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository


def _parse_maintenance_type(value: str) -> MaintenanceType:
    try:
        return MaintenanceType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("maintenance_type is invalid") from exc


def _parse_interval_type(value: str) -> MaintenanceIntervalType:
    try:
        return MaintenanceIntervalType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("interval_type is invalid") from exc


def _parse_due_basis(value: str) -> MaintenanceDueBasis:
    try:
        return MaintenanceDueBasis(value.strip().upper())
    except Exception as exc:
        raise ValidationException("due_basis is invalid") from exc


@dataclass(frozen=True, slots=True)
class AddMaintenanceRequirementRequest:
    maintenance_plan_id: UUID
    title: str
    description: str
    maintenance_type: str
    interval_type: str
    interval_value: int
    due_basis: str
    instructions: str | None = None
    notes: str | None = None

    def validate(self) -> None:
        if not isinstance(self.maintenance_plan_id, UUID):
            raise ValidationException("maintenance_plan_id must be UUID")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationException("title must be a non-empty string")
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValidationException("description must be a non-empty string")
        if not isinstance(self.maintenance_type, str) or not self.maintenance_type.strip():
            raise ValidationException("maintenance_type must be a non-empty string")
        if not isinstance(self.interval_type, str) or not self.interval_type.strip():
            raise ValidationException("interval_type must be a non-empty string")
        if not isinstance(self.interval_value, int) or self.interval_value <= 0:
            raise ValidationException("interval_value must be a positive int")
        if not isinstance(self.due_basis, str) or not self.due_basis.strip():
            raise ValidationException("due_basis must be a non-empty string")
        if self.instructions is not None and not isinstance(self.instructions, str):
            raise ValidationException("instructions must be string or None")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")


@dataclass(frozen=True, slots=True)
class AddMaintenanceRequirementResponse:
    plan: MaintenancePlanResponse


class AddMaintenanceRequirementUseCase:
    """Add maintenance requirement through MaintenancePlan aggregate API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: AddMaintenanceRequirementRequest,
    ) -> AddMaintenanceRequirementResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: MaintenancePlanRepository = uow.maintenance_plan_repository
                plan = repository.get_by_id(request.maintenance_plan_id)
                if plan is None:
                    raise BusinessRuleViolation(
                        f"Maintenance plan {request.maintenance_plan_id} does not exist"
                    )

                requirement = MaintenanceRequirement(
                    id=uuid4(),
                    title=request.title,
                    description=request.description,
                    maintenance_target=plan.maintenance_target,
                    maintenance_type=_parse_maintenance_type(request.maintenance_type),
                    interval=MaintenanceInterval(
                        interval_type=_parse_interval_type(request.interval_type),
                        interval_value=request.interval_value,
                    ),
                    due_basis=_parse_due_basis(request.due_basis),
                    instructions=request.instructions,
                    notes=request.notes,
                )

                plan.add_requirement(requirement)
                repository.update(plan)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Add maintenance requirement failed") from exc

        return AddMaintenanceRequirementResponse(plan=to_plan_response(plan))
