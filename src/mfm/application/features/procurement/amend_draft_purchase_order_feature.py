"""Amend draft purchase order feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.features.procurement.create_purchase_order_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    PurchaseOrderLineInput,
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
from mfm.application.features.procurement.create_purchase_order_feature import (
    to_service_purchase_order_line_input,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderRequest as ServiceRequest,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderResponse as ServiceResponse,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderUseCase,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    PurchaseOrderLineUpdateInput as ServicePurchaseOrderLineUpdateInput,
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


class AmendDraftPurchaseOrderService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_purchase_order_line_update_input(
    value: PurchaseOrderLineUpdateInput,
) -> ServicePurchaseOrderLineUpdateInput:
    return ServicePurchaseOrderLineUpdateInput(
        purchase_order_line_id=value.purchase_order_line_id,
        description_snapshot=value.description_snapshot,
        quantity=value.quantity,
        unit_price_amount=value.unit_price_amount,
        inventory_item_reference=value.inventory_item_reference,
        expected_delivery_at=value.expected_delivery_at,
        line_note=value.line_note,
    )


class AmendDraftPurchaseOrderFeature:
    """Feature facade for draft purchase order amendments."""

    def __init__(self, *, service: AmendDraftPurchaseOrderService) -> None:
        self._service = service

    def execute(self, request: AmendDraftPurchaseOrderRequest) -> AmendDraftPurchaseOrderResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    purchase_order_id=request.purchase_order_id,
                    supplier_reference=request.supplier_reference,
                    supplier_name_snapshot=request.supplier_name_snapshot,
                    supplier_contact_snapshot=request.supplier_contact_snapshot,
                    notes=request.notes,
                    requested_by_reference=request.requested_by_reference,
                    add_lines=tuple(
                        to_service_purchase_order_line_input(item)
                        for item in request.add_lines
                    ),
                    update_lines=tuple(
                        to_service_purchase_order_line_update_input(item)
                        for item in request.update_lines
                    ),
                    remove_line_ids=request.remove_line_ids,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Amend draft purchase order feature failed") from exc

        return AmendDraftPurchaseOrderResponse(
            purchase_order=to_feature_purchase_order_response(service_response.purchase_order)
        )
