"""Currency enum for finance domain."""

from enum import Enum


class Currency(str, Enum):
    """Supported ISO-4217 currencies."""

    DKK = "DKK"
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    NOK = "NOK"
    SEK = "SEK"
