"""Remove Document reference use case."""

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
from mfm.domain.document.exceptions import DocumentError


@dataclass(frozen=True, slots=True)
class RemoveReferenceRequest:
    document_id: UUID
    reference_id: UUID
    removed_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.reference_id, UUID):
            raise ValidationException("reference_id must be UUID")
        if self.removed_at is not None and not isinstance(self.removed_at, datetime):
            raise ValidationException("removed_at must be datetime or None")


@dataclass(frozen=True, slots=True)
class RemoveReferenceResponse:
    document: DocumentResponse


class RemoveReferenceUseCase:
    """Remove one cross-capability reference from a document."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: RemoveReferenceRequest) -> RemoveReferenceResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document = repository.get(DocumentId(request.document_id))
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                remaining = [
                    reference
                    for reference in document.references
                    if reference.id != request.reference_id
                ]
                if len(remaining) == len(document.references):
                    raise BusinessRuleViolation(
                        f"Reference {request.reference_id} does not exist on document {request.document_id}"
                    )

                document.references = remaining
                document.update_metadata(updated_at=request.removed_at)
                repository.update(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Remove document reference failed") from exc

        return RemoveReferenceResponse(document=to_document_response(document))
