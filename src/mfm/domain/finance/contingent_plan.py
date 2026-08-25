"""Contingent plan aggregate for finance domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.finance.billing_period import BillingPeriod
from mfm.domain.finance.contingent_plan_id import ContingentPlanId
from mfm.domain.finance.exceptions import InvalidContingentPlanAmountError
from mfm.domain.finance.exceptions import InvalidContingentPlanDatesError
from mfm.domain.finance.exceptions import InvalidContingentPlanReferenceError
from mfm.domain.finance.exceptions import MultipleActiveContingentPlansError
from mfm.domain.finance.exceptions import OverlappingContingentPlanError
from mfm.domain.finance.money import Money


@dataclass(slots=True)
class ContingentPlan(AggregateRoot):
    """Aggregate root representing a membership contingent plan."""

    membership_type_id: UUID
    amount: Money
    billing_period: BillingPeriod
    valid_from: date
    valid_to: date | None = None
    active: bool = False
    id: ContingentPlanId = field(default_factory=ContingentPlanId.new)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, ContingentPlanId):
            raise InvalidContingentPlanReferenceError("id must be a ContingentPlanId")

        if not isinstance(self.membership_type_id, UUID):
            raise InvalidContingentPlanReferenceError(
                "membership_type_id must be a UUID"
            )

        if not isinstance(self.amount, Money):
            raise InvalidContingentPlanReferenceError("amount must be Money")

        if self.amount.amount <= 0:
            raise InvalidContingentPlanAmountError("amount must be greater than zero")

        if not isinstance(self.billing_period, BillingPeriod):
            raise InvalidContingentPlanReferenceError(
                "billing_period must be a BillingPeriod"
            )

        if not isinstance(self.valid_from, date):
            raise InvalidContingentPlanDatesError("valid_from must be a date")

        if self.valid_to is not None and not isinstance(self.valid_to, date):
            raise InvalidContingentPlanDatesError("valid_to must be a date or None")

        if self.valid_to is not None and self.valid_from >= self.valid_to:
            raise InvalidContingentPlanDatesError("valid_from must be before valid_to")

        if self.billing_period == BillingPeriod.LIFETIME and self.valid_to is not None:
            raise InvalidContingentPlanDatesError(
                "Lifetime billing period must not have an end date"
            )

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def is_valid(self, at_date: date) -> bool:
        if at_date < self.valid_from:
            return False

        if self.valid_to is not None and at_date >= self.valid_to:
            return False

        return True

    def overlaps(self, other: "ContingentPlan") -> bool:
        if not isinstance(other, ContingentPlan):
            raise InvalidContingentPlanReferenceError("other must be a ContingentPlan")

        if self.membership_type_id != other.membership_type_id:
            return False

        end_a = self.valid_to or date.max
        end_b = other.valid_to or date.max
        return self.valid_from < end_b and other.valid_from < end_a

    def replace_with(self, new_plan: "ContingentPlan") -> None:
        if not isinstance(new_plan, ContingentPlan):
            raise InvalidContingentPlanReferenceError(
                "new_plan must be a ContingentPlan"
            )

        if self.membership_type_id != new_plan.membership_type_id:
            raise InvalidContingentPlanReferenceError(
                "new_plan must target the same membership_type_id"
            )

        if self.overlaps(new_plan):
            raise OverlappingContingentPlanError(
                "replacement plan validity periods must not overlap"
            )

        self.deactivate()
        new_plan.activate()

    @staticmethod
    def ensure_single_active(plans: list["ContingentPlan"], membership_type_id: UUID) -> None:
        active_count = sum(
            1
            for plan in plans
            if plan.membership_type_id == membership_type_id and plan.active
        )

        if active_count > 1:
            raise MultipleActiveContingentPlansError(
                f"Membership type {membership_type_id} cannot have more than one active contingent plan"
            )
