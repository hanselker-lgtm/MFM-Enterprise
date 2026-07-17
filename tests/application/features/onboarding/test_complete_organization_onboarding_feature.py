from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.complete_organization_onboarding_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.complete_organization_onboarding_feature import (
    CompleteOrganizationOnboardingFeature,
)
from mfm.application.features.onboarding.complete_organization_onboarding_feature import (
    CompleteOrganizationOnboardingRequest,
)
from mfm.application.features.onboarding.complete_organization_onboarding_feature import (
    ValidationException,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflowResponse,
)
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    WorkflowExecutionError,
)
from mfm.domain.organization.organization_type import OrganizationType


@dataclass
class _ServiceStub:
    response: CompleteOrganizationOnboardingWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> CompleteOrganizationOnboardingRequest:
    return CompleteOrganizationOnboardingRequest(
        organization_number="ORG-FEAT-001",
        organization_name="Feature Org",
        organization_type=OrganizationType.ASSOCIATION,
        fiscal_year=2031,
    )


def test_feature_happy_path() -> None:
    response = CompleteOrganizationOnboardingWorkflowResponse(
        organization_id=uuid4(),
        organization_status="ACTIVE",
        document_library_id=uuid4(),
        fiscal_year_id=uuid4(),
        ledger_account_ids=(uuid4(), uuid4()),
        completed_steps=("STEP-001", "STEP-007"),
    )
    feature = CompleteOrganizationOnboardingFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.organization_status == "ACTIVE"
    assert result.completed_steps == ("STEP-001", "STEP-007")


def test_feature_maps_workflow_execution_error() -> None:
    feature = CompleteOrganizationOnboardingFeature(
        service=_ServiceStub(error=WorkflowExecutionError("STEP-004", "Create first fiscal year failed"))
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-004"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = CompleteOrganizationOnboardingFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="organization_number"):
        feature.execute(
            CompleteOrganizationOnboardingRequest(
                organization_number="",
                organization_name="Feature Org",
                organization_type=OrganizationType.ASSOCIATION,
                fiscal_year=2031,
            )
        )
