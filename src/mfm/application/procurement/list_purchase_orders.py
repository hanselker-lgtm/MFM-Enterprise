"""List PurchaseOrders use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.procurement.create_purchase_order import ApplicationException
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.create_purchase_order import to_purchase_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersUseCase:
    """List all purchase orders with repository-provided deterministic ordering."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListPurchaseOrdersRequest) -> ListPurchaseOrdersResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                orders = repository.list()
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List purchase orders failed") from exc

        return ListPurchaseOrdersResponse(
            purchase_orders=tuple(to_purchase_order_response(item) for item in orders)
        )
