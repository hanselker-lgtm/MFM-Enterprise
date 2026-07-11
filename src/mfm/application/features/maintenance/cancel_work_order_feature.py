"""Cancel work order feature facade following Public API Standard."""

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
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderRequest as ServiceRequest
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderResponse as ServiceResponse
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderUseCase
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
class CancelWorkOrderRequest:
    work_order_id: UUID
    notes: str | None = None

    def validate(self) -> None:
        if not isinstance(self.work_order_id, UUID):
            raise ValidationException("work_order_id must be UUID")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")


@dataclass(frozen=True, slots=True)
class CancelWorkOrderResponse:
    work_order: WorkOrderResponse


class CancelWorkOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CancelWorkOrderFeature:
    """Feature facade for cancelling work orders."""

    def __init__(self, *, service: CancelWorkOrderService) -> None:
        self._service = service

    def execute(self, request: CancelWorkOrderRequest) -> CancelWorkOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    work_order_id=request.work_order_id,
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
            raise RepositoryException("Cancel work order feature failed") from exc

        return CancelWorkOrderResponse(
            work_order=to_feature_work_order_response(service_response.work_order)
        )
