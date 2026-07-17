"""Feature API entry point for REP-004 budget vs actual reporting."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.reporting.budget_vs_actual_service import ApplicationException as ServiceApplicationException
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualRequest as ServiceRequest
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualService as ReportingBudgetVsActualService
from mfm.application.reporting.budget_vs_actual_service import RepositoryException as ServiceRepositoryException
from mfm.application.reporting.budget_vs_actual_service import ValidationException as ServiceValidationException
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualDTO


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when report business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class BudgetVsActualRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


BudgetVsActualService = ReportingBudgetVsActualService


class BudgetVsActualFeature:
    """Feature facade for budget-vs-actual reporting."""

    def __init__(self, *, service: ReportingBudgetVsActualService) -> None:
        self._service = service

    def execute(self, request: BudgetVsActualRequest) -> BudgetVsActualDTO:
        request.validate()

        try:
            return self._service.execute(ServiceRequest(project_id=request.project_id))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Budget vs actual feature failed") from exc


def budget_vs_actual(
    *,
    service: ReportingBudgetVsActualService,
    request: BudgetVsActualRequest,
) -> BudgetVsActualDTO:
    return BudgetVsActualFeature(service=service).execute(request)
