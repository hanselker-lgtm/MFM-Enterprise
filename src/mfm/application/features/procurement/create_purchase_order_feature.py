"""Create purchase order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.procurement.create_purchase_order import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.procurement.create_purchase_order import (
    CreatePurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.create_purchase_order import (
    CreatePurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.create_purchase_order import (
    CreatePurchaseOrderUseCase,
)
from mfm.application.procurement.create_purchase_order import (
    PurchaseOrderLineInput as ServicePurchaseOrderLineInput,
)
from mfm.application.procurement.create_purchase_order import (
    PurchaseOrderLineResponse as ServicePurchaseOrderLineResponse,
)
from mfm.application.procurement.create_purchase_order import (
    PurchaseOrderResponse as ServicePurchaseOrderResponse,
)
from mfm.application.procurement.create_purchase_order import (
    PurchaseReceiptLineResponse as ServicePurchaseReceiptLineResponse,
)
from mfm.application.procurement.create_purchase_order import (
    PurchaseReceiptResponse as ServicePurchaseReceiptResponse,
)
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for procurement feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class PurchaseOrderLineInput:
    description_snapshot: str
    quantity: Decimal | str | int
    unit_price_amount: Decimal | str | int
    inventory_item_reference: str | None = None
    expected_delivery_at: datetime | None = None
    line_note: str | None = None
    line_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.description_snapshot, str) or not self.description_snapshot.strip():
            raise ValidationException(
                f"{field_name}.description_snapshot must be a non-empty string"
            )
        if isinstance(self.quantity, bool) or isinstance(self.quantity, float):
            raise ValidationException(f"{field_name}.quantity must not be bool/float")
        if isinstance(self.unit_price_amount, bool) or isinstance(
            self.unit_price_amount,
            float,
        ):
            raise ValidationException(
                f"{field_name}.unit_price_amount must not be bool/float"
            )
        if self.inventory_item_reference is not None and not isinstance(
            self.inventory_item_reference,
            str,
        ):
            raise ValidationException(
                f"{field_name}.inventory_item_reference must be string or None"
            )
        if self.expected_delivery_at is not None and not isinstance(
            self.expected_delivery_at,
            datetime,
        ):
            raise ValidationException(
                f"{field_name}.expected_delivery_at must be datetime or None"
            )
        if self.line_note is not None and not isinstance(self.line_note, str):
            raise ValidationException(f"{field_name}.line_note must be string or None")
        if self.line_id is not None and not isinstance(self.line_id, UUID):
            raise ValidationException(f"{field_name}.line_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class PurchaseReceiptLineInput:
    purchase_order_line_id: UUID
    quantity: Decimal | str | int

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.purchase_order_line_id, UUID):
            raise ValidationException(f"{field_name}.purchase_order_line_id must be UUID")
        if isinstance(self.quantity, bool) or isinstance(self.quantity, float):
            raise ValidationException(f"{field_name}.quantity must not be bool/float")


@dataclass(frozen=True, slots=True)
class PurchaseOrderLineResponse:
    purchase_order_line_id: UUID
    description_snapshot: str
    quantity: Decimal
    unit_price_amount: Decimal
    unit_price_currency: str
    line_total_amount: Decimal
    received_quantity: Decimal
    outstanding_quantity: Decimal
    inventory_item_reference: str | None
    expected_delivery_at: datetime | None
    line_note: str | None


@dataclass(frozen=True, slots=True)
class PurchaseReceiptLineResponse:
    purchase_order_line_id: UUID
    quantity: Decimal


@dataclass(frozen=True, slots=True)
class PurchaseReceiptResponse:
    purchase_receipt_id: UUID
    receipt_reference: str
    received_at: datetime
    lines: tuple[PurchaseReceiptLineResponse, ...]


@dataclass(frozen=True, slots=True)
class PurchaseOrderResponse:
    purchase_order_id: UUID
    purchase_order_number: str
    supplier_reference: str
    status: str
    currency: str
    created_at: datetime
    supplier_name_snapshot: str | None
    supplier_contact_snapshot: str | None
    notes: str | None
    requested_by_reference: str | None
    approved_by_reference: str | None
    approved_at: datetime | None
    ordered_at: datetime | None
    external_order_reference: str | None
    cancelled_at: datetime | None
    cancellation_reason: str | None
    order_total_amount: Decimal
    received_total_amount: Decimal
    lines: tuple[PurchaseOrderLineResponse, ...]
    receipts: tuple[PurchaseReceiptResponse, ...]


@dataclass(frozen=True, slots=True)
class CreatePurchaseOrderRequest:
    purchase_order_number: str
    supplier_reference: str
    currency: str
    created_at: datetime
    lines: tuple[PurchaseOrderLineInput, ...]
    purchase_order_id: UUID | None = None
    supplier_name_snapshot: str | None = None
    supplier_contact_snapshot: str | None = None
    notes: str | None = None
    requested_by_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.purchase_order_number, str) or not self.purchase_order_number.strip():
            raise ValidationException("purchase_order_number must be a non-empty string")
        if not isinstance(self.supplier_reference, str) or not self.supplier_reference.strip():
            raise ValidationException("supplier_reference must be a non-empty string")
        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValidationException("currency must be a non-empty string")
        if not isinstance(self.created_at, datetime):
            raise ValidationException("created_at must be datetime")
        if self.purchase_order_id is not None and not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID or None")
        if self.supplier_name_snapshot is not None and not isinstance(
            self.supplier_name_snapshot,
            str,
        ):
            raise ValidationException("supplier_name_snapshot must be string or None")
        if self.supplier_contact_snapshot is not None and not isinstance(
            self.supplier_contact_snapshot,
            str,
        ):
            raise ValidationException("supplier_contact_snapshot must be string or None")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if self.requested_by_reference is not None and not isinstance(
            self.requested_by_reference,
            str,
        ):
            raise ValidationException("requested_by_reference must be string or None")
        if not isinstance(self.lines, tuple):
            raise ValidationException("lines must be tuple")
        for index, line in enumerate(self.lines):
            line.validate(field_name=f"lines[{index}]")


@dataclass(frozen=True, slots=True)
class CreatePurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class CreatePurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_purchase_order_line_input(
    value: PurchaseOrderLineInput,
) -> ServicePurchaseOrderLineInput:
    return ServicePurchaseOrderLineInput(
        description_snapshot=value.description_snapshot,
        quantity=value.quantity,
        unit_price_amount=value.unit_price_amount,
        inventory_item_reference=value.inventory_item_reference,
        expected_delivery_at=value.expected_delivery_at,
        line_note=value.line_note,
        line_id=value.line_id,
    )


def to_feature_purchase_order_line_response(
    response: ServicePurchaseOrderLineResponse,
) -> PurchaseOrderLineResponse:
    return PurchaseOrderLineResponse(
        purchase_order_line_id=response.purchase_order_line_id,
        description_snapshot=response.description_snapshot,
        quantity=response.quantity,
        unit_price_amount=response.unit_price_amount,
        unit_price_currency=response.unit_price_currency,
        line_total_amount=response.line_total_amount,
        received_quantity=response.received_quantity,
        outstanding_quantity=response.outstanding_quantity,
        inventory_item_reference=response.inventory_item_reference,
        expected_delivery_at=response.expected_delivery_at,
        line_note=response.line_note,
    )


def to_feature_purchase_receipt_line_response(
    response: ServicePurchaseReceiptLineResponse,
) -> PurchaseReceiptLineResponse:
    return PurchaseReceiptLineResponse(
        purchase_order_line_id=response.purchase_order_line_id,
        quantity=response.quantity,
    )


def to_feature_purchase_receipt_response(
    response: ServicePurchaseReceiptResponse,
) -> PurchaseReceiptResponse:
    return PurchaseReceiptResponse(
        purchase_receipt_id=response.purchase_receipt_id,
        receipt_reference=response.receipt_reference,
        received_at=response.received_at,
        lines=tuple(
            to_feature_purchase_receipt_line_response(item)
            for item in response.lines
        ),
    )


def to_feature_purchase_order_response(
    response: ServicePurchaseOrderResponse,
) -> PurchaseOrderResponse:
    return PurchaseOrderResponse(
        purchase_order_id=response.purchase_order_id,
        purchase_order_number=response.purchase_order_number,
        supplier_reference=response.supplier_reference,
        status=response.status,
        currency=response.currency,
        created_at=response.created_at,
        supplier_name_snapshot=response.supplier_name_snapshot,
        supplier_contact_snapshot=response.supplier_contact_snapshot,
        notes=response.notes,
        requested_by_reference=response.requested_by_reference,
        approved_by_reference=response.approved_by_reference,
        approved_at=response.approved_at,
        ordered_at=response.ordered_at,
        external_order_reference=response.external_order_reference,
        cancelled_at=response.cancelled_at,
        cancellation_reason=response.cancellation_reason,
        order_total_amount=response.order_total_amount,
        received_total_amount=response.received_total_amount,
        lines=tuple(
            to_feature_purchase_order_line_response(item)
            for item in response.lines
        ),
        receipts=tuple(
            to_feature_purchase_receipt_response(item)
            for item in response.receipts
        ),
    )


class CreatePurchaseOrderFeature:
    """Feature facade for purchase order creation."""

    def __init__(self, *, service: CreatePurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: CreatePurchaseOrderRequest) -> CreatePurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_number=request.purchase_order_number,
                    supplier_reference=request.supplier_reference,
                    currency=request.currency,
                    created_at=request.created_at,
                    lines=tuple(
                        to_service_purchase_order_line_input(item)
                        for item in request.lines
                    ),
                    purchase_order_id=request.purchase_order_id,
                    supplier_name_snapshot=request.supplier_name_snapshot,
                    supplier_contact_snapshot=request.supplier_contact_snapshot,
                    notes=request.notes,
                    requested_by_reference=request.requested_by_reference,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create purchase order feature failed") from exc

        return CreatePurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
