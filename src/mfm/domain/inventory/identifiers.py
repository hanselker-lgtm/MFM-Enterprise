"""Identity value objects for the inventory domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class InventoryItemId(ValueObject):
    """Identity for the InventoryItem aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("InventoryItemId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "InventoryItemId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class StockMovementId(ValueObject):
    """Identity for a stock movement entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("StockMovementId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "StockMovementId":
        return cls(uuid4())