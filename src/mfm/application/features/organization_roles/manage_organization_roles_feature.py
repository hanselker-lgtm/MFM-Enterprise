"""Feature API for Organization & Roles foundation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.organization_roles.organization_roles_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.organization_roles.organization_roles_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.organization_roles.organization_roles_service import (
    CreateOrganizationRolesFoundationRequest as ServiceRequest,
)
from mfm.application.organization_roles.organization_roles_service import (
    CreateOrganizationRolesFoundationResponse as ServiceResponse,
)
from mfm.application.organization_roles.organization_roles_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.organization_roles.organization_roles_service import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ManageOrganizationRolesRequest:
    organization_id: UUID
    board_name: str
    role_name: str
    committee_name: str
    committee_mandate: str
    election_period_name: str
    election_starts_on: date
    election_ends_on: date

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.board_name, str) or not self.board_name.strip():
            raise ValidationException("board_name must be non-empty string")
        if not isinstance(self.role_name, str) or not self.role_name.strip():
            raise ValidationException("role_name must be non-empty string")
        if not isinstance(self.committee_name, str) or not self.committee_name.strip():
            raise ValidationException("committee_name must be non-empty string")
        if not isinstance(self.committee_mandate, str) or not self.committee_mandate.strip():
            raise ValidationException("committee_mandate must be non-empty string")
        if not isinstance(self.election_period_name, str) or not self.election_period_name.strip():
            raise ValidationException("election_period_name must be non-empty string")
        if not isinstance(self.election_starts_on, date):
            raise ValidationException("election_starts_on must be date")
        if not isinstance(self.election_ends_on, date):
            raise ValidationException("election_ends_on must be date")
        if self.election_ends_on < self.election_starts_on:
            raise ValidationException("election_ends_on cannot be before election_starts_on")


@dataclass(frozen=True, slots=True)
class ManageOrganizationRolesResponse:
    organization_id: UUID
    role_count: int
    assignment_count: int
    committee_count: int
    board_name: str
    election_period_count: int
    generated_at: datetime


class OrganizationRolesServicePort(Protocol):
    def create_foundation(self, request: ServiceRequest) -> ServiceResponse: ...


class ManageOrganizationRolesFeature:
    """Feature facade for independent organization roles capability."""

    def __init__(self, *, service: OrganizationRolesServicePort) -> None:
        self._service = service

    def execute(
        self,
        request: ManageOrganizationRolesRequest,
    ) -> ManageOrganizationRolesResponse:
        request.validate()

        try:
            response = self._service.create_foundation(
                ServiceRequest(
                    organization_id=request.organization_id,
                    board_name=request.board_name,
                    role_name=request.role_name,
                    committee_name=request.committee_name,
                    committee_mandate=request.committee_mandate,
                    election_period_name=request.election_period_name,
                    election_starts_on=request.election_starts_on,
                    election_ends_on=request.election_ends_on,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Manage organization roles feature failed") from exc

        return ManageOrganizationRolesResponse(
            organization_id=response.organization_id,
            role_count=response.role_count,
            assignment_count=response.assignment_count,
            committee_count=response.committee_count,
            board_name=response.board_name,
            election_period_count=response.election_period_count,
            generated_at=response.generated_at,
        )
