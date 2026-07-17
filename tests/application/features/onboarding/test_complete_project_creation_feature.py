from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.complete_project_creation_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.complete_project_creation_feature import (
    CompleteProjectCreationFeature,
)
from mfm.application.features.onboarding.complete_project_creation_feature import (
    CompleteProjectCreationRequest,
)
from mfm.application.features.onboarding.complete_project_creation_feature import (
    ValidationException,
)
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflowResponse,
)
from mfm.application.workflows.complete_project_creation_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _ServiceStub:
    response: CompleteProjectCreationWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> CompleteProjectCreationRequest:
    return CompleteProjectCreationRequest(
        organization_id=uuid4(),
        organization_owner_contact_id=uuid4(),
        project_number="PRJ-FEAT-001",
        project_name="Feature Project",
        project_priority="HIGH",
        project_created_at=datetime(2036, 1, 1, 8, 0, tzinfo=UTC),
    )


def test_feature_happy_path() -> None:
    response = CompleteProjectCreationWorkflowResponse(
        project_id=uuid4(),
        project_status="ACTIVE",
        organization_id=uuid4(),
        project_document_library_id=uuid4(),
        project_budget_container_id=uuid4(),
        completed_steps=("STEP-001", "STEP-007"),
    )
    feature = CompleteProjectCreationFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.project_status == "ACTIVE"
    assert result.completed_steps == ("STEP-001", "STEP-007")


def test_feature_maps_workflow_execution_error() -> None:
    feature = CompleteProjectCreationFeature(
        service=_ServiceStub(error=WorkflowExecutionError("STEP-002", "Assign organization ownership failed"))
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-002"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = CompleteProjectCreationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="project_number"):
        feature.execute(
            CompleteProjectCreationRequest(
                organization_id=uuid4(),
                organization_owner_contact_id=uuid4(),
                project_number="",
                project_name="Feature Project",
            )
        )


def test_feature_rejects_naive_datetime() -> None:
    feature = CompleteProjectCreationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="timezone-aware"):
        feature.execute(
            CompleteProjectCreationRequest(
                organization_id=uuid4(),
                organization_owner_contact_id=uuid4(),
                project_number="PRJ-001",
                project_name="Feature Project",
                project_created_at=datetime(2036, 1, 1, 8, 0),
            )
        )
