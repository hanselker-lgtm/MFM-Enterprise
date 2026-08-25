"""Money value object for finance domain."""

from __future__ import annotations

import json
from dataclasses import dataclass
from decimal import Decimal
from decimal import InvalidOperation
from decimal import ROUND_HALF_UP
from typing import Any
from typing import Mapping

from mfm.common.value_object import ValueObject
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import CurrencyMismatchError
from mfm.domain.finance.exceptions import InvalidCurrencyError
from mfm.domain.finance.exceptions import InvalidMoneyAmountError
from mfm.domain.finance.exceptions import MoneySerializationError


_MONEY_SCALE = Decimal("0.01")


@dataclass(frozen=True, slots=True)
class Money(ValueObject):
    """Immutable money value object using Decimal internally."""

    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        object.__setattr__(self, "amount", self._normalize_amount(self.amount))
        object.__setattr__(self, "currency", self._normalize_currency(self.currency))

    @staticmethod
    def _normalize_currency(value: Currency | str) -> Currency:
        if isinstance(value, Currency):
            return value

        if isinstance(value, str):
            try:
                return Currency(value.upper())
            except ValueError as exc:
                raise InvalidCurrencyError("Unsupported currency") from exc

        raise InvalidCurrencyError("currency must be a Currency or ISO code")

    @staticmethod
    def _normalize_amount(value: Decimal | str | int) -> Decimal:
        if isinstance(value, bool) or isinstance(value, float):
            raise InvalidMoneyAmountError("amount must not be float")

        try:
            decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise InvalidMoneyAmountError("Invalid amount") from exc

        if not decimal_value.is_finite():
            raise InvalidMoneyAmountError("amount must be finite")

        return decimal_value.quantize(_MONEY_SCALE, rounding=ROUND_HALF_UP)

    def _assert_same_currency(self, other: object) -> Money:
        if not isinstance(other, Money):
            raise TypeError("operand must be Money")

        if self.currency != other.currency:
            raise CurrencyMismatchError("Cannot mix different currencies")

        return other

    @staticmethod
    def _normalize_scalar(value: Decimal | str | int) -> Decimal:
        if isinstance(value, bool) or isinstance(value, float):
            raise InvalidMoneyAmountError("scalar must not be float")

        try:
            decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise InvalidMoneyAmountError("Invalid scalar") from exc

        if not decimal_value.is_finite():
            raise InvalidMoneyAmountError("scalar must be finite")

        return decimal_value

    def __add__(self, other: object) -> Money:
        right = self._assert_same_currency(other)
        return Money(amount=self.amount + right.amount, currency=self.currency)

    def __sub__(self, other: object) -> Money:
        right = self._assert_same_currency(other)
        return Money(amount=self.amount - right.amount, currency=self.currency)

    def __mul__(self, other: Decimal | str | int) -> Money:
        scalar = self._normalize_scalar(other)
        return Money(amount=self.amount * scalar, currency=self.currency)

    def __rmul__(self, other: Decimal | str | int) -> Money:
        return self.__mul__(other)

    def __truediv__(self, other: Decimal | str | int) -> Money:
        scalar = self._normalize_scalar(other)
        if scalar == Decimal("0"):
            raise InvalidMoneyAmountError("Division by zero")
        return Money(amount=self.amount / scalar, currency=self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        self._assert_same_currency(other)
        return self.amount == other.amount

    def __lt__(self, other: object) -> bool:
        right = self._assert_same_currency(other)
        return self.amount < right.amount

    def __le__(self, other: object) -> bool:
        right = self._assert_same_currency(other)
        return self.amount <= right.amount

    def __gt__(self, other: object) -> bool:
        right = self._assert_same_currency(other)
        return self.amount > right.amount

    def __ge__(self, other: object) -> bool:
        right = self._assert_same_currency(other)
        return self.amount >= right.amount

    def format(self, with_currency: bool = True) -> str:
        amount_text = f"{self.amount:.2f}"
        if with_currency:
            return f"{self.currency.value} {amount_text}"
        return amount_text

    def __str__(self) -> str:
        return self.format()

    def to_dict(self) -> dict[str, str]:
        return {
            "amount": f"{self.amount:.2f}",
            "currency": self.currency.value,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Money:
        if not isinstance(data, Mapping):
            raise MoneySerializationError("data must be a mapping")

        if "amount" not in data or "currency" not in data:
            raise MoneySerializationError("data must include amount and currency")

        try:
            return cls(amount=data["amount"], currency=data["currency"])
        except (InvalidCurrencyError, InvalidMoneyAmountError, TypeError) as exc:
            raise MoneySerializationError("Invalid serialized money") from exc

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data: str) -> Money:
        try:
            payload = json.loads(data)
        except json.JSONDecodeError as exc:
            raise MoneySerializationError("Invalid JSON for money") from exc

        return cls.from_dict(payload)
