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
from mfm.application.workflows.register_payment_workflow import PaymentRegisteredEvent
from mfm.application.workflows.register_payment_workflow import RegisterPaymentWorkflow
from mfm.application.workflows.register_payment_workflow import RegisterPaymentWorkflowInput
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import InvalidPaymentAmountError
from mfm.domain.finance.exceptions import InvoiceOverpaymentError
from mfm.domain.finance.exceptions import InvoicePaymentError
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.invoice_status import InvoiceStatus
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_method import PaymentMethod


def _money(value: str) -> Money:
    return Money(amount=Decimal(value), currency=Currency.DKK)


def _invoice(total: str = "100.00") -> Invoice:
    invoice = Invoice(
        invoice_number=InvoiceNumber(f"INV-{uuid4().hex[:8]}"),
        member_id=uuid4(),
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 10),
        lines=[
            InvoiceLine(
                description="Membership fee",
                quantity=Decimal("1"),
                unit_price=_money(total),
            )
        ],
    )
    invoice.issue()
    return invoice


class InMemoryInvoiceRepository:
    def __init__(self, invoices: list[Invoice] | None = None) -> None:
        self._invoices = {invoice.id: invoice for invoice in (invoices or [])}

    def get(self, invoice_id: UUID) -> Invoice | None:
        return self._invoices.get(invoice_id)

    def update(self, invoice: Invoice) -> None:
        self._invoices[invoice.id] = invoice


class InMemoryPaymentRepository:
    def __init__(self) -> None:
        self._payments: dict[UUID, Payment] = {}
        self._payments_by_external_reference: dict[str, Payment] = {}
        self.fail_on_add = False

    def add(self, payment: Payment) -> None:
        if self.fail_on_add:
            raise RuntimeError("payment add failed")
        self._payments[payment.id] = payment
        if payment.external_reference:
            self._payments_by_external_reference[payment.external_reference] = payment

    def get_by_external_reference(self, external_reference: str) -> Payment | None:
        return self._payments_by_external_reference.get(external_reference)


class InMemoryJournalRepository:
    def __init__(self) -> None:
        self._journals: dict[UUID, JournalEntry] = {}

    def add(self, journal: JournalEntry) -> None:
        self._journals[journal.id] = journal


class InMemoryLedgerRepository:
    def __init__(self) -> None:
        self.applied_journal_ids: list[UUID] = []

    def apply_journal_entry(self, journal: JournalEntry) -> None:
        self.applied_journal_ids.append(journal.id)


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
        invoice_repo: InMemoryInvoiceRepository,
        payment_repo: InMemoryPaymentRepository,
        journal_repo: InMemoryJournalRepository,
        ledger_repo: InMemoryLedgerRepository,
        fiscal_year_repo: InMemoryFiscalYearRepository,
    ) -> None:
        super().__init__()
        self._invoice_repo = invoice_repo
        self._payment_repo = payment_repo
        self._journal_repo = journal_repo
        self._ledger_repo = ledger_repo
        self._fiscal_year_repo = fiscal_year_repo
        self.commits = 0
        self.rollbacks = 0
        self.flushes = 0
        self.closes = 0

    def _start_scope(self) -> None:
        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = _NoopRepo()
        self.invoice_repository = self._invoice_repo
        self.payment_repository = self._payment_repo
        self.journal_repository = self._journal_repo
        self.ledger_repository = self._ledger_repo
        self.fiscal_year_repository = self._fiscal_year_repo

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
        self.events: list[PaymentRegisteredEvent] = []

    def handle(self, event) -> None:
        if isinstance(event, PaymentRegisteredEvent):
            self.events.append(event)


def _workflow(invoice: Invoice) -> tuple[
    RegisterPaymentWorkflow,
    FakeUnitOfWork,
    InMemoryPaymentRepository,
    InMemoryJournalRepository,
    InMemoryLedgerRepository,
    InMemoryFiscalYearRepository,
    EventCollector,
]:
    invoice_repo = InMemoryInvoiceRepository([invoice])
    payment_repo = InMemoryPaymentRepository()
    journal_repo = InMemoryJournalRepository()
    ledger_repo = InMemoryLedgerRepository()
    fiscal_year_repo = InMemoryFiscalYearRepository()
    uow = FakeUnitOfWork(
        invoice_repo,
        payment_repo,
        journal_repo,
        ledger_repo,
        fiscal_year_repo,
    )

    dispatcher = DomainEventDispatcher()
    collector = EventCollector()
    dispatcher.register(PaymentRegisteredEvent, collector)

    workflow = RegisterPaymentWorkflow(unit_of_work=uow, dispatcher=dispatcher)
    return workflow, uow, payment_repo, journal_repo, ledger_repo, fiscal_year_repo, collector


