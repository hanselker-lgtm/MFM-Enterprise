from __future__ import annotations
from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.application.features.accounts_receivable_service import AccountsReceivableService
from mfm.application.features.accounts_receivable_service import AccountsReceivableSummary
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_method import PaymentMethod
from mfm.domain.finance.payment_reference import PaymentReference


class InMemoryInvoiceRepository:
    def __init__(self, invoices: list[Invoice] | None = None) -> None:
        self._invoices = invoices or []

    def list(self) -> list[Invoice]:
        return list(self._invoices)


class InMemoryPaymentRepository:
    def __init__(self, payments: list[Payment] | None = None) -> None:
        self._payments = payments or []

    def list(self) -> list[Payment]:
        return list(self._payments)


def _invoice(*, number: str, due_date: date, amount: str = "100.00", member_id: UUID | None = None) -> Invoice:
    issue_date = date(due_date.year, due_date.month, 1)
    return Invoice(
        invoice_number=InvoiceNumber(number),
        member_id=member_id or uuid4(),
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


def _payment(*, invoice: Invoice, amount: str = "100.00") -> Payment:
    payment = Payment(
        payment_reference=PaymentReference(f"PAY-{invoice.id.hex[:8]}-{uuid4().hex[:4]}"),
        invoice_id=invoice.id,
        member_id=invoice.member_id,
        amount=Money(amount=Decimal(amount), currency=Currency.DKK),
        payment_date=max(invoice.issue_date, date(2026, 1, 1)),
        method=PaymentMethod.BANK_TRANSFER,
        invoice_issue_date=invoice.issue_date,
    )
    payment.confirm()
    return payment


def _service(invoices: list[Invoice], payments: list[Payment]) -> AccountsReceivableService:
    return AccountsReceivableService(
        invoice_repository=InMemoryInvoiceRepository(invoices),
        payment_repository=InMemoryPaymentRepository(payments),
    )


def _aging_map(summary: AccountsReceivableSummary) -> dict[str, tuple[Decimal, int]]:
    result: dict[str, tuple[Decimal, int]] = {}
    for bucket in summary.aging_buckets:
        result[bucket.label] = (bucket.amount.amount, bucket.invoice_count)
    return result


def test_empty():
    summary = _service([], []).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("0.00"), currency=Currency.DKK)
    assert summary.overdue_amount == Money(amount=Decimal("0.00"), currency=Currency.DKK)
    assert summary.invoices_due_today == 0
    assert summary.invoices_due_this_week == 0
    assert summary.invoices_due_this_month == 0
    assert summary.oldest_invoice is None


def test_one_invoice():
    invoice = _invoice(number="INV-SVC-001", due_date=date(2026, 3, 1), amount="125.00")

    summary = _service([invoice], []).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("125.00"), currency=Currency.DKK)
    assert summary.overdue_amount == Money(amount=Decimal("0.00"), currency=Currency.DKK)
    assert summary.invoices_due_today == 1
    assert summary.invoices_due_this_week == 1
    assert summary.invoices_due_this_month == 1
    assert summary.oldest_invoice == invoice.id


def test_partial_payment():
    invoice = _invoice(number="INV-SVC-002", due_date=date(2026, 3, 5), amount="100.00")
    payment = _payment(invoice=invoice, amount="40.00")

    summary = _service([invoice], [payment]).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("60.00"), currency=Currency.DKK)
    assert summary.oldest_invoice == invoice.id


def test_overdue():
    overdue_invoice = _invoice(number="INV-SVC-003", due_date=date(2026, 2, 10), amount="90.00")
    current_invoice = _invoice(number="INV-SVC-004", due_date=date(2026, 3, 20), amount="110.00")

    summary = _service([overdue_invoice, current_invoice], []).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("200.00"), currency=Currency.DKK)
    assert summary.overdue_amount == Money(amount=Decimal("90.00"), currency=Currency.DKK)
    assert summary.oldest_invoice == overdue_invoice.id


def test_aging():
    invoices = [
        _invoice(number="INV-SVC-005", due_date=date(2026, 3, 1), amount="10.00"),
        _invoice(number="INV-SVC-006", due_date=date(2026, 2, 15), amount="20.00"),
        _invoice(number="INV-SVC-007", due_date=date(2026, 1, 15), amount="30.00"),
        _invoice(number="INV-SVC-008", due_date=date(2025, 12, 15), amount="40.00"),
        _invoice(number="INV-SVC-009", due_date=date(2025, 11, 15), amount="50.00"),
    ]

    summary = _service(invoices, []).summarize(as_of_date=date(2026, 3, 1))
    buckets = _aging_map(summary)

    assert buckets["current"] == (Decimal("10.00"), 1)
    assert buckets["1-30"] == (Decimal("20.00"), 1)
    assert buckets["31-60"] == (Decimal("30.00"), 1)
    assert buckets["61-90"] == (Decimal("40.00"), 1)
    assert buckets["90+"] == (Decimal("50.00"), 1)


def test_multiple_invoices():
    invoices = [
        _invoice(number="INV-SVC-010", due_date=date(2026, 3, 1), amount="100.00"),
        _invoice(number="INV-SVC-011", due_date=date(2026, 3, 3), amount="200.00"),
        _invoice(number="INV-SVC-012", due_date=date(2026, 3, 25), amount="50.00"),
    ]

    summary = _service(invoices, []).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("350.00"), currency=Currency.DKK)
    assert summary.invoices_due_today == 1
    assert summary.invoices_due_this_week == 2
    assert summary.invoices_due_this_month == 3


def test_multiple_members():
    member_a = uuid4()
    member_b = uuid4()
    invoice_a = _invoice(
        number="INV-SVC-013",
        due_date=date(2026, 3, 1),
        amount="100.00",
        member_id=member_a,
    )
    invoice_b = _invoice(
        number="INV-SVC-014",
        due_date=date(2026, 2, 1),
        amount="80.00",
        member_id=member_b,
    )
    payment_b = _payment(invoice=invoice_b, amount="30.00")

    summary = _service([invoice_a, invoice_b], [payment_b]).summarize(as_of_date=date(2026, 3, 1))

    assert summary.total_open_amount == Money(amount=Decimal("150.00"), currency=Currency.DKK)
    assert summary.overdue_amount == Money(amount=Decimal("50.00"), currency=Currency.DKK)
    assert summary.oldest_invoice == invoice_b.id
