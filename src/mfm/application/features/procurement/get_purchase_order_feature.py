"""Get purchase order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.procurement.create_purchase_order_feature import (
    BusinessRuleViolation,
)
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
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderRequest as ServiceRequest
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderResponse as ServiceResponse
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderUseCase


@dataclass(frozen=True, slots=True)
class GetPurchaseOrderRequest:
    purchase_order_id: UUID

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetPurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class GetPurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetPurchaseOrderFeature:
    """Feature facade for purchase order retrieval."""

    def __init__(self, *, service: GetPurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: GetPurchaseOrderRequest) -> GetPurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(purchase_order_id=request.purchase_order_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get purchase order feature failed") from exc

        return GetPurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
