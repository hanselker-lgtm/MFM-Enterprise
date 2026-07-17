from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.domain.events_activities.activity import Activity
from mfm.domain.events_activities.attendance import Attendance
from mfm.domain.events_activities.event import Event
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.domain.events_activities.registration import Registration
from mfm.domain.events_activities.schedule import Schedule
from mfm.domain.events_activities.venue import Venue


def _schedule(hour_start: int, hour_end: int) -> Schedule:
    return Schedule(
        start_at=datetime(2026, 1, 1, hour_start, 0, tzinfo=UTC),
        end_at=datetime(2026, 1, 1, hour_end, 0, tzinfo=UTC),
        timezone="UTC",
    )


def test_profile_supports_activity_registration_attendance() -> None:
    event = Event(
        name="General Assembly",
        venue=Venue(name="Hall A", address="Harbor 1", capacity=150),
        schedule=_schedule(10, 12),
    )
    profile = EventActivityProfile(event=event)

    activity = Activity(
        event_id=event.event_id,
        title="Opening",
        schedule=_schedule(10, 11),
    )
    profile.add_activity(activity)

    member_id = uuid4()
    profile.add_registration(
        Registration(
            event_id=event.event_id,
            member_id=member_id,
            registered_at=datetime(2026, 1, 1, 8, 0, tzinfo=UTC),
        )
    )
    profile.add_attendance(
        Attendance(
            event_id=event.event_id,
            activity_id=activity.activity_id,
            member_id=member_id,
            attended_at=datetime(2026, 1, 1, 10, 30, tzinfo=UTC),
            present=True,
        )
    )

    assert len(profile.activities) == 1
    assert len(profile.registrations) == 1
    assert len(profile.attendances) == 1


def test_schedule_rejects_inverted_range() -> None:
    with pytest.raises(ValueError, match="after"):
        Schedule(
            start_at=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
            end_at=datetime(2026, 1, 1, 10, 0, tzinfo=UTC),
            timezone="UTC",
        )
