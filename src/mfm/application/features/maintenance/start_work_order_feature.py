"""Start work order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
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
from mfm.application.maintenance.start_work_order import StartWorkOrderRequest as ServiceRequest
from mfm.application.maintenance.start_work_order import StartWorkOrderResponse as ServiceResponse
from mfm.application.maintenance.start_work_order import StartWorkOrderUseCase


@dataclass(frozen=True, slots=True)
class StartWorkOrderRequest:
    work_order_id: UUID
    started_at: datetime

    def validate(self) -> None:
        if not isinstance(self.work_order_id, UUID):
            raise ValidationException("work_order_id must be UUID")
        if not isinstance(self.started_at, datetime):
            raise ValidationException("started_at must be datetime")


@dataclass(frozen=True, slots=True)
class StartWorkOrderResponse:
    work_order: WorkOrderResponse


class StartWorkOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class StartWorkOrderFeature:
    """Feature facade for starting work orders."""

    def __init__(self, *, service: StartWorkOrderService) -> None:
        self._service = service

    def execute(self, request: StartWorkOrderRequest) -> StartWorkOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    work_order_id=request.work_order_id,
                    started_at=request.started_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Start work order feature failed") from exc

        return StartWorkOrderResponse(
            work_order=to_feature_work_order_response(service_response.work_order)
        )
