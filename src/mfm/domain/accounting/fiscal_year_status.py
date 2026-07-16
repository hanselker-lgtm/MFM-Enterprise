"""Fiscal year status enum for accounting domain."""

from enum import Enum


class FiscalYearStatus(str, Enum):
    """Lifecycle states for a fiscal year."""

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"
