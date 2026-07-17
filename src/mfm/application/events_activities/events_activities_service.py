"""Application service for events and activities capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.domain.events_activities.activity import Activity
from mfm.domain.events_activities.attendance import Attendance
from mfm.domain.events_activities.event import Event
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.domain.events_activities.registration import Registration
from mfm.domain.events_activities.schedule import Schedule
from mfm.domain.events_activities.venue import Venue


class ApplicationException(Exception):
    """Base exception for events activities service failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class CreateEventRequest:
    event_name: str
    venue_name: str
    venue_address: str
    venue_capacity: int
    start_at: datetime
    end_at: datetime
    timezone: str = "UTC"
    event_description: str | None = None

    def validate(self) -> None:
        if not isinstance(self.event_name, str) or not self.event_name.strip():
            raise ValidationException("event_name must be non-empty string")
        if not isinstance(self.venue_name, str) or not self.venue_name.strip():
            raise ValidationException("venue_name must be non-empty string")
        if not isinstance(self.venue_address, str) or not self.venue_address.strip():
            raise ValidationException("venue_address must be non-empty string")
        if not isinstance(self.venue_capacity, int) or self.venue_capacity <= 0:
            raise ValidationException("venue_capacity must be positive integer")
        if not isinstance(self.start_at, datetime) or self.start_at.tzinfo is None:
            raise ValidationException("start_at must be timezone-aware datetime")
        if not isinstance(self.end_at, datetime) or self.end_at.tzinfo is None:
            raise ValidationException("end_at must be timezone-aware datetime")
        if not isinstance(self.timezone, str) or not self.timezone.strip():
            raise ValidationException("timezone must be non-empty string")


@dataclass(frozen=True, slots=True)
class AddActivityRequest:
    event_id: UUID
    title: str
    start_at: datetime
    end_at: datetime
    timezone: str = "UTC"
    status: str = "PLANNED"
    description: str | None = None

    def validate(self) -> None:
        if not isinstance(self.event_id, UUID):
            raise ValidationException("event_id must be UUID")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationException("title must be non-empty string")
        if not isinstance(self.start_at, datetime) or self.start_at.tzinfo is None:
            raise ValidationException("start_at must be timezone-aware datetime")
        if not isinstance(self.end_at, datetime) or self.end_at.tzinfo is None:
            raise ValidationException("end_at must be timezone-aware datetime")
        if not isinstance(self.timezone, str) or not self.timezone.strip():
            raise ValidationException("timezone must be non-empty string")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")


@dataclass(frozen=True, slots=True)
class RegisterParticipantRequest:
    event_id: UUID
    member_id: UUID
    registered_at: datetime

    def validate(self) -> None:
        if not isinstance(self.event_id, UUID):
            raise ValidationException("event_id must be UUID")
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")
        if not isinstance(self.registered_at, datetime) or self.registered_at.tzinfo is None:
            raise ValidationException("registered_at must be timezone-aware datetime")


@dataclass(frozen=True, slots=True)
class RecordAttendanceRequest:
    event_id: UUID
    activity_id: UUID
    member_id: UUID
    attended_at: datetime
    present: bool = True

    def validate(self) -> None:
        if not isinstance(self.event_id, UUID):
            raise ValidationException("event_id must be UUID")
        if not isinstance(self.activity_id, UUID):
            raise ValidationException("activity_id must be UUID")
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")
        if not isinstance(self.attended_at, datetime) or self.attended_at.tzinfo is None:
            raise ValidationException("attended_at must be timezone-aware datetime")
        if not isinstance(self.present, bool):
            raise ValidationException("present must be bool")


@dataclass(frozen=True, slots=True)
class EventsActivitiesResponse:
    event_id: UUID
    event_name: str
    event_status: str
    activities_count: int
    registrations_count: int
    attendances_count: int
    generated_at: datetime


class EventsActivitiesRepositoryPort(Protocol):
    def get(self, event_id: UUID) -> EventActivityProfile | None: ...

    def save(self, profile: EventActivityProfile) -> None: ...


class EventsActivitiesService:
    """Manage events, activities, registrations, and attendance."""

    def __init__(self, *, repository: EventsActivitiesRepositoryPort) -> None:
        self._repository = repository

    def create_event(self, request: CreateEventRequest) -> EventsActivitiesResponse:
        request.validate()

        try:
            venue = Venue(
                name=request.venue_name,
                address=request.venue_address,
                capacity=request.venue_capacity,
            )
            schedule = Schedule(
                start_at=request.start_at,
                end_at=request.end_at,
                timezone=request.timezone,
            )
            event = Event(
                name=request.event_name,
                venue=venue,
                schedule=schedule,
                description=request.event_description,
                status="PLANNED",
            )
            profile = EventActivityProfile(event=event)
            self._repository.save(profile)
            return self._to_response(profile)
        except ValidationException:
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create event failed") from exc

    def add_activity(self, request: AddActivityRequest) -> EventsActivitiesResponse:
        request.validate()

        try:
            profile = self._require_profile(request.event_id)
            activity = Activity(
                event_id=request.event_id,
                title=request.title,
                schedule=Schedule(
                    start_at=request.start_at,
                    end_at=request.end_at,
                    timezone=request.timezone,
                ),
                status=request.status,
                description=request.description,
            )
            profile.add_activity(activity)
            self._repository.save(profile)
            return self._to_response(profile)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Add activity failed") from exc

    def register_participant(self, request: RegisterParticipantRequest) -> EventsActivitiesResponse:
        request.validate()

        try:
            profile = self._require_profile(request.event_id)
            profile.add_registration(
                Registration(
                    event_id=request.event_id,
                    member_id=request.member_id,
                    registered_at=request.registered_at,
                )
            )
            self._repository.save(profile)
            return self._to_response(profile)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Register participant failed") from exc

    def record_attendance(self, request: RecordAttendanceRequest) -> EventsActivitiesResponse:
        request.validate()

        try:
            profile = self._require_profile(request.event_id)
            profile.add_attendance(
                Attendance(
                    event_id=request.event_id,
                    activity_id=request.activity_id,
                    member_id=request.member_id,
                    attended_at=request.attended_at,
                    present=request.present,
                )
            )
            self._repository.save(profile)
            return self._to_response(profile)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Record attendance failed") from exc

    def _require_profile(self, event_id: UUID) -> EventActivityProfile:
        profile = self._repository.get(event_id)
        if profile is None:
            raise BusinessRuleViolation(f"Event profile {event_id} not found")
        return profile

    @staticmethod
    def _to_response(profile: EventActivityProfile) -> EventsActivitiesResponse:
        return EventsActivitiesResponse(
            event_id=profile.event.event_id,
            event_name=profile.event.name,
            event_status=profile.event.status,
            activities_count=len(profile.activities),
            registrations_count=len(profile.registrations),
            attendances_count=len(profile.attendances),
            generated_at=datetime.now(UTC),
        )
