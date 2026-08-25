"""Invoice status enum for finance domain."""

from enum import Enum


class InvoiceStatus(str, Enum):
    """Allowed invoice lifecycle statuses."""

    DRAFT = "DRAFT"
    ISSUED = "ISSUED"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
    CREDITED = "CREDITED"
