"""Get PurchaseOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.procurement.create_purchase_order import ApplicationException
from mfm.application.procurement.create_purchase_order import BusinessRuleViolation
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.create_purchase_order import ValidationException
from mfm.application.procurement.create_purchase_order import to_purchase_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


@dataclass(frozen=True, slots=True)
class GetPurchaseOrderRequest:
    purchase_order_id: UUID

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetPurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class GetPurchaseOrderUseCase:
    """Load one purchase order through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetPurchaseOrderRequest) -> GetPurchaseOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                order = repository.get_by_id(request.purchase_order_id)
                if order is None:
                    raise BusinessRuleViolation(
                        f"Purchase order {request.purchase_order_id} does not exist"
                    )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get purchase order failed") from exc

        return GetPurchaseOrderResponse(purchase_order=to_purchase_order_response(order))
