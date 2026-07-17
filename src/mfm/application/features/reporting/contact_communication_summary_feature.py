"""Feature API for contact communication summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.reporting.contact_communication_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.contact_communication_summary_service import (
    ContactCommunicationSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.contact_communication_summary_service import (
    ContactCommunicationSummaryService as ReportingContactCommunicationSummaryService,
)
from mfm.application.reporting.contact_communication_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.contact_communication_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.contact_communication_summary_dto import (
    ContactCommunicationSummaryResponse,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when report business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ContactCommunicationSummaryRequest:
    contact_id: UUID

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")


ContactCommunicationSummaryService = ReportingContactCommunicationSummaryService


class ContactCommunicationSummaryServicePort(Protocol):
    def execute(self, request: ServiceRequest) -> ContactCommunicationSummaryResponse: ...


class ContactCommunicationSummaryFeature:
    """Feature facade for contact communication summary reporting."""

    def __init__(self, *, service: ContactCommunicationSummaryServicePort) -> None:
        self._service = service

    def execute(self, request: ContactCommunicationSummaryRequest) -> ContactCommunicationSummaryResponse:
        request.validate()

        try:
            return self._service.execute(ServiceRequest(contact_id=request.contact_id))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Contact communication summary feature failed") from exc
