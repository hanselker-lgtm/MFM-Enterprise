"""Adjust stock feature facade following Public API Standard."""

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
from mfm.application.inventory.adjust_stock import AdjustStockRequest as ServiceRequest
from mfm.application.inventory.adjust_stock import AdjustStockResponse as ServiceResponse
from mfm.application.inventory.adjust_stock import AdjustStockUseCase
from mfm.application.inventory.create_inventory_item import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.create_inventory_item import (
    ValidationException as ServiceValidationException,
)


@dataclass(frozen=True, slots=True)
class AdjustStockRequest:
    inventory_item_id: UUID
    location: StockLocationInput
    counted_quantity: Decimal | str | int
    reason: str
    occurred_at: datetime
    note: str | None = None

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")
        self.location.validate(field_name="location")
        if isinstance(self.counted_quantity, bool) or isinstance(self.counted_quantity, float):
            raise ValidationException("counted_quantity must be Decimal, str, or int")
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ValidationException("reason must be a non-empty string")
        if not isinstance(self.occurred_at, datetime):
            raise ValidationException("occurred_at must be datetime")
        if self.note is not None and not isinstance(self.note, str):
            raise ValidationException("note must be string or None")


@dataclass(frozen=True, slots=True)
class AdjustStockResponse:
    inventory_item: InventoryItemResponse


class AdjustStockService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class AdjustStockFeature:
    """Feature facade for inventory stock adjustment."""

    def __init__(self, *, service: AdjustStockService) -> None:
        self._service = service

    def execute(self, request: AdjustStockRequest) -> AdjustStockResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    inventory_item_id=request.inventory_item_id,
                    location=to_service_stock_location_input(request.location),
                    counted_quantity=request.counted_quantity,
                    reason=request.reason,
                    occurred_at=request.occurred_at,
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
            raise RepositoryException("Adjust stock feature failed") from exc

        return AdjustStockResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
