from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.application.events_activities.events_activities_service import EventsActivitiesResponse
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesRequest,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesResponse,
)
from mfm.application.workflows.events_activities_workflow import EventsActivitiesWorkflow
from mfm.application.workflows.events_activities_workflow import EventsActivitiesWorkflowInput


class StubFeature:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _request() -> ManageEventsActivitiesRequest:
    return ManageEventsActivitiesRequest(
        operation="create-event",
        event_name="Annual Meetup",
        venue_name="Harbor Hall",
        venue_address="Dock 12",
        venue_capacity=200,
        start_at=datetime(2026, 1, 1, 9, 0, tzinfo=UTC),
        end_at=datetime(2026, 1, 1, 17, 0, tzinfo=UTC),
    )


def test_workflow_returns_success() -> None:
    response = ManageEventsActivitiesResponse(
        result=EventsActivitiesResponse(
            event_id=uuid4(),
            event_name="Annual Meetup",
            event_status="PLANNED",
            activities_count=0,
            registrations_count=0,
            attendances_count=0,
            generated_at=datetime(2026, 1, 1, tzinfo=UTC),
        )
    )
    workflow = EventsActivitiesWorkflow(feature=StubFeature(response=response))

    result = workflow.execute(EventsActivitiesWorkflowInput(request=_request()))

    assert result.success is True
    assert result.response == response


def test_workflow_returns_failure() -> None:
    workflow = EventsActivitiesWorkflow(feature=StubFeature(error=RuntimeError("failed")))

    result = workflow.execute(EventsActivitiesWorkflowInput(request=_request()))

    assert result.success is False
    assert result.response is None
    assert "failed" in result.message
