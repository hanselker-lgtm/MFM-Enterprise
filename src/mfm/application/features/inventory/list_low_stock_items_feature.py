"""List low-stock inventory items feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.features.inventory.create_inventory_item_feature import (
    InventoryItemResponse,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    RepositoryException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    to_feature_inventory_item_response,
)
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsRequest as ServiceRequest
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsResponse as ServiceResponse
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsUseCase


@dataclass(frozen=True, slots=True)
class ListLowStockItemsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListLowStockItemsResponse:
    items: tuple[InventoryItemResponse, ...]


class ListLowStockItemsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListLowStockItemsFeature:
    """Feature facade for low-stock inventory item listing."""

    def __init__(self, *, service: ListLowStockItemsService) -> None:
        self._service = service

    def execute(self, request: ListLowStockItemsRequest) -> ListLowStockItemsResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List low-stock inventory items feature failed") from exc

        return ListLowStockItemsResponse(
            items=tuple(
                to_feature_inventory_item_response(item)
                for item in service_response.items
            )
        )
