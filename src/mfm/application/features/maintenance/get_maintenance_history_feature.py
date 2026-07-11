"""Get maintenance history feature facade following Public API Standard."""

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
    MaintenanceRecordResponse,
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
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    to_feature_record_response,
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
from mfm.application.maintenance.get_maintenance_history import (
    GetMaintenanceHistoryRequest as ServiceRequest,
)
from mfm.application.maintenance.get_maintenance_history import (
    GetMaintenanceHistoryResponse as ServiceResponse,
)
from mfm.application.maintenance.get_maintenance_history import (
    GetMaintenanceHistoryUseCase,
)


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


class GetMaintenanceHistoryService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetMaintenanceHistoryFeature:
    """Feature facade for maintenance history retrieval."""

    def __init__(self, *, service: GetMaintenanceHistoryService) -> None:
        self._service = service

    def execute(
        self,
        request: GetMaintenanceHistoryRequest,
    ) -> GetMaintenanceHistoryResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    target_type=request.target_type,
                    target_id=request.target_id,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get maintenance history feature failed") from exc

        return GetMaintenanceHistoryResponse(
            target_type=service_response.target_type,
            target_id=service_response.target_id,
            plans=tuple(to_feature_plan_response(item) for item in service_response.plans),
            records=tuple(
                to_feature_record_response(item) for item in service_response.records
            ),
        )
