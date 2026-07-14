"""Create Inventory Item use case and shared inventory application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.inventory.exceptions import InventoryError
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement import StockMovement
from mfm.domain.inventory.stock_position import StockPosition
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure
from mfm.repositories.inventory_repository import InventoryRepository


class ApplicationException(Exception):
    """Base exception for inventory application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


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


class CreateInventoryItemUseCase:
    """Create inventory item aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateInventoryItemRequest) -> CreateInventoryItemResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: InventoryRepository = uow.inventory_repository

                normalized_reference = request.item_reference.strip()
                if repository.exists_by_reference(normalized_reference):
                    raise BusinessRuleViolation(
                        f"Inventory reference {normalized_reference} already exists"
                    )

                create_kwargs: dict[str, object] = {}
                if request.inventory_item_id is not None:
                    create_kwargs["id"] = request.inventory_item_id

                item = InventoryItem(
                    item_reference=request.item_reference,
                    name=request.name,
                    unit_of_measure=UnitOfMeasure(
                        unit_code=request.unit_code,
                        decimal_places=request.unit_decimal_places,
                        display_name=request.unit_display_name,
                    ),
                    description=request.description,
                    minimum_stock_level=request.minimum_stock_level,
                    **create_kwargs,
                )
                repository.add(item)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except InventoryError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create inventory item failed") from exc

        return CreateInventoryItemResponse(inventory_item=to_inventory_item_response(item))


def to_stock_location(value: StockLocationInput) -> StockLocation:
    return StockLocation(
        location_key=value.location_key,
        location_name=value.location_name,
        vessel_id=value.vessel_id,
    )


def to_stock_position_response(position: StockPosition) -> StockLocationBalanceResponse:
    return StockLocationBalanceResponse(
        location_key=position.location.location_key,
        location_name=position.location.location_name,
        vessel_id=position.location.vessel_id,
        quantity=position.quantity,
    )


def to_stock_movement_response(movement: StockMovement) -> StockMovementResponse:
    return StockMovementResponse(
        movement_id=movement.id.value,
        movement_type=movement.movement_type.value,
        quantity=movement.quantity,
        occurred_at=movement.occurred_at,
        location_key=movement.location.location_key,
        location_name=movement.location.location_name,
        vessel_id=movement.location.vessel_id,
        external_reference=movement.external_reference,
        note=movement.note,
        reason=movement.reason,
    )


def to_inventory_item_response(item: InventoryItem) -> InventoryItemResponse:
    return InventoryItemResponse(
        inventory_item_id=item.id.value,
        item_reference=item.item_reference,
        name=item.name,
        description=item.description,
        unit_code=item.unit_of_measure.unit_code,
        unit_decimal_places=item.unit_of_measure.decimal_places,
        unit_display_name=item.unit_of_measure.display_name,
        status=item.status.value,
        total_quantity=item.total_quantity,
        minimum_stock_level=item.minimum_stock_level,
        low_stock=item.low_stock,
        positions=tuple(to_stock_position_response(position) for position in item.positions),
        movements=tuple(to_stock_movement_response(movement) for movement in item.movements),
    )
