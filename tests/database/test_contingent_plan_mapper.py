from datetime import date
from decimal import Decimal

from mfm.database.mappers.contingent_plan_mapper import ContingentPlanMapper
from mfm.database.models.contingent_plan_model import ContingentPlanModel
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType


def test_contingent_plan_mapper_domain_to_orm_and_back():
    membership_type = MembershipType(code="STANDARD", name="Standard")
    plan = ContingentPlan(
        membership_type=membership_type,
        price=Money(amount=Decimal("199.00"), currency=Currency.DKK),
        invoice_rule=InvoiceRule(
            billing_period=BillingPeriod.MONTHLY,
            due_days=10,
            prorate_on_start=True,
        ),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )

    orm = ContingentPlanMapper.to_orm(plan)

    assert isinstance(orm, ContingentPlanModel)
    assert orm.id == plan.id
    assert orm.membership_type_id == membership_type.id
    assert orm.amount == Decimal("199.00")
    assert orm.currency == Currency.DKK
    assert orm.billing_period == BillingPeriod.MONTHLY
    assert orm.due_days == 10
    assert orm.prorate_on_start is True

    round_tripped = ContingentPlanMapper.to_domain(orm, membership_type)

    assert round_tripped.id == plan.id
    assert round_tripped.membership_type_id == membership_type.id
    assert round_tripped.price.amount == Decimal("199.00")
    assert round_tripped.price.currency == Currency.DKK
    assert round_tripped.invoice_rule.billing_period == BillingPeriod.MONTHLY
    assert round_tripped.invoice_rule.due_days == 10
