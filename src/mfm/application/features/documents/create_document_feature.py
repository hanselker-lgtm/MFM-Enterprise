"""Create document feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    CreateDocumentRequest as ServiceRequest,
)
from mfm.application.documents.create_document import (
    CreateDocumentResponse as ServiceResponse,
)
from mfm.application.documents.create_document import (
    DocumentReferenceInput as ServiceDocumentReferenceInput,
)
from mfm.application.documents.create_document import (
    DocumentReferenceResponse as ServiceDocumentReferenceResponse,
)
from mfm.application.documents.create_document import (
    DocumentResponse as ServiceDocumentResponse,
)
from mfm.application.documents.create_document import (
    DocumentSearchResultResponse as ServiceDocumentSearchResultResponse,
)
from mfm.application.documents.create_document import (
    DocumentVersionInput as ServiceDocumentVersionInput,
)
from mfm.application.documents.create_document import (
    DocumentVersionResponse as ServiceDocumentVersionResponse,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for document feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class DocumentVersionInput:
    version_number: int
    storage_key: str
    file_name: str | None = None
    mime_type: str | None = None
    checksum: str | None = None
    size_bytes: int | None = None
    created_at: datetime | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.version_number, int) or isinstance(self.version_number, bool):
            raise ValidationException(f"{field_name}.version_number must be integer")
        if not isinstance(self.storage_key, str) or not self.storage_key.strip():
            raise ValidationException(f"{field_name}.storage_key must be a non-empty string")
        if self.file_name is not None and not isinstance(self.file_name, str):
            raise ValidationException(f"{field_name}.file_name must be string or None")
        if self.mime_type is not None and not isinstance(self.mime_type, str):
            raise ValidationException(f"{field_name}.mime_type must be string or None")
        if self.checksum is not None and not isinstance(self.checksum, str):
            raise ValidationException(f"{field_name}.checksum must be string or None")
        if self.size_bytes is not None and (
            not isinstance(self.size_bytes, int) or isinstance(self.size_bytes, bool)
        ):
            raise ValidationException(f"{field_name}.size_bytes must be integer or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValidationException(f"{field_name}.created_at must be datetime or None")


@dataclass(frozen=True, slots=True)
class DocumentReferenceInput:
    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    exists: bool
    authorized: bool
    is_soft_deleted: bool
    is_archived: bool
    checked_at: datetime
    description: str | None = None
    reference_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.target_capability, str) or not self.target_capability.strip():
            raise ValidationException(f"{field_name}.target_capability must be a non-empty string")
        if not isinstance(self.target_aggregate_type, str) or not self.target_aggregate_type.strip():
            raise ValidationException(
                f"{field_name}.target_aggregate_type must be a non-empty string"
            )
        if not isinstance(self.target_aggregate_id, str) or not self.target_aggregate_id.strip():
            raise ValidationException(f"{field_name}.target_aggregate_id must be a non-empty string")
        for name, value in (
            ("exists", self.exists),
            ("authorized", self.authorized),
            ("is_soft_deleted", self.is_soft_deleted),
            ("is_archived", self.is_archived),
        ):
            if not isinstance(value, bool):
                raise ValidationException(f"{field_name}.{name} must be bool")
        if not isinstance(self.checked_at, datetime):
            raise ValidationException(f"{field_name}.checked_at must be datetime")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")
        if self.reference_id is not None and not isinstance(self.reference_id, UUID):
            raise ValidationException(f"{field_name}.reference_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class DocumentVersionResponse:
    version_number: int
    storage_key: str
    file_name: str | None
    mime_type: str | None
    checksum: str | None
    size_bytes: int | None
    created_at: datetime


@dataclass(frozen=True, slots=True)
class DocumentReferenceResponse:
    reference_id: UUID
    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    exists: bool
    authorized: bool
    is_soft_deleted: bool
    is_archived: bool
    checked_at: datetime
    description: str | None


@dataclass(frozen=True, slots=True)
class DocumentResponse:
    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str
    description: str | None
    created_at: datetime
    updated_at: datetime | None
    archived_at: datetime | None
    disposed_at: datetime | None
    version: int
    versions: tuple[DocumentVersionResponse, ...]
    references: tuple[DocumentReferenceResponse, ...]


@dataclass(frozen=True, slots=True)
class DocumentSearchResultResponse:
    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str


@dataclass(frozen=True, slots=True)
class CreateDocumentRequest:
    document_number: str
    document_title: str
    document_type: str
    document_id: UUID | None = None
    status: str = "DRAFT"
    description: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    archived_at: datetime | None = None
    disposed_at: datetime | None = None
    versions: tuple[DocumentVersionInput, ...] = ()
    references: tuple[DocumentReferenceInput, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.document_number, str) or not self.document_number.strip():
            raise ValidationException("document_number must be a non-empty string")
        if not isinstance(self.document_title, str) or not self.document_title.strip():
            raise ValidationException("document_title must be a non-empty string")
        if not isinstance(self.document_type, str) or not self.document_type.strip():
            raise ValidationException("document_type must be a non-empty string")
        if self.document_id is not None and not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID or None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValidationException("created_at must be datetime or None")
        if self.updated_at is not None and not isinstance(self.updated_at, datetime):
            raise ValidationException("updated_at must be datetime or None")
        if self.archived_at is not None and not isinstance(self.archived_at, datetime):
            raise ValidationException("archived_at must be datetime or None")
        if self.disposed_at is not None and not isinstance(self.disposed_at, datetime):
            raise ValidationException("disposed_at must be datetime or None")
        if not isinstance(self.versions, tuple):
            raise ValidationException("versions must be tuple")
        if not isinstance(self.references, tuple):
            raise ValidationException("references must be tuple")

        for index, version in enumerate(self.versions):
            version.validate(field_name=f"versions[{index}]")
        for index, reference in enumerate(self.references):
            reference.validate(field_name=f"references[{index}]")


@dataclass(frozen=True, slots=True)
class CreateDocumentResponse:
    document: DocumentResponse


class CreateDocumentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_document_version_input(value: DocumentVersionInput) -> ServiceDocumentVersionInput:
    return ServiceDocumentVersionInput(
        version_number=value.version_number,
        storage_key=value.storage_key,
        file_name=value.file_name,
        mime_type=value.mime_type,
        checksum=value.checksum,
        size_bytes=value.size_bytes,
        created_at=value.created_at,
    )


def to_service_document_reference_input(value: DocumentReferenceInput) -> ServiceDocumentReferenceInput:
    return ServiceDocumentReferenceInput(
        target_capability=value.target_capability,
        target_aggregate_type=value.target_aggregate_type,
        target_aggregate_id=value.target_aggregate_id,
        exists=value.exists,
        authorized=value.authorized,
        is_soft_deleted=value.is_soft_deleted,
        is_archived=value.is_archived,
        checked_at=value.checked_at,
        description=value.description,
        reference_id=value.reference_id,
    )


def to_feature_document_version_response(
    response: ServiceDocumentVersionResponse,
) -> DocumentVersionResponse:
    return DocumentVersionResponse(
        version_number=response.version_number,
        storage_key=response.storage_key,
        file_name=response.file_name,
        mime_type=response.mime_type,
        checksum=response.checksum,
        size_bytes=response.size_bytes,
        created_at=response.created_at,
    )


def to_feature_document_reference_response(
    response: ServiceDocumentReferenceResponse,
) -> DocumentReferenceResponse:
    return DocumentReferenceResponse(
        reference_id=response.reference_id,
        target_capability=response.target_capability,
        target_aggregate_type=response.target_aggregate_type,
        target_aggregate_id=response.target_aggregate_id,
        exists=response.exists,
        authorized=response.authorized,
        is_soft_deleted=response.is_soft_deleted,
        is_archived=response.is_archived,
        checked_at=response.checked_at,
        description=response.description,
    )


def to_feature_document_response(response: ServiceDocumentResponse) -> DocumentResponse:
    return DocumentResponse(
        document_id=response.document_id,
        document_number=response.document_number,
        document_title=response.document_title,
        document_type=response.document_type,
        status=response.status,
        description=response.description,
        created_at=response.created_at,
        updated_at=response.updated_at,
        archived_at=response.archived_at,
        disposed_at=response.disposed_at,
        version=response.version,
        versions=tuple(
            to_feature_document_version_response(item)
            for item in response.versions
        ),
        references=tuple(
            to_feature_document_reference_response(item)
            for item in response.references
        ),
    )


def to_feature_document_search_result_response(
    response: ServiceDocumentSearchResultResponse,
) -> DocumentSearchResultResponse:
    return DocumentSearchResultResponse(
        document_id=response.document_id,
        document_number=response.document_number,
        document_title=response.document_title,
        document_type=response.document_type,
        status=response.status,
    )


class CreateDocumentFeature:
    """Feature facade for document creation."""

    def __init__(self, *, service: CreateDocumentService) -> None:
        self._service = service

    def execute(self, request: CreateDocumentRequest) -> CreateDocumentResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    document_number=request.document_number,
                    document_title=request.document_title,
                    document_type=request.document_type,
                    document_id=request.document_id,
                    status=request.status,
                    description=request.description,
                    created_at=request.created_at,
                    updated_at=request.updated_at,
                    archived_at=request.archived_at,
                    disposed_at=request.disposed_at,
                    versions=tuple(
                        to_service_document_version_input(item)
                        for item in request.versions
                    ),
                    references=tuple(
                        to_service_document_reference_input(item)
                        for item in request.references
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create document feature failed") from exc

        return CreateDocumentResponse(
            document=to_feature_document_response(service_response.document)
        )
