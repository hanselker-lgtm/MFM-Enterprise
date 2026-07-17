from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.membership.membership_management_service import (
    BusinessRuleViolation,
)
from mfm.application.membership.membership_management_service import (
    ChangeMembershipStatusRequest,
)
from mfm.application.membership.membership_management_service import (
    ListMembershipsRequest,
)
from mfm.application.membership.membership_management_service import (
    MembershipManagementService,
)
from mfm.application.membership.membership_management_service import (
    RegisterMembershipRequest,
)
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


class InMemoryMembershipRepository:
    def __init__(self) -> None:
        self._memberships: dict[UUID, Membership] = {}
        self._known_members: set[UUID] = set()

    def add(self, membership: Membership) -> None:
        active = [
            item
            for item in self._memberships.values()
            if item.member_id == membership.member_id
            and item.status is MembershipStatus.ACTIVE
        ]
        if membership.status is MembershipStatus.ACTIVE and active:
            raise ValueError("active membership already exists")
        self._memberships[membership.id] = membership

    def update(self, membership: Membership) -> None:
        self._memberships[membership.id] = membership

    def get(self, membership_id: UUID) -> Membership | None:
        return self._memberships.get(membership_id)

    def list_by_member(self, member_id: UUID) -> list[Membership]:
        return [
            item for item in self._memberships.values() if item.member_id == member_id
        ]

    def member_exists(self, member_id: UUID) -> bool:
        return member_id in self._known_members


class InMemoryMembershipTypeRepository:
    def __init__(self) -> None:
        self._items: dict[UUID, MembershipType] = {}

    def get(self, membership_type_id: UUID) -> MembershipType | None:
        return self._items.get(membership_type_id)


@dataclass(slots=True)
class _Fixture:
    service: MembershipManagementService
    membership_repository: InMemoryMembershipRepository
    membership_type_repository: InMemoryMembershipTypeRepository
    member_id: UUID
    membership_type: MembershipType


def _fixture() -> _Fixture:
    membership_repository = InMemoryMembershipRepository()
    membership_type_repository = InMemoryMembershipTypeRepository()

    member_id = uuid4()
    membership_repository._known_members.add(member_id)

    membership_type = MembershipType(
        code="STANDARD",
        name="Standard",
        category=MembershipCategory.GENERAL,
    )
    membership_type_repository._items[membership_type.id] = membership_type

    service = MembershipManagementService(
        membership_repository=membership_repository,
        membership_type_repository=membership_type_repository,
    )
    return _Fixture(
        service=service,
        membership_repository=membership_repository,
        membership_type_repository=membership_type_repository,
        member_id=member_id,
        membership_type=membership_type,
    )


def test_register_membership_success() -> None:
    fx = _fixture()

    response = fx.service.register_membership(
        RegisterMembershipRequest(
            member_id=fx.member_id,
            membership_type_id=fx.membership_type.id,
            start_date=date(2026, 1, 5),
        )
    )

    assert response.member_id == fx.member_id
    assert response.membership_type_code == "STANDARD"
    assert response.status == MembershipStatus.ACTIVE.value


def test_register_membership_rejects_duplicate_active_membership() -> None:
    fx = _fixture()
    fx.service.register_membership(
        RegisterMembershipRequest(
            member_id=fx.member_id,
            membership_type_id=fx.membership_type.id,
        )
    )

    with pytest.raises(BusinessRuleViolation):
        fx.service.register_membership(
            RegisterMembershipRequest(
                member_id=fx.member_id,
                membership_type_id=fx.membership_type.id,
            )
        )


def test_change_membership_status_success() -> None:
    fx = _fixture()
    created = fx.service.register_membership(
        RegisterMembershipRequest(
            member_id=fx.member_id,
            membership_type_id=fx.membership_type.id,
            start_date=date(2026, 1, 1),
        )
    )

    changed = fx.service.change_membership_status(
        ChangeMembershipStatusRequest(
            membership_id=created.membership_id,
            target_status=MembershipStatus.SUSPENDED,
        )
    )

    assert changed.status == MembershipStatus.SUSPENDED.value


def test_list_memberships_supports_active_only() -> None:
    fx = _fixture()
    created = fx.service.register_membership(
        RegisterMembershipRequest(
            member_id=fx.member_id,
            membership_type_id=fx.membership_type.id,
            start_date=date(2026, 1, 1),
        )
    )
    fx.service.change_membership_status(
        ChangeMembershipStatusRequest(
            membership_id=created.membership_id,
            target_status=MembershipStatus.ENDED,
            effective_date=date(2026, 2, 1),
        )
    )

    all_memberships = fx.service.list_memberships(
        ListMembershipsRequest(member_id=fx.member_id)
    )
    active_only = fx.service.list_memberships(
        ListMembershipsRequest(member_id=fx.member_id, active_only=True)
    )

    assert len(all_memberships) == 1
    assert len(active_only) == 0
