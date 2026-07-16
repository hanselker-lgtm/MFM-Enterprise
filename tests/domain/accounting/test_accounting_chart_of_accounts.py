from uuid import uuid4

import pytest

from mfm.domain.accounting.account_category import AccountCategory
from mfm.domain.accounting.account_group import AccountGroup
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.chart_of_accounts import ChartOfAccounts
from mfm.domain.accounting.exceptions import AccountHasPostingsError
from mfm.domain.accounting.exceptions import DuplicateAccountInChartError
from mfm.domain.accounting.exceptions import InvalidAccountGroupError
from mfm.domain.accounting.exceptions import InvalidChartOfAccountsError
from mfm.domain.accounting.exceptions import LockedChartOfAccountsError
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance


def _account(number: str, *, name: str = "Account") -> LedgerAccount:
    return LedgerAccount(
        account_number=AccountNumber(number),
        name=name,
        account_type=AccountType.ASSET,
        normal_balance=NormalBalance.DEBIT,
    )


def _chart() -> ChartOfAccounts:
    return ChartOfAccounts(name="Main Chart", version="2026.1")


def test_create_chart():
    chart = _chart()

    assert chart.name == "Main Chart"
    assert chart.version == "2026.1"
    assert chart.active is True
    assert chart.accounts == []


def test_duplicate_account_is_rejected():
    chart = _chart()
    account = _account(f"3000-{uuid4().hex[:6]}")

    chart.add_account(account)

    with pytest.raises(DuplicateAccountInChartError):
        chart.add_account(account)


def test_remove_account():
    chart = _chart()
    account = _account(f"3100-{uuid4().hex[:6]}")
    chart.add_account(account)

    chart.remove_account(account.account_number)

    assert chart.contains(account.account_number) is False


def test_lookup_and_contains():
    chart = _chart()
    account = _account(f"3200-{uuid4().hex[:6]}")
    chart.add_account(account)

    found = chart.find_account(account.account_number)
    assert found == account
    assert chart.contains(account.account_number) is True


def test_validation_and_empty_chart():
    chart = _chart()

    with pytest.raises(InvalidChartOfAccountsError):
        chart.validate()

    account = _account(f"3300-{uuid4().hex[:6]}")
    chart.add_account(account)
    chart.validate()


def test_locking_prevents_changes():
    chart = _chart()
    account = _account(f"3400-{uuid4().hex[:6]}")
    chart.lock()

    with pytest.raises(LockedChartOfAccountsError):
        chart.add_account(account)

    with pytest.raises(LockedChartOfAccountsError):
        chart.deactivate()


def test_activation_and_deactivation():
    chart = _chart()

    chart.deactivate()
    assert chart.active is False

    chart.activate()
    assert chart.active is True


def test_invalid_groups_are_rejected():
    chart = _chart()
    account = _account(f"3500-{uuid4().hex[:6]}")

    with pytest.raises(InvalidAccountGroupError):
        chart.add_account(account, group="Assets")  # type: ignore[arg-type]

    with pytest.raises(InvalidAccountGroupError):
        chart.add_account(account, category="ASSETS")  # type: ignore[arg-type]


def test_valid_groups_and_categories_are_accepted():
    chart = _chart()
    account = _account(f"3600-{uuid4().hex[:6]}")

    chart.add_account(
        account,
        group=AccountGroup.CURRENT_ASSETS,
        category=AccountCategory.ASSETS,
    )

    assert chart.contains(account.account_number) is True


def test_account_with_postings_cannot_be_removed():
    chart = _chart()
    account = _account(f"3700-{uuid4().hex[:6]}")
    chart.add_account(account)
    account.mark_posted()

    with pytest.raises(AccountHasPostingsError):
        chart.remove_account(account.account_number)
