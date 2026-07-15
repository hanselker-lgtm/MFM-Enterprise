"""List purchase orders feature facade following Public API Standard."""

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
    to_feature_purchase_order_response,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersRequest as ServiceRequest
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersResponse as ServiceResponse
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersUseCase


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListPurchaseOrdersFeature:
    """Feature facade for purchase order listing."""

    def __init__(self, *, service: ListPurchaseOrdersService) -> None:
        self._service = service

    def execute(self, request: ListPurchaseOrdersRequest) -> ListPurchaseOrdersResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List purchase orders feature failed") from exc

        return ListPurchaseOrdersResponse(
            purchase_orders=tuple(
                to_feature_purchase_order_response(item)
                for item in service_response.purchase_orders
            )
        )
