"""Certificate target type enum."""

from enum import Enum


class CertificateTargetType(str, Enum):
    """Supported certificate target types in v1."""

    VESSEL = "VESSEL"
    ORGANIZATION = "ORGANIZATION"
