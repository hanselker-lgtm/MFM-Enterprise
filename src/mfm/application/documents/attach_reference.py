"""Attach Document reference use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import BusinessRuleViolation
from mfm.application.documents.create_document import DocumentReferenceInput
from mfm.application.documents.create_document import DocumentResponse
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.documents.create_document import to_document_reference
from mfm.application.documents.create_document import to_document_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.exceptions import DocumentError


@dataclass(frozen=True, slots=True)
class AttachReferenceRequest:
    document_id: UUID
    reference: DocumentReferenceInput
    attached_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.reference, DocumentReferenceInput):
            raise ValidationException("reference must be DocumentReferenceInput")
        self.reference.validate(field_name="reference")
        if self.attached_at is not None and not isinstance(self.attached_at, datetime):
            raise ValidationException("attached_at must be datetime or None")


@dataclass(frozen=True, slots=True)
class AttachReferenceResponse:
    document: DocumentResponse


class AttachReferenceUseCase:
    """Attach cross-capability reference metadata to document."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: AttachReferenceRequest) -> AttachReferenceResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document = repository.get(DocumentId(request.document_id))
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                document.add_reference(
                    to_document_reference(request.reference),
                    when=request.attached_at,
                )
                repository.update(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Attach document reference failed") from exc

        return AttachReferenceResponse(document=to_document_response(document))
