"""Role identity value object."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class RoleId(ValueObject):
    """Identity value object for Role aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return

        if not isinstance(self.value, UUID):
            raise TypeError("RoleId value must be a UUID or UUID string")

    @classmethod
    def new(cls) -> "RoleId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)
