from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.project_budget_initialization_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.project_budget_initialization_feature import (
    ProjectBudgetInitializationFeature,
)
from mfm.application.features.onboarding.project_budget_initialization_feature import (
    ProjectBudgetInitializationRequest,
)
from mfm.application.features.onboarding.project_budget_initialization_feature import (
    ValidationException,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflowResponse,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _ServiceStub:
    response: ProjectBudgetInitializationWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ProjectBudgetInitializationRequest:
    return ProjectBudgetInitializationRequest(
        project_id=uuid4(),
        fiscal_year=2039,
    )


def test_feature_happy_path() -> None:
    response = ProjectBudgetInitializationWorkflowResponse(
        project_id=uuid4(),
        budget_container_id=uuid4(),
        budget_category_ids=(uuid4(), uuid4()),
        fiscal_year_id=uuid4(),
        budget_status="READY",
        completed_steps=("STEP-001", "STEP-007"),
    )
    feature = ProjectBudgetInitializationFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.budget_status == "READY"
    assert result.completed_steps == ("STEP-001", "STEP-007")


def test_feature_maps_workflow_execution_error() -> None:
    feature = ProjectBudgetInitializationFeature(
        service=_ServiceStub(
            error=WorkflowExecutionError("STEP-005", "Assign fiscal year failed")
        )
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-005"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = ProjectBudgetInitializationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="fiscal_year"):
        feature.execute(
            ProjectBudgetInitializationRequest(
                project_id=uuid4(),
                fiscal_year=1999,
            )
        )


def test_feature_rejects_empty_category_name() -> None:
    feature = ProjectBudgetInitializationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match=r"default_budget_categories\[1\]"):
        feature.execute(
            ProjectBudgetInitializationRequest(
                project_id=uuid4(),
                fiscal_year=2039,
                default_budget_categories=("LABOR", ""),
            )
        )
