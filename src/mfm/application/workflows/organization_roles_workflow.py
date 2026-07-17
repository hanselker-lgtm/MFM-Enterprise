"""Workflow for Organization & Roles capability."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesFeature,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesRequest,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesResponse,
)


@dataclass(frozen=True, slots=True)
class OrganizationRolesWorkflowInput:
    request: ManageOrganizationRolesRequest


@dataclass(frozen=True, slots=True)
class OrganizationRolesWorkflowResult:
    success: bool
    response: ManageOrganizationRolesResponse | None = None
    message: str = ""


class OrganizationRolesWorkflow:
    """Workflow wrapper around Organization & Roles feature API."""

    def __init__(self, *, feature: ManageOrganizationRolesFeature) -> None:
        self._feature = feature

    def execute(self, data: OrganizationRolesWorkflowInput) -> OrganizationRolesWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return OrganizationRolesWorkflowResult(
                success=True,
                response=response,
                message="Organization roles foundation completed",
            )
        except Exception as exc:
            return OrganizationRolesWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
