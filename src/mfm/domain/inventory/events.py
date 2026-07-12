"""Inventory domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class InventoryItemCreated(DomainEvent):
    inventory_item_id: UUID | None = None
    item_reference: str | None = None


@dataclass(slots=True)
class StockReceived(DomainEvent):
    inventory_item_id: UUID | None = None
    stock_movement_id: UUID | None = None
    location_key: str | None = None
    quantity: Decimal | None = None
    occurred_at: datetime | None = None


@dataclass(slots=True)
class StockIssued(DomainEvent):
    inventory_item_id: UUID | None = None
    stock_movement_id: UUID | None = None
    location_key: str | None = None
    quantity: Decimal | None = None
    occurred_at: datetime | None = None


@dataclass(slots=True)
class StockAdjusted(DomainEvent):
    inventory_item_id: UUID | None = None
    stock_movement_id: UUID | None = None
    location_key: str | None = None
    quantity: Decimal | None = None
    movement_type: str | None = None
    occurred_at: datetime | None = None


@dataclass(slots=True)
class InventoryItemDeactivated(DomainEvent):
    inventory_item_id: UUID | None = None


@dataclass(slots=True)
class InventoryItemReactivated(DomainEvent):
    inventory_item_id: UUID | None = None