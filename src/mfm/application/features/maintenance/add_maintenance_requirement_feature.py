"""Add maintenance requirement feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    MaintenancePlanResponse,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    RepositoryException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    ValidationException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    to_feature_plan_response,
)
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementRequest as ServiceRequest,
)
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementResponse as ServiceResponse,
)
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementUseCase,
)
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    ValidationException as ServiceValidationException,
)


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


class AddMaintenanceRequirementService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class AddMaintenanceRequirementFeature:
    """Feature facade for adding maintenance requirements."""

    def __init__(self, *, service: AddMaintenanceRequirementService) -> None:
        self._service = service

    def execute(
        self,
        request: AddMaintenanceRequirementRequest,
    ) -> AddMaintenanceRequirementResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    maintenance_plan_id=request.maintenance_plan_id,
                    title=request.title,
                    description=request.description,
                    maintenance_type=request.maintenance_type,
                    interval_type=request.interval_type,
                    interval_value=request.interval_value,
                    due_basis=request.due_basis,
                    instructions=request.instructions,
                    notes=request.notes,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException(
                "Add maintenance requirement feature failed"
            ) from exc

        return AddMaintenanceRequirementResponse(
            plan=to_feature_plan_response(service_response.plan)
        )
