"""In-memory backed repository adapter for Organization & Roles foundation."""

from __future__ import annotations

from copy import deepcopy
from uuid import UUID

from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)
from mfm.repositories.organization_roles_repository import OrganizationRolesRepository


class SQLiteOrganizationRolesRepository(OrganizationRolesRepository):
    """Repository adapter preserving organization roles aggregates in-process.

    This capability foundation is intentionally independent from legacy organization
    persistence models. Storage is scoped to process lifetime and can be replaced by
    a dedicated ORM model when CAP-002 progresses.
    """

    _store: dict[UUID, OrganizationRolesFoundation] = {}

    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None:
        foundation = self._store.get(organization_id)
        if foundation is None:
            return None
        return deepcopy(foundation)

    def save(self, foundation: OrganizationRolesFoundation) -> None:
        self._store[foundation.organization_id] = deepcopy(foundation)

    def list(self) -> list[OrganizationRolesFoundation]:
        return [deepcopy(item) for item in self._store.values()]

    @classmethod
    def clear(cls) -> None:
        cls._store.clear()
