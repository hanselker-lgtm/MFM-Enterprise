"""Issuer reference type enum."""

from enum import Enum


class IssuerReferenceType(str, Enum):
    """Supported issuer classifications."""

    AUTHORITY = "AUTHORITY"
    CLASSIFICATION_SOCIETY = "CLASSIFICATION_SOCIETY"
    INSPECTION_BODY = "INSPECTION_BODY"
    OTHER_ORGANIZATION = "OTHER_ORGANIZATION"
