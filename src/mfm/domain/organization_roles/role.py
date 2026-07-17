"""Role entity for organization roles capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4

from mfm.domain.organization_roles.permission import Permission
from mfm.domain.organization_roles.responsibility import Responsibility


@dataclass(slots=True)
class Role:
    """Role definition with permissions and responsibilities."""

    name: str
    permissions: tuple[Permission, ...] = ()
    responsibilities: tuple[Responsibility, ...] = ()
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")

        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        self.name = self.name.strip()

        normalized_permissions: list[Permission] = []
        for value in self.permissions:
            if not isinstance(value, Permission):
                value = Permission(str(value).upper())
            normalized_permissions.append(value)
        self.permissions = tuple(dict.fromkeys(normalized_permissions))

        normalized_responsibilities: list[Responsibility] = []
        for value in self.responsibilities:
            if not isinstance(value, Responsibility):
                raise ValueError("responsibilities must be Responsibility values")
            normalized_responsibilities.append(value)
        self.responsibilities = tuple(normalized_responsibilities)

    def grant_permission(self, permission: Permission) -> None:
        if not isinstance(permission, Permission):
            permission = Permission(str(permission).upper())
        if permission in self.permissions:
            return
        self.permissions = (*self.permissions, permission)

    def add_responsibility(self, responsibility: Responsibility) -> None:
        if not isinstance(responsibility, Responsibility):
            raise ValueError("responsibility must be Responsibility")

        if any(item.title.casefold() == responsibility.title.casefold() for item in self.responsibilities):
            return
        self.responsibilities = (*self.responsibilities, responsibility)
