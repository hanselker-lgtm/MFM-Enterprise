"""Technical configuration status enum."""

from enum import Enum


class TechnicalConfigurationStatus(str, Enum):
    """Lifecycle status for technical configuration aggregate."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
