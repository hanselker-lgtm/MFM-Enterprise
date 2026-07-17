"""Workflow for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationFeature,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationRequest,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationResponse,
)


@dataclass(frozen=True, slots=True)
class ContactCommunicationWorkflowInput:
    request: ManageContactCommunicationRequest


@dataclass(frozen=True, slots=True)
class ContactCommunicationWorkflowResult:
    success: bool
    response: ManageContactCommunicationResponse | None = None
    message: str = ""


class ContactCommunicationWorkflow:
    """Workflow wrapper around contact communication feature API."""

    def __init__(self, *, feature: ManageContactCommunicationFeature) -> None:
        self._feature = feature

    def execute(self, data: ContactCommunicationWorkflowInput) -> ContactCommunicationWorkflowResult:
        try:
            response = self._feature.execute(data.request)
            return ContactCommunicationWorkflowResult(
                success=True,
                response=response,
                message="Contact communication setup completed",
            )
        except Exception as exc:
            return ContactCommunicationWorkflowResult(
                success=False,
                response=None,
                message=str(exc),
            )
