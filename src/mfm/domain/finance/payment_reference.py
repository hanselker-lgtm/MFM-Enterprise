"""Payment reference value object for finance domain."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.finance.exceptions import InvalidPaymentReferenceError


@dataclass(frozen=True, slots=True)
class PaymentReference(ValueObject):
    """Strongly typed payment reference."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not self.value.strip():
            raise InvalidPaymentReferenceError(
                "payment_reference must be a non-empty string"
            )
        object.__setattr__(self, "value", self.value.strip().upper())

    def __str__(self) -> str:
        return self.value
