"""CreateMemberFeature: register a new member (and their contact record).

Follows the Public API Standard: immutable Request/Response DTOs,
no domain or SQLAlchemy types on the boundary, ApplicationException
hierarchy, execute(request) -> response.

This is a straightforward member registration -- it creates a Contact
and a Member in one transaction. It intentionally does not also
generate invoices/journal entries the way the richer
``mfm.application.features.member_enrollment.MemberEnrollmentFeature``
does; that workflow needs contingent-plan and invoicing infrastructure
this module does not depend on. Billing a new member's first
contingent is a separate, later step through the Membership Billing
area once that workspace exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.member.exceptions import (
    ContactReferenceNotFoundError,
    DuplicateMemberNumberError,
    InvalidMemberNumberError,
    InvalidMembershipDatesError,
    InvalidMemberReferenceError,
)
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class MemberDTO:
    member_id: UUID
    contact_id: UUID
    member_number: str
    display_name: str
    status: str
    join_date: date
    leave_date: date | None


@dataclass(frozen=True, slots=True)
class CreateMemberRequest:
    contact_number: str
    member_number: str
    first_name: str
    last_name: str
    join_date: date
    middle_name: str = ""
    title: str = ""

    def validate(self) -> None:
        for field_name, value in (
            ("contact_number", self.contact_number),
            ("member_number", self.member_number),
            ("first_name", self.first_name),
            ("last_name", self.last_name),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValidationException(f"{field_name} must be a non-empty string")
        if not isinstance(self.join_date, date):
            raise ValidationException("join_date must be a date")


@dataclass(frozen=True, slots=True)
class CreateMemberResponse:
    member: MemberDTO


def _to_member_dto(member: Member, *, display_name: str) -> MemberDTO:
    return MemberDTO(
        member_id=member.id,
        contact_id=member.contact_id,
        member_number=member.member_number,
        display_name=display_name,
        status=member.status.value,
        join_date=member.join_date,
        leave_date=member.leave_date,
    )


class CreateMemberFeature:
    """Public application entry point for registering a new member."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateMemberRequest) -> CreateMemberResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                contact = Contact(
                    party=Person(
                        first_name=request.first_name,
                        last_name=request.last_name,
                        middle_name=request.middle_name,
                        title=request.title,
                    ),
                    contact_number=request.contact_number,
                )
                uow.contact_repository.add(contact)

                member = Member(
                    contact_id=contact.id,
                    member_number=request.member_number,
                    status=MemberStatus.ACTIVE,
                    join_date=request.join_date,
                )
                uow.member_repository.add(member)
        except (InvalidMemberNumberError, InvalidMembershipDatesError, InvalidMemberReferenceError) as exc:
            raise ValidationException(str(exc)) from exc
        except (DuplicateMemberNumberError, ContactReferenceNotFoundError, ValueError) as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Create member feature failed") from exc

        return CreateMemberResponse(
            member=_to_member_dto(member, display_name=contact.party.display_name)
        )
