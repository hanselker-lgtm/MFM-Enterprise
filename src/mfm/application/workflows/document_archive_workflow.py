"""Workflow for CAP-006 document archive capability."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveFeature,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveRequest,
)
from mfm.application.features.document_archive.manage_document_archive_feature import (
    ManageDocumentArchiveResponse,
)


@dataclass(frozen=True, slots=True)
class DocumentArchiveWorkflowInput:
    request: ManageDocumentArchiveRequest


@dataclass(frozen=True, slots=True)
class DocumentArchiveWorkflowResult:
    success: bool
    response: ManageDocumentArchiveResponse | None = None
    message: str = ""


class DocumentArchiveWorkflow:
    """Workflow wrapper around document archive feature API."""

    def __init__(self, *, feature: ManageDocumentArchiveFeature) -> None:
        self._feature = feature

    def execute(self, data: DocumentArchiveWorkflowInput) -> DocumentArchiveWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return DocumentArchiveWorkflowResult(
                success=True,
                response=response,
                message="Document archive operation completed",
            )
        except Exception as exc:
            return DocumentArchiveWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
