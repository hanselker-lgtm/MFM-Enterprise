from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import uuid4

from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipRequest,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipResponse,
)
from mfm.application.membership.membership_management_service import (
    MembershipRecordResponse,
)
from mfm.application.workflows.membership_management_workflow import (
    MembershipManagementWorkflow,
)
from mfm.application.workflows.membership_management_workflow import (
    MembershipManagementWorkflowInput,
)
from mfm.domain.membership.membership_status import MembershipStatus


@dataclass
class _FeatureStub:
    response: ManageMembershipResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _response() -> ManageMembershipResponse:
    return ManageMembershipResponse(
        memberships=(
            MembershipRecordResponse(
                membership_id=uuid4(),
                member_id=uuid4(),
                membership_type_id=uuid4(),
                membership_type_code="STANDARD",
                membership_type_name="Standard",
                status=MembershipStatus.ACTIVE.value,
                start_date=date(2026, 1, 1),
                end_date=None,
            ),
        )
    )


def test_membership_management_workflow_success() -> None:
    workflow = MembershipManagementWorkflow(feature=_FeatureStub(response=_response()))
    result = workflow.execute(
        MembershipManagementWorkflowInput(
            request=ManageMembershipRequest(
                operation="list",
                member_id=uuid4(),
            )
        )
    )

    assert result.success is True
    assert result.response is not None
    assert len(result.response.memberships) == 1


def test_membership_management_workflow_failure() -> None:
    workflow = MembershipManagementWorkflow(feature=_FeatureStub(error=RuntimeError("boom")))
    result = workflow.execute(
        MembershipManagementWorkflowInput(
            request=ManageMembershipRequest(
                operation="list",
                member_id=uuid4(),
            )
        )
    )

    assert result.success is False
    assert result.response is None
    assert "boom" in result.message
