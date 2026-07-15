"""Cancel purchase order feature facade following Public API Standard."""

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
from mfm.application.procurement.cancel_purchase_order import (
    CancelPurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.cancel_purchase_order import (
    CancelPurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.cancel_purchase_order import CancelPurchaseOrderUseCase
from mfm.application.procurement.create_purchase_order import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)


@dataclass(frozen=True, slots=True)
class CancelPurchaseOrderRequest:
    purchase_order_id: UUID
    cancelled_at: datetime
    cancelled_by_reference: str | None = None
    cancellation_reason: str | None = None

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.cancelled_at, datetime):
            raise ValidationException("cancelled_at must be datetime")
        if self.cancelled_by_reference is not None and not isinstance(
            self.cancelled_by_reference,
            str,
        ):
            raise ValidationException("cancelled_by_reference must be string or None")
        if self.cancellation_reason is not None and not isinstance(
            self.cancellation_reason,
            str,
        ):
            raise ValidationException("cancellation_reason must be string or None")


@dataclass(frozen=True, slots=True)
class CancelPurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class CancelPurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CancelPurchaseOrderFeature:
    """Feature facade for purchase order cancellation."""

    def __init__(self, *, service: CancelPurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: CancelPurchaseOrderRequest) -> CancelPurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    cancelled_at=request.cancelled_at,
                    cancelled_by_reference=request.cancelled_by_reference,
                    cancellation_reason=request.cancellation_reason,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Cancel purchase order feature failed") from exc

        return CancelPurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
