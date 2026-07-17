from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.contact_communication_summary_feature import (
    ContactCommunicationSummaryFeature,
)
from mfm.application.features.reporting.contact_communication_summary_feature import (
    ContactCommunicationSummaryRequest,
)
from mfm.application.features.reporting.contact_communication_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.contact_communication_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.models.contact_communication_summary_dto import (
    ContactCommunicationSummaryResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error

    def execute(self, request):
        _ = request
        if self._error is not None:
            raise self._error
        return self._response


def test_summary_feature_returns_service_response() -> None:
    contact_id = uuid4()
    feature = ContactCommunicationSummaryFeature(
        service=StubService(
            response=ContactCommunicationSummaryResponse(
                contact_id=contact_id,
                method_count=3,
                notification_count=2,
                has_preference=True,
                pending_notifications=1,
                sent_notifications=1,
                failed_notifications=0,
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(ContactCommunicationSummaryRequest(contact_id=contact_id))

    assert response.contact_id == contact_id
    assert response.method_count == 3


def test_summary_feature_maps_unknown_error() -> None:
    feature = ContactCommunicationSummaryFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(ContactCommunicationSummaryRequest(contact_id=uuid4()))


def test_summary_feature_validates_request() -> None:
    feature = ContactCommunicationSummaryFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(ContactCommunicationSummaryRequest(contact_id="invalid"))
