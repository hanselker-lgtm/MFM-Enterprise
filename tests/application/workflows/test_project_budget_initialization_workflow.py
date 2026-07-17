from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.accounting import FiscalPeriodResponse
from mfm.application.features.accounting import FiscalYearResponse
from mfm.application.features.accounting import LedgerAccountResponse
from mfm.application.features.accounting import ListFiscalYearsResponse
from mfm.application.features.accounting import ListLedgerAccountsResponse
from mfm.application.features.projects import ExternalReferenceResponse
from mfm.application.features.projects import GetProjectResponse
from mfm.application.features.projects import ProjectResponse
from mfm.application.features.projects import UpdateProjectResponse
from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflow,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflowRequest,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _State:
    project_id: UUID = uuid4()
    references: tuple[ExternalReferenceResponse, ...] = ()


class _GetProjectFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("project not found")
        _ = request
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
                references=self.state.references,
            )
        )


class _UpdateProjectFeature:
    def __init__(self, state: _State, *, fail_for_description_prefix: str | None = None) -> None:
        self.state = state
        self.fail_for_description_prefix = fail_for_description_prefix

    def execute(self, request):
        if self.fail_for_description_prefix is not None:
            for ref in request.references or ():
                if (ref.description or "").startswith(self.fail_for_description_prefix):
                    raise RuntimeError("update failed")

        now = datetime.now(UTC)
        references = tuple(
            ExternalReferenceResponse(
                reference_id=ref.reference_id or uuid4(),
                reference_type=ref.reference_type,
                external_id=ref.external_id,
                description=ref.description,
                created_at=ref.created_at or now,
            )
            for ref in request.references or ()
        )
        self.state.references = references

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


class _ListFiscalYearsFeature:
    def __init__(self, *, include_year: bool = True) -> None:
        self.include_year = include_year

    def execute(self, request):
        _ = request
        fiscal_years: tuple[FiscalYearResponse, ...]
        if self.include_year:
            fiscal_years = (
                FiscalYearResponse(
                    fiscal_year_id=uuid4(),
                    year=2039,
                    start_date=date(2039, 1, 1),
                    end_date=date(2039, 12, 31),
                    status="OPEN",
                    periods=(
                        FiscalPeriodResponse(
                            number=1,
                            start_date=date(2039, 1, 1),
                            end_date=date(2039, 12, 31),
                            closed=False,
                        ),
                    ),
                ),
            )
        else:
            fiscal_years = ()

        return ListFiscalYearsResponse(fiscal_years=fiscal_years)


class _ListLedgerAccountsFeature:
    def __init__(self, *, include_accounts: bool = True) -> None:
        self.include_accounts = include_accounts

    def execute(self, request):
        _ = request
        accounts: tuple[LedgerAccountResponse, ...]
        if self.include_accounts:
            accounts = (
                LedgerAccountResponse(
                    account_id=uuid4(),
                    account_number="4000-REV",
                    name="Revenue",
                    account_type="INCOME",
                    normal_balance="CREDIT",
                    active=True,
                    locked=False,
                    has_postings=False,
                ),
            )
        else:
            accounts = ()

        return ListLedgerAccountsResponse(accounts=accounts)


def _workflow(
    *,
    project_missing: bool = False,
    fiscal_year_missing: bool = False,
    accounts_missing: bool = False,
    fail_ready_update: bool = False,
) -> tuple[ProjectBudgetInitializationWorkflow, _State]:
    state = _State()
    workflow = ProjectBudgetInitializationWorkflow(
        get_project_feature=_GetProjectFeature(state, should_fail=project_missing),
        update_project_feature=_UpdateProjectFeature(
            state,
            fail_for_description_prefix=(
                "BUDGET_STATUS:" if fail_ready_update else None
            ),
        ),
        list_fiscal_years_feature=_ListFiscalYearsFeature(include_year=not fiscal_year_missing),
        list_ledger_accounts_feature=_ListLedgerAccountsFeature(
            include_accounts=not accounts_missing
        ),
    )
    return workflow, state


def _request(state: _State) -> ProjectBudgetInitializationWorkflowRequest:
    return ProjectBudgetInitializationWorkflowRequest(
        project_id=state.project_id,
        fiscal_year=2039,
    )


def test_workflow_happy_path() -> None:
    workflow, state = _workflow()

    result = workflow.execute(_request(state))

    assert result.project_id == state.project_id
    assert result.budget_status == "READY"
    assert len(result.budget_category_ids) == 5
    assert result.completed_steps == (
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

    with pytest.raises(WorkflowExecutionError, match="Verify project exists failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_failure_when_fiscal_year_missing() -> None:
    workflow, state = _workflow(fiscal_year_missing=True)

    with pytest.raises(WorkflowExecutionError, match="Assign fiscal year failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-005"


def test_failure_when_budget_structure_invalid() -> None:
    workflow, state = _workflow(accounts_missing=True)

    with pytest.raises(WorkflowExecutionError, match="Budget structure validation failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-006"


def test_failure_when_mark_ready_fails() -> None:
    workflow, state = _workflow(fail_ready_update=True)

    with pytest.raises(WorkflowExecutionError, match="Mark budget READY failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-007"
