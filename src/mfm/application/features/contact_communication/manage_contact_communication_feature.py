"""Feature API for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.contact_communication.contact_communication_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.contact_communication.contact_communication_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.contact_communication.contact_communication_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.contact_communication.contact_communication_service import (
    SetupContactCommunicationRequest as ServiceRequest,
)
from mfm.application.contact_communication.contact_communication_service import (
    SetupContactCommunicationResponse as ServiceResponse,
)
from mfm.application.contact_communication.contact_communication_service import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ManageContactCommunicationRequest:
    contact_id: UUID
    email_address: str
    phone_number: str
    postal_line1: str
    postal_code: str
    postal_city: str
    postal_country: str
    allow_marketing: bool = False

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")
        if not isinstance(self.email_address, str) or not self.email_address.strip():
            raise ValidationException("email_address must be non-empty string")
        if not isinstance(self.phone_number, str) or not self.phone_number.strip():
            raise ValidationException("phone_number must be non-empty string")
        if not isinstance(self.postal_line1, str) or not self.postal_line1.strip():
            raise ValidationException("postal_line1 must be non-empty string")
        if not isinstance(self.postal_code, str) or not self.postal_code.strip():
            raise ValidationException("postal_code must be non-empty string")
        if not isinstance(self.postal_city, str) or not self.postal_city.strip():
            raise ValidationException("postal_city must be non-empty string")
        if not isinstance(self.postal_country, str) or not self.postal_country.strip():
            raise ValidationException("postal_country must be non-empty string")
        if not isinstance(self.allow_marketing, bool):
            raise ValidationException("allow_marketing must be bool")


@dataclass(frozen=True, slots=True)
class ManageContactCommunicationResponse:
    contact_id: UUID
    method_count: int
    notification_count: int
    preferred_method_type: str
    allow_marketing: bool
    generated_at: datetime


class ContactCommunicationServicePort(Protocol):
    def setup(self, request: ServiceRequest) -> ServiceResponse: ...


class ManageContactCommunicationFeature:
    """Feature facade for contact communication setup."""

    def __init__(self, *, service: ContactCommunicationServicePort) -> None:
        self._service = service

    def execute(self, request: ManageContactCommunicationRequest) -> ManageContactCommunicationResponse:
        request.validate()

        try:
            response = self._service.setup(
                ServiceRequest(
                    contact_id=request.contact_id,
                    email_address=request.email_address,
                    phone_number=request.phone_number,
                    postal_line1=request.postal_line1,
                    postal_code=request.postal_code,
                    postal_city=request.postal_city,
                    postal_country=request.postal_country,
                    allow_marketing=request.allow_marketing,
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
            raise RepositoryException("Manage contact communication feature failed") from exc

        return ManageContactCommunicationResponse(
            contact_id=response.contact_id,
            method_count=response.method_count,
            notification_count=response.notification_count,
            preferred_method_type=response.preferred_method_type,
            allow_marketing=response.allow_marketing,
            generated_at=response.generated_at,
        )
