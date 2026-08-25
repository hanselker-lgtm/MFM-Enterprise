from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.finance.accounts_receivable import AccountsReceivable
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.money import Money


def _invoice(*, number: str, due_date: date, amount: str = "100.00") -> Invoice:
    issue_date = date(due_date.year, due_date.month, 1)
    return Invoice(
        invoice_number=InvoiceNumber(number),
        member_id=uuid4(),
        issue_date=issue_date,
        due_date=due_date,
        lines=[
            InvoiceLine(
                description="Membership fee",
                quantity=Decimal("1"),
                unit_price=Money(amount=Decimal(amount), currency=Currency.DKK),
            )
        ],
    )


def _bucket_map(ar: AccountsReceivable, at_date: date) -> dict[str, tuple[Decimal, int]]:
    result: dict[str, tuple[Decimal, int]] = {}
    for bucket in ar.aging(at_date=at_date):
        result[bucket.label] = (bucket.amount.amount, bucket.invoice_count)
    return result


def test_new_receivable():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-001", due_date=date(2026, 1, 20), amount="125.00")

    ar.add_invoice(invoice)

    assert ar.balance() == Money(amount=Decimal("125.00"), currency=Currency.DKK)


def test_payment():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-002", due_date=date(2026, 1, 20), amount="100.00")
    ar.add_invoice(invoice)

    ar.register_payment(
        invoice_id=invoice.id,
        payment_id=uuid4(),
        amount=Money(amount=Decimal("100.00"), currency=Currency.DKK),
    )

    assert ar.balance() == Money(amount=Decimal("0.00"), currency=Currency.DKK)


def test_partial_payment():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-003", due_date=date(2026, 1, 20), amount="100.00")
    ar.add_invoice(invoice)

    ar.register_payment(
        invoice_id=invoice.id,
        payment_id=uuid4(),
        amount=Money(amount=Decimal("40.00"), currency=Currency.DKK),
    )

    assert ar.balance() == Money(amount=Decimal("60.00"), currency=Currency.DKK)


def test_overdue():
    ar = AccountsReceivable()
    overdue_invoice = _invoice(
        number="INV-AR-004",
        due_date=date(2026, 1, 10),
        amount="100.00",
    )
    current_invoice = _invoice(
        number="INV-AR-005",
        due_date=date(2026, 2, 10),
        amount="100.00",
    )
    ar.add_invoice(overdue_invoice)
    ar.add_invoice(current_invoice)

    result = ar.overdue(at_date=date(2026, 1, 25))

    assert len(result) == 1
    assert result[0].invoice_id == overdue_invoice.id


def test_aging():
    ar = AccountsReceivable()

    current = _invoice(number="INV-AR-006", due_date=date(2026, 3, 1), amount="10.00")
    bucket_1_30 = _invoice(number="INV-AR-007", due_date=date(2026, 2, 15), amount="20.00")
    bucket_31_60 = _invoice(number="INV-AR-008", due_date=date(2026, 1, 15), amount="30.00")
    bucket_61_90 = _invoice(number="INV-AR-009", due_date=date(2025, 12, 15), amount="40.00")
    bucket_90_plus = _invoice(number="INV-AR-010", due_date=date(2025, 11, 15), amount="50.00")

    for invoice in [current, bucket_1_30, bucket_31_60, bucket_61_90, bucket_90_plus]:
        ar.add_invoice(invoice)

    buckets = _bucket_map(ar, date(2026, 3, 1))

    assert buckets["current"] == (Decimal("10.00"), 1)
    assert buckets["1-30"] == (Decimal("20.00"), 1)
    assert buckets["31-60"] == (Decimal("30.00"), 1)
    assert buckets["61-90"] == (Decimal("40.00"), 1)
    assert buckets["90+"] == (Decimal("50.00"), 1)


def test_close_invoice():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-011", due_date=date(2026, 1, 10), amount="100.00")
    ar.add_invoice(invoice)

    ar.close_invoice(invoice_id=invoice.id)

    assert ar.balance() == Money(amount=Decimal("0.00"), currency=Currency.DKK)
    assert ar.overdue(at_date=date(2026, 2, 1)) == []


def test_duplicate_payment():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-012", due_date=date(2026, 1, 20), amount="100.00")
    ar.add_invoice(invoice)
    payment_id: UUID = uuid4()

    ar.register_payment(
        invoice_id=invoice.id,
        payment_id=payment_id,
        amount=Money(amount=Decimal("25.00"), currency=Currency.DKK),
    )

    with pytest.raises(ValueError):
        ar.register_payment(
            invoice_id=invoice.id,
            payment_id=payment_id,
            amount=Money(amount=Decimal("25.00"), currency=Currency.DKK),
        )


def test_zero_balance():
    ar = AccountsReceivable()
    invoice = _invoice(number="INV-AR-013", due_date=date(2026, 1, 20), amount="100.00")
    ar.add_invoice(invoice)

    with pytest.raises(ValueError):
        ar.register_payment(
            invoice_id=invoice.id,
            payment_id=uuid4(),
            amount=Money(amount=Decimal("150.00"), currency=Currency.DKK),
        )

    ar.register_payment(
        invoice_id=invoice.id,
        payment_id=uuid4(),
        amount=Money(amount=Decimal("100.00"), currency=Currency.DKK),
    )

    assert ar.balance() == Money(amount=Decimal("0.00"), currency=Currency.DKK)
