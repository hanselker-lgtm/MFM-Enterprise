from __future__ import annotations

from dataclasses import FrozenInstanceError
from dataclasses import is_dataclass
from datetime import date
from decimal import Decimal
from importlib import import_module
from uuid import UUID

import pytest

from mfm.application.accounting.create_journal import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.close_fiscal_year import CloseFiscalYearRequest
from mfm.application.accounting.close_fiscal_year import CloseFiscalYearUseCase
from mfm.application.accounting.get_fiscal_year import GetFiscalYearUseCase
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.get_ledger_account import GetLedgerAccountUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.list_journals import ListJournalsUseCase
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsUseCase
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearRequest
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearUseCase
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.accounting.reverse_journal import ReverseJournalUseCase
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.accounting.update_ledger_account import UpdateLedgerAccountUseCase
from mfm.application.features.accounting import close_fiscal_year
from mfm.application.features.accounting import create_fiscal_year
from mfm.application.features.accounting import create_journal
from mfm.application.features.accounting import create_ledger_account
from mfm.application.features.accounting import get_fiscal_year
from mfm.application.features.accounting import get_journal
from mfm.application.features.accounting import get_ledger_account
from mfm.application.features.accounting import list_fiscal_years
from mfm.application.features.accounting import list_journals
from mfm.application.features.accounting import list_ledger_accounts
from mfm.application.features.accounting import open_fiscal_year
from mfm.application.features.accounting import post_journal
from mfm.application.features.accounting import reverse_journal
from mfm.application.features.accounting import search_journals
from mfm.application.features.accounting import update_ledger_account
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearFeature,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearRequest,
)
from mfm.application.features.accounting.create_fiscal_year_feature import FiscalPeriodInput
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalFeature,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalRequest,
)
from mfm.application.features.accounting.create_journal_feature import JournalLineInput
from mfm.application.features.accounting.create_journal_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.accounting.create_journal_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountFeature,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountRequest,
)
from mfm.application.features.accounting.get_fiscal_year_feature import (
    GetFiscalYearRequest,
)
from mfm.application.features.accounting.get_journal_feature import GetJournalFeature
from mfm.application.features.accounting.get_journal_feature import GetJournalRequest
from mfm.application.features.accounting.get_ledger_account_feature import (
    GetLedgerAccountRequest,
)
from mfm.application.features.accounting.list_journals_feature import ListJournalsFeature
from mfm.application.features.accounting.list_journals_feature import ListJournalsRequest
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsRequest,
)
from mfm.application.features.accounting.list_ledger_accounts_feature import (
    ListLedgerAccountsRequest,
)
from mfm.application.features.accounting.post_journal_feature import PostJournalFeature
from mfm.application.features.accounting.post_journal_feature import PostJournalRequest
from mfm.application.features.accounting.reverse_journal_feature import ReverseJournalFeature
from mfm.application.features.accounting.reverse_journal_feature import ReverseJournalRequest
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsFeature,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsRequest,
)
from mfm.application.features.accounting.update_ledger_account_feature import (
    UpdateLedgerAccountRequest,
)
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.ledger_account import LedgerAccount
from tests.application.accounting.test_accounting_use_cases import FakeAccountingUnitOfWork


@pytest.fixture(autouse=True)
def _reset_accounting_class_state() -> None:
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        LedgerAccount._registered_numbers.clear()
        FiscalYear._open_year_id = None


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def execute(self, request):  # noqa: ANN001
        _ = request
        if self._error is not None:
            raise self._error
        return self._response


def _period(number: int, start_day: int, end_day: int, *, year: int) -> FiscalPeriodInput:
    return FiscalPeriodInput(
        number=number,
        start_date=date(year, 1, start_day),
        end_date=date(year, 1, end_day),
        closed=False,
    )


def _closed_period(number: int, start_day: int, end_day: int, *, year: int) -> FiscalPeriodInput:
    return FiscalPeriodInput(
        number=number,
        start_date=date(year, 1, start_day),
        end_date=date(year, 1, end_day),
        closed=True,
    )


