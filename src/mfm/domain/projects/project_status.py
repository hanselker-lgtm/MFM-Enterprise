"""Lifecycle states for projects."""

from __future__ import annotations

from enum import StrEnum


class ProjectStatus(StrEnum):
    """Lifecycle state for a project."""

    DRAFT = "DRAFT"
    PLANNED = "PLANNED"
    ACTIVE = "ACTIVE"
    ON_HOLD = "ON_HOLD"
    COMPLETED = "COMPLETED"
    ARCHIVED = "ARCHIVED"