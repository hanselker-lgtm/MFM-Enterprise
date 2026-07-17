"""Schedule value object for events and activities."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Schedule:
    """Represents start/end timing metadata."""

    start_at: datetime
    end_at: datetime
    timezone: str = "UTC"

    def __post_init__(self) -> None:
        if not isinstance(self.start_at, datetime):
            raise ValueError("start_at must be datetime")
        if not isinstance(self.end_at, datetime):
            raise ValueError("end_at must be datetime")
        if self.start_at.tzinfo is None or self.end_at.tzinfo is None:
            raise ValueError("start_at and end_at must be timezone-aware")
        if self.end_at <= self.start_at:
            raise ValueError("end_at must be after start_at")

        self.timezone = str(self.timezone).strip().upper()
        if not self.timezone:
            raise ValueError("timezone cannot be empty")
