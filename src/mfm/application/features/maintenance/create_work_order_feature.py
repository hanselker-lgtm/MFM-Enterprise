"""Create work order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    RepositoryException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    ValidationException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    WorkOrderResponse,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    to_feature_work_order_response,
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
from mfm.application.maintenance.create_work_order import (
    CreateWorkOrderRequest as ServiceRequest,
)
from mfm.application.maintenance.create_work_order import (
    CreateWorkOrderResponse as ServiceResponse,
)
from mfm.application.maintenance.create_work_order import CreateWorkOrderUseCase


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


class CreateWorkOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateWorkOrderFeature:
    """Feature facade for work order creation."""

    def __init__(self, *, service: CreateWorkOrderService) -> None:
        self._service = service

    def execute(self, request: CreateWorkOrderRequest) -> CreateWorkOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    maintenance_plan_id=request.maintenance_plan_id,
                    maintenance_requirement_id=request.maintenance_requirement_id,
                    title=request.title,
                    description=request.description,
                    planned_date=request.planned_date,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create work order feature failed") from exc

        return CreateWorkOrderResponse(
            work_order=to_feature_work_order_response(service_response.work_order)
        )
