"""Accounting domain events."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class ChartOfAccountsLocked(DomainEvent):
    chart_id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class LedgerAccountCreated(DomainEvent):
    account_id: UUID = field(default_factory=uuid4)
    account_number: str = ""


@dataclass(slots=True)
class LedgerAccountRenamed(DomainEvent):
    account_id: UUID = field(default_factory=uuid4)
    name: str = ""


@dataclass(slots=True)
class LedgerAccountLocked(DomainEvent):
    account_id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class JournalEntryDrafted(DomainEvent):
    journal_id: UUID = field(default_factory=uuid4)
    journal_number: str = ""


@dataclass(slots=True)
class JournalEntryPosted(DomainEvent):
    journal_id: UUID = field(default_factory=uuid4)
    journal_number: str = ""


@dataclass(slots=True)
class JournalEntryReversed(DomainEvent):
    journal_id: UUID = field(default_factory=uuid4)
    journal_number: str = ""


@dataclass(slots=True)
class FiscalPeriodClosed(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    period_number: int = 0


@dataclass(slots=True)
class FiscalPeriodReopened(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    period_number: int = 0


@dataclass(slots=True)
class FiscalYearClosed(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    year: int = 0


@dataclass(slots=True)
class FiscalYearReopened(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    year: int = 0


@dataclass(slots=True)
class FiscalYearArchived(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    year: int = 0


@dataclass(slots=True)
class OpeningBalanceRegistered(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    effective_date: date = field(default_factory=lambda: datetime.now(UTC).date())


@dataclass(slots=True)
class ClosingBalanceFinalized(DomainEvent):
    fiscal_year_id: UUID = field(default_factory=uuid4)
    effective_date: date = field(default_factory=lambda: datetime.now(UTC).date())
