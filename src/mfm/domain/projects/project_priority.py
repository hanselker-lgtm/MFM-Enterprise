"""Priority levels for projects."""

from __future__ import annotations

from enum import StrEnum


class ProjectPriority(StrEnum):
    """Priority classification for a project."""

    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    URGENT = "URGENT"