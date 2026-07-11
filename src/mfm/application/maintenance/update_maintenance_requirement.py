"""Update MaintenanceRequirement use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.maintenance.add_maintenance_requirement import _parse_due_basis
from mfm.application.maintenance.add_maintenance_requirement import _parse_interval_type
from mfm.application.maintenance.add_maintenance_requirement import _parse_maintenance_type
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
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository


@dataclass(frozen=True, slots=True)
class UpdateMaintenanceRequirementRequest:
    maintenance_plan_id: UUID
    maintenance_requirement_id: UUID
    title: str | None = None
    description: str | None = None
    maintenance_type: str | None = None
    interval_type: str | None = None
    interval_value: int | None = None
    due_basis: str | None = None
    instructions: str | None = None
    notes: str | None = None

    def validate(self) -> None:
        if not isinstance(self.maintenance_plan_id, UUID):
            raise ValidationException("maintenance_plan_id must be UUID")
        if not isinstance(self.maintenance_requirement_id, UUID):
            raise ValidationException("maintenance_requirement_id must be UUID")
        if self.title is not None and (
            not isinstance(self.title, str) or not self.title.strip()
        ):
            raise ValidationException("title must be non-empty string or None")
        if self.description is not None and (
            not isinstance(self.description, str) or not self.description.strip()
        ):
            raise ValidationException("description must be non-empty string or None")
        if self.maintenance_type is not None and (
            not isinstance(self.maintenance_type, str) or not self.maintenance_type.strip()
        ):
            raise ValidationException("maintenance_type must be non-empty string or None")
        if self.interval_type is not None and (
            not isinstance(self.interval_type, str) or not self.interval_type.strip()
        ):
            raise ValidationException("interval_type must be non-empty string or None")
        if self.interval_value is not None and (
            not isinstance(self.interval_value, int) or self.interval_value <= 0
        ):
            raise ValidationException("interval_value must be positive int or None")
        if self.due_basis is not None and (
            not isinstance(self.due_basis, str) or not self.due_basis.strip()
        ):
            raise ValidationException("due_basis must be non-empty string or None")

        if (self.interval_type is None) != (self.interval_value is None):
            raise ValidationException(
                "interval_type and interval_value must both be set or both be None"
            )


@dataclass(frozen=True, slots=True)
class UpdateMaintenanceRequirementResponse:
    plan: MaintenancePlanResponse


class UpdateMaintenanceRequirementUseCase:
    """Update maintenance requirement through MaintenancePlan aggregate API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: UpdateMaintenanceRequirementRequest,
    ) -> UpdateMaintenanceRequirementResponse:
        request.validate()

        kwargs: dict[str, object] = {}
        if request.title is not None:
            kwargs["title"] = request.title
        if request.description is not None:
            kwargs["description"] = request.description
        if request.maintenance_type is not None:
            kwargs["maintenance_type"] = _parse_maintenance_type(request.maintenance_type)
        if request.interval_type is not None and request.interval_value is not None:
            kwargs["interval"] = MaintenanceInterval(
                interval_type=_parse_interval_type(request.interval_type),
                interval_value=request.interval_value,
            )
        if request.due_basis is not None:
            kwargs["due_basis"] = _parse_due_basis(request.due_basis)
        if request.instructions is not None:
            kwargs["instructions"] = request.instructions
        if request.notes is not None:
            kwargs["notes"] = request.notes

        try:
            with self._unit_of_work as uow:
                repository: MaintenancePlanRepository = uow.maintenance_plan_repository
                plan = repository.get_by_id(request.maintenance_plan_id)
                if plan is None:
                    raise BusinessRuleViolation(
                        f"Maintenance plan {request.maintenance_plan_id} does not exist"
                    )

                if plan.get_requirement(request.maintenance_requirement_id) is None:
                    raise BusinessRuleViolation(
                        f"Maintenance requirement {request.maintenance_requirement_id} does not exist"
                    )

                plan.update_requirement(request.maintenance_requirement_id, **kwargs)
                repository.update(plan)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update maintenance requirement failed") from exc

        return UpdateMaintenanceRequirementResponse(plan=to_plan_response(plan))
