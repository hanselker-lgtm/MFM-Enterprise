"""Currency enum for contingent plans."""

from enum import Enum


class Currency(str, Enum):
    """Supported currencies for contingent amounts."""

    DKK = "DKK"
    EUR = "EUR"
    USD = "USD"