def test_full_payment():
    invoice = _invoice("100.00")
    workflow, uow, _, journal_repo, ledger_repo, fiscal_year_repo, _ = _workflow(invoice)

    result = workflow.execute(
        RegisterPaymentWorkflowInput(
            invoice_id=invoice.id,
            amount=_money("100.00"),
            payment_method=PaymentMethod.BANK_TRANSFER,
            payment_date=date(2026, 1, 5),
            external_reference="TXN-100",
            notes="Paid in full",
        )
    )

    assert result.success is True
    assert result.invoice is not None
    assert result.invoice.status == InvoiceStatus.PAID
    assert result.journal is not None
    assert result.journal.status.value == "POSTED"
    assert result.payment is not None
    assert result.payment.notes == "Paid in full"
    assert len(journal_repo._journals) == 1
    assert len(ledger_repo.applied_journal_ids) == 1
    assert fiscal_year_repo.checked_dates == [date(2026, 1, 5)]
    assert uow.commits == 1


def test_partial_payment():
    invoice = _invoice("100.00")
    workflow, _, _, _, _, _, _ = _workflow(invoice)

    result = workflow.execute(
        RegisterPaymentWorkflowInput(
            invoice_id=invoice.id,
            amount=_money("40.00"),
            payment_method=PaymentMethod.CASH,
            payment_date=date(2026, 1, 5),
            external_reference=None,
        )
    )

    assert result.invoice is not None
    assert result.invoice.status == InvoiceStatus.PARTIALLY_PAID


def test_overpayment():
    invoice = _invoice("100.00")
    workflow, _, _, _, _, _, _ = _workflow(invoice)

    with pytest.raises(InvoiceOverpaymentError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("120.00"),
                payment_method=PaymentMethod.CASH,
                payment_date=date(2026, 1, 5),
                external_reference=None,
            )
        )


def test_cancelled_invoice():
    invoice = _invoice("100.00")
    invoice.cancel()
    workflow, _, _, _, _, _, _ = _workflow(invoice)

    with pytest.raises(InvoicePaymentError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("20.00"),
                payment_method=PaymentMethod.CASH,
                payment_date=date(2026, 1, 5),
                external_reference=None,
            )
        )


def test_invalid_payment():
    invoice = _invoice("100.00")
    workflow, _, _, _, _, _, _ = _workflow(invoice)

    with pytest.raises(InvalidPaymentAmountError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("0.00"),
                payment_method=PaymentMethod.CASH,
                payment_date=date(2026, 1, 5),
                external_reference=None,
            )
        )


def test_rollback():
    invoice = _invoice("100.00")
    workflow, uow, payment_repo, journal_repo, ledger_repo, _, _ = _workflow(invoice)
    payment_repo.fail_on_add = True

    with pytest.raises(RuntimeError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("50.00"),
                payment_method=PaymentMethod.BANK_TRANSFER,
                payment_date=date(2026, 1, 5),
                external_reference="TXN-500",
            )
        )

    assert uow.rollbacks == 1
    assert uow.commits == 0
    assert len(payment_repo._payments) == 0
    assert len(journal_repo._journals) == 0
    assert len(ledger_repo.applied_journal_ids) == 0


def test_event_dispatch():
    invoice = _invoice("100.00")
    workflow, _, _, _, _, _, collector = _workflow(invoice)

    result = workflow.execute(
        RegisterPaymentWorkflowInput(
            invoice_id=invoice.id,
            amount=_money("100.00"),
            payment_method=PaymentMethod.PAYPAL,
            payment_date=date(2026, 1, 5),
            external_reference="TXN-EVT",
        )
    )

    assert result.payment is not None
    assert len(collector.events) == 1
    assert collector.events[0].payment_id == result.payment.id
    assert collector.events[0].invoice_id == invoice.id


def test_duplicate_payment():
    invoice = _invoice("100.00")
    workflow, _, payment_repo, _, _, _, _ = _workflow(invoice)

    first = workflow.execute(
        RegisterPaymentWorkflowInput(
            invoice_id=invoice.id,
            amount=_money("20.00"),
            payment_method=PaymentMethod.BANK_TRANSFER,
            payment_date=date(2026, 1, 5),
            external_reference="TXN-DUP",
        )
    )
    assert first.success is True

    with pytest.raises(ValueError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("20.00"),
                payment_method=PaymentMethod.BANK_TRANSFER,
                payment_date=date(2026, 1, 5),
                external_reference="TXN-DUP",
            )
        )

    assert len(payment_repo._payments) == 1


def test_closed_fiscal_year():
    invoice = _invoice("100.00")
    workflow, uow, payment_repo, journal_repo, ledger_repo, fiscal_year_repo, _ = _workflow(invoice)
    fiscal_year_repo.closed = True

    with pytest.raises(ValueError):
        workflow.execute(
            RegisterPaymentWorkflowInput(
                invoice_id=invoice.id,
                amount=_money("30.00"),
                payment_method=PaymentMethod.CASH,
                payment_date=date(2026, 1, 5),
                external_reference="TXN-CLOSED",
            )
        )

    assert uow.rollbacks == 1
    assert len(payment_repo._payments) == 0
    assert len(journal_repo._journals) == 0
    assert len(ledger_repo.applied_journal_ids) == 0
