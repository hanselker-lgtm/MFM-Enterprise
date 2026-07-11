"""Certificate lifecycle status enum."""

from enum import Enum


class CertificateStatus(str, Enum):
    """Persisted certificate lifecycle states."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    REVOKED = "REVOKED"
    EXPIRED = "EXPIRED"
