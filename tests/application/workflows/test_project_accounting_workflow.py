from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.accounting import FiscalPeriodResponse
from mfm.application.features.accounting import FiscalYearResponse
from mfm.application.features.accounting import JournalLineResponse
from mfm.application.features.accounting import JournalResponse
from mfm.application.features.accounting import ListFiscalYearsResponse
from mfm.application.features.accounting import PostJournalResponse
from mfm.application.features.accounting.create_journal_feature import CreateJournalResponse
from mfm.application.features.accounting.get_journal_feature import GetJournalResponse
from mfm.application.features.projects import ExternalReferenceResponse
from mfm.application.features.projects import GetProjectResponse
from mfm.application.features.projects import ProjectResponse
from mfm.application.features.projects import UpdateProjectResponse
from mfm.application.workflows.project_accounting_workflow import ProjectAccountingWorkflow
from mfm.application.workflows.project_accounting_workflow import (
    ProjectAccountingWorkflowRequest,
)
from mfm.application.workflows.project_accounting_workflow import WorkflowExecutionError


@dataclass
class _State:
    project_id: UUID = uuid4()
    journal_id: UUID = uuid4()
    references: tuple[ExternalReferenceResponse, ...] = (
        ExternalReferenceResponse(
            reference_id=uuid4(),
            reference_type="DOCUMENT",
            external_id=uuid4(),
            description="BUDGET_STATUS:READY",
            created_at=datetime.now(UTC),
        ),
    )
    journal_status: str = "POSTED"


class _GetProjectFeature:
    def __init__(self, state: _State, *, should_fail: bool = False, budget_ready: bool = True) -> None:
        self.state = state
        self.should_fail = should_fail
        self.budget_ready = budget_ready

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("project not found")
        _ = request
        refs = self.state.references
        if not self.budget_ready:
            refs = tuple(
                ref
                for ref in refs
                if (ref.description or "").strip().upper() != "BUDGET_STATUS:READY"
            )

        return GetProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status="ACTIVE",
                priority="HIGH",
                description=None,
                start_date=None,
                end_date=None,
                created_at=datetime.now(UTC),
                updated_at=None,
                archived_at=None,
                version=1,
                milestones=(),
                activities=(),
                assignments=(),
                references=refs,
            )
        )


class _UpdateProjectFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("update failed")

        now = datetime.now(UTC)
        self.state.references = tuple(
            ExternalReferenceResponse(
                reference_id=ref.reference_id or uuid4(),
                reference_type=ref.reference_type,
                external_id=ref.external_id,
                description=ref.description,
                created_at=ref.created_at or now,
            )
            for ref in request.references or ()
        )

        return UpdateProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status="ACTIVE",
                priority="HIGH",
                description=None,
                start_date=None,
                end_date=None,
                created_at=now,
                updated_at=now,
                archived_at=None,
                version=1,
                milestones=(),
                activities=(),
                assignments=(),
                references=self.state.references,
            )
        )


class _CreateJournalFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("create journal failed")
        return CreateJournalResponse(
            journal=JournalResponse(
                journal_id=self.state.journal_id,
                journal_number=request.journal_number,
                posting_date=request.posting_date,
                description=request.description,
                reference=request.reference,
                status="DRAFT",
                version=1,
                lines=(
                    JournalLineResponse(
                        account_id=request.lines[0].account_id,
                        side="DEBIT",
                        amount=Decimal(request.lines[0].amount),
                        currency=request.lines[0].currency,
                        description=request.lines[0].description,
                    ),
                    JournalLineResponse(
                        account_id=request.lines[1].account_id,
                        side="CREDIT",
                        amount=Decimal(request.lines[1].amount),
                        currency=request.lines[1].currency,
                        description=request.lines[1].description,
                    ),
                ),
            )
        )


class _ListFiscalYearsFeature:
    def __init__(self, *, is_open: bool = True) -> None:
        self.is_open = is_open

    def execute(self, request):
        _ = request
        return ListFiscalYearsResponse(
            fiscal_years=(
                FiscalYearResponse(
                    fiscal_year_id=uuid4(),
                    year=2040,
                    start_date=date(2040, 1, 1),
                    end_date=date(2040, 12, 31),
                    status=("OPEN" if self.is_open else "CLOSED"),
                    periods=(
                        FiscalPeriodResponse(
                            number=1,
                            start_date=date(2040, 1, 1),
                            end_date=date(2040, 12, 31),
                            closed=not self.is_open,
                        ),
                    ),
                ),
            )
        )


