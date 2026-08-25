from __future__ import annotations
from datetime import date
from decimal import Decimal
from uuid import UUID

import pytest

from mfm.application.contingent.create_contingent_plan_use_case import (
    CreateContingentPlanUseCase,
)
from mfm.application.contingent.update_contingent_plan_use_case import (
    UpdateContingentPlanUseCase,
)
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.exceptions import (
    ContingentPlanNotFoundError,
    OverlappingContingentPlanError,
)
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.contingent_plan_repository import ContingentPlanRepository


class InMemoryContingentPlanRepository(ContingentPlanRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, ContingentPlan] = {}

    def add(self, plan: ContingentPlan) -> None:
        self._items[plan.id] = plan

    def update(self, plan: ContingentPlan) -> None:
        self._items[plan.id] = plan

    def get(self, plan_id: UUID) -> ContingentPlan | None:
        return self._items.get(plan_id)

    def list(self) -> list[ContingentPlan]:
        return list(self._items.values())

    def list_by_membership_type(self, membership_type_id: UUID) -> list[ContingentPlan]:
        return [
            item
            for item in self._items.values()
            if item.membership_type_id == membership_type_id
        ]

    def exists(self, plan_id: UUID) -> bool:
        return plan_id in self._items

    def delete(self, plan_id: UUID) -> None:
        self._items.pop(plan_id, None)


def _membership_type(code: str = "STANDARD") -> MembershipType:
    return MembershipType(code=code, name=code.title())


def _plan(
    *,
    membership_type: MembershipType,
    amount: str,
    valid_from: date,
    valid_to: date | None,
) -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=Money(amount=Decimal(amount), currency=Currency.DKK),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY, due_days=8),
        valid_from=valid_from,
        valid_to=valid_to,
    )


def test_create_contingent_plan_use_case_success_for_historical_prices():
    repository = InMemoryContingentPlanRepository()
    use_case = CreateContingentPlanUseCase(repository)
    membership_type = _membership_type("STANDARD")

    old_plan = _plan(
        membership_type=membership_type,
        amount="100.00",
        valid_from=date(2025, 1, 1),
        valid_to=date(2025, 12, 31),
    )
    new_plan = _plan(
        membership_type=membership_type,
        amount="120.00",
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )

    use_case.execute(old_plan)
    created = use_case.execute(new_plan)

    assert created.id == new_plan.id
    assert len(repository.list_by_membership_type(membership_type.id)) == 2


def test_create_contingent_plan_use_case_rejects_overlapping_periods():
    repository = InMemoryContingentPlanRepository()
    use_case = CreateContingentPlanUseCase(repository)
    membership_type = _membership_type("STANDARD")

    first = _plan(
        membership_type=membership_type,
        amount="100.00",
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 6, 30),
    )
    second = _plan(
        membership_type=membership_type,
        amount="110.00",
        valid_from=date(2026, 6, 1),
        valid_to=date(2026, 12, 31),
    )

    use_case.execute(first)

    with pytest.raises(OverlappingContingentPlanError):
        use_case.execute(second)


def test_create_contingent_plan_use_case_rejects_open_ended_overlap():
    repository = InMemoryContingentPlanRepository()
    use_case = CreateContingentPlanUseCase(repository)
    membership_type = _membership_type("STANDARD")

    first = _plan(
        membership_type=membership_type,
        amount="100.00",
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )
    second = _plan(
        membership_type=membership_type,
        amount="110.00",
        valid_from=date(2026, 2, 1),
        valid_to=None,
    )

    use_case.execute(first)

    with pytest.raises(OverlappingContingentPlanError):
        use_case.execute(second)


def test_update_contingent_plan_use_case_success():
    repository = InMemoryContingentPlanRepository()
    use_case = UpdateContingentPlanUseCase(repository)
    membership_type = _membership_type("STANDARD")

    plan = _plan(
        membership_type=membership_type,
        amount="100.00",
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )
    repository.add(plan)

    updated_plan = ContingentPlan(
        id=plan.id,
        membership_type=membership_type,
        price=Money(amount=Decimal("130.00"), currency=Currency.DKK),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY, due_days=14),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )

    result = use_case.execute(updated_plan)

    assert result.price.amount == Decimal("130.00")
    assert repository.get(plan.id) is not None


def test_update_contingent_plan_use_case_rejects_missing_plan():
    repository = InMemoryContingentPlanRepository()
    use_case = UpdateContingentPlanUseCase(repository)
    membership_type = _membership_type("STANDARD")

    plan = _plan(
        membership_type=membership_type,
        amount="100.00",
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )

    with pytest.raises(ContingentPlanNotFoundError):
        use_case.execute(plan)
