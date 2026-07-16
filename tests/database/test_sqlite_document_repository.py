from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pathlib import Path
import weakref
from uuid import UUID

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def _aware(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int = 0,
    *,
    offset_hours: int = 0,
) -> datetime:
    local_tz = timezone(timedelta(hours=offset_hours))
    return datetime(year, month, day, hour, minute, tzinfo=local_tz)


def _version(number: int) -> DocumentVersion:
    return DocumentVersion(
        version_number=number,
        storage_key=f"documents/doc-repo/v{number}.pdf",
        file_name=f"v{number}.pdf",
        mime_type="application/pdf",
        checksum=f"sha256:{number:02d}",
        size_bytes=1024 * number,
        created_at=_aware(2031, 1, number, 9, 0, offset_hours=1),
    )


def _reference(index: int) -> DocumentReference:
    return DocumentReference(
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id=f"00000000-0000-0000-0000-00000000E{index:03d}",
        exists=True,
        authorized=True,
        is_soft_deleted=False,
        is_archived=False,
        checked_at=_aware(2031, 1, index, 10, 0, offset_hours=1),
        description=f"Reference {index}",
    )


def _document(
    *,
    document_id: UUID,
    number: str,
    status: DocumentStatus = DocumentStatus.DRAFT,
    include_rows: int = 1,
) -> Document:
    document = Document(
        id=DocumentId(document_id),
        document_number=DocumentNumber(number),
        document_title=DocumentTitle("Inspection dossier"),
        document_type=DocumentType("MAINTENANCE_REPORT"),
        status=DocumentStatus.DRAFT,
        description="Repository integration aggregate",
        created_at=_aware(2031, 1, 1, 8, 0, offset_hours=1),
        updated_at=_aware(2031, 1, 2, 9, 0, offset_hours=1),
    )

    if include_rows:
        for idx in range(1, include_rows + 1):
            document.add_version(_version(idx))
            document.add_reference(_reference(idx))

    if status is DocumentStatus.ACTIVE:
        document.change_status(DocumentStatus.ACTIVE, when=_aware(2031, 2, 1, 12, 0, offset_hours=1))
    elif status is DocumentStatus.ARCHIVED:
        document.change_status(DocumentStatus.ACTIVE, when=_aware(2031, 2, 1, 12, 0, offset_hours=1))
        document.change_status(DocumentStatus.ARCHIVED, when=_aware(2031, 3, 1, 12, 0, offset_hours=1))
    elif status is DocumentStatus.DISPOSED:
        document.change_status(DocumentStatus.ACTIVE, when=_aware(2031, 2, 1, 12, 0, offset_hours=1))
        document.change_status(DocumentStatus.DISPOSED, when=_aware(2031, 3, 15, 12, 0, offset_hours=1))

    document.version = 1
    document.pull_events()
    return document


def test_document_repository_create_read_and_missing(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-add-get.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D001"),
            number="DOC-REPO-001",
            include_rows=1,
        )

        repository.add(document)
        session.commit()

        loaded = repository.get(document.id)
        assert loaded is not None
        assert loaded.id == document.id
        assert loaded.document_number.value == "DOC-REPO-001"
        assert loaded.document_title.value == "Inspection dossier"

        missing = repository.get(DocumentId(UUID("00000000-0000-0000-0000-00000000D999")))
        assert missing is None
    finally:
        session.close()


def test_document_repository_exists_and_next_identity(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-exists.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D002"),
            number="DOC-REPO-002",
            include_rows=1,
        )

        repository.add(document)
        session.commit()

        assert repository.exists(document.id) is True
        assert (
            repository.exists(DocumentId(UUID("00000000-0000-0000-0000-00000000D998")))
            is False
        )
        assert isinstance(repository.next_identity(), DocumentId)
    finally:
        session.close()


def test_document_repository_update_persists_aggregate_roundtrip(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-update.sqlite"
    first_session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(first_session))
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D003"),
            number="DOC-REPO-003",
            include_rows=1,
        )

        repository.add(document)
        first_session.commit()

        loaded = repository.get(document.id)
        assert loaded is not None
        loaded.update_metadata(
            document_title="Inspection dossier updated",
            description="Updated repository plan",
            updated_at=_aware(2031, 2, 1, 8, 0, offset_hours=1),
        )
        loaded.add_version(_version(2))
        loaded.add_reference(_reference(2))

        repository.update(loaded)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(second_session))
        restored = repository.get(DocumentId(UUID("00000000-0000-0000-0000-00000000D003")))

        assert restored is not None
        assert restored.document_title.value == "Inspection dossier updated"
        assert restored.description == "Updated repository plan"
        assert len(restored.versions) == 2
        assert len(restored.references) == 2
        assert restored.versions[1].version_number == 2
        assert restored.references[1].target_aggregate_id.endswith("E002")
        assert restored.version == 2
        assert restored.created_at is not None and restored.created_at.tzinfo is UTC
    finally:
        second_session.close()


