from __future__ import annotations

from datetime import date
from uuid import uuid4

from mfm.application.reporting.membership_summary_service import (
    MembershipSummaryRequest,
)
from mfm.application.reporting.membership_summary_service import MembershipSummaryService
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


class _MembershipRepositoryStub:
    def __init__(self, memberships: list[Membership]) -> None:
        self._memberships = memberships

    def list(self):
        return list(self._memberships)

    def list_active(self):
        return [
            item for item in self._memberships if item.status is MembershipStatus.ACTIVE
        ]


def _membership(category: MembershipCategory, status: MembershipStatus) -> Membership:
    membership_type = MembershipType(
        code=f"{category.value}-TYPE",
        name=category.value.title(),
        category=category,
    )
    membership = Membership(
        member_id=uuid4(),
        membership_type=membership_type,
        start_date=date(2026, 1, 1),
    )
    if status is MembershipStatus.SUSPENDED:
        membership.suspend()
    elif status is MembershipStatus.ENDED:
        membership.end(date(2026, 2, 1))
    elif status is MembershipStatus.EXPIRED:
        membership.expire(date(2026, 2, 1))
    return membership


def test_membership_summary_service_counts_statuses_and_categories() -> None:
    memberships = [
        _membership(MembershipCategory.GENERAL, MembershipStatus.ACTIVE),
        _membership(MembershipCategory.YOUTH, MembershipStatus.ACTIVE),
        _membership(MembershipCategory.SENIOR, MembershipStatus.SUSPENDED),
        _membership(MembershipCategory.FAMILY, MembershipStatus.ENDED),
        _membership(MembershipCategory.CORPORATE, MembershipStatus.EXPIRED),
    ]
    service = MembershipSummaryService(
        membership_repository=_MembershipRepositoryStub(memberships)
    )

    result = service.execute(MembershipSummaryRequest(include_inactive=True))

    assert result.status_totals.total == 5
    assert result.status_totals.active == 2
    assert result.status_totals.suspended == 1
    assert result.status_totals.ended == 2
    assert result.status_totals.expired == 0
    assert result.category_totals.general == 1
    assert result.category_totals.youth == 1
    assert result.category_totals.senior == 1
    assert result.category_totals.family == 1
    assert result.category_totals.corporate == 1


def test_membership_summary_service_active_only_mode() -> None:
    memberships = [
        _membership(MembershipCategory.GENERAL, MembershipStatus.ACTIVE),
        _membership(MembershipCategory.FAMILY, MembershipStatus.ENDED),
    ]
    service = MembershipSummaryService(
        membership_repository=_MembershipRepositoryStub(memberships)
    )

    result = service.execute(MembershipSummaryRequest(include_inactive=False))

    assert result.status_totals.total == 1
    assert result.status_totals.active == 1
    assert result.category_totals.general == 1
    assert result.category_totals.family == 0
