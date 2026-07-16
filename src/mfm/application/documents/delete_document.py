"""Delete Document use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import BusinessRuleViolation
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_repository import DocumentRepository


@dataclass(frozen=True, slots=True)
class DeleteDocumentRequest:
    document_id: UUID

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")


@dataclass(frozen=True, slots=True)
class DeleteDocumentResponse:
    document_id: UUID


class DeleteDocumentUseCase:
    """Delete one document aggregate by identifier."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: DeleteDocumentRequest) -> DeleteDocumentResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document_id = DocumentId(request.document_id)
                document = repository.get(document_id)
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                repository.remove(document_id)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Delete document failed") from exc

        return DeleteDocumentResponse(document_id=request.document_id)
