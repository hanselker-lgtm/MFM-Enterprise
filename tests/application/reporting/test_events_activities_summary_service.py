from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.application.reporting.events_activities_summary_service import (
    EventsActivitiesSummaryRequest,
)
from mfm.application.reporting.events_activities_summary_service import (
    EventsActivitiesSummaryService,
)
from mfm.domain.events_activities.event import Event
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.domain.events_activities.schedule import Schedule
from mfm.domain.events_activities.venue import Venue


class InMemoryRepository:
    def __init__(self, profiles: list[EventActivityProfile]) -> None:
        self.profiles = profiles

    def list(self) -> list[EventActivityProfile]:
        return self.profiles


def test_summary_service_returns_event_metrics() -> None:
    profile = EventActivityProfile(
        event=Event(
            name="Annual Meetup",
            venue=Venue(name="Harbor Hall", address="Dock 12", capacity=200),
            schedule=Schedule(
                start_at=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
                end_at=datetime(2026, 1, 1, 17, 0, tzinfo=UTC),
            ),
        )
    )
    service = EventsActivitiesSummaryService(repository=InMemoryRepository([profile]))

    response = service.execute(EventsActivitiesSummaryRequest())

    assert len(response.events) == 1
    assert response.events[0].event_name == "Annual Meetup"
    assert response.events[0].venue_name == "Harbor Hall"
