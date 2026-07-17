from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesFeature,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesRequest,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    RepositoryException,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ValidationException,
)
from mfm.application.organization_roles.organization_roles_service import (
    CreateOrganizationRolesFoundationResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def create_foundation(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


def test_manage_organization_roles_feature_maps_response() -> None:
    organization_id = uuid4()
    service = StubService(
        response=CreateOrganizationRolesFoundationResponse(
            organization_id=organization_id,
            role_count=2,
            assignment_count=2,
            committee_count=1,
            board_name="National Board",
            election_period_count=1,
            generated_at=datetime(2026, 1, 1, tzinfo=UTC),
        )
    )
    feature = ManageOrganizationRolesFeature(service=service)

    response = feature.execute(
        ManageOrganizationRolesRequest(
            organization_id=organization_id,
            board_name="National Board",
            role_name="Board Chair",
            committee_name="Governance Committee",
            committee_mandate="Oversee policy and governance.",
            election_period_name="Election 2026",
            election_starts_on=datetime(2026, 1, 1, tzinfo=UTC).date(),
            election_ends_on=datetime(2026, 12, 31, tzinfo=UTC).date(),
        )
    )

    assert response.organization_id == organization_id
    assert response.role_count == 2
    assert response.board_name == "National Board"


def test_manage_organization_roles_feature_validates_input() -> None:
    feature = ManageOrganizationRolesFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(
            ManageOrganizationRolesRequest(
                organization_id=uuid4(),
                board_name="",
                role_name="Board Chair",
                committee_name="Governance Committee",
                committee_mandate="Oversee policy and governance.",
                election_period_name="Election 2026",
                election_starts_on=datetime(2026, 1, 1, tzinfo=UTC).date(),
                election_ends_on=datetime(2026, 12, 31, tzinfo=UTC).date(),
            )
        )


def test_manage_organization_roles_feature_maps_unknown_error_to_repository_exception() -> None:
    feature = ManageOrganizationRolesFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(
            ManageOrganizationRolesRequest(
                organization_id=uuid4(),
                board_name="National Board",
                role_name="Board Chair",
                committee_name="Governance Committee",
                committee_mandate="Oversee policy and governance.",
                election_period_name="Election 2026",
                election_starts_on=datetime(2026, 1, 1, tzinfo=UTC).date(),
                election_ends_on=datetime(2026, 12, 31, tzinfo=UTC).date(),
            )
        )
