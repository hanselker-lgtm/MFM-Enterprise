from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.events_activities.events_activities_service import EventsActivitiesResponse
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesFeature,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesRequest,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    RepositoryException,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ValidationException,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def create_event(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def add_activity(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def register_participant(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def record_attendance(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _response() -> EventsActivitiesResponse:
    return EventsActivitiesResponse(
        event_id=uuid4(),
        event_name="Annual Meetup",
        event_status="PLANNED",
        activities_count=1,
        registrations_count=1,
        attendances_count=0,
        generated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )


def _dt(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, 0, tzinfo=UTC)


def test_feature_routes_create_event_and_maps_response() -> None:
    feature = ManageEventsActivitiesFeature(service=StubService(response=_response()))

    result = feature.execute(
        ManageEventsActivitiesRequest(
            operation="create-event",
            event_name="Annual Meetup",
            venue_name="Harbor Hall",
            venue_address="Dock 12",
            venue_capacity=200,
            start_at=_dt(9),
            end_at=_dt(17),
        )
    )

    assert result.result.event_name == "Annual Meetup"


def test_feature_validates_request() -> None:
    feature = ManageEventsActivitiesFeature(service=StubService(response=_response()))

    with pytest.raises(ValidationException):
        feature.execute(
            ManageEventsActivitiesRequest(
                operation="register",
                event_id=uuid4(),
                member_id=uuid4(),
                start_at=None,
            )
        )


def test_feature_maps_unknown_error() -> None:
    feature = ManageEventsActivitiesFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(
            ManageEventsActivitiesRequest(
                operation="create-event",
                event_name="Annual Meetup",
                venue_name="Harbor Hall",
                venue_address="Dock 12",
                venue_capacity=200,
                start_at=_dt(9),
                end_at=_dt(17),
            )
        )
