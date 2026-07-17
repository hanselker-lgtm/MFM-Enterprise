from __future__ import annotations

from datetime import UTC
from datetime import datetime

import pytest

from mfm.application.features.reporting.document_archive_summary_feature import (
    DocumentArchiveSummaryFeature,
)
from mfm.application.features.reporting.document_archive_summary_feature import (
    DocumentArchiveSummaryRequest,
)
from mfm.application.features.reporting.document_archive_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.document_archive_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveIntegrationDTO,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryItemDTO,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryResponse,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self.response = response
        self.error = error

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def test_reporting_feature_returns_response() -> None:
    feature = DocumentArchiveSummaryFeature(
        service=StubService(
            response=DocumentArchiveSummaryResponse(
                documents=(
                    DocumentArchiveSummaryItemDTO(
                        category_code="DOC",
                        folder_path="/docs/specs",
                        status="ACTIVE",
                        versions_count=2,
                        attachments_count=1,
                    ),
                ),
                integration=DocumentArchiveIntegrationDTO(
                    membership_links=0,
                    organization_links=0,
                    events_links=0,
                    billing_links=0,
                    projects_links=1,
                ),
                generated_at=datetime(2026, 1, 1, tzinfo=UTC),
            )
        )
    )

    response = feature.execute(DocumentArchiveSummaryRequest())

    assert len(response.documents) == 1
    assert response.integration.projects_links == 1


def test_reporting_feature_validates_request() -> None:
    feature = DocumentArchiveSummaryFeature(service=StubService(response=None))

    with pytest.raises(ValidationException):
        feature.execute(DocumentArchiveSummaryRequest(include_archived="invalid"))


def test_reporting_feature_maps_unknown_error() -> None:
    feature = DocumentArchiveSummaryFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException):
        feature.execute(DocumentArchiveSummaryRequest())
