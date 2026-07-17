"""Application reporting service for REP-004 budget vs actual."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import GetJournalRequest
from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.projects import GetProjectRequest
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualAccountingResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualBudgetResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualDTO
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualStatusResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualVarianceResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualProjectResponse


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when dashboard request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when dependent feature APIs fail."""


@dataclass(frozen=True, slots=True)
class BudgetVsActualRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class GetJournalFeaturePort(Protocol):
    def execute(self, request: GetJournalRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class BudgetVsActualService:
    """Compose the budget-vs-actual report from existing feature APIs only."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        search_journals_feature: SearchJournalsFeaturePort,
        get_journal_feature: GetJournalFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._search_journals = search_journals_feature
        self._get_journal = get_journal_feature
        self._list_fiscal_years = list_fiscal_years_feature

    def execute(self, request: BudgetVsActualRequest) -> BudgetVsActualDTO:
        request.validate()

        try:
            project = self._get_project.execute(GetProjectRequest(project_id=request.project_id)).project
            journal_summaries = self._search_journals.execute(SearchJournalsRequest(status="POSTED")).journals
            fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Budget vs actual data retrieval failed") from exc

        project_journals = tuple(
            self._get_journal.execute(GetJournalRequest(journal_id=item.journal_id)).journal
            for item in journal_summaries
            if item.reference is not None and str(project.project_id) in item.reference
        )

        actual_total = self._sum_journal_amounts(project_journals)
        journal_count = len(project_journals)
        last_journal_date = max((journal.posting_date for journal in project_journals), default=None)

        budget_categories = tuple(self._budget_categories(project.references))
        budget_ready = any(
            ref.reference_type == "DOCUMENT"
            and (ref.description or "").strip().upper() == "BUDGET_STATUS:READY"
            for ref in project.references
        )
        budget_status = (
            "READY"
            if budget_ready
            else "MARKER_ONLY"
            if budget_categories
            else "UNAVAILABLE"
        )
        planned_budget_total = None

        fiscal_year = next(
            (
                item.year
                for item in fiscal_years
                if str(item.status).upper() == "OPEN" and item.year == last_journal_date.year
            ),
            None,
        ) if last_journal_date is not None else None
        if fiscal_year is None and last_journal_date is not None:
            fiscal_year = last_journal_date.year

        variance = None
        variance_percentage = None
        within_budget = None
        reporting_confidence = "LIMITED_BUDGET_METADATA"

        return BudgetVsActualResponse(
            project=BudgetVsActualProjectResponse(
                project_id=project.project_id,
                project_name=project.project_name,
            ),
            budget=BudgetVsActualBudgetResponse(
                budget_status=budget_status,
                budget_categories=budget_categories,
                planned_budget_total=planned_budget_total,
                budget_ready=budget_ready,
            ),
            accounting=BudgetVsActualAccountingResponse(
                actual_total=actual_total,
                journal_count=journal_count,
                last_journal_date=last_journal_date,
                fiscal_year=fiscal_year,
            ),
            variance=BudgetVsActualVarianceResponse(
                budget_variance=variance,
                variance_percentage=variance_percentage,
            ),
            status=BudgetVsActualStatusResponse(
                within_budget=within_budget,
                reporting_confidence=reporting_confidence,
            ),
        )

    @staticmethod
    def _budget_categories(references) -> list[str]:
        categories: list[str] = []
        for reference in references:
            description = (reference.description or "").strip().upper()
            if reference.reference_type != "DOCUMENT" or not description.startswith("BUDGET_CATEGORY:"):
                continue
            categories.append(description.split(":", 1)[1])
        return categories

    @staticmethod
    def _sum_journal_amounts(journals) -> Decimal:
        total = Decimal("0")
        for journal in journals:
            for line in journal.lines:
                if str(line.side).upper() == "DEBIT":
                    total += line.amount
        return total
