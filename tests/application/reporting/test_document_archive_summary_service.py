from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryRequest,
)
from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryService,
)
from mfm.domain.document_archive.attachment import Attachment
from mfm.domain.document_archive.category import Category
from mfm.domain.document_archive.document import Document
from mfm.domain.document_archive.folder import Folder
from mfm.domain.document_archive.version import Version


class InMemoryRepository:
    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents

    def list(self) -> list[Document]:
        return self.documents


def test_summary_service_returns_metrics_and_integration_counts() -> None:
    document = Document(
        document_id=uuid4(),
        document_number="DOC-CAP006-400",
        document_title="Integration Spec",
        document_type="SPEC",
        status="ACTIVE",
        folder=Folder(name="Specs", path="/docs/specs"),
        category=Category(code="DOC", name="Documents"),
        versions=[
            Version(
                version_number=1,
                storage_key="docs/specs/doc-cap006-400/v1.pdf",
                created_at=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
            )
        ],
        attachments=[
            Attachment(
                target_capability="PROJECTS",
                target_aggregate_type="PROJECT",
                target_aggregate_id=str(uuid4()),
            ),
            Attachment(
                target_capability="MEMBERSHIP",
                target_aggregate_type="MEMBERSHIP",
                target_aggregate_id=str(uuid4()),
            ),
        ],
    )

    service = DocumentArchiveSummaryService(repository=InMemoryRepository([document]))
    response = service.execute(DocumentArchiveSummaryRequest())

    assert len(response.documents) == 1
    assert response.documents[0].category_code == "DOC"
    assert response.integration.projects_links == 1
    assert response.integration.membership_links == 1
