"""Controller for the Memberships workspace."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.members import (
    CreateMemberRequest,
    GetMemberRequest,
    ListMembersRequest,
)
from mfm.application.features.membership.manage_membership_feature import (
    ManageMembershipRequest,
)
from mfm.application.features.membership_type import (
    ListMembershipTypesRequest,
)
from mfm.presentation.memberships.membership_viewmodels import (
    CreateMemberCommandViewModel,
    MemberDetailViewModel,
    MemberListItemViewModel,
    MemberListViewModel,
    MembershipRecordViewModel,
    MembershipTypeOptionViewModel,
    RegisterMembershipCommandViewModel,
)


class CreateMemberPort(Protocol):
    def execute(self, request: CreateMemberRequest): ...


class ListMembersPort(Protocol):
    def execute(self, request: ListMembersRequest): ...


class GetMemberPort(Protocol):
    def execute(self, request: GetMemberRequest): ...


class ListMembershipTypesPort(Protocol):
    def execute(self, request: ListMembershipTypesRequest): ...


class ManageMembershipPort(Protocol):
    def execute(self, request: ManageMembershipRequest): ...


class MembershipController:
    """UI controller that orchestrates member and membership features."""

    def __init__(
        self,
        *,
        create_member_feature: CreateMemberPort,
        list_members_feature: ListMembersPort,
        get_member_feature: GetMemberPort,
        list_membership_types_feature: ListMembershipTypesPort,
        manage_membership_feature: ManageMembershipPort,
    ) -> None:
        self._create_member = create_member_feature
        self._list_members = list_members_feature
        self._get_member = get_member_feature
        self._list_membership_types = list_membership_types_feature
        self._manage_membership = manage_membership_feature

    def load_member_list(self) -> MemberListViewModel:
        response = self._list_members.execute(ListMembersRequest())
        items = tuple(
            MemberListItemViewModel(
                member_id=member.member_id,
                member_number=member.member_number,
                display_name=member.display_name,
                status=member.status,
                join_date=member.join_date,
            )
            for member in response.members
        )
        return MemberListViewModel(items=items)

    def load_member_detail(self, member_id: UUID) -> MemberDetailViewModel:
        response = self._get_member.execute(GetMemberRequest(member_id=member_id))
        memberships = self._manage_membership.execute(
            ManageMembershipRequest(operation="list", member_id=member_id)
        ).memberships

        return MemberDetailViewModel(
            member_id=response.member.member_id,
            member_number=response.member.member_number,
            display_name=response.member.display_name,
            status=response.member.status,
            join_date=response.member.join_date,
            leave_date=response.member.leave_date,
            memberships=tuple(
                MembershipRecordViewModel(
                    membership_id=record.membership_id,
                    membership_type_code=record.membership_type_code,
                    membership_type_name=record.membership_type_name,
                    status=record.status,
                    start_date=record.start_date,
                    end_date=record.end_date,
                )
                for record in memberships
            ),
        )

    def load_membership_type_options(self) -> tuple[MembershipTypeOptionViewModel, ...]:
        response = self._list_membership_types.execute(
            ListMembershipTypesRequest(active_only=True)
        )
        return tuple(
            MembershipTypeOptionViewModel(
                membership_type_id=mt.membership_type_id, code=mt.code, name=mt.name
            )
            for mt in response.membership_types
        )

    def create_member(self, command: CreateMemberCommandViewModel) -> UUID:
        response = self._create_member.execute(
            CreateMemberRequest(
                contact_number=command.contact_number,
                member_number=command.member_number,
                first_name=command.first_name,
                last_name=command.last_name,
                join_date=command.join_date,
                middle_name=command.middle_name,
                title=command.title,
            )
        )
        return response.member.member_id

    def register_membership(self, command: RegisterMembershipCommandViewModel) -> UUID:
        response = self._manage_membership.execute(
            ManageMembershipRequest(
                operation="register",
                member_id=command.member_id,
                membership_type_id=command.membership_type_id,
                start_date=command.start_date,
            )
        )
        return response.memberships[0].membership_id
