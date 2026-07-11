"""Create MaintenancePlan use case and shared maintenance DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository


class ApplicationException(Exception):
    """Base exception for maintenance application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


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


def to_target_response(target: MaintenanceTarget) -> MaintenanceTargetResponse:
    return MaintenanceTargetResponse(
        target_type=target.target_type.value,
        target_id=target.target_id,
    )


def to_requirement_response(requirement) -> MaintenanceRequirementResponse:
    last_completed_date = None
    last_completed_running_hours = None
    next_due_date = None
    next_due_running_hours = None

    if requirement.due_basis.value == "CALENDAR_DATE":
        last_completed_date = requirement.last_completed
        next_due_date = requirement.next_due
    else:
        last_completed_running_hours = requirement.last_completed
        next_due_running_hours = requirement.next_due

    return MaintenanceRequirementResponse(
        id=requirement.id.value,
        title=requirement.title,
        description=requirement.description,
        target_type=requirement.maintenance_target.target_type.value,
        target_id=requirement.maintenance_target.target_id,
        maintenance_type=requirement.maintenance_type.value,
        interval=MaintenanceIntervalResponse(
            interval_type=requirement.interval.interval_type.value,
            interval_value=requirement.interval.interval_value,
        ),
        due_basis=requirement.due_basis.value,
        last_completed_date=last_completed_date,
        last_completed_running_hours=last_completed_running_hours,
        next_due_date=next_due_date,
        next_due_running_hours=next_due_running_hours,
        status=requirement.status.value,
        instructions=requirement.instructions,
        notes=requirement.notes,
    )


def to_plan_response(plan: MaintenancePlan) -> MaintenancePlanResponse:
    return MaintenancePlanResponse(
        id=plan.id.value,
        target=to_target_response(plan.maintenance_target),
        status=plan.status.value,
        requirements=tuple(to_requirement_response(item) for item in plan.list_requirements()),
    )


def to_performer_response(
    performer: PerformerReference | None,
) -> PerformerReferenceResponse | None:
    if performer is None:
        return None

    return PerformerReferenceResponse(
        performer_type=performer.performer_type.value,
        performer_id_or_external_key=performer.performer_id_or_external_key,
        display_name_snapshot=performer.display_name_snapshot,
    )


def to_record_response(record) -> MaintenanceRecordResponse:
    return MaintenanceRecordResponse(
        id=record.id.value,
        work_order_id=record.work_order_id.value,
        maintenance_requirement_id=(
            record.maintenance_requirement_id.value
            if record.maintenance_requirement_id is not None
            else None
        ),
        target_type=record.maintenance_target.target_type.value,
        target_id=record.maintenance_target.target_id,
        completed_at=record.completed_at,
        performer=to_performer_response(record.performed_by),
        notes=record.notes,
        finding=record.finding,
        replacement_may_be_required=record.replacement_may_be_required,
    )


def to_work_order_response(work_order: WorkOrder) -> WorkOrderResponse:
    return WorkOrderResponse(
        id=work_order.id.value,
        maintenance_requirement_id=(
            work_order.maintenance_requirement_id.value
            if work_order.maintenance_requirement_id is not None
            else None
        ),
        target_type=work_order.maintenance_target.target_type.value,
        target_id=work_order.maintenance_target.target_id,
        title=work_order.title,
        description=work_order.description,
        status=work_order.status.value,
        planned_date=work_order.planned_date,
        started_at=work_order.started_at,
        completed_at=work_order.completed_at,
        performed_by=to_performer_response(work_order.performed_by),
        notes=work_order.notes,
        maintenance_record=(
            to_record_response(work_order.maintenance_record)
            if work_order.maintenance_record is not None
            else None
        ),
    )


def parse_target_type(value: str) -> MaintenanceTargetType:
    try:
        return MaintenanceTargetType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("target_type is invalid") from exc


def parse_performer_type(value: str) -> PerformerReferenceType:
    try:
        return PerformerReferenceType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("performer_type is invalid") from exc


class CreateMaintenancePlanUseCase:
    """Create maintenance plan aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateMaintenancePlanRequest) -> CreateMaintenancePlanResponse:
        request.validate()

        target = MaintenanceTarget(
            target_type=parse_target_type(request.target_type),
            target_id=request.target_id,
        )

        try:
            with self._unit_of_work as uow:
                repository: MaintenancePlanRepository = uow.maintenance_plan_repository

                if repository.get_by_target(target):
                    raise BusinessRuleViolation(
                        "Maintenance plan for target already exists"
                    )

                plan = MaintenancePlan(maintenance_target=target)
                repository.add(plan)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create maintenance plan failed") from exc

        return CreateMaintenancePlanResponse(plan=to_plan_response(plan))
