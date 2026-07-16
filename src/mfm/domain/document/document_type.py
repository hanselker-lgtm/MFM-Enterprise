"""Document type value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.document.exceptions import InvalidDocumentTypeError


@dataclass(frozen=True, slots=True)
class DocumentType(ValueObject):
    """Classification type for a document."""

    value: str

    def __post_init__(self) -> None:
        value = str(self.value).strip().upper()
        if not value:
            raise InvalidDocumentTypeError("document type cannot be empty")
        object.__setattr__(self, "value", value)
