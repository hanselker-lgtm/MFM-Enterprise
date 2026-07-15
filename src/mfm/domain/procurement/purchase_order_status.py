"""Purchase order lifecycle states."""

from enum import Enum


class PurchaseOrderStatus(str, Enum):
    """Supported purchase order lifecycle states."""

    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    ORDERED = "ORDERED"
    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"
