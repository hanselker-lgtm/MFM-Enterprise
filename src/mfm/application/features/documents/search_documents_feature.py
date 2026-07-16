"""Search documents feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.documents.search_documents import SearchDocumentsRequest as ServiceRequest
from mfm.application.documents.search_documents import SearchDocumentsResponse as ServiceResponse
from mfm.application.features.documents.create_document_feature import (
    DocumentSearchResultResponse,
)
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_search_result_response,
)


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
                raise ValidationException(
                    f"{field_name} must be non-empty when provided"
                )


@dataclass(frozen=True, slots=True)
class SearchDocumentsResponse:
    documents: tuple[DocumentSearchResultResponse, ...]


class SearchDocumentsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class SearchDocumentsFeature:
    """Feature facade for document search."""

    def __init__(self, *, service: SearchDocumentsService) -> None:
        self._service = service

    def execute(self, request: SearchDocumentsRequest) -> SearchDocumentsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    text=request.text,
                    status=request.status,
                    target_capability=request.target_capability,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Search documents feature failed") from exc

        return SearchDocumentsResponse(
            documents=tuple(
                to_feature_document_search_result_response(item)
                for item in service_response.documents
            )
        )
