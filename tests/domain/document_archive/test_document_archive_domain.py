from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.domain.document_archive.archive import Archive
from mfm.domain.document_archive.attachment import Attachment
from mfm.domain.document_archive.category import Category
from mfm.domain.document_archive.document import Document
from mfm.domain.document_archive.folder import Folder
from mfm.domain.document_archive.version import Version


def test_document_supports_version_attachment_and_archive() -> None:
    document = Document(
        document_id=uuid4(),
        document_number="DOC-CAP006-001",
        document_title="Membership Policy",
        document_type="POLICY",
        status="ACTIVE",
        folder=Folder(name="Policies", path="/docs/policies"),
        category=Category(code="GOV", name="Governance"),
    )

    document.add_version(
        Version(
            version_number=1,
            storage_key="docs/policies/doc-cap006-001/v1.pdf",
            created_at=datetime(2026, 1, 1, 10, 0, tzinfo=UTC),
        )
    )
    document.add_attachment(
        Attachment(
            target_capability="MEMBERSHIP",
            target_aggregate_type="MEMBERSHIP",
            target_aggregate_id=str(uuid4()),
            description="Membership policy reference",
        )
    )
    document.mark_archived(
        Archive(
            archived_at=datetime(2026, 1, 2, 10, 0, tzinfo=UTC),
            reason="Replaced by newer policy",
        )
    )

    assert len(document.versions) == 1
    assert len(document.attachments) == 1
    assert document.archive is not None
    assert document.status == "ARCHIVED"


def test_document_rejects_duplicate_version() -> None:
    document = Document(
        document_id=uuid4(),
        document_number="DOC-CAP006-002",
        document_title="Charter",
        document_type="CHARTER",
        status="ACTIVE",
        folder=Folder(name="Charters", path="/docs/charters"),
        category=Category(code="ORG", name="Organization"),
    )
    version = Version(
        version_number=1,
        storage_key="docs/charters/doc-cap006-002/v1.pdf",
        created_at=datetime(2026, 1, 1, 10, 0, tzinfo=UTC),
    )
    document.add_version(version)

    with pytest.raises(ValueError, match="already exists"):
        document.add_version(version)
