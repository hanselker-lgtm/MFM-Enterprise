"""Workflow for membership fees and billing capability."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingFeature,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingRequest,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingResponse,
)


@dataclass(frozen=True, slots=True)
class MembershipBillingWorkflowInput:
    request: ManageMembershipBillingRequest


@dataclass(frozen=True, slots=True)
class MembershipBillingWorkflowResult:
    success: bool
    response: ManageMembershipBillingResponse | None = None
    message: str = ""


class MembershipBillingWorkflow:
    """Workflow wrapper around membership billing feature API."""

    def __init__(self, *, feature: ManageMembershipBillingFeature) -> None:
        self._feature = feature

    def execute(self, data: MembershipBillingWorkflowInput) -> MembershipBillingWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return MembershipBillingWorkflowResult(
                success=True,
                response=response,
                message="Membership billing operation completed",
            )
        except Exception as exc:
            return MembershipBillingWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
