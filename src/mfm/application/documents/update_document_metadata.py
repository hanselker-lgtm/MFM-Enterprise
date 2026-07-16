"""Update Document metadata use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import BusinessRuleViolation
from mfm.application.documents.create_document import DocumentResponse
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.documents.create_document import to_document_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.exceptions import DocumentError


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


class UpdateDocumentMetadataUseCase:
    """Update mutable document metadata."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: UpdateDocumentMetadataRequest,
    ) -> UpdateDocumentMetadataResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document = repository.get(DocumentId(request.document_id))
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                document.update_metadata(
                    document_title=(
                        DocumentTitle(request.document_title)
                        if request.document_title is not None
                        else None
                    ),
                    document_type=(
                        DocumentType(request.document_type)
                        if request.document_type is not None
                        else None
                    ),
                    description=request.description,
                    updated_at=request.updated_at,
                )

                repository.update(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update document metadata failed") from exc

        return UpdateDocumentMetadataResponse(document=to_document_response(document))
