from __future__ import annotations

from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingRequest,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingResponse,
)
from mfm.application.membership_billing.membership_billing_service import MembershipBillingResponse
from mfm.application.workflows.membership_billing_workflow import MembershipBillingWorkflow
from mfm.application.workflows.membership_billing_workflow import MembershipBillingWorkflowInput


class StubFeature:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _request() -> ManageMembershipBillingRequest:
    return ManageMembershipBillingRequest(
        operation="setup-fee",
        membership_type_id=uuid4(),
        membership_type_code="GEN",
        membership_type_name="General",
        amount=Decimal("1200.00"),
        currency="DKK",
        due_days=14,
    )


def test_workflow_returns_success() -> None:
    response = ManageMembershipBillingResponse(
        result=MembershipBillingResponse(
            membership_type_id=uuid4(),
            fee_amount="1200.00",
            currency="DKK",
            due_days=14,
            run_processed=0,
            run_invoices_created=0,
            reminder_count=0,
            generated_at=datetime(2026, 1, 1, tzinfo=UTC),
        )
    )
    workflow = MembershipBillingWorkflow(feature=StubFeature(response=response))

    result = workflow.execute(MembershipBillingWorkflowInput(request=_request()))

    assert result.success is True
    assert result.response == response


def test_workflow_returns_failure() -> None:
    workflow = MembershipBillingWorkflow(feature=StubFeature(error=RuntimeError("failed")))

    result = workflow.execute(MembershipBillingWorkflowInput(request=_request()))

    assert result.success is False
    assert result.response is None
    assert "failed" in result.message
