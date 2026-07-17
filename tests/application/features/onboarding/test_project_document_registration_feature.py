from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.project_document_registration_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.project_document_registration_feature import (
    ProjectDocumentRegistrationFeature,
)
from mfm.application.features.onboarding.project_document_registration_feature import (
    ProjectDocumentRegistrationRequest,
)
from mfm.application.features.onboarding.project_document_registration_feature import (
    ValidationException,
)
from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflowResponse,
)
from mfm.application.workflows.project_document_registration_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _ServiceStub:
    response: ProjectDocumentRegistrationWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ProjectDocumentRegistrationRequest:
    return ProjectDocumentRegistrationRequest(
        project_id=uuid4(),
        document_number="DOC-FEAT-001",
        document_title="Project Plan",
        initial_document_type="UNCLASSIFIED",
        classification_document_type="PROJECT_SPECIFICATION",
        created_at=datetime(2037, 1, 10, 8, 0, tzinfo=UTC),
    )


def test_feature_happy_path() -> None:
    response = ProjectDocumentRegistrationWorkflowResponse(
        project_id=uuid4(),
        document_id=uuid4(),
        classification_document_type="PROJECT_SPECIFICATION",
        completed_steps=("STEP-001", "STEP-007"),
    )
    feature = ProjectDocumentRegistrationFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.classification_document_type == "PROJECT_SPECIFICATION"
    assert result.completed_steps == ("STEP-001", "STEP-007")


def test_feature_maps_workflow_execution_error() -> None:
    feature = ProjectDocumentRegistrationFeature(
        service=_ServiceStub(
            error=WorkflowExecutionError("STEP-004", "Attach document to project failed")
        )
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-004"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = ProjectDocumentRegistrationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="document_number"):
        feature.execute(
            ProjectDocumentRegistrationRequest(
                project_id=uuid4(),
                document_number="",
                document_title="Project Plan",
            )
        )


def test_feature_rejects_naive_datetime() -> None:
    feature = ProjectDocumentRegistrationFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="timezone-aware"):
        feature.execute(
            ProjectDocumentRegistrationRequest(
                project_id=uuid4(),
                document_number="DOC-001",
                document_title="Project Plan",
                created_at=datetime(2037, 1, 10, 8, 0),
            )
        )
