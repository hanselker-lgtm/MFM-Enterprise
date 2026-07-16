from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.documents.archive_document import ArchiveDocumentUseCase
from mfm.application.documents.attach_reference import AttachReferenceUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.delete_document import DeleteDocumentUseCase
from mfm.application.documents.get_document import GetDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.documents.register_document_version import RegisterDocumentVersionUseCase
from mfm.application.documents.remove_reference import RemoveReferenceUseCase
from mfm.application.documents.search_documents import SearchDocumentsUseCase
from mfm.application.documents.update_document_metadata import UpdateDocumentMetadataUseCase
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentFeature
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentRequest
from mfm.application.features.documents.attach_reference_feature import AttachReferenceFeature
from mfm.application.features.documents.attach_reference_feature import AttachReferenceRequest
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import CreateDocumentFeature
from mfm.application.features.documents.create_document_feature import CreateDocumentRequest
from mfm.application.features.documents.create_document_feature import DocumentReferenceInput
from mfm.application.features.documents.create_document_feature import DocumentVersionInput
from mfm.application.features.documents.delete_document_feature import DeleteDocumentFeature
from mfm.application.features.documents.delete_document_feature import DeleteDocumentRequest
from mfm.application.features.documents.get_document_feature import GetDocumentFeature
from mfm.application.features.documents.get_document_feature import GetDocumentRequest
from mfm.application.features.documents.list_documents_feature import ListDocumentsFeature
from mfm.application.features.documents.list_documents_feature import ListDocumentsRequest
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionFeature,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionRequest,
)
from mfm.application.features.documents.remove_reference_feature import (
    RemoveReferenceFeature,
)
from mfm.application.features.documents.remove_reference_feature import (
    RemoveReferenceRequest,
)
from mfm.application.features.documents.search_documents_feature import (
    SearchDocumentsFeature,
)
from mfm.application.features.documents.search_documents_feature import (
    SearchDocumentsRequest,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataFeature,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataRequest,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteDocumentsApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.document_repository = SQLiteDocumentRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class DocumentsFeatureStack:
    create: CreateDocumentFeature
    get: GetDocumentFeature
    update: UpdateDocumentMetadataFeature
    register_version: RegisterDocumentVersionFeature
    attach_reference: AttachReferenceFeature
    archive: ArchiveDocumentFeature
    list_documents: ListDocumentsFeature
    search_documents: SearchDocumentsFeature
    remove_reference: RemoveReferenceFeature
    delete: DeleteDocumentFeature


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "documents_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_feature_stack(session: Session) -> DocumentsFeatureStack:
    uow = SQLiteDocumentsApplicationUnitOfWork(session)

    return DocumentsFeatureStack(
        create=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        get=GetDocumentFeature(service=GetDocumentUseCase(unit_of_work=uow)),
        update=UpdateDocumentMetadataFeature(
            service=UpdateDocumentMetadataUseCase(unit_of_work=uow)
        ),
        register_version=RegisterDocumentVersionFeature(
            service=RegisterDocumentVersionUseCase(unit_of_work=uow)
        ),
        attach_reference=AttachReferenceFeature(
            service=AttachReferenceUseCase(unit_of_work=uow)
        ),
        archive=ArchiveDocumentFeature(service=ArchiveDocumentUseCase(unit_of_work=uow)),
        list_documents=ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)),
        search_documents=SearchDocumentsFeature(
            service=SearchDocumentsUseCase(unit_of_work=uow)
        ),
        remove_reference=RemoveReferenceFeature(
            service=RemoveReferenceUseCase(unit_of_work=uow)
        ),
        delete=DeleteDocumentFeature(service=DeleteDocumentUseCase(unit_of_work=uow)),
    )


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _version(number: int, *, day: int) -> DocumentVersionInput:
    return DocumentVersionInput(
        version_number=number,
        storage_key=f"documents/e2e/v{number}.pdf",
        file_name=f"v{number}.pdf",
        mime_type="application/pdf",
        checksum=f"sha256:e2e{number}",
        size_bytes=2048 * number,
        created_at=_aware_utc(2033, 1, day, 8),
    )


def _reference(index: int, *, day: int) -> DocumentReferenceInput:
    return DocumentReferenceInput(
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id=f"00000000-0000-0000-0000-00000000E{index:03d}",
        exists=True,
        authorized=True,
        is_soft_deleted=False,
        is_archived=False,
        checked_at=_aware_utc(2033, 1, day, 9),
        description=f"E2E ref {index}",
    )


def test_e2e_workflow_full_document_lifecycle_with_reopen_persistence(sqlite_session_factory) -> None:
    document_id: UUID | None = None

    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)

        created = stack.create.execute(
            CreateDocumentRequest(
                document_number="DOC-E2E-001",
                document_title="Drydock compliance package",
                document_type="COMPLIANCE_REPORT",
                status="DRAFT",
                description="Primary lifecycle test",
                created_at=_aware_utc(2033, 1, 1, 8),
                versions=(_version(1, day=1),),
                references=(_reference(1, day=1),),
            )
        )
        document_id = created.document.document_id

        loaded = stack.get.execute(GetDocumentRequest(document_id=document_id))
        assert loaded.document.document_number == "DOC-E2E-001"
        assert loaded.document.status == "DRAFT"
        assert len(loaded.document.versions) == 1

        updated = stack.update.execute(
            UpdateDocumentMetadataRequest(
                document_id=document_id,
                document_title="Drydock compliance package rev A",
                description="Scope refined",
                updated_at=_aware_utc(2033, 1, 2, 8),
            )
        )
        assert updated.document.document_title.endswith("rev A")

        versioned = stack.register_version.execute(
            RegisterDocumentVersionRequest(
                document_id=document_id,
                version=_version(2, day=2),
                registered_at=_aware_utc(2033, 1, 2, 9),
            )
        )
        assert len(versioned.document.versions) == 2

        attached = stack.attach_reference.execute(
            AttachReferenceRequest(
                document_id=document_id,
                reference=_reference(2, day=3),
                attached_at=_aware_utc(2033, 1, 3, 8),
            )
        )
        assert len(attached.document.references) == 2

        archived = stack.archive.execute(
            ArchiveDocumentRequest(document_id=document_id, archived_at=_aware_utc(2033, 1, 4, 8))
        )
        assert archived.document.status == "ARCHIVED"

        listed = stack.list_documents.execute(ListDocumentsRequest(status="ARCHIVED"))
        assert [item.document_number for item in listed.documents] == ["DOC-E2E-001"]

        searched = stack.search_documents.execute(
            SearchDocumentsRequest(text="compliance", target_capability="PROJECTS")
        )
        assert [item.document_number for item in searched.documents] == ["DOC-E2E-001"]

        removed = stack.remove_reference.execute(
            RemoveReferenceRequest(
                document_id=document_id,
                reference_id=attached.document.references[0].reference_id,
                removed_at=_aware_utc(2033, 1, 5, 8),
            )
        )
        assert len(removed.document.references) == 1

        deleted = stack.delete.execute(DeleteDocumentRequest(document_id=document_id))
        assert deleted.document_id == document_id
    finally:
        write_session.close()

    assert document_id is not None

    read_session = sqlite_session_factory()
    try:
        reopened = _build_feature_stack(read_session)
        with pytest.raises(BusinessRuleViolation):
            reopened.get.execute(GetDocumentRequest(document_id=document_id))
    finally:
        read_session.close()
