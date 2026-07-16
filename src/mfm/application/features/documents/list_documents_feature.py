"""List documents feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.list_documents import ListDocumentsRequest as ServiceRequest
from mfm.application.documents.list_documents import ListDocumentsResponse as ServiceResponse
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_response,
)


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


class ListDocumentsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListDocumentsFeature:
    """Feature facade for document listing."""

    def __init__(self, *, service: ListDocumentsService) -> None:
        self._service = service

    def execute(self, request: ListDocumentsRequest) -> ListDocumentsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(status=request.status)
            )
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List documents feature failed") from exc

        return ListDocumentsResponse(
            documents=tuple(
                to_feature_document_response(item)
                for item in service_response.documents
            )
        )
