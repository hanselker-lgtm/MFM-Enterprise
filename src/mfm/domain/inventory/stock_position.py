"""Current stock position entity for one inventory location."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from mfm.domain.inventory.exceptions import InvalidInventoryQuantityError
from mfm.domain.inventory.stock_location import StockLocation


@dataclass(slots=True)
class StockPosition:
    """Current authoritative quantity for one location."""

    location: StockLocation
    quantity: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.location, StockLocation):
            raise TypeError("location must be StockLocation")
        if not isinstance(self.quantity, Decimal):
            raise InvalidInventoryQuantityError("quantity must be Decimal")
        if self.quantity < Decimal("0"):
            raise InvalidInventoryQuantityError("quantity cannot be negative")

    def increase(self, amount: Decimal) -> None:
        self._validate_amount(amount)
        self.quantity += amount

    def decrease(self, amount: Decimal) -> None:
        self._validate_amount(amount)
        next_quantity = self.quantity - amount
        if next_quantity < Decimal("0"):
            raise InvalidInventoryQuantityError("quantity cannot be negative")
        self.quantity = next_quantity

    def set_quantity(self, quantity: Decimal) -> None:
        if not isinstance(quantity, Decimal):
            raise InvalidInventoryQuantityError("quantity must be Decimal")
        if quantity < Decimal("0"):
            raise InvalidInventoryQuantityError("quantity cannot be negative")
        self.quantity = quantity

    @staticmethod
    def _validate_amount(amount: Decimal) -> None:
        if not isinstance(amount, Decimal):
            raise InvalidInventoryQuantityError("amount must be Decimal")
        if amount <= Decimal("0"):
            raise InvalidInventoryQuantityError("amount must be positive")