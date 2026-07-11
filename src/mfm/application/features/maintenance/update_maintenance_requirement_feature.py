"""Update maintenance requirement feature facade following Public API Standard."""

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
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    ValidationException as ServiceValidationException,
)
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementRequest as ServiceRequest,
)
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementResponse as ServiceResponse,
)
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementUseCase,
)


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


class UpdateMaintenanceRequirementService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateMaintenanceRequirementFeature:
    """Feature facade for updating maintenance requirements."""

    def __init__(self, *, service: UpdateMaintenanceRequirementService) -> None:
        self._service = service

    def execute(
        self,
        request: UpdateMaintenanceRequirementRequest,
    ) -> UpdateMaintenanceRequirementResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    maintenance_plan_id=request.maintenance_plan_id,
                    maintenance_requirement_id=request.maintenance_requirement_id,
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
                "Update maintenance requirement feature failed"
            ) from exc

        return UpdateMaintenanceRequirementResponse(
            plan=to_feature_plan_response(service_response.plan)
        )