def _create_fiscal_year(uow: FakeAccountingUnitOfWork, *, year: int) -> UUID:
    created = CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)).execute(
        CreateFiscalYearRequest(
            year=year,
            start_date=date(year, 1, 1),
            end_date=date(year, 1, 31),
            periods=(
                _period(1, 1, 10, year=year),
                _period(2, 11, 20, year=year),
                _period(3, 21, 31, year=year),
            ),
        )
    )
    return created.fiscal_year.fiscal_year_id


def _create_account(
    uow: FakeAccountingUnitOfWork,
    *,
    number: str,
    name: str,
    account_type: str,
    normal_balance: str,
) -> UUID:
    created = CreateLedgerAccountFeature(
        service=CreateLedgerAccountUseCase(unit_of_work=uow)
    ).execute(
        CreateLedgerAccountRequest(
            account_number=number,
            name=name,
            account_type=account_type,
            normal_balance=normal_balance,
        )
    )
    return created.account.account_id


def _line(account_id: UUID, side: str, amount: str) -> JournalLineInput:
    return JournalLineInput(
        account_id=account_id,
        side=side,
        amount=Decimal(amount),
        currency="DKK",
    )


def test_create_feature_request_mapping_response_mapping_and_immutability() -> None:
    uow = FakeAccountingUnitOfWork()
    _create_fiscal_year(uow, year=2030)
    debit_id = _create_account(
        uow,
        number="1100-AR",
        name="Accounts receivable",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    credit_id = _create_account(
        uow,
        number="4100-SALES",
        name="Sales income",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    request = CreateJournalRequest(
        journal_number="JRN-FEAT-001",
        posting_date=date(2030, 1, 10),
        description="Feature journal",
        reference="INV-001",
        lines=(
            _line(debit_id, "DEBIT", "100.00"),
            _line(credit_id, "CREDIT", "100.00"),
        ),
    )

    response = CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)).execute(
        request
    )

    assert response.journal.journal_number == "JRN-FEAT-001"
    assert response.journal.status == "DRAFT"
    assert response.journal.lines[0].amount == Decimal("100.00")
    assert is_dataclass(response.journal)

    with pytest.raises(FrozenInstanceError):
        request.description = "Changed"  # type: ignore[misc]


def test_create_feature_error_mapping() -> None:
    invalid = CreateJournalFeature(service=StubService(error=ServiceValidationException("bad")))
    with pytest.raises(FeatureValidationException):
        invalid.execute(
            CreateJournalRequest(
                journal_number="JRN-ERR-1",
                posting_date=date(2030, 1, 1),
                description="x",
                lines=(
                    _line(UUID("00000000-0000-0000-0000-000000000111"), "DEBIT", "1.00"),
                    _line(UUID("00000000-0000-0000-0000-000000000222"), "CREDIT", "1.00"),
                ),
            )
        )

    duplicate = CreateJournalFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreateJournalRequest(
                journal_number="JRN-ERR-2",
                posting_date=date(2030, 1, 1),
                description="x",
                lines=(
                    _line(UUID("00000000-0000-0000-0000-000000000333"), "DEBIT", "1.00"),
                    _line(UUID("00000000-0000-0000-0000-000000000444"), "CREDIT", "1.00"),
                ),
            )
        )

    failing = CreateJournalFeature(service=StubService(error=ServiceRepositoryException("fail")))
    with pytest.raises(FeatureRepositoryException):
        failing.execute(
            CreateJournalRequest(
                journal_number="JRN-ERR-3",
                posting_date=date(2030, 1, 1),
                description="x",
                lines=(
                    _line(UUID("00000000-0000-0000-0000-000000000555"), "DEBIT", "1.00"),
                    _line(UUID("00000000-0000-0000-0000-000000000666"), "CREDIT", "1.00"),
                ),
            )
        )


