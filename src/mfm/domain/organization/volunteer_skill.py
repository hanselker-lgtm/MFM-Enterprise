"""Volunteer skill value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.organization.exceptions import InvalidVolunteerSkillError


@dataclass(frozen=True, slots=True)
class VolunteerSkill(ValueObject):
    """Canonical skill representation for volunteer competencies."""

    name: str

    def __post_init__(self) -> None:
        if not isinstance(self.name, str):
            raise InvalidVolunteerSkillError("skill name must be a string")
        normalized = self.name.strip().upper()
        if not normalized:
            raise InvalidVolunteerSkillError("skill name cannot be empty")
        object.__setattr__(self, "name", normalized)

    def __str__(self) -> str:
        return self.name
