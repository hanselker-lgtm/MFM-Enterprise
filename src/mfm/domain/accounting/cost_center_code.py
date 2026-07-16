"""Cost center code value object for accounting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidJournalReferenceError


@dataclass(frozen=True, slots=True)
class CostCenterCode(ValueObject):
    """Immutable cost center code."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not self.value.strip():
            raise InvalidJournalReferenceError("cost_center_code must be a non-empty string")

        normalized = self.value.strip().upper()
        if any(char.isspace() for char in normalized):
            raise InvalidJournalReferenceError("cost_center_code must not contain spaces")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
