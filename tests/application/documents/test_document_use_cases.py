from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from pathlib import Path
from typing import Any
from uuid import UUID

import pytest

from mfm.application.documents.archive_document import ArchiveDocumentRequest
from mfm.application.documents.archive_document import ArchiveDocumentUseCase
from mfm.application.documents.attach_reference import AttachReferenceRequest
from mfm.application.documents.attach_reference import AttachReferenceUseCase
from mfm.application.documents.create_document import BusinessRuleViolation
from mfm.application.documents.create_document import CreateDocumentRequest
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.create_document import DocumentReferenceInput
from mfm.application.documents.create_document import DocumentVersionInput
from mfm.application.documents.create_document import RepositoryException
from mfm.application.documents.delete_document import DeleteDocumentRequest
from mfm.application.documents.delete_document import DeleteDocumentUseCase
from mfm.application.documents.get_document import GetDocumentRequest
from mfm.application.documents.get_document import GetDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsRequest
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.documents.register_document_version import (
    RegisterDocumentVersionRequest,
)
from mfm.application.documents.register_document_version import RegisterDocumentVersionUseCase
from mfm.application.documents.remove_reference import RemoveReferenceRequest
from mfm.application.documents.remove_reference import RemoveReferenceUseCase
from mfm.application.documents.search_documents import SearchDocumentsRequest
from mfm.application.documents.search_documents import SearchDocumentsUseCase
from mfm.application.documents.update_document_metadata import (
    UpdateDocumentMetadataRequest,
)
from mfm.application.documents.update_document_metadata import (
    UpdateDocumentMetadataUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.document_status import DocumentStatus


class InMemoryDocumentRepository(DocumentRepository):
    def __init__(self, *, fail_on_add: bool = False, fail_on_update: bool = False) -> None:
        self._documents: dict[UUID, Document] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def snapshot(self) -> dict[UUID, Document]:
        return deepcopy(self._documents)

    def restore(self, snapshot: dict[UUID, Document]) -> None:
        self._documents = deepcopy(snapshot)

    def add(self, document: Document) -> None:
        if self._fail_on_add:
            raise RuntimeError("document add failed")
        if self.get_by_number(document.document_number) is not None:
            raise ValueError(f"Document number {document.document_number.value} already exists")
        self._documents[document.id.value] = deepcopy(document)

    def update(self, document: Document) -> None:
        if self._fail_on_update:
            raise RuntimeError("document update failed")
        if document.id.value not in self._documents:
            raise ValueError(f"Document {document.id.value} does not exist")
        duplicate = next(
            (
                existing
                for existing in self._documents.values()
                if existing.document_number == document.document_number
                and existing.id != document.id
            ),
            None,
        )
        if duplicate is not None:
            raise ValueError(f"Document number {document.document_number.value} already exists")

        document.version += 1
        self._documents[document.id.value] = deepcopy(document)

    def remove(self, document_id: DocumentId) -> None:
        normalized = document_id if isinstance(document_id, DocumentId) else DocumentId(document_id)
        if normalized.value not in self._documents:
            raise ValueError(f"Document {normalized.value} does not exist")
        del self._documents[normalized.value]

    def get(self, document_id: DocumentId) -> Document | None:
        normalized = document_id if isinstance(document_id, DocumentId) else DocumentId(document_id)
        value = self._documents.get(normalized.value)
        return deepcopy(value) if value is not None else None

    def exists(self, document_id: DocumentId) -> bool:
        normalized = document_id if isinstance(document_id, DocumentId) else DocumentId(document_id)
        return normalized.value in self._documents

    def get_by_number(self, document_number: DocumentNumber) -> Document | None:
        normalized = (
            document_number if isinstance(document_number, DocumentNumber) else DocumentNumber(document_number)
        )
        for value in self._documents.values():
            if value.document_number == normalized:
                return deepcopy(value)
        return None

    def list(self, filters: Any | None = None) -> list[Document]:
        values = sorted(
            self._documents.values(),
            key=lambda item: (item.document_number.value, str(item.id.value)),
        )
        if isinstance(filters, dict) and filters.get("status") is not None:
            status = filters["status"]
            normalized = (
                status if isinstance(status, DocumentStatus) else DocumentStatus(str(status).upper())
            )
            values = [value for value in values if value.status is normalized]
        return [deepcopy(value) for value in values]

    def search(self, criteria: Any) -> list[Any]:
        if isinstance(criteria, str):
            filters = {"text": criteria}
        elif isinstance(criteria, dict):
            filters = dict(criteria)
        else:
            filters = {}

        text = str(filters.get("text", "")).strip().casefold()
        status = filters.get("status")
        if status is not None:
            status = status if isinstance(status, DocumentStatus) else DocumentStatus(str(status).upper())
        target_capability = filters.get("target_capability")
        if target_capability is not None:
            target_capability = str(target_capability).strip().upper()

        rows: list[dict[str, Any]] = []
        for document in self.list():
            haystack = (
                f"{document.document_number.value} {document.document_title.value} "
                f"{document.document_type.value} {document.description or ''}"
            ).casefold()
            if text and text not in haystack:
                continue
            if status is not None and document.status is not status:
                continue
            if target_capability is not None and all(
                ref.target_capability != target_capability for ref in document.references
            ):
                continue
            rows.append(
                {
                    "id": document.id.value,
                    "document_number": document.document_number.value,
                    "document_title": document.document_title.value,
                    "document_type": document.document_type.value,
                    "status": document.status,
                }
            )

        return rows

    def next_identity(self) -> DocumentId:
        return DocumentId.new()

    def list_by_status(self, status: DocumentStatus) -> list[Document]:
        normalized = status if isinstance(status, DocumentStatus) else DocumentStatus(str(status).upper())
        return [value for value in self.list() if value.status is normalized]


class FakeDocumentsUnitOfWork(AbstractUnitOfWork):
    def __init__(self, *, fail_add: bool = False, fail_update: bool = False, fail_commit: bool = False) -> None:
        super().__init__()
        self._fail_commit = fail_commit
        self._repository = InMemoryDocumentRepository(
            fail_on_add=fail_add,
            fail_on_update=fail_update,
        )
        self._snapshot: dict[UUID, Document] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.document_repository = self._repository
        self._snapshot = self._repository.snapshot()

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _version(number: int) -> DocumentVersionInput:
    return DocumentVersionInput(
        version_number=number,
        storage_key=f"documents/doc-app/v{number}.pdf",
        file_name=f"v{number}.pdf",
        mime_type="application/pdf",
        checksum=f"sha256:{number:02d}",
        size_bytes=1024 * number,
        created_at=_aware(2032, 1, number, 8),
    )


def _reference(index: int) -> DocumentReferenceInput:
    return DocumentReferenceInput(
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id=f"00000000-0000-0000-0000-00000000A{index:03d}",
        exists=True,
        authorized=True,
        is_soft_deleted=False,
        is_archived=False,
        checked_at=_aware(2032, 1, index, 9),
        description=f"Reference {index}",
    )


def _create_document(
    uow: FakeDocumentsUnitOfWork,
    *,
    number: str = "DOC-APP-001",
    status: str = "DRAFT",
) -> UUID:
    response = CreateDocumentUseCase(unit_of_work=uow).execute(
        CreateDocumentRequest(
            document_number=number,
            document_title="Inspection package",
            document_type="MAINTENANCE_REPORT",
            status=status,
            description="Initial scope",
            created_at=_aware(2032, 1, 1, 8),
            versions=(_version(1),),
            references=(_reference(1),),
        )
    )
    return response.document.document_id


def test_create_document_success_and_duplicate_number() -> None:
    uow = FakeDocumentsUnitOfWork()
    use_case = CreateDocumentUseCase(unit_of_work=uow)

    created = use_case.execute(
        CreateDocumentRequest(
            document_number="DOC-APP-100",
            document_title="Drydock dossier",
            document_type="PROJECT_EVIDENCE",
            versions=(_version(1),),
            references=(_reference(1),),
        )
    )

    assert uow.commits == 1
    assert created.document.document_number == "DOC-APP-100"
    assert created.document.document_type == "PROJECT_EVIDENCE"
    assert len(created.document.versions) == 1

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateDocumentRequest(
                document_number="DOC-APP-100",
                document_title="Duplicate",
                document_type="PROJECT_EVIDENCE",
            )
        )

    assert uow.commits == 1


