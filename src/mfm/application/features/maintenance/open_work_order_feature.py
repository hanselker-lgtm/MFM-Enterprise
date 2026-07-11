"""Open work order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
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
from mfm.application.maintenance.open_work_order import OpenWorkOrderRequest as ServiceRequest
from mfm.application.maintenance.open_work_order import OpenWorkOrderResponse as ServiceResponse
from mfm.application.maintenance.open_work_order import OpenWorkOrderUseCase


@dataclass(frozen=True, slots=True)
class OpenWorkOrderRequest:
    work_order_id: UUID

    def validate(self) -> None:
        if not isinstance(self.work_order_id, UUID):
            raise ValidationException("work_order_id must be UUID")


@dataclass(frozen=True, slots=True)
class OpenWorkOrderResponse:
    work_order: WorkOrderResponse


class OpenWorkOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class OpenWorkOrderFeature:
    """Feature facade for opening work orders."""

    def __init__(self, *, service: OpenWorkOrderService) -> None:
        self._service = service

    def execute(self, request: OpenWorkOrderRequest) -> OpenWorkOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(work_order_id=request.work_order_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Open work order feature failed") from exc

        return OpenWorkOrderResponse(
            work_order=to_feature_work_order_response(service_response.work_order)
        )
