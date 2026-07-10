"""Role code value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.organization.exceptions import InvalidRoleCodeError


@dataclass(frozen=True, slots=True)
class RoleCode(ValueObject):
    """Canonical role code value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise InvalidRoleCodeError("role_code must be a string")

        normalized = self.value.strip().upper()
        if not normalized:
            raise InvalidRoleCodeError("role_code cannot be empty")

        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
