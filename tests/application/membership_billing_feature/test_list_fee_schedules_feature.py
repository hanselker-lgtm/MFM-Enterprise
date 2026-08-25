from __future__ import annotations

from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.application.features.membership_billing import (
    ListFeeSchedulesFeature,
    ListFeeSchedulesRequest,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_fee import MembershipFee


class InMemoryMembershipBillingRepository:
    def __init__(self, store: dict[UUID, MembershipBillingProfile]) -> None:
        self._store = store

    def get(self, membership_type_id: UUID):
        return self._store.get(membership_type_id)

    def save(self, profile: MembershipBillingProfile) -> None:
        self._store[profile.membership_type_id] = profile

    def list(self):
        return list(self._store.values())


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        super().__init__()
        self._profiles: dict[UUID, MembershipBillingProfile] = {}

    def _start_scope(self) -> None:
        self.membership_billing_repository = InMemoryMembershipBillingRepository(self._profiles)

    def _commit_impl(self) -> None:
        pass

    def _rollback_impl(self) -> None:
        pass

    def _flush_impl(self) -> None:
        pass

    def _close_impl(self) -> None:
        pass


def test_list_fee_schedules_returns_empty_when_none_configured() -> None:
    uow = FakeUnitOfWork()
    response = ListFeeSchedulesFeature(unit_of_work=uow).execute(ListFeeSchedulesRequest())
    assert response.fee_schedules == ()


def test_list_fee_schedules_returns_configured_schedules() -> None:
    uow = FakeUnitOfWork()
    membership_type_id = uuid4()
    with uow:
        uow.membership_billing_repository.save(
            MembershipBillingProfile(
                membership_type_id=membership_type_id,
                fee_schedule=FeeSchedule(
                    membership_fee=MembershipFee(
                        membership_type_id=membership_type_id,
                        membership_type_code="STD",
                        membership_type_name="Standard",
                        amount=Decimal("250.00"),
                        currency="DKK",
                    ),
                    due_days=30,
                ),
            )
        )

    response = ListFeeSchedulesFeature(unit_of_work=uow).execute(ListFeeSchedulesRequest())

    assert len(response.fee_schedules) == 1
    assert response.fee_schedules[0].membership_type_code == "STD"
    assert response.fee_schedules[0].fee_amount == "250.00"
