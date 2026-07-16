"""Account group enum for chart of accounts."""

from enum import Enum


class AccountGroup(str, Enum):
    """Detailed account group classifications."""

    ASSETS = "ASSETS"
    CURRENT_ASSETS = "CURRENT_ASSETS"
    FIXED_ASSETS = "FIXED_ASSETS"
    LIABILITIES = "LIABILITIES"
    SHORT_TERM_LIABILITIES = "SHORT_TERM_LIABILITIES"
    LONG_TERM_LIABILITIES = "LONG_TERM_LIABILITIES"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSES = "EXPENSES"
