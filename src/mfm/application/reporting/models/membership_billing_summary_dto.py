"""DTOs for membership billing summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class MembershipBillingSummaryItemDTO:
    membership_type_code: str
    membership_type_name: str
    currency: str
    fee_amount: str
    due_days: int
    reminders: int
    last_run_processed: int
    last_run_invoices_created: int


@dataclass(frozen=True, slots=True)
class MembershipBillingSummaryResponse:
    profiles: tuple[MembershipBillingSummaryItemDTO, ...]
    generated_at: datetime
