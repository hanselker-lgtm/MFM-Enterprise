"""List purchase orders by state feature facade following Public API Standard."""

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
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateRequest as ServiceRequest,
)
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateResponse as ServiceResponse,
)
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateUseCase,
)


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersByStateRequest:
    status: str

    def validate(self) -> None:
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ListPurchaseOrdersByStateResponse:
    purchase_orders: tuple[PurchaseOrderResponse, ...]


class ListPurchaseOrdersByStateService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListPurchaseOrdersByStateFeature:
    """Feature facade for purchase order list-by-state."""

    def __init__(self, *, service: ListPurchaseOrdersByStateService) -> None:
        self._service = service

    def execute(
        self,
        request: ListPurchaseOrdersByStateRequest,
    ) -> ListPurchaseOrdersByStateResponse:
        request.validate()

        try:
            service_response = self._service.execute(ServiceRequest(status=request.status))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List purchase orders by state feature failed") from exc

        return ListPurchaseOrdersByStateResponse(
            purchase_orders=tuple(
                to_feature_purchase_order_response(item)
                for item in service_response.purchase_orders
            )
        )
