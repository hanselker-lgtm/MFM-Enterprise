"""Aggregate profile for event and activity operations."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from mfm.domain.events_activities.activity import Activity
from mfm.domain.events_activities.attendance import Attendance
from mfm.domain.events_activities.event import Event
from mfm.domain.events_activities.registration import Registration


@dataclass(slots=True)
class EventActivityProfile:
    """Aggregate boundary for CAP-005 event management."""

    event: Event
    activities: list[Activity] = field(default_factory=list)
    registrations: list[Registration] = field(default_factory=list)
    attendances: list[Attendance] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not isinstance(self.event, Event):
            raise ValueError("event must be Event")

        self.activities = list(self.activities)
        self.registrations = list(self.registrations)
        self.attendances = list(self.attendances)

    def add_activity(self, activity: Activity) -> None:
        if activity.event_id != self.event.event_id:
            raise ValueError("activity event_id does not match profile event")
        if any(item.activity_id == activity.activity_id for item in self.activities):
            raise ValueError(f"Activity {activity.activity_id} already exists")
        self.activities.append(activity)

    def add_registration(self, registration: Registration) -> None:
        if registration.event_id != self.event.event_id:
            raise ValueError("registration event_id does not match profile event")
        if any(item.member_id == registration.member_id for item in self.registrations):
            raise ValueError(f"Member {registration.member_id} already registered")
        self.registrations.append(registration)

    def add_attendance(self, attendance: Attendance) -> None:
        if attendance.event_id != self.event.event_id:
            raise ValueError("attendance event_id does not match profile event")
        if not any(item.activity_id == attendance.activity_id for item in self.activities):
            raise ValueError("attendance activity not found in event")
        if not any(item.member_id == attendance.member_id for item in self.registrations):
            raise ValueError("attendance member is not registered")
        self.attendances.append(attendance)
