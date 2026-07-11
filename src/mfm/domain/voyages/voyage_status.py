"""Lifecycle states for voyages."""

from __future__ import annotations

from enum import StrEnum


class VoyageStatus(StrEnum):
    """Lifecycle state for a voyage."""

    DRAFT = "DRAFT"
    PLANNED = "PLANNED"
    UNDERWAY = "UNDERWAY"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"