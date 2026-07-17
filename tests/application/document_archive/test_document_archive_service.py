from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.document_archive.document_archive_service import AddArchiveVersionRequest
from mfm.application.document_archive.document_archive_service import ArchiveDocumentRecordRequest
from mfm.application.document_archive.document_archive_service import AttachArchiveRequest
from mfm.application.document_archive.document_archive_service import BusinessRuleViolation
from mfm.application.document_archive.document_archive_service import CreateArchiveDocumentRequest
from mfm.application.document_archive.document_archive_service import DocumentArchiveService
from mfm.domain.document_archive.document import Document


class InMemoryRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, Document] = {}

    def get(self, document_id: UUID) -> Document | None:
        return self.store.get(document_id)

    def save(self, document: Document) -> None:
        self.store[document.document_id] = document


class StubCreateDocumentFeature:
    def execute(self, request):
        now = request.created_at
        doc_id = uuid4()
        return type(
            "CreateDocumentResponseObj",
            (),
            {
                "document": type(
                    "DocumentResponseObj",
                    (),
                    {
                        "document_id": doc_id,
                        "document_number": request.document_number,
                        "document_title": request.document_title,
                        "document_type": request.document_type,
                        "status": request.status,
                        "created_at": now,
                    },
                )()
            },
        )()


class StubRegisterDocumentVersionFeature:
    def execute(self, request):
        _ = request
        return None


class StubAttachReferenceFeature:
    def execute(self, request):
        _ = request
        return None


class StubArchiveDocumentFeature:
    def execute(self, request):
        _ = request
        return None


def _service() -> DocumentArchiveService:
    return DocumentArchiveService(
        repository=InMemoryRepository(),
        create_document_feature=StubCreateDocumentFeature(),
        register_document_version_feature=StubRegisterDocumentVersionFeature(),
        attach_reference_feature=StubAttachReferenceFeature(),
        archive_document_feature=StubArchiveDocumentFeature(),
    )


def _dt(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, 0, tzinfo=UTC)


def test_service_create_add_attach_archive() -> None:
    service = _service()

    created = service.create_document(
        CreateArchiveDocumentRequest(
            document_number="DOC-CAP006-100",
            document_title="Program Plan",
            document_type="PLAN",
            folder_name="Plans",
            folder_path="/docs/plans",
            category_code="PRJ",
            category_name="Projects",
            initial_storage_key="docs/plans/doc-cap006-100/v1.pdf",
            created_at=_dt(9),
        )
    )

    updated = service.add_version(
        AddArchiveVersionRequest(
            document_id=created.document_id,
            version_number=2,
            storage_key="docs/plans/doc-cap006-100/v2.pdf",
            created_at=_dt(10),
        )
    )

    attached = service.attach(
        AttachArchiveRequest(
            document_id=created.document_id,
            target_capability="PROJECTS",
            target_aggregate_type="PROJECT",
            target_aggregate_id=str(uuid4()),
            description="Project charter",
            checked_at=_dt(11),
        )
    )

    archived = service.archive(
        ArchiveDocumentRecordRequest(
            document_id=created.document_id,
            reason="Superseded",
            archived_at=_dt(12),
        )
    )

    assert created.versions_count == 1
    assert updated.versions_count == 2
    assert attached.attachments_count == 1
    assert archived.archived is True


def test_service_rejects_unknown_document_on_add_version() -> None:
    service = _service()

    with pytest.raises(BusinessRuleViolation, match="not found"):
        service.add_version(
            AddArchiveVersionRequest(
                document_id=uuid4(),
                version_number=2,
                storage_key="docs/x/v2.pdf",
                created_at=_dt(10),
            )
        )
