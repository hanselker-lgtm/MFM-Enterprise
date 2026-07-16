"""Document number value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.document.exceptions import InvalidDocumentNumberError


@dataclass(frozen=True, slots=True)
class DocumentNumber(ValueObject):
    """Business identifier for a document."""

    value: str

    def __post_init__(self) -> None:
        value = str(self.value).strip()
        if not value:
            raise InvalidDocumentNumberError("document number cannot be empty")
        object.__setattr__(self, "value", value)
