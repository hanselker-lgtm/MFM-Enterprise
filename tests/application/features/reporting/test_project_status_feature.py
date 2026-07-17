from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.project_status_feature import ProjectStatusFeature
from mfm.application.features.reporting.project_status_feature import ProjectStatusRequest
from mfm.application.features.reporting.project_status_feature import RepositoryException
from mfm.application.features.reporting.project_status_feature import ValidationException
from mfm.application.reporting.models.project_status_dto import ProjectStatusAccountingResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusArchiveResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusBudgetResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusDTO
from mfm.application.reporting.models.project_status_dto import ProjectStatusDocumentsResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusHealthResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusOrganizationResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusProjectResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.application.reporting.project_status_service import (
    ValidationException as ServiceValidationException,
)


@dataclass
class _ServiceStub:
    response: ProjectStatusDTO | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ProjectStatusRequest:
    return ProjectStatusRequest(project_id=uuid4())


def test_feature_happy_path() -> None:
    project_id = uuid4()
    response = ProjectStatusResponse(
        project=ProjectStatusProjectResponse(
            project_id=project_id,
            name="Project Alpha",
            status="ACTIVE",
            created_date=date(2040, 1, 1),
            last_updated=datetime(2040, 2, 1, 8, 0, tzinfo=UTC),
            organization=ProjectStatusOrganizationResponse(
                organization_id=uuid4(),
                name=None,
                status=None,
            ),
        ),
        documents=ProjectStatusDocumentsResponse(
            total_documents=2,
            finalized_documents=1,
            outstanding_documents=1,
        ),
        budget=ProjectStatusBudgetResponse(
            budget_status="READY",
            budget_categories=("LABOR", "MATERIALS"),
            budget_ready=True,
        ),
        accounting=ProjectStatusAccountingResponse(
            journal_count=2,
            last_journal="JRN-002",
            fiscal_year=2040,
            accounting_status="COMPLETE",
        ),
        archive=ProjectStatusArchiveResponse(
            archive_status="READY_FOR_ARCHIVE",
            closure_status="OPEN",
        ),
        health=ProjectStatusHealthResponse(
            overall_health_indicator="HEALTHY",
            missing_requirements=(),
            ready_for_closure=True,
        ),
    )

    feature = ProjectStatusFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.project.project_id == project_id
    assert result.health.overall_health_indicator == "HEALTHY"


def test_feature_maps_service_validation_errors() -> None:
    feature = ProjectStatusFeature(
        service=_ServiceStub(error=ServiceValidationException("invalid request"))
    )

    with pytest.raises(ValidationException, match="invalid request"):
        feature.execute(_request())


def test_feature_validates_request() -> None:
    feature = ProjectStatusFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="project_id"):
        feature.execute(ProjectStatusRequest(project_id="bad"))  # type: ignore[arg-type]


def test_feature_wraps_unexpected_errors() -> None:
    feature = ProjectStatusFeature(service=_ServiceStub(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException, match="feature failed"):
        feature.execute(_request())
