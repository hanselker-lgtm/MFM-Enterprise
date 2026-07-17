from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import uuid4

import pytest

from mfm.application.features.membership.manage_membership_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipFeature,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipRequest,
)
from mfm.application.features.membership.manage_membership_feature import (
    RepositoryException,
)
from mfm.application.features.membership.manage_membership_feature import (
    ValidationException,
)
from mfm.application.membership.membership_management_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.membership.membership_management_service import (
    MembershipRecordResponse,
)
from mfm.domain.membership.membership_status import MembershipStatus


@dataclass
class _ServiceStub:
    response: tuple[MembershipRecordResponse, ...] = ()
    error: Exception | None = None

    def register_membership(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response[0]

    def change_membership_status(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response[0]

    def list_memberships(self, request):
        _ = request
        if self.error is not None:
            raise self.error
        return self.response


def _membership_response() -> MembershipRecordResponse:
    return MembershipRecordResponse(
        membership_id=uuid4(),
        member_id=uuid4(),
        membership_type_id=uuid4(),
        membership_type_code="STANDARD",
        membership_type_name="Standard",
        status=MembershipStatus.ACTIVE.value,
        start_date=date(2026, 1, 1),
        end_date=None,
    )


def test_manage_membership_feature_register_happy_path() -> None:
    service = _ServiceStub(response=(_membership_response(),))
    feature = ManageMembershipFeature(service=service)

    request = ManageMembershipRequest(
        operation="register",
        member_id=uuid4(),
        membership_type_id=uuid4(),
    )

    result = feature.execute(request)
    assert len(result.memberships) == 1


def test_manage_membership_feature_list_happy_path() -> None:
    service = _ServiceStub(response=(_membership_response(), _membership_response()))
    feature = ManageMembershipFeature(service=service)

    result = feature.execute(
        ManageMembershipRequest(operation="list", member_id=uuid4())
    )

    assert len(result.memberships) == 2


def test_manage_membership_feature_maps_business_errors() -> None:
    feature = ManageMembershipFeature(
        service=_ServiceStub(error=ServiceBusinessRuleViolation("rule"))
    )

    with pytest.raises(BusinessRuleViolation, match="rule"):
        feature.execute(
            ManageMembershipRequest(
                operation="register",
                member_id=uuid4(),
                membership_type_id=uuid4(),
            )
        )


def test_manage_membership_feature_validates_request() -> None:
    feature = ManageMembershipFeature(service=_ServiceStub())

    with pytest.raises(ValidationException):
        feature.execute(ManageMembershipRequest(operation="list", member_id=None))


def test_manage_membership_feature_wraps_unexpected_errors() -> None:
    feature = ManageMembershipFeature(service=_ServiceStub(error=RuntimeError("boom")))

    with pytest.raises(RepositoryException, match="feature failed"):
        feature.execute(
            ManageMembershipRequest(
                operation="change-status",
                membership_id=uuid4(),
                target_status=MembershipStatus.SUSPENDED,
            )
        )
