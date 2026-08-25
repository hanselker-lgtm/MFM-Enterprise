"""Accounts receivable application service."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import timedelta
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.domain.finance.accounts_receivable import AccountsReceivable
from mfm.domain.finance.aging_bucket import AgingBucket
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_status import PaymentStatus
from mfm.domain.finance.receivable import Receivable


@dataclass(slots=True)
class AccountsReceivableSummary:
    total_open_amount: Money
    overdue_amount: Money
    invoices_due_today: int
    invoices_due_this_week: int
    invoices_due_this_month: int
    oldest_invoice: UUID | None
    aging_buckets: list[AgingBucket]
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


class InvoiceRepository(Protocol):
    def list(self) -> list[Invoice]: ...


class PaymentRepository(Protocol):
    def list(self) -> list[Payment]: ...


class AccountsReceivableService:
    """Provides one consolidated view of all open accounts receivable."""

    def __init__(
        self,
        *,
        invoice_repository: InvoiceRepository,
        payment_repository: PaymentRepository,
    ) -> None:
        self._invoice_repository = invoice_repository
        self._payment_repository = payment_repository

    def summarize(self, *, as_of_date: date) -> AccountsReceivableSummary:
        invoices = self._invoice_repository.list()
        payments = self._payment_repository.list()

        if not invoices:
            zero = Money(amount=Decimal("0"), currency="DKK")
            empty_buckets = [
                AgingBucket(label="current", amount=zero, invoice_count=0),
                AgingBucket(label="1-30", amount=zero, invoice_count=0),
                AgingBucket(label="31-60", amount=zero, invoice_count=0),
                AgingBucket(label="61-90", amount=zero, invoice_count=0),
                AgingBucket(label="90+", amount=zero, invoice_count=0),
            ]
            return AccountsReceivableSummary(
                total_open_amount=zero,
                overdue_amount=zero,
                invoices_due_today=0,
                invoices_due_this_week=0,
                invoices_due_this_month=0,
                oldest_invoice=None,
                aging_buckets=empty_buckets,
            )

        accounts_receivable = AccountsReceivable()
        for invoice in invoices:
            accounts_receivable.add_invoice(invoice)

        errors: list[str] = []
        for payment in payments:
            if payment.status is not PaymentStatus.CONFIRMED:
                continue
            try:
                accounts_receivable.register_payment(
                    invoice_id=payment.invoice_id,
                    payment_id=payment.id,
                    amount=payment.amount,
                )
            except ValueError as exc:
                errors.append(str(exc))

        open_receivables = [
            receivable
            for receivable in accounts_receivable._receivables.values()
            if not receivable.closed and receivable.balance().amount > Decimal("0")
        ]

        total_open_amount = accounts_receivable.balance()

        overdue_amount = Money(
            amount=Decimal("0"),
            currency=total_open_amount.currency,
        )
        for receivable in accounts_receivable.overdue(at_date=as_of_date):
            overdue_amount = overdue_amount + receivable.balance()

        oldest = min(open_receivables, key=lambda receivable: receivable.due_date, default=None)

        return AccountsReceivableSummary(
            total_open_amount=total_open_amount,
            overdue_amount=overdue_amount,
            invoices_due_today=self._count_due_today(open_receivables, as_of_date),
            invoices_due_this_week=self._count_due_this_week(open_receivables, as_of_date),
            invoices_due_this_month=self._count_due_this_month(open_receivables, as_of_date),
            oldest_invoice=oldest.invoice_id if oldest is not None else None,
            aging_buckets=accounts_receivable.aging(at_date=as_of_date),
            errors=errors,
        )

    @staticmethod
    def _count_due_today(receivables: list[Receivable], as_of_date: date) -> int:
        return sum(1 for receivable in receivables if receivable.due_date == as_of_date)

    @staticmethod
    def _count_due_this_week(receivables: list[Receivable], as_of_date: date) -> int:
        end_date = as_of_date + timedelta(days=6)
        return sum(
            1
            for receivable in receivables
            if as_of_date <= receivable.due_date <= end_date
        )

    @staticmethod
    def _count_due_this_month(receivables: list[Receivable], as_of_date: date) -> int:
        return sum(
            1
            for receivable in receivables
            if receivable.due_date.year == as_of_date.year
            and receivable.due_date.month == as_of_date.month
        )
