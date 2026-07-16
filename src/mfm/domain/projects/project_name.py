"""Project name value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.projects.exceptions import InvalidProjectNameError


@dataclass(frozen=True, slots=True)
class ProjectName(ValueObject):
    """Display name for a project."""

    value: str

    def __post_init__(self) -> None:
        value = str(self.value).strip()
        if not value:
            raise InvalidProjectNameError("project name cannot be empty")
        object.__setattr__(self, "value", value)