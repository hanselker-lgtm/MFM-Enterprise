"""ListFeeSchedulesFeature: list configured membership fee schedules.

``ManageMembershipBillingFeature`` covers setup/run/reminder
operations but has no read-only listing operation of its own; this
fills that gap so a UI can show what's already configured.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class FeeScheduleDTO:
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    fee_amount: str
    currency: str
    due_days: int
    billing_period: str
    active: bool
    reminder_count: int
    run_count: int


@dataclass(frozen=True, slots=True)
class ListFeeSchedulesRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListFeeSchedulesResponse:
    fee_schedules: tuple[FeeScheduleDTO, ...]


class ListFeeSchedulesFeature:
    """Public application entry point for listing membership fee schedules."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListFeeSchedulesRequest) -> ListFeeSchedulesResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                profiles = uow.membership_billing_repository.list()
        except Exception as exc:
            raise RepositoryException("List fee schedules feature failed") from exc

        return ListFeeSchedulesResponse(
            fee_schedules=tuple(
                FeeScheduleDTO(
                    membership_type_id=profile.membership_type_id,
                    membership_type_code=profile.fee_schedule.membership_fee.membership_type_code,
                    membership_type_name=profile.fee_schedule.membership_fee.membership_type_name,
                    fee_amount=str(profile.fee_schedule.membership_fee.amount),
                    currency=profile.fee_schedule.membership_fee.currency,
                    due_days=profile.fee_schedule.due_days,
                    billing_period=profile.fee_schedule.billing_period,
                    active=profile.fee_schedule.active,
                    reminder_count=len(profile.reminders),
                    run_count=len(profile.runs),
                )
                for profile in profiles
            )
        )
