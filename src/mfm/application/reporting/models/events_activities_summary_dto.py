"""DTOs for events activities summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class EventsActivitiesSummaryItemDTO:
    event_id: UUID
    event_name: str
    event_status: str
    venue_name: str
    activities_count: int
    registrations_count: int
    attendances_count: int


@dataclass(frozen=True, slots=True)
class EventsActivitiesSummaryResponse:
    events: tuple[EventsActivitiesSummaryItemDTO, ...]
    generated_at: datetime
