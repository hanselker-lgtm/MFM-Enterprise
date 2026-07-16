"""Delete document feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.documents.delete_document import DeleteDocumentRequest as ServiceRequest
from mfm.application.documents.delete_document import DeleteDocumentResponse as ServiceResponse
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException


@dataclass(frozen=True, slots=True)
class DeleteDocumentRequest:
    document_id: UUID

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")


@dataclass(frozen=True, slots=True)
class DeleteDocumentResponse:
    document_id: UUID


class DeleteDocumentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class DeleteDocumentFeature:
    """Feature facade for document deletion."""

    def __init__(self, *, service: DeleteDocumentService) -> None:
        self._service = service

    def execute(self, request: DeleteDocumentRequest) -> DeleteDocumentResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(document_id=request.document_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Delete document feature failed") from exc

        return DeleteDocumentResponse(document_id=service_response.document_id)
