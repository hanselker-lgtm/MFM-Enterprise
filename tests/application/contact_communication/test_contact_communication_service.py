from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.contact_communication.contact_communication_service import (
    BusinessRuleViolation,
)
from mfm.application.contact_communication.contact_communication_service import (
    ContactCommunicationService,
)
from mfm.application.contact_communication.contact_communication_service import (
    SetupContactCommunicationRequest,
)
from mfm.application.contact_communication.contact_communication_service import (
    ValidationException,
)
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)


class InMemoryContactCommunicationRepository:
    def __init__(self) -> None:
        self._store: dict[UUID, ContactCommunicationProfile] = {}

    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None:
        return self._store.get(contact_id)

    def save(self, profile: ContactCommunicationProfile) -> None:
        self._store[profile.contact_id] = profile


def _request(contact_id: UUID) -> SetupContactCommunicationRequest:
    _ = date(2026, 1, 1)
    return SetupContactCommunicationRequest(
        contact_id=contact_id,
        email_address="person@example.com",
        phone_number="+45 20 30 40 50",
        postal_line1="Harbor Street 1",
        postal_code="5700",
        postal_city="Svendborg",
        postal_country="Denmark",
        allow_marketing=True,
    )


def test_setup_creates_profile_with_methods_preference_and_notification() -> None:
    contact_id = uuid4()
    repository = InMemoryContactCommunicationRepository()
    service = ContactCommunicationService(repository=repository)

    response = service.setup(_request(contact_id))

    assert response.contact_id == contact_id
    assert response.method_count == 3
    assert response.notification_count == 1
    assert response.preferred_method_type == "EMAIL"
    assert response.allow_marketing is True


def test_setup_rejects_duplicate_profile() -> None:
    contact_id = uuid4()
    repository = InMemoryContactCommunicationRepository()
    service = ContactCommunicationService(repository=repository)

    _ = service.setup(_request(contact_id))

    with pytest.raises(BusinessRuleViolation, match="already exists"):
        service.setup(_request(contact_id))


def test_setup_validates_request() -> None:
    service = ContactCommunicationService(repository=InMemoryContactCommunicationRepository())

    with pytest.raises(ValidationException):
        service.setup(
            SetupContactCommunicationRequest(
                contact_id=uuid4(),
                email_address="",
                phone_number="+4520304050",
                postal_line1="Harbor Street 1",
                postal_code="5700",
                postal_city="Svendborg",
                postal_country="Denmark",
            )
        )
