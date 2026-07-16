from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.infrastructure.persistence.documents.document_mapper import DocumentMapper
from mfm.infrastructure.persistence.documents.document_model import DocumentModel
from mfm.infrastructure.persistence.documents.document_reference_model import (
    DocumentReferenceModel,
)


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    connection = engine.connect()
    BaseModel.metadata.create_all(connection)
    session = Session(bind=connection)
    session.info["test_connection"] = connection
    session.info["test_engine"] = engine
    return session


def _close_session(session: Session) -> None:
    connection = session.info.pop("test_connection", None)
    engine = session.info.pop("test_engine", None)
    session.close()
    if isinstance(connection, Connection):
        connection.close()
    if isinstance(engine, Engine):
        engine.dispose()


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


def _document(*, document_id: UUID, number: str, with_rows: int = 1) -> Document:
    document = Document(
        id=DocumentId(document_id),
        document_number=DocumentNumber(number),
        document_title=DocumentTitle("Drydock report"),
        document_type=DocumentType("MAINTENANCE_REPORT"),
        status=DocumentStatus.DRAFT,
        description="Metadata only",
        created_at=_aware(2029, 4, 1, 8, 0, offset_hours=1),
        updated_at=_aware(2029, 4, 2, 9, 30, offset_hours=1),
    )
    document.pull_events()

    for index in range(with_rows):
        reference_id = UUID(f"00000000-0000-0000-0000-00000000A{index + 1:03d}")
        target_id = f"00000000-0000-0000-0000-00000000B{index + 1:03d}"
        document.add_version(
            DocumentVersion(
                version_number=index + 1,
                storage_key=f"documents/{number.lower()}/v{index + 1}.pdf",
                file_name=f"v{index + 1}.pdf",
                mime_type="application/pdf",
                checksum=f"sha256:{index + 1:02d}",
                size_bytes=1024 * (index + 1),
                created_at=_aware(2029, 4, 3 + index, 10, 0, offset_hours=2),
            )
        )
        document.add_reference(
            {
                "id": reference_id,
                "target_capability": "PROJECTS",
                "target_aggregate_type": "PROJECT",
                "target_aggregate_id": target_id,
                "exists": True,
                "authorized": True,
                "is_soft_deleted": False,
                "is_archived": False,
                "checked_at": _aware(2029, 4, 3 + index, 11, 0, offset_hours=2),
                "description": f"Link {index + 1}",
            }
        )

    document.version = 4
    document.pull_events()
    return document


def _persist_and_reload(session: Session, document: Document) -> Document:
    orm = DocumentMapper.to_orm_document(document)
    session.add(orm)
    session.commit()
    session.expunge_all()

    loaded = session.get(DocumentModel, document.id.value)
    assert loaded is not None
    return DocumentMapper.to_domain_document(loaded)


def test_document_model_creation_persists_expected_columns(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-model-creation")
    try:
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C001"),
            number="DOC-2029-001",
            with_rows=1,
        )

        orm = DocumentMapper.to_orm_document(document)
        session.add(orm)
        session.commit()

        loaded = session.get(DocumentModel, document.id.value)
        assert loaded is not None
        assert loaded.document_number == "DOC-2029-001"
        assert loaded.document_type == "MAINTENANCE_REPORT"
        assert loaded.status is DocumentStatus.DRAFT
        assert len(loaded.references) == 1
        assert loaded.references[0].storage_key.endswith("v1.pdf")
        assert loaded.references[0].mime_type == "application/pdf"
        assert loaded.references[0].checksum == "sha256:01"
        assert loaded.references[0].size_bytes == 1024
    finally:
        _close_session(session)


def test_document_to_orm_mapping_preserves_metadata_versions_and_references(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-to-orm")
    try:
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C002"),
            number="DOC-2029-002",
            with_rows=2,
        )

        orm = DocumentMapper.to_orm_document(document)
        session.add(orm)
        session.commit()

        stored = session.get(DocumentModel, document.id.value)
        assert stored is not None
        assert stored.version == 4
        assert len(stored.references) == 2
        assert [row.version_number for row in stored.references] == [1, 2]
        assert [row.reference_order for row in stored.references] == [0, 1]
        assert stored.references[1].target_aggregate_id.endswith("B002")
    finally:
        _close_session(session)


