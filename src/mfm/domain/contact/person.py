"""
Person Entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Person:
    """
    Represents a physical person.
    """

    first_name: str

    last_name: str

    middle_name: str = ""

    title: str = ""

    birth_date: date | None = None

    def __post_init__(self) -> None:

        self.first_name = self.first_name.strip()

        self.middle_name = self.middle_name.strip()

        self.last_name = self.last_name.strip()

        self.title = self.title.strip()

    @property
    def full_name(self) -> str:

        parts = [
            self.first_name,
            self.middle_name,
            self.last_name,
        ]

        return " ".join(
            part for part in parts if part
        )

    @property
    def initials(self) -> str:

        result = ""

        if self.first_name:
            result += self.first_name[0]

        if self.middle_name:
            result += self.middle_name[0]

        if self.last_name:
            result += self.last_name[0]

        return result.upper()

    def __str__(self) -> str:

        return self.full_name