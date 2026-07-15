"""Submit purchase order feature facade following Public API Standard."""

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
from mfm.application.procurement.submit_purchase_order import (
    SubmitPurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.submit_purchase_order import (
    SubmitPurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.submit_purchase_order import SubmitPurchaseOrderUseCase


@dataclass(frozen=True, slots=True)
class SubmitPurchaseOrderRequest:
    purchase_order_id: UUID
    submitted_at: datetime

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.submitted_at, datetime):
            raise ValidationException("submitted_at must be datetime")


@dataclass(frozen=True, slots=True)
class SubmitPurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class SubmitPurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class SubmitPurchaseOrderFeature:
    """Feature facade for purchase order submission."""

    def __init__(self, *, service: SubmitPurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: SubmitPurchaseOrderRequest) -> SubmitPurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    submitted_at=request.submitted_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Submit purchase order feature failed") from exc

        return SubmitPurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
