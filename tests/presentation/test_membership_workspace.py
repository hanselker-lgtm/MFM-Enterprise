from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID
from uuid import uuid4

from mfm.presentation.memberships.membership_controller import MembershipController
from mfm.presentation.memberships.membership_viewmodels import (
    CreateMemberCommandViewModel,
    RegisterMembershipCommandViewModel,
)
from mfm.presentation.memberships.membership_workspace import MembershipWorkspace


@dataclass(frozen=True, slots=True)
class _MemberDTO:
    member_id: UUID
    contact_id: UUID
    member_number: str
    display_name: str
    status: str
    join_date: date
    leave_date: date | None = None


class _FakeCreateMemberFeature:
    def __init__(self, store: dict[UUID, _MemberDTO]) -> None:
        self._store = store

    def execute(self, request):
        member_id = uuid4()
        dto = _MemberDTO(
            member_id=member_id,
            contact_id=uuid4(),
            member_number=request.member_number,
            display_name=f"{request.first_name} {request.last_name}",
            status="ACTIVE",
            join_date=request.join_date,
        )
        self._store[member_id] = dto

        class _Response:
            member = dto

        return _Response()


class _FakeListMembersFeature:
    def __init__(self, store: dict[UUID, _MemberDTO]) -> None:
        self._store = store

    def execute(self, request):
        class _Response:
            members = tuple(self._store.values())

        return _Response()


class _FakeGetMemberFeature:
    def __init__(self, store: dict[UUID, _MemberDTO]) -> None:
        self._store = store

    def execute(self, request):
        class _Response:
            member = self._store[request.member_id]

        return _Response()


class _FakeListMembershipTypesFeature:
    def execute(self, request):
        class _Type:
            membership_type_id = uuid4()
            code = "STANDARD"
            name = "Standard"

        class _Response:
            membership_types = (_Type(),)

        return _Response()


class _FakeManageMembershipFeature:
    def execute(self, request):
        class _Record:
            membership_id = uuid4()
            member_id = request.member_id
            membership_type_id = getattr(request, "membership_type_id", None)
            membership_type_code = "STANDARD"
            membership_type_name = "Standard"
            status = "ACTIVE"
            start_date = date.today()
            end_date = None

        class _Response:
            memberships = (_Record(),)

        return _Response()


def test_membership_workspace_builds_and_shows_created_member(qapp) -> None:
    store: dict[UUID, _MemberDTO] = {}
    controller = MembershipController(
        create_member_feature=_FakeCreateMemberFeature(store),
        list_members_feature=_FakeListMembersFeature(store),
        get_member_feature=_FakeGetMemberFeature(store),
        list_membership_types_feature=_FakeListMembershipTypesFeature(),
        manage_membership_feature=_FakeManageMembershipFeature(),
    )

    member_id = controller.create_member(
        CreateMemberCommandViewModel(
            contact_number="C-1",
            member_number="M-1",
            first_name="Test",
            last_name="Person",
            join_date=date.today(),
        )
    )

    workspace = MembershipWorkspace(controller=controller)

    assert workspace._list.count() == 1

    detail = controller.load_member_detail(member_id)
    assert detail.display_name == "Test Person"

    membership_id = controller.register_membership(
        RegisterMembershipCommandViewModel(
            member_id=member_id,
            membership_type_id=uuid4(),
        )
    )
    assert membership_id is not None
