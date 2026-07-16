"""Normal balance enum for ledger accounts."""

from enum import Enum


class NormalBalance(str, Enum):
    """Normal balance side for a ledger account."""

    DEBIT = "DEBIT"
    CREDIT = "CREDIT"
