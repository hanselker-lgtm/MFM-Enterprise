"""Project number value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.projects.exceptions import InvalidProjectNumberError


@dataclass(frozen=True, slots=True)
class ProjectNumber(ValueObject):
    """Business identifier for a project."""

    value: str

    def __post_init__(self) -> None:
        value = str(self.value).strip()
        if not value:
            raise InvalidProjectNumberError("project number cannot be empty")
        object.__setattr__(self, "value", value)