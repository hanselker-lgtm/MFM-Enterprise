"""Receivable entity in accounts receivable domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from decimal import Decimal
from uuid import UUID

from mfm.domain.finance.money import Money


@dataclass(slots=True)
class Receivable:
    """Tracks one invoice receivable including payments and outstanding balance."""

    invoice_id: UUID
    member_id: UUID
    due_date: date
    original_amount: Money
    paid_amount: Money = field(init=False)
    payment_ids: set[UUID] = field(default_factory=set)
    closed: bool = False

    def __post_init__(self) -> None:
        self.paid_amount = Money(
            amount=Decimal("0"),
            currency=self.original_amount.currency,
        )

    def register_payment(self, *, payment_id: UUID, amount: Money) -> None:
        if payment_id in self.payment_ids:
            raise ValueError(f"Payment {payment_id} is already registered")

        if amount.currency != self.original_amount.currency:
            raise ValueError("Payment currency must match receivable currency")

        if amount.amount <= Decimal("0"):
            raise ValueError("Payment amount must be greater than zero")

        if amount > self.balance():
            raise ValueError("Payment cannot exceed outstanding balance")

        self.payment_ids.add(payment_id)
        self.paid_amount = self.paid_amount + amount

        if self.balance().amount == Decimal("0.00"):
            self.closed = True

    def balance(self) -> Money:
        return self.original_amount - self.paid_amount

    def is_overdue(self, at_date: date) -> bool:
        return not self.closed and self.balance().amount > Decimal("0") and self.due_date < at_date

    def close(self) -> None:
        self.closed = True
