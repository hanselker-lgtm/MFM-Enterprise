"""Archive lifecycle metadata for document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Archive:
    """Archive metadata for one document."""

    archived_at: datetime
    reason: str

    def __post_init__(self) -> None:
        if not isinstance(self.archived_at, datetime) or self.archived_at.tzinfo is None:
            raise ValueError("archived_at must be timezone-aware datetime")

        self.reason = str(self.reason).strip()
        if not self.reason:
            raise ValueError("archive reason cannot be empty")
