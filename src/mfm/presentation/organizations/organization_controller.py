"""Controller for the Organizations workspace."""

from __future__ import annotations

from typing import Protocol

from mfm.application.features.organizations import (
    CreateOrganizationRequest,
    ListOrganizationsRequest,
    UpdateOrganizationRequest,
)
from mfm.presentation.organizations.organization_viewmodels import (
    CreateOrganizationCommandViewModel,
    OrganizationListItemViewModel,
    OrganizationListViewModel,
    UpdateOrganizationCommandViewModel,
)


class CreateOrganizationPort(Protocol):
    def execute(self, request: CreateOrganizationRequest): ...


class UpdateOrganizationPort(Protocol):
    def execute(self, request: UpdateOrganizationRequest): ...


class ListOrganizationsPort(Protocol):
    def execute(self, request: ListOrganizationsRequest): ...


class OrganizationController:
    """UI controller that orchestrates organization features."""

    def __init__(
        self,
        *,
        create_organization_feature: CreateOrganizationPort,
        update_organization_feature: UpdateOrganizationPort,
        list_organizations_feature: ListOrganizationsPort,
    ) -> None:
        self._create_organization = create_organization_feature
        self._update_organization = update_organization_feature
        self._list_organizations = list_organizations_feature

    def load_organization_list(self) -> OrganizationListViewModel:
        response = self._list_organizations.execute(ListOrganizationsRequest())
        items = tuple(
            OrganizationListItemViewModel(
                organization_id=org.organization_id,
                organization_number=org.organization_number,
                name=org.name,
                organization_type=org.organization_type,
                status=org.status,
            )
            for org in response.organizations
        )
        return OrganizationListViewModel(items=items)

    def create_organization(self, command: CreateOrganizationCommandViewModel):
        response = self._create_organization.execute(
            CreateOrganizationRequest(
                organization_number=command.organization_number,
                name=command.name,
                organization_type=command.organization_type,
            )
        )
        return response.organization_id

    def update_organization(self, command: UpdateOrganizationCommandViewModel) -> None:
        self._update_organization.execute(
            UpdateOrganizationRequest(
                organization_id=command.organization_id,
                name=command.name,
                organization_type=command.organization_type,
                status=command.status,
            )
        )
