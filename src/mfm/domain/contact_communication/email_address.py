"""Email address value object for contact communication capability."""

from __future__ import annotations

import re
from dataclasses import dataclass

_EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


@dataclass(frozen=True, slots=True)
class EmailAddress:
    """Immutable normalized email address."""

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()
        if not _EMAIL_PATTERN.fullmatch(normalized):
            raise ValueError(f"Invalid email address: {self.value}")
        object.__setattr__(self, "value", normalized)
