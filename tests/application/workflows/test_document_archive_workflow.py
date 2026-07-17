from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.application.document_archive.document_archive_service import DocumentArchiveResponse
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveRequest,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveResponse,
)
from mfm.application.workflows.document_archive_workflow import DocumentArchiveWorkflow
from mfm.application.workflows.document_archive_workflow import DocumentArchiveWorkflowInput


class StubFeature:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _request() -> ManageDocumentArchiveRequest:
    return ManageDocumentArchiveRequest(
        operation="create-document",
        document_number="DOC-CAP006-300",
        document_title="Archive Workflow",
        document_type="PLAN",
        folder_name="Plans",
        folder_path="/docs/plans",
        category_code="PRJ",
        category_name="Projects",
        initial_storage_key="docs/plans/doc-cap006-300/v1.pdf",
        timestamp=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
    )


def test_workflow_returns_success() -> None:
    response = ManageDocumentArchiveResponse(
        result=DocumentArchiveResponse(
            document_id=uuid4(),
            document_number="DOC-CAP006-300",
            document_title="Archive Workflow",
            status="ACTIVE",
            category_code="PRJ",
            folder_path="/docs/plans",
            versions_count=1,
            attachments_count=0,
            archived=False,
            generated_at=datetime(2026, 1, 1, tzinfo=UTC),
        )
    )
    workflow = DocumentArchiveWorkflow(feature=StubFeature(response=response))

    result = workflow.execute(DocumentArchiveWorkflowInput(request=_request()))

    assert result.success is True
    assert result.response == response


def test_workflow_returns_failure() -> None:
    workflow = DocumentArchiveWorkflow(feature=StubFeature(error=RuntimeError("failed")))

    result = workflow.execute(DocumentArchiveWorkflowInput(request=_request()))

    assert result.success is False
    assert result.response is None
    assert "failed" in result.message
