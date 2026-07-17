"""DTOs for contact communication reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ContactCommunicationSummaryResponse:
    contact_id: UUID
    method_count: int
    notification_count: int
    has_preference: bool
    pending_notifications: int
    sent_notifications: int
    failed_notifications: int
    generated_at: datetime
