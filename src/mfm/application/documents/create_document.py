"""Create Document use case and shared document application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from typing import Mapping
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.domain.document.exceptions import DocumentError


class ApplicationException(Exception):
    """Base exception for document application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


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


class CreateDocumentUseCase:
    """Create document aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateDocumentRequest) -> CreateDocumentResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: DocumentRepository = uow.document_repository

                normalized_number = DocumentNumber(request.document_number)
                existing = repository.get_by_number(normalized_number)
                if existing is not None:
                    raise BusinessRuleViolation(
                        f"Document number {normalized_number.value} already exists"
                    )

                document_id = (
                    DocumentId(request.document_id)
                    if request.document_id is not None
                    else repository.next_identity()
                )

                document = Document(
                    id=document_id,
                    document_number=normalized_number,
                    document_title=DocumentTitle(request.document_title),
                    document_type=DocumentType(request.document_type),
                    status=DocumentStatus(request.status.strip().upper()),
                    description=request.description,
                    created_at=request.created_at,
                    updated_at=request.updated_at,
                    archived_at=request.archived_at,
                    disposed_at=request.disposed_at,
                    versions=[to_document_version(item) for item in request.versions],
                    references=[to_document_reference(item) for item in request.references],
                )
                repository.add(document)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except DocumentError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create document failed") from exc

        return CreateDocumentResponse(document=to_document_response(document))


def to_document_version(value: DocumentVersionInput) -> DocumentVersion:
    create_kwargs: dict[str, object] = {
        "version_number": value.version_number,
        "storage_key": value.storage_key,
        "file_name": value.file_name,
        "mime_type": value.mime_type,
        "checksum": value.checksum,
        "size_bytes": value.size_bytes,
    }
    if value.created_at is not None:
        create_kwargs["created_at"] = value.created_at
    return DocumentVersion(**create_kwargs)


def to_document_reference(value: DocumentReferenceInput) -> DocumentReference:
    create_kwargs: dict[str, object] = {
        "target_capability": value.target_capability,
        "target_aggregate_type": value.target_aggregate_type,
        "target_aggregate_id": value.target_aggregate_id,
        "exists": value.exists,
        "authorized": value.authorized,
        "is_soft_deleted": value.is_soft_deleted,
        "is_archived": value.is_archived,
        "checked_at": value.checked_at,
        "description": value.description,
    }
    if value.reference_id is not None:
        create_kwargs["id"] = value.reference_id
    return DocumentReference(**create_kwargs)


def to_document_version_response(value: DocumentVersion) -> DocumentVersionResponse:
    return DocumentVersionResponse(
        version_number=value.version_number,
        storage_key=value.storage_key,
        file_name=value.file_name,
        mime_type=value.mime_type,
        checksum=value.checksum,
        size_bytes=value.size_bytes,
        created_at=value.created_at,
    )


def to_document_reference_response(value: DocumentReference) -> DocumentReferenceResponse:
    return DocumentReferenceResponse(
        reference_id=value.id,
        target_capability=value.target_capability,
        target_aggregate_type=value.target_aggregate_type,
        target_aggregate_id=value.target_aggregate_id,
        exists=value.exists,
        authorized=value.authorized,
        is_soft_deleted=value.is_soft_deleted,
        is_archived=value.is_archived,
        checked_at=value.checked_at,
        description=value.description,
    )


def to_document_response(value: Document) -> DocumentResponse:
    return DocumentResponse(
        document_id=value.id.value,
        document_number=value.document_number.value,
        document_title=value.document_title.value,
        document_type=value.document_type.value,
        status=str(value.status),
        description=value.description,
        created_at=value.created_at,
        updated_at=value.updated_at,
        archived_at=value.archived_at,
        disposed_at=value.disposed_at,
        version=value.version,
        versions=tuple(to_document_version_response(item) for item in value.versions),
        references=tuple(
            to_document_reference_response(item) for item in value.references
        ),
    )


def to_document_search_result_response(row: Mapping[str, Any]) -> DocumentSearchResultResponse:
    return DocumentSearchResultResponse(
        document_id=UUID(str(row["id"])),
        document_number=str(row["document_number"]),
        document_title=str(row["document_title"]),
        document_type=str(row["document_type"]),
        status=str(row["status"]),
    )
