"""Complete work order feature facade following Public API Standard."""

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
from mfm.application.maintenance.complete_work_order import (
    CompleteWorkOrderRequest as ServiceRequest,
)
from mfm.application.maintenance.complete_work_order import (
    CompleteWorkOrderResponse as ServiceResponse,
)
from mfm.application.maintenance.complete_work_order import CompleteWorkOrderUseCase
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
class CompleteWorkOrderRequest:
    work_order_id: UUID
    completed_at: datetime
    performer_type: str | None = None
    performer_id_or_external_key: str | None = None
    performer_display_name_snapshot: str | None = None
    notes: str | None = None
    finding: str | None = None
    replacement_may_be_required: bool = False

    def validate(self) -> None:
        if not isinstance(self.work_order_id, UUID):
            raise ValidationException("work_order_id must be UUID")
        if not isinstance(self.completed_at, datetime):
            raise ValidationException("completed_at must be datetime")

        performer_has_type = self.performer_type is not None
        performer_has_key = self.performer_id_or_external_key is not None
        if performer_has_type != performer_has_key:
            raise ValidationException(
                "performer_type and performer_id_or_external_key must both be set or both be None"
            )

        if self.performer_type is not None and not isinstance(self.performer_type, str):
            raise ValidationException("performer_type must be string or None")
        if self.performer_id_or_external_key is not None and (
            not isinstance(self.performer_id_or_external_key, str)
            or not self.performer_id_or_external_key.strip()
        ):
            raise ValidationException(
                "performer_id_or_external_key must be non-empty string when set"
            )

        if self.performer_display_name_snapshot is not None and not isinstance(
            self.performer_display_name_snapshot,
            str,
        ):
            raise ValidationException(
                "performer_display_name_snapshot must be string or None"
            )
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if self.finding is not None and not isinstance(self.finding, str):
            raise ValidationException("finding must be string or None")
        if not isinstance(self.replacement_may_be_required, bool):
            raise ValidationException("replacement_may_be_required must be bool")


@dataclass(frozen=True, slots=True)
class CompleteWorkOrderResponse:
    work_order: WorkOrderResponse


class CompleteWorkOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CompleteWorkOrderFeature:
    """Feature facade for completing work orders."""

    def __init__(self, *, service: CompleteWorkOrderService) -> None:
        self._service = service

    def execute(self, request: CompleteWorkOrderRequest) -> CompleteWorkOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    work_order_id=request.work_order_id,
                    completed_at=request.completed_at,
                    performer_type=request.performer_type,
                    performer_id_or_external_key=request.performer_id_or_external_key,
                    performer_display_name_snapshot=request.performer_display_name_snapshot,
                    notes=request.notes,
                    finding=request.finding,
                    replacement_may_be_required=request.replacement_may_be_required,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete work order feature failed") from exc

        return CompleteWorkOrderResponse(
            work_order=to_feature_work_order_response(service_response.work_order)
        )
