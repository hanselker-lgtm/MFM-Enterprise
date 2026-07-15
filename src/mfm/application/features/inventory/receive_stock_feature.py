"""Receive stock feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.features.inventory.create_inventory_item_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    InventoryItemResponse,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    RepositoryException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    StockLocationInput,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    ValidationException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    to_feature_inventory_item_response,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    to_service_stock_location_input,
)
from mfm.application.inventory.create_inventory_item import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.create_inventory_item import (
    ValidationException as ServiceValidationException,
)
from mfm.application.inventory.receive_stock import ReceiveStockRequest as ServiceRequest
from mfm.application.inventory.receive_stock import ReceiveStockResponse as ServiceResponse
from mfm.application.inventory.receive_stock import ReceiveStockUseCase


@dataclass(frozen=True, slots=True)
class ReceiveStockRequest:
    inventory_item_id: UUID
    location: StockLocationInput
    quantity: Decimal | str | int
    occurred_at: datetime
    external_reference: str | None = None
    note: str | None = None

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")
        self.location.validate(field_name="location")
        if isinstance(self.quantity, bool) or isinstance(self.quantity, float):
            raise ValidationException("quantity must be Decimal, str, or int")
        if not isinstance(self.occurred_at, datetime):
            raise ValidationException("occurred_at must be datetime")
        if self.external_reference is not None and not isinstance(self.external_reference, str):
            raise ValidationException("external_reference must be string or None")
        if self.note is not None and not isinstance(self.note, str):
            raise ValidationException("note must be string or None")


@dataclass(frozen=True, slots=True)
class ReceiveStockResponse:
    inventory_item: InventoryItemResponse


class ReceiveStockService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ReceiveStockFeature:
    """Feature facade for inventory stock receipt."""

    def __init__(self, *, service: ReceiveStockService) -> None:
        self._service = service

    def execute(self, request: ReceiveStockRequest) -> ReceiveStockResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    inventory_item_id=request.inventory_item_id,
                    location=to_service_stock_location_input(request.location),
                    quantity=request.quantity,
                    occurred_at=request.occurred_at,
                    external_reference=request.external_reference,
                    note=request.note,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Receive stock feature failed") from exc

        return ReceiveStockResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
