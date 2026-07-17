from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.active_projects_feature import (
    ActiveProjectsDashboardRequest,
)
from mfm.application.features.reporting.active_projects_feature import ActiveProjectsFeature
from mfm.application.features.reporting.active_projects_feature import RepositoryException
from mfm.application.features.reporting.active_projects_feature import ValidationException
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectDashboardProjectDTO,
)
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectsDashboardResponse,
)
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectsDashboardTotalsDTO,
)
from mfm.application.reporting.active_projects_service import (
    ValidationException as ServiceValidationException,
)


@dataclass
class _ServiceStub:
    response: ActiveProjectsDashboardResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ActiveProjectsDashboardRequest:
    return ActiveProjectsDashboardRequest(organization_id=uuid4())


def test_feature_happy_path() -> None:
    project_id = uuid4()
    response = ActiveProjectsDashboardResponse(
        projects=(
            ActiveProjectDashboardProjectDTO(
                project_id=project_id,
                name="Project Alpha",
                status="ACTIVE",
                created_date=datetime(2040, 1, 1, 8, 0, tzinfo=UTC).date(),
                budget_status="READY",
                accounting_status="COMPLETE",
                documentation_status="COMPLETE",
                archive_status="READY_FOR_CLOSURE",
                last_activity=datetime(2040, 3, 1, 8, 0, tzinfo=UTC),
                health_indicator="HEALTHY",
            ),
        ),
        totals=ActiveProjectsDashboardTotalsDTO(
            active_project_count=1,
            projects_missing_budget=0,
            projects_missing_documentation=0,
            projects_missing_accounting=0,
            projects_ready_for_closure=1,
        ),
    )
    feature = ActiveProjectsFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.totals.active_project_count == 1
    assert result.projects[0].project_id == project_id


def test_feature_maps_service_validation_errors() -> None:
    feature = ActiveProjectsFeature(
        service=_ServiceStub(error=ServiceValidationException("invalid request"))
    )

    with pytest.raises(ValidationException, match="invalid request"):
        feature.execute(_request())


def test_feature_validates_request() -> None:
    feature = ActiveProjectsFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="organization_id"):
        feature.execute(ActiveProjectsDashboardRequest(organization_id="bad"))  # type: ignore[arg-type]


def test_feature_wraps_unexpected_errors() -> None:
    feature = ActiveProjectsFeature(service=_ServiceStub(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException, match="feature failed"):
        feature.execute(_request())
