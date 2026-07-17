from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesRequest,
)
from mfm.application.features.organization_roles.manage_organization_roles_feature import (
    ManageOrganizationRolesResponse,
)
from mfm.application.workflows.organization_roles_workflow import (
    OrganizationRolesWorkflow,
)
from mfm.application.workflows.organization_roles_workflow import (
    OrganizationRolesWorkflowInput,
)


class StubFeature:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def execute(self, request):
        _ = request
        if self._error is not None:
            raise self._error
        return self._response


def _request() -> ManageOrganizationRolesRequest:
    return ManageOrganizationRolesRequest(
        organization_id=uuid4(),
        board_name="National Board",
        role_name="Board Chair",
        committee_name="Governance Committee",
        committee_mandate="Oversee policy and governance.",
        election_period_name="Election 2026",
        election_starts_on=datetime(2026, 1, 1, tzinfo=UTC).date(),
        election_ends_on=datetime(2026, 12, 31, tzinfo=UTC).date(),
    )


def test_workflow_returns_success_result() -> None:
    response = ManageOrganizationRolesResponse(
        organization_id=uuid4(),
        role_count=1,
        assignment_count=1,
        committee_count=1,
        board_name="National Board",
        election_period_count=1,
        generated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )
    workflow = OrganizationRolesWorkflow(feature=StubFeature(response=response))

    result = workflow.execute(OrganizationRolesWorkflowInput(request=_request()))

    assert result.success is True
    assert result.response == response


def test_workflow_returns_failure_result() -> None:
    workflow = OrganizationRolesWorkflow(feature=StubFeature(error=RuntimeError("failed")))

    result = workflow.execute(OrganizationRolesWorkflowInput(request=_request()))

    assert result.success is False
    assert result.response is None
    assert "failed" in result.message
