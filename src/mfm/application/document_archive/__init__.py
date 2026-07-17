"""Application service exports for CAP-006 document archive capability."""

from mfm.application.document_archive.document_archive_service import AddArchiveVersionRequest
from mfm.application.document_archive.document_archive_service import ArchiveDocumentRecordRequest
from mfm.application.document_archive.document_archive_service import AttachArchiveRequest
from mfm.application.document_archive.document_archive_service import CreateArchiveDocumentRequest
from mfm.application.document_archive.document_archive_service import DocumentArchiveResponse
from mfm.application.document_archive.document_archive_service import DocumentArchiveService

__all__ = [
    "AddArchiveVersionRequest",
    "ArchiveDocumentRecordRequest",
    "AttachArchiveRequest",
    "CreateArchiveDocumentRequest",
    "DocumentArchiveResponse",
    "DocumentArchiveService",
]
