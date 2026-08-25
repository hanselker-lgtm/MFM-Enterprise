from __future__ import annotations
from datetime import date
from uuid import UUID, uuid4

import pytest

from mfm.application.member.activate_member_use_case import ActivateMemberUseCase
from mfm.application.member.deactivate_member_use_case import DeactivateMemberUseCase
from mfm.application.member.resign_member_use_case import ResignMemberUseCase
from mfm.domain.member.exceptions import (
    InvalidMemberStatusTransitionError,
    MemberNotFoundError,
)
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus
from mfm.repositories.member_repository import MemberRepository


class InMemoryMemberRepository(MemberRepository):
    def __init__(self) -> None:
        self._members: dict[UUID, Member] = {}

    def add(self, member: Member) -> None:
        self._members[member.id] = member

    def update(self, member: Member) -> None:
        self._members[member.id] = member

    def get(self, member_id: UUID) -> Member | None:
        return self._members.get(member_id)

    def get_by_number(self, member_number: str) -> Member | None:
        for member in self._members.values():
            if member.member_number == member_number:
                return member
        return None

    def list(self) -> list[Member]:
        return list(self._members.values())

    def exists(self, member_id: UUID) -> bool:
        return member_id in self._members

    def delete(self, member_id: UUID) -> None:
        self._members.pop(member_id, None)

    def contact_exists(self, contact_id: UUID) -> bool:
        return True


def test_activate_member_use_case_success():
    repository = InMemoryMemberRepository()
    member = Member(
        contact_id=uuid4(),
        member_number="M-500001",
        status=MemberStatus.INACTIVE,
        join_date=date(2026, 1, 1),
        leave_date=date(2026, 2, 1),
    )
    repository.add(member)
    use_case = ActivateMemberUseCase(repository)

    updated = use_case.execute(member.id)

    assert updated.status == MemberStatus.ACTIVE
    assert updated.leave_date is None


def test_deactivate_member_use_case_success():
    repository = InMemoryMemberRepository()
    member = Member(
        contact_id=uuid4(),
        member_number="M-500002",
        status=MemberStatus.ACTIVE,
    )
    repository.add(member)
    use_case = DeactivateMemberUseCase(repository)

    updated = use_case.execute(member.id)

    assert updated.status == MemberStatus.INACTIVE


def test_resign_member_use_case_success():
    repository = InMemoryMemberRepository()
    member = Member(
        contact_id=uuid4(),
        member_number="M-500003",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 1),
    )
    repository.add(member)
    use_case = ResignMemberUseCase(repository)

    updated = use_case.execute(member.id, date(2026, 3, 1))

    assert updated.status == MemberStatus.TERMINATED
    assert updated.leave_date == date(2026, 3, 1)


def test_activate_member_use_case_not_found():
    repository = InMemoryMemberRepository()
    use_case = ActivateMemberUseCase(repository)

    with pytest.raises(MemberNotFoundError):
        use_case.execute(uuid4())


def test_deactivate_member_use_case_not_found():
    repository = InMemoryMemberRepository()
    use_case = DeactivateMemberUseCase(repository)

    with pytest.raises(MemberNotFoundError):
        use_case.execute(uuid4())


def test_resign_member_use_case_not_found():
    repository = InMemoryMemberRepository()
    use_case = ResignMemberUseCase(repository)

    with pytest.raises(MemberNotFoundError):
        use_case.execute(uuid4())


def test_lifecycle_use_case_propagates_invalid_transition():
    repository = InMemoryMemberRepository()
    member = Member(
        contact_id=uuid4(),
        member_number="M-500004",
        status=MemberStatus.TERMINATED,
    )
    repository.add(member)
    use_case = ActivateMemberUseCase(repository)

    with pytest.raises(InvalidMemberStatusTransitionError):
        use_case.execute(member.id)
