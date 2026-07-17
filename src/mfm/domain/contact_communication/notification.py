"""Notification entity for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from enum import Enum
from uuid import UUID
from uuid import uuid4


class NotificationStatus(str, Enum):
    """Lifecycle status for notifications."""

    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"


@dataclass(slots=True)
class Notification:
    """Notification to be delivered through a contact method."""

    contact_id: UUID
    method_id: UUID
    subject: str
    message: str
    status: NotificationStatus = NotificationStatus.PENDING
    sent_at: datetime | None = None
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.contact_id, UUID):
            raise ValueError("contact_id must be UUID")
        if not isinstance(self.method_id, UUID):
            raise ValueError("method_id must be UUID")
        if not isinstance(self.subject, str) or not self.subject.strip():
            raise ValueError("subject must be a non-empty string")
        if not isinstance(self.message, str) or not self.message.strip():
            raise ValueError("message must be a non-empty string")
        if not isinstance(self.status, NotificationStatus):
            self.status = NotificationStatus(str(self.status).upper())
        if self.sent_at is not None and not isinstance(self.sent_at, datetime):
            raise ValueError("sent_at must be datetime or None")

        self.subject = self.subject.strip()
        self.message = self.message.strip()

    def mark_sent(self, at: datetime | None = None) -> None:
        self.status = NotificationStatus.SENT
        self.sent_at = at or datetime.now(UTC)

    def mark_failed(self) -> None:
        self.status = NotificationStatus.FAILED
