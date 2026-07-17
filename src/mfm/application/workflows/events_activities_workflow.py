"""Workflow for CAP-005 events and activities capability."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesFeature,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesRequest,
)
from mfm.application.features.events_activities.manage_events_activities_feature import (
    ManageEventsActivitiesResponse,
)


@dataclass(frozen=True, slots=True)
class EventsActivitiesWorkflowInput:
    request: ManageEventsActivitiesRequest


@dataclass(frozen=True, slots=True)
class EventsActivitiesWorkflowResult:
    success: bool
    response: ManageEventsActivitiesResponse | None = None
    message: str = ""


class EventsActivitiesWorkflow:
    """Workflow wrapper around events activities feature API."""

    def __init__(self, *, feature: ManageEventsActivitiesFeature) -> None:
        self._feature = feature

    def execute(self, data: EventsActivitiesWorkflowInput) -> EventsActivitiesWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return EventsActivitiesWorkflowResult(
                success=True,
                response=response,
                message="Events activities operation completed",
            )
        except Exception as exc:
            return EventsActivitiesWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
