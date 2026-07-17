from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.document_archive.document_archive_service import DocumentArchiveResponse
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveFeature,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveRequest,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    RepositoryException,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ValidationException,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def create_document(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def add_version(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def attach(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def archive(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _response() -> DocumentArchiveResponse:
    return DocumentArchiveResponse(
        document_id=uuid4(),
        document_number="DOC-CAP006-200",
        document_title="Archive Spec",
        status="ACTIVE",
        category_code="DOC",
        folder_path="/docs/specs",
        versions_count=1,
        attachments_count=0,
        archived=False,
        generated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )


def _dt(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, 0, tzinfo=UTC)


def test_feature_routes_create_document() -> None:
    feature = ManageDocumentArchiveFeature(service=StubService(response=_response()))

    result = feature.execute(
        ManageDocumentArchiveRequest(
            operation="create-document",
            document_number="DOC-CAP006-200",
            document_title="Archive Spec",
            document_type="SPEC",
            folder_name="Specs",
            folder_path="/docs/specs",
            category_code="DOC",
            category_name="Documents",
            initial_storage_key="docs/specs/doc-cap006-200/v1.pdf",
            timestamp=_dt(9),
        )
    )

    assert result.result.document_number == "DOC-CAP006-200"


def test_feature_validates_request() -> None:
    feature = ManageDocumentArchiveFeature(service=StubService(response=_response()))

    with pytest.raises(ValidationException):
        feature.execute(
            ManageDocumentArchiveRequest(
                operation="add-version",
                document_id=uuid4(),
                version_number=0,
                storage_key="docs/specs/v2.pdf",
            )
        )


def test_feature_maps_unknown_error() -> None:
    feature = ManageDocumentArchiveFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(
            ManageDocumentArchiveRequest(
                operation="archive",
                document_id=uuid4(),
                reason="cleanup",
                timestamp=_dt(10),
            )
        )
