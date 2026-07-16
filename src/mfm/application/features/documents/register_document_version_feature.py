"""Register document version feature facade following Public API Standard."""

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
from mfm.application.documents.register_document_version import (
    RegisterDocumentVersionRequest as ServiceRequest,
)
from mfm.application.documents.register_document_version import (
    RegisterDocumentVersionResponse as ServiceResponse,
)
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import DocumentVersionInput
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.create_document_feature import (
    to_feature_document_response,
)
from mfm.application.features.documents.create_document_feature import (
    to_service_document_version_input,
)


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


class RegisterDocumentVersionService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RegisterDocumentVersionFeature:
    """Feature facade for registering document versions."""

    def __init__(self, *, service: RegisterDocumentVersionService) -> None:
        self._service = service

    def execute(
        self,
        request: RegisterDocumentVersionRequest,
    ) -> RegisterDocumentVersionResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_id=request.document_id,
                    version=to_service_document_version_input(request.version),
                    registered_at=request.registered_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Register document version feature failed") from exc

        return RegisterDocumentVersionResponse(
            document=to_feature_document_response(service_response.document)
        )
