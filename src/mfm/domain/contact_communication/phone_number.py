"""Phone number value object for contact communication capability."""

from __future__ import annotations

import re
from dataclasses import dataclass

_PHONE_PATTERN = re.compile(r"^\+?[0-9]{6,20}$")


@dataclass(frozen=True, slots=True)
class PhoneNumber:
    """Immutable normalized phone number."""

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.replace(" ", "")
        if not _PHONE_PATTERN.fullmatch(normalized):
            raise ValueError(f"Invalid phone number: {self.value}")
        object.__setattr__(self, "value", normalized)