def test_get_document_existing_and_missing_no_commit() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-APP-GET")
    before = uow.commits

    response = GetDocumentUseCase(unit_of_work=uow).execute(
        GetDocumentRequest(document_id=document_id)
    )

    assert response.document.document_id == document_id
    assert uow.commits == before

    with pytest.raises(BusinessRuleViolation):
        GetDocumentUseCase(unit_of_work=uow).execute(
            GetDocumentRequest(document_id=UUID("00000000-0000-0000-0000-00000000B801"))
        )

    assert uow.commits == before


def test_update_register_and_attach_reference() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-APP-UPD")

    updated = UpdateDocumentMetadataUseCase(unit_of_work=uow).execute(
        UpdateDocumentMetadataRequest(
            document_id=document_id,
            document_title="Inspection package updated",
            description="Updated scope",
            updated_at=_aware(2032, 1, 2, 8),
        )
    )
    assert updated.document.document_title == "Inspection package updated"

    versioned = RegisterDocumentVersionUseCase(unit_of_work=uow).execute(
        RegisterDocumentVersionRequest(
            document_id=document_id,
            version=_version(2),
            registered_at=_aware(2032, 1, 3, 8),
        )
    )
    assert len(versioned.document.versions) == 2

    attached = AttachReferenceUseCase(unit_of_work=uow).execute(
        AttachReferenceRequest(
            document_id=document_id,
            reference=_reference(2),
            attached_at=_aware(2032, 1, 4, 8),
        )
    )
    assert len(attached.document.references) == 2
    assert uow.commits == 4