class _PostJournalFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("post failed")
        _ = request
        self.state.journal_status = "POSTED"
        return PostJournalResponse(
            journal=JournalResponse(
                journal_id=self.state.journal_id,
                journal_number="JRN-WF005-001",
                posting_date=date(2040, 6, 15),
                description="Project transaction",
                reference=f"PROJECT:{self.state.project_id}",
                status="POSTED",
                version=2,
                lines=(
                    JournalLineResponse(
                        account_id=uuid4(),
                        side="DEBIT",
                        amount=Decimal("100.00"),
                        currency="DKK",
                        description="debit",
                    ),
                    JournalLineResponse(
                        account_id=uuid4(),
                        side="CREDIT",
                        amount=Decimal("100.00"),
                        currency="DKK",
                        description="credit",
                    ),
                ),
            )
        )


class _GetJournalFeature:
    def __init__(self, state: _State, *, invalid: bool = False) -> None:
        self.state = state
        self.invalid = invalid

    def execute(self, request):
        _ = request
        status = "DRAFT" if self.invalid else "POSTED"
        reference = "OTHER:123" if self.invalid else f"PROJECT:{self.state.project_id}"
        amount = Decimal("99.00") if self.invalid else Decimal("100.00")

        return GetJournalResponse(
            journal=JournalResponse(
                journal_id=self.state.journal_id,
                journal_number="JRN-WF005-001",
                posting_date=date(2040, 6, 15),
                description="Project transaction",
                reference=reference,
                status=status,
                version=2,
                lines=(
                    JournalLineResponse(
                        account_id=uuid4(),
                        side="DEBIT",
                        amount=Decimal("100.00"),
                        currency="DKK",
                        description="debit",
                    ),
                    JournalLineResponse(
                        account_id=uuid4(),
                        side="CREDIT",
                        amount=amount,
                        currency="DKK",
                        description="credit",
                    ),
                ),
            )
        )


def _workflow(
    *,
    project_missing: bool = False,
    budget_not_ready: bool = False,
    fiscal_year_closed: bool = False,
    post_fail: bool = False,
    link_fail: bool = False,
    invalid_integrity: bool = False,
):
    state = _State()
    workflow = ProjectAccountingWorkflow(
        get_project_feature=_GetProjectFeature(
            state,
            should_fail=project_missing,
            budget_ready=not budget_not_ready,
        ),
        update_project_feature=_UpdateProjectFeature(state, should_fail=link_fail),
        create_journal_feature=_CreateJournalFeature(state),
        list_fiscal_years_feature=_ListFiscalYearsFeature(is_open=not fiscal_year_closed),
        post_journal_feature=_PostJournalFeature(state, should_fail=post_fail),
        get_journal_feature=_GetJournalFeature(state, invalid=invalid_integrity),
    )
    return workflow, state


def _request(state: _State) -> ProjectAccountingWorkflowRequest:
    return ProjectAccountingWorkflowRequest(
        project_id=state.project_id,
        journal_number="JRN-WF005-001",
        posting_date=date(2040, 6, 15),
        transaction_description="Project transaction",
        debit_account_id=uuid4(),
        credit_account_id=uuid4(),
        amount=Decimal("100.00"),
    )


def test_workflow_happy_path() -> None:
    workflow, state = _workflow()

    response = workflow.execute(_request(state))

    assert response.project_id == state.project_id
    assert response.journal_id == state.journal_id
    assert response.journal_status == "POSTED"
    assert response.completed_steps == (
        "STEP-001",
        "STEP-002",
        "STEP-003",
        "STEP-004",
        "STEP-005",
        "STEP-006",
        "STEP-007",
    )


def test_failure_when_project_missing() -> None:
    workflow, state = _workflow(project_missing=True)

    with pytest.raises(WorkflowExecutionError, match="Verify project and budget READY failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_failure_when_budget_not_ready() -> None:
    workflow, state = _workflow(budget_not_ready=True)

    with pytest.raises(WorkflowExecutionError, match="Verify project and budget READY failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_failure_when_fiscal_year_not_open() -> None:
    workflow, state = _workflow(fiscal_year_closed=True)

    with pytest.raises(WorkflowExecutionError, match="Validate fiscal year OPEN failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-004"


def test_failure_when_post_fails() -> None:
    workflow, state = _workflow(post_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Post journal entry failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-005"


def test_failure_when_link_fails() -> None:
    workflow, state = _workflow(link_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Link transaction to project failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-006"


def test_failure_when_integrity_check_fails() -> None:
    workflow, state = _workflow(invalid_integrity=True)

    with pytest.raises(WorkflowExecutionError, match="Accounting integrity verification failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-007"
