"""Account category enum for chart of accounts."""

from enum import Enum


class AccountCategory(str, Enum):
    """Top-level account categories."""

    ASSETS = "ASSETS"
    LIABILITIES = "LIABILITIES"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSES = "EXPENSES"
