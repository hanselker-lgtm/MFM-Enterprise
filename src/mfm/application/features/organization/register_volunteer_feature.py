"""Register volunteer feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.organization.create_organization import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException
from mfm.application.organization.register_volunteer import RegisterVolunteerRequest as ServiceRequest
from mfm.application.organization.register_volunteer import RegisterVolunteerResponse as ServiceResponse
from mfm.application.organization.register_volunteer import RegisterVolunteerUseCase
from mfm.application.organization.register_volunteer import VolunteerCertificateInput as ServiceVolunteerCertificateInput


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class VolunteerCertificateInput:
    name: str
    expires_at: date | None = None


@dataclass(frozen=True, slots=True)
class RegisterVolunteerRequest:
    contact_id: UUID
    member_id: UUID | None
    is_available: bool
    max_hours_per_week: int
    preferred_days: tuple[str, ...]
    skills: tuple[str, ...]
    certificates: tuple[VolunteerCertificateInput, ...]
    joined_at: date

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")
        if self.member_id is not None and not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID or None")
        if not isinstance(self.is_available, bool):
            raise ValidationException("is_available must be bool")
        if not isinstance(self.max_hours_per_week, int) or self.max_hours_per_week < 0:
            raise ValidationException("max_hours_per_week must be non-negative integer")
        if not isinstance(self.preferred_days, tuple):
            raise ValidationException("preferred_days must be tuple")
        if not isinstance(self.skills, tuple):
            raise ValidationException("skills must be tuple")
        if not isinstance(self.certificates, tuple):
            raise ValidationException("certificates must be tuple")
        if not isinstance(self.joined_at, date):
            raise ValidationException("joined_at must be date")


@dataclass(frozen=True, slots=True)
class RegisterVolunteerResponse:
    volunteer_id: UUID
    contact_id: UUID


class RegisterVolunteerService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RegisterVolunteerFeature:
    """Feature facade for volunteer registration with standardized API behavior."""

    def __init__(self, *, service: RegisterVolunteerService) -> None:
        self._service = service

    def execute(self, request: RegisterVolunteerRequest) -> RegisterVolunteerResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    contact_id=request.contact_id,
                    member_id=request.member_id,
                    is_available=request.is_available,
                    max_hours_per_week=request.max_hours_per_week,
                    preferred_days=request.preferred_days,
                    skills=request.skills,
                    certificates=tuple(
                        ServiceVolunteerCertificateInput(
                            name=certificate.name,
                            expires_at=certificate.expires_at,
                        )
                        for certificate in request.certificates
                    ),
                    joined_at=request.joined_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Register volunteer feature failed") from exc

        return RegisterVolunteerResponse(
            volunteer_id=service_response.volunteer_id,
            contact_id=service_response.contact_id,
        )
