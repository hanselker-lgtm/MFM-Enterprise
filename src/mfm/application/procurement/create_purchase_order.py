"""Create PurchaseOrder use case and shared procurement application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
from mfm.domain.procurement.exceptions import ProcurementError
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_receipt import PurchaseReceipt
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


class ApplicationException(Exception):
    """Base exception for procurement application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


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


def to_purchase_order_line(line: PurchaseOrderLineInput, *, currency: Currency) -> PurchaseOrderLine:
    create_kwargs: dict[str, object] = {}
    if line.line_id is not None:
        create_kwargs["id"] = line.line_id

    return PurchaseOrderLine(
        description_snapshot=line.description_snapshot,
        quantity=line.quantity,
        unit_price=Money(amount=line.unit_price_amount, currency=currency),
        inventory_item_reference=line.inventory_item_reference,
        expected_delivery_at=line.expected_delivery_at,
        line_note=line.line_note,
        **create_kwargs,
    )


def to_purchase_order_response(order: PurchaseOrder) -> PurchaseOrderResponse:
    return PurchaseOrderResponse(
        purchase_order_id=order.id.value,
        purchase_order_number=order.purchase_order_number.value,
        supplier_reference=order.supplier_reference.value,
        status=order.status.value,
        currency=order.currency.value,
        created_at=order.created_at,
        supplier_name_snapshot=order.supplier_name_snapshot,
        supplier_contact_snapshot=order.supplier_contact_snapshot,
        notes=order.notes,
        requested_by_reference=order.requested_by_reference,
        approved_by_reference=order.approved_by_reference,
        approved_at=order.approved_at,
        ordered_at=order.ordered_at,
        external_order_reference=order.external_order_reference,
        cancelled_at=order.cancelled_at,
        cancellation_reason=order.cancellation_reason,
        order_total_amount=order.order_total.amount,
        received_total_amount=order.received_total.amount,
        lines=tuple(
            PurchaseOrderLineResponse(
                purchase_order_line_id=line.id.value,
                description_snapshot=line.description_snapshot,
                quantity=line.quantity,
                unit_price_amount=line.unit_price.amount,
                unit_price_currency=line.unit_price.currency.value,
                line_total_amount=line.line_total.amount,
                received_quantity=line.received_quantity,
                outstanding_quantity=line.outstanding_quantity,
                inventory_item_reference=line.inventory_item_reference,
                expected_delivery_at=line.expected_delivery_at,
                line_note=line.line_note,
            )
            for line in order.lines
        ),
        receipts=tuple(
            to_purchase_receipt_response(receipt)
            for receipt in order.receipts
        ),
    )


def to_purchase_receipt_response(receipt: PurchaseReceipt) -> PurchaseReceiptResponse:
    return PurchaseReceiptResponse(
        purchase_receipt_id=receipt.id.value,
        receipt_reference=receipt.receipt_reference,
        received_at=receipt.received_at,
        lines=tuple(
            PurchaseReceiptLineResponse(
                purchase_order_line_id=line.purchase_order_line_id.value,
                quantity=line.quantity,
            )
            for line in receipt.lines
        ),
    )


def to_purchase_receipt_line(line: PurchaseReceiptLineInput) -> PurchaseReceiptLine:
    return PurchaseReceiptLine(
        purchase_order_line_id=line.purchase_order_line_id,
        quantity=line.quantity,
    )


class CreatePurchaseOrderUseCase:
    """Create purchase order aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreatePurchaseOrderRequest) -> CreatePurchaseOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository

                normalized_order_number = request.purchase_order_number.strip()
                if repository.exists_by_number(normalized_order_number):
                    raise BusinessRuleViolation(
                        f"Purchase order number {normalized_order_number} already exists"
                    )

                create_kwargs: dict[str, object] = {}
                if request.purchase_order_id is not None:
                    create_kwargs["id"] = request.purchase_order_id

                currency = Currency(request.currency.strip().upper())
                order = PurchaseOrder(
                    purchase_order_number=request.purchase_order_number,
                    supplier_reference=request.supplier_reference,
                    currency=currency,
                    created_at=request.created_at,
                    lines=[
                        to_purchase_order_line(item, currency=currency)
                        for item in request.lines
                    ],
                    supplier_name_snapshot=request.supplier_name_snapshot,
                    supplier_contact_snapshot=request.supplier_contact_snapshot,
                    notes=request.notes,
                    requested_by_reference=request.requested_by_reference,
                    **create_kwargs,
                )

                repository.add(order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProcurementError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ValueError as exc:
            if "already exists" in str(exc).lower():
                raise BusinessRuleViolation(str(exc)) from exc
            raise RepositoryException("Create purchase order failed") from exc
        except Exception as exc:
            raise RepositoryException("Create purchase order failed") from exc

        return CreatePurchaseOrderResponse(purchase_order=to_purchase_order_response(order))
