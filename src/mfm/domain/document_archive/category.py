"""Category value object for document archive capability."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Category:
    """Classification category for archived documents."""

    code: str
    name: str

    def __post_init__(self) -> None:
        self.code = str(self.code).strip().upper()
        if not self.code:
            raise ValueError("category code cannot be empty")

        self.name = str(self.name).strip()
        if not self.name:
            raise ValueError("category name cannot be empty")
