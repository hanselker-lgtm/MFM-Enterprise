"""Technical component status enum."""

from enum import Enum


class TechnicalComponentStatus(str, Enum):
    """Lifecycle status for technical components."""

    PLANNED = "PLANNED"
    INSTALLED = "INSTALLED"
    REMOVED = "REMOVED"
    RETIRED = "RETIRED"
