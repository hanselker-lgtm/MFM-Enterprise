"""Domain entities for CAP-005 events and activities capability."""

from mfm.domain.events_activities.activity import Activity
from mfm.domain.events_activities.attendance import Attendance
from mfm.domain.events_activities.event import Event
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.domain.events_activities.registration import Registration
from mfm.domain.events_activities.schedule import Schedule
from mfm.domain.events_activities.venue import Venue

__all__ = [
    "Activity",
    "Attendance",
    "Event",
    "EventActivityProfile",
    "Registration",
    "Schedule",
    "Venue",
]
