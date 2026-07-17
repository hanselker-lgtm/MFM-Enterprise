from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.contact_communication.contact_communication_service import (
    SetupContactCommunicationResponse,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationFeature,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ManageContactCommunicationRequest,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    RepositoryException,
)
from mfm.application.features.contact_communication.manage_contact_communication_feature import (
    ValidationException,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def setup(self, request):
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
        allow_marketing=False,
    )


def test_feature_maps_service_response() -> None:
    contact_id = uuid4()
    feature = ManageContactCommunicationFeature(
        service=StubService(
            response=SetupContactCommunicationResponse(
                contact_id=contact_id,
                method_count=3,
                notification_count=1,
                preferred_method_type="EMAIL",
                allow_marketing=False,
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(_request())

    assert response.contact_id == contact_id
    assert response.method_count == 3


def test_feature_validates_request() -> None:
    feature = ManageContactCommunicationFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(
            ManageContactCommunicationRequest(
                contact_id=uuid4(),
                email_address="",
                phone_number="+4520304050",
                postal_line1="Harbor Street 1",
                postal_code="5700",
                postal_city="Svendborg",
                postal_country="Denmark",
            )
        )


def test_feature_maps_unknown_error_to_repository_exception() -> None:
    feature = ManageContactCommunicationFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(_request())
