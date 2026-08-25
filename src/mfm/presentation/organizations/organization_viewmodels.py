"""Pure view-model types for the Organizations workspace (no Qt imports)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class OrganizationListItemViewModel:
    organization_id: UUID
    organization_number: str
    name: str
    organization_type: str
    status: str


@dataclass(frozen=True, slots=True)
class OrganizationListViewModel:
    items: tuple[OrganizationListItemViewModel, ...]


@dataclass(frozen=True, slots=True)
class CreateOrganizationCommandViewModel:
    organization_number: str
    name: str
    organization_type: str


@dataclass(frozen=True, slots=True)
class UpdateOrganizationCommandViewModel:
    organization_id: UUID
    name: str | None = None
    organization_type: str | None = None
    status: str | None = None
