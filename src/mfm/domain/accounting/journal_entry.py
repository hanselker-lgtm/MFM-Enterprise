"""Journal entry aggregate for accounting."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from decimal import Decimal
from enum import Enum
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.accounting.exceptions import InvalidJournalBalanceError
from mfm.domain.accounting.exceptions import InvalidJournalLineError
from mfm.domain.accounting.exceptions import InvalidJournalReferenceError
from mfm.domain.accounting.exceptions import InvalidJournalTransitionError
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.money import Money


class JournalEntryStatus(str, Enum):
    """Status for journal entry lifecycle."""

    DRAFT = "DRAFT"
    POSTED = "POSTED"
    REVERSED = "REVERSED"


@dataclass(slots=True)
class JournalEntry(AggregateRoot):
    """Aggregate root for a balanced accounting journal entry."""

    posting_date: date
    description: str
    lines: list[JournalLine]
    reference: str | None = None
    status: JournalEntryStatus = JournalEntryStatus.DRAFT
    id: UUID = field(default_factory=uuid4)
    _journal_number: str = field(default="", repr=False)

    def __init__(
        self,
        *,
        journal_number: str,
        posting_date: date,
        description: str,
        lines: list[JournalLine],
        reference: str | None = None,
        status: JournalEntryStatus = JournalEntryStatus.DRAFT,
        id: UUID | None = None,
    ) -> None:
        self._journal_number = journal_number
        self.posting_date = posting_date
        self.description = description
        self.lines = lines
        self.reference = reference
        self.status = status
        self.id = uuid4() if id is None else id
        self.__post_init__()

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, UUID):
            raise InvalidJournalReferenceError("id must be a UUID")

        if not isinstance(self._journal_number, str) or not self._journal_number.strip():
            raise InvalidJournalReferenceError("journal_number must be a non-empty string")

        self._journal_number = self._journal_number.strip().upper()

        if not isinstance(self.posting_date, date):
            raise InvalidJournalReferenceError("posting_date must be a date")

        if not isinstance(self.description, str) or not self.description.strip():
            raise InvalidJournalReferenceError("description must be a non-empty string")

        self.description = self.description.strip()

        if self.reference is not None:
            if not isinstance(self.reference, str):
                raise InvalidJournalReferenceError("reference must be a string")
            normalized_reference = self.reference.strip()
            self.reference = normalized_reference or None

        if not isinstance(self.status, JournalEntryStatus):
            raise InvalidJournalReferenceError("status must be JournalEntryStatus")

        if not isinstance(self.lines, list):
            raise InvalidJournalLineError("lines must be a list")

        for line in self.lines:
            if not isinstance(line, JournalLine):
                raise InvalidJournalLineError("all lines must be JournalLine")

        self.validate()

    @property
    def journal_number(self) -> str:
        return self._journal_number

    def add_line(self, line: JournalLine) -> None:
        self._assert_modifiable()
        if not isinstance(line, JournalLine):
            raise InvalidJournalLineError("line must be JournalLine")

        if self.lines and line.amount.currency != self.lines[0].amount.currency:
            raise InvalidJournalLineError("all journal lines must use same currency")

        self.lines.append(line)

    def remove_line(self, line: JournalLine) -> None:
        self._assert_modifiable()
        if line not in self.lines:
            raise InvalidJournalLineError("line does not exist on journal")
        if len(self.lines) <= 2:
            raise InvalidJournalLineError("journal must contain at least two lines")
        self.lines.remove(line)

    def validate(self) -> None:
        if len(self.lines) < 2:
            raise InvalidJournalLineError("journal must contain at least two lines")

        for line in self.lines:
            if line.amount.amount <= Decimal("0"):
                raise InvalidJournalLineError("journal lines cannot be zero or negative")

        if not self.is_balanced():
            raise InvalidJournalBalanceError("total debit must equal total credit")

    def post(self) -> None:
        if self.status == JournalEntryStatus.POSTED:
            raise InvalidJournalTransitionError("POSTED journal cannot be changed")
        if self.status == JournalEntryStatus.REVERSED:
            raise InvalidJournalTransitionError("REVERSED journal cannot be posted again")

        self.validate()
        self.status = JournalEntryStatus.POSTED

    @classmethod
    def create_for_fiscal_year(
        cls,
        *,
        fiscal_year: FiscalYear,
        journal_number: str,
        posting_date: date,
        description: str,
        lines: list[JournalLine],
        reference: str | None = None,
        status: JournalEntryStatus = JournalEntryStatus.DRAFT,
        id: UUID | None = None,
    ) -> JournalEntry:
        fiscal_year.ensure_posting_allowed(posting_date)
        normalized_number = fiscal_year.register_journal_number(journal_number)

        return cls(
            journal_number=normalized_number,
            posting_date=posting_date,
            description=description,
            lines=lines,
            reference=reference,
            status=status,
            id=id,
        )

    def post_in_fiscal_year(self, *, fiscal_year: FiscalYear) -> None:
        fiscal_year.ensure_posting_allowed(self.posting_date)
        self.post()

    def reverse(self) -> None:
        if self.status == JournalEntryStatus.DRAFT:
            raise InvalidJournalTransitionError("DRAFT journal must be posted before reverse")
        if self.status == JournalEntryStatus.REVERSED:
            raise InvalidJournalTransitionError("journal is already reversed")

        self.status = JournalEntryStatus.REVERSED

    def total_debit(self) -> Money:
        currency = self.lines[0].amount.currency
        total = Money(amount=Decimal("0"), currency=currency)
        for line in self.lines:
            if line.side == PostingSide.DEBIT:
                total = total + line.amount
        return total

    def total_credit(self) -> Money:
        currency = self.lines[0].amount.currency
        total = Money(amount=Decimal("0"), currency=currency)
        for line in self.lines:
            if line.side == PostingSide.CREDIT:
                total = total + line.amount
        return total

    def is_balanced(self) -> bool:
        return self.total_debit() == self.total_credit()

    def _assert_modifiable(self) -> None:
        if self.status == JournalEntryStatus.POSTED:
            raise InvalidJournalTransitionError("POSTED journal cannot be changed")
        if self.status == JournalEntryStatus.REVERSED:
            raise InvalidJournalTransitionError("REVERSED journal cannot be posted again")
