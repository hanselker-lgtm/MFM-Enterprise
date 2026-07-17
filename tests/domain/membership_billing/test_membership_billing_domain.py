from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingRun
from mfm.domain.membership_billing.membership_fee import MembershipFee
from mfm.domain.membership_billing.reminder import Reminder


def _membership_fee() -> MembershipFee:
    return MembershipFee(
        membership_type_id=uuid4(),
        membership_type_code="GEN",
        membership_type_name="General",
        amount=Decimal("1200.00"),
        currency="DKK",
    )


def test_profile_supports_fee_schedule_run_and_reminder() -> None:
    fee = _membership_fee()
    schedule = FeeSchedule(membership_fee=fee, due_days=14)
    profile = MembershipBillingProfile(
        membership_type_id=fee.membership_type_id,
        fee_schedule=schedule,
    )

    profile.add_run(
        MembershipBillingRun(
            fiscal_year=2026,
            billing_date=date(2026, 1, 1),
            processed=10,
            invoices_created=8,
            journals_created=8,
            skipped=2,
        )
    )
    profile.add_reminder(
        Reminder(
            member_id=uuid4(),
            message="Membership fee due",
            due_date=date(2026, 2, 1),
        )
    )

    assert len(profile.runs) == 1
    assert len(profile.reminders) == 1


def test_fee_rejects_invalid_amount() -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        MembershipFee(
            membership_type_id=uuid4(),
            membership_type_code="GEN",
            membership_type_name="General",
            amount=Decimal("0"),
            currency="DKK",
        )
