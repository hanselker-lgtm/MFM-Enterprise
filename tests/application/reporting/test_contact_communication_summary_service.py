from __future__ import annotations

from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.reporting.contact_communication_summary_service import (
    ContactCommunicationSummaryRequest,
)
from mfm.application.reporting.contact_communication_summary_service import (
    ContactCommunicationSummaryService,
)
from mfm.application.reporting.contact_communication_summary_service import (
    ValidationException,
)
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.domain.contact_communication.contact_method import ContactMethod
from mfm.domain.contact_communication.contact_method import ContactMethodType
from mfm.domain.contact_communication.email_address import EmailAddress
from mfm.domain.contact_communication.notification import Notification


class InMemoryRepository:
    def __init__(self, store: dict[UUID, ContactCommunicationProfile]) -> None:
        self._store = store

    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None:
        return self._store.get(contact_id)


def test_summary_service_returns_metrics() -> None:
    contact_id = uuid4()
    profile = ContactCommunicationProfile(contact_id=contact_id)
    method = ContactMethod(
        method_type=ContactMethodType.EMAIL,
        email=EmailAddress("person@example.com"),
        is_primary=True,
    )
    profile.add_method(method)
    profile.schedule_notification(
        Notification(
            contact_id=contact_id,
            method_id=method.id,
            subject="Welcome",
            message="Created",
        )
    )

    service = ContactCommunicationSummaryService(
        repository=InMemoryRepository({contact_id: profile})
    )

    response = service.execute(ContactCommunicationSummaryRequest(contact_id=contact_id))

    assert response.contact_id == contact_id
    assert response.method_count == 1
    assert response.notification_count == 1
    assert response.pending_notifications == 1


def test_summary_service_raises_when_missing() -> None:
    service = ContactCommunicationSummaryService(repository=InMemoryRepository({}))

    with pytest.raises(ValidationException, match="not found"):
        service.execute(ContactCommunicationSummaryRequest(contact_id=uuid4()))
