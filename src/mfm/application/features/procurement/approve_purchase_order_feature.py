"""Approve purchase order feature facade following Public API Standard."""

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
from mfm.application.procurement.approve_purchase_order import (
    ApprovePurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.approve_purchase_order import (
    ApprovePurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.approve_purchase_order import ApprovePurchaseOrderUseCase
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
class ApprovePurchaseOrderRequest:
    purchase_order_id: UUID
    approved_at: datetime
    approved_by_reference: str

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.approved_at, datetime):
            raise ValidationException("approved_at must be datetime")
        if not isinstance(self.approved_by_reference, str) or not self.approved_by_reference.strip():
            raise ValidationException("approved_by_reference must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ApprovePurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class ApprovePurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ApprovePurchaseOrderFeature:
    """Feature facade for purchase order approval."""

    def __init__(self, *, service: ApprovePurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: ApprovePurchaseOrderRequest) -> ApprovePurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    approved_at=request.approved_at,
                    approved_by_reference=request.approved_by_reference,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Approve purchase order feature failed") from exc

        return ApprovePurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