def test_archive_remove_reference_and_delete_document() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-APP-LIFE", status="ACTIVE")

    archived = ArchiveDocumentUseCase(unit_of_work=uow).execute(
        ArchiveDocumentRequest(document_id=document_id, archived_at=_aware(2032, 1, 5, 8))
    )
    assert archived.document.status == "ARCHIVED"

    reference_id = archived.document.references[0].reference_id
    removed = RemoveReferenceUseCase(unit_of_work=uow).execute(
        RemoveReferenceRequest(document_id=document_id, reference_id=reference_id)
    )
    assert len(removed.document.references) == 0

    deleted = DeleteDocumentUseCase(unit_of_work=uow).execute(
        DeleteDocumentRequest(document_id=document_id)
    )
    assert deleted.document_id == document_id

    with pytest.raises(BusinessRuleViolation):
        GetDocumentUseCase(unit_of_work=uow).execute(GetDocumentRequest(document_id=document_id))


def test_list_and_search_documents_delegate_and_preserve_order() -> None:
    uow = FakeDocumentsUnitOfWork()
    _create_document(uow, number="DOC-APP-A")
    _create_document(uow, number="DOC-APP-B")
    doc_c = _create_document(uow, number="DOC-APP-C", status="ACTIVE")

    ArchiveDocumentUseCase(unit_of_work=uow).execute(
        ArchiveDocumentRequest(document_id=doc_c, archived_at=_aware(2032, 1, 8, 8))
    )

    listed = ListDocumentsUseCase(unit_of_work=uow).execute(ListDocumentsRequest())
    archived = ListDocumentsUseCase(unit_of_work=uow).execute(
        ListDocumentsRequest(status="ARCHIVED")
    )
    searched = SearchDocumentsUseCase(unit_of_work=uow).execute(
        SearchDocumentsRequest(text="APP-B")
    )

    assert [item.document_number for item in listed.documents] == [
        "DOC-APP-A",
        "DOC-APP-B",
        "DOC-APP-C",
    ]
    assert [item.document_number for item in archived.documents] == ["DOC-APP-C"]
    assert [item.document_number for item in searched.documents] == ["DOC-APP-B"]


def test_application_wraps_repository_failures_and_rolls_back() -> None:
    uow = FakeDocumentsUnitOfWork(fail_add=True)

    with pytest.raises(RepositoryException):
        CreateDocumentUseCase(unit_of_work=uow).execute(
            CreateDocumentRequest(
                document_number="DOC-APP-ERR",
                document_title="Failure",
                document_type="PROJECT_EVIDENCE",
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_document_application_has_no_sqlalchemy_or_infrastructure_imports() -> None:
    documents_dir = Path("src/mfm/application/documents")
    forbidden_markers = (
        "sqlalchemy",
        "mfm.infrastructure.persistence",
        "mfm.database.models",
    )

    python_files = sorted(documents_dir.glob("*.py"))
    assert python_files, "expected document application python files"

    for file_path in python_files:
        content = file_path.read_text(encoding="utf-8").lower()
        for marker in forbidden_markers:
            assert marker not in content, f"forbidden marker '{marker}' found in {file_path}"


def test_document_response_dtos_are_immutable_dataclasses() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-APP-DTO")

    response = GetDocumentUseCase(unit_of_work=uow).execute(
        GetDocumentRequest(document_id=document_id)
    )

    assert is_dataclass(response.document)
    assert isinstance(response.document.versions, tuple)
    assert isinstance(response.document.references, tuple)
