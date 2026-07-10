"""Create committee feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.organization.create_committee import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_committee import CommitteeMemberInput as ServiceCommitteeMemberInput
from mfm.application.organization.create_committee import CreateCommitteeRequest as ServiceRequest
from mfm.application.organization.create_committee import CreateCommitteeResponse as ServiceResponse
from mfm.application.organization.create_committee import CreateCommitteeUseCase
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
class CommitteeMemberInput:
    reference_id: UUID
    function_title: str
    joined_at: date
    left_at: date | None = None


@dataclass(frozen=True, slots=True)
class CreateCommitteeRequest:
    organization_id: UUID
    name: str
    purpose: str
    members: tuple[CommitteeMemberInput, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.purpose, str):
            raise ValidationException("purpose must be a string")
        if not isinstance(self.members, tuple):
            raise ValidationException("members must be a tuple")


@dataclass(frozen=True, slots=True)
class CreateCommitteeResponse:
    committee_id: UUID
    organization_id: UUID
    name: str


class CreateCommitteeService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateCommitteeFeature:
    """Feature facade for committee creation with standardized API behavior."""

    def __init__(self, *, service: CreateCommitteeService) -> None:
        self._service = service

    def execute(self, request: CreateCommitteeRequest) -> CreateCommitteeResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    name=request.name,
                    purpose=request.purpose,
                    members=tuple(
                        ServiceCommitteeMemberInput(
                            reference_id=member.reference_id,
                            function_title=member.function_title,
                            joined_at=member.joined_at,
                            left_at=member.left_at,
                        )
                        for member in request.members
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create committee feature failed") from exc

        return CreateCommitteeResponse(
            committee_id=service_response.committee_id,
            organization_id=service_response.organization_id,
            name=service_response.name,
        )
