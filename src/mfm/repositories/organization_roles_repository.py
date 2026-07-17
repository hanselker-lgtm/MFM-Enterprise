"""Repository contract for Organization & Roles foundation."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)


class OrganizationRolesRepository(ABC):
    """Persistence contract for organization roles aggregate root."""

    @abstractmethod
    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, foundation: OrganizationRolesFoundation) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[OrganizationRolesFoundation]:
        raise NotImplementedError
