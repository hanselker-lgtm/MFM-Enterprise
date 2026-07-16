"""Create Journal use case and shared accounting journal DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any
from typing import Mapping
from uuid import UUID
from uuid import uuid4

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.accounting.repositories import FiscalYearRepository
from mfm.domain.accounting.repositories import JournalRepository
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money


class ApplicationException(Exception):
    """Base exception for accounting application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


@dataclass(frozen=True, slots=True)
class JournalLineInput:
    account_id: UUID
    side: str
    amount: Decimal | str | int
    currency: str = "DKK"
    description: str | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.account_id, UUID):
            raise ValidationException(f"{field_name}.account_id must be UUID")
        if not isinstance(self.side, str) or not self.side.strip():
            raise ValidationException(f"{field_name}.side must be a non-empty string")
        if isinstance(self.amount, bool) or isinstance(self.amount, float):
            raise ValidationException(
                f"{field_name}.amount must not be bool/float"
            )
        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValidationException(f"{field_name}.currency must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")


@dataclass(frozen=True, slots=True)
class JournalLineResponse:
    account_id: UUID
    side: str
    amount: Decimal
    currency: str
    description: str | None


@dataclass(frozen=True, slots=True)
class JournalResponse:
    journal_id: UUID
    journal_number: str
    posting_date: date
    description: str
    reference: str | None
    status: str
    version: int
    lines: tuple[JournalLineResponse, ...]


@dataclass(frozen=True, slots=True)
class JournalSearchResultResponse:
    journal_id: UUID
    fiscal_year_id: UUID
    journal_number: str
    posting_date: date
    status: str
    reference: str | None


@dataclass(frozen=True, slots=True)
class CreateJournalRequest:
    journal_number: str
    posting_date: date
    description: str
    lines: tuple[JournalLineInput, ...]
    journal_id: UUID | None = None
    reference: str | None = None
    status: str = "DRAFT"

    def validate(self) -> None:
        if not isinstance(self.journal_number, str) or not self.journal_number.strip():
            raise ValidationException("journal_number must be a non-empty string")
        if not isinstance(self.posting_date, date):
            raise ValidationException("posting_date must be date")
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValidationException("description must be a non-empty string")
        if self.journal_id is not None and not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID or None")
        if self.reference is not None and not isinstance(self.reference, str):
            raise ValidationException("reference must be string or None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if not isinstance(self.lines, tuple):
            raise ValidationException("lines must be tuple")
        if len(self.lines) < 2:
            raise ValidationException("lines must contain at least two entries")

        for index, line in enumerate(self.lines):
            line.validate(field_name=f"lines[{index}]")


@dataclass(frozen=True, slots=True)
class CreateJournalResponse:
    journal: JournalResponse


class CreateJournalUseCase:
    """Create journal aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateJournalRequest) -> CreateJournalResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                journal_repository: JournalRepository = uow.journal_repository
                fiscal_year_repository: FiscalYearRepository = uow.fiscal_year_repository

                fiscal_year = fiscal_year_repository.get_by_year(request.posting_date.year)
                if fiscal_year is None:
                    raise BusinessRuleViolation(
                        f"Fiscal year {request.posting_date.year} does not exist"
                    )

                fiscal_year.ensure_posting_allowed(request.posting_date)

                journal = Journal(
                    id=request.journal_id or uuid4(),
                    journal_number=request.journal_number,
                    posting_date=request.posting_date,
                    description=request.description,
                    lines=[to_journal_line(item) for item in request.lines],
                    reference=request.reference,
                    status=JournalEntryStatus(request.status.strip().upper()),
                )

                journal_repository.add(journal)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create journal failed") from exc

        return CreateJournalResponse(journal=to_journal_response(journal))


def to_journal_line(value: JournalLineInput) -> JournalLine:
    return JournalLine(
        account_id=value.account_id,
        side=PostingSide(value.side.strip().upper()),
        amount=Money(amount=value.amount, currency=Currency(value.currency.strip().upper())),
        description=value.description,
    )


def to_journal_line_response(value: JournalLine) -> JournalLineResponse:
    return JournalLineResponse(
        account_id=value.account_id,
        side=value.side.value,
        amount=value.amount.amount,
        currency=value.amount.currency.value,
        description=value.description,
    )


def to_journal_response(value: Journal) -> JournalResponse:
    return JournalResponse(
        journal_id=value.id,
        journal_number=value.journal_number,
        posting_date=value.posting_date,
        description=value.description,
        reference=value.reference,
        status=value.status.value,
        version=value.version,
        lines=tuple(to_journal_line_response(line) for line in value.lines),
    )


def _as_string(value: Any) -> str:
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def to_journal_search_result_response(
    value: Mapping[str, Any],
) -> JournalSearchResultResponse:
    return JournalSearchResultResponse(
        journal_id=UUID(str(value["id"])),
        fiscal_year_id=UUID(str(value["fiscal_year_id"])),
        journal_number=str(value["journal_number"]),
        posting_date=value["posting_date"],
        status=_as_string(value["status"]),
        reference=(
            None
            if value.get("reference") is None
            else str(value["reference"])
        ),
    )
