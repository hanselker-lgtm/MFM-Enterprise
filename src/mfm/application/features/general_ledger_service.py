"""General ledger application service."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.money import Money


class ApplicationException(Exception):
    """Base exception for application-level feature failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ListGeneralLedgerResponse:
    account_number: str
    account_name: str
    opening_balance_amount: Decimal
    opening_balance_currency: str
    debit_turnover_amount: Decimal
    debit_turnover_currency: str
    credit_turnover_amount: Decimal
    credit_turnover_currency: str
    closing_balance_amount: Decimal
    closing_balance_currency: str


@dataclass(frozen=True, slots=True)
class ListGeneralLedgerRequest:
    fiscal_year: int
    from_date: date
    to_date: date
    account_range: tuple[str, str] | None = None

    def validate(self) -> None:
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValidationException("fiscal_year must be an integer >= 2000")
        if not isinstance(self.from_date, date) or not isinstance(self.to_date, date):
            raise ValidationException("from_date and to_date must be date values")
        if self.from_date > self.to_date:
            raise ValidationException("from_date must be less than or equal to to_date")
        if self.account_range is not None:
            start, end = self.account_range
            if not isinstance(start, str) or not isinstance(end, str):
                raise ValidationException("account_range must contain string values")
            if not start.strip() or not end.strip():
                raise ValidationException("account_range values must be non-empty")
            if start.strip().upper() > end.strip().upper():
                raise ValidationException("account_range start must be <= end")


class LedgerAccountLike(Protocol):
    id: UUID
    name: str
    normal_balance: NormalBalance

    @property
    def account_number(self) -> object: ...


class JournalRepository(Protocol):
    def list(self) -> list[JournalEntry]: ...


class AccountRepository(Protocol):
    def list(self) -> list[LedgerAccountLike]: ...


class ListGeneralLedgerFeature:
    """Builds general ledger view dynamically from posted journal entries."""

    def __init__(
        self,
        *,
        journal_repository: JournalRepository,
        account_repository: AccountRepository,
    ) -> None:
        self._journal_repository = journal_repository
        self._account_repository = account_repository

    def execute(self, request: ListGeneralLedgerRequest) -> list[ListGeneralLedgerResponse]:
        request.validate()
        try:
            accounts = self._filter_accounts(
                self._account_repository.list(),
                request.account_range,
            )

            if not accounts:
                return []

            journals = [
                journal
                for journal in self._journal_repository.list()
                if journal.status is JournalEntryStatus.POSTED
                and journal.posting_date.year == request.fiscal_year
            ]
            journals.sort(key=lambda journal: journal.posting_date)

            opening_totals = self._build_zero_totals(accounts)
            debit_totals = self._build_zero_totals(accounts)
            credit_totals = self._build_zero_totals(accounts)

            for journal in journals:
                for line in journal.lines:
                    if line.account_id not in opening_totals:
                        continue

                    if line.side is PostingSide.DEBIT:
                        if journal.posting_date < request.from_date:
                            opening_totals[line.account_id] = (
                                opening_totals[line.account_id] + line.amount
                            )
                        elif request.from_date <= journal.posting_date <= request.to_date:
                            debit_totals[line.account_id] = (
                                debit_totals[line.account_id] + line.amount
                            )
                    elif line.side is PostingSide.CREDIT:
                        if journal.posting_date < request.from_date:
                            opening_totals[line.account_id] = (
                                opening_totals[line.account_id] - line.amount
                            )
                        elif request.from_date <= journal.posting_date <= request.to_date:
                            credit_totals[line.account_id] = (
                                credit_totals[line.account_id] + line.amount
                            )

            rows: list[ListGeneralLedgerResponse] = []
            for account in sorted(accounts, key=lambda item: str(item.account_number)):
                opening = opening_totals[account.id]
                debit = debit_totals[account.id]
                credit = credit_totals[account.id]
                if account.normal_balance is NormalBalance.DEBIT:
                    closing = opening + debit - credit
                else:
                    closing = opening - debit + credit

                rows.append(
                    ListGeneralLedgerResponse(
                        account_number=str(account.account_number),
                        account_name=account.name,
                        opening_balance_amount=opening.amount,
                        opening_balance_currency=self._currency_code(opening),
                        debit_turnover_amount=debit.amount,
                        debit_turnover_currency=self._currency_code(debit),
                        credit_turnover_amount=credit.amount,
                        credit_turnover_currency=self._currency_code(credit),
                        closing_balance_amount=closing.amount,
                        closing_balance_currency=self._currency_code(closing),
                    )
                )

            return rows
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("General ledger generation failed") from exc

    @staticmethod
    def _build_zero_totals(accounts: list[LedgerAccountLike]) -> dict[UUID, Money]:
        return {
            account.id: Money(amount=Decimal("0"), currency="DKK")
            for account in accounts
        }

    @staticmethod
    def _currency_code(value: Money) -> str:
        currency = value.currency
        return str(getattr(currency, "value", currency))

    @staticmethod
    def _filter_accounts(
        accounts: list[LedgerAccountLike],
        account_range: tuple[str, str] | None,
    ) -> list[LedgerAccountLike]:
        if account_range is None:
            return accounts

        start, end = account_range
        start_normalized = start.strip().upper()
        end_normalized = end.strip().upper()

        return [
            account
            for account in accounts
            if start_normalized <= str(account.account_number) <= end_normalized
        ]


class GeneralLedgerService(ListGeneralLedgerFeature):
    """Backward-compatible alias for the standardized feature."""


GeneralLedgerRequest = ListGeneralLedgerRequest
GeneralLedgerDTO = ListGeneralLedgerResponse
