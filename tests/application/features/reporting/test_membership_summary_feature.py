from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime

import pytest

from mfm.application.features.reporting.membership_summary_feature import (
    MembershipSummaryFeature,
)
from mfm.application.features.reporting.membership_summary_feature import (
    MembershipSummaryRequest,
)
from mfm.application.features.reporting.membership_summary_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.membership_summary_feature import (
    ValidationException,
)
from mfm.application.reporting.membership_summary_service import (
    ValidationException as ServiceValidationException,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryCategoryTotalsDTO,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryResponse,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryStatusTotalsDTO,
)


@dataclass
class _ServiceStub:
    response: MembershipSummaryResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _response() -> MembershipSummaryResponse:
    return MembershipSummaryResponse(
        status_totals=MembershipSummaryStatusTotalsDTO(
            total=2,
            active=1,
            suspended=1,
            ended=0,
            expired=0,
        ),
        category_totals=MembershipSummaryCategoryTotalsDTO(
            general=1,
            youth=1,
            senior=0,
            family=0,
            corporate=0,
        ),
        generated_at=datetime(2040, 1, 1, 8, 0, tzinfo=UTC),
    )


def test_membership_summary_feature_happy_path() -> None:
    feature = MembershipSummaryFeature(service=_ServiceStub(response=_response()))

    result = feature.execute(MembershipSummaryRequest(include_inactive=True))

    assert result.status_totals.total == 2
    assert result.category_totals.general == 1


def test_membership_summary_feature_maps_service_validation_errors() -> None:
    feature = MembershipSummaryFeature(
        service=_ServiceStub(error=ServiceValidationException("invalid request"))
    )

    with pytest.raises(ValidationException, match="invalid request"):
        feature.execute(MembershipSummaryRequest(include_inactive=True))


def test_membership_summary_feature_wraps_unexpected_errors() -> None:
    feature = MembershipSummaryFeature(service=_ServiceStub(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException, match="feature failed"):
        feature.execute(MembershipSummaryRequest(include_inactive=True))
