"""Calculate due maintenance feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    MaintenanceRequirementResponse,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    RepositoryException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    ValidationException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    to_feature_requirement_response,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceRequest as ServiceRequest,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceResponse as ServiceResponse,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceUseCase,
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


class CalculateDueMaintenanceService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CalculateDueMaintenanceFeature:
    """Feature facade for due maintenance calculations."""

    def __init__(self, *, service: CalculateDueMaintenanceService) -> None:
        self._service = service

    def execute(
        self,
        request: CalculateDueMaintenanceRequest,
    ) -> CalculateDueMaintenanceResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    maintenance_plan_id=request.maintenance_plan_id,
                    as_of_date=request.as_of_date,
                    running_hours_by_requirement_id=request.running_hours_by_requirement_id,
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
                "Calculate due maintenance feature failed"
            ) from exc

        return CalculateDueMaintenanceResponse(
            due_requirements=tuple(
                to_feature_requirement_response(item)
                for item in service_response.due_requirements
            )
        )
