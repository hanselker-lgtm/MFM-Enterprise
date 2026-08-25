from __future__ import annotations
from uuid import UUID, uuid4

import pytest

from mfm.application.member.create_member_use_case import CreateMemberUseCase
from mfm.domain.member.exceptions import (
    ContactReferenceNotFoundError,
    DuplicateMemberNumberError,
)
from mfm.domain.member.member import Member
from mfm.repositories.member_repository import MemberRepository


class InMemoryMemberRepository(MemberRepository):
    def __init__(self) -> None:
        self._members: dict[str, Member] = {}
        self._known_contacts: set[UUID] = set()

    def add(self, member: Member) -> None:
        self._members[member.member_number] = member

    def update(self, member: Member) -> None:
        self._members[member.member_number] = member

    def get(self, member_id: UUID) -> Member | None:
        for member in self._members.values():
            if member.id == member_id:
                return member
        return None

    def get_by_number(self, member_number: str) -> Member | None:
        return self._members.get(member_number)

    def list(self) -> list[Member]:
        return list(self._members.values())

    def exists(self, member_id: UUID) -> bool:
        return self.get(member_id) is not None

    def delete(self, member_id: UUID) -> None:
        for number, member in list(self._members.items()):
            if member.id == member_id:
                del self._members[number]
                return

    def contact_exists(self, contact_id: UUID) -> bool:
        return contact_id in self._known_contacts


def test_create_member_use_case_success():
    repository = InMemoryMemberRepository()
    contact_id = uuid4()
    repository._known_contacts.add(contact_id)
    use_case = CreateMemberUseCase(repository)

    member = Member(contact_id=contact_id, member_number="M-300001")

    created = use_case.execute(member)

    assert created is member
    assert repository.get_by_number("M-300001") is member


def test_create_member_use_case_rejects_duplicate_member_number():
    repository = InMemoryMemberRepository()
    contact_id = uuid4()
    repository._known_contacts.add(contact_id)
    use_case = CreateMemberUseCase(repository)

    first = Member(contact_id=contact_id, member_number="M-300002")
    second = Member(contact_id=contact_id, member_number="M-300002")

    use_case.execute(first)

    with pytest.raises(DuplicateMemberNumberError):
        use_case.execute(second)


def test_create_member_use_case_rejects_missing_contact_reference():
    repository = InMemoryMemberRepository()
    use_case = CreateMemberUseCase(repository)

    member = Member(contact_id=uuid4(), member_number="M-300003")

    with pytest.raises(ContactReferenceNotFoundError):
        use_case.execute(member)


def test_create_member_use_case_rejects_invalid_input_type():
    repository = InMemoryMemberRepository()
    use_case = CreateMemberUseCase(repository)

    with pytest.raises(TypeError):
        use_case.execute("not-a-member")  # type: ignore[arg-type]
