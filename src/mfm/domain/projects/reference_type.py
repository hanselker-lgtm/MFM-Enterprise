"""Reference type enum for projects external references."""

from __future__ import annotations

from enum import StrEnum


class ReferenceType(StrEnum):
    """Supported cross-capability identifier reference types."""

    ASSET = "ASSET"
    ORGANISATION = "ORGANISATION"
    CONTACT = "CONTACT"
    PURCHASE_ORDER = "PURCHASE_ORDER"
    INVENTORY_ITEM = "INVENTORY_ITEM"
    MAINTENANCE_WORK_ORDER = "MAINTENANCE_WORK_ORDER"
    DOCUMENT = "DOCUMENT"
    CERTIFICATE = "CERTIFICATE"
