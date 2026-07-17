from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import uuid4

import pytest

from mfm.application.features.reporting.organization_dashboard_feature import (
    OrganizationDashboardFeature,
)
from mfm.application.features.reporting.organization_dashboard_feature import (
    OrganizationDashboardRequest,
)
from mfm.application.features.reporting.organization_dashboard_feature import (
    RepositoryException,
)
from mfm.application.features.reporting.organization_dashboard_feature import (
    ValidationException,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportResponse,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationHealthIndicatorsView,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationInfoView,
)
from mfm.application.reports.organization_dashboard_report import (
    ValidationException as ServiceValidationException,
)


@dataclass
class _ServiceStub:
    response: OrganizationDashboardReportResponse | None = None
    error: Exception | None = None

    def execute(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        assert self.response is not None
        return self.response


def _request() -> OrganizationDashboardRequest:
    return OrganizationDashboardRequest(
        organization_id=uuid4(),
        organization_number="ORG-001",
        organization_name="Acme Maritime",
        organization_type="MEMBER",
        organization_status="ACTIVE",
        period_start=date(2040, 1, 1),
        period_end=date(2040, 12, 31),
    )


def test_feature_happy_path() -> None:
    organization_id = uuid4()
    service_response = OrganizationDashboardReportResponse(
        organization=OrganizationInfoView(
            organization_id=organization_id,
            organization_number="ORG-001",
            organization_name="Acme Maritime",
            organization_type="MEMBER",
            organization_status="ACTIVE",
        ),
        active_projects=2,
        closed_projects=1,
        archived_projects=0,
        project_documents=5,
        accounting_journals=3,
        open_fiscal_years=1,
        last_accounting_activity=date(2040, 6, 3),
        last_document_activity=datetime(2040, 6, 1, 8, 0, tzinfo=UTC),
        health_indicators=OrganizationHealthIndicatorsView(
            healthy_projects=1,
            at_risk_projects=1,
            projects_with_budget_ready=2,
            projects_with_unposted_journals=1,
            overall_health_status="AT_RISK",
        ),
    )

    feature = OrganizationDashboardFeature(service=_ServiceStub(response=service_response))

    result = feature.execute(_request())

    assert result.organization.organization_id == organization_id
    assert result.active_projects == 2
    assert result.health_indicators.overall_health_status == "AT_RISK"


def test_feature_maps_service_validation_errors() -> None:
    feature = OrganizationDashboardFeature(
        service=_ServiceStub(error=ServiceValidationException("invalid period"))
    )

    with pytest.raises(ValidationException, match="invalid period"):
        feature.execute(_request())


def test_feature_validates_request() -> None:
    feature = OrganizationDashboardFeature(service=_ServiceStub(response=None))

    with pytest.raises(ValidationException, match="organization_id"):
        feature.execute(
            OrganizationDashboardRequest(
                organization_id="not-a-uuid",  # type: ignore[arg-type]
            )
        )


def test_feature_wraps_unexpected_errors() -> None:
    feature = OrganizationDashboardFeature(service=_ServiceStub(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException, match="feature failed"):
        feature.execute(_request())
