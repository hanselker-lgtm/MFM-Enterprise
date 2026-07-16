"""Remove document reference feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.documents.remove_reference import RemoveReferenceRequest as ServiceRequest
from mfm.application.documents.remove_reference import RemoveReferenceResponse as ServiceResponse
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_response,
)


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


class RemoveReferenceService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RemoveReferenceFeature:
    """Feature facade for removing document references."""

    def __init__(self, *, service: RemoveReferenceService) -> None:
        self._service = service

    def execute(self, request: RemoveReferenceRequest) -> RemoveReferenceResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_id=request.document_id,
                    reference_id=request.reference_id,
                    removed_at=request.removed_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Remove reference feature failed") from exc

        return RemoveReferenceResponse(
            document=to_feature_document_response(service_response.document)
        )
