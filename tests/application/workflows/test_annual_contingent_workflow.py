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
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.annual_contingent_workflow import AnnualContingentWorkflow
from mfm.application.workflows.annual_contingent_workflow import InvoiceCreatedEvent
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency as ContingentCurrency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money as ContingentMoney
from mfm.domain.finance.invoice import Invoice
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType


def _membership_type(code: str = "STANDARD") -> MembershipType:
    return MembershipType(code=code, name=code.title())


def _membership(member_id: UUID, membership_type: MembershipType) -> Membership:
    return Membership(
        member_id=member_id,
        membership_type=membership_type,
        start_date=date(2026, 1, 1),
    )


def _plan(membership_type: MembershipType) -> ContingentPlan:
    return ContingentPlan(
        membership_type=membership_type,
        price=ContingentMoney(
            amount=Decimal("300.00"),
            currency=ContingentCurrency.DKK,
        ),
        invoice_rule=InvoiceRule(
            billing_period=BillingPeriod.YEARLY,
            due_days=14,
        ),
        valid_from=date(2026, 1, 1),
        valid_to=None,
    )


class InMemoryMembershipRepository:
    def __init__(self, memberships: list[Membership] | None = None) -> None:
        self._memberships = memberships or []

    def list_active(self) -> list[Membership]:
        return list(self._memberships)


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
    def __init__(self) -> None:
        self._invoices: dict[UUID, Invoice] = {}
        self.fail_on_add = False

    def add(self, invoice: Invoice) -> None:
        if self.fail_on_add:
            raise RuntimeError("invoice add failed")
        self._invoices[invoice.id] = invoice

    def exists_for_member_and_year(self, member_id: UUID, year: int) -> bool:
        return any(
            invoice.member_id == member_id and invoice.issue_date.year == year
            for invoice in self._invoices.values()
        )


class InMemoryJournalRepository:
    def __init__(self) -> None:
        self._journals: dict[UUID, JournalEntry] = {}

    def add(self, journal: JournalEntry) -> None:
        self._journals[journal.id] = journal


class InMemoryFiscalYearRepository:
    def __init__(self) -> None:
        self.closed = False
        self.checked_dates: list[date] = []

    def ensure_posting_allowed(self, posting_date: date) -> None:
        self.checked_dates.append(posting_date)
        if self.closed:
            raise ValueError("closed fiscal year")


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity: Any) -> None:
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        memberships: list[Membership],
        plans: list[ContingentPlan],
    ) -> None:
        super().__init__()
        self.membership_repo = InMemoryMembershipRepository(memberships)
        self.contingent_repo = InMemoryContingentRepository(plans)
        self.invoice_repo = InMemoryInvoiceRepository()
        self.journal_repo = InMemoryJournalRepository()
        self.fiscal_repo = InMemoryFiscalYearRepository()
        self.commits = 0
        self.rollbacks = 0
        self.flushes = 0
        self.closes = 0

    def _start_scope(self) -> None:
        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = self.membership_repo
        self.contingent_repository = self.contingent_repo
        self.invoice_repository = self.invoice_repo
        self.payment_repository = _NoopRepo()
        self.journal_repository = self.journal_repo
        self.fiscal_year_repository = self.fiscal_repo

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1

    def _flush_impl(self) -> None:
        self.flushes += 1

    def _close_impl(self) -> None:
        self.closes += 1


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[InvoiceCreatedEvent] = []

    def handle(self, event) -> None:
        if isinstance(event, InvoiceCreatedEvent):
            self.events.append(event)


def _workflow(
    memberships: list[Membership],
    plans: list[ContingentPlan],
) -> tuple[AnnualContingentWorkflow, FakeUnitOfWork, EventCollector]:
    uow = FakeUnitOfWork(memberships, plans)
    dispatcher = DomainEventDispatcher()
    collector = EventCollector()
    dispatcher.register(InvoiceCreatedEvent, collector)
    return AnnualContingentWorkflow(unit_of_work=uow, dispatcher=dispatcher), uow, collector


