from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.annual_contingent_generation import CreateAnnualContingentResponse
from mfm.application.membership_billing.membership_billing_service import (
    BusinessRuleViolation,
)
from mfm.application.membership_billing.membership_billing_service import (
    CreateReminderRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    MembershipBillingService,
)
from mfm.application.membership_billing.membership_billing_service import (
    RunMembershipBillingRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    SetupFeeScheduleRequest,
)
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile


class InMemoryRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, MembershipBillingProfile] = {}

    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None:
        return self.store.get(membership_type_id)

    def save(self, profile: MembershipBillingProfile) -> None:
        self.store[profile.membership_type_id] = profile


class StubAnnualContingentFeature:
    def __init__(self) -> None:
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        return CreateAnnualContingentResponse(
            processed=6,
            invoices_created=5,
            journal_drafts_created=5,
            skipped=1,
            warnings=(),
            errors=(),
        )


def test_setup_schedule_run_billing_and_create_reminder() -> None:
    membership_type_id = uuid4()
    repository = InMemoryRepository()
    annual_feature = StubAnnualContingentFeature()
    service = MembershipBillingService(
        repository=repository,
        annual_contingent_feature=annual_feature,
    )

    setup_result = service.setup_fee_schedule(
        SetupFeeScheduleRequest(
            membership_type_id=membership_type_id,
            membership_type_code="GEN",
            membership_type_name="General",
            amount=Decimal("1200.00"),
            currency="DKK",
            due_days=14,
        )
    )
    assert setup_result.run_invoices_created == 0

    run_result = service.run_billing(
        RunMembershipBillingRequest(
            membership_type_id=membership_type_id,
            fiscal_year=2026,
            billing_date=date(2026, 1, 1),
            dry_run=False,
        )
    )
    assert run_result.run_processed == 6
    assert run_result.run_invoices_created == 5

    reminder_result = service.create_reminder(
        CreateReminderRequest(
            membership_type_id=membership_type_id,
            member_id=uuid4(),
            message="Please pay your membership fee",
            due_date=date(2026, 2, 1),
        )
    )
    assert reminder_result.reminder_count == 1


def test_run_billing_requires_existing_fee_schedule() -> None:
    service = MembershipBillingService(
        repository=InMemoryRepository(),
        annual_contingent_feature=StubAnnualContingentFeature(),
    )

    with pytest.raises(BusinessRuleViolation, match="not found"):
        service.run_billing(
            RunMembershipBillingRequest(
                membership_type_id=uuid4(),
                fiscal_year=2026,
                billing_date=date(2026, 1, 1),
            )
        )
