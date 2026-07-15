"""List PurchaseOrders by supplier use case."""

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
class ListPurchaseOrdersBySupplierRequest:
    supplier_reference: str

    def validate(self) -> None:
        if not isinstance(self.supplier_reference, str) or not self.supplier_reference.strip():
            raise ValidationException("supplier_reference must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersBySupplierResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersBySupplierUseCase:
    """List purchase orders by supplier reference through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: ListPurchaseOrdersBySupplierRequest,
    ) -> ListPurchaseOrdersBySupplierResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                orders = repository.list_by_supplier_reference(request.supplier_reference)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("List purchase orders by supplier failed") from exc

        return ListPurchaseOrdersBySupplierResponse(
            purchase_orders=tuple(to_purchase_order_response(item) for item in orders)
        )
