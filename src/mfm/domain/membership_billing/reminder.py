"""Reminder domain entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from enum import Enum
from uuid import UUID
from uuid import uuid4


class ReminderStatus(str, Enum):
    """Reminder lifecycle states."""

    PENDING = "PENDING"
    SENT = "SENT"
    CANCELLED = "CANCELLED"


@dataclass(slots=True)
class Reminder:
    """Reminder tied to a member and optional invoice."""

    member_id: UUID
    message: str
    due_date: date
    invoice_id: UUID | None = None
    status: ReminderStatus = ReminderStatus.PENDING
    sent_at: datetime | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.member_id, UUID):
            raise ValueError("member_id must be UUID")
        if self.invoice_id is not None and not isinstance(self.invoice_id, UUID):
            raise ValueError("invoice_id must be UUID or None")
        if not isinstance(self.message, str) or not self.message.strip():
            raise ValueError("message must be non-empty string")
        if not isinstance(self.due_date, date):
            raise ValueError("due_date must be date")
        if not isinstance(self.status, ReminderStatus):
            self.status = ReminderStatus(str(self.status).upper())
        if self.sent_at is not None and not isinstance(self.sent_at, datetime):
            raise ValueError("sent_at must be datetime or None")

        self.message = self.message.strip()

    def mark_sent(self, at: datetime | None = None) -> None:
        self.status = ReminderStatus.SENT
        self.sent_at = at or datetime.now(UTC)
