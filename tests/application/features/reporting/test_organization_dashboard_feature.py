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
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardAccountingDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardDocumentsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardHealthIndicatorsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardOperationsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardOrganizationDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardProjectsDTO,
)
from mfm.application.reporting.organization_dashboard_service import (
    ValidationException as ServiceValidationException,
)


@dataclass
class _ServiceStub:
    response: OrganizationDashboardDTO | None = None
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
        organization_name="Acme Maritime",
        organization_status="ACTIVE",
        period_start=date(2040, 1, 1),
        period_end=date(2040, 12, 31),
    )


def test_feature_happy_path() -> None:
    organization_id = uuid4()
    service_response = OrganizationDashboardDTO(
        organization=OrganizationDashboardOrganizationDTO(
            organization_id=organization_id,
            name="Acme Maritime",
            status="ACTIVE",
        ),
        projects=OrganizationDashboardProjectsDTO(
            active_projects=2,
            closed_projects=1,
            archived_projects=0,
            total_projects=3,
        ),
        documents=OrganizationDashboardDocumentsDTO(
            total_documents=5,
            documents_added_last_30_days=2,
        ),
        accounting=OrganizationDashboardAccountingDTO(
            journal_count=3,
            last_posted_journal="JRN-0003",
            open_fiscal_years=1,
            closed_fiscal_years=2,
        ),
        operations=OrganizationDashboardOperationsDTO(
            last_accounting_activity=date(2040, 6, 3),
            last_document_activity=datetime(2040, 6, 1, 8, 0, tzinfo=UTC),
        ),
        health_indicators=OrganizationDashboardHealthIndicatorsDTO(
            budget_coverage=1.0,
            accounting_status="AT_RISK",
            documentation_status="COMPLETE",
            archive_status="ON_TRACK",
        ),
    )

    feature = OrganizationDashboardFeature(service=_ServiceStub(response=service_response))

    result = feature.execute(_request())

    assert result.organization.organization_id == organization_id
    assert result.projects.active_projects == 2
    assert result.health_indicators.accounting_status == "AT_RISK"


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
