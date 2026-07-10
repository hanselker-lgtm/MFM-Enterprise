from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.events.event_handler import EventHandler
from mfm.application.features.member_enrollment import BusinessRuleViolation
from mfm.application.features.member_enrollment import CreateMemberFeature
from mfm.application.features.member_enrollment import CreateMemberRequest
from mfm.application.features.member_enrollment import CreateMemberResponse
from mfm.application.features.member_enrollment import MemberEnrolledEvent
from mfm.application.features.member_enrollment import RepositoryException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency as ContingentCurrency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money as ContingentMoney
from mfm.domain.finance.invoice import Invoice
from mfm.domain.member.member import Member
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType
from mfm.domain.accounting.journal_entry import JournalEntry


def _contact(number: str) -> Contact:
    return Contact(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number=number,
    )


def _membership_type(code: str = "STANDARD") -> MembershipType:
    return MembershipType(code=code, name=code.title())


def _plan(membership_type: MembershipType) -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=ContingentMoney(
            amount=Decimal("399.00"),
            currency=ContingentCurrency.DKK,
        ),
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.YEARLY, due_days=10),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )


def _request(contact_number: str, membership_type: MembershipType, join_date: date) -> CreateMemberRequest:
    return CreateMemberRequest(
        contact_number=contact_number,
        first_name="Hans",
        last_name="Hansen",
        membership_type_id=membership_type.id,
        membership_type_code=membership_type.code,
        membership_type_name=membership_type.name,
        join_date=join_date,
    )


class InMemoryContactRepository:
    def __init__(self, store: dict[UUID, Contact]) -> None:
        self._store = store

    def add(self, contact: Contact) -> None:
        self._store[contact.id] = contact


class InMemoryMemberRepository:
    def __init__(self, store: dict[UUID, Member]) -> None:
        self._store = store

    def add(self, member: Member) -> None:
        self._store[member.id] = member

    def get_by_number(self, member_number: str) -> Member | None:
        for member in self._store.values():
            if member.member_number == member_number:
                return member
        return None


class InMemoryMembershipRepository:
    def __init__(self, store: dict[UUID, Membership]) -> None:
        self._store = store

    def add(self, membership: Membership) -> None:
        self._store[membership.id] = membership


class InMemoryContingentRepository:
    def __init__(self, plans: list[ContingentPlan] | None = None) -> None:
        self._plans = plans or []

    def get_active_for_membership_type(
        self,
        membership_type_id: UUID,
        at_date: date,
    ) -> ContingentPlan | None:
        for plan in self._plans:
            if plan.membership_type_id == membership_type_id and plan.is_active_on(at_date):
                return plan
        return None


class InMemoryInvoiceRepository:
    def __init__(self, store: dict[UUID, Invoice], *, fail_on_add: bool = False) -> None:
        self._store = store
        self._fail_on_add = fail_on_add

    def add(self, invoice: Invoice) -> None:
        if self._fail_on_add:
            raise RuntimeError("invoice add failed")
        self._store[invoice.id] = invoice


class InMemoryJournalRepository:
    def __init__(self, store: dict[UUID, JournalEntry]) -> None:
        self._store = store

    def add(self, journal: JournalEntry) -> None:
        self._store[journal.id] = journal


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity: Any) -> None:
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        plans: list[ContingentPlan],
        fail_invoice_add: bool = False,
    ) -> None:
        super().__init__()
        self._plans = plans
        self._fail_invoice_add = fail_invoice_add

        self.contacts: dict[UUID, Contact] = {}
        self.members: dict[UUID, Member] = {}
        self.memberships: dict[UUID, Membership] = {}
        self.invoices: dict[UUID, Invoice] = {}
        self.journals: dict[UUID, JournalEntry] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self._snapshot = (
            dict(self.contacts),
            dict(self.members),
            dict(self.memberships),
            dict(self.invoices),
            dict(self.journals),
        )

        self.contact_repository = InMemoryContactRepository(self.contacts)
        self.member_repository = InMemoryMemberRepository(self.members)
        self.membership_repository = InMemoryMembershipRepository(self.memberships)
        self.contingent_repository = InMemoryContingentRepository(self._plans)
        self.invoice_repository = InMemoryInvoiceRepository(
            self.invoices,
            fail_on_add=self._fail_invoice_add,
        )
        self.payment_repository = _NoopRepo()
        self.journal_repository = InMemoryJournalRepository(self.journals)

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        contacts, members, memberships, invoices, journals = self._snapshot
        self.contacts.clear()
        self.contacts.update(contacts)
        self.members.clear()
        self.members.update(members)
        self.memberships.clear()
        self.memberships.update(memberships)
        self.invoices.clear()
        self.invoices.update(invoices)
        self.journals.clear()
        self.journals.update(journals)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[MemberEnrolledEvent] = []

    def handle(self, event) -> None:
        if isinstance(event, MemberEnrolledEvent):
            self.events.append(event)


