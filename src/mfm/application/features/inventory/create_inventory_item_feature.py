"""Create inventory item feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.inventory.create_inventory_item import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.inventory.create_inventory_item import (
    CreateInventoryItemRequest as ServiceRequest,
)
from mfm.application.inventory.create_inventory_item import (
    CreateInventoryItemResponse as ServiceResponse,
)
from mfm.application.inventory.create_inventory_item import CreateInventoryItemUseCase
from mfm.application.inventory.create_inventory_item import (
    InventoryItemResponse as ServiceInventoryItemResponse,
)
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.create_inventory_item import (
    StockLocationBalanceResponse as ServiceStockLocationBalanceResponse,
)
from mfm.application.inventory.create_inventory_item import (
    StockLocationInput as ServiceStockLocationInput,
)
from mfm.application.inventory.create_inventory_item import (
    StockMovementResponse as ServiceStockMovementResponse,
)
from mfm.application.inventory.create_inventory_item import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for inventory feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class StockLocationInput:
    location_key: str
    location_name: str
    vessel_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.location_key, str) or not self.location_key.strip():
            raise ValidationException(f"{field_name}.location_key must be a non-empty string")
        if not isinstance(self.location_name, str) or not self.location_name.strip():
            raise ValidationException(f"{field_name}.location_name must be a non-empty string")
        if self.vessel_id is not None and not isinstance(self.vessel_id, UUID):
            raise ValidationException(f"{field_name}.vessel_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class StockLocationBalanceResponse:
    location_key: str
    location_name: str
    vessel_id: UUID | None
    quantity: Decimal


@dataclass(frozen=True, slots=True)
class StockMovementResponse:
    movement_id: UUID
    movement_type: str
    quantity: Decimal
    occurred_at: datetime
    location_key: str
    location_name: str
    vessel_id: UUID | None
    external_reference: str | None
    note: str | None
    reason: str | None


@dataclass(frozen=True, slots=True)
class InventoryItemResponse:
    inventory_item_id: UUID
    item_reference: str
    name: str
    description: str | None
    unit_code: str
    unit_decimal_places: int
    unit_display_name: str | None
    status: str
    total_quantity: Decimal
    minimum_stock_level: Decimal | None
    low_stock: bool
    positions: tuple[StockLocationBalanceResponse, ...]
    movements: tuple[StockMovementResponse, ...]


@dataclass(frozen=True, slots=True)
class CreateInventoryItemRequest:
    item_reference: str
    name: str
    unit_code: str
    unit_decimal_places: int
    inventory_item_id: UUID | None = None
    description: str | None = None
    unit_display_name: str | None = None
    minimum_stock_level: Decimal | str | int | None = None

    def validate(self) -> None:
        if not isinstance(self.item_reference, str) or not self.item_reference.strip():
            raise ValidationException("item_reference must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.unit_code, str) or not self.unit_code.strip():
            raise ValidationException("unit_code must be a non-empty string")
        if not isinstance(self.unit_decimal_places, int) or isinstance(
            self.unit_decimal_places,
            bool,
        ):
            raise ValidationException("unit_decimal_places must be integer")
        if self.inventory_item_id is not None and not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID or None")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.unit_display_name is not None and not isinstance(self.unit_display_name, str):
            raise ValidationException("unit_display_name must be string or None")


@dataclass(frozen=True, slots=True)
class CreateInventoryItemResponse:
    inventory_item: InventoryItemResponse


class CreateInventoryItemService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_stock_location_input(value: StockLocationInput) -> ServiceStockLocationInput:
    return ServiceStockLocationInput(
        location_key=value.location_key,
        location_name=value.location_name,
        vessel_id=value.vessel_id,
    )


def to_feature_stock_location_balance_response(
    response: ServiceStockLocationBalanceResponse,
) -> StockLocationBalanceResponse:
    return StockLocationBalanceResponse(
        location_key=response.location_key,
        location_name=response.location_name,
        vessel_id=response.vessel_id,
        quantity=response.quantity,
    )


def to_feature_stock_movement_response(
    response: ServiceStockMovementResponse,
) -> StockMovementResponse:
    return StockMovementResponse(
        movement_id=response.movement_id,
        movement_type=response.movement_type,
        quantity=response.quantity,
        occurred_at=response.occurred_at,
        location_key=response.location_key,
        location_name=response.location_name,
        vessel_id=response.vessel_id,
        external_reference=response.external_reference,
        note=response.note,
        reason=response.reason,
    )


def to_feature_inventory_item_response(
    response: ServiceInventoryItemResponse,
) -> InventoryItemResponse:
    return InventoryItemResponse(
        inventory_item_id=response.inventory_item_id,
        item_reference=response.item_reference,
        name=response.name,
        description=response.description,
        unit_code=response.unit_code,
        unit_decimal_places=response.unit_decimal_places,
        unit_display_name=response.unit_display_name,
        status=response.status,
        total_quantity=response.total_quantity,
        minimum_stock_level=response.minimum_stock_level,
        low_stock=response.low_stock,
        positions=tuple(
            to_feature_stock_location_balance_response(item)
            for item in response.positions
        ),
        movements=tuple(
            to_feature_stock_movement_response(item)
            for item in response.movements
        ),
    )


class CreateInventoryItemFeature:
    """Feature facade for inventory item creation."""

    def __init__(self, *, service: CreateInventoryItemService) -> None:
        self._service = service

    def execute(self, request: CreateInventoryItemRequest) -> CreateInventoryItemResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    item_reference=request.item_reference,
                    name=request.name,
                    unit_code=request.unit_code,
                    unit_decimal_places=request.unit_decimal_places,
                    inventory_item_id=request.inventory_item_id,
                    description=request.description,
                    unit_display_name=request.unit_display_name,
                    minimum_stock_level=request.minimum_stock_level,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create inventory item feature failed") from exc

        return CreateInventoryItemResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
