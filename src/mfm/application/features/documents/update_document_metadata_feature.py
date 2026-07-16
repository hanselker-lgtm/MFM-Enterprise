"""Update document metadata feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
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
from mfm.application.documents.update_document_metadata import (
    UpdateDocumentMetadataRequest as ServiceRequest,
)
from mfm.application.documents.update_document_metadata import (
    UpdateDocumentMetadataResponse as ServiceResponse,
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
class UpdateDocumentMetadataRequest:
    document_id: UUID
    document_title: str | None = None
    document_type: str | None = None
    description: str | None = None
    updated_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if self.document_title is not None and (
            not isinstance(self.document_title, str) or not self.document_title.strip()
        ):
            raise ValidationException("document_title must be a non-empty string or None")
        if self.document_type is not None and (
            not isinstance(self.document_type, str) or not self.document_type.strip()
        ):
            raise ValidationException("document_type must be a non-empty string or None")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.updated_at is not None and not isinstance(self.updated_at, datetime):
            raise ValidationException("updated_at must be datetime or None")


@dataclass(frozen=True, slots=True)
class UpdateDocumentMetadataResponse:
    document: DocumentResponse


class UpdateDocumentMetadataService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateDocumentMetadataFeature:
    """Feature facade for document metadata updates."""

    def __init__(self, *, service: UpdateDocumentMetadataService) -> None:
        self._service = service

    def execute(
        self,
        request: UpdateDocumentMetadataRequest,
    ) -> UpdateDocumentMetadataResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_id=request.document_id,
                    document_title=request.document_title,
                    document_type=request.document_type,
                    description=request.description,
                    updated_at=request.updated_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update document metadata feature failed") from exc

        return UpdateDocumentMetadataResponse(
            document=to_feature_document_response(service_response.document)
        )
