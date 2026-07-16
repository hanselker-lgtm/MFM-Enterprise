"""Archive document feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.documents.archive_document import ArchiveDocumentRequest as ServiceRequest
from mfm.application.documents.archive_document import ArchiveDocumentResponse as ServiceResponse
from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_response,
)


@dataclass(frozen=True, slots=True)
class ArchiveDocumentRequest:
    document_id: UUID
    archived_at: datetime

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.archived_at, datetime):
            raise ValidationException("archived_at must be datetime")


@dataclass(frozen=True, slots=True)
class ArchiveDocumentResponse:
    document: DocumentResponse


class ArchiveDocumentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ArchiveDocumentFeature:
    """Feature facade for archiving documents."""

    def __init__(self, *, service: ArchiveDocumentService) -> None:
        self._service = service

    def execute(self, request: ArchiveDocumentRequest) -> ArchiveDocumentResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_id=request.document_id,
                    archived_at=request.archived_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Archive document feature failed") from exc

        return ArchiveDocumentResponse(
            document=to_feature_document_response(service_response.document)
        )
