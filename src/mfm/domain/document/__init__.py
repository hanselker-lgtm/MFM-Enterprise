"""Document domain package."""

from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.document_status import DocumentStatus
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.domain.document.events import DocumentArchived
from mfm.domain.document.events import DocumentCreated
from mfm.domain.document.events import DocumentDisposed
from mfm.domain.document.events import DocumentReferenceAdded
from mfm.domain.document.events import DocumentStatusChanged
from mfm.domain.document.events import DocumentUpdated
from mfm.domain.document.events import DocumentVersionAdded
from mfm.domain.document.exceptions import DocumentError
from mfm.domain.document.exceptions import InvalidDocumentError
from mfm.domain.document.exceptions import InvalidDocumentNumberError
from mfm.domain.document.exceptions import InvalidDocumentReferenceError
from mfm.domain.document.exceptions import InvalidDocumentStateError
from mfm.domain.document.exceptions import InvalidDocumentTitleError
from mfm.domain.document.exceptions import InvalidDocumentTypeError
from mfm.domain.document.exceptions import InvalidDocumentVersionError

__all__ = [
    "Document",
    "DocumentArchived",
    "DocumentCreated",
    "DocumentDisposed",
    "DocumentError",
    "DocumentId",
    "DocumentNumber",
    "DocumentReference",
    "DocumentReferenceAdded",
    "DocumentRepository",
    "DocumentStatus",
    "DocumentStatusChanged",
    "DocumentTitle",
    "DocumentType",
    "DocumentUpdated",
    "DocumentVersion",
    "DocumentVersionAdded",
    "InvalidDocumentError",
    "InvalidDocumentNumberError",
    "InvalidDocumentReferenceError",
    "InvalidDocumentStateError",
    "InvalidDocumentTitleError",
    "InvalidDocumentTypeError",
    "InvalidDocumentVersionError",
]
