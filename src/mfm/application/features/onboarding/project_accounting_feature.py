"""Feature API entry point for project accounting workflow."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.project_accounting_workflow import (
    ProjectAccountingWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.project_accounting_workflow import (
    ProjectAccountingWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.project_accounting_workflow import WorkflowExecutionError


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when workflow business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ProjectAccountingRequest:
    project_id: UUID
    journal_number: str
    posting_date: date
    transaction_description: str
    debit_account_id: UUID
    credit_account_id: UUID
    amount: Decimal | str | int
    currency: str = "DKK"
    transaction_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.journal_number, str) or not self.journal_number.strip():
            raise ValidationException("journal_number must be a non-empty string")
        if not isinstance(self.posting_date, date):
            raise ValidationException("posting_date must be date")
        if not isinstance(self.transaction_description, str) or not self.transaction_description.strip():
            raise ValidationException("transaction_description must be a non-empty string")
        if not isinstance(self.debit_account_id, UUID):
            raise ValidationException("debit_account_id must be UUID")
        if not isinstance(self.credit_account_id, UUID):
            raise ValidationException("credit_account_id must be UUID")
        if isinstance(self.amount, bool) or isinstance(self.amount, float):
            raise ValidationException("amount must not be bool/float")
        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValidationException("currency must be a non-empty string")
        if self.transaction_reference is not None and not isinstance(self.transaction_reference, str):
            raise ValidationException("transaction_reference must be string or None")


@dataclass(frozen=True, slots=True)
class ProjectAccountingResponse:
    project_id: UUID
    journal_id: UUID
    journal_number: str
    journal_status: str
    completed_steps: tuple[str, ...]


class ProjectAccountingService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ProjectAccountingFeature:
    """Feature facade for project accounting orchestration."""

    def __init__(self, *, service: ProjectAccountingService) -> None:
        self._service = service

    def execute(self, request: ProjectAccountingRequest) -> ProjectAccountingResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    journal_number=request.journal_number,
                    posting_date=request.posting_date,
                    transaction_description=request.transaction_description,
                    debit_account_id=request.debit_account_id,
                    credit_account_id=request.credit_account_id,
                    amount=request.amount,
                    currency=request.currency,
                    transaction_reference=request.transaction_reference,
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Project accounting feature failed") from exc

        return ProjectAccountingResponse(
            project_id=service_response.project_id,
            journal_id=service_response.journal_id,
            journal_number=service_response.journal_number,
            journal_status=service_response.journal_status,
            completed_steps=service_response.completed_steps,
        )
