from __future__ import annotations
from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.application.features.open_items_service import OpenItemsRequest
from mfm.application.features.open_items_service import OpenItemsService
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


def _invoice(*, number: str, issue_date: date, due_date: date, amount: str = "100.00", member_id: UUID | None = None) -> Invoice:
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


def _service(invoices: list[Invoice], payments: list[Payment]) -> OpenItemsService:
    return OpenItemsService(
        invoice_repository=InMemoryInvoiceRepository(invoices),
        payment_repository=InMemoryPaymentRepository(payments),
    )


def test_empty():
    result = _service([], []).list_open_items(OpenItemsRequest())

    assert result == []


def test_one_invoice():
    invoice = _invoice(
        number="INV-OPEN-001",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 20),
        amount="120.00",
    )

    result = _service([invoice], []).list_open_items(
        OpenItemsRequest(to_date=date(2026, 1, 10))
    )

    assert len(result) == 1
    row = result[0]
    assert row.invoice_number == "INV-OPEN-001"
    assert row.original_amount == Money(amount=Decimal("120.00"), currency=Currency.DKK)
    assert row.paid_amount == Money(amount=Decimal("0.00"), currency=Currency.DKK)
    assert row.outstanding_amount == Money(amount=Decimal("120.00"), currency=Currency.DKK)
    assert row.status == "OPEN"


def test_many_invoices():
    invoices = [
        _invoice(number="INV-OPEN-002", issue_date=date(2026, 1, 1), due_date=date(2026, 1, 10), amount="50.00"),
        _invoice(number="INV-OPEN-003", issue_date=date(2026, 1, 1), due_date=date(2026, 1, 11), amount="60.00"),
        _invoice(number="INV-OPEN-004", issue_date=date(2026, 1, 1), due_date=date(2026, 1, 12), amount="70.00"),
    ]

    result = _service(invoices, []).list_open_items(OpenItemsRequest(to_date=date(2026, 1, 5)))

    assert len(result) == 3
    assert [row.invoice_number for row in result] == ["INV-OPEN-002", "INV-OPEN-003", "INV-OPEN-004"]


def test_partial_payment():
    invoice = _invoice(
        number="INV-OPEN-005",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 20),
        amount="100.00",
    )
    payment = _payment(invoice=invoice, amount="30.00")

    result = _service([invoice], [payment]).list_open_items(OpenItemsRequest(to_date=date(2026, 1, 15)))

    assert len(result) == 1
    row = result[0]
    assert row.paid_amount == Money(amount=Decimal("30.00"), currency=Currency.DKK)
    assert row.outstanding_amount == Money(amount=Decimal("70.00"), currency=Currency.DKK)


def test_overdue():
    invoice = _invoice(
        number="INV-OPEN-006",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 10),
        amount="80.00",
    )

    result = _service([invoice], []).list_open_items(OpenItemsRequest(to_date=date(2026, 1, 25)))

    assert len(result) == 1
    row = result[0]
    assert row.days_overdue == 15
    assert row.status == "OVERDUE"


def test_filtering():
    member_a = uuid4()
    member_b = uuid4()
    invoice_a = _invoice(
        number="INV-OPEN-007",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 15),
        amount="100.00",
        member_id=member_a,
    )
    invoice_b = _invoice(
        number="INV-OPEN-008",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 2, 15),
        amount="100.00",
        member_id=member_b,
    )

    result = _service([invoice_a, invoice_b], []).list_open_items(
        OpenItemsRequest(
            member_id=member_a,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    assert len(result) == 1
    assert result[0].invoice_number == "INV-OPEN-007"


def test_sorting():
    first = _invoice(
        number="INV-OPEN-009",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 25),
        amount="10.00",
    )
    second = _invoice(
        number="INV-OPEN-010",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 5),
        amount="10.00",
    )
    third = _invoice(
        number="INV-OPEN-011",
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 15),
        amount="10.00",
    )

    result = _service([first, second, third], []).list_open_items(OpenItemsRequest(to_date=date(2026, 1, 1)))

    assert [row.invoice_number for row in result] == [
        "INV-OPEN-010",
        "INV-OPEN-011",
        "INV-OPEN-009",
    ]
