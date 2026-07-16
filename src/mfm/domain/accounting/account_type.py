"""Account type enum for ledger accounts."""

from enum import Enum


class AccountType(str, Enum):
    """Classification of a ledger account."""

    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
