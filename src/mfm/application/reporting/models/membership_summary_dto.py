"""DTOs for membership management summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class MembershipSummaryStatusTotalsDTO:
    total: int
    active: int
    suspended: int
    ended: int
    expired: int


@dataclass(frozen=True, slots=True)
class MembershipSummaryCategoryTotalsDTO:
    general: int
    youth: int
    senior: int
    family: int
    corporate: int


@dataclass(frozen=True, slots=True)
class MembershipSummaryResponse:
    status_totals: MembershipSummaryStatusTotalsDTO
    category_totals: MembershipSummaryCategoryTotalsDTO
    generated_at: datetime
