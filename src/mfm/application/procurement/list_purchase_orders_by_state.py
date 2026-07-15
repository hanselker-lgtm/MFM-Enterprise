"""List PurchaseOrders by state use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.procurement.create_purchase_order import ApplicationException
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.create_purchase_order import ValidationException
from mfm.application.procurement.create_purchase_order import to_purchase_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersByStateRequest:
    status: str

    def validate(self) -> None:
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersByStateResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersByStateUseCase:
    """List purchase orders by lifecycle state through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: ListPurchaseOrdersByStateRequest,
    ) -> ListPurchaseOrdersByStateResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                orders = repository.list_by_state(request.status)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("List purchase orders by state failed") from exc

        return ListPurchaseOrdersByStateResponse(
            purchase_orders=tuple(to_purchase_order_response(item) for item in orders)
        )
