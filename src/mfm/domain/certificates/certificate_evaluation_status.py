"""Derived certificate evaluation status enum."""

from enum import Enum


class CertificateEvaluationStatus(str, Enum):
    """Result states from explicit certificate status evaluation."""

    DRAFT = "DRAFT"
    VALID = "VALID"
    EXPIRING = "EXPIRING"
    EXPIRED = "EXPIRED"
    SUSPENDED = "SUSPENDED"
    REVOKED = "REVOKED"
