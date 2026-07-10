"""Vessel status enum."""

from enum import Enum


class VesselStatus(str, Enum):
    """Lifecycle status for a vessel."""

    ACTIVE = "ACTIVE"
    LAID_UP = "LAID_UP"
    RESTORATION = "RESTORATION"
    RETIRED = "RETIRED"
