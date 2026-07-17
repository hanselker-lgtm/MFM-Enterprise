from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.events_activities_summary_feature import (
    EventsActivitiesSummaryFeature,
)
from mfm.application.features.reporting.events_activities_summary_feature import (
    EventsActivitiesSummaryRequest,
)
from mfm.application.features.reporting.events_activities_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.events_activities_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryItemDTO,
)
from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def test_reporting_feature_returns_response() -> None:
    feature = EventsActivitiesSummaryFeature(
        service=StubService(
            response=EventsActivitiesSummaryResponse(
                events=(
                    EventsActivitiesSummaryItemDTO(
                        event_id=uuid4(),
                        event_name="Annual Meetup",
                        event_status="PLANNED",
                        venue_name="Harbor Hall",
                        activities_count=1,
                        registrations_count=2,
                        attendances_count=1,
                    ),
                ),
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(EventsActivitiesSummaryRequest())

    assert len(response.events) == 1
    assert response.events[0].event_name == "Annual Meetup"


def test_reporting_feature_validates_request() -> None:
    feature = EventsActivitiesSummaryFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(EventsActivitiesSummaryRequest(include_inactive="invalid"))


def test_reporting_feature_maps_unknown_error() -> None:
    feature = EventsActivitiesSummaryFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(EventsActivitiesSummaryRequest())
