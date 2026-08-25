from __future__ import annotations

from datetime import date
from uuid import UUID

import pytest

from mfm.application.features.members import (
    BusinessRuleViolation,
    CreateMemberFeature,
    CreateMemberRequest,
    GetMemberFeature,
    GetMemberRequest,
    ListMembersFeature,
    ListMembersRequest,
    ValidationException,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.contact.contact import Contact
from mfm.domain.member.member import Member


class InMemoryContactRepository:
    def __init__(self, store: dict[UUID, Contact]) -> None:
        self._store = store

    def add(self, contact: Contact) -> None:
        self._store[contact.id] = contact

    def get(self, contact_id: UUID) -> Contact | None:
        return self._store.get(contact_id)


class InMemoryMemberRepository:
    def __init__(self, store: dict[UUID, Member]) -> None:
        self._store = store

    def add(self, member: Member) -> None:
        if self.get_by_number(member.member_number) is not None:
            raise ValueError(f"Member number {member.member_number} already exists")
        self._store[member.id] = member

    def get(self, member_id: UUID) -> Member | None:
        return self._store.get(member_id)

    def get_by_number(self, member_number: str) -> Member | None:
        for member in self._store.values():
            if member.member_number == member_number:
                return member
        return None

    def list(self) -> list[Member]:
        return list(self._store.values())


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        super().__init__()
        self._contacts: dict[UUID, Contact] = {}
        self._members: dict[UUID, Member] = {}

    def _start_scope(self) -> None:
        self.contact_repository = InMemoryContactRepository(self._contacts)
        self.member_repository = InMemoryMemberRepository(self._members)

    def _commit_impl(self) -> None:
        pass

    def _rollback_impl(self) -> None:
        pass

    def _flush_impl(self) -> None:
        pass

    def _close_impl(self) -> None:
        pass


def test_create_member_registers_contact_and_member() -> None:
    uow = FakeUnitOfWork()
    feature = CreateMemberFeature(unit_of_work=uow)

    response = feature.execute(
        CreateMemberRequest(
            contact_number="C-000001",
            member_number="M-0001",
            first_name="Anna",
            last_name="Berg",
            join_date=date(2026, 1, 15),
        )
    )

    assert response.member.member_number == "M-0001"
    assert response.member.display_name == "Anna Berg"
    assert response.member.status == "ACTIVE"


def test_create_member_rejects_empty_first_name() -> None:
    uow = FakeUnitOfWork()
    feature = CreateMemberFeature(unit_of_work=uow)

    with pytest.raises(ValidationException):
        feature.execute(
            CreateMemberRequest(
                contact_number="C-000002",
                member_number="M-0002",
                first_name="   ",
                last_name="Berg",
                join_date=date(2026, 1, 15),
            )
        )


def test_create_member_rejects_duplicate_member_number() -> None:
    uow = FakeUnitOfWork()
    feature = CreateMemberFeature(unit_of_work=uow)
    request = CreateMemberRequest(
        contact_number="C-000003",
        member_number="M-0003",
        first_name="Bo",
        last_name="Nissen",
        join_date=date(2026, 1, 15),
    )
    feature.execute(request)

    with pytest.raises(BusinessRuleViolation):
        feature.execute(
            CreateMemberRequest(
                contact_number="C-000004",
                member_number="M-0003",
                first_name="Bo2",
                last_name="Nissen2",
                join_date=date(2026, 1, 15),
            )
        )


def test_list_members_returns_all_registered_members() -> None:
    uow = FakeUnitOfWork()
    create_feature = CreateMemberFeature(unit_of_work=uow)
    create_feature.execute(
        CreateMemberRequest(
            contact_number="C-000005",
            member_number="M-0005",
            first_name="Eva",
            last_name="Olsen",
            join_date=date(2026, 2, 1),
        )
    )

    response = ListMembersFeature(unit_of_work=uow).execute(ListMembersRequest())

    assert len(response.members) == 1
    assert response.members[0].member_number == "M-0005"


def test_get_member_returns_requested_member() -> None:
    uow = FakeUnitOfWork()
    created = CreateMemberFeature(unit_of_work=uow).execute(
        CreateMemberRequest(
            contact_number="C-000006",
            member_number="M-0006",
            first_name="Finn",
            last_name="Krogh",
            join_date=date(2026, 2, 2),
        )
    )

    response = GetMemberFeature(unit_of_work=uow).execute(
        GetMemberRequest(member_id=created.member.member_id)
    )

    assert response.member.member_number == "M-0006"
