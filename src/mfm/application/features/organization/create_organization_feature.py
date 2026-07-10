"""Create organization feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.organization.create_organization import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_organization import CreateOrganizationRequest as ServiceRequest
from mfm.application.organization.create_organization import CreateOrganizationResponse as ServiceResponse
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException
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
class CreateOrganizationRequest:
    organization_number: str
    name: str
    organization_type: OrganizationType

    def validate(self) -> None:
        if not isinstance(self.organization_number, str) or not self.organization_number.strip():
            raise ValidationException("organization_number must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.organization_type, OrganizationType):
            raise ValidationException("organization_type must be OrganizationType")


@dataclass(frozen=True, slots=True)
class CreateOrganizationResponse:
    organization_id: UUID
    organization_number: str
    name: str


class CreateOrganizationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateOrganizationFeature:
    """Feature facade for organization creation with standardized API behavior."""

    def __init__(self, *, service: CreateOrganizationService) -> None:
        self._service = service

    def execute(self, request: CreateOrganizationRequest) -> CreateOrganizationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_number=request.organization_number,
                    name=request.name,
                    organization_type=request.organization_type,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create organization feature failed") from exc

        return CreateOrganizationResponse(
            organization_id=service_response.organization_id,
            organization_number=service_response.organization_number,
            name=service_response.name,
        )
