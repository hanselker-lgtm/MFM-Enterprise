from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID

import pytest

from mfm.application.features.accounting import GetJournalResponse
from mfm.application.features.accounting import FiscalYearResponse
from mfm.application.features.accounting import JournalLineResponse
from mfm.application.features.accounting import JournalResponse
from mfm.application.features.accounting import JournalSearchResultResponse
from mfm.application.features.accounting import ListFiscalYearsResponse
from mfm.application.features.accounting import SearchJournalsResponse
from mfm.application.features.projects.create_project_feature import ExternalReferenceResponse
from mfm.application.features.projects.create_project_feature import ProjectResponse
from mfm.application.features.projects.get_project_feature import GetProjectResponse
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualRequest
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualService
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse


@dataclass(frozen=True)
class _GetProjectFeature:
    response: GetProjectResponse

    def execute(self, request):
        return self.response


@dataclass(frozen=True)
class _SearchJournalsFeature:
    response: SearchJournalsResponse

    def execute(self, request):
        return self.response


@dataclass(frozen=True)
class _GetJournalFeature:
    response: GetJournalResponse

    def execute(self, request):
        return self.response


@dataclass(frozen=True)
class _ListFiscalYearsFeature:
    response: ListFiscalYearsResponse

    def execute(self, request):
        return self.response


@pytest.fixture()
def project_id() -> UUID:
    return UUID("11111111-1111-1111-1111-111111111111")


@pytest.fixture()
def service(project_id: UUID) -> BudgetVsActualService:
    journal_id = UUID("22222222-2222-2222-2222-222222222222")
    return BudgetVsActualService(
        get_project_feature=_GetProjectFeature(
            GetProjectResponse(
                project=ProjectResponse(
                    project_id=project_id,
                    project_number="HP-001",
                    project_name="Harbor Project",
                    status="ACTIVE",
                    priority="NORMAL",
                    description=None,
                    start_date=datetime(2024, 1, 1, 8, 0),
                    end_date=None,
                    created_at=datetime(2024, 1, 1, 8, 0),
                    updated_at=None,
                    archived_at=None,
                    version=1,
                    milestones=(),
                    activities=(),
                    assignments=(),
                    references=(
                        ExternalReferenceResponse(
                            reference_id=UUID("44444444-4444-4444-4444-444444444444"),
                            reference_type="DOCUMENT",
                            external_id=UUID("55555555-5555-5555-5555-555555555555"),
                            description="BUDGET_STATUS:READY",
                            created_at=datetime(2024, 1, 2, 8, 0),
                        ),
                        ExternalReferenceResponse(
                            reference_id=UUID("66666666-6666-6666-6666-666666666666"),
                            reference_type="DOCUMENT",
                            external_id=UUID("77777777-7777-7777-7777-777777777777"),
                            description="BUDGET_CATEGORY:CAPEX",
                            created_at=datetime(2024, 1, 3, 8, 0),
                        ),
                    ),
                )
            )
        ),
        search_journals_feature=_SearchJournalsFeature(
            SearchJournalsResponse(
                journals=(
                    JournalSearchResultResponse(
                        journal_id=journal_id,
                        fiscal_year_id=UUID("88888888-8888-8888-8888-888888888888"),
                        journal_number="J-001",
                        posting_date=date(2024, 2, 1),
                        status="POSTED",
                        reference=f"project:{project_id}",
                    ),
                )
            )
        ),
        get_journal_feature=_GetJournalFeature(
            GetJournalResponse(
                journal=JournalResponse(
                    journal_id=journal_id,
                    journal_number="J-001",
                    posting_date=date(2024, 2, 1),
                    description="Project cost",
                    reference=f"project:{project_id}",
                    status="POSTED",
                    version=1,
                    lines=(
                        JournalLineResponse(account_id=UUID("99999999-9999-9999-9999-999999999999"), side="DEBIT", amount=Decimal("125.50"), currency="DKK", description="Materials"),
                        JournalLineResponse(account_id=UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"), side="CREDIT", amount=Decimal("125.50"), currency="DKK", description="Cash"),
                    ),
                )
            )
        ),
        list_fiscal_years_feature=_ListFiscalYearsFeature(
            ListFiscalYearsResponse(
                fiscal_years=(
                    FiscalYearResponse(
                        fiscal_year_id=UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"),
                        year=2024,
                        start_date=date(2024, 1, 1),
                        end_date=date(2024, 12, 31),
                        status="OPEN",
                        periods=(),
                    ),
                )
            )
        ),
    )


def test_budget_vs_actual_service_reports_null_planned_budget_and_explicit_confidence(service: BudgetVsActualService, project_id: UUID) -> None:
    response = service.execute(BudgetVsActualRequest(project_id=project_id))

    assert isinstance(response, BudgetVsActualResponse)
    assert response.project.project_id == project_id
    assert response.budget.planned_budget_total is None
    assert response.budget.budget_ready is True
    assert response.budget.budget_status == "READY"
    assert response.budget.budget_categories == ("CAPEX",)
    assert response.accounting.actual_total == Decimal("125.50")
    assert response.accounting.journal_count == 1
    assert response.accounting.last_journal_date == date(2024, 2, 1)
    assert response.accounting.fiscal_year == 2024
    assert response.variance.budget_variance is None
    assert response.variance.variance_percentage is None
    assert response.status.within_budget is None
    assert response.status.reporting_confidence == "LIMITED_BUDGET_METADATA"
