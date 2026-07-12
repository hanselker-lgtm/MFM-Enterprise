"""Inventory unit of measure value object."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from decimal import InvalidOperation
from decimal import ROUND_HALF_UP

from mfm.common.value_object import ValueObject
from mfm.domain.inventory.exceptions import InvalidInventoryQuantityError
from mfm.domain.inventory.exceptions import InvalidUnitOfMeasureError


@dataclass(frozen=True, slots=True)
class UnitOfMeasure(ValueObject):
    """Immutable unit of measure owned by Inventory."""

    unit_code: str
    decimal_places: int
    display_name: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.unit_code, str) or not self.unit_code.strip():
            raise InvalidUnitOfMeasureError("unit_code must be a non-empty string")

        normalized_code = self.unit_code.strip().upper()
        if any(character.isspace() for character in normalized_code):
            raise InvalidUnitOfMeasureError("unit_code must not contain whitespace")
        object.__setattr__(self, "unit_code", normalized_code)

        if not isinstance(self.decimal_places, int) or isinstance(self.decimal_places, bool):
            raise InvalidUnitOfMeasureError("decimal_places must be integer")
        if self.decimal_places < 0:
            raise InvalidUnitOfMeasureError("decimal_places cannot be negative")

        if self.display_name is not None:
            if not isinstance(self.display_name, str):
                raise InvalidUnitOfMeasureError("display_name must be string or None")
            object.__setattr__(self, "display_name", self.display_name.strip() or None)

    @property
    def scale(self) -> Decimal:
        if self.decimal_places == 0:
            return Decimal("1")
        return Decimal("1").scaleb(-self.decimal_places)

    def normalize_quantity(self, value: Decimal | str | int) -> Decimal:
        if isinstance(value, bool) or isinstance(value, float):
            raise InvalidInventoryQuantityError("quantity must not be float")

        try:
            decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise InvalidInventoryQuantityError("quantity is invalid") from exc

        if not decimal_value.is_finite():
            raise InvalidInventoryQuantityError("quantity must be finite")

        return decimal_value.quantize(self.scale, rounding=ROUND_HALF_UP)