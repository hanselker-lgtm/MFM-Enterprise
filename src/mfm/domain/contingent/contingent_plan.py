"""Contingent plan domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from mfm.domain.contingent.exceptions import (
    InvalidContingentDatesError,
    InvalidContingentReferenceError,
    MultipleActiveContingentPlansError,
    OverlappingContingentPlanError,
)
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType


@dataclass(slots=True)
class ContingentPlan:
    """Domain entity representing price and validity for a membership type."""

    membership_type: MembershipType
    price: Money
    invoice_rule: InvoiceRule
    valid_from: date = field(default_factory=lambda: datetime.now(UTC).date())
    valid_to: date | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise InvalidContingentReferenceError("id must be a UUID")

        if not isinstance(self.membership_type, MembershipType):
            raise InvalidContingentReferenceError(
                "membership_type must be a MembershipType"
            )

        if not isinstance(self.price, Money):
            raise InvalidContingentReferenceError("price must be a Money")

        if not isinstance(self.invoice_rule, InvoiceRule):
            raise InvalidContingentReferenceError(
                "invoice_rule must be an InvoiceRule"
            )

        if self.valid_to is not None and self.valid_to < self.valid_from:
            raise InvalidContingentDatesError(
                "valid_to cannot be before valid_from"
            )

    @property
    def amount(self):
        """Compatibility access to price amount."""

        return self.price.amount

    @property
    def currency(self):
        """Compatibility access to price currency."""

        return self.price.currency

    @property
    def billing_period(self):
        """Compatibility access to invoice rule billing period."""

        return self.invoice_rule.billing_period

    @property
    def membership_type_id(self) -> UUID:
        return self.membership_type.id

    def is_active_on(self, at_date: date | None = None) -> bool:
        target_date = at_date or datetime.now(UTC).date()

        if target_date < self.valid_from:
            return False

        if self.valid_to is not None and target_date > self.valid_to:
            return False

        return True

    @staticmethod
    def ensure_single_active(
        plans: list["ContingentPlan"],
        membership_type_id: UUID,
        *,
        at_date: date | None = None,
    ) -> None:
        active_count = sum(
            1
            for plan in plans
            if plan.membership_type_id == membership_type_id
            and plan.is_active_on(at_date)
        )

        if active_count > 1:
            raise MultipleActiveContingentPlansError(
                f"Membership type {membership_type_id} cannot have more than one active contingent plan"
            )

    @staticmethod
    def ensure_no_overlaps(
        plans: list["ContingentPlan"],
        membership_type_id: UUID,
    ) -> None:
        relevant = [
            plan for plan in plans if plan.membership_type_id == membership_type_id
        ]

        for index, first in enumerate(relevant):
            for second in relevant[index + 1 :]:
                if _periods_overlap(
                    first.valid_from,
                    first.valid_to,
                    second.valid_from,
                    second.valid_to,
                ):
                    raise OverlappingContingentPlanError(
                        f"Contingent plan periods overlap for membership type {membership_type_id}"
                    )


def _periods_overlap(
    start_a: date,
    end_a: date | None,
    start_b: date,
    end_b: date | None,
) -> bool:
    normalized_end_a = end_a or date.max
    normalized_end_b = end_b or date.max
    return start_a <= normalized_end_b and start_b <= normalized_end_a
