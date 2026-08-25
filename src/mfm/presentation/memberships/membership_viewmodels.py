"""Pure view-model types for the Memberships workspace (no Qt imports)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True, slots=True)
class MemberListItemViewModel:
    member_id: UUID
    member_number: str
    display_name: str
    status: str
    join_date: date


@dataclass(frozen=True, slots=True)
class MemberListViewModel:
    items: tuple[MemberListItemViewModel, ...]


@dataclass(frozen=True, slots=True)
class MembershipRecordViewModel:
    membership_id: UUID
    membership_type_code: str
    membership_type_name: str
    status: str
    start_date: date
    end_date: date | None


@dataclass(frozen=True, slots=True)
class MemberDetailViewModel:
    member_id: UUID
    member_number: str
    display_name: str
    status: str
    join_date: date
    leave_date: date | None
    memberships: tuple[MembershipRecordViewModel, ...] = ()


@dataclass(frozen=True, slots=True)
class MembershipTypeOptionViewModel:
    membership_type_id: UUID
    code: str
    name: str


@dataclass(frozen=True, slots=True)
class CreateMemberCommandViewModel:
    contact_number: str
    member_number: str
    first_name: str
    last_name: str
    join_date: date
    middle_name: str = ""
    title: str = ""


@dataclass(frozen=True, slots=True)
class RegisterMembershipCommandViewModel:
    member_id: UUID
    membership_type_id: UUID
    start_date: date | None = None
