from __future__ import annotations

from datetime import date
from uuid import uuid4

from mfm.presentation.accounting.accounting_viewmodels import JournalDetailViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalFiscalYearViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalInfoViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListFilterViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListItemViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalProjectLinkViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalProjectSummaryViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalAuditViewModel
from mfm.presentation.accounting.accounting_viewmodels import PaginationViewModel
from mfm.presentation.accounting.accounting_workspace import AccountingWorkspace


class _WorkspaceControllerStub:
    def __init__(self) -> None:
        self.load_calls = 0
        self.last_filters: JournalListFilterViewModel | None = None

    @property
    def last_selected_journal_id(self):
        return None

    def load_journal_list(self, *, filters: JournalListFilterViewModel) -> JournalListViewModel:
        self.load_calls += 1
        self.last_filters = filters
        return JournalListViewModel(
            filters=filters,
            items=(
                JournalListItemViewModel(
                    journal_id=uuid4(),
                    fiscal_year_id=None,
                    journal_number="JRN-777",
                    posting_date=date(2025, 1, 1),
                    status="DRAFT",
                    reference=None,
                ),
            ),
            pagination=PaginationViewModel(
                page=filters.page,
                page_size=filters.page_size,
                total_items=1,
                total_pages=1,
                has_previous=False,
                has_next=False,
            ),
        )

    def refresh(self):
        return self.load_journal_list(filters=self.last_filters or JournalListFilterViewModel()), None

    def open_journal(self, journal_id):
        _ = journal_id
        return JournalDetailViewModel(
            journal=JournalInfoViewModel(
                journal_id=uuid4(),
                journal_number="JRN-777",
                posting_date=date(2025, 1, 1),
                description="",
                reference=None,
                posting_status="DRAFT",
            ),
            project_link=JournalProjectLinkViewModel(project_id=None, linked=False),
            fiscal_year=JournalFiscalYearViewModel(fiscal_year_id=None, fiscal_year_label="2025"),
            audit=JournalAuditViewModel(references=()),
            lines=(),
            project_summary=JournalProjectSummaryViewModel(
                health_indicator=None,
                budget_status=None,
                actual_total=None,
                budget_variance=None,
            ),
        )

    def create_journal(self, command):
        _ = command
        return uuid4()

    def post_journal(self, journal_id):
        _ = journal_id

    def open_project(self, project_id):
        _ = project_id

    def open_fiscal_year(self, fiscal_year_id):
        _ = fiscal_year_id


def test_accounting_workspace_performs_initial_lazy_load(qapp) -> None:
    controller = _WorkspaceControllerStub()

    _ = AccountingWorkspace(controller=controller)

    assert controller.load_calls == 1
