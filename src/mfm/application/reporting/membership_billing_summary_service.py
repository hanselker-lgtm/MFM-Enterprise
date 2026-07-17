"""Reporting service for membership billing capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol

from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryItemDTO,
)
from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryResponse,
)
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class MembershipBillingSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


class MembershipBillingRepositoryPort(Protocol):
    def list(self) -> list[MembershipBillingProfile]: ...


class MembershipBillingSummaryService:
    """Build summary metrics from membership billing profiles."""

    def __init__(self, *, repository: MembershipBillingRepositoryPort) -> None:
        self._repository = repository

    def execute(self, request: MembershipBillingSummaryRequest) -> MembershipBillingSummaryResponse:
        request.validate()

        try:
            profiles = self._repository.list()
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Membership billing summary retrieval failed") from exc

        items: list[MembershipBillingSummaryItemDTO] = []
        for profile in profiles:
            if not request.include_inactive and not profile.fee_schedule.active:
                continue

            last_run = profile.runs[-1] if profile.runs else None
            items.append(
                MembershipBillingSummaryItemDTO(
                    membership_type_code=profile.fee_schedule.membership_fee.membership_type_code,
                    membership_type_name=profile.fee_schedule.membership_fee.membership_type_name,
                    currency=profile.fee_schedule.membership_fee.currency,
                    fee_amount=str(profile.fee_schedule.membership_fee.amount),
                    due_days=profile.fee_schedule.due_days,
                    reminders=len(profile.reminders),
                    last_run_processed=(last_run.processed if last_run else 0),
                    last_run_invoices_created=(last_run.invoices_created if last_run else 0),
                )
            )

        return MembershipBillingSummaryResponse(
            profiles=tuple(items),
            generated_at=datetime.now(UTC),
        )
