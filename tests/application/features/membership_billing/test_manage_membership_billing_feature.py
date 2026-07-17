from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingFeature,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingRequest,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    RepositoryException,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ValidationException,
)
from mfm.application.membership_billing.membership_billing_service import MembershipBillingResponse


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def setup_fee_schedule(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def run_billing(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response

    def create_reminder(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _response() -> MembershipBillingResponse:
    return MembershipBillingResponse(
        membership_type_id=uuid4(),
        fee_amount="1200.00",
        currency="DKK",
        due_days=14,
        run_processed=6,
        run_invoices_created=5,
        reminder_count=1,
        generated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )


def test_feature_routes_setup_and_maps_response() -> None:
    feature = ManageMembershipBillingFeature(service=StubService(response=_response()))

    result = feature.execute(
        ManageMembershipBillingRequest(
            operation="setup-fee",
            membership_type_id=uuid4(),
            membership_type_code="GEN",
            membership_type_name="General",
            amount=Decimal("1200.00"),
            currency="DKK",
            due_days=14,
        )
    )

    assert result.result.currency == "DKK"


def test_feature_validates_request() -> None:
    feature = ManageMembershipBillingFeature(service=StubService(response=_response()))

    with pytest.raises(ValidationException):
        feature.execute(
            ManageMembershipBillingRequest(
                operation="run-billing",
                membership_type_id=uuid4(),
                fiscal_year=2026,
                billing_date=None,
            )
        )


def test_feature_maps_unknown_error() -> None:
    feature = ManageMembershipBillingFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(
            ManageMembershipBillingRequest(
                operation="run-billing",
                membership_type_id=uuid4(),
                fiscal_year=2026,
                billing_date=date(2026, 1, 1),
            )
        )