def test_orm_to_domain_mapping_preserves_document_without_information_loss(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-from-orm")
    try:
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C003"),
            number="DOC-2029-003",
            with_rows=2,
        )
        restored = _persist_and_reload(session, document)

        assert restored.id == document.id
        assert restored.document_number == document.document_number
        assert restored.document_title == document.document_title
        assert restored.document_type == document.document_type
        assert restored.description == document.description
        assert restored.version == 4
        assert len(restored.versions) == 2
        assert restored.versions[1].storage_key.endswith("v2.pdf")
        assert restored.versions[1].checksum == "sha256:02"
        assert len(restored.references) == 2
        assert restored.references[0].target_capability == "PROJECTS"
        assert restored.references[1].target_aggregate_id.endswith("B002")
    finally:
        _close_session(session)


def test_document_roundtrip_preserves_exact_metadata_and_reference_order(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-roundtrip")
    try:
        original = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C004"),
            number="DOC-2029-004",
            with_rows=2,
        )

        restored = _persist_and_reload(session, original)

        assert [version.version_number for version in restored.versions] == [1, 2]
        assert [reference.description for reference in restored.references] == [
            "Link 1",
            "Link 2",
        ]
        assert restored.versions[0].mime_type == "application/pdf"
        assert restored.versions[0].size_bytes == 1024
        assert restored.pull_events() == []
    finally:
        _close_session(session)


def test_document_mapper_supports_empty_aggregate(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-empty")
    try:
        empty_document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C005"),
            number="DOC-2029-005",
            with_rows=0,
        )

        restored = _persist_and_reload(session, empty_document)

        assert restored.id == empty_document.id
        assert restored.document_number.value == "DOC-2029-005"
        assert restored.versions == []
        assert restored.references == []
    finally:
        _close_session(session)


def test_document_mapper_supports_multiple_references(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-multi-reference")
    try:
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C006"),
            number="DOC-2029-006",
            with_rows=3,
        )

        restored = _persist_and_reload(session, document)

        assert len(restored.references) == 3
        assert [item.target_aggregate_id[-4:] for item in restored.references] == [
            "B001",
            "B002",
            "B003",
        ]
        assert [item.version_number for item in restored.versions] == [1, 2, 3]
    finally:
        _close_session(session)


def test_document_metadata_registers_document_tables(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-metadata")
    try:
        inspector = inspect(session.info["test_connection"])
        tables = set(inspector.get_table_names())

        assert "document" in tables
        assert "document_reference" in tables
    finally:
        _close_session(session)


def test_invalid_persistence_state_unknown_status_fails_restore() -> None:
    orm = DocumentModel(
        id=UUID("00000000-0000-0000-0000-00000000C007"),
        document_number="DOC-2029-007",
        document_title="Invalid status",
        document_type="MAINTENANCE_REPORT",
        status="UNKNOWN",  # type: ignore[arg-type]
        document_created_at=_aware(2029, 4, 1, 8, 0),
        version=1,
    )

    with pytest.raises((ValueError, TypeError)):
        DocumentMapper.to_domain_document(orm)


def test_timezone_roundtrip_normalizes_document_and_reference_times_to_utc(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "document-timezone")
    try:
        document = _document(
            document_id=UUID("00000000-0000-0000-0000-00000000C008"),
            number="DOC-2029-008",
            with_rows=1,
        )

        restored = _persist_and_reload(session, document)

        assert restored.created_at is not None
        assert restored.created_at.tzinfo is UTC
        assert restored.updated_at is not None
        assert restored.updated_at.tzinfo is UTC
        assert restored.versions[0].created_at.tzinfo is UTC
        assert restored.references[0].checked_at.tzinfo is UTC
    finally:
        _close_session(session)


def test_document_reference_model_creation_directly() -> None:
    model = DocumentReferenceModel(
        id=UUID("00000000-0000-0000-0000-00000000D001"),
        document_id=UUID("00000000-0000-0000-0000-00000000D101"),
        reference_order=0,
        version_number=1,
        storage_key="documents/doc-1/v1.pdf",
        file_name="v1.pdf",
        mime_type="application/pdf",
        checksum="sha256:11",
        size_bytes=512,
        version_created_at=_aware(2029, 4, 1, 8, 0),
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id="00000000-0000-0000-0000-00000000D201",
        exists=True,
        authorized=True,
        is_soft_deleted=False,
        is_archived=False,
        checked_at=_aware(2029, 4, 1, 8, 5),
        description="Direct model creation",
    )

    assert model.version_number == 1
    assert model.storage_key.endswith("v1.pdf")
    assert model.target_capability == "PROJECTS"
