from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.organization_roles_summary_feature import (
    OrganizationRolesSummaryFeature,
)
from mfm.application.features.reporting.organization_roles_summary_feature import (
    OrganizationRolesSummaryRequest,
)
from mfm.application.features.reporting.organization_roles_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.organization_roles_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.models.organization_roles_summary_dto import (
    OrganizationRolesSummaryResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def execute(self, request):
        _ = request
        if self._error is not None:
            raise self._error
        return self._response


def test_summary_feature_returns_service_response() -> None:
    organization_id = uuid4()
    feature = OrganizationRolesSummaryFeature(
        service=StubService(
            response=OrganizationRolesSummaryResponse(
                organization_id=organization_id,
                total_roles=2,
                total_assignments=2,
                total_committees=1,
                has_board=True,
                total_election_periods=1,
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(
        OrganizationRolesSummaryRequest(organization_id=organization_id)
    )

    assert response.organization_id == organization_id
    assert response.total_roles == 2


def test_summary_feature_maps_unknown_error() -> None:
    feature = OrganizationRolesSummaryFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(OrganizationRolesSummaryRequest(organization_id=uuid4()))


def test_summary_feature_validates_request() -> None:
    feature = OrganizationRolesSummaryFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(OrganizationRolesSummaryRequest(organization_id="invalid"))
