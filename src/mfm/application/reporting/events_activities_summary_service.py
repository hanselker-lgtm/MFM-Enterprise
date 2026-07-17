"""Reporting service for events and activities capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol

from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryItemDTO,
)
from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryResponse,
)
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class EventsActivitiesSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


class EventsActivitiesRepositoryPort(Protocol):
    def list(self) -> list[EventActivityProfile]: ...


class EventsActivitiesSummaryService:
    """Build summary metrics from events activities profiles."""

    def __init__(self, *, repository: EventsActivitiesRepositoryPort) -> None:
        self._repository = repository

    def execute(self, request: EventsActivitiesSummaryRequest) -> EventsActivitiesSummaryResponse:
        request.validate()

        try:
            profiles = self._repository.list()
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Events activities summary retrieval failed") from exc

        items: list[EventsActivitiesSummaryItemDTO] = []
        for profile in profiles:
            if not request.include_inactive and profile.event.status.upper() == "CANCELLED":
                continue

            items.append(
                EventsActivitiesSummaryItemDTO(
                    event_id=profile.event.event_id,
                    event_name=profile.event.name,
                    event_status=profile.event.status,
                    venue_name=profile.event.venue.name,
                    activities_count=len(profile.activities),
                    registrations_count=len(profile.registrations),
                    attendances_count=len(profile.attendances),
                )
            )

        return EventsActivitiesSummaryResponse(
            events=tuple(items),
            generated_at=datetime.now(UTC),
        )
