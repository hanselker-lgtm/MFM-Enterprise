"""Archive Document use case."""

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
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.exceptions import DocumentError


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


class ArchiveDocumentUseCase:
    """Transition document lifecycle state to ARCHIVED."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ArchiveDocumentRequest) -> ArchiveDocumentResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document = repository.get(DocumentId(request.document_id))
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                document.change_status(DocumentStatus.ARCHIVED, when=request.archived_at)
                repository.update(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Archive document failed") from exc

        return ArchiveDocumentResponse(document=to_document_response(document))
