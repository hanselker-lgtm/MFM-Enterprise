"""Document aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.domain.document.events import DocumentArchived
from mfm.domain.document.events import DocumentCreated
from mfm.domain.document.events import DocumentDisposed
from mfm.domain.document.events import DocumentReferenceAdded
from mfm.domain.document.events import DocumentStatusChanged
from mfm.domain.document.events import DocumentUpdated
from mfm.domain.document.events import DocumentVersionAdded
from mfm.domain.document.exceptions import InvalidDocumentError
from mfm.domain.document.exceptions import InvalidDocumentReferenceError
from mfm.domain.document.exceptions import InvalidDocumentStateError
from mfm.domain.document.exceptions import InvalidDocumentVersionError


@dataclass(slots=True)
class Document(AggregateRoot):
    """Aggregate root for cross-capability document metadata."""

    document_number: DocumentNumber
    document_title: DocumentTitle
    document_type: DocumentType
    id: DocumentId = field(default_factory=DocumentId.new)
    status: DocumentStatus = DocumentStatus.DRAFT
    description: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    archived_at: datetime | None = None
    disposed_at: datetime | None = None
    versions: list[DocumentVersion] = field(default_factory=list)
    references: list[DocumentReference] = field(default_factory=list)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, DocumentId):
            self.id = DocumentId(self.id)

        if not isinstance(self.document_number, DocumentNumber):
            self.document_number = DocumentNumber(self.document_number)

        if not isinstance(self.document_title, DocumentTitle):
            self.document_title = DocumentTitle(self.document_title)

        if not isinstance(self.document_type, DocumentType):
            self.document_type = DocumentType(self.document_type)

        if not isinstance(self.status, DocumentStatus):
            self.status = DocumentStatus(str(self.status).upper())

        self.description = self._normalize_optional_text(self.description)
        self.created_at = self._normalize_optional_datetime(self.created_at) or datetime.now(UTC)
        self.updated_at = self._normalize_optional_datetime(self.updated_at)
        self.archived_at = self._normalize_optional_datetime(self.archived_at)
        self.disposed_at = self._normalize_optional_datetime(self.disposed_at)

        self.versions = [
            version
            if isinstance(version, DocumentVersion)
            else DocumentVersion(**version)
            for version in self.versions
        ]
        self.references = [
            reference
            if isinstance(reference, DocumentReference)
            else DocumentReference(**reference)
            for reference in self.references
        ]

        self._validate_state()
        self._validate_versions_sequence()

        self.add_event(DocumentCreated(document_id=self.id.value))

    def update_metadata(
        self,
        *,
        document_title: DocumentTitle | str | None = None,
        document_type: DocumentType | str | None = None,
        description: str | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """Update mutable document metadata."""
        if self.status is DocumentStatus.DISPOSED:
            raise InvalidDocumentStateError("disposed documents cannot be updated")

        if document_title is not None:
            self.document_title = (
                document_title
                if isinstance(document_title, DocumentTitle)
                else DocumentTitle(document_title)
            )

        if document_type is not None:
            self.document_type = (
                document_type
                if isinstance(document_type, DocumentType)
                else DocumentType(document_type)
            )

        if description is not None:
            self.description = self._normalize_optional_text(description)

        self.updated_at = self._normalize_optional_datetime(updated_at) or datetime.now(UTC)
        self.add_event(DocumentUpdated(document_id=self.id.value))

    def add_version(self, version: DocumentVersion | dict[str, object], *, when: datetime | None = None) -> None:
        """Append a version while enforcing immutable sequence semantics."""
        if self.status in {DocumentStatus.ARCHIVED, DocumentStatus.DISPOSED}:
            raise InvalidDocumentStateError("cannot add versions to archived or disposed documents")

        new_version = version if isinstance(version, DocumentVersion) else DocumentVersion(**version)
        expected_number = 1 if not self.versions else self.versions[-1].version_number + 1
        if new_version.version_number != expected_number:
            raise InvalidDocumentVersionError(
                f"invalid version sequence: expected {expected_number}, got {new_version.version_number}"
            )

        self.versions.append(new_version)
        self.updated_at = self._normalize_optional_datetime(when) or datetime.now(UTC)
        self.add_event(
            DocumentVersionAdded(
                document_id=self.id.value,
                version_number=new_version.version_number,
            )
        )

    def add_reference(
        self,
        reference: DocumentReference | dict[str, object],
        *,
        when: datetime | None = None,
    ) -> None:
        """Attach a validated cross-capability reference."""
        if self.status is DocumentStatus.DISPOSED:
            raise InvalidDocumentStateError("disposed documents cannot add references")

        new_reference = reference if isinstance(reference, DocumentReference) else DocumentReference(**reference)
        if any(
            existing.target_capability == new_reference.target_capability
            and existing.target_aggregate_type == new_reference.target_aggregate_type
            and existing.target_aggregate_id == new_reference.target_aggregate_id
            for existing in self.references
        ):
            raise InvalidDocumentReferenceError("duplicate document reference")

        self.references.append(new_reference)
        self.updated_at = self._normalize_optional_datetime(when) or datetime.now(UTC)
        self.add_event(
            DocumentReferenceAdded(
                document_id=self.id.value,
                target_capability=new_reference.target_capability,
                target_aggregate_type=new_reference.target_aggregate_type,
                target_aggregate_id=new_reference.target_aggregate_id,
            )
        )

    def change_status(self, status: DocumentStatus | str, *, when: datetime | None = None) -> None:
        """Change lifecycle state while enforcing allowed transitions."""
        new_status = status if isinstance(status, DocumentStatus) else DocumentStatus(str(status).upper())

        allowed_transitions: dict[DocumentStatus, set[DocumentStatus]] = {
            DocumentStatus.DRAFT: {DocumentStatus.ACTIVE},
            DocumentStatus.ACTIVE: {DocumentStatus.ARCHIVED, DocumentStatus.DISPOSED},
            DocumentStatus.ARCHIVED: {DocumentStatus.ACTIVE, DocumentStatus.DISPOSED},
            DocumentStatus.DISPOSED: set(),
        }

        if new_status is self.status:
            return

        if new_status not in allowed_transitions[self.status]:
            raise InvalidDocumentStateError(
                f"invalid document status transition: {self.status} -> {new_status}"
            )

        if new_status is DocumentStatus.ACTIVE and not self.versions:
            raise InvalidDocumentStateError("active documents require at least one version")

        previous_status = self.status
        changed_at = self._normalize_optional_datetime(when) or datetime.now(UTC)
        self.status = new_status
        self.updated_at = changed_at

        if new_status is DocumentStatus.ARCHIVED:
            self.archived_at = changed_at
            self.disposed_at = None
            self.add_event(DocumentArchived(document_id=self.id.value, archived_at=changed_at))
            return

        if new_status is DocumentStatus.DISPOSED:
            self.disposed_at = changed_at
            self.add_event(DocumentDisposed(document_id=self.id.value, disposed_at=changed_at))
            return

        self.archived_at = None
        self.disposed_at = None
        self.add_event(
            DocumentStatusChanged(
                document_id=self.id.value,
                previous_status=str(previous_status),
                new_status=str(new_status),
            )
        )

    def _validate_state(self) -> None:
        if self.status is DocumentStatus.ACTIVE and not self.versions:
            raise InvalidDocumentStateError("active documents require at least one version")

        if self.status is DocumentStatus.ARCHIVED and self.archived_at is None:
            raise InvalidDocumentStateError("archived documents require archived_at")

        if self.status is not DocumentStatus.ARCHIVED and self.archived_at is not None:
            raise InvalidDocumentStateError("archived_at is only allowed for ARCHIVED status")

        if self.status is DocumentStatus.DISPOSED and self.disposed_at is None:
            raise InvalidDocumentStateError("disposed documents require disposed_at")

        if self.status is not DocumentStatus.DISPOSED and self.disposed_at is not None:
            raise InvalidDocumentStateError("disposed_at is only allowed for DISPOSED status")

    def _validate_versions_sequence(self) -> None:
        expected = 1
        for version in self.versions:
            if version.version_number != expected:
                raise InvalidDocumentVersionError(
                    f"invalid version sequence: expected {expected}, got {version.version_number}"
                )
            expected += 1

    @staticmethod
    def _normalize_optional_text(value: str | None) -> str | None:
        if value is None:
            return None
        normalized = str(value).strip()
        return normalized or None

    @staticmethod
    def _normalize_optional_datetime(value: datetime | None) -> datetime | None:
        if value is None:
            return None
        if value.tzinfo is None:
            raise InvalidDocumentError("datetime values must be timezone-aware")
        return value.astimezone(UTC)
