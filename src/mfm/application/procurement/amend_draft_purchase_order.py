"""Amend draft PurchaseOrder use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.application.procurement.create_purchase_order import ApplicationException
from mfm.application.procurement.create_purchase_order import BusinessRuleViolation
from mfm.application.procurement.create_purchase_order import PurchaseOrderLineInput
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.create_purchase_order import ValidationException
from mfm.application.procurement.create_purchase_order import to_purchase_order_line
from mfm.application.procurement.create_purchase_order import to_purchase_order_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.finance.money import Money
from mfm.domain.procurement.exceptions import ProcurementError
from mfm.domain.procurement.identifiers import PurchaseOrderLineId
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


@dataclass(frozen=True, slots=True)
class PurchaseOrderLineUpdateInput:
    purchase_order_line_id: UUID
    description_snapshot: str | None = None
    quantity: Decimal | str | int | None = None
    unit_price_amount: Decimal | str | int | None = None
    inventory_item_reference: str | None = None
    expected_delivery_at: datetime | None = None
    line_note: str | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.purchase_order_line_id, UUID):
            raise ValidationException(f"{field_name}.purchase_order_line_id must be UUID")
        if self.description_snapshot is not None and (
            not isinstance(self.description_snapshot, str)
            or not self.description_snapshot.strip()
        ):
            raise ValidationException(
                f"{field_name}.description_snapshot must be non-empty string or None"
            )
        if self.quantity is not None and (
            isinstance(self.quantity, bool)
            or isinstance(self.quantity, float)
        ):
            raise ValidationException(f"{field_name}.quantity must not be bool/float")
        if self.unit_price_amount is not None and (
            isinstance(self.unit_price_amount, bool)
            or isinstance(self.unit_price_amount, float)
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


@dataclass(frozen=True, slots=True)
class AmendDraftPurchaseOrderRequest:
    purchase_order_id: UUID
    supplier_reference: str | None = None
    supplier_name_snapshot: str | None = None
    supplier_contact_snapshot: str | None = None
    notes: str | None = None
    requested_by_reference: str | None = None
    add_lines: tuple[PurchaseOrderLineInput, ...] = ()
    update_lines: tuple[PurchaseOrderLineUpdateInput, ...] = ()
    remove_line_ids: tuple[UUID, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.purchase_order_id, UUID):
            raise ValidationException("purchase_order_id must be UUID")
        if self.supplier_reference is not None and not isinstance(
            self.supplier_reference,
            str,
        ):
            raise ValidationException("supplier_reference must be string or None")
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
        if not isinstance(self.add_lines, tuple):
            raise ValidationException("add_lines must be tuple")
        if not isinstance(self.update_lines, tuple):
            raise ValidationException("update_lines must be tuple")
        if not isinstance(self.remove_line_ids, tuple):
            raise ValidationException("remove_line_ids must be tuple")

        for index, line in enumerate(self.add_lines):
            line.validate(field_name=f"add_lines[{index}]")
        for index, line in enumerate(self.update_lines):
            line.validate(field_name=f"update_lines[{index}]")
        for index, line_id in enumerate(self.remove_line_ids):
            if not isinstance(line_id, UUID):
                raise ValidationException(f"remove_line_ids[{index}] must be UUID")


@dataclass(frozen=True, slots=True)
class AmendDraftPurchaseOrderResponse:
    purchase_order: PurchaseOrderResponse


class AmendDraftPurchaseOrderUseCase:
    """Amend draft purchase order through domain APIs."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: AmendDraftPurchaseOrderRequest,
    ) -> AmendDraftPurchaseOrderResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: PurchaseOrderRepository = uow.purchase_order_repository
                order = repository.get_by_id(request.purchase_order_id)
                if order is None:
                    raise BusinessRuleViolation(
                        f"Purchase order {request.purchase_order_id} does not exist"
                    )

                if any(
                    value is not None
                    for value in (
                        request.supplier_reference,
                        request.supplier_name_snapshot,
                        request.supplier_contact_snapshot,
                        request.notes,
                        request.requested_by_reference,
                    )
                ):
                    order.amend_draft(
                        supplier_reference=request.supplier_reference,
                        supplier_name_snapshot=request.supplier_name_snapshot,
                        supplier_contact_snapshot=request.supplier_contact_snapshot,
                        notes=request.notes,
                        requested_by_reference=request.requested_by_reference,
                    )

                for line in request.add_lines:
                    order.add_line(to_purchase_order_line(line, currency=order.currency))

                for line in request.update_lines:
                    changes: dict[str, object] = {}
                    if line.description_snapshot is not None:
                        changes["description_snapshot"] = line.description_snapshot
                    if line.quantity is not None:
                        changes["quantity"] = line.quantity
                    if line.unit_price_amount is not None:
                        changes["unit_price"] = Money(
                            amount=line.unit_price_amount,
                            currency=order.currency,
                        )
                    if line.inventory_item_reference is not None:
                        changes["inventory_item_reference"] = line.inventory_item_reference
                    if line.expected_delivery_at is not None:
                        changes["expected_delivery_at"] = line.expected_delivery_at
                    if line.line_note is not None:
                        changes["line_note"] = line.line_note

                    order.update_line(
                        PurchaseOrderLineId(line.purchase_order_line_id),
                        **changes,
                    )

                for line_id in request.remove_line_ids:
                    order.remove_line(PurchaseOrderLineId(line_id))

                repository.update(order)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProcurementError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Amend draft purchase order failed") from exc

        return AmendDraftPurchaseOrderResponse(
            purchase_order=to_purchase_order_response(order)
        )
