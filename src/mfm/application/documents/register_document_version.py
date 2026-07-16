"""Register Document version use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import BusinessRuleViolation
from mfm.application.documents.create_document import DocumentResponse
from mfm.application.documents.create_document import DocumentVersionInput
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.documents.create_document import to_document_response
from mfm.application.documents.create_document import to_document_version
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.exceptions import DocumentError


@dataclass(frozen=True, slots=True)
class RegisterDocumentVersionRequest:
    document_id: UUID
    version: DocumentVersionInput
    registered_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.version, DocumentVersionInput):
            raise ValidationException("version must be DocumentVersionInput")
        self.version.validate(field_name="version")
        if self.registered_at is not None and not isinstance(self.registered_at, datetime):
            raise ValidationException("registered_at must be datetime or None")


@dataclass(frozen=True, slots=True)
class RegisterDocumentVersionResponse:
    document: DocumentResponse


class RegisterDocumentVersionUseCase:
    """Append a version to an existing document."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: RegisterDocumentVersionRequest,
    ) -> RegisterDocumentVersionResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                document = repository.get(DocumentId(request.document_id))
                if document is None:
                    raise BusinessRuleViolation(
                        f"Document {request.document_id} does not exist"
                    )

                document.add_version(
                    to_document_version(request.version),
                    when=request.registered_at,
                )
                repository.update(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Register document version failed") from exc

        return RegisterDocumentVersionResponse(document=to_document_response(document))