def test_document_repository_remove_and_notfound_handling(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-remove.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D004"),
            number="DOC-REPO-004",
            include_rows=1,
        )
        repository.add(document)
        session.commit()

        repository.remove(document.id)
        session.commit()

        assert repository.get(document.id) is None

        with pytest.raises(ValueError):
            repository.remove(document.id)
    finally:
        session.close()


def test_document_repository_list_and_status_filter(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-list.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))

        draft = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D005"),
            number="DOC-REPO-A",
            status=DocumentStatus.DRAFT,
            include_rows=1,
        )
        active = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D006"),
            number="DOC-REPO-B",
            status=DocumentStatus.ACTIVE,
            include_rows=1,
        )
        archived = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D007"),
            number="DOC-REPO-C",
            status=DocumentStatus.ARCHIVED,
            include_rows=1,
        )

        for entity in (active, archived, draft):
            repository.add(entity)
        session.commit()

        listed = repository.list()
        assert [item.document_number.value for item in listed] == [
            "DOC-REPO-A",
            "DOC-REPO-B",
            "DOC-REPO-C",
        ]

        active_only = repository.list(filters={"status": "ACTIVE"})
        assert [item.document_number.value for item in active_only] == ["DOC-REPO-B"]

        archived_only = repository.list_by_status(DocumentStatus.ARCHIVED)
        assert [item.document_number.value for item in archived_only] == ["DOC-REPO-C"]
    finally:
        session.close()


def test_document_repository_search_returns_projections(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-search.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))

        first = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D008"),
            number="DOC-SEARCH-001",
            status=DocumentStatus.DRAFT,
            include_rows=1,
        )
        second = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D009"),
            number="DOC-SEARCH-002",
            status=DocumentStatus.ACTIVE,
            include_rows=1,
        )

        repository.add(first)
        repository.add(second)
        session.commit()

        text_hits = repository.search("SEARCH-001")
        assert len(text_hits) == 1
        assert text_hits[0]["document_number"] == "DOC-SEARCH-001"

        active_hits = repository.search({"status": "ACTIVE"})
        assert [row["document_number"] for row in active_hits] == ["DOC-SEARCH-002"]

        capability_hits = repository.search({"target_capability": "PROJECTS"})
        assert sorted(row["document_number"] for row in capability_hits) == [
            "DOC-SEARCH-001",
            "DOC-SEARCH-002",
        ]
    finally:
        session.close()


def test_document_repository_duplicate_and_notfound_and_version_conflict(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-errors.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(session))
        first = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D010"),
            number="DOC-REPO-DUP",
            include_rows=1,
        )
        duplicate = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D011"),
            number="DOC-REPO-DUP",
            include_rows=1,
        )

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(duplicate)

        missing = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D012"),
            number="DOC-REPO-MISSING",
            include_rows=1,
        )
        with pytest.raises(ValueError):
            repository.update(missing)

        stale = repository.get(first.id)
        assert stale is not None
        stale.version = 0
        with pytest.raises(ValueError):
            repository.update(stale)
    finally:
        session.close()


def test_document_repository_roundtrip_persists_full_aggregate(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-document-repository-roundtrip.sqlite"
    first_session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(first_session))
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000D013"),
            number="DOC-REPO-ROUNDTRIP",
            include_rows=2,
        )

        repository.add(document)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteDocumentRepository(UnitOfWork(second_session))
        restored = repository.get(DocumentId(UUID("00000000-0000-0000-0000-00000000D013")))

        assert restored is not None
        assert restored.document_number.value == "DOC-REPO-ROUNDTRIP"
        assert restored.document_type.value == "MAINTENANCE_REPORT"
        assert restored.description == "Repository integration aggregate"
        assert [version.version_number for version in restored.versions] == [1, 2]
        assert [reference.target_aggregate_id[-4:] for reference in restored.references] == [
            "E001",
            "E002",
        ]
        assert restored.pull_events() == []
    finally:
        second_session.close()
