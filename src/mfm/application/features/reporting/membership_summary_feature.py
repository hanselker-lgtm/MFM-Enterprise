"""Feature API entry point for membership summary reporting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.reporting.membership_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.membership_summary_service import (
    MembershipSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.membership_summary_service import (
    MembershipSummaryService as ReportingMembershipSummaryService,
)
from mfm.application.reporting.membership_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.membership_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryResponse,
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
class MembershipSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


MembershipSummaryService = ReportingMembershipSummaryService


class MembershipSummaryFeature:
    """Feature facade for membership summary reporting."""

    def __init__(self, *, service: ReportingMembershipSummaryService) -> None:
        self._service = service

    def execute(self, request: MembershipSummaryRequest) -> MembershipSummaryResponse:
        request.validate()

        try:
            return self._service.execute(
                ServiceRequest(include_inactive=request.include_inactive)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Membership summary feature failed") from exc


def membership_summary(
    *,
    service: ReportingMembershipSummaryService,
    request: MembershipSummaryRequest,
) -> MembershipSummaryResponse:
    return MembershipSummaryFeature(service=service).execute(request)
