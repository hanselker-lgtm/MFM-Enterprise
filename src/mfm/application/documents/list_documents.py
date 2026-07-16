"""List Documents use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import DocumentResponse
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.documents.create_document import to_document_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_repository import DocumentRepository


@dataclass(frozen=True, slots=True)
class ListDocumentsRequest:
    status: str | None = None

    def validate(self) -> None:
        if self.status is not None:
            if not isinstance(self.status, str) or not self.status.strip():
                raise ValidationException("status must be a non-empty string or None")


@dataclass(frozen=True, slots=True)
class ListDocumentsResponse:
    documents: tuple[DocumentResponse, ...]


class ListDocumentsUseCase:
    """List documents with repository-provided deterministic ordering."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListDocumentsRequest) -> ListDocumentsResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                if request.status is None:
                    documents = repository.list()
                else:
                    documents = repository.list(filters={"status": request.status.strip()})
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("List documents failed") from exc

        return ListDocumentsResponse(
            documents=tuple(to_document_response(item) for item in documents)
        )
