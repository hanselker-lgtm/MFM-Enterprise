from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.accounting import CreateFiscalYearResponse
from mfm.application.features.accounting import CreateLedgerAccountResponse
from mfm.application.features.accounting import FiscalPeriodResponse
from mfm.application.features.accounting import FiscalYearResponse
from mfm.application.features.accounting import LedgerAccountResponse
from mfm.application.features.accounting import ListFiscalYearsResponse
from mfm.application.features.accounting import ListLedgerAccountsResponse
from mfm.application.features.documents import CreateDocumentResponse
from mfm.application.features.documents import DocumentResponse
from mfm.application.features.documents import ListDocumentsResponse
from mfm.application.features.organization import CreateOrganizationResponse
from mfm.application.features.organization import UpdateOrganizationResponse
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflow,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflowRequest,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    WorkflowExecutionError,
)
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@dataclass
class _State:
    organization_id: UUID = uuid4()
    document_id: UUID = uuid4()
    fiscal_year_id: UUID = uuid4()
    account_ids: tuple[UUID, ...] = (uuid4(), uuid4(), uuid4(), uuid4(), uuid4(), uuid4())
    updated_status: str = OrganizationStatus.INACTIVE.value


class _CreateOrganizationFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        _ = request
        return CreateOrganizationResponse(
            organization_id=self.state.organization_id,
            organization_number="ORG-001",
            name="Org",
        )


class _UpdateOrganizationFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        status = request.status.value if request.status is not None else self.state.updated_status
        self.state.updated_status = status
        return UpdateOrganizationResponse(
            organization_id=request.organization_id,
            organization_number="ORG-001",
            name="Org",
            status=status,
        )


class _CreateDocumentFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        now = datetime.now(UTC)
        return CreateDocumentResponse(
            document=DocumentResponse(
                document_id=self.state.document_id,
                document_number=request.document_number,
                document_title=request.document_title,
                document_type=request.document_type,
                status="ACTIVE",
                description=request.description,
                created_at=now,
                updated_at=None,
                archived_at=None,
                disposed_at=None,
                version=1,
                versions=(),
                references=(),
            )
        )


class _ListDocumentsFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        return ListDocumentsResponse(
            documents=(
                DocumentResponse(
                    document_id=self.state.document_id,
                    document_number="LIB-ORG-001",
                    document_title="Default Organization Library",
                    document_type="LIBRARY",
                    status="ACTIVE",
                    description=None,
                    created_at=now,
                    updated_at=None,
                    archived_at=None,
                    disposed_at=None,
                    version=1,
                    versions=(),
                    references=(),
                ),
            )
        )


class _CreateFiscalYearFeature:
    def __init__(self, state: _State, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("fiscal year create failed")
        return CreateFiscalYearResponse(
            fiscal_year=FiscalYearResponse(
                fiscal_year_id=self.state.fiscal_year_id,
                year=request.year,
                start_date=request.start_date,
                end_date=request.end_date,
                status="OPEN",
                periods=tuple(
                    FiscalPeriodResponse(
                        number=period.number,
                        start_date=period.start_date,
                        end_date=period.end_date,
                        closed=period.closed,
                    )
                    for period in request.periods
                ),
            )
        )


class _ListFiscalYearsFeature:
    def __init__(self, state: _State, year: int = 2030) -> None:
        self.state = state
        self.year = year

    def execute(self, request):
        _ = request
        return ListFiscalYearsResponse(
            fiscal_years=(
                FiscalYearResponse(
                    fiscal_year_id=self.state.fiscal_year_id,
                    year=self.year,
                    start_date=datetime(self.year, 1, 1, tzinfo=UTC).date(),
                    end_date=datetime(self.year, 12, 31, tzinfo=UTC).date(),
                    status="OPEN",
                    periods=(),
                ),
            )
        )


class _CreateLedgerAccountFeature:
    def __init__(self, state: _State) -> None:
        self.state = state
        self.index = 0

    def execute(self, request):
        account_id = self.state.account_ids[self.index]
        self.index += 1
        return CreateLedgerAccountResponse(
            account=LedgerAccountResponse(
                account_id=account_id,
                account_number=request.account_number,
                name=request.name,
                account_type=request.account_type,
                normal_balance=request.normal_balance,
                active=True,
                locked=False,
                has_postings=False,
            )
        )


class _ListLedgerAccountsFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        _ = request
        return ListLedgerAccountsResponse(
            accounts=tuple(
                LedgerAccountResponse(
                    account_id=account_id,
                    account_number=f"ACC-{idx}",
                    name="Account",
                    account_type="ASSET",
                    normal_balance="DEBIT",
                    active=True,
                    locked=False,
                    has_postings=False,
                )
                for idx, account_id in enumerate(self.state.account_ids, start=1)
            )
        )


def _workflow(*, fiscal_year_fail: bool = False, verification_year: int = 2030):
    state = _State()
    return CompleteOrganizationOnboardingWorkflow(
        create_organization_feature=_CreateOrganizationFeature(state),
        update_organization_feature=_UpdateOrganizationFeature(state),
        create_document_feature=_CreateDocumentFeature(state),
        list_documents_feature=_ListDocumentsFeature(state),
        create_fiscal_year_feature=_CreateFiscalYearFeature(state, should_fail=fiscal_year_fail),
        list_fiscal_years_feature=_ListFiscalYearsFeature(state, year=verification_year),
        create_ledger_account_feature=_CreateLedgerAccountFeature(state),
        list_ledger_accounts_feature=_ListLedgerAccountsFeature(state),
    )


def _request(year: int = 2030) -> CompleteOrganizationOnboardingWorkflowRequest:
    return CompleteOrganizationOnboardingWorkflowRequest(
        organization_number="ORG-ONB-001",
        organization_name="Onboarding Org",
        organization_type=OrganizationType.ASSOCIATION,
        fiscal_year=year,
    )


def test_workflow_happy_path() -> None:
    workflow = _workflow()

    result = workflow.execute(_request())

    assert result.organization_status == OrganizationStatus.ACTIVE.value
    assert result.completed_steps == (
        "STEP-001",
        "STEP-002",
        "STEP-003",
        "STEP-004",
        "STEP-005",
        "STEP-006",
        "STEP-007",
    )
    assert len(result.ledger_account_ids) == 6


def test_workflow_failure_on_fiscal_year_creation() -> None:
    workflow = _workflow(fiscal_year_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Create first fiscal year failed") as exc:
        workflow.execute(_request())

    assert exc.value.step == "STEP-004"


def test_workflow_failure_on_verification_when_year_missing() -> None:
    workflow = _workflow(verification_year=2099)

    with pytest.raises(WorkflowExecutionError, match="Fiscal year verification failed") as exc:
        workflow.execute(_request(year=2030))

    assert exc.value.step == "STEP-006"
