"""Attach document reference feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.documents.attach_reference import AttachReferenceRequest as ServiceRequest
from mfm.application.documents.attach_reference import AttachReferenceResponse as ServiceResponse
from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import DocumentReferenceInput
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_response,
)
from mfm.application.features.documents.create_document_feature import (
    to_service_document_reference_input,
)


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


class AttachReferenceService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class AttachReferenceFeature:
    """Feature facade for attaching document references."""

    def __init__(self, *, service: AttachReferenceService) -> None:
        self._service = service

    def execute(self, request: AttachReferenceRequest) -> AttachReferenceResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_id=request.document_id,
                    reference=to_service_document_reference_input(request.reference),
                    attached_at=request.attached_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Attach reference feature failed") from exc

        return AttachReferenceResponse(
            document=to_feature_document_response(service_response.document)
        )
