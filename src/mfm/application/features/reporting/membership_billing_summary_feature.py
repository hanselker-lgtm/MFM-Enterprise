"""Feature API for membership billing summary reporting."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.reporting.membership_billing_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.membership_billing_summary_service import (
    MembershipBillingSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.membership_billing_summary_service import (
    MembershipBillingSummaryService as ReportingMembershipBillingSummaryService,
)
from mfm.application.reporting.membership_billing_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.membership_billing_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryResponse,
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
class MembershipBillingSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


MembershipBillingSummaryService = ReportingMembershipBillingSummaryService


class MembershipBillingSummaryFeature:
    """Feature facade for membership billing summary reporting."""

    def __init__(self, *, service: ReportingMembershipBillingSummaryService) -> None:
        self._service = service

    def execute(self, request: MembershipBillingSummaryRequest) -> MembershipBillingSummaryResponse:
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
            raise RepositoryException("Membership billing summary feature failed") from exc
