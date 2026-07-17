"""Aggregate root for membership billing capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID

from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.reminder import Reminder


@dataclass(slots=True)
class MembershipBillingRun:
    """Historical record of one billing execution."""

    fiscal_year: int
    billing_date: date
    processed: int
    invoices_created: int
    journals_created: int
    skipped: int
    errors: tuple[str, ...] = ()


@dataclass(slots=True)
class MembershipBillingProfile:
    """Billing profile for one membership type."""

    membership_type_id: UUID
    fee_schedule: FeeSchedule
    reminders: list[Reminder] = field(default_factory=list)
    runs: list[MembershipBillingRun] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not isinstance(self.membership_type_id, UUID):
            raise ValueError("membership_type_id must be UUID")
        if not isinstance(self.fee_schedule, FeeSchedule):
            raise ValueError("fee_schedule must be FeeSchedule")

        self.reminders = list(self.reminders)
        self.runs = list(self.runs)

    def add_reminder(self, reminder: Reminder) -> None:
        if any(item.id == reminder.id for item in self.reminders):
            raise ValueError(f"Reminder {reminder.id} already exists")
        self.reminders.append(reminder)

    def add_run(self, run: MembershipBillingRun) -> None:
        self.runs.append(run)
