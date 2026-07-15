"""Record purchase receipt feature facade following Public API Standard."""

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
    PurchaseReceiptLineInput,
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
    PurchaseReceiptLineInput as ServicePurchaseReceiptLineInput,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptRequest as ServiceRequest,
)
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptResponse as ServiceResponse,
)
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptUseCase,
)


@dataclass(frozen=True, slots=True)
class RecordPurchaseReceiptRequest:
    purchase_order_id: UUID
    receipt_reference: str
    received_at: datetime
    lines: tuple[PurchaseReceiptLineInput, ...]

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if not isinstance(self.receipt_reference, str) or not self.receipt_reference.strip():
            raise ValidationException("receipt_reference must be a non-empty string")
        if not isinstance(self.received_at, datetime):
            raise ValidationException("received_at must be datetime")
        if not isinstance(self.lines, tuple) or not self.lines:
            raise ValidationException("lines must be a non-empty tuple")
        for index, line in enumerate(self.lines):
            line.validate(field_name=f"lines[{index}]")


@dataclass(frozen=True, slots=True)
class RecordPurchaseReceiptResponse:
    purchase_order: PurchaseOrderResponse


class RecordPurchaseReceiptService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_purchase_receipt_line_input(
    value: PurchaseReceiptLineInput,
) -> ServicePurchaseReceiptLineInput:
    return ServicePurchaseReceiptLineInput(
        purchase_order_line_id=value.purchase_order_line_id,
        quantity=value.quantity,
    )


class RecordPurchaseReceiptFeature:
    """Feature facade for purchase receipt recording."""

    def __init__(self, *, service: RecordPurchaseReceiptService) -> None:
        self._service = service

    def execute(self, request: RecordPurchaseReceiptRequest) -> RecordPurchaseReceiptResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    receipt_reference=request.receipt_reference,
                    received_at=request.received_at,
                    lines=tuple(
                        to_service_purchase_receipt_line_input(item)
                        for item in request.lines
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Record purchase receipt feature failed") from exc

        return RecordPurchaseReceiptResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
