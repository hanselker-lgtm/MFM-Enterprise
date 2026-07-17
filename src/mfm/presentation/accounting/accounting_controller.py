"""Controller for accounting workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import GetJournalRequest
from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import ListJournalsRequest
from mfm.application.features.accounting import PostJournalRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingRequest,
)
from mfm.application.features.reporting import BudgetVsActualRequest
from mfm.application.features.reporting import ProjectStatusRequest
from mfm.presentation.accounting.accounting_viewmodels import CreateJournalCommandViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalAuditViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalDetailViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalFiscalYearViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalInfoViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalLineViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListFilterViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListItemViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalProjectLinkViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalProjectSummaryViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalSortField
from mfm.presentation.accounting.accounting_viewmodels import PaginationViewModel


class ListJournalsPort(Protocol):
    def execute(self, request: ListJournalsRequest): ...


class SearchJournalsPort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class GetJournalPort(Protocol):
    def execute(self, request: GetJournalRequest): ...


class PostJournalPort(Protocol):
    def execute(self, request: PostJournalRequest): ...


class ListFiscalYearsPort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class ProjectAccountingWorkflowPort(Protocol):
    def execute(self, request: ProjectAccountingRequest): ...


class ProjectStatusReportPort(Protocol):
    def execute(self, request: ProjectStatusRequest): ...


class BudgetVsActualReportPort(Protocol):
    def execute(self, request: BudgetVsActualRequest): ...


@dataclass(frozen=True, slots=True)
class AccountingNavigationCallbacks:
    to_project: Callable[[UUID], None] | None = None
    to_fiscal_year: Callable[[UUID], None] | None = None


class AccountingController:
    """UI controller that orchestrates accounting features and reporting features."""

    def __init__(
        self,
        *,
        list_journals_feature: ListJournalsPort,
        search_journals_feature: SearchJournalsPort,
        get_journal_feature: GetJournalPort,
        post_journal_feature: PostJournalPort,
        list_fiscal_years_feature: ListFiscalYearsPort,
        project_accounting_workflow_feature: ProjectAccountingWorkflowPort,
        project_status_feature: ProjectStatusReportPort,
        budget_vs_actual_feature: BudgetVsActualReportPort,
        navigation: AccountingNavigationCallbacks | None = None,
    ) -> None:
        self._list_journals = list_journals_feature
        self._search_journals = search_journals_feature
        self._get_journal = get_journal_feature
        self._post_journal = post_journal_feature
        self._list_fiscal_years = list_fiscal_years_feature
        self._project_accounting_workflow = project_accounting_workflow_feature
        self._project_status = project_status_feature
        self._budget_vs_actual = budget_vs_actual_feature
        self._navigation = navigation or AccountingNavigationCallbacks()
        self._last_filters = JournalListFilterViewModel()
        self._last_selected_journal_id: UUID | None = None

    @property
    def last_selected_journal_id(self) -> UUID | None:
        return self._last_selected_journal_id

    def load_journal_list(self, *, filters: JournalListFilterViewModel) -> JournalListViewModel:
        self._last_filters = filters

        if filters.text.strip() or filters.status != "ALL" or filters.fiscal_year is not None:
            status = None if filters.status == "ALL" else filters.status
            response = self._search_journals.execute(
                SearchJournalsRequest(
                    text=filters.text.strip() or None,
                    status=status,
                    fiscal_year=filters.fiscal_year,
                )
            )
            items = tuple(
                JournalListItemViewModel(
                    journal_id=item.journal_id,
                    fiscal_year_id=item.fiscal_year_id,
                    journal_number=item.journal_number,
                    posting_date=item.posting_date,
                    status=item.status,
                    reference=item.reference,
                )
                for item in response.journals
            )
        else:
            response = self._list_journals.execute(ListJournalsRequest())
            items = tuple(
                JournalListItemViewModel(
                    journal_id=item.journal_id,
                    fiscal_year_id=None,
                    journal_number=item.journal_number,
                    posting_date=item.posting_date,
                    status=item.status,
                    reference=item.reference,
                )
                for item in response.journals
            )

        sorted_items = self._sort_items(items, filters)
        paged_items, pagination = self._paginate(sorted_items, filters)
        return JournalListViewModel(filters=filters, items=paged_items, pagination=pagination)

    def open_journal(self, journal_id: UUID) -> JournalDetailViewModel:
        self._last_selected_journal_id = journal_id
        journal = self._get_journal.execute(GetJournalRequest(journal_id=journal_id)).journal
        fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years

        fiscal_match = next(
            (
                year
                for year in fiscal_years
                if year.start_date <= journal.posting_date <= year.end_date
            ),
            None,
        )
        project_id = self._extract_project_id(journal.reference)

        summary = JournalProjectSummaryViewModel(
            health_indicator=None,
            budget_status=None,
            actual_total=None,
            budget_variance=None,
        )
        if project_id is not None:
            status = self._project_status.execute(ProjectStatusRequest(project_id=project_id))
            budget = self._budget_vs_actual.execute(BudgetVsActualRequest(project_id=project_id))
            summary = JournalProjectSummaryViewModel(
                health_indicator=status.health.overall_health_indicator,
                budget_status=budget.budget.budget_status,
                actual_total=budget.accounting.actual_total,
                budget_variance=budget.variance.budget_variance,
            )

        return JournalDetailViewModel(
            journal=JournalInfoViewModel(
                journal_id=journal.journal_id,
                journal_number=journal.journal_number,
                posting_date=journal.posting_date,
                description=journal.description,
                reference=journal.reference,
                posting_status=journal.status,
            ),
            project_link=JournalProjectLinkViewModel(
                project_id=project_id,
                linked=project_id is not None,
            ),
            fiscal_year=JournalFiscalYearViewModel(
                fiscal_year_id=fiscal_match.fiscal_year_id if fiscal_match is not None else None,
                fiscal_year_label=str(fiscal_match.year) if fiscal_match is not None else "Unresolved",
            ),
            audit=JournalAuditViewModel(
                references=tuple(
                    item
                    for item in (
                        journal.reference,
                        f"JOURNAL:{journal.journal_number}",
                    )
                    if item
                )
            ),
            lines=tuple(
                JournalLineViewModel(
                    account_id=line.account_id,
                    side=line.side,
                    amount=line.amount,
                    currency=line.currency,
                    description=line.description,
                )
                for line in journal.lines
            ),
            project_summary=summary,
        )

    def create_journal(self, command: CreateJournalCommandViewModel) -> UUID:
        response = self._project_accounting_workflow.execute(
            ProjectAccountingRequest(
                project_id=command.project_id,
                journal_number=command.journal_number,
                posting_date=command.posting_date,
                transaction_description=command.description,
                debit_account_id=command.debit_account_id,
                credit_account_id=command.credit_account_id,
                amount=command.amount,
                currency=command.currency,
                transaction_reference=command.transaction_reference,
            )
        )
        self._last_selected_journal_id = response.journal_id
        return response.journal_id

    def post_journal(self, journal_id: UUID) -> None:
        self._post_journal.execute(PostJournalRequest(journal_id=journal_id))
        self._last_selected_journal_id = journal_id

    def refresh(self) -> tuple[JournalListViewModel, JournalDetailViewModel | None]:
        list_vm = self.load_journal_list(filters=self._last_filters)
        detail_vm = None
        if self._last_selected_journal_id is not None:
            detail_vm = self.open_journal(self._last_selected_journal_id)
        return list_vm, detail_vm

    def open_project(self, project_id: UUID) -> None:
        if self._navigation.to_project is not None:
            self._navigation.to_project(project_id)

    def open_fiscal_year(self, fiscal_year_id: UUID) -> None:
        if self._navigation.to_fiscal_year is not None:
            self._navigation.to_fiscal_year(fiscal_year_id)

    @staticmethod
    def _sort_items(
        items: tuple[JournalListItemViewModel, ...],
        filters: JournalListFilterViewModel,
    ) -> tuple[JournalListItemViewModel, ...]:
        key_map = {
            JournalSortField.JOURNAL_NUMBER: lambda value: value.journal_number,
            JournalSortField.POSTING_DATE: lambda value: value.posting_date,
            JournalSortField.STATUS: lambda value: value.status,
        }
        return tuple(sorted(items, key=key_map[filters.sort_by], reverse=filters.descending))

    @staticmethod
    def _paginate(
        items: tuple[JournalListItemViewModel, ...],
        filters: JournalListFilterViewModel,
    ) -> tuple[tuple[JournalListItemViewModel, ...], PaginationViewModel]:
        total_items = len(items)
        page_size = max(filters.page_size, 1)
        total_pages = max((total_items + page_size - 1) // page_size, 1)
        page = min(max(filters.page, 1), total_pages)
        start = (page - 1) * page_size
        end = start + page_size

        pagination = PaginationViewModel(
            page=page,
            page_size=page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_previous=page > 1,
            has_next=page < total_pages,
        )
        return tuple(items[start:end]), pagination

    @staticmethod
    def _extract_project_id(reference: str | None) -> UUID | None:
        if reference is None:
            return None

        token = "PROJECT:"
        start = reference.find(token)
        if start < 0:
            return None

        start += len(token)
        end = reference.find("|", start)
        raw = reference[start:] if end < 0 else reference[start:end]

        try:
            return UUID(raw.strip())
        except (TypeError, ValueError, AttributeError):
            return None
