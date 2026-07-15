"""List inventory items feature facade following Public API Standard."""

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
from mfm.application.inventory.list_inventory_items import ListInventoryItemsRequest as ServiceRequest
from mfm.application.inventory.list_inventory_items import ListInventoryItemsResponse as ServiceResponse
from mfm.application.inventory.list_inventory_items import ListInventoryItemsUseCase


@dataclass(frozen=True, slots=True)
class ListInventoryItemsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListInventoryItemsResponse:
    items: tuple[InventoryItemResponse, ...]


class ListInventoryItemsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListInventoryItemsFeature:
    """Feature facade for inventory item listing."""

    def __init__(self, *, service: ListInventoryItemsService) -> None:
        self._service = service

    def execute(self, request: ListInventoryItemsRequest) -> ListInventoryItemsResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List inventory items feature failed") from exc

        return ListInventoryItemsResponse(
            items=tuple(
                to_feature_inventory_item_response(item)
                for item in service_response.items
            )
        )
