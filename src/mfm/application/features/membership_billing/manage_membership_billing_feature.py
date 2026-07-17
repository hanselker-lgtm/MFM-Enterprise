"""Feature API for membership fees and billing capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal
from typing import Protocol
from uuid import UUID

from mfm.application.membership_billing.membership_billing_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.membership_billing.membership_billing_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.membership_billing.membership_billing_service import (
    CreateReminderRequest as ServiceReminderRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    MembershipBillingResponse,
)
from mfm.application.membership_billing.membership_billing_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.membership_billing.membership_billing_service import (
    RunMembershipBillingRequest as ServiceRunRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    SetupFeeScheduleRequest as ServiceSetupRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
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


MembershipBillingOperation = Literal["setup-fee", "run-billing", "create-reminder"]


@dataclass(frozen=True, slots=True)
class ManageMembershipBillingRequest:
    operation: MembershipBillingOperation
    membership_type_id: UUID
    membership_type_code: str | None = None
    membership_type_name: str | None = None
    amount: Decimal | None = None
    currency: str | None = None
    due_days: int | None = None
    fiscal_year: int | None = None
    billing_date: date | None = None
    dry_run: bool = False
    member_id: UUID | None = None
    message: str | None = None
    invoice_id: UUID | None = None

    def validate(self) -> None:
        if self.operation not in ("setup-fee", "run-billing", "create-reminder"):
            raise ValidationException("operation must be setup-fee, run-billing or create-reminder")
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be UUID")

        if self.operation == "setup-fee":
            if not isinstance(self.membership_type_code, str) or not self.membership_type_code.strip():
                raise ValidationException("membership_type_code must be non-empty string")
            if not isinstance(self.membership_type_name, str) or not self.membership_type_name.strip():
                raise ValidationException("membership_type_name must be non-empty string")
            if self.amount is None:
                raise ValidationException("amount is required for setup-fee")
            if not isinstance(self.currency, str) or len(self.currency.strip()) != 3:
                raise ValidationException("currency must be 3-letter code")
            if not isinstance(self.due_days, int) or self.due_days < 0:
                raise ValidationException("due_days must be integer >= 0")

        if self.operation == "run-billing":
            if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
                raise ValidationException("fiscal_year must be integer >= 2000")
            if not isinstance(self.billing_date, date):
                raise ValidationException("billing_date must be date")
            if not isinstance(self.dry_run, bool):
                raise ValidationException("dry_run must be bool")

        if self.operation == "create-reminder":
            if not isinstance(self.member_id, UUID):
                raise ValidationException("member_id must be UUID")
            if not isinstance(self.message, str) or not self.message.strip():
                raise ValidationException("message must be non-empty string")
            if not isinstance(self.billing_date, date):
                raise ValidationException("billing_date must be date for reminder due date")
            if self.invoice_id is not None and not isinstance(self.invoice_id, UUID):
                raise ValidationException("invoice_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ManageMembershipBillingResponse:
    result: MembershipBillingResponse


class MembershipBillingServicePort(Protocol):
    def setup_fee_schedule(self, request: ServiceSetupRequest) -> MembershipBillingResponse: ...

    def run_billing(self, request: ServiceRunRequest) -> MembershipBillingResponse: ...

    def create_reminder(self, request: ServiceReminderRequest) -> MembershipBillingResponse: ...


class ManageMembershipBillingFeature:
    """Feature facade for membership fee and billing operations."""

    def __init__(self, *, service: MembershipBillingServicePort) -> None:
        self._service = service

    def execute(self, request: ManageMembershipBillingRequest) -> ManageMembershipBillingResponse:
        request.validate()

        try:
            if request.operation == "setup-fee":
                result = self._service.setup_fee_schedule(
                    ServiceSetupRequest(
                        membership_type_id=request.membership_type_id,
                        membership_type_code=request.membership_type_code,
                        membership_type_name=request.membership_type_name,
                        amount=request.amount,
                        currency=request.currency,
                        due_days=request.due_days,
                    )
                )
                return ManageMembershipBillingResponse(result=result)

            if request.operation == "run-billing":
                result = self._service.run_billing(
                    ServiceRunRequest(
                        membership_type_id=request.membership_type_id,
                        fiscal_year=request.fiscal_year,
                        billing_date=request.billing_date,
                        dry_run=request.dry_run,
                    )
                )
                return ManageMembershipBillingResponse(result=result)

            result = self._service.create_reminder(
                ServiceReminderRequest(
                    membership_type_id=request.membership_type_id,
                    member_id=request.member_id,
                    message=request.message,
                    due_date=request.billing_date,
                    invoice_id=request.invoice_id,
                )
            )
            return ManageMembershipBillingResponse(result=result)
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Manage membership billing feature failed") from exc
