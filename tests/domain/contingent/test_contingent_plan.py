from datetime import date
from decimal import Decimal

import pytest

from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.exceptions import (
    InvalidContingentAmountError,
    InvalidContingentDatesError,
    InvalidContingentReferenceError,
    MultipleActiveContingentPlansError,
    OverlappingContingentPlanError,
)
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType


def _membership_type(code: str = "STANDARD") -> MembershipType:
    return MembershipType(code=code, name=code.title())


def _plan(
    *,
    membership_type: MembershipType,
    amount: str = "100.00",
    valid_from: date = date(2026, 1, 1),
    valid_to: date | None = None,
) -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=Money(amount=Decimal(amount), currency=Currency.DKK),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY, due_days=8),
        valid_from=valid_from,
        valid_to=valid_to,
    )


def test_contingent_plan_defaults_and_fields():
    membership_type = _membership_type()

    plan = _plan(membership_type=membership_type)

    assert plan.membership_type == membership_type
    assert plan.membership_type_id == membership_type.id
    assert plan.price.amount == Decimal("100.00")
    assert plan.price.currency == Currency.DKK
    assert plan.invoice_rule.billing_period == BillingPeriod.MONTHLY
    assert plan.invoice_rule.due_days == 8


def test_contingent_plan_rejects_invalid_references():
    with pytest.raises(InvalidContingentReferenceError):
        ContingentPlan(
            membership_type="not-a-membership-type",  # type: ignore[arg-type]
            price=Money(amount=Decimal("10.00"), currency=Currency.DKK),
            invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY),
        )

    with pytest.raises(InvalidContingentReferenceError):
        ContingentPlan(
            membership_type=_membership_type(),
            price="not-money",  # type: ignore[arg-type]
            invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY),
        )

    with pytest.raises(InvalidContingentReferenceError):
        ContingentPlan(
            membership_type=_membership_type(),
            price=Money(amount=Decimal("10.00"), currency=Currency.DKK),
            invoice_rule="monthly",  # type: ignore[arg-type]
        )


def test_contingent_plan_rejects_negative_amount():
    with pytest.raises(InvalidContingentAmountError):
        Money(amount=Decimal("-0.01"), currency=Currency.DKK)


def test_contingent_plan_rejects_invalid_dates():
    with pytest.raises(InvalidContingentDatesError):
        _plan(
            membership_type=_membership_type(),
            valid_from=date(2026, 2, 1),
            valid_to=date(2026, 1, 31),
        )


def test_contingent_plan_active_period_evaluation():
    plan = _plan(
        membership_type=_membership_type(),
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )

    assert plan.is_active_on(date(2026, 1, 1)) is True
    assert plan.is_active_on(date(2026, 6, 1)) is True
    assert plan.is_active_on(date(2025, 12, 31)) is False
    assert plan.is_active_on(date(2027, 1, 1)) is False


def test_membership_type_can_have_historical_contingent_plans_and_single_active():
    membership_type = _membership_type("STANDARD")

    historical = _plan(
        membership_type=membership_type,
        valid_from=date(2025, 1, 1),
        valid_to=date(2025, 12, 31),
    )
    active = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )

    ContingentPlan.ensure_single_active(
        [historical, active],
        membership_type.id,
        at_date=date(2026, 6, 1),
    )


def test_membership_type_rejects_more_than_one_active_contingent_plan():
    membership_type = _membership_type("STANDARD")

    first = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )
    second = _plan(
        membership_type=membership_type,
        amount="120.00",
        valid_from=date(2026, 3, 1),
        valid_to=None,
    )

    with pytest.raises(MultipleActiveContingentPlansError):
        ContingentPlan.ensure_single_active(
            [first, second],
            membership_type.id,
            at_date=date(2026, 6, 1),
        )


def test_contingent_plan_rejects_overlapping_validity_periods():
    membership_type = _membership_type("STANDARD")

    first = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
    )
    second = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 6, 15),
        valid_to=date(2026, 12, 31),
    )

    with pytest.raises(OverlappingContingentPlanError):
        ContingentPlan.ensure_no_overlaps([first, second], membership_type.id)


def test_contingent_plan_allows_adjacent_non_overlapping_validity_periods():
    membership_type = _membership_type("STANDARD")

    first = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
    )
    second = _plan(
        membership_type=membership_type,
        valid_from=date(2026, 7, 1),
        valid_to=date(2026, 12, 31),
    )

    ContingentPlan.ensure_no_overlaps([first, second], membership_type.id)


def test_overlap_checks_are_scoped_to_membership_type():
    standard = _membership_type("STANDARD")
    premium = _membership_type("PREMIUM")

    standard_plan = _plan(
        membership_type=standard,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )
    premium_plan = _plan(
        membership_type=premium,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )

    ContingentPlan.ensure_no_overlaps([standard_plan, premium_plan], standard.id)
    ContingentPlan.ensure_no_overlaps([standard_plan, premium_plan], premium.id)


def test_single_active_is_scoped_to_membership_type():
    standard = _membership_type("STANDARD")
    premium = _membership_type("PREMIUM")

    standard_plan = _plan(membership_type=standard, valid_from=date(2026, 1, 1))
    premium_plan = _plan(membership_type=premium, valid_from=date(2026, 1, 1))

    ContingentPlan.ensure_single_active(
        [standard_plan, premium_plan],
        standard.id,
        at_date=date(2026, 2, 1),
    )
    ContingentPlan.ensure_single_active(
        [standard_plan, premium_plan],
        premium.id,
        at_date=date(2026, 2, 1),
    )
