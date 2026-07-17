"""Feature API for document archive summary reporting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.reporting.document_archive_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryService as ReportingDocumentArchiveSummaryService,
)
from mfm.application.reporting.document_archive_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.document_archive_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryResponse,
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
class DocumentArchiveSummaryRequest:
    include_archived: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_archived, bool):
            raise ValidationException("include_archived must be bool")


DocumentArchiveSummaryService = ReportingDocumentArchiveSummaryService


class DocumentArchiveSummaryFeature:
    """Feature facade for document archive summary reporting."""

    def __init__(self, *, service: ReportingDocumentArchiveSummaryService) -> None:
        self._service = service

    def execute(self, request: DocumentArchiveSummaryRequest) -> DocumentArchiveSummaryResponse:
        request.validate()

        try:
            return self._service.execute(ServiceRequest(include_archived=request.include_archived))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Document archive summary feature failed") from exc
