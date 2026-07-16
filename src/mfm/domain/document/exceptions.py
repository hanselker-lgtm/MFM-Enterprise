"""Domain exceptions for the Document capability."""


class DocumentError(Exception):
    """Base exception for document domain errors."""


class InvalidDocumentError(DocumentError):
    """Raised when document aggregate state is invalid."""


class InvalidDocumentStateError(DocumentError):
    """Raised when document lifecycle state is invalid."""


class InvalidDocumentNumberError(DocumentError):
    """Raised when document number data is invalid."""


class InvalidDocumentTitleError(DocumentError):
    """Raised when document title data is invalid."""


class InvalidDocumentTypeError(DocumentError):
    """Raised when document type data is invalid."""


class InvalidDocumentVersionError(DocumentError):
    """Raised when document version data is invalid."""


class InvalidDocumentReferenceError(DocumentError):
    """Raised when document reference data is invalid."""
