"""Payment method enum for finance domain."""

from enum import Enum


class PaymentMethod(str, Enum):
    """Supported payment methods."""

    CASH = "CASH"
    BANK_TRANSFER = "BANK_TRANSFER"
    CREDIT_CARD = "CREDIT_CARD"
    MOBILEPAY = "MOBILEPAY"
    PAYPAL = "PAYPAL"
    OTHER = "OTHER"
