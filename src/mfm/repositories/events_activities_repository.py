"""Repository contract for CAP-005 events and activities capability."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.events_activities.event_activity_profile import EventActivityProfile


class EventsActivitiesRepository(ABC):
    """Persistence contract for event activity profiles."""

    @abstractmethod
    def get(self, event_id: UUID) -> EventActivityProfile | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, profile: EventActivityProfile) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[EventActivityProfile]:
        raise NotImplementedError
