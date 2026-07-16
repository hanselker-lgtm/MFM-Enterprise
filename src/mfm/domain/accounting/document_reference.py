"""Document reference value object for accounting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidJournalReferenceError


@dataclass(frozen=True, slots=True)
class DocumentReference(ValueObject):
    """Immutable document reference token."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not self.value.strip():
            raise InvalidJournalReferenceError("document_reference must be a non-empty string")

        normalized = self.value.strip().upper()
        if any(char.isspace() for char in normalized):
            raise InvalidJournalReferenceError("document_reference must not contain spaces")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
