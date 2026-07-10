"""Update organization feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.organization.create_organization import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException
from mfm.application.organization.update_organization import UpdateOrganizationRequest as ServiceRequest
from mfm.application.organization.update_organization import UpdateOrganizationResponse as ServiceResponse
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class UpdateOrganizationRequest:
    organization_id: UUID
    organization_number: str | None = None
    name: str | None = None
    organization_type: OrganizationType | None = None
    status: OrganizationStatus | None = None

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if self.organization_number is not None and not self.organization_number.strip():
            raise ValidationException("organization_number cannot be empty")
        if self.name is not None and not self.name.strip():
            raise ValidationException("name cannot be empty")
        if self.organization_type is not None and not isinstance(self.organization_type, OrganizationType):
            raise ValidationException("organization_type must be OrganizationType")
        if self.status is not None and not isinstance(self.status, OrganizationStatus):
            raise ValidationException("status must be OrganizationStatus")


@dataclass(frozen=True, slots=True)
class UpdateOrganizationResponse:
    organization_id: UUID
    organization_number: str
    name: str
    status: str


class UpdateOrganizationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateOrganizationFeature:
    """Feature facade for organization updates with standardized API behavior."""

    def __init__(self, *, service: UpdateOrganizationService) -> None:
        self._service = service

    def execute(self, request: UpdateOrganizationRequest) -> UpdateOrganizationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    organization_number=request.organization_number,
                    name=request.name,
                    organization_type=request.organization_type,
                    status=request.status,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update organization feature failed") from exc

        return UpdateOrganizationResponse(
            organization_id=service_response.organization_id,
            organization_number=service_response.organization_number,
            name=service_response.name,
            status=service_response.status.value,
        )
