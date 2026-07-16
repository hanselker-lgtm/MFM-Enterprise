from uuid import uuid4

import pytest

from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.exceptions import DuplicateAccountNumberError
from mfm.domain.accounting.exceptions import InvalidLedgerAccountNameError
from mfm.domain.accounting.exceptions import InvalidLedgerAccountReferenceError
from mfm.domain.accounting.exceptions import LockedLedgerAccountError
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance


def _account(number: str, *, active: bool = True, locked: bool = False) -> LedgerAccount:
    return LedgerAccount(
        account_number=AccountNumber(number),
        name="Accounts Receivable",
        account_type=AccountType.ASSET,
        normal_balance=NormalBalance.DEBIT,
        active=active,
        locked=locked,
    )


def test_create_account():
    account = _account(f"1100-{uuid4().hex[:6]}")

    assert account.name == "Accounts Receivable"
    assert account.account_type == AccountType.ASSET
    assert account.normal_balance == NormalBalance.DEBIT
    assert account.active is True
    assert account.locked is False


def test_invalid_account_number():
    with pytest.raises(InvalidLedgerAccountReferenceError):
        AccountNumber("   ")

    with pytest.raises(InvalidLedgerAccountReferenceError):
        AccountNumber("10 01")


def test_account_number_must_be_unique():
    value = f"1200-{uuid4().hex[:6]}"
    _account(value)

    with pytest.raises(DuplicateAccountNumberError):
        _account(value)


def test_empty_name_is_rejected():
    with pytest.raises(InvalidLedgerAccountNameError):
        LedgerAccount(
            account_number=AccountNumber(f"1300-{uuid4().hex[:6]}"),
            name=" ",
            account_type=AccountType.ASSET,
            normal_balance=NormalBalance.DEBIT,
        )


def test_activate_and_deactivate():
    account = _account(f"1400-{uuid4().hex[:6]}", active=False)

    account.activate()
    assert account.active is True

    account.deactivate()
    assert account.active is False


def test_lock_and_unlock():
    account = _account(f"1500-{uuid4().hex[:6]}", locked=False)

    account.lock()
    assert account.locked is True

    account.unlock()
    assert account.locked is False


def test_rename():
    account = _account(f"1600-{uuid4().hex[:6]}")

    account.rename(name="Trade Receivables")

    assert account.name == "Trade Receivables"


def test_account_number_cannot_be_changed():
    account = _account(f"1700-{uuid4().hex[:6]}")

    with pytest.raises(AttributeError):
        account.account_number = AccountNumber(f"1701-{uuid4().hex[:6]}")  # type: ignore[misc]


def test_can_post_true_when_active_and_unlocked():
    account = _account(f"1800-{uuid4().hex[:6]}", active=True, locked=False)

    assert account.can_post() is True


def test_inactive_account_cannot_post():
    account = _account(f"1900-{uuid4().hex[:6]}", active=False, locked=False)

    assert account.can_post() is False


def test_locked_account_cannot_post_or_mutate():
    account = _account(f"2000-{uuid4().hex[:6]}", active=True, locked=True)

    assert account.can_post() is False

    with pytest.raises(LockedLedgerAccountError):
        account.rename(name="Renamed")

    with pytest.raises(LockedLedgerAccountError):
        account.deactivate()


def test_enum_values():
    assert AccountType.ASSET.value == "ASSET"
    assert AccountType.LIABILITY.value == "LIABILITY"
    assert AccountType.EQUITY.value == "EQUITY"
    assert AccountType.INCOME.value == "INCOME"
    assert AccountType.EXPENSE.value == "EXPENSE"

    assert NormalBalance.DEBIT.value == "DEBIT"
    assert NormalBalance.CREDIT.value == "CREDIT"
