from __future__ import annotations
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.membership_type.create_membership_type_use_case import (
    CreateMembershipTypeUseCase,
)
from mfm.application.membership_type.delete_membership_type_use_case import (
    DeleteMembershipTypeUseCase,
)
from mfm.application.membership_type.get_membership_type_use_case import (
    GetMembershipTypeUseCase,
)
from mfm.application.membership_type.list_membership_types_use_case import (
    ListMembershipTypesUseCase,
)
from mfm.application.membership_type.update_membership_type_use_case import (
    UpdateMembershipTypeUseCase,
)
from mfm.domain.membership.exceptions import (
    DuplicateMembershipTypeCodeError,
    MembershipTypeNotFoundError,
)
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class InMemoryMembershipTypeRepository(MembershipTypeRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, MembershipType] = {}

    def add(self, membership_type: MembershipType) -> None:
        self._items[membership_type.id] = membership_type

    def update(self, membership_type: MembershipType) -> None:
        self._items[membership_type.id] = membership_type

    def get(self, membership_type_id: UUID) -> MembershipType | None:
        return self._items.get(membership_type_id)

    def get_by_code(self, code: str) -> MembershipType | None:
        normalized = code.strip().upper()
        for item in self._items.values():
            if item.code == normalized:
                return item
        return None

    def list(self) -> list[MembershipType]:
        return list(self._items.values())

    def exists(self, membership_type_id: UUID) -> bool:
        return membership_type_id in self._items

    def delete(self, membership_type_id: UUID) -> None:
        self._items.pop(membership_type_id, None)


def test_create_membership_type_use_case_success():
    repository = InMemoryMembershipTypeRepository()
    use_case = CreateMembershipTypeUseCase(repository)

    membership_type = MembershipType(code="STANDARD", name="Standard")

    created = use_case.execute(membership_type)

    assert created is membership_type
    assert repository.get_by_code("STANDARD") is membership_type


def test_create_membership_type_use_case_rejects_duplicate_code():
    repository = InMemoryMembershipTypeRepository()
    use_case = CreateMembershipTypeUseCase(repository)

    first = MembershipType(code="VIP", name="VIP")
    second = MembershipType(code="VIP", name="VIP 2")

    use_case.execute(first)

    with pytest.raises(DuplicateMembershipTypeCodeError):
        use_case.execute(second)


def test_get_membership_type_use_case_by_id_and_code():
    repository = InMemoryMembershipTypeRepository()
    use_case = GetMembershipTypeUseCase(repository)
    membership_type = MembershipType(code="YOUTH", name="Youth")
    repository.add(membership_type)

    assert use_case.execute_by_id(membership_type.id).id == membership_type.id
    assert use_case.execute_by_code(" youth ").id == membership_type.id


def test_get_membership_type_use_case_rejects_missing_membership_type():
    repository = InMemoryMembershipTypeRepository()
    use_case = GetMembershipTypeUseCase(repository)

    with pytest.raises(MembershipTypeNotFoundError):
        use_case.execute_by_id(uuid4())


def test_update_membership_type_use_case_success_and_uniqueness_check():
    repository = InMemoryMembershipTypeRepository()
    use_case = UpdateMembershipTypeUseCase(repository)

    standard = MembershipType(code="STANDARD", name="Standard")
    vip = MembershipType(code="VIP", name="VIP")
    repository.add(standard)
    repository.add(vip)

    standard.rename(name="Standard Plus", description="Default plan")
    updated = use_case.execute(standard)

    assert updated.name == "Standard Plus"

    standard.code = "VIP"
    with pytest.raises(DuplicateMembershipTypeCodeError):
        use_case.execute(standard)


def test_delete_membership_type_use_case_success_and_not_found():
    repository = InMemoryMembershipTypeRepository()
    use_case = DeleteMembershipTypeUseCase(repository)

    membership_type = MembershipType(code="BASIC", name="Basic")
    repository.add(membership_type)

    assert use_case.execute(membership_type.id) is True
    assert repository.get(membership_type.id) is None

    with pytest.raises(MembershipTypeNotFoundError):
        use_case.execute(membership_type.id)


def test_list_membership_types_use_case_supports_sort_filter_and_paging():
    repository = InMemoryMembershipTypeRepository()
    use_case = ListMembershipTypesUseCase(repository)

    vip = MembershipType(code="VIP", name="VIP")
    youth = MembershipType(code="YOUTH", name="Youth")
    basic = MembershipType(code="BASIC", name="Basic")
    youth.deactivate()
    repository.add(vip)
    repository.add(youth)
    repository.add(basic)

    listed = use_case.execute(sort_by="code")
    assert [item.code for item in listed] == ["BASIC", "VIP", "YOUTH"]

    active_only = use_case.execute(active_only=True, sort_by="code")
    assert [item.code for item in active_only] == ["BASIC", "VIP"]

    paged = use_case.execute(sort_by="code", offset=1, limit=1)
    assert [item.code for item in paged] == ["VIP"]
