"""Register payment workflow orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_method import PaymentMethod
from mfm.domain.finance.payment_reference import PaymentReference


class InvoiceRepository(Protocol):
    def get(self, invoice_id: UUID) -> Invoice | None: ...

    def update(self, invoice: Invoice) -> None: ...


class PaymentRepository(Protocol):
    def add(self, payment: Payment) -> None: ...

    def get_by_external_reference(self, external_reference: str) -> Payment | None: ...


class JournalRepository(Protocol):
    def add(self, journal: JournalEntry) -> None: ...


class LedgerRepository(Protocol):
    def apply_journal_entry(self, journal: JournalEntry) -> None: ...


class FiscalYearRepository(Protocol):
    def ensure_posting_allowed(self, posting_date: date) -> None: ...


@dataclass(slots=True)
class RegisterPaymentWorkflowInput:
    invoice_id: UUID
    amount: Money
    payment_method: PaymentMethod
    payment_date: date
    external_reference: str | None = None
    notes: str | None = None


@dataclass(slots=True)
class RegisterPaymentWorkflowResult:
    success: bool
    invoice: Invoice | None = None
    payment: Payment | None = None
    journal: JournalEntry | None = None


@dataclass(slots=True)
class PaymentRegisteredEvent(DomainEvent):
    payment_id: UUID = field(default_factory=uuid4)
    invoice_id: UUID = field(default_factory=uuid4)
    member_id: UUID = field(default_factory=uuid4)


class RegisterPaymentWorkflow:
    """Orchestrates payment registration without domain rule implementation details."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, data: RegisterPaymentWorkflowInput) -> RegisterPaymentWorkflowResult:
        with self._unit_of_work as uow:
            invoice_repository: InvoiceRepository = uow.invoice_repository
            payment_repository: PaymentRepository = uow.payment_repository
            journal_repository: JournalRepository = uow.journal_repository
            ledger_repository: LedgerRepository = uow.ledger_repository
            fiscal_year_repository: FiscalYearRepository = uow.fiscal_year_repository

            invoice = uow.invoice_repository.get(data.invoice_id)
            if invoice is None:
                raise ValueError(f"Invoice {data.invoice_id} was not found")

            if data.external_reference:
                existing_payment = payment_repository.get_by_external_reference(
                    data.external_reference
                )
                if existing_payment is not None:
                    raise ValueError(
                        f"Payment with external reference {data.external_reference} already exists"
                    )

            fiscal_year_repository.ensure_posting_allowed(data.payment_date)

            payment_reference = PaymentReference(
                f"PAY-{data.invoice_id.hex[:8]}-{data.payment_date:%Y%m%d}-{uuid4().hex[:6]}"
            )
            payment = Payment(
                payment_reference=payment_reference,
                invoice_id=invoice.id,
                member_id=invoice.member_id,
                amount=data.amount,
                payment_date=data.payment_date,
                method=data.payment_method,
                external_reference=data.external_reference,
                notes=data.notes,
                invoice_issue_date=invoice.issue_date,
            )
            payment_repository.add(payment)

            payment.confirm()

            if data.amount == invoice.total:
                invoice.register_payment()
            else:
                invoice.register_partial_payment(data.amount)
            invoice_repository.update(invoice)

            journal = JournalEntry(
                journal_number=f"PAY-{payment.id.hex[:10]}",
                posting_date=data.payment_date,
                description=f"Payment registration for invoice {invoice.invoice_number}",
                reference=str(invoice.invoice_number),
                lines=[
                    JournalLine(
                        account_id=uuid4(),
                        side=PostingSide.DEBIT,
                        amount=data.amount,
                        description="Cash/Bank",
                    ),
                    JournalLine(
                        account_id=uuid4(),
                        side=PostingSide.CREDIT,
                        amount=data.amount,
                        description="Accounts receivable",
                    ),
                ],
            )
            journal.post()
            journal_repository.add(journal)

            ledger_repository.apply_journal_entry(journal)

            uow.commit()

        self._dispatcher.dispatch(
            PaymentRegisteredEvent(
                payment_id=payment.id,
                invoice_id=invoice.id,
                member_id=invoice.member_id,
            )
        )

        return RegisterPaymentWorkflowResult(
            success=True,
            invoice=invoice,
            payment=payment,
            journal=journal,
        )
