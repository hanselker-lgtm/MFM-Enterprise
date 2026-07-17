from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID

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
from mfm.application.features.reporting.budget_vs_actual_feature import BudgetVsActualFeature
from mfm.application.features.reporting.budget_vs_actual_feature import BudgetVsActualRequest
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualService


@dataclass(frozen=True)
class _Stub:
    response: object

    def execute(self, request):
        return self.response


def test_budget_vs_actual_feature_returns_reporting_confidence() -> None:
    project_id = UUID("11111111-1111-1111-1111-111111111111")
    journal_id = UUID("22222222-2222-2222-2222-222222222222")

    service = BudgetVsActualService(
        get_project_feature=_Stub(
            GetProjectResponse(
                project=ProjectResponse(
                    project_id=project_id,
                    project_number="HP-001",
                    project_name="Harbor Project",
                    status="ACTIVE",
                    priority="NORMAL",
                    description=None,
                    start_date=date(2024, 1, 1),
                    end_date=None,
                    created_at=date(2024, 1, 1),
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
                            created_at=date(2024, 1, 2),
                        ),
                    ),
                )
            )
        ),
        search_journals_feature=_Stub(
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
        get_journal_feature=_Stub(
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
        list_fiscal_years_feature=_Stub(
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

    feature = BudgetVsActualFeature(service=service)
    response = feature.execute(BudgetVsActualRequest(project_id=project_id))

    assert response.status.reporting_confidence == "LIMITED_BUDGET_METADATA"
    assert response.budget.planned_budget_total is None
    assert response.accounting.actual_total == Decimal("125.50")
