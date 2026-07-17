"""Application service for CAP-006 document and archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Any
from typing import Protocol
from uuid import UUID

from mfm.domain.document_archive.archive import Archive
from mfm.domain.document_archive.attachment import Attachment
from mfm.domain.document_archive.category import Category
from mfm.domain.document_archive.document import Document
from mfm.domain.document_archive.folder import Folder
from mfm.domain.document_archive.version import Version


class ApplicationException(Exception):
    """Base exception for document archive service failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


ALLOWED_CAPABILITIES: tuple[str, ...] = (
    "MEMBERSHIP",
    "ORGANIZATION",
    "EVENTS",
    "BILLING",
    "PROJECTS",
)


@dataclass(frozen=True, slots=True)
class CreateArchiveDocumentRequest:
    document_number: str
    document_title: str
    document_type: str
    folder_name: str
    folder_path: str
    category_code: str
    category_name: str
    initial_storage_key: str
    file_name: str | None = None
    description: str | None = None
    created_at: datetime | None = None

    def validate(self) -> None:
        for name, value in (
            ("document_number", self.document_number),
            ("document_title", self.document_title),
            ("document_type", self.document_type),
            ("folder_name", self.folder_name),
            ("folder_path", self.folder_path),
            ("category_code", self.category_code),
            ("category_name", self.category_name),
            ("initial_storage_key", self.initial_storage_key),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValidationException(f"{name} must be non-empty string")
        if self.file_name is not None and not isinstance(self.file_name, str):
            raise ValidationException("file_name must be string or None")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.created_at is not None and (
            not isinstance(self.created_at, datetime) or self.created_at.tzinfo is None
        ):
            raise ValidationException("created_at must be timezone-aware datetime or None")


@dataclass(frozen=True, slots=True)
class AddArchiveVersionRequest:
    document_id: UUID
    version_number: int
    storage_key: str
    file_name: str | None = None
    created_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.version_number, int) or self.version_number <= 0:
            raise ValidationException("version_number must be positive integer")
        if not isinstance(self.storage_key, str) or not self.storage_key.strip():
            raise ValidationException("storage_key must be non-empty string")
        if self.file_name is not None and not isinstance(self.file_name, str):
            raise ValidationException("file_name must be string or None")
        if self.created_at is not None and (
            not isinstance(self.created_at, datetime) or self.created_at.tzinfo is None
        ):
            raise ValidationException("created_at must be timezone-aware datetime or None")


@dataclass(frozen=True, slots=True)
class AttachArchiveRequest:
    document_id: UUID
    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    description: str | None = None
    checked_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.target_capability, str) or not self.target_capability.strip():
            raise ValidationException("target_capability must be non-empty string")
        if not isinstance(self.target_aggregate_type, str) or not self.target_aggregate_type.strip():
            raise ValidationException("target_aggregate_type must be non-empty string")
        if not isinstance(self.target_aggregate_id, str) or not self.target_aggregate_id.strip():
            raise ValidationException("target_aggregate_id must be non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.checked_at is not None and (
            not isinstance(self.checked_at, datetime) or self.checked_at.tzinfo is None
        ):
            raise ValidationException("checked_at must be timezone-aware datetime or None")


@dataclass(frozen=True, slots=True)
class ArchiveDocumentRecordRequest:
    document_id: UUID
    reason: str
    archived_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.document_id, UUID):
            raise ValidationException("document_id must be UUID")
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ValidationException("reason must be non-empty string")
        if self.archived_at is not None and (
            not isinstance(self.archived_at, datetime) or self.archived_at.tzinfo is None
        ):
            raise ValidationException("archived_at must be timezone-aware datetime or None")


@dataclass(frozen=True, slots=True)
class DocumentArchiveResponse:
    document_id: UUID
    document_number: str
    document_title: str
    status: str
    category_code: str
    folder_path: str
    versions_count: int
    attachments_count: int
    archived: bool
    generated_at: datetime


class DocumentArchiveRepositoryPort(Protocol):
    def get(self, document_id: UUID) -> Document | None: ...

    def save(self, document: Document) -> None: ...


class CreateDocumentFeaturePort(Protocol):
    def execute(self, request: Any): ...


class RegisterDocumentVersionFeaturePort(Protocol):
    def execute(self, request: Any): ...


class AttachReferenceFeaturePort(Protocol):
    def execute(self, request: Any): ...


class ArchiveDocumentFeaturePort(Protocol):
    def execute(self, request: Any): ...