def test_journal_lifecycle_posting_reversal_and_search_list() -> None:
    uow = FakeAccountingUnitOfWork()
    _create_fiscal_year(uow, year=2031)
    debit_id = _create_account(
        uow,
        number="1200-AR",
        name="Receivable",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    credit_id = _create_account(
        uow,
        number="4200-SALES",
        name="Revenue",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    created = CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)).execute(
        CreateJournalRequest(
            journal_number="JRN-2031-0001",
            posting_date=date(2031, 1, 15),
            description="Membership annual invoice",
            reference="INV-2031-0001",
            lines=(
                _line(debit_id, "DEBIT", "100.00"),
                _line(credit_id, "CREDIT", "100.00"),
            ),
        )
    )

    loaded = GetJournalFeature(service=GetJournalUseCase(unit_of_work=uow)).execute(
        GetJournalRequest(journal_id=created.journal.journal_id)
    )
    assert loaded.journal.status == "DRAFT"

    posted = PostJournalFeature(service=PostJournalUseCase(unit_of_work=uow)).execute(
        PostJournalRequest(journal_id=created.journal.journal_id)
    )
    assert posted.journal.status == "POSTED"

    reversed_journal = ReverseJournalFeature(
        service=ReverseJournalUseCase(unit_of_work=uow)
    ).execute(ReverseJournalRequest(journal_id=created.journal.journal_id))
    assert reversed_journal.journal.status == "REVERSED"

    listed = ListJournalsFeature(service=ListJournalsUseCase(unit_of_work=uow)).execute(
        ListJournalsRequest()
    )
    assert [item.journal_number for item in listed.journals] == ["JRN-2031-0001"]

    searched_text = SearchJournalsFeature(
        service=SearchJournalsUseCase(unit_of_work=uow)
    ).execute(SearchJournalsRequest(text="invoice"))
    assert [item.journal_number for item in searched_text.journals] == ["JRN-2031-0001"]


def test_ledger_account_lifecycle() -> None:
    uow = FakeAccountingUnitOfWork()

    created = CreateLedgerAccountFeature(
        service=CreateLedgerAccountUseCase(unit_of_work=uow)
    ).execute(
        CreateLedgerAccountRequest(
            account_number="1400-BANK",
            name="Bank",
            account_type="ASSET",
            normal_balance="DEBIT",
        )
    )

    loaded = get_ledger_account(
        service=GetLedgerAccountUseCase(unit_of_work=uow),
        request=GetLedgerAccountRequest(account_id=created.account.account_id),
    )
    assert loaded.account.name == "Bank"

    updated = update_ledger_account(
        service=UpdateLedgerAccountUseCase(unit_of_work=uow),
        request=UpdateLedgerAccountRequest(
            account_id=created.account.account_id,
            name="Bank operating account",
            active=False,
            locked=True,
        ),
    )
    assert updated.account.name == "Bank operating account"
    assert updated.account.active is False
    assert updated.account.locked is True

    listed_all = list_ledger_accounts(
        service=ListLedgerAccountsUseCase(unit_of_work=uow),
        request=ListLedgerAccountsRequest(),
    )
    listed_active = list_ledger_accounts(
        service=ListLedgerAccountsUseCase(unit_of_work=uow),
        request=ListLedgerAccountsRequest(active_only=True),
    )

    assert len(listed_all.accounts) == 1
    assert len(listed_active.accounts) == 0


def test_fiscal_year_lifecycle() -> None:
    uow = FakeAccountingUnitOfWork()

    created = create_fiscal_year(
        service=CreateFiscalYearUseCase(unit_of_work=uow),
        request=CreateFiscalYearRequest(
            year=2033,
            start_date=date(2033, 1, 1),
            end_date=date(2033, 1, 31),
            periods=(
                _closed_period(1, 1, 10, year=2033),
                _closed_period(2, 11, 20, year=2033),
                _closed_period(3, 21, 31, year=2033),
            ),
        ),
    )

    closed = close_fiscal_year(
        service=CloseFiscalYearUseCase(unit_of_work=uow),
        request=CloseFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id),
    )
    assert closed.fiscal_year.status == "CLOSED"

    opened = open_fiscal_year(
        service=OpenFiscalYearUseCase(unit_of_work=uow),
        request=OpenFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id),
    )
    assert opened.fiscal_year.status == "OPEN"

    loaded = get_fiscal_year(
        service=GetFiscalYearUseCase(unit_of_work=uow),
        request=GetFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id),
    )
    listed = list_fiscal_years(
        service=ListFiscalYearsUseCase(unit_of_work=uow),
        request=ListFiscalYearsRequest(),
    )

    assert loaded.fiscal_year.year == 2033
    assert [item.year for item in listed.fiscal_years] == [2033]