def test_empty_database():
    workflow, uow, collector = _workflow([], [])

    summary = workflow.execute(run_date=date(2026, 1, 10))

    assert summary.memberships_processed == 0
    assert summary.invoices_created == 0
    assert summary.journals_created == 0
    assert summary.skipped == 0
    assert summary.failed == 0
    assert uow.commits == 1
    assert len(collector.events) == 0


def test_one_member():
    mt = _membership_type("STANDARD")
    member_id = uuid4()
    workflow, uow, collector = _workflow([_membership(member_id, mt)], [_plan(mt)])

    summary = workflow.execute(run_date=date(2026, 1, 10))

    assert summary.memberships_processed == 1
    assert summary.invoices_created == 1
    assert summary.journals_created == 1
    assert summary.skipped == 0
    assert len(uow.invoice_repo._invoices) == 1
    assert len(uow.journal_repo._journals) == 1
    assert len(collector.events) == 1


def test_multiple_members():
    mt = _membership_type("STANDARD")
    memberships = [_membership(uuid4(), mt), _membership(uuid4(), mt), _membership(uuid4(), mt)]
    workflow, _, _ = _workflow(memberships, [_plan(mt)])

    summary = workflow.execute(run_date=date(2026, 1, 10))

    assert summary.memberships_processed == 3
    assert summary.invoices_created == 3
    assert summary.journals_created == 3
    assert summary.skipped == 0


def test_duplicate_run():
    mt = _membership_type("STANDARD")
    memberships = [_membership(uuid4(), mt), _membership(uuid4(), mt)]
    workflow, uow, _ = _workflow(memberships, [_plan(mt)])

    first = workflow.execute(run_date=date(2026, 1, 10))
    second = workflow.execute(run_date=date(2026, 1, 15))

    assert first.invoices_created == 2
    assert second.memberships_processed == 2
    assert second.invoices_created == 0
    assert second.journals_created == 0
    assert second.skipped == 2
    assert len(uow.invoice_repo._invoices) == 2


def test_missing_contingent_plan():
    mt = _membership_type("STANDARD")
    workflow, _, _ = _workflow([_membership(uuid4(), mt)], [])

    summary = workflow.execute(run_date=date(2026, 1, 10))

    assert summary.memberships_processed == 1
    assert summary.invoices_created == 0
    assert summary.journals_created == 0
    assert summary.skipped == 1


def test_closed_fiscal_year():
    mt = _membership_type("STANDARD")
    workflow, uow, _ = _workflow([_membership(uuid4(), mt)], [_plan(mt)])
    uow.fiscal_repo.closed = True

    with pytest.raises(ValueError):
        workflow.execute(run_date=date(2026, 1, 10))

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.invoice_repo._invoices) == 0
    assert len(uow.journal_repo._journals) == 0


def test_rollback():
    mt = _membership_type("STANDARD")
    workflow, uow, _ = _workflow([_membership(uuid4(), mt)], [_plan(mt)])
    uow.invoice_repo.fail_on_add = True

    with pytest.raises(RuntimeError):
        workflow.execute(run_date=date(2026, 1, 10))

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.invoice_repo._invoices) == 0
    assert len(uow.journal_repo._journals) == 0


def test_summary():
    mt_standard = _membership_type("STANDARD")
    mt_premium = _membership_type("PREMIUM")
    memberships = [
        _membership(uuid4(), mt_standard),
        _membership(uuid4(), mt_standard),
        _membership(uuid4(), mt_premium),
    ]
    workflow, _, _ = _workflow(memberships, [_plan(mt_standard)])

    summary = workflow.execute(run_date=date(2026, 1, 10))

    assert summary.memberships_processed == 3
    assert summary.invoices_created == 2
    assert summary.journals_created == 2
    assert summary.skipped == 1
    assert summary.failed == 0
