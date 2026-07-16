"""Search Documents use case."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mfm.application.documents.create_document import ApplicationException
from mfm.application.documents.create_document import DocumentSearchResultResponse
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.create_document import ValidationException
from mfm.application.documents.create_document import to_document_search_result_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document_repository import DocumentRepository


@dataclass(frozen=True, slots=True)
class SearchDocumentsRequest:
    text: str | None = None
    status: str | None = None
    target_capability: str | None = None

    def validate(self) -> None:
        for field_name, value in (
            ("text", self.text),
            ("status", self.status),
            ("target_capability", self.target_capability),
        ):
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValidationException(f"{field_name} must be string or None")
            if not value.strip():
                raise ValidationException(f"{field_name} must be non-empty when provided")


@dataclass(frozen=True, slots=True)
class SearchDocumentsResponse:
    documents: tuple[DocumentSearchResultResponse, ...]


class SearchDocumentsUseCase:
    """Search documents through repository projection queries."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: SearchDocumentsRequest) -> SearchDocumentsResponse:
        request.validate()

        criteria: dict[str, Any] = {}
        if request.text is not None:
            criteria["text"] = request.text.strip()
        if request.status is not None:
            criteria["status"] = request.status.strip()
        if request.target_capability is not None:
            criteria["target_capability"] = request.target_capability.strip()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository
                rows = repository.search(criteria)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Search documents failed") from exc

        return SearchDocumentsResponse(
            documents=tuple(to_document_search_result_response(row) for row in rows)
        )
