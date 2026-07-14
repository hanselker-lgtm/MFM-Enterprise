"""Issue stock use case."""

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
class IssueStockRequest:
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
class IssueStockResponse:
    inventory_item: InventoryItemResponse


class IssueStockUseCase:
    """Issue stock through aggregate-owned issue operation."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: IssueStockRequest) -> IssueStockResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: InventoryRepository = uow.inventory_repository
                item = repository.get_by_id(request.inventory_item_id)
                if item is None:
                    raise BusinessRuleViolation(
                        f"Inventory item {request.inventory_item_id} does not exist"
                    )

                item.issue_stock(
                    location=to_stock_location(request.location),
                    quantity=request.quantity,
                    occurred_at=request.occurred_at,
                    external_reference=request.external_reference,
                    note=request.note,
                )
                repository.update(item)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except InventoryError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Issue stock failed") from exc

        return IssueStockResponse(inventory_item=to_inventory_item_response(item))
