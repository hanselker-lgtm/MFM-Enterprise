"""Feature API for CAP-005 events and activities capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from typing import Protocol
from uuid import UUID

from mfm.application.events_activities.events_activities_service import (
    AddActivityRequest as ServiceAddActivityRequest,
)
from mfm.application.events_activities.events_activities_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.events_activities.events_activities_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.events_activities.events_activities_service import (
    CreateEventRequest as ServiceCreateEventRequest,
)
from mfm.application.events_activities.events_activities_service import (
    EventsActivitiesResponse,
)
from mfm.application.events_activities.events_activities_service import (
    RecordAttendanceRequest as ServiceRecordAttendanceRequest,
)
from mfm.application.events_activities.events_activities_service import (
    RegisterParticipantRequest as ServiceRegisterParticipantRequest,
)
from mfm.application.events_activities.events_activities_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.events_activities.events_activities_service import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


EventsActivitiesOperation = Literal[
    "create-event",
    "add-activity",
    "register",
    "record-attendance",
]


@dataclass(frozen=True, slots=True)
class ManageEventsActivitiesRequest:
    operation: EventsActivitiesOperation
    event_id: UUID | None = None
    event_name: str | None = None
    event_description: str | None = None
    venue_name: str | None = None
    venue_address: str | None = None
    venue_capacity: int | None = None
    title: str | None = None
    status: str = "PLANNED"
    description: str | None = None
    start_at: datetime | None = None
    end_at: datetime | None = None
    timezone: str = "UTC"
    member_id: UUID | None = None
    attended_at: datetime | None = None
    present: bool = True
    activity_id: UUID | None = None

    def validate(self) -> None:
        if self.operation not in (
            "create-event",
            "add-activity",
            "register",
            "record-attendance",
        ):
            raise ValidationException("operation must be create-event, add-activity, register, or record-attendance")

        if self.operation == "create-event":
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

        if self.operation == "add-activity":
            if not isinstance(self.event_id, UUID):
                raise ValidationException("event_id must be UUID")
            if not isinstance(self.title, str) or not self.title.strip():
                raise ValidationException("title must be non-empty string")
            if not isinstance(self.start_at, datetime) or self.start_at.tzinfo is None:
                raise ValidationException("start_at must be timezone-aware datetime")
            if not isinstance(self.end_at, datetime) or self.end_at.tzinfo is None:
                raise ValidationException("end_at must be timezone-aware datetime")

        if self.operation == "register":
            if not isinstance(self.event_id, UUID):
                raise ValidationException("event_id must be UUID")
            if not isinstance(self.member_id, UUID):
                raise ValidationException("member_id must be UUID")
            if not isinstance(self.start_at, datetime) or self.start_at.tzinfo is None:
                raise ValidationException("start_at must be timezone-aware datetime for registration")

        if self.operation == "record-attendance":
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
class ManageEventsActivitiesResponse:
    result: EventsActivitiesResponse


class EventsActivitiesServicePort(Protocol):
    def create_event(self, request: ServiceCreateEventRequest) -> EventsActivitiesResponse: ...

    def add_activity(self, request: ServiceAddActivityRequest) -> EventsActivitiesResponse: ...

    def register_participant(self, request: ServiceRegisterParticipantRequest) -> EventsActivitiesResponse: ...

    def record_attendance(self, request: ServiceRecordAttendanceRequest) -> EventsActivitiesResponse: ...


class ManageEventsActivitiesFeature:
    """Feature facade for events and activities operations."""

    def __init__(self, *, service: EventsActivitiesServicePort) -> None:
        self._service = service

    def execute(self, request: ManageEventsActivitiesRequest) -> ManageEventsActivitiesResponse:
        request.validate()

        try:
            if request.operation == "create-event":
                result = self._service.create_event(
                    ServiceCreateEventRequest(
                        event_name=request.event_name,
                        event_description=request.event_description,
                        venue_name=request.venue_name,
                        venue_address=request.venue_address,
                        venue_capacity=request.venue_capacity,
                        start_at=request.start_at,
                        end_at=request.end_at,
                        timezone=request.timezone,
                    )
                )
                return ManageEventsActivitiesResponse(result=result)

            if request.operation == "add-activity":
                result = self._service.add_activity(
                    ServiceAddActivityRequest(
                        event_id=request.event_id,
                        title=request.title,
                        status=request.status,
                        description=request.description,
                        start_at=request.start_at,
                        end_at=request.end_at,
                        timezone=request.timezone,
                    )
                )
                return ManageEventsActivitiesResponse(result=result)

            if request.operation == "register":
                result = self._service.register_participant(
                    ServiceRegisterParticipantRequest(
                        event_id=request.event_id,
                        member_id=request.member_id,
                        registered_at=request.start_at,
                    )
                )
                return ManageEventsActivitiesResponse(result=result)

            result = self._service.record_attendance(
                ServiceRecordAttendanceRequest(
                    event_id=request.event_id,
                    activity_id=request.activity_id,
                    member_id=request.member_id,
                    attended_at=request.attended_at,
                    present=request.present,
                )
            )
            return ManageEventsActivitiesResponse(result=result)
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Manage events activities feature failed") from exc
