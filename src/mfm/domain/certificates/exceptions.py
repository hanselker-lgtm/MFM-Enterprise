"""Domain exceptions for Certificates and Compliance capability."""


class CertificateError(Exception):
    """Base exception for certificates domain errors."""


class InvalidCertificateTargetError(CertificateError):
    """Raised when certificate target data is invalid."""


class InvalidCertificateTypeError(CertificateError):
    """Raised when certificate type data is invalid."""


class InvalidIssuerReferenceError(CertificateError):
    """Raised when issuer reference data is invalid."""


class InvalidCertificateStateError(CertificateError):
    """Raised when certificate aggregate invariants are violated."""


class InvalidCertificateLifecycleError(CertificateError):
    """Raised when certificate lifecycle transition is invalid."""


class InvalidCertificateChronologyError(CertificateError):
    """Raised when certificate chronology is invalid."""


class InvalidComplianceObservationError(CertificateError):
    """Raised when compliance observation data is invalid."""
