"""Member enrollment feature orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from typing import Callable
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.finance.currency import Currency as FinanceCurrency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.money import Money as FinanceMoney
from mfm.domain.member.member import Member
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType


class ApplicationException(Exception):
    """Base exception for application-level feature failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class CreateMemberRequest:
    contact_number: str
    first_name: str
    last_name: str
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    join_date: date
    middle_name: str = ""
    title: str = ""

    def validate(self) -> None:
        if not isinstance(self.contact_number, str) or not self.contact_number.strip():
            raise ValidationException("contact_number must be a non-empty string")
        if not isinstance(self.first_name, str) or not self.first_name.strip():
            raise ValidationException("first_name must be a non-empty string")
        if not isinstance(self.last_name, str) or not self.last_name.strip():
            raise ValidationException("last_name must be a non-empty string")
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be a UUID")
        if not isinstance(self.membership_type_code, str) or not self.membership_type_code.strip():
            raise ValidationException("membership_type_code must be a non-empty string")
        if not isinstance(self.membership_type_name, str) or not self.membership_type_name.strip():
            raise ValidationException("membership_type_name must be a non-empty string")
        if not isinstance(self.join_date, date):
            raise ValidationException("join_date must be a date")


@dataclass(frozen=True, slots=True)
class CreateMemberResponse:
    member_id: UUID
    member_number: str
    invoice_id: UUID
    journal_id: UUID


@dataclass(slots=True)
class MemberEnrolledEvent(DomainEvent):
    member_id: UUID = field(default_factory=uuid4)
    member_number: str = ""
    invoice_id: UUID = field(default_factory=uuid4)
    journal_id: UUID = field(default_factory=uuid4)


class ContactRepository(Protocol):
    def add(self, contact: Contact) -> None: ...


class MemberRepository(Protocol):
    def add(self, member: Member) -> None: ...

    def get_by_number(self, member_number: str) -> Member | None: ...


class MembershipRepository(Protocol):
    def add(self, membership: Membership) -> None: ...


class ContingentRepository(Protocol):
    def get_active_for_membership_type(
        self,
        membership_type_id: UUID,
        at_date: date,
    ) -> ContingentPlan | None: ...


class InvoiceRepository(Protocol):
    def add(self, invoice: Invoice) -> None: ...


class JournalRepository(Protocol):
    def add(self, journal: JournalEntry) -> None: ...


class MemberEnrollmentFeature:
    """Enroll a member by orchestrating domain operations across repositories."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
        member_number_factory: Callable[[CreateMemberRequest], str] | None = None,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher
        self._member_number_factory = member_number_factory or self._default_member_number

    def execute(self, request: CreateMemberRequest) -> CreateMemberResponse:
        request.validate()
        try:
            with self._unit_of_work as uow:
                contact_repository: ContactRepository = uow.contact_repository
                member_repository: MemberRepository = uow.member_repository
                membership_repository: MembershipRepository = uow.membership_repository
                contingent_repository: ContingentRepository = uow.contingent_repository
                invoice_repository: InvoiceRepository = uow.invoice_repository
                journal_repository: JournalRepository = uow.journal_repository

                contact = Contact(
                    party=Person(
                        first_name=request.first_name,
                        last_name=request.last_name,
                        middle_name=request.middle_name,
                        title=request.title,
                    ),
                    contact_number=request.contact_number,
                )
                contact_repository.add(contact)

                membership_type = MembershipType(
                    id=request.membership_type_id,
                    code=request.membership_type_code,
                    name=request.membership_type_name,
                )

                member_number = self._member_number_factory(request)
                if member_repository.get_by_number(member_number) is not None:
                    raise BusinessRuleViolation(
                        f"Member number {member_number} already exists"
                    )

                member = Member(
                    contact_id=contact.id,
                    member_number=member_number,
                    join_date=request.join_date,
                )
                member_repository.add(member)

                membership = Membership(
                    member_id=member.id,
                    membership_type=membership_type,
                    start_date=request.join_date,
                )
                membership_repository.add(membership)

                contingent_plan = contingent_repository.get_active_for_membership_type(
                    membership_type.id,
                    request.join_date,
                )
                if contingent_plan is None:
                    raise BusinessRuleViolation(
                        "No active contingent plan for the selected membership type"
                    )

                invoice_total = FinanceMoney(
                    amount=contingent_plan.amount,
                    currency=FinanceCurrency(contingent_plan.currency.value),
                )
                invoice = Invoice(
                    invoice_number=InvoiceNumber(
                        f"INV-{member.member_number}-{request.join_date:%Y%m%d}"
                    ),
                    member_id=member.id,
                    issue_date=request.join_date,
                    due_date=request.join_date
                    + timedelta(days=contingent_plan.invoice_rule.due_days),
                    lines=[
                        InvoiceLine(
                            description=(
                                f"{membership_type.name} enrollment contingent"
                            ),
                            quantity=Decimal("1"),
                            unit_price=invoice_total,
                        )
                    ],
                )
                invoice_repository.add(invoice)

                journal = JournalEntry(
                    journal_number=f"JRN-{member.member_number}-{request.join_date:%Y%m%d}",
                    posting_date=request.join_date,
                    description=f"Enrollment draft for member {member.member_number}",
                    reference=str(invoice.invoice_number),
                    lines=[
                        JournalLine(
                            account_id=uuid4(),
                            side=PostingSide.DEBIT,
                            amount=invoice.total,
                            description="Accounts receivable",
                        ),
                        JournalLine(
                            account_id=uuid4(),
                            side=PostingSide.CREDIT,
                            amount=invoice.total,
                            description="Membership revenue",
                        ),
                    ],
                )
                journal_repository.add(journal)

                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Member enrollment failed") from exc

        self._dispatcher.dispatch(
            MemberEnrolledEvent(
                member_id=member.id,
                member_number=member.member_number,
                invoice_id=invoice.id,
                journal_id=journal.id,
            )
        )

        return CreateMemberResponse(
            member_id=member.id,
            member_number=member.member_number,
            invoice_id=invoice.id,
            journal_id=journal.id,
        )

    @staticmethod
    def _default_member_number(request: CreateMemberRequest) -> str:
        today = datetime.now(UTC).strftime("%H%M%S")
        return f"M-{request.join_date:%Y%m%d}-{today}"


class CreateMemberFeature(MemberEnrollmentFeature):
    """Public feature name following the standard naming convention."""


# Backward-compat aliases for transition.
EnrollmentRequest = CreateMemberRequest
EnrollmentResult = CreateMemberResponse
NoActiveContingentPlanError = BusinessRuleViolation
