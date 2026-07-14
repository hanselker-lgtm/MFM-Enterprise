"""Get Inventory Item use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.inventory.create_inventory_item import ApplicationException
from mfm.application.inventory.create_inventory_item import BusinessRuleViolation
from mfm.application.inventory.create_inventory_item import InventoryItemResponse
from mfm.application.inventory.create_inventory_item import RepositoryException
from mfm.application.inventory.create_inventory_item import ValidationException
from mfm.application.inventory.create_inventory_item import to_inventory_item_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.inventory_repository import InventoryRepository


@dataclass(frozen=True, slots=True)
class GetInventoryItemRequest:
    inventory_item_id: UUID

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetInventoryItemResponse:
    inventory_item: InventoryItemResponse


class GetInventoryItemUseCase:
    """Load one inventory item through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetInventoryItemRequest) -> GetInventoryItemResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: InventoryRepository = uow.inventory_repository
                item = repository.get_by_id(request.inventory_item_id)
                if item is None:
                    raise BusinessRuleViolation(
                        f"Inventory item {request.inventory_item_id} does not exist"
                    )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get inventory item failed") from exc

        return GetInventoryItemResponse(inventory_item=to_inventory_item_response(item))
