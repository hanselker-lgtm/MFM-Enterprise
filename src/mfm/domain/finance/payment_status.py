"""Payment status enum for finance domain."""

from enum import Enum


class PaymentStatus(str, Enum):
    """Allowed payment lifecycle states."""

    REGISTERED = "REGISTERED"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"
    REFUNDED = "REFUNDED"
