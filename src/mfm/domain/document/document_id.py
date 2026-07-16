"""Identity value object for the Document domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class DocumentId(ValueObject):
    """Identity for the Document aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("DocumentId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "DocumentId":
        return cls(uuid4())
