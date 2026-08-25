from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID

import pytest

from mfm.application.workflows.enroll_member_workflow import EnrollMemberWorkflow
from mfm.application.workflows.enroll_member_workflow import EnrollMemberWorkflowInput
from mfm.application.workflows.enroll_member_workflow import NoActiveContingentPlanError
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency as ContingentCurrency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money as ContingentMoney
from mfm.domain.finance.invoice import Invoice
from mfm.domain.member.exceptions import DuplicateMemberNumberError
from mfm.domain.member.member import Member
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType
from mfm.domain.accounting.journal_entry import JournalEntry


class InMemoryContactRepository:
    def __init__(self) -> None:
        self.contacts: dict[UUID, Contact] = {}

    def add(self, contact: Contact) -> None:
        self.contacts[contact.id] = contact

    def delete(self, contact_id: UUID) -> None:
        self.contacts.pop(contact_id, None)


class InMemoryMemberRepository:
    def __init__(self) -> None:
        self.members_by_id: dict[UUID, Member] = {}
        self.members_by_number: dict[str, Member] = {}

    def add(self, member: Member) -> None:
        self.members_by_id[member.id] = member
        self.members_by_number[member.member_number] = member

    def get_by_number(self, member_number: str) -> Member | None:
        return self.members_by_number.get(member_number)

    def delete(self, member_id: UUID) -> None:
        member = self.members_by_id.pop(member_id, None)
        if member is not None:
            self.members_by_number.pop(member.member_number, None)


class InMemoryMembershipRepository:
    def __init__(self) -> None:
        self.memberships: dict[UUID, Membership] = {}

    def add(self, membership: Membership) -> None:
        self.memberships[membership.id] = membership

    def list_by_member(self, member_id: UUID) -> list[Membership]:
        return [m for m in self.memberships.values() if m.member_id == member_id]

    def delete(self, membership_id: UUID) -> None:
        self.memberships.pop(membership_id, None)


class InMemoryContingentRepository:
    def __init__(self, plans: list[ContingentPlan] | None = None) -> None:
        self.plans = plans or []

    def get_active_for_membership_type(
        self,
        membership_type_id: UUID,
        at_date: date,
    ) -> ContingentPlan | None:
        for plan in self.plans:
            if plan.membership_type_id == membership_type_id and plan.is_active_on(at_date):
                return plan
        return None


class InMemoryInvoiceRepository:
    def __init__(self) -> None:
        self.invoices: dict[UUID, Invoice] = {}
        self.fail_on_add = False

    def add(self, invoice: Invoice) -> None:
        if self.fail_on_add:
            raise RuntimeError("invoice add failed")
        self.invoices[invoice.id] = invoice

    def list_by_member(self, member_id: UUID) -> list[Invoice]:
        return [i for i in self.invoices.values() if i.member_id == member_id]

    def delete(self, invoice_id: UUID) -> None:
        self.invoices.pop(invoice_id, None)


class InMemoryJournalRepository:
    def __init__(self) -> None:
        self.journals: dict[UUID, JournalEntry] = {}
        self.fail_on_add = False

    def add(self, journal: JournalEntry) -> None:
        if self.fail_on_add:
            raise RuntimeError("journal add failed")
        self.journals[journal.id] = journal

    def list_by_reference(self, reference: str) -> list[JournalEntry]:
        return [j for j in self.journals.values() if j.reference == reference]

    def delete(self, journal_id: UUID) -> None:
        self.journals.pop(journal_id, None)


def _contact(number: str = "C-200001") -> Contact:
    return Contact(party=Person(first_name="Hans", last_name="Hansen"), contact_number=number)


def _membership_type(code: str = "STANDARD") -> MembershipType:
    return MembershipType(code=code, name=code.title())


def _contingent_plan(membership_type: MembershipType) -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=ContingentMoney(amount=Decimal("299.00"), currency=ContingentCurrency.DKK),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.MONTHLY, due_days=8),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )


def _workflow(
    *,
    contingent_repo: InMemoryContingentRepository,
    contact_repo: InMemoryContactRepository | None = None,
    member_repo: InMemoryMemberRepository | None = None,
    membership_repo: InMemoryMembershipRepository | None = None,
    invoice_repo: InMemoryInvoiceRepository | None = None,
    journal_repo: InMemoryJournalRepository | None = None,
) -> tuple[
    EnrollMemberWorkflow,
    InMemoryContactRepository,
    InMemoryMemberRepository,
    InMemoryMembershipRepository,
    InMemoryInvoiceRepository,
    InMemoryJournalRepository,
]:
    c_repo = contact_repo or InMemoryContactRepository()
    m_repo = member_repo or InMemoryMemberRepository()
    ms_repo = membership_repo or InMemoryMembershipRepository()
    i_repo = invoice_repo or InMemoryInvoiceRepository()
    j_repo = journal_repo or InMemoryJournalRepository()

    return (
        EnrollMemberWorkflow(
            contact_repository=c_repo,
            member_repository=m_repo,
            membership_repository=ms_repo,
            contingent_repository=contingent_repo,
            invoice_repository=i_repo,
            journal_repository=j_repo,
        ),
        c_repo,
        m_repo,
        ms_repo,
        i_repo,
        j_repo,
    )


