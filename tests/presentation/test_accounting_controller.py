from __future__ import annotations

from datetime import date
from decimal import Decimal
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

from mfm.presentation.accounting import AccountingController
from mfm.presentation.accounting import AccountingNavigationCallbacks
from mfm.presentation.accounting import CreateJournalCommandViewModel
from mfm.presentation.accounting import JournalListFilterViewModel
from mfm.presentation.accounting import JournalSortField


class _StubPort:
    def __init__(self, response: object) -> None:
        self.response = response
        self.requests: list[object] = []

    def execute(self, request: object) -> object:
        self.requests.append(request)
        return self.response


def _list_item(number: str, posting_date: date) -> SimpleNamespace:
    return SimpleNamespace(
        journal_id=uuid4(),
        journal_number=number,
        posting_date=posting_date,
        status="DRAFT",
        reference=None,
    )


def test_accounting_controller_loads_and_paginates_journal_list() -> None:
    list_port = _StubPort(
        SimpleNamespace(
            journals=(
                _list_item("JRN-2", date(2025, 2, 1)),
                _list_item("JRN-1", date(2025, 1, 1)),
            )
        )
    )

    controller = AccountingController(
        list_journals_feature=list_port,
        search_journals_feature=_StubPort(SimpleNamespace(journals=())),
        get_journal_feature=_StubPort(None),
        post_journal_feature=_StubPort(None),
        list_fiscal_years_feature=_StubPort(SimpleNamespace(fiscal_years=())),
        project_accounting_workflow_feature=_StubPort(None),
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
    )

    vm = controller.load_journal_list(
        filters=JournalListFilterViewModel(
            sort_by=JournalSortField.JOURNAL_NUMBER,
            descending=False,
            page=1,
            page_size=1,
        )
    )

    assert len(list_port.requests) == 1
    assert vm.items[0].journal_number == "JRN-1"
    assert vm.pagination.total_items == 2
    assert vm.pagination.total_pages == 2


def test_accounting_controller_uses_search_when_filtering() -> None:
    search_port = _StubPort(
        SimpleNamespace(
            journals=(
                SimpleNamespace(
                    journal_id=uuid4(),
                    fiscal_year_id=uuid4(),
                    journal_number="JRN-S",
                    posting_date=date(2025, 3, 10),
                    status="POSTED",
                    reference="PROJECT:00000000-0000-0000-0000-000000000111",
                ),
            )
        )
    )

    controller = AccountingController(
        list_journals_feature=_StubPort(SimpleNamespace(journals=())),
        search_journals_feature=search_port,
        get_journal_feature=_StubPort(None),
        post_journal_feature=_StubPort(None),
        list_fiscal_years_feature=_StubPort(SimpleNamespace(fiscal_years=())),
        project_accounting_workflow_feature=_StubPort(None),
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
    )

    vm = controller.load_journal_list(filters=JournalListFilterViewModel(text="S"))

    assert len(search_port.requests) == 1
    assert vm.items[0].journal_number == "JRN-S"


def test_accounting_controller_maps_detail_and_navigation_callbacks() -> None:
    journal_id = uuid4()
    project_id = uuid4()
    fiscal_year_id = uuid4()
    project_calls: list[UUID] = []
    fiscal_calls: list[UUID] = []

    controller = AccountingController(
        list_journals_feature=_StubPort(SimpleNamespace(journals=())),
        search_journals_feature=_StubPort(SimpleNamespace(journals=())),
        get_journal_feature=_StubPort(
            SimpleNamespace(
                journal=SimpleNamespace(
                    journal_id=journal_id,
                    journal_number="JRN-100",
                    posting_date=date(2025, 5, 5),
                    description="Posting",
                    reference=f"PROJECT:{project_id}|REF:abc",
                    status="POSTED",
                    lines=(
                        SimpleNamespace(
                            account_id=uuid4(),
                            side="DEBIT",
                            amount=Decimal("100"),
                            currency="DKK",
                            description="d",
                        ),
                        SimpleNamespace(
                            account_id=uuid4(),
                            side="CREDIT",
                            amount=Decimal("100"),
                            currency="DKK",
                            description="c",
                        ),
                    ),
                )
            )
        ),
        post_journal_feature=_StubPort(None),
        list_fiscal_years_feature=_StubPort(
            SimpleNamespace(
                fiscal_years=(
                    SimpleNamespace(
                        fiscal_year_id=fiscal_year_id,
                        year=2025,
                        start_date=date(2025, 1, 1),
                        end_date=date(2025, 12, 31),
                    ),
                )
            )
        ),
        project_accounting_workflow_feature=_StubPort(None),
        project_status_feature=_StubPort(
            SimpleNamespace(
                health=SimpleNamespace(overall_health_indicator="GREEN"),
            )
        ),
        budget_vs_actual_feature=_StubPort(
            SimpleNamespace(
                budget=SimpleNamespace(budget_status="OK"),
                accounting=SimpleNamespace(actual_total=Decimal("100")),
                variance=SimpleNamespace(budget_variance=Decimal("0")),
            )
        ),
        navigation=AccountingNavigationCallbacks(
            to_project=lambda value: project_calls.append(value),
            to_fiscal_year=lambda value: fiscal_calls.append(value),
        ),
    )

    detail = controller.open_journal(journal_id)

    assert detail.journal.journal_number == "JRN-100"
    assert detail.project_link.project_id == project_id
    assert detail.fiscal_year.fiscal_year_id == fiscal_year_id

    controller.open_project(project_id)
    controller.open_fiscal_year(fiscal_year_id)

    assert project_calls == [project_id]
    assert fiscal_calls == [fiscal_year_id]


def test_accounting_controller_create_and_post_operations() -> None:
    created_journal_id = uuid4()
    post_port = _StubPort(None)
    workflow_port = _StubPort(SimpleNamespace(journal_id=created_journal_id))

    controller = AccountingController(
        list_journals_feature=_StubPort(SimpleNamespace(journals=())),
        search_journals_feature=_StubPort(SimpleNamespace(journals=())),
        get_journal_feature=_StubPort(None),
        post_journal_feature=post_port,
        list_fiscal_years_feature=_StubPort(SimpleNamespace(fiscal_years=())),
        project_accounting_workflow_feature=workflow_port,
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
    )

    journal_id = controller.create_journal(
        CreateJournalCommandViewModel(
            project_id=UUID("00000000-0000-0000-0000-000000000001"),
            journal_number="JRN-500",
            posting_date=date(2025, 1, 1),
            description="Create",
            debit_account_id=UUID("00000000-0000-0000-0000-000000000101"),
            credit_account_id=UUID("00000000-0000-0000-0000-000000000202"),
            amount=Decimal("50"),
        )
    )

    controller.post_journal(journal_id)

    assert journal_id == created_journal_id
    assert controller.last_selected_journal_id == created_journal_id
    assert len(workflow_port.requests) == 1
    assert len(post_port.requests) == 1