class DocumentArchiveService:
    """Orchestrates document and archive operations via feature APIs only."""

    def __init__(
        self,
        *,
        repository: DocumentArchiveRepositoryPort,
        create_document_feature: CreateDocumentFeaturePort,
        register_document_version_feature: RegisterDocumentVersionFeaturePort,
        attach_reference_feature: AttachReferenceFeaturePort,
        archive_document_feature: ArchiveDocumentFeaturePort,
    ) -> None:
        self._repository = repository
        self._create_document_feature = create_document_feature
        self._register_document_version_feature = register_document_version_feature
        self._attach_reference_feature = attach_reference_feature
        self._archive_document_feature = archive_document_feature

    def create_document(self, request: CreateArchiveDocumentRequest) -> DocumentArchiveResponse:
        request.validate()
        now = request.created_at or datetime.now(UTC)

        try:
            from mfm.application.features.documents.create_document_feature import (
                CreateDocumentRequest,
            )
            from mfm.application.features.documents.create_document_feature import (
                DocumentVersionInput,
            )

            created = self._create_document_feature.execute(
                CreateDocumentRequest(
                    document_number=request.document_number,
                    document_title=request.document_title,
                    document_type=request.document_type,
                    status="ACTIVE",
                    description=request.description,
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=request.initial_storage_key,
                            file_name=request.file_name,
                            created_at=now,
                        ),
                    ),
                )
            )

            folder = Folder(name=request.folder_name, path=request.folder_path)
            category = Category(code=request.category_code, name=request.category_name)
            document = Document(
                document_id=created.document.document_id,
                document_number=created.document.document_number,
                document_title=created.document.document_title,
                document_type=created.document.document_type,
                status=created.document.status,
                folder=folder,
                category=category,
                versions=[
                    Version(
                        version_number=1,
                        storage_key=request.initial_storage_key,
                        file_name=request.file_name,
                        created_at=now,
                    )
                ],
            )
            self._repository.save(document)
            return self._to_response(document)
        except ValidationException:
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create archive document failed") from exc

    def add_version(self, request: AddArchiveVersionRequest) -> DocumentArchiveResponse:
        request.validate()
        now = request.created_at or datetime.now(UTC)

        try:
            from mfm.application.features.documents.create_document_feature import (
                DocumentVersionInput,
            )
            from mfm.application.features.documents.register_document_version_feature import (
                RegisterDocumentVersionRequest,
            )

            document = self._require_document(request.document_id)
            self._register_document_version_feature.execute(
                RegisterDocumentVersionRequest(
                    document_id=request.document_id,
                    version=DocumentVersionInput(
                        version_number=request.version_number,
                        storage_key=request.storage_key,
                        file_name=request.file_name,
                        created_at=now,
                    ),
                    registered_at=now,
                )
            )

            document.add_version(
                Version(
                    version_number=request.version_number,
                    storage_key=request.storage_key,
                    file_name=request.file_name,
                    created_at=now,
                )
            )
            self._repository.save(document)
            return self._to_response(document)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Add archive version failed") from exc

    def attach(self, request: AttachArchiveRequest) -> DocumentArchiveResponse:
        request.validate()
        checked_at = request.checked_at or datetime.now(UTC)

        capability = request.target_capability.strip().upper()
        if capability not in ALLOWED_CAPABILITIES:
            allowed = ", ".join(ALLOWED_CAPABILITIES)
            raise ValidationException(f"target_capability must be one of: {allowed}")

        try:
            from mfm.application.features.documents.attach_reference_feature import (
                AttachReferenceRequest,
            )
            from mfm.application.features.documents.create_document_feature import (
                DocumentReferenceInput,
            )

            document = self._require_document(request.document_id)
            self._attach_reference_feature.execute(
                AttachReferenceRequest(
                    document_id=request.document_id,
                    reference=DocumentReferenceInput(
                        target_capability=capability,
                        target_aggregate_type=request.target_aggregate_type,
                        target_aggregate_id=request.target_aggregate_id,
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=checked_at,
                        description=request.description,
                    ),
                    attached_at=checked_at,
                )
            )

            document.add_attachment(
                Attachment(
                    target_capability=capability,
                    target_aggregate_type=request.target_aggregate_type,
                    target_aggregate_id=request.target_aggregate_id,
                    description=request.description,
                )
            )
            self._repository.save(document)
            return self._to_response(document)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Attach archive reference failed") from exc

    def archive(self, request: ArchiveDocumentRecordRequest) -> DocumentArchiveResponse:
        request.validate()
        archived_at = request.archived_at or datetime.now(UTC)

        try:
            from mfm.application.features.documents.archive_document_feature import (
                ArchiveDocumentRequest,
            )

            document = self._require_document(request.document_id)
            self._archive_document_feature.execute(
                ArchiveDocumentRequest(
                    document_id=request.document_id,
                    archived_at=archived_at,
                )
            )

            document.mark_archived(
                Archive(
                    archived_at=archived_at,
                    reason=request.reason,
                )
            )
            self._repository.save(document)
            return self._to_response(document)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Archive document record failed") from exc

    def _require_document(self, document_id: UUID) -> Document:
        document = self._repository.get(document_id)
        if document is None:
            raise BusinessRuleViolation(f"Document archive profile {document_id} not found")
        return document

    @staticmethod
    def _to_response(document: Document) -> DocumentArchiveResponse:
        return DocumentArchiveResponse(
            document_id=document.document_id,
            document_number=document.document_number,
            document_title=document.document_title,
            status=document.status,
            category_code=document.category.code,
            folder_path=document.folder.path,
            versions_count=len(document.versions),
            attachments_count=len(document.attachments),
            archived=document.archive is not None,
            generated_at=datetime.now(UTC),
        )
