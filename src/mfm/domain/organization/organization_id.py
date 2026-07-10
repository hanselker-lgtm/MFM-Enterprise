"""Organization value objects."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject
from mfm.domain.organization.exceptions import InvalidOrganizationNumberError


@dataclass(frozen=True, slots=True)
class OrganizationId(ValueObject):
    """Identity value object for Organization aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return

        if not isinstance(self.value, UUID):
            raise TypeError("OrganizationId value must be a UUID or UUID string")

    @classmethod
    def new(cls) -> "OrganizationId":
        return cls(uuid4())

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True, slots=True)
class OrganizationNumber(ValueObject):
    """Canonical organization number value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidOrganizationNumberError("organization_number must be a string")

        normalized = self.value.strip().upper()
        if not normalized:
            raise InvalidOrganizationNumberError("organization_number cannot be empty")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
