"""List purchase orders by supplier feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.features.procurement.create_purchase_order_feature import (
    PurchaseOrderResponse,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    RepositoryException,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    ValidationException,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    to_feature_purchase_order_response,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierRequest as ServiceRequest,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierResponse as ServiceResponse,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierUseCase,
)


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersBySupplierRequest:
    supplier_reference: str

    def validate(self) -> None:
        if not isinstance(self.supplier_reference, str) or not self.supplier_reference.strip():
            raise ValidationException("supplier_reference must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersBySupplierResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersBySupplierService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListPurchaseOrdersBySupplierFeature:
    """Feature facade for purchase order list-by-supplier."""

    def __init__(self, *, service: ListPurchaseOrdersBySupplierService) -> None:
        self._service = service

    def execute(
        self,
        request: ListPurchaseOrdersBySupplierRequest,
    ) -> ListPurchaseOrdersBySupplierResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(supplier_reference=request.supplier_reference)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List purchase orders by supplier feature failed") from exc

        return ListPurchaseOrdersBySupplierResponse(
            purchase_orders=tuple(
                to_feature_purchase_order_response(item)
                for item in service_response.purchase_orders
            )
        )
