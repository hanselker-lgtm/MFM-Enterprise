from __future__ import annotations

from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import UUID

import pytest

from mfm.domain.document.document import Document
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_repository import DocumentRepository
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


def _dt(year: int, month: int, day: int, hour: int = 8, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _version(number: int) -> DocumentVersion:
    return DocumentVersion(
        version_number=number,
        storage_key=f"documents/doc-001/v{number}.pdf",
        file_name=f"v{number}.pdf",
        mime_type="application/pdf",
        checksum=f"sha256:{number:02d}",
        size_bytes=2048,
        created_at=_dt(2027, 1, number),
    )


def _reference(
    *,
    exists: bool = True,
    authorized: bool = True,
    is_soft_deleted: bool = False,
    is_archived: bool = False,
) -> DocumentReference:
    return DocumentReference(
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id="0c8ca4d4-410c-4f42-95f8-40eb1f2afc0f",
        exists=exists,
        authorized=authorized,
        is_soft_deleted=is_soft_deleted,
        is_archived=is_archived,
        checked_at=_dt(2027, 1, 5),
    )


def _document(*, status: DocumentStatus = DocumentStatus.DRAFT, versions: list[DocumentVersion] | None = None) -> Document:
    return Document(
        document_number=DocumentNumber("DOC-001"),
        document_title=DocumentTitle("Class certificate annex"),
        document_type=DocumentType("CERTIFICATE_ATTACHMENT"),
        status=status,
        versions=versions or [],
    )


def test_document_creation_normalizes_and_emits_created_event() -> None:
    document = _document()
    events = document.pull_events()

    assert document.document_number.value == "DOC-001"
    assert document.document_title.value == "Class certificate annex"
    assert document.document_type.value == "CERTIFICATE_ATTACHMENT"
    assert document.status is DocumentStatus.DRAFT
    assert document.created_at is not None
    assert document.created_at.tzinfo is UTC
    assert any(isinstance(event, DocumentCreated) for event in events)


def test_document_rejects_naive_datetime_values() -> None:
    with pytest.raises(InvalidDocumentError):
        Document(
            document_number=DocumentNumber("DOC-001"),
            document_title=DocumentTitle("Class certificate annex"),
            document_type=DocumentType("CERTIFICATE_ATTACHMENT"),
            created_at=datetime(2027, 1, 1, 8, 0),
        )


def test_active_document_requires_at_least_one_version() -> None:
    with pytest.raises(InvalidDocumentStateError):
        _document(status=DocumentStatus.ACTIVE)


def test_archived_status_requires_archived_at() -> None:
    with pytest.raises(InvalidDocumentStateError):
        _document(status=DocumentStatus.ARCHIVED)


def test_update_metadata_emits_updated_event() -> None:
    document = _document()
    document.pull_events()

    document.update_metadata(
        document_title="Updated annex",
        document_type="SURVEY_REPORT",
        description="Annual renewal evidence",
    )
    events = document.pull_events()

    assert document.document_title.value == "Updated annex"
    assert document.document_type.value == "SURVEY_REPORT"
    assert document.description == "Annual renewal evidence"
    assert document.updated_at is not None
    assert any(isinstance(event, DocumentUpdated) for event in events)


def test_add_version_enforces_sequence_and_emits_event() -> None:
    document = _document()
    document.pull_events()

    document.add_version(_version(1), when=_dt(2027, 1, 10))
    events = document.pull_events()

    assert len(document.versions) == 1
    assert document.versions[0].version_number == 1
    assert any(isinstance(event, DocumentVersionAdded) for event in events)


def test_add_version_rejects_invalid_sequence() -> None:
    document = _document()
    document.add_version(_version(1))

    with pytest.raises(InvalidDocumentVersionError):
        document.add_version(_version(3))


def test_add_reference_uses_cross_capability_contract_fields() -> None:
    document = _document()
    document.pull_events()

    document.add_reference(_reference(), when=_dt(2027, 1, 11))
    events = document.pull_events()

    assert len(document.references) == 1
    assert document.references[0].target_capability == "PROJECTS"
    assert document.references[0].target_aggregate_type == "PROJECT"
    assert document.references[0].target_aggregate_id == "0c8ca4d4-410c-4f42-95f8-40eb1f2afc0f"
    assert any(isinstance(event, DocumentReferenceAdded) for event in events)


def test_add_reference_rejects_non_existing_target() -> None:
    with pytest.raises(InvalidDocumentReferenceError):
        _reference(exists=False)


def test_change_status_emits_archived_and_disposed_events() -> None:
    document = _document(versions=[_version(1)])
    document.pull_events()

    archived_at = _dt(2027, 2, 1, 10)
    disposed_at = _dt(2027, 3, 1, 10)

    document.change_status(DocumentStatus.ACTIVE, when=_dt(2027, 1, 20, 10))
    active_events = document.pull_events()
    assert any(isinstance(event, DocumentStatusChanged) for event in active_events)

    document.change_status(DocumentStatus.ARCHIVED, when=archived_at)
    archived_events = document.pull_events()
    assert document.archived_at == archived_at
    assert any(isinstance(event, DocumentArchived) for event in archived_events)

    document.change_status(DocumentStatus.DISPOSED, when=disposed_at)
    disposed_events = document.pull_events()
    assert document.disposed_at == disposed_at
    assert any(isinstance(event, DocumentDisposed) for event in disposed_events)


def test_change_status_rejects_invalid_transition() -> None:
    document = _document(versions=[_version(1)])

    with pytest.raises(InvalidDocumentStateError):
        document.change_status(DocumentStatus.DISPOSED)


def test_document_domain_has_no_infrastructure_or_sqlalchemy_imports() -> None:
    document_dir = Path("src/mfm/domain/document")
    forbidden_markers = (
        "sqlalchemy",
        "mfm.infrastructure",
        "mfm.database",
    )

    python_files = sorted(document_dir.glob("*.py"))
    assert python_files, "expected document domain python files"

    for file_path in python_files:
        content = file_path.read_text(encoding="utf-8").lower()
        for marker in forbidden_markers:
            assert marker not in content, f"forbidden marker '{marker}' found in {file_path}"


def test_document_repository_contract_methods_match_document_aggregate_scope() -> None:
    methods = {
        name
        for name, value in DocumentRepository.__dict__.items()
        if callable(value) and not name.startswith("_")
    }

    expected_methods = {
        "add",
        "update",
        "remove",
        "get",
        "exists",
        "get_by_number",
        "list",
        "search",
        "next_identity",
        "list_by_status",
    }

    assert expected_methods.issubset(methods)


def test_document_id_is_uuid_backed_identity() -> None:
    document = _document()

    assert isinstance(document.id.value, UUID)
