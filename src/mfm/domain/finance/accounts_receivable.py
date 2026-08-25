"""Accounts receivable aggregate for finance domain."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.domain.finance.aging_bucket import AgingBucket
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.money import Money
from mfm.domain.finance.receivable import Receivable


@dataclass(slots=True)
class AccountsReceivable:
    """Manages open invoices, balances, due dates, and dynamic aging buckets."""

    _receivables: dict[UUID, Receivable]

    def __init__(self) -> None:
        self._receivables = {}

    def add_invoice(self, invoice: Invoice) -> None:
        if invoice.id in self._receivables:
            return

        self._receivables[invoice.id] = Receivable(
            invoice_id=invoice.id,
            member_id=invoice.member_id,
            due_date=invoice.due_date,
            original_amount=invoice.total,
        )

    def register_payment(self, *, invoice_id: UUID, payment_id: UUID | None = None, amount: Money) -> None:
        receivable = self._get_receivable(invoice_id)
        receivable.register_payment(payment_id=payment_id or uuid4(), amount=amount)

    def balance(self) -> Money:
        if not self._receivables:
            return Money(amount=Decimal("0"), currency="DKK")

        currency = next(iter(self._receivables.values())).original_amount.currency
        total = Money(amount=Decimal("0"), currency=currency)
        for receivable in self._receivables.values():
            if receivable.closed:
                continue
            total = total + receivable.balance()
        return total

    def overdue(self, *, at_date: date) -> list[Receivable]:
        return [
            receivable
            for receivable in self._receivables.values()
            if receivable.is_overdue(at_date)
        ]

    def aging(self, *, at_date: date) -> list[AgingBucket]:
        if not self._receivables:
            zero = Money(amount=Decimal("0"), currency="DKK")
            return [
                AgingBucket(label="current", amount=zero, invoice_count=0),
                AgingBucket(label="1-30", amount=zero, invoice_count=0),
                AgingBucket(label="31-60", amount=zero, invoice_count=0),
                AgingBucket(label="61-90", amount=zero, invoice_count=0),
                AgingBucket(label="90+", amount=zero, invoice_count=0),
            ]

        currency = next(iter(self._receivables.values())).original_amount.currency
        buckets = {
            "current": {"amount": Money(amount=Decimal("0"), currency=currency), "count": 0},
            "1-30": {"amount": Money(amount=Decimal("0"), currency=currency), "count": 0},
            "31-60": {"amount": Money(amount=Decimal("0"), currency=currency), "count": 0},
            "61-90": {"amount": Money(amount=Decimal("0"), currency=currency), "count": 0},
            "90+": {"amount": Money(amount=Decimal("0"), currency=currency), "count": 0},
        }

        for receivable in self._receivables.values():
            outstanding = receivable.balance()
            if receivable.closed or outstanding.amount <= Decimal("0"):
                continue

            days_overdue = (at_date - receivable.due_date).days
            if days_overdue <= 0:
                key = "current"
            elif days_overdue <= 30:
                key = "1-30"
            elif days_overdue <= 60:
                key = "31-60"
            elif days_overdue <= 90:
                key = "61-90"
            else:
                key = "90+"

            buckets[key]["amount"] = buckets[key]["amount"] + outstanding
            buckets[key]["count"] += 1

        return [
            AgingBucket(label="current", amount=buckets["current"]["amount"], invoice_count=buckets["current"]["count"]),
            AgingBucket(label="1-30", amount=buckets["1-30"]["amount"], invoice_count=buckets["1-30"]["count"]),
            AgingBucket(label="31-60", amount=buckets["31-60"]["amount"], invoice_count=buckets["31-60"]["count"]),
            AgingBucket(label="61-90", amount=buckets["61-90"]["amount"], invoice_count=buckets["61-90"]["count"]),
            AgingBucket(label="90+", amount=buckets["90+"]["amount"], invoice_count=buckets["90+"]["count"]),
        ]

    def close_invoice(self, *, invoice_id: UUID) -> None:
        receivable = self._get_receivable(invoice_id)
        receivable.close()

    def _get_receivable(self, invoice_id: UUID) -> Receivable:
        receivable = self._receivables.get(invoice_id)
        if receivable is None:
            raise ValueError(f"Invoice {invoice_id} was not found in accounts receivable")
        return receivable
