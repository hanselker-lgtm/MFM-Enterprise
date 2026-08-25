from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.domain.finance.billing_period import BillingPeriod
from mfm.domain.finance.contingent_plan import ContingentPlan
from mfm.domain.finance.contingent_plan_id import ContingentPlanId
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import InvalidContingentPlanAmountError
from mfm.domain.finance.exceptions import InvalidContingentPlanDatesError
from mfm.domain.finance.exceptions import InvalidContingentPlanReferenceError
from mfm.domain.finance.exceptions import MultipleActiveContingentPlansError
from mfm.domain.finance.exceptions import OverlappingContingentPlanError
from mfm.domain.finance.money import Money


def _plan(
    *,
    membership_type_id=None,
    amount: str = "199.00",
    billing_period: BillingPeriod = BillingPeriod.MONTHLY,
    valid_from: date = date(2026, 1, 1),
    valid_to: date | None = date(2026, 12, 31),
    active: bool = False,
) -> ContingentPlan:
    return ContingentPlan(
        membership_type_id=membership_type_id or uuid4(),
        amount=Money(amount=Decimal(amount), currency=Currency.DKK),
        billing_period=billing_period,
        valid_from=valid_from,
        valid_to=valid_to,
        active=active,
    )


def test_valid_construction():
    membership_type_id = uuid4()
    plan = _plan(membership_type_id=membership_type_id)

    assert isinstance(plan.id, ContingentPlanId)
    assert plan.membership_type_id == membership_type_id
    assert plan.amount.amount == Decimal("199.00")
    assert plan.billing_period == BillingPeriod.MONTHLY
    assert plan.valid_from == date(2026, 1, 1)
    assert plan.valid_to == date(2026, 12, 31)
    assert plan.active is False


def test_invalid_amount():
    with pytest.raises(InvalidContingentPlanAmountError):
        _plan(amount="0.00")


def test_invalid_dates_when_from_is_not_before_to():
    with pytest.raises(InvalidContingentPlanDatesError):
        _plan(valid_from=date(2026, 1, 1), valid_to=date(2026, 1, 1))

    with pytest.raises(InvalidContingentPlanDatesError):
        _plan(valid_from=date(2026, 2, 1), valid_to=date(2026, 1, 31))


def test_lifetime_memberships_must_not_have_end_date():
    with pytest.raises(InvalidContingentPlanDatesError):
        _plan(
            billing_period=BillingPeriod.LIFETIME,
            valid_to=date(2099, 1, 1),
        )

    plan = _plan(billing_period=BillingPeriod.LIFETIME, valid_to=None)
    assert plan.valid_to is None


def test_overlap_detection_same_membership_type():
    membership_type_id = uuid4()
    first = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
    )
    second = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 6, 15),
        valid_to=date(2026, 12, 31),
    )

    assert first.overlaps(second) is True


def test_overlap_detection_is_scoped_to_membership_type():
    first = _plan(
        membership_type_id=uuid4(),
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
    )
    second = _plan(
        membership_type_id=uuid4(),
        valid_from=date(2026, 3, 1),
        valid_to=date(2026, 5, 1),
    )

    assert first.overlaps(second) is False


def test_activate_and_deactivate():
    plan = _plan(active=False)

    plan.activate()
    assert plan.active is True

    plan.deactivate()
    assert plan.active is False


def test_is_valid_respects_interval_boundaries():
    plan = _plan(valid_from=date(2026, 1, 1), valid_to=date(2026, 12, 31))

    assert plan.is_valid(date(2025, 12, 31)) is False
    assert plan.is_valid(date(2026, 1, 1)) is True
    assert plan.is_valid(date(2026, 6, 1)) is True
    assert plan.is_valid(date(2026, 12, 30)) is True
    assert plan.is_valid(date(2026, 12, 31)) is False


def test_replace_with_switches_active_plan_without_overlap():
    membership_type_id = uuid4()
    current = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
        active=True,
    )
    replacement = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 6, 30),
        valid_to=date(2026, 12, 31),
        active=False,
    )

    current.replace_with(replacement)

    assert current.active is False
    assert replacement.active is True


def test_replace_with_rejects_overlap():
    membership_type_id = uuid4()
    current = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 7, 1),
        active=True,
    )
    replacement = _plan(
        membership_type_id=membership_type_id,
        valid_from=date(2026, 6, 1),
        valid_to=date(2026, 12, 31),
        active=False,
    )

    with pytest.raises(OverlappingContingentPlanError):
        current.replace_with(replacement)


def test_replace_with_requires_same_membership_type():
    current = _plan(membership_type_id=uuid4(), active=True)
    replacement = _plan(membership_type_id=uuid4(), active=False)

    with pytest.raises(InvalidContingentPlanReferenceError):
        current.replace_with(replacement)


def test_only_one_active_plan_per_membership_type():
    membership_type_id = uuid4()
    first = _plan(membership_type_id=membership_type_id, active=True)
    second = _plan(membership_type_id=membership_type_id, active=True)

    with pytest.raises(MultipleActiveContingentPlansError):
        ContingentPlan.ensure_single_active([first, second], membership_type_id)


def test_contingent_plan_id_accepts_uuid_and_string():
    value = uuid4()

    direct = ContingentPlanId(value=value)
    from_string = ContingentPlanId(value=str(value))

    assert direct.value == value
    assert from_string.value == value


def test_contingent_plan_id_rejects_invalid_values():
    with pytest.raises(InvalidContingentPlanReferenceError):
        ContingentPlanId(value="not-a-uuid")

    with pytest.raises(InvalidContingentPlanReferenceError):
        ContingentPlanId(value=123)  # type: ignore[arg-type]
