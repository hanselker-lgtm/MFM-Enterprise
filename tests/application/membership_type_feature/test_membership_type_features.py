from __future__ import annotations

from uuid import UUID

import pytest

from mfm.application.features.membership_type import (
    BusinessRuleViolation,
    CreateMembershipTypeFeature,
    CreateMembershipTypeRequest,
    ListMembershipTypesFeature,
    ListMembershipTypesRequest,
    ValidationException,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.membership.membership_type import MembershipType


class InMemoryMembershipTypeRepository:
    def __init__(self, store: dict[UUID, MembershipType]) -> None:
        self._store = store

    def add(self, membership_type: MembershipType) -> None:
        for existing in self._store.values():
            if existing.code == membership_type.code:
                raise ValueError(f"Membership type code {membership_type.code} already exists")
        self._store[membership_type.id] = membership_type

    def list(self) -> list[MembershipType]:
        return list(self._store.values())


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        super().__init__()
        self._membership_types: dict[UUID, MembershipType] = {}

    def _start_scope(self) -> None:
        self.membership_type_repository = InMemoryMembershipTypeRepository(self._membership_types)

    def _commit_impl(self) -> None:
        pass

    def _rollback_impl(self) -> None:
        pass

    def _flush_impl(self) -> None:
        pass

    def _close_impl(self) -> None:
        pass


def test_create_membership_type_succeeds() -> None:
    uow = FakeUnitOfWork()
    response = CreateMembershipTypeFeature(unit_of_work=uow).execute(
        CreateMembershipTypeRequest(code="STANDARD", name="Standard Membership")
    )

    assert response.membership_type.code == "STANDARD"
    assert response.membership_type.category == "GENERAL"
    assert response.membership_type.is_active is True


def test_create_membership_type_rejects_invalid_category() -> None:
    uow = FakeUnitOfWork()

    with pytest.raises(ValidationException):
        CreateMembershipTypeFeature(unit_of_work=uow).execute(
            CreateMembershipTypeRequest(code="X", name="X", category="NOT_A_CATEGORY")
        )


def test_create_membership_type_rejects_duplicate_code() -> None:
    uow = FakeUnitOfWork()
    feature = CreateMembershipTypeFeature(unit_of_work=uow)
    feature.execute(CreateMembershipTypeRequest(code="YOUTH", name="Youth"))

    with pytest.raises(BusinessRuleViolation):
        feature.execute(CreateMembershipTypeRequest(code="YOUTH", name="Youth Again"))


def test_list_membership_types_returns_created_types() -> None:
    uow = FakeUnitOfWork()
    CreateMembershipTypeFeature(unit_of_work=uow).execute(
        CreateMembershipTypeRequest(code="SENIOR", name="Senior", category="SENIOR")
    )

    response = ListMembershipTypesFeature(unit_of_work=uow).execute(
        ListMembershipTypesRequest()
    )

    assert len(response.membership_types) == 1
    assert response.membership_types[0].code == "SENIOR"


def test_list_membership_types_active_only_filters_inactive() -> None:
    uow = FakeUnitOfWork()
    CreateMembershipTypeFeature(unit_of_work=uow).execute(
        CreateMembershipTypeRequest(code="ACTIVE1", name="Active One")
    )

    response = ListMembershipTypesFeature(unit_of_work=uow).execute(
        ListMembershipTypesRequest(active_only=True)
    )

    assert len(response.membership_types) == 1
