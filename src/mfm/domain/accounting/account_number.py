"""Account number value object for ledger accounts."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidLedgerAccountReferenceError


@dataclass(frozen=True, slots=True)
class AccountNumber(ValueObject):
    """Immutable account number value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not self.value.strip():
            raise InvalidLedgerAccountReferenceError(
                "account_number must be a non-empty string"
            )

        normalized = self.value.strip().upper()
        if any(char.isspace() for char in normalized):
            raise InvalidLedgerAccountReferenceError(
                "account_number must not contain spaces"
            )

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
