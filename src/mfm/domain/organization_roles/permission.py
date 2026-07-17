"""Permission enum for organization roles capability."""

from __future__ import annotations

from enum import Enum


class Permission(str, Enum):
    """Permission scope granted to a role."""

    MANAGE_BOARD = "MANAGE_BOARD"
    MANAGE_COMMITTEES = "MANAGE_COMMITTEES"
    MANAGE_ELECTIONS = "MANAGE_ELECTIONS"
    ASSIGN_ROLES = "ASSIGN_ROLES"
    VIEW_REPORTS = "VIEW_REPORTS"
