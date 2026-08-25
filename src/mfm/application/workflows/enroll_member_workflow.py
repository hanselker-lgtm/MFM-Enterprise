"""Enroll member application workflow."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from typing import Protocol
from typing import runtime_checkable
from uuid import UUID
from uuid import uuid4

from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.contact.contact import Contact
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.finance.currency import Currency as FinanceCurrency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.money import Money as FinanceMoney
from mfm.domain.member.exceptions import DuplicateMemberNumberError
from mfm.domain.member.member import Member
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


class NoActiveContingentPlanError(Exception):
    """Raised when no active contingent plan exists for the selected membership type."""


@runtime_checkable
class ContactRepository(Protocol):
    def add(self, contact: Contact) -> None: ...

    def delete(self, contact_id: UUID) -> None: ...


@runtime_checkable
class MemberRepository(Protocol):
    def add(self, member: Member) -> None: ...

    def get_by_number(self, member_number: str) -> Member | None: ...

    def delete(self, member_id: UUID) -> None: ...


@runtime_checkable
class MembershipRepository(Protocol):
    def add(self, membership: Membership) -> None: ...

    def list_by_member(self, member_id: UUID) -> list[Membership]: ...

    def delete(self, membership_id: UUID) -> None: ...


@runtime_checkable
class ContingentRepository(Protocol):
    def get_active_for_membership_type(
        self,
        membership_type_id: UUID,
        at_date: date,
    ) -> ContingentPlan | None: ...


@runtime_checkable
class InvoiceRepository(Protocol):
    def add(self, invoice: Invoice) -> None: ...

    def list_by_member(self, member_id: UUID) -> list[Invoice]: ...

    def delete(self, invoice_id: UUID) -> None: ...


@runtime_checkable
class JournalRepository(Protocol):
    def add(self, journal: JournalEntry) -> None: ...

    def list_by_reference(self, reference: str) -> list[JournalEntry]: ...

    def delete(self, journal_id: UUID) -> None: ...


@dataclass(slots=True)
class EnrollMemberWorkflowInput:
    contact: Contact
    member_number: str
    membership_type: MembershipType
    enrollment_date: date | None = None
    invoice_number: str | None = None
    journal_number: str | None = None
    receivable_account_id: UUID | None = None
    revenue_account_id: UUID | None = None


@dataclass(slots=True)
class EnrollMemberWorkflowResult:
    success: bool
    contact: Contact | None = None
    member: Member | None = None
    membership: Membership | None = None
    contingent_plan: ContingentPlan | None = None
    invoice: Invoice | None = None
    journal: JournalEntry | None = None
    idempotent: bool = False
    message: str = ""


class EnrollMemberWorkflow:
    """Orchestrates member enrollment across contact, member, finance, and accounting."""

    def __init__(
        self,
        *,
        contact_repository: ContactRepository,
        member_repository: MemberRepository,
        membership_repository: MembershipRepository,
        contingent_repository: ContingentRepository,
        invoice_repository: InvoiceRepository,
        journal_repository: JournalRepository,
    ) -> None:
        self._contact_repository = contact_repository
        self._member_repository = member_repository
        self._membership_repository = membership_repository
        self._contingent_repository = contingent_repository
        self._invoice_repository = invoice_repository
        self._journal_repository = journal_repository

    def execute(self, data: EnrollMemberWorkflowInput) -> EnrollMemberWorkflowResult:
        enrollment_date = data.enrollment_date or datetime.now(UTC).date()

        existing_member = self._member_repository.get_by_number(data.member_number)
        if existing_member is not None:
            existing_memberships = self._membership_repository.list_by_member(existing_member.id)
            existing_membership = next(
                (
                    membership
                    for membership in existing_memberships
                    if membership.status is MembershipStatus.ACTIVE
                    and membership.membership_type_id == data.membership_type.id
                ),
                None,
            )
            if existing_membership is not None:
                existing_invoices = self._invoice_repository.list_by_member(existing_member.id)
                existing_invoice = existing_invoices[-1] if existing_invoices else None
                existing_journal = None
                if existing_invoice is not None:
                    journals = self._journal_repository.list_by_reference(
                        str(existing_invoice.invoice_number)
                    )
                    existing_journal = journals[-1] if journals else None

                return EnrollMemberWorkflowResult(
                    success=True,
                    contact=None,
                    member=existing_member,
                    membership=existing_membership,
                    contingent_plan=None,
                    invoice=existing_invoice,
                    journal=existing_journal,
                    idempotent=True,
                    message="Enrollment already exists",
                )

            raise DuplicateMemberNumberError(
                f"Member number {data.member_number} already exists"
            )

        rollback_actions: list[callable] = []

        try:
            self._contact_repository.add(data.contact)
            rollback_actions.append(lambda: self._contact_repository.delete(data.contact.id))

            member = Member(contact_id=data.contact.id, member_number=data.member_number)
            self._member_repository.add(member)
            rollback_actions.append(lambda: self._member_repository.delete(member.id))

            membership = Membership(
                member_id=member.id,
                membership_type=data.membership_type,
                start_date=enrollment_date,
            )
            self._membership_repository.add(membership)
            rollback_actions.append(
                lambda: self._membership_repository.delete(membership.id)
            )

            contingent_plan = self._contingent_repository.get_active_for_membership_type(
                data.membership_type.id,
                enrollment_date,
            )
            if contingent_plan is None:
                raise NoActiveContingentPlanError(
                    f"No active contingent plan for membership type {data.membership_type.id}"
                )

            unit_price = FinanceMoney(
                amount=contingent_plan.amount,
                currency=FinanceCurrency(contingent_plan.currency.value),
            )
            invoice_line = InvoiceLine(
                description=f"{data.membership_type.name} membership enrollment",
                quantity=Decimal("1"),
                unit_price=unit_price,
            )

            invoice_number = data.invoice_number or (
                f"INV-{data.member_number}-{enrollment_date:%Y%m%d}"
            )
            due_date = enrollment_date + timedelta(
                days=contingent_plan.invoice_rule.due_days
            )
            invoice = Invoice(
                invoice_number=InvoiceNumber(invoice_number),
                member_id=member.id,
                issue_date=enrollment_date,
                due_date=due_date,
                lines=[invoice_line],
            )
            self._invoice_repository.add(invoice)
            rollback_actions.append(lambda: self._invoice_repository.delete(invoice.id))

            receivable_account_id = data.receivable_account_id or uuid4()
            revenue_account_id = data.revenue_account_id or uuid4()
            journal_number = data.journal_number or (
                f"JRN-{data.member_number}-{enrollment_date:%Y%m%d}"
            )
            journal = JournalEntry(
                journal_number=journal_number,
                posting_date=enrollment_date,
                description=(
                    f"Enrollment journal draft for member {data.member_number}"
                ),
                reference=str(invoice.invoice_number),
                status=JournalEntryStatus.DRAFT,
                lines=[
                    JournalLine(
                        account_id=receivable_account_id,
                        side=PostingSide.DEBIT,
                        amount=invoice.total,
                        description="Accounts receivable",
                    ),
                    JournalLine(
                        account_id=revenue_account_id,
                        side=PostingSide.CREDIT,
                        amount=invoice.total,
                        description="Membership revenue",
                    ),
                ],
            )
            self._journal_repository.add(journal)
            rollback_actions.append(lambda: self._journal_repository.delete(journal.id))

            return EnrollMemberWorkflowResult(
                success=True,
                contact=data.contact,
                member=member,
                membership=membership,
                contingent_plan=contingent_plan,
                invoice=invoice,
                journal=journal,
                idempotent=False,
                message="Enrollment completed",
            )
        except Exception:
            for action in reversed(rollback_actions):
                try:
                    action()
                except Exception:
                    continue
            raise
