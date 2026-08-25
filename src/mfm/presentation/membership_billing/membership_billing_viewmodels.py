"""Pure view-model types for the Membership Billing workspace (no Qt imports)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True, slots=True)
class FeeScheduleListItemViewModel:
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    fee_amount: str
    currency: str
    due_days: int
    reminder_count: int


@dataclass(frozen=True, slots=True)
class FeeScheduleListViewModel:
    items: tuple[FeeScheduleListItemViewModel, ...]


@dataclass(frozen=True, slots=True)
class SetupFeeScheduleCommandViewModel:
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    amount: str
    currency: str
    due_days: int


@dataclass(frozen=True, slots=True)
class RunBillingCommandViewModel:
    membership_type_id: UUID
    fiscal_year: int
    billing_date: date
    dry_run: bool = False


@dataclass(frozen=True, slots=True)
class RunBillingResultViewModel:
    processed: int
    invoices_created: int
    reminder_count: int
