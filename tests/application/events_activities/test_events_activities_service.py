from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.events_activities.events_activities_service import AddActivityRequest
from mfm.application.events_activities.events_activities_service import BusinessRuleViolation
from mfm.application.events_activities.events_activities_service import CreateEventRequest
from mfm.application.events_activities.events_activities_service import EventsActivitiesService
from mfm.application.events_activities.events_activities_service import RecordAttendanceRequest
from mfm.application.events_activities.events_activities_service import RegisterParticipantRequest
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile


class InMemoryRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, EventActivityProfile] = {}

    def get(self, event_id: UUID) -> EventActivityProfile | None:
        return self.store.get(event_id)

    def save(self, profile: EventActivityProfile) -> None:
        self.store[profile.event.event_id] = profile


def _dt(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, 0, tzinfo=UTC)


def test_service_create_add_register_and_attend() -> None:
    repository = InMemoryRepository()
    service = EventsActivitiesService(repository=repository)

    create_result = service.create_event(
        CreateEventRequest(
            event_name="Annual Meetup",
            venue_name="Harbor Hall",
            venue_address="Dock 12",
            venue_capacity=250,
            start_at=_dt(9),
            end_at=_dt(17),
        )
    )

    add_result = service.add_activity(
        AddActivityRequest(
            event_id=create_result.event_id,
            title="Welcome Session",
            start_at=_dt(10),
            end_at=_dt(11),
        )
    )

    member_id = uuid4()
    register_result = service.register_participant(
        RegisterParticipantRequest(
            event_id=create_result.event_id,
            member_id=member_id,
            registered_at=_dt(8),
        )
    )

    profile = repository.get(create_result.event_id)
    assert profile is not None
    activity_id = profile.activities[0].activity_id

    attendance_result = service.record_attendance(
        RecordAttendanceRequest(
            event_id=create_result.event_id,
            activity_id=activity_id,
            member_id=member_id,
            attended_at=_dt(10),
            present=True,
        )
    )

    assert create_result.activities_count == 0
    assert add_result.activities_count == 1
    assert register_result.registrations_count == 1
    assert attendance_result.attendances_count == 1


def test_service_requires_existing_event_for_activity() -> None:
    service = EventsActivitiesService(repository=InMemoryRepository())

    with pytest.raises(BusinessRuleViolation, match="not found"):
        service.add_activity(
            AddActivityRequest(
                event_id=uuid4(),
                title="Talk",
                start_at=_dt(10),
                end_at=_dt(11),
            )
        )
