"""Identity and reference value objects for procurement domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject
from mfm.domain.procurement.exceptions import InvalidPurchaseOrderReferenceError
from mfm.domain.procurement.exceptions import InvalidSupplierReferenceError


def _normalize_text(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise InvalidPurchaseOrderReferenceError(f"{field_name} must be a string")
    normalized = value.strip()
    if not normalized:
        raise InvalidPurchaseOrderReferenceError(f"{field_name} cannot be empty")
    return normalized


@dataclass(frozen=True, slots=True)
class PurchaseOrderId(ValueObject):
    """Identity for purchase order aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise InvalidPurchaseOrderReferenceError(
                "PurchaseOrderId value must be UUID or UUID string"
            )

    @classmethod
    def new(cls) -> "PurchaseOrderId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class PurchaseOrderLineId(ValueObject):
    """Identity for purchase order line entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise InvalidPurchaseOrderReferenceError(
                "PurchaseOrderLineId value must be UUID or UUID string"
            )

    @classmethod
    def new(cls) -> "PurchaseOrderLineId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class PurchaseReceiptId(ValueObject):
    """Identity for purchase receipt record."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise InvalidPurchaseOrderReferenceError(
                "PurchaseReceiptId value must be UUID or UUID string"
            )

    @classmethod
    def new(cls) -> "PurchaseReceiptId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class PurchaseOrderNumber(ValueObject):
    """Controlled purchase order number/reference."""

    value: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _normalize_text(self.value, "purchase_order_number"))


@dataclass(frozen=True, slots=True)
class SupplierReference(ValueObject):
    """Opaque supplier reference value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidSupplierReferenceError("supplier_reference must be a string")
        normalized = self.value.strip()
        if not normalized:
            raise InvalidSupplierReferenceError("supplier_reference cannot be empty")
        object.__setattr__(self, "value", normalized)
