"""Membership management application workflow."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipFeature,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipRequest,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipResponse,
)


@dataclass(frozen=True, slots=True)
class MembershipManagementWorkflowInput:
    request: ManageMembershipRequest


@dataclass(frozen=True, slots=True)
class MembershipManagementWorkflowResult:
    success: bool
    response: ManageMembershipResponse | None = None
    message: str = ""


class MembershipManagementWorkflow:
    """Workflow wrapper around membership feature API operations."""

    def __init__(self, *, feature: ManageMembershipFeature) -> None:
        self._feature = feature

    def execute(
        self,
        data: MembershipManagementWorkflowInput,
    ) -> MembershipManagementWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return MembershipManagementWorkflowResult(
                success=True,
                response=response,
                message="Membership operation completed",
            )
        except Exception as exc:
            return MembershipManagementWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
