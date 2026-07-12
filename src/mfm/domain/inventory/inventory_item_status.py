"""Inventory item lifecycle status enum."""

from enum import StrEnum


class InventoryItemStatus(StrEnum):
    """Lifecycle states for InventoryItem."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"