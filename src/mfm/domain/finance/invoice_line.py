"""Invoice line value object for finance domain."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from mfm.common.value_object import ValueObject
from mfm.domain.finance.exceptions import InvalidInvoiceLineError
from mfm.domain.finance.money import Money


@dataclass(frozen=True, slots=True)
class InvoiceLine(ValueObject):
    """Single invoice line with quantity and unit price."""

    description: str
    quantity: Decimal
    unit_price: Money

    def __post_init__(self) -> None:
        if not isinstance(self.description, str) or not self.description.strip():
            raise InvalidInvoiceLineError("description must be a non-empty string")

        try:
            quantity_value = (
                self.quantity
                if isinstance(self.quantity, Decimal)
                else Decimal(str(self.quantity))
            )
        except Exception as exc:
            raise InvalidInvoiceLineError("quantity must be a valid decimal") from exc

        if quantity_value <= Decimal("0"):
            raise InvalidInvoiceLineError("quantity must be greater than zero")

        if not isinstance(self.unit_price, Money):
            raise InvalidInvoiceLineError("unit_price must be Money")

        object.__setattr__(self, "description", self.description.strip())
        object.__setattr__(self, "quantity", quantity_value)

    @property
    def total(self) -> Money:
        return self.unit_price * self.quantity
