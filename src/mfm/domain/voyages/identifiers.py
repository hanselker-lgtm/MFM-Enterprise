"""Identity value objects for the voyages domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class VoyageId(ValueObject):
    """Identity for the Voyage aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("VoyageId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "VoyageId":
        return cls(uuid4())