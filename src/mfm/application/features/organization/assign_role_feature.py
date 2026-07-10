"""Assign role feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.organization.assign_role import AssignRoleRequest as ServiceRequest
from mfm.application.organization.assign_role import AssignRoleResponse as ServiceResponse
from mfm.application.organization.assign_role import AssignRoleUseCase
from mfm.application.organization.create_organization import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class AssignRoleRequest:
    role_id: UUID
    assignee_id: UUID
    organization_id: UUID
    valid_from: date
    valid_to: date | None = None

    def validate(self) -> None:
        if not isinstance(self.role_id, UUID):
            raise ValidationException("role_id must be UUID")
        if not isinstance(self.assignee_id, UUID):
            raise ValidationException("assignee_id must be UUID")
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.valid_from, date):
            raise ValidationException("valid_from must be date")
        if self.valid_to is not None and not isinstance(self.valid_to, date):
            raise ValidationException("valid_to must be date or None")
        if self.valid_to is not None and self.valid_to < self.valid_from:
            raise ValidationException("valid_to cannot be before valid_from")


@dataclass(frozen=True, slots=True)
class AssignRoleResponse:
    role_id: UUID
    assignee_id: UUID
    organization_id: UUID


class AssignRoleService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class AssignRoleFeature:
    """Feature facade for role assignment with standardized API behavior."""

    def __init__(self, *, service: AssignRoleService) -> None:
        self._service = service

    def execute(self, request: AssignRoleRequest) -> AssignRoleResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    role_id=request.role_id,
                    assignee_id=request.assignee_id,
                    organization_id=request.organization_id,
                    valid_from=request.valid_from,
                    valid_to=request.valid_to,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Assign role feature failed") from exc

        return AssignRoleResponse(
            role_id=service_response.role_id,
            assignee_id=service_response.assignee_id,
            organization_id=service_response.organization_id,
        )
