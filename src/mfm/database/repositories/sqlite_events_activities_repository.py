"""In-process repository adapter for events and activities profiles."""

from __future__ import annotations

from copy import deepcopy
from uuid import UUID

from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.repositories.events_activities_repository import EventsActivitiesRepository


class SQLiteEventsActivitiesRepository(EventsActivitiesRepository):
    """Repository adapter preserving event profiles for process lifetime."""

    _store: dict[UUID, EventActivityProfile] = {}

    def get(self, event_id: UUID) -> EventActivityProfile | None:
        profile = self._store.get(event_id)
        if profile is None:
            return None
        return deepcopy(profile)

    def save(self, profile: EventActivityProfile) -> None:
        self._store[profile.event.event_id] = deepcopy(profile)

    def list(self) -> list[EventActivityProfile]:
        return [deepcopy(item) for item in self._store.values()]

    @classmethod
    def clear(cls) -> None:
        cls._store.clear()
