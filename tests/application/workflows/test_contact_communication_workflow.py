from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationRequest,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationResponse,
)
from mfm.application.workflows.contact_communication_workflow import (
    ContactCommunicationWorkflow,
)
from mfm.application.workflows.contact_communication_workflow import (
    ContactCommunicationWorkflowInput,
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


def _request() -> ManageContactCommunicationRequest:
    return ManageContactCommunicationRequest(
        contact_id=uuid4(),
        email_address="person@example.com",
        phone_number="+45 20 30 40 50",
        postal_line1="Harbor Street 1",
        postal_code="5700",
        postal_city="Svendborg",
        postal_country="Denmark",
    )


def test_workflow_returns_success() -> None:
    response = ManageContactCommunicationResponse(
        contact_id=uuid4(),
        method_count=3,
        notification_count=1,
        preferred_method_type="EMAIL",
        allow_marketing=False,
        generated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )
    workflow = ContactCommunicationWorkflow(feature=StubFeature(response=response))

    result = workflow.execute(ContactCommunicationWorkflowInput(request=_request()))

    assert result.success is True
    assert result.response == response


def test_workflow_returns_failure() -> None:
    workflow = ContactCommunicationWorkflow(feature=StubFeature(error=RuntimeError("failed")))

    result = workflow.execute(ContactCommunicationWorkflowInput(request=_request()))

    assert result.success is False
    assert result.response is None
    assert "failed" in result.message
