"""Complete WorkOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.maintenance.create_maintenance_plan import (
    ApplicationException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_maintenance_plan import parse_performer_type
from mfm.application.maintenance.create_maintenance_plan import WorkOrderResponse
from mfm.application.maintenance.create_maintenance_plan import to_work_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.repositories.work_order_repository import WorkOrderRepository


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


class CompleteWorkOrderUseCase:
    """Complete an in-progress work order through domain lifecycle API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CompleteWorkOrderRequest) -> CompleteWorkOrderResponse:
        request.validate()

        performer = None
        if request.performer_type is not None and request.performer_id_or_external_key is not None:
            performer = PerformerReference(
                performer_type=parse_performer_type(request.performer_type),
                performer_id_or_external_key=request.performer_id_or_external_key,
                display_name_snapshot=request.performer_display_name_snapshot,
            )

        try:
            with self._unit_of_work as uow:
                repository: WorkOrderRepository = uow.work_order_repository
                work_order = repository.get_by_id(request.work_order_id)
                if work_order is None:
                    raise BusinessRuleViolation(
                        f"Work order {request.work_order_id} does not exist"
                    )

                work_order.complete(
                    completed_at=request.completed_at,
                    performed_by=performer,
                    notes=request.notes,
                    finding=request.finding,
                    replacement_may_be_required=request.replacement_may_be_required,
                )
                repository.update(work_order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete work order failed") from exc

        return CompleteWorkOrderResponse(work_order=to_work_order_response(work_order))