def _build_feature(
    *,
    plans: list[ContingentPlan],
    member_number: str,
    fail_invoice_add: bool = False,
) -> tuple[MemberEnrollmentFeature, FakeUnitOfWork, EventCollector]:
    uow = FakeUnitOfWork(plans=plans, fail_invoice_add=fail_invoice_add)
    dispatcher = DomainEventDispatcher()
    collector = EventCollector()
    dispatcher.register(MemberEnrolledEvent, collector)

    feature = CreateMemberFeature(
        unit_of_work=uow,
        dispatcher=dispatcher,
        member_number_factory=lambda _request: member_number,
    )
    return feature, uow, collector


def test_happy_path():
    membership_type = _membership_type("STANDARD")
    feature, uow, _ = _build_feature(plans=[_plan(membership_type)], member_number="M-100001")

    result = feature.execute(
        _request("C-300001", membership_type, date(2026, 1, 15))
    )

    assert isinstance(result, CreateMemberResponse)
    assert result.member_number == "M-100001"
    assert len(uow.contacts) == 1
    assert len(uow.members) == 1
    assert len(uow.memberships) == 1
    assert len(uow.invoices) == 1
    assert len(uow.journals) == 1
    assert uow.commits == 1


def test_duplicate_member():
    membership_type = _membership_type("STANDARD")
    feature, uow, _ = _build_feature(plans=[_plan(membership_type)], member_number="M-100002")

    existing_member = Member(contact_id=uuid4(), member_number="M-100002")
    uow.members[existing_member.id] = existing_member

    with pytest.raises(BusinessRuleViolation):
        feature.execute(
            _request("C-300002", membership_type, date(2026, 1, 15))
        )

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.members) == 1
    assert len(uow.invoices) == 0


def test_missing_contingent_plan():
    membership_type = _membership_type("STANDARD")
    feature, uow, _ = _build_feature(plans=[], member_number="M-100003")

    with pytest.raises(BusinessRuleViolation):
        feature.execute(
            _request("C-300003", membership_type, date(2026, 1, 15))
        )

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.invoices) == 0
    assert len(uow.journals) == 0


def test_rollback():
    membership_type = _membership_type("STANDARD")
    feature, uow, _ = _build_feature(
        plans=[_plan(membership_type)],
        member_number="M-100004",
        fail_invoice_add=True,
    )

    with pytest.raises(RepositoryException):
        feature.execute(
            _request("C-300004", membership_type, date(2026, 1, 15))
        )

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.contacts) == 0
    assert len(uow.members) == 0
    assert len(uow.memberships) == 0
    assert len(uow.invoices) == 0
    assert len(uow.journals) == 0


def test_event_dispatch():
    membership_type = _membership_type("STANDARD")
    feature, _, collector = _build_feature(plans=[_plan(membership_type)], member_number="M-100005")

    result = feature.execute(
        _request("C-300005", membership_type, date(2026, 1, 15))
    )

    assert len(collector.events) == 1
    event = collector.events[0]
    assert event.member_id == result.member_id
    assert event.member_number == result.member_number
    assert event.invoice_id == result.invoice_id
    assert event.journal_id == result.journal_id


def test_result_dto():
    membership_type = _membership_type("PREMIUM")
    feature, _, _ = _build_feature(plans=[_plan(membership_type)], member_number="M-100006")

    result = feature.execute(
        _request("C-300006", membership_type, date(2026, 2, 1))
    )

    assert isinstance(result.member_id, UUID)
    assert isinstance(result.invoice_id, UUID)
    assert isinstance(result.journal_id, UUID)
    assert result.member_number == "M-100006"
