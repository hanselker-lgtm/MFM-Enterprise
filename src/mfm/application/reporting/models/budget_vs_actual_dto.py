"""DTOs for REP-004 budget vs actual."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True, slots=True)
class BudgetVsActualProjectResponse:
    project_id: UUID
    project_name: str


@dataclass(frozen=True, slots=True)
class BudgetVsActualBudgetResponse:
    budget_status: str
    budget_categories: tuple[str, ...]
    planned_budget_total: Decimal | None
    budget_ready: bool


@dataclass(frozen=True, slots=True)
class BudgetVsActualAccountingResponse:
    actual_total: Decimal
    journal_count: int
    last_journal_date: date | None
    fiscal_year: int | None


@dataclass(frozen=True, slots=True)
class BudgetVsActualVarianceResponse:
    budget_variance: Decimal | None
    variance_percentage: Decimal | None


@dataclass(frozen=True, slots=True)
class BudgetVsActualStatusResponse:
    within_budget: bool | None
    reporting_confidence: str


@dataclass(frozen=True, slots=True)
class BudgetVsActualResponse:
    project: BudgetVsActualProjectResponse
    budget: BudgetVsActualBudgetResponse
    accounting: BudgetVsActualAccountingResponse
    variance: BudgetVsActualVarianceResponse
    status: BudgetVsActualStatusResponse


BudgetVsActualDTO = BudgetVsActualResponse
