from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.application.features.onboarding.project_accounting_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingFeature,
)
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingRequest,
)
from mfm.application.features.onboarding.project_accounting_feature import (
    ValidationException,
)
from mfm.application.workflows.project_accounting_workflow import (
    ProjectAccountingWorkflowResponse,
)
from mfm.application.workflows.project_accounting_workflow import WorkflowExecutionError


@dataclass
class _ServiceStub:
    response: ProjectAccountingWorkflowResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> ProjectAccountingRequest:
    return ProjectAccountingRequest(
        project_id=uuid4(),
        journal_number="JRN-WF005-001",
        posting_date=date(2040, 6, 15),
        transaction_description="Project transaction",
        debit_account_id=uuid4(),
        credit_account_id=uuid4(),
        amount=Decimal("100.00"),
    )


def test_feature_happy_path() -> None:
    response = ProjectAccountingWorkflowResponse(
        project_id=uuid4(),
        journal_id=uuid4(),
        journal_number="JRN-WF005-001",
        journal_status="POSTED",
        completed_steps=("STEP-001", "STEP-007"),
    )
    feature = ProjectAccountingFeature(service=_ServiceStub(response=response))

    result = feature.execute(_request())

    assert result.journal_status == "POSTED"
    assert result.completed_steps == ("STEP-001", "STEP-007")


def test_feature_maps_workflow_execution_error() -> None:
    feature = ProjectAccountingFeature(
        service=_ServiceStub(
            error=WorkflowExecutionError("STEP-005", "Post journal entry failed")
        )
    )

    with pytest.raises(BusinessRuleViolation, match="STEP-005"):
        feature.execute(_request())


def test_feature_validates_input() -> None:
    feature = ProjectAccountingFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="journal_number"):
        feature.execute(
            ProjectAccountingRequest(
                project_id=uuid4(),
                journal_number="",
                posting_date=date(2040, 6, 15),
                transaction_description="Project transaction",
                debit_account_id=uuid4(),
                credit_account_id=uuid4(),
                amount=Decimal("100.00"),
            )
        )


def test_feature_rejects_float_amount() -> None:
    feature = ProjectAccountingFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="amount"):
        feature.execute(
            ProjectAccountingRequest(
                project_id=uuid4(),
                journal_number="JRN-WF005-001",
                posting_date=date(2040, 6, 15),
                transaction_description="Project transaction",
                debit_account_id=uuid4(),
                credit_account_id=uuid4(),
                amount=100.0,
            )
        )
