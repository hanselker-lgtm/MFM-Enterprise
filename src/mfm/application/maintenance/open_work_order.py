"""Open WorkOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
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
from mfm.application.maintenance.create_maintenance_plan import WorkOrderResponse
from mfm.application.maintenance.create_maintenance_plan import to_work_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.exceptions import MaintenanceError
from mfm.repositories.work_order_repository import WorkOrderRepository


@dataclass(frozen=True, slots=True)
class OpenWorkOrderRequest:
    work_order_id: UUID

    def validate(self) -> None:
        if not isinstance(self.work_order_id, UUID):
            raise ValidationException("work_order_id must be UUID")


@dataclass(frozen=True, slots=True)
class OpenWorkOrderResponse:
    work_order: WorkOrderResponse


class OpenWorkOrderUseCase:
    """Open a planned work order through domain lifecycle API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: OpenWorkOrderRequest) -> OpenWorkOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: WorkOrderRepository = uow.work_order_repository
                work_order = repository.get_by_id(request.work_order_id)
                if work_order is None:
                    raise BusinessRuleViolation(
                        f"Work order {request.work_order_id} does not exist"
                    )

                work_order.open()
                repository.update(work_order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except MaintenanceError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Open work order failed") from exc

        return OpenWorkOrderResponse(work_order=to_work_order_response(work_order))
