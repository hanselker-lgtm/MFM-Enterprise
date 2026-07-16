"""Posting side enum for journal lines."""

from enum import Enum


class PostingSide(str, Enum):
    """Accounting posting side."""

    DEBIT = "DEBIT"
    CREDIT = "CREDIT"
