from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import CurrencyMismatchError
from mfm.domain.finance.exceptions import InvalidMoneyAmountError
from mfm.domain.finance.exceptions import MoneySerializationError
from mfm.domain.finance.money import Money


def test_money_is_immutable_value_object():
    money = Money(amount=Decimal("100.00"), currency=Currency.DKK)

    with pytest.raises(FrozenInstanceError):
        money.amount = Decimal("200.00")  # type: ignore[misc]


def test_money_supports_addition():
    left = Money(amount=Decimal("100.25"), currency=Currency.DKK)
    right = Money(amount=Decimal("24.75"), currency=Currency.DKK)

    assert left + right == Money(amount=Decimal("125.00"), currency=Currency.DKK)


def test_money_supports_subtraction():
    left = Money(amount=Decimal("100.00"), currency=Currency.DKK)
    right = Money(amount=Decimal("20.00"), currency=Currency.DKK)

    assert left - right == Money(amount=Decimal("80.00"), currency=Currency.DKK)


def test_money_supports_multiplication():
    value = Money(amount=Decimal("99.99"), currency=Currency.DKK)

    assert value * Decimal("2") == Money(amount=Decimal("199.98"), currency=Currency.DKK)
    assert 2 * value == Money(amount=Decimal("199.98"), currency=Currency.DKK)


def test_money_supports_division():
    value = Money(amount=Decimal("100.00"), currency=Currency.DKK)

    assert value / Decimal("4") == Money(amount=Decimal("25.00"), currency=Currency.DKK)


def test_money_division_by_zero_is_rejected():
    value = Money(amount=Decimal("100.00"), currency=Currency.DKK)

    with pytest.raises(InvalidMoneyAmountError):
        _ = value / Decimal("0")


def test_money_supports_comparisons():
    low = Money(amount=Decimal("50.00"), currency=Currency.DKK)
    high = Money(amount=Decimal("100.00"), currency=Currency.DKK)

    assert low < high
    assert low <= high
    assert high > low
    assert high >= low
    assert low <= low
    assert high >= high


def test_money_supports_equality_and_inequality():
    left = Money(amount=Decimal("75.00"), currency=Currency.EUR)
    same = Money(amount=Decimal("75.00"), currency=Currency.EUR)
    different = Money(amount=Decimal("74.99"), currency=Currency.EUR)

    assert left == same
    assert left != different


def test_money_rejects_currency_mismatch_in_operations_and_comparisons():
    dkk = Money(amount=Decimal("100.00"), currency=Currency.DKK)
    eur = Money(amount=Decimal("100.00"), currency=Currency.EUR)

    with pytest.raises(CurrencyMismatchError):
        _ = dkk + eur

    with pytest.raises(CurrencyMismatchError):
        _ = dkk - eur

    with pytest.raises(CurrencyMismatchError):
        _ = dkk < eur

    with pytest.raises(CurrencyMismatchError):
        _ = dkk == eur


def test_money_serialization_round_trip_dict_and_json():
    money = Money(amount=Decimal("123.45"), currency=Currency.GBP)

    payload = money.to_dict()
    assert payload == {"amount": "123.45", "currency": "GBP"}
    assert Money.from_dict(payload) == money

    json_payload = money.to_json()
    assert Money.from_json(json_payload) == money


def test_money_serialization_rejects_invalid_data():
    with pytest.raises(MoneySerializationError):
        Money.from_dict({"currency": "DKK"})

    with pytest.raises(MoneySerializationError):
        Money.from_json("not-json")


def test_money_formatting_outputs_currency_and_amount():
    money = Money(amount=Decimal("1234.5"), currency=Currency.USD)

    assert money.format() == "USD 1234.50"
    assert money.format(with_currency=False) == "1234.50"
    assert str(money) == "USD 1234.50"


def test_money_supports_negative_values():
    money = Money(amount=Decimal("-10.10"), currency=Currency.DKK)

    assert money.amount == Decimal("-10.10")


def test_money_supports_zero_values():
    money = Money(amount=Decimal("0"), currency=Currency.DKK)

    assert money.amount == Decimal("0.00")


def test_money_rounding_uses_two_decimals_half_up():
    rounded_up = Money(amount=Decimal("10.005"), currency=Currency.DKK)
    rounded_down = Money(amount=Decimal("10.004"), currency=Currency.DKK)

    assert rounded_up.amount == Decimal("10.01")
    assert rounded_down.amount == Decimal("10.00")


def test_money_rejects_float_values_internally():
    with pytest.raises(InvalidMoneyAmountError):
        Money(amount=10.5, currency=Currency.DKK)  # type: ignore[arg-type]

    money = Money(amount=Decimal("100.00"), currency=Currency.DKK)
    with pytest.raises(InvalidMoneyAmountError):
        _ = money * 1.5  # type: ignore[arg-type]
