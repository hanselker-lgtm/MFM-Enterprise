"""Repository contract for InventoryItem aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.inventory.inventory_item import InventoryItem


class InventoryRepository(ABC):
    """Persistence contract for InventoryItem aggregate roots."""

    @abstractmethod
    def add(self, item: InventoryItem) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_reference(self, item_reference: str) -> InventoryItem | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: InventoryItem) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists_by_reference(self, item_reference: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[InventoryItem]:
        raise NotImplementedError

    @abstractmethod
    def get_low_stock(self) -> list[InventoryItem]:
        raise NotImplementedError
