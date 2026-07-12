from datetime import date
from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.database.repositories.sqlite_contingent_plan_repository import (
    SQLiteContingentPlanRepository,
)
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType


def _create_session():
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _create_membership_type(session: Session, code: str = "STANDARD") -> MembershipType:
    membership_type = MembershipType(code=code, name=code.title())
    session.add(
        MembershipTypeModel(
            id=membership_type.id,
            code=membership_type.code,
            name=membership_type.name,
            description=membership_type.description,
            is_active=membership_type.is_active,
        )
    )
    session.flush()
    return membership_type


def _plan(membership_type: MembershipType, amount: str = "100.00") -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=Money(amount=Decimal(amount), currency=Currency.DKK),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY, due_days=8),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )


def test_contingent_plan_repository_persists_and_reads_plan():
    engine, session = _create_session()
    try:
        membership_type = _create_membership_type(session)
        repository = SQLiteContingentPlanRepository(session)

        plan = _plan(membership_type)
        repository.add(plan)
        session.commit()

        stored = repository.get(plan.id)
        assert stored is not None
        assert stored.membership_type_id == membership_type.id
        assert stored.price.amount == Decimal("100.00")
    finally:
        session.close()
        engine.dispose()


def test_contingent_plan_repository_supports_list_exists_delete():
    engine, session = _create_session()
    try:
        membership_type = _create_membership_type(session)
        repository = SQLiteContingentPlanRepository(session)

        plan = _plan(membership_type)
        repository.add(plan)
        session.commit()

        assert repository.exists(plan.id) is True
        assert len(repository.list()) == 1
        assert len(repository.list_by_membership_type(membership_type.id)) == 1

        repository.delete(plan.id)
        session.commit()

        assert repository.exists(plan.id) is False
        assert repository.get(plan.id) is None
    finally:
        session.close()
        engine.dispose()


def test_contingent_plan_repository_updates_fields():
    engine, session = _create_session()
    try:
        membership_type = _create_membership_type(session)
        repository = SQLiteContingentPlanRepository(session)

        plan = _plan(membership_type)
        repository.add(plan)
        session.commit()

        updated = ContingentPlan(
            id=plan.id,
            membership_type=membership_type,
            price=Money(amount=Decimal("140.00"), currency=Currency.EUR),
            invoice_rule=InvoiceRule(
                billing_period=BillingPeriod.YEARLY,
                due_days=20,
                prorate_on_start=False,
            ),
            valid_from=date(2026, 1, 1),
            valid_to=date(2026, 12, 31),
        )

        repository.update(updated)
        session.commit()

        stored = repository.get(plan.id)
        assert stored is not None
        assert stored.price.amount == Decimal("140.00")
        assert stored.price.currency == Currency.EUR
        assert stored.invoice_rule.billing_period == BillingPeriod.YEARLY
        assert stored.invoice_rule.due_days == 20
        assert stored.invoice_rule.prorate_on_start is False
    finally:
        session.close()
        engine.dispose()


def test_contingent_plan_repository_update_rejects_missing_plan():
    engine, session = _create_session()
    try:
        membership_type = _create_membership_type(session)
        repository = SQLiteContingentPlanRepository(session)

        with pytest.raises(ValueError):
            repository.update(_plan(membership_type))
    finally:
        session.close()
        engine.dispose()
