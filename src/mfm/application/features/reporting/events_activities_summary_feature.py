"""Feature API for events activities summary reporting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.reporting.events_activities_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.events_activities_summary_service import (
    EventsActivitiesSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.events_activities_summary_service import (
    EventsActivitiesSummaryService as ReportingEventsActivitiesSummaryService,
)
from mfm.application.reporting.events_activities_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.events_activities_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryResponse,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when report business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class EventsActivitiesSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


EventsActivitiesSummaryService = ReportingEventsActivitiesSummaryService


class EventsActivitiesSummaryFeature:
    """Feature facade for events activities summary reporting."""

    def __init__(self, *, service: ReportingEventsActivitiesSummaryService) -> None:
        self._service = service

    def execute(self, request: EventsActivitiesSummaryRequest) -> EventsActivitiesSummaryResponse:
        request.validate()

        try:
            return self._service.execute(ServiceRequest(include_inactive=request.include_inactive))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Events activities summary feature failed") from exc