def test_successful_enrollment():
    membership_type = _membership_type("STANDARD")
    workflow, contact_repo, member_repo, membership_repo, invoice_repo, journal_repo = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)])
    )

    result = workflow.execute(
        EnrollMemberWorkflowInput(
            contact=_contact("C-200010"),
            member_number="M-900001",
            membership_type=membership_type,
            enrollment_date=date(2026, 1, 15),
        )
    )

    assert result.success is True
    assert result.idempotent is False
    assert result.member is not None
    assert len(contact_repo.contacts) == 1
    assert len(member_repo.members_by_id) == 1
    assert len(membership_repo.memberships) == 1
    assert len(invoice_repo.invoices) == 1
    assert len(journal_repo.journals) == 1


def test_duplicate_member():
    membership_type = _membership_type("STANDARD")
    contact_repo = InMemoryContactRepository()
    member_repo = InMemoryMemberRepository()
    existing = Member(contact_id=_contact("C-200011").id, member_number="M-900002")
    member_repo.add(existing)

    workflow, _, _, _, _, _ = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)]),
        contact_repo=contact_repo,
        member_repo=member_repo,
    )

    with pytest.raises(DuplicateMemberNumberError):
        workflow.execute(
            EnrollMemberWorkflowInput(
                contact=_contact("C-200012"),
                member_number="M-900002",
                membership_type=membership_type,
                enrollment_date=date(2026, 1, 15),
            )
        )


def test_no_contingent_plan():
    membership_type = _membership_type("STANDARD")
    workflow, _, _, _, _, _ = _workflow(contingent_repo=InMemoryContingentRepository([]))

    with pytest.raises(NoActiveContingentPlanError):
        workflow.execute(
            EnrollMemberWorkflowInput(
                contact=_contact("C-200013"),
                member_number="M-900003",
                membership_type=membership_type,
                enrollment_date=date(2026, 1, 15),
            )
        )


def test_invoice_creation():
    membership_type = _membership_type("PREMIUM")
    workflow, _, _, _, invoice_repo, _ = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)])
    )

    result = workflow.execute(
        EnrollMemberWorkflowInput(
            contact=_contact("C-200014"),
            member_number="M-900004",
            membership_type=membership_type,
            enrollment_date=date(2026, 1, 20),
            invoice_number="INV-CUSTOM-1",
        )
    )

    assert result.invoice is not None
    assert result.invoice.total.amount == Decimal("299.00")
    assert len(invoice_repo.invoices) == 1


def test_journal_draft_creation():
    membership_type = _membership_type("BASIC")
    workflow, _, _, _, _, journal_repo = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)])
    )

    result = workflow.execute(
        EnrollMemberWorkflowInput(
            contact=_contact("C-200015"),
            member_number="M-900005",
            membership_type=membership_type,
            enrollment_date=date(2026, 1, 20),
            journal_number="JRN-CUSTOM-1",
        )
    )

    assert result.journal is not None
    assert result.journal.status is result.journal.status.DRAFT
    assert len(journal_repo.journals) == 1


def test_rollback_on_failure():
    membership_type = _membership_type("STANDARD")
    journal_repo = InMemoryJournalRepository()
    journal_repo.fail_on_add = True
    workflow, contact_repo, member_repo, membership_repo, invoice_repo, _ = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)]),
        journal_repo=journal_repo,
    )

    with pytest.raises(RuntimeError):
        workflow.execute(
            EnrollMemberWorkflowInput(
                contact=_contact("C-200016"),
                member_number="M-900006",
                membership_type=membership_type,
                enrollment_date=date(2026, 1, 20),
            )
        )

    assert len(contact_repo.contacts) == 0
    assert len(member_repo.members_by_id) == 0
    assert len(membership_repo.memberships) == 0
    assert len(invoice_repo.invoices) == 0
    assert len(journal_repo.journals) == 0


def test_idempotency():
    membership_type = _membership_type("STANDARD")
    workflow, contact_repo, member_repo, membership_repo, invoice_repo, journal_repo = _workflow(
        contingent_repo=InMemoryContingentRepository([_contingent_plan(membership_type)])
    )

    first = workflow.execute(
        EnrollMemberWorkflowInput(
            contact=_contact("C-200017"),
            member_number="M-900007",
            membership_type=membership_type,
            enrollment_date=date(2026, 1, 20),
        )
    )
    second = workflow.execute(
        EnrollMemberWorkflowInput(
            contact=_contact("C-200018"),
            member_number="M-900007",
            membership_type=membership_type,
            enrollment_date=date(2026, 1, 20),
        )
    )

    assert first.success is True
    assert second.success is True
    assert second.idempotent is True
    assert len(contact_repo.contacts) == 1
    assert len(member_repo.members_by_id) == 1
    assert len(membership_repo.memberships) == 1
    assert len(invoice_repo.invoices) == 1
    assert len(journal_repo.journals) == 1
