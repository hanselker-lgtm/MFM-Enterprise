"""Reporting service for Organization & Roles foundation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.reporting.models.organization_roles_summary_dto import (
    OrganizationRolesSummaryResponse,
)
from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class OrganizationRolesSummaryRequest:
    organization_id: UUID

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")


class OrganizationRolesRepositoryPort(Protocol):
    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None: ...


class OrganizationRolesSummaryService:
    """Build summary metrics for the organization roles foundation."""

    def __init__(self, *, repository: OrganizationRolesRepositoryPort) -> None:
        self._repository = repository

    def execute(self, request: OrganizationRolesSummaryRequest) -> OrganizationRolesSummaryResponse:
        request.validate()

        try:
            foundation = self._repository.get(request.organization_id)
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Organization roles summary retrieval failed") from exc

        if foundation is None:
            raise ValidationException(
                f"Organization roles foundation not found for {request.organization_id}"
            )

        return OrganizationRolesSummaryResponse(
            organization_id=foundation.organization_id,
            total_roles=len(foundation.roles),
            total_assignments=len(foundation.assignments),
            total_committees=len(foundation.committees),
            has_board=foundation.board is not None,
            total_election_periods=len(foundation.election_periods),
            generated_at=datetime.now(UTC),
        )
