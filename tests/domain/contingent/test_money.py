from decimal import Decimal

import pytest

from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.exceptions import (
    InvalidContingentAmountError,
    InvalidContingentReferenceError,
)
from mfm.domain.contingent.money import Money


def test_money_accepts_non_negative_amount_and_currency():
    money = Money(amount=Decimal("123.45"), currency=Currency.DKK)

    assert money.amount == Decimal("123.45")
    assert money.currency == Currency.DKK


def test_money_rejects_negative_amount():
    with pytest.raises(InvalidContingentAmountError):
        Money(amount=Decimal("-1.00"), currency=Currency.DKK)


def test_money_rejects_invalid_currency_reference():
    with pytest.raises(InvalidContingentReferenceError):
        Money(amount=Decimal("1.00"), currency="DKK")  # type: ignore[arg-type]