def test_package_entrypoint_helpers_delegate_to_feature_execute() -> None:
    uow = FakeAccountingUnitOfWork()
    _create_fiscal_year(uow, year=2034)

    receivable_id = create_ledger_account(
        service=CreateLedgerAccountUseCase(unit_of_work=uow),
        request=CreateLedgerAccountRequest(
            account_number="1500-AR",
            name="Accounts receivable",
            account_type="ASSET",
            normal_balance="DEBIT",
        ),
    ).account.account_id
    revenue_id = create_ledger_account(
        service=CreateLedgerAccountUseCase(unit_of_work=uow),
        request=CreateLedgerAccountRequest(
            account_number="4500-SALES",
            name="Sales income",
            account_type="INCOME",
            normal_balance="CREDIT",
        ),
    ).account.account_id

    created = create_journal(
        service=CreateJournalUseCase(unit_of_work=uow),
        request=CreateJournalRequest(
            journal_number="JRN-API-0001",
            posting_date=date(2034, 1, 10),
            description="API helper flow",
            reference="REF-API-1",
            lines=(
                _line(receivable_id, "DEBIT", "250.00"),
                _line(revenue_id, "CREDIT", "250.00"),
            ),
        ),
    )
    journal_id = created.journal.journal_id

    posted = post_journal(
        service=PostJournalUseCase(unit_of_work=uow),
        request=PostJournalRequest(journal_id=journal_id),
    )
    assert posted.journal.status == "POSTED"

    reversed_journal = reverse_journal(
        service=ReverseJournalUseCase(unit_of_work=uow),
        request=ReverseJournalRequest(journal_id=journal_id),
    )
    assert reversed_journal.journal.status == "REVERSED"

    loaded = get_journal(
        service=GetJournalUseCase(unit_of_work=uow),
        request=GetJournalRequest(journal_id=journal_id),
    )
    assert loaded.journal.journal_id == journal_id

    listed_journals = list_journals(
        service=ListJournalsUseCase(unit_of_work=uow),
        request=ListJournalsRequest(),
    )
    assert any(item.journal_id == journal_id for item in listed_journals.journals)

    searched = search_journals(
        service=SearchJournalsUseCase(unit_of_work=uow),
        request=SearchJournalsRequest(text="API helper"),
    )
    assert any(item.journal_id == journal_id for item in searched.journals)


def test_feature_modules_do_not_reference_sqlalchemy_or_sqlite_repo() -> None:
    modules = [
        import_module("mfm.application.features.accounting.create_journal_feature"),
        import_module("mfm.application.features.accounting.get_journal_feature"),
        import_module("mfm.application.features.accounting.list_journals_feature"),
        import_module("mfm.application.features.accounting.search_journals_feature"),
        import_module("mfm.application.features.accounting.post_journal_feature"),
        import_module("mfm.application.features.accounting.reverse_journal_feature"),
        import_module("mfm.application.features.accounting.create_ledger_account_feature"),
        import_module("mfm.application.features.accounting.update_ledger_account_feature"),
        import_module("mfm.application.features.accounting.get_ledger_account_feature"),
        import_module("mfm.application.features.accounting.list_ledger_accounts_feature"),
        import_module("mfm.application.features.accounting.create_fiscal_year_feature"),
        import_module("mfm.application.features.accounting.open_fiscal_year_feature"),
        import_module("mfm.application.features.accounting.close_fiscal_year_feature"),
        import_module("mfm.application.features.accounting.get_fiscal_year_feature"),
        import_module("mfm.application.features.accounting.list_fiscal_years_feature"),
    ]

    for module in modules:
        text = (module.__doc__ or "") + "\n" + "\n".join(sorted(module.__dict__.keys()))
        lowered = text.lower()
        assert "sqlalchemy" not in lowered
        assert "sqlite" not in lowered
        assert "session" not in lowered
