"""List low-stock Inventory Items use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.inventory.create_inventory_item import ApplicationException
from mfm.application.inventory.create_inventory_item import InventoryItemResponse
from mfm.application.inventory.create_inventory_item import RepositoryException
from mfm.application.inventory.create_inventory_item import to_inventory_item_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.inventory_repository import InventoryRepository


@dataclass(frozen=True, slots=True)
class ListLowStockItemsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListLowStockItemsResponse:
    items: tuple[InventoryItemResponse, ...]


class ListLowStockItemsUseCase:
    """List inventory items that are below their minimum stock level."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListLowStockItemsRequest) -> ListLowStockItemsResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                repository: InventoryRepository = uow.inventory_repository
                items = repository.get_low_stock()
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List low-stock inventory items failed") from exc

        return ListLowStockItemsResponse(
            items=tuple(to_inventory_item_response(item) for item in items)
        )
