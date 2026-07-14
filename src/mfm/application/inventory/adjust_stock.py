"""Adjust stock use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.application.inventory.create_inventory_item import ApplicationException
from mfm.application.inventory.create_inventory_item import BusinessRuleViolation
from mfm.application.inventory.create_inventory_item import InventoryItemResponse
from mfm.application.inventory.create_inventory_item import RepositoryException
from mfm.application.inventory.create_inventory_item import StockLocationInput
from mfm.application.inventory.create_inventory_item import ValidationException
from mfm.application.inventory.create_inventory_item import to_inventory_item_response
from mfm.application.inventory.create_inventory_item import to_stock_location
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.inventory.exceptions import InventoryError
from mfm.repositories.inventory_repository import InventoryRepository


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


class AdjustStockUseCase:
    """Adjust stock through aggregate-owned stock count correction."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: AdjustStockRequest) -> AdjustStockResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: InventoryRepository = uow.inventory_repository
                item = repository.get_by_id(request.inventory_item_id)
                if item is None:
                    raise BusinessRuleViolation(
                        f"Inventory item {request.inventory_item_id} does not exist"
                    )

                item.adjust_stock_to_count(
                    location=to_stock_location(request.location),
                    counted_quantity=request.counted_quantity,
                    reason=request.reason,
                    occurred_at=request.occurred_at,
                    note=request.note,
                )
                repository.update(item)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except InventoryError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Adjust stock failed") from exc

        return AdjustStockResponse(inventory_item=to_inventory_item_response(item))
