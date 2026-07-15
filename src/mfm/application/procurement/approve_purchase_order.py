"""Approve PurchaseOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.procurement.create_purchase_order import ApplicationException
from mfm.application.procurement.create_purchase_order import BusinessRuleViolation
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.create_purchase_order import ValidationException
from mfm.application.procurement.create_purchase_order import to_purchase_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.procurement.exceptions import ProcurementError
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


@dataclass(frozen=True, slots=True)
class ApprovePurchaseOrderRequest:
    purchase_order_id: UUID
    approved_at: datetime
    approved_by_reference: str

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.approved_at, datetime):
            raise ValidationException("approved_at must be datetime")
        if not isinstance(self.approved_by_reference, str) or not self.approved_by_reference.strip():
            raise ValidationException("approved_by_reference must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ApprovePurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class ApprovePurchaseOrderUseCase:
    """Approve purchase order through domain lifecycle API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ApprovePurchaseOrderRequest) -> ApprovePurchaseOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                order = repository.get_by_id(request.purchase_order_id)
                if order is None:
                    raise BusinessRuleViolation(
                        f"Purchase order {request.purchase_order_id} does not exist"
                    )

                order.approve(
                    approved_at=request.approved_at,
                    approved_by_reference=request.approved_by_reference,
                )
                repository.update(order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProcurementError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Approve purchase order failed") from exc

        return ApprovePurchaseOrderResponse(purchase_order=to_purchase_order_response(order))
