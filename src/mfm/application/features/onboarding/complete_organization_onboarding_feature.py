"""Feature API entry point for complete organization onboarding workflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    DefaultLedgerAccountInput as ServiceLedgerAccountInput,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    WorkflowExecutionError,
)
from mfm.domain.organization.organization_type import OrganizationType


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when workflow business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class DefaultLedgerAccountInput:
    account_number: str
    name: str
    account_type: str
    normal_balance: str


@dataclass(frozen=True, slots=True)
class CompleteOrganizationOnboardingRequest:
    organization_number: str
    organization_name: str
    organization_type: OrganizationType
    fiscal_year: int
    document_library_number: str | None = None
    document_library_title: str = "Default Organization Library"
    chart_of_accounts: tuple[DefaultLedgerAccountInput, ...] = (
        DefaultLedgerAccountInput(
            account_number="1000-CASH",
            name="Cash",
            account_type="ASSET",
            normal_balance="DEBIT",
        ),
        DefaultLedgerAccountInput(
            account_number="1100-AR",
            name="Accounts Receivable",
            account_type="ASSET",
            normal_balance="DEBIT",
        ),
        DefaultLedgerAccountInput(
            account_number="2000-AP",
            name="Accounts Payable",
            account_type="LIABILITY",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="3000-EQUITY",
            name="Retained Earnings",
            account_type="EQUITY",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="4000-REV",
            name="Operating Revenue",
            account_type="INCOME",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="5000-EXP",
            name="Operating Expense",
            account_type="EXPENSE",
            normal_balance="DEBIT",
        ),
    )

    def validate(self) -> None:
        if not isinstance(self.organization_number, str) or not self.organization_number.strip():
            raise ValidationException("organization_number must be a non-empty string")
        if not isinstance(self.organization_name, str) or not self.organization_name.strip():
            raise ValidationException("organization_name must be a non-empty string")
        if not isinstance(self.organization_type, OrganizationType):
            raise ValidationException("organization_type must be OrganizationType")
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValidationException("fiscal_year must be integer >= 2000")
        if self.document_library_number is not None and (
            not isinstance(self.document_library_number, str)
            or not self.document_library_number.strip()
        ):
            raise ValidationException("document_library_number must be a non-empty string when provided")
        if not isinstance(self.document_library_title, str) or not self.document_library_title.strip():
            raise ValidationException("document_library_title must be a non-empty string")
        if not isinstance(self.chart_of_accounts, tuple) or not self.chart_of_accounts:
            raise ValidationException("chart_of_accounts must be a non-empty tuple")


@dataclass(frozen=True, slots=True)
class CompleteOrganizationOnboardingResponse:
    organization_id: UUID
    organization_status: str
    document_library_id: UUID
    fiscal_year_id: UUID
    ledger_account_ids: tuple[UUID, ...]
    completed_steps: tuple[str, ...]


class CompleteOrganizationOnboardingService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CompleteOrganizationOnboardingFeature:
    """Feature facade for complete organization onboarding orchestration."""

    def __init__(self, *, service: CompleteOrganizationOnboardingService) -> None:
        self._service = service

    def execute(self, request: CompleteOrganizationOnboardingRequest) -> CompleteOrganizationOnboardingResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_number=request.organization_number,
                    organization_name=request.organization_name,
                    organization_type=request.organization_type,
                    fiscal_year=request.fiscal_year,
                    document_library_number=request.document_library_number,
                    document_library_title=request.document_library_title,
                    chart_of_accounts=tuple(
                        ServiceLedgerAccountInput(
                            account_number=account.account_number,
                            name=account.name,
                            account_type=account.account_type,
                            normal_balance=account.normal_balance,
                        )
                        for account in request.chart_of_accounts
                    ),
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete organization onboarding feature failed") from exc

        return CompleteOrganizationOnboardingResponse(
            organization_id=service_response.organization_id,
            organization_status=service_response.organization_status,
            document_library_id=service_response.document_library_id,
            fiscal_year_id=service_response.fiscal_year_id,
            ledger_account_ids=service_response.ledger_account_ids,
            completed_steps=service_response.completed_steps,
        )
