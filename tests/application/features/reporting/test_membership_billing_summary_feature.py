from __future__ import annotations

from datetime import UTC
from datetime import datetime

import pytest

from mfm.application.features.reporting.membership_billing_summary_feature import (
    MembershipBillingSummaryFeature,
)
from mfm.application.features.reporting.membership_billing_summary_feature import (
    MembershipBillingSummaryRequest,
)
from mfm.application.features.reporting.membership_billing_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.membership_billing_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryItemDTO,
)
from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def test_reporting_feature_returns_response() -> None:
    feature = MembershipBillingSummaryFeature(
        service=StubService(
            response=MembershipBillingSummaryResponse(
                profiles=(
                    MembershipBillingSummaryItemDTO(
                        membership_type_code="GEN",
                        membership_type_name="General",
                        currency="DKK",
                        fee_amount="1200.00",
                        due_days=14,
                        reminders=0,
                        last_run_processed=6,
                        last_run_invoices_created=5,
                    ),
                ),
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(MembershipBillingSummaryRequest())

    assert len(response.profiles) == 1
    assert response.profiles[0].membership_type_code == "GEN"


def test_reporting_feature_validates_request() -> None:
    feature = MembershipBillingSummaryFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(MembershipBillingSummaryRequest(include_inactive="invalid"))


def test_reporting_feature_maps_unknown_error() -> None:
    feature = MembershipBillingSummaryFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(MembershipBillingSummaryRequest())
