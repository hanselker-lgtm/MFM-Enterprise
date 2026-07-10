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
from mfm.application.features.annual_contingent_generation import AnnualContingentGenerationFeature
from mfm.application.features.annual_contingent_generation import CreateAnnualContingentFeature
from mfm.application.features.annual_contingent_generation import CreateAnnualContingentRequest
from mfm.application.features.annual_contingent_generation import CreateAnnualContingentResponse
from mfm.application.features.annual_contingent_generation import InvoiceCreatedEvent
from mfm.application.features.annual_contingent_generation import RepositoryException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
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
        invoice_rule=InvoiceRule(billing_period=BillingPeriod.YEARLY, due_days=14),
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
    def __init__(self, *, fail_on_add: bool = False) -> None:
        self._invoices: dict[UUID, Invoice] = {}
        self._fail_on_add = fail_on_add

    def add(self, invoice: Invoice) -> None:
        if self._fail_on_add:
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
        self.checked_dates: list[date] = []

    def ensure_posting_allowed(self, posting_date: date) -> None:
        self.checked_dates.append(posting_date)


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity: Any) -> None:
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        memberships: list[Membership],
        plans: list[ContingentPlan],
        *,
        fail_invoice_add: bool = False,
    ) -> None:
        super().__init__()
        self._memberships = memberships
        self._plans = plans
        self._fail_invoice_add = fail_invoice_add

        self.memberships: list[Membership] = list(memberships)
        self.invoices: dict[UUID, Invoice] = {}
        self.journals: dict[UUID, JournalEntry] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self._snapshot = (dict(self.invoices), dict(self.journals))

        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = InMemoryMembershipRepository(self.memberships)
        self.contingent_repository = InMemoryContingentRepository(self._plans)
        self.invoice_repository = InMemoryInvoiceRepository(fail_on_add=self._fail_invoice_add)
        self.journal_repository = InMemoryJournalRepository()
        self.fiscal_year_repository = InMemoryFiscalYearRepository()
        self.payment_repository = _NoopRepo()

        self.invoice_repository._invoices = self.invoices
        self.journal_repository._journals = self.journals

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        invoices, journals = self._snapshot
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
        self.events: list[InvoiceCreatedEvent] = []

    def handle(self, event) -> None:
        if isinstance(event, InvoiceCreatedEvent):
            self.events.append(event)


def _feature(
    memberships: list[Membership],
    plans: list[ContingentPlan],
    *,
    fail_invoice_add: bool = False,
) -> tuple[CreateAnnualContingentFeature, FakeUnitOfWork, EventCollector]:
    uow = FakeUnitOfWork(memberships, plans, fail_invoice_add=fail_invoice_add)
    dispatcher = DomainEventDispatcher()
    collector = EventCollector()
    dispatcher.register(InvoiceCreatedEvent, collector)
    feature = CreateAnnualContingentFeature(unit_of_work=uow, dispatcher=dispatcher)
    return feature, uow, collector


def test_empty_system():
    feature, uow, collector = _feature([], [])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
        )
    )

    assert result.processed == 0
    assert result.invoices_created == 0
    assert result.journal_drafts_created == 0
    assert result.skipped == 0
    assert result.warnings == ()
    assert result.errors == ()
    assert uow.commits == 1
    assert len(collector.events) == 0


def test_one_member():
    mt = _membership_type("STANDARD")
    feature, uow, collector = _feature([_membership(uuid4(), mt)], [_plan(mt)])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
        )
    )

    assert result.processed == 1
    assert result.invoices_created == 1
    assert result.journal_drafts_created == 1
    assert result.skipped == 0
    assert len(uow.invoices) == 1
    assert len(uow.journals) == 1
    assert len(collector.events) == 1


def test_many_members():
    mt_standard = _membership_type("STANDARD")
    mt_premium = _membership_type("PREMIUM")
    memberships = [
        _membership(uuid4(), mt_standard),
        _membership(uuid4(), mt_standard),
        _membership(uuid4(), mt_premium),
    ]

    feature, _, _ = _feature(memberships, [_plan(mt_standard), _plan(mt_premium)])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
            membership_type_id=mt_standard.id,
        )
    )

    assert result.processed == 2
    assert result.invoices_created == 2
    assert result.journal_drafts_created == 2
    assert result.skipped == 0


def test_dry_run():
    mt = _membership_type("STANDARD")
    feature, uow, collector = _feature([_membership(uuid4(), mt)], [_plan(mt)])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
            dry_run=True,
        )
    )

    assert result.processed == 1
    assert result.invoices_created == 1
    assert result.journal_drafts_created == 1
    assert result.skipped == 0
    assert uow.commits == 0
    assert len(uow.invoices) == 0
    assert len(uow.journals) == 0
    assert len(collector.events) == 0


def test_duplicate_execution():
    mt = _membership_type("STANDARD")
    feature, uow, _ = _feature([_membership(uuid4(), mt), _membership(uuid4(), mt)], [_plan(mt)])

    first = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
        )
    )
    second = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 2, 10),
        )
    )

    assert first.invoices_created == 2
    assert second.processed == 2
    assert second.invoices_created == 0
    assert second.journal_drafts_created == 0
    assert second.skipped == 2
    assert len(second.warnings) == 2
    assert len(uow.invoices) == 2


def test_missing_contingent_plan():
    mt = _membership_type("STANDARD")
    feature, _, _ = _feature([_membership(uuid4(), mt)], [])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
        )
    )

    assert result.processed == 1
    assert result.invoices_created == 0
    assert result.journal_drafts_created == 0
    assert result.skipped == 1
    assert len(result.warnings) == 1


def test_rollback():
    mt = _membership_type("STANDARD")
    feature, uow, _ = _feature([_membership(uuid4(), mt)], [_plan(mt)], fail_invoice_add=True)

    with pytest.raises(RepositoryException):
        feature.execute(
            CreateAnnualContingentRequest(
                fiscal_year=2026,
                billing_date=date(2026, 1, 10),
            )
        )

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(uow.invoices) == 0
    assert len(uow.journals) == 0


def test_summary_dto():
    mt_standard = _membership_type("STANDARD")
    mt_premium = _membership_type("PREMIUM")
    memberships = [
        _membership(uuid4(), mt_standard),
        _membership(uuid4(), mt_premium),
    ]

    feature, _, _ = _feature(memberships, [_plan(mt_standard)])

    result = feature.execute(
        CreateAnnualContingentRequest(
            fiscal_year=2026,
            billing_date=date(2026, 1, 10),
        )
    )

    assert isinstance(result, CreateAnnualContingentResponse)
    assert result.processed == 2
    assert result.invoices_created == 1
    assert result.journal_drafts_created == 1
    assert result.skipped == 1
    assert len(result.warnings) == 1
    assert result.errors == ()
