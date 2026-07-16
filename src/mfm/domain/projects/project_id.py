"""Identity value object for the Projects domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class ProjectId(ValueObject):
    """Identity for the Project aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("ProjectId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "ProjectId":
        return cls(uuid4())