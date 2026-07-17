from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.organization_roles.organization_roles_service import (
    CreateOrganizationRolesFoundationRequest,
)
from mfm.application.organization_roles.organization_roles_service import (
    OrganizationRolesService,
)
from mfm.application.organization_roles.organization_roles_service import (
    ValidationException,
)
from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)


class InMemoryOrganizationRolesRepository:
    def __init__(self) -> None:
        self._store: dict[UUID, OrganizationRolesFoundation] = {}

    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None:
        return self._store.get(organization_id)

    def save(self, foundation: OrganizationRolesFoundation) -> None:
        self._store[foundation.organization_id] = foundation


def test_create_foundation_populates_required_capability_artifacts() -> None:
    organization_id = uuid4()
    repository = InMemoryOrganizationRolesRepository()
    service = OrganizationRolesService(repository=repository)

    response = service.create_foundation(
        CreateOrganizationRolesFoundationRequest(
            organization_id=organization_id,
            board_name="National Board",
            role_name="Board Chair",
            committee_name="Governance Committee",
            committee_mandate="Oversee policy and governance.",
            election_period_name="Election 2026",
            election_starts_on=date(2026, 1, 1),
            election_ends_on=date(2026, 12, 31),
        )
    )

    assert response.organization_id == organization_id
    assert response.role_count == 1
    assert response.assignment_count == 1
    assert response.committee_count == 1
    assert response.board_name == "National Board"
    assert response.election_period_count == 1


def test_create_foundation_validates_date_order() -> None:
    service = OrganizationRolesService(repository=InMemoryOrganizationRolesRepository())

    with pytest.raises(ValidationException, match="cannot be before"):
        service.create_foundation(
            CreateOrganizationRolesFoundationRequest(
                organization_id=uuid4(),
                board_name="National Board",
                role_name="Board Chair",
                committee_name="Governance Committee",
                committee_mandate="Oversee policy and governance.",
                election_period_name="Election 2026",
                election_starts_on=date(2026, 12, 31),
                election_ends_on=date(2026, 1, 1),
            )
        )
