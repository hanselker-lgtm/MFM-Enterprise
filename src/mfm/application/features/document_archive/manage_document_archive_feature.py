"""Feature API for CAP-006 document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from typing import Protocol
from uuid import UUID

from mfm.application.document_archive.document_archive_service import (
    AddArchiveVersionRequest as ServiceAddArchiveVersionRequest,
)
from mfm.application.document_archive.document_archive_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.document_archive.document_archive_service import (
    ArchiveDocumentRecordRequest as ServiceArchiveDocumentRecordRequest,
)
from mfm.application.document_archive.document_archive_service import (
    AttachArchiveRequest as ServiceAttachArchiveRequest,
)
from mfm.application.document_archive.document_archive_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.document_archive.document_archive_service import (
    CreateArchiveDocumentRequest as ServiceCreateArchiveDocumentRequest,
)
from mfm.application.document_archive.document_archive_service import (
    DocumentArchiveResponse,
)
from mfm.application.document_archive.document_archive_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.document_archive.document_archive_service import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


DocumentArchiveOperation = Literal[
    "create-document",
    "add-version",
    "attach",
    "archive",
]


@dataclass(frozen=True, slots=True)
class ManageDocumentArchiveRequest:
    operation: DocumentArchiveOperation
    document_id: UUID | None = None
    document_number: str | None = None
    document_title: str | None = None
    document_type: str | None = None
    folder_name: str | None = None
    folder_path: str | None = None
    category_code: str | None = None
    category_name: str | None = None
    initial_storage_key: str | None = None
    version_number: int | None = None
    storage_key: str | None = None
    file_name: str | None = None
    description: str | None = None
    target_capability: str | None = None
    target_aggregate_type: str | None = None
    target_aggregate_id: str | None = None
    reason: str | None = None
    timestamp: datetime | None = None

    def validate(self) -> None:
        if self.operation not in (
            "create-document",
            "add-version",
            "attach",
            "archive",
        ):
            raise ValidationException("operation must be create-document, add-version, attach, or archive")

        if self.operation == "create-document":
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

        if self.operation == "add-version":
            if not isinstance(self.document_id, UUID):
                raise ValidationException("document_id must be UUID")
            if not isinstance(self.version_number, int) or self.version_number <= 0:
                raise ValidationException("version_number must be positive integer")
            if not isinstance(self.storage_key, str) or not self.storage_key.strip():
                raise ValidationException("storage_key must be non-empty string")

        if self.operation == "attach":
            if not isinstance(self.document_id, UUID):
                raise ValidationException("document_id must be UUID")
            if not isinstance(self.target_capability, str) or not self.target_capability.strip():
                raise ValidationException("target_capability must be non-empty string")
            if not isinstance(self.target_aggregate_type, str) or not self.target_aggregate_type.strip():
                raise ValidationException("target_aggregate_type must be non-empty string")
            if not isinstance(self.target_aggregate_id, str) or not self.target_aggregate_id.strip():
                raise ValidationException("target_aggregate_id must be non-empty string")

        if self.operation == "archive":
            if not isinstance(self.document_id, UUID):
                raise ValidationException("document_id must be UUID")
            if not isinstance(self.reason, str) or not self.reason.strip():
                raise ValidationException("reason must be non-empty string")

        if self.timestamp is not None and (
            not isinstance(self.timestamp, datetime) or self.timestamp.tzinfo is None
        ):
            raise ValidationException("timestamp must be timezone-aware datetime or None")


@dataclass(frozen=True, slots=True)
class ManageDocumentArchiveResponse:
    result: DocumentArchiveResponse


class DocumentArchiveServicePort(Protocol):
    def create_document(self, request: ServiceCreateArchiveDocumentRequest) -> DocumentArchiveResponse: ...

    def add_version(self, request: ServiceAddArchiveVersionRequest) -> DocumentArchiveResponse: ...

    def attach(self, request: ServiceAttachArchiveRequest) -> DocumentArchiveResponse: ...

    def archive(self, request: ServiceArchiveDocumentRecordRequest) -> DocumentArchiveResponse: ...


class ManageDocumentArchiveFeature:
    """Feature facade for document archive operations."""

    def __init__(self, *, service: DocumentArchiveServicePort) -> None:
        self._service = service

    def execute(self, request: ManageDocumentArchiveRequest) -> ManageDocumentArchiveResponse:
        request.validate()

        try:
            if request.operation == "create-document":
                result = self._service.create_document(
                    ServiceCreateArchiveDocumentRequest(
                        document_number=request.document_number,
                        document_title=request.document_title,
                        document_type=request.document_type,
                        folder_name=request.folder_name,
                        folder_path=request.folder_path,
                        category_code=request.category_code,
                        category_name=request.category_name,
                        initial_storage_key=request.initial_storage_key,
                        file_name=request.file_name,
                        description=request.description,
                        created_at=request.timestamp,
                    )
                )
                return ManageDocumentArchiveResponse(result=result)

            if request.operation == "add-version":
                result = self._service.add_version(
                    ServiceAddArchiveVersionRequest(
                        document_id=request.document_id,
                        version_number=request.version_number,
                        storage_key=request.storage_key,
                        file_name=request.file_name,
                        created_at=request.timestamp,
                    )
                )
                return ManageDocumentArchiveResponse(result=result)

            if request.operation == "attach":
                result = self._service.attach(
                    ServiceAttachArchiveRequest(
                        document_id=request.document_id,
                        target_capability=request.target_capability,
                        target_aggregate_type=request.target_aggregate_type,
                        target_aggregate_id=request.target_aggregate_id,
                        description=request.description,
                        checked_at=request.timestamp,
                    )
                )
                return ManageDocumentArchiveResponse(result=result)

            result = self._service.archive(
                ServiceArchiveDocumentRecordRequest(
                    document_id=request.document_id,
                    reason=request.reason,
                    archived_at=request.timestamp,
                )
            )
            return ManageDocumentArchiveResponse(result=result)
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Manage document archive feature failed") from exc
