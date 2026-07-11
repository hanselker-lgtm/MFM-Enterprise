"""Create maintenance plan feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanRequest as ServiceRequest,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanResponse as ServiceResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanUseCase,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenanceIntervalResponse as ServiceIntervalResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenancePlanResponse as ServicePlanResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenanceRecordResponse as ServiceRecordResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenanceRequirementResponse as ServiceRequirementResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    MaintenanceTargetResponse as ServiceTargetResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    PerformerReferenceResponse as ServicePerformerResponse,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    ValidationException as ServiceValidationException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    WorkOrderResponse as ServiceWorkOrderResponse,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class MaintenanceTargetResponse:
    target_type: str
    target_id: UUID


@dataclass(frozen=True, slots=True)
class MaintenanceIntervalResponse:
    interval_type: str
    interval_value: int


@dataclass(frozen=True, slots=True)
class MaintenanceRequirementResponse:
    id: UUID
    title: str
    description: str
    target_type: str
    target_id: UUID
    maintenance_type: str
    interval: MaintenanceIntervalResponse
    due_basis: str
    last_completed_date: date | None
    last_completed_running_hours: int | None
    next_due_date: date | None
    next_due_running_hours: int | None
    status: str
    instructions: str | None
    notes: str | None


@dataclass(frozen=True, slots=True)
class MaintenancePlanResponse:
    id: UUID
    target: MaintenanceTargetResponse
    status: str
    requirements: tuple[MaintenanceRequirementResponse, ...]


@dataclass(frozen=True, slots=True)
class PerformerReferenceResponse:
    performer_type: str
    performer_id_or_external_key: str
    display_name_snapshot: str | None


@dataclass(frozen=True, slots=True)
class MaintenanceRecordResponse:
    id: UUID
    work_order_id: UUID
    maintenance_requirement_id: UUID | None
    target_type: str
    target_id: UUID
    completed_at: datetime
    performer: PerformerReferenceResponse | None
    notes: str | None
    finding: str | None
    replacement_may_be_required: bool


@dataclass(frozen=True, slots=True)
class WorkOrderResponse:
    id: UUID
    maintenance_requirement_id: UUID | None
    target_type: str
    target_id: UUID
    title: str
    description: str
    status: str
    planned_date: date | None
    started_at: datetime | None
    completed_at: datetime | None
    performed_by: PerformerReferenceResponse | None
    notes: str | None
    maintenance_record: MaintenanceRecordResponse | None


@dataclass(frozen=True, slots=True)
class CreateMaintenancePlanRequest:
    target_type: str
    target_id: UUID

    def validate(self) -> None:
        if not isinstance(self.target_type, str) or not self.target_type.strip():
            raise ValidationException("target_type must be a non-empty string")
        if not isinstance(self.target_id, UUID):
            raise ValidationException("target_id must be UUID")


@dataclass(frozen=True, slots=True)
class CreateMaintenancePlanResponse:
    plan: MaintenancePlanResponse


class CreateMaintenancePlanService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_feature_target_response(response: ServiceTargetResponse) -> MaintenanceTargetResponse:
    return MaintenanceTargetResponse(
        target_type=response.target_type,
        target_id=response.target_id,
    )


def to_feature_interval_response(
    response: ServiceIntervalResponse,
) -> MaintenanceIntervalResponse:
    return MaintenanceIntervalResponse(
        interval_type=response.interval_type,
        interval_value=response.interval_value,
    )


def to_feature_requirement_response(
    response: ServiceRequirementResponse,
) -> MaintenanceRequirementResponse:
    return MaintenanceRequirementResponse(
        id=response.id,
        title=response.title,
        description=response.description,
        target_type=response.target_type,
        target_id=response.target_id,
        maintenance_type=response.maintenance_type,
        interval=to_feature_interval_response(response.interval),
        due_basis=response.due_basis,
        last_completed_date=response.last_completed_date,
        last_completed_running_hours=response.last_completed_running_hours,
        next_due_date=response.next_due_date,
        next_due_running_hours=response.next_due_running_hours,
        status=response.status,
        instructions=response.instructions,
        notes=response.notes,
    )


def to_feature_plan_response(response: ServicePlanResponse) -> MaintenancePlanResponse:
    return MaintenancePlanResponse(
        id=response.id,
        target=to_feature_target_response(response.target),
        status=response.status,
        requirements=tuple(
            to_feature_requirement_response(item) for item in response.requirements
        ),
    )


def to_feature_performer_response(
    response: ServicePerformerResponse | None,
) -> PerformerReferenceResponse | None:
    if response is None:
        return None

    return PerformerReferenceResponse(
        performer_type=response.performer_type,
        performer_id_or_external_key=response.performer_id_or_external_key,
        display_name_snapshot=response.display_name_snapshot,
    )


def to_feature_record_response(response: ServiceRecordResponse) -> MaintenanceRecordResponse:
    return MaintenanceRecordResponse(
        id=response.id,
        work_order_id=response.work_order_id,
        maintenance_requirement_id=response.maintenance_requirement_id,
        target_type=response.target_type,
        target_id=response.target_id,
        completed_at=response.completed_at,
        performer=to_feature_performer_response(response.performer),
        notes=response.notes,
        finding=response.finding,
        replacement_may_be_required=response.replacement_may_be_required,
    )


def to_feature_work_order_response(response: ServiceWorkOrderResponse) -> WorkOrderResponse:
    return WorkOrderResponse(
        id=response.id,
        maintenance_requirement_id=response.maintenance_requirement_id,
        target_type=response.target_type,
        target_id=response.target_id,
        title=response.title,
        description=response.description,
        status=response.status,
        planned_date=response.planned_date,
        started_at=response.started_at,
        completed_at=response.completed_at,
        performed_by=to_feature_performer_response(response.performed_by),
        notes=response.notes,
        maintenance_record=(
            to_feature_record_response(response.maintenance_record)
            if response.maintenance_record is not None
            else None
        ),
    )


class CreateMaintenancePlanFeature:
    """Feature facade for maintenance plan creation."""

    def __init__(self, *, service: CreateMaintenancePlanService) -> None:
        self._service = service

    def execute(self, request: CreateMaintenancePlanRequest) -> CreateMaintenancePlanResponse:
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
            raise RepositoryException("Create maintenance plan feature failed") from exc

        return CreateMaintenancePlanResponse(
            plan=to_feature_plan_response(service_response.plan)
        )
