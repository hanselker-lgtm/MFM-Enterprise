from __future__ import annotations

from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.reporting.organization_roles_summary_service import (
    OrganizationRolesSummaryRequest,
)
from mfm.application.reporting.organization_roles_summary_service import (
    OrganizationRolesSummaryService,
)
from mfm.application.reporting.organization_roles_summary_service import (
    ValidationException,
)
from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)
from mfm.domain.organization_roles.role import Role


class InMemoryOrganizationRolesRepository:
    def __init__(self, store: dict[UUID, OrganizationRolesFoundation]) -> None:
        self._store = store

    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None:
        return self._store.get(organization_id)


def test_summary_service_returns_expected_metrics() -> None:
    organization_id = uuid4()
    foundation = OrganizationRolesFoundation(organization_id=organization_id)
    foundation.add_role(Role(name="Board Chair"))

    service = OrganizationRolesSummaryService(
        repository=InMemoryOrganizationRolesRepository({organization_id: foundation})
    )

    response = service.execute(
        OrganizationRolesSummaryRequest(organization_id=organization_id)
    )

    assert response.organization_id == organization_id
    assert response.total_roles == 1
    assert response.total_assignments == 0
    assert response.total_committees == 0
    assert response.has_board is False
    assert response.total_election_periods == 0


def test_summary_service_raises_when_foundation_missing() -> None:
    service = OrganizationRolesSummaryService(
        repository=InMemoryOrganizationRolesRepository({})
    )

    with pytest.raises(ValidationException, match="not found"):
        service.execute(OrganizationRolesSummaryRequest(organization_id=uuid4()))
