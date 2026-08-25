"""Mapper between domain contingent plans and persistence rows."""

from __future__ import annotations

from mfm.database.models.contingent_plan_model import ContingentPlanModel
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType


class ContingentPlanMapper:
    """Map between ContingentPlan domain entities and ORM rows."""

    @staticmethod
    def to_orm(plan: ContingentPlan) -> ContingentPlanModel:
        return ContingentPlanModel(
            id=plan.id,
            membership_type_id=plan.membership_type_id,
            amount=plan.price.amount,
            currency=plan.price.currency,
            billing_period=plan.invoice_rule.billing_period,
            due_days=plan.invoice_rule.due_days,
            prorate_on_start=plan.invoice_rule.prorate_on_start,
            valid_from=plan.valid_from,
            valid_to=plan.valid_to,
        )

    @staticmethod
    def to_domain(orm: ContingentPlanModel, membership_type: MembershipType) -> ContingentPlan:
        return ContingentPlan(
            id=orm.id,
            membership_type=membership_type,
            price=Money(amount=orm.amount, currency=orm.currency),
            invoice_rule=InvoiceRule(
                billing_period=orm.billing_period,
                due_days=orm.due_days,
                prorate_on_start=orm.prorate_on_start,
            ),
            valid_from=orm.valid_from,
            valid_to=orm.valid_to,
        )
