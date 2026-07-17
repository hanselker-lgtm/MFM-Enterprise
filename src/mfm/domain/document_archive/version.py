"""Version entity for document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Version:
    """Immutable-like snapshot of one document revision metadata."""

    version_number: int
    storage_key: str
    created_at: datetime
    file_name: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.version_number, int) or self.version_number <= 0:
            raise ValueError("version_number must be positive integer")

        self.storage_key = str(self.storage_key).strip()
        if not self.storage_key:
            raise ValueError("storage_key cannot be empty")

        if not isinstance(self.created_at, datetime) or self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware datetime")

        if self.file_name is not None:
            self.file_name = str(self.file_name).strip() or None
