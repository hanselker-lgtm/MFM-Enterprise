from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import uuid4

from mfm.application.reporting.membership_billing_summary_service import (
    MembershipBillingSummaryRequest,
)
from mfm.application.reporting.membership_billing_summary_service import (
    MembershipBillingSummaryService,
)
from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingRun
from mfm.domain.membership_billing.membership_fee import MembershipFee


class InMemoryRepository:
    def __init__(self, profiles: list[MembershipBillingProfile]) -> None:
        self.profiles = profiles

    def list(self) -> list[MembershipBillingProfile]:
        return self.profiles


def test_summary_service_returns_profile_metrics() -> None:
    fee = MembershipFee(
        membership_type_id=uuid4(),
        membership_type_code="GEN",
        membership_type_name="General",
        amount=Decimal("1200.00"),
        currency="DKK",
    )
    profile = MembershipBillingProfile(
        membership_type_id=fee.membership_type_id,
        fee_schedule=FeeSchedule(membership_fee=fee, due_days=14),
        runs=[
            MembershipBillingRun(
                fiscal_year=2026,
                billing_date=date(2026, 1, 1),
                processed=6,
                invoices_created=5,
                journals_created=5,
                skipped=1,
            )
        ],
    )
    service = MembershipBillingSummaryService(repository=InMemoryRepository([profile]))

    response = service.execute(MembershipBillingSummaryRequest())

    assert len(response.profiles) == 1
    assert response.profiles[0].membership_type_code == "GEN"
    assert response.profiles[0].last_run_invoices_created == 5
