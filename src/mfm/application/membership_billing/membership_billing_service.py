"""Application service for membership fees and billing capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.features.annual_contingent_generation import (
    CreateAnnualContingentRequest,
)
from mfm.application.features.annual_contingent_generation import (
    CreateAnnualContingentResponse,
)
from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingRun
from mfm.domain.membership_billing.membership_fee import MembershipFee
from mfm.domain.membership_billing.reminder import Reminder


class ApplicationException(Exception):
    """Base exception for membership billing service failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class SetupFeeScheduleRequest:
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    amount: Decimal
    currency: str
    due_days: int

    def validate(self) -> None:
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be UUID")
        if not isinstance(self.membership_type_code, str) or not self.membership_type_code.strip():
            raise ValidationException("membership_type_code must be non-empty string")
        if not isinstance(self.membership_type_name, str) or not self.membership_type_name.strip():
            raise ValidationException("membership_type_name must be non-empty string")
        if not isinstance(self.currency, str) or len(self.currency.strip()) != 3:
            raise ValidationException("currency must be 3-letter code")
        if not isinstance(self.due_days, int) or self.due_days < 0:
            raise ValidationException("due_days must be integer >= 0")


@dataclass(frozen=True, slots=True)
class RunMembershipBillingRequest:
    membership_type_id: UUID
    fiscal_year: int
    billing_date: date
    dry_run: bool = False

    def validate(self) -> None:
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be UUID")
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValidationException("fiscal_year must be integer >= 2000")
        if not isinstance(self.billing_date, date):
            raise ValidationException("billing_date must be date")
        if not isinstance(self.dry_run, bool):
            raise ValidationException("dry_run must be bool")


@dataclass(frozen=True, slots=True)
class CreateReminderRequest:
    membership_type_id: UUID
    member_id: UUID
    message: str
    due_date: date
    invoice_id: UUID | None = None

    def validate(self) -> None:
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be UUID")
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")
        if self.invoice_id is not None and not isinstance(self.invoice_id, UUID):
            raise ValidationException("invoice_id must be UUID or None")
        if not isinstance(self.message, str) or not self.message.strip():
            raise ValidationException("message must be non-empty string")
        if not isinstance(self.due_date, date):
            raise ValidationException("due_date must be date")


@dataclass(frozen=True, slots=True)
class MembershipBillingResponse:
    membership_type_id: UUID
    fee_amount: str
    currency: str
    due_days: int
    run_processed: int
    run_invoices_created: int
    reminder_count: int
    generated_at: datetime


class MembershipBillingRepositoryPort(Protocol):
    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None: ...

    def save(self, profile: MembershipBillingProfile) -> None: ...


class AnnualContingentFeaturePort(Protocol):
    def execute(self, request: CreateAnnualContingentRequest) -> CreateAnnualContingentResponse: ...


class MembershipBillingService:
    """Manage membership fee schedule and billing orchestration."""

    def __init__(
        self,
        *,
        repository: MembershipBillingRepositoryPort,
        annual_contingent_feature: AnnualContingentFeaturePort,
    ) -> None:
        self._repository = repository
        self._annual_contingent_feature = annual_contingent_feature

    def setup_fee_schedule(self, request: SetupFeeScheduleRequest) -> MembershipBillingResponse:
        request.validate()

        try:
            fee = MembershipFee(
                membership_type_id=request.membership_type_id,
                membership_type_code=request.membership_type_code,
                membership_type_name=request.membership_type_name,
                amount=request.amount,
                currency=request.currency,
            )
            schedule = FeeSchedule(
                membership_fee=fee,
                due_days=request.due_days,
                billing_period="YEARLY",
                active=True,
            )

            existing = self._repository.get(request.membership_type_id)
            if existing is None:
                profile = MembershipBillingProfile(
                    membership_type_id=request.membership_type_id,
                    fee_schedule=schedule,
                )
            else:
                profile = existing
                profile.fee_schedule = schedule

            self._repository.save(profile)

            return MembershipBillingResponse(
                membership_type_id=profile.membership_type_id,
                fee_amount=str(profile.fee_schedule.membership_fee.amount),
                currency=profile.fee_schedule.membership_fee.currency,
                due_days=profile.fee_schedule.due_days,
                run_processed=(profile.runs[-1].processed if profile.runs else 0),
                run_invoices_created=(profile.runs[-1].invoices_created if profile.runs else 0),
                reminder_count=len(profile.reminders),
                generated_at=datetime.now(UTC),
            )
        except ValidationException:
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Setup fee schedule failed") from exc

    def run_billing(self, request: RunMembershipBillingRequest) -> MembershipBillingResponse:
        request.validate()

        try:
            profile = self._repository.get(request.membership_type_id)
            if profile is None:
                raise BusinessRuleViolation(
                    f"Fee schedule for membership type {request.membership_type_id} not found"
                )

            run_result = self._annual_contingent_feature.execute(
                CreateAnnualContingentRequest(
                    fiscal_year=request.fiscal_year,
                    billing_date=request.billing_date,
                    membership_type_id=request.membership_type_id,
                    dry_run=request.dry_run,
                )
            )

            profile.add_run(
                MembershipBillingRun(
                    fiscal_year=request.fiscal_year,
                    billing_date=request.billing_date,
                    processed=run_result.processed,
                    invoices_created=run_result.invoices_created,
                    journals_created=run_result.journal_drafts_created,
                    skipped=run_result.skipped,
                    errors=run_result.errors,
                )
            )
            self._repository.save(profile)

            return MembershipBillingResponse(
                membership_type_id=profile.membership_type_id,
                fee_amount=str(profile.fee_schedule.membership_fee.amount),
                currency=profile.fee_schedule.membership_fee.currency,
                due_days=profile.fee_schedule.due_days,
                run_processed=run_result.processed,
                run_invoices_created=run_result.invoices_created,
                reminder_count=len(profile.reminders),
                generated_at=datetime.now(UTC),
            )
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Run membership billing failed") from exc

    def create_reminder(self, request: CreateReminderRequest) -> MembershipBillingResponse:
        request.validate()

        try:
            profile = self._repository.get(request.membership_type_id)
            if profile is None:
                raise BusinessRuleViolation(
                    f"Fee schedule for membership type {request.membership_type_id} not found"
                )

            profile.add_reminder(
                Reminder(
                    member_id=request.member_id,
                    message=request.message,
                    due_date=request.due_date,
                    invoice_id=request.invoice_id,
                )
            )
            self._repository.save(profile)

            latest_run = profile.runs[-1] if profile.runs else None
            return MembershipBillingResponse(
                membership_type_id=profile.membership_type_id,
                fee_amount=str(profile.fee_schedule.membership_fee.amount),
                currency=profile.fee_schedule.membership_fee.currency,
                due_days=profile.fee_schedule.due_days,
                run_processed=(latest_run.processed if latest_run else 0),
                run_invoices_created=(latest_run.invoices_created if latest_run else 0),
                reminder_count=len(profile.reminders),
                generated_at=datetime.now(UTC),
            )
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create reminder failed") from exc
