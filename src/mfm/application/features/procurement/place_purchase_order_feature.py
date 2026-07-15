"""Place purchase order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
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
from mfm.application.procurement.place_purchase_order import (
    PlacePurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.place_purchase_order import (
    PlacePurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.place_purchase_order import PlacePurchaseOrderUseCase


@dataclass(frozen=True, slots=True)
class PlacePurchaseOrderRequest:
    purchase_order_id: UUID
    ordered_at: datetime
    external_order_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.ordered_at, datetime):
            raise ValidationException("ordered_at must be datetime")
        if self.external_order_reference is not None and not isinstance(
            self.external_order_reference,
            str,
        ):
            raise ValidationException("external_order_reference must be string or None")


@dataclass(frozen=True, slots=True)
class PlacePurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class PlacePurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class PlacePurchaseOrderFeature:
    """Feature facade for purchase order placement."""

    def __init__(self, *, service: PlacePurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: PlacePurchaseOrderRequest) -> PlacePurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    ordered_at=request.ordered_at,
                    external_order_reference=request.external_order_reference,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Place purchase order feature failed") from exc

        return PlacePurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
