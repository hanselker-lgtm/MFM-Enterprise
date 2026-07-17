from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.project_closure_archive_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.project_closure_archive_feature import (
    ProjectClosureArchiveFeature,
)
from mfm.application.features.onboarding.project_closure_archive_feature import (
    ProjectClosureArchiveRequest,
)
from mfm.application.features.onboarding.project_closure_archive_feature import (
    ValidationException,
)
from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflowResponse,
)
from mfm.application.workflows.project_closure_archive_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _ServiceStub:
    response: ProjectClosureArchiveWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ProjectClosureArchiveRequest:
    return ProjectClosureArchiveRequest(
        project_id=uuid4(),
        archived_at=datetime(2041, 12, 31, 10, 0, tzinfo=UTC),
    )


def test_feature_happy_path() -> None:
    response = ProjectClosureArchiveWorkflowResponse(
        project_id=uuid4(),
        archive_manifest_id=uuid4(),
        project_status="ARCHIVED",
        closure_status="CLOSED",
        completed_steps=("STEP-001", "STEP-008"),
    )
    feature = ProjectClosureArchiveFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.project_status == "ARCHIVED"
    assert result.closure_status == "CLOSED"


def test_feature_maps_workflow_execution_error() -> None:
    feature = ProjectClosureArchiveFeature(
        service=_ServiceStub(
            error=WorkflowExecutionError("STEP-004", "Verify no unposted accounting journals remain failed")
        )
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-004"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = ProjectClosureArchiveFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="archive_manifest_title"):
        feature.execute(
            ProjectClosureArchiveRequest(
                project_id=uuid4(),
                archive_manifest_title="",
            )
        )


def test_feature_rejects_naive_datetime() -> None:
    feature = ProjectClosureArchiveFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="timezone-aware"):
        feature.execute(
            ProjectClosureArchiveRequest(
                project_id=uuid4(),
                archived_at=datetime(2041, 12, 31, 10, 0),
            )
        )
