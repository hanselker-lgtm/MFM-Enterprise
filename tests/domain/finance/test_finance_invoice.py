from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import EmptyInvoiceError
from mfm.domain.finance.exceptions import InvalidInvoiceDatesError
from mfm.domain.finance.exceptions import InvalidInvoiceLineError
from mfm.domain.finance.exceptions import InvalidInvoiceTransitionError
from mfm.domain.finance.exceptions import InvoiceOverpaymentError
from mfm.domain.finance.exceptions import InvoicePaymentError
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.invoice_status import InvoiceStatus
from mfm.domain.finance.money import Money


def _line(
    *, description: str = "Membership fee", quantity: str = "1", unit_price: str = "100.00"
) -> InvoiceLine:
    return InvoiceLine(
        description=description,
        quantity=Decimal(quantity),
        unit_price=Money(amount=Decimal(unit_price), currency=Currency.DKK),
    )


def _invoice(*, lines: list[InvoiceLine] | None = None) -> Invoice:
    normalized_lines = [_line()] if lines is None else lines
    return Invoice(
        invoice_number=InvoiceNumber("INV-2026-0001"),
        member_id=uuid4(),
        issue_date=date(2026, 1, 1),
        due_date=date(2026, 1, 15),
        lines=normalized_lines,
    )


def test_create_invoice():
    invoice = _invoice()

    assert invoice.status == InvoiceStatus.DRAFT
    assert invoice.invoice_number.value == "INV-2026-0001"
    assert invoice.currency == Currency.DKK
    assert invoice.total == Money(amount=Decimal("100.00"), currency=Currency.DKK)


def test_empty_invoice_is_rejected():
    with pytest.raises(EmptyInvoiceError):
        _invoice(lines=[])


def test_due_date_must_be_on_or_after_issue_date():
    with pytest.raises(InvalidInvoiceDatesError):
        Invoice(
            invoice_number=InvoiceNumber("INV-2026-0002"),
            member_id=uuid4(),
            issue_date=date(2026, 1, 15),
            due_date=date(2026, 1, 14),
            lines=[_line()],
        )


def test_add_line_updates_calculated_total():
    invoice = _invoice()

    invoice.add_line(_line(description="Boat storage", quantity="2", unit_price="50.00"))

    assert invoice.total == Money(amount=Decimal("200.00"), currency=Currency.DKK)


def test_remove_line_updates_calculated_total():
    first = _line(description="Membership", quantity="1", unit_price="100.00")
    second = _line(description="Key deposit", quantity="1", unit_price="200.00")
    invoice = _invoice(lines=[first, second])

    invoice.remove_line(second)

    assert invoice.total == Money(amount=Decimal("100.00"), currency=Currency.DKK)


def test_remove_last_line_is_rejected():
    invoice = _invoice()

    with pytest.raises(EmptyInvoiceError):
        invoice.remove_line(invoice.lines[0])


def test_calculate_total_matches_total_property():
    invoice = _invoice(
        lines=[
            _line(quantity="2", unit_price="100.00"),
            _line(quantity="1", unit_price="50.00"),
        ]
    )

    assert invoice.calculate_total() == Money(amount=Decimal("250.00"), currency=Currency.DKK)
    assert invoice.total == Money(amount=Decimal("250.00"), currency=Currency.DKK)


def test_total_cannot_be_edited_directly():
    invoice = _invoice()

    with pytest.raises(AttributeError):
        invoice.total = Money(amount=Decimal("999.00"), currency=Currency.DKK)  # type: ignore[misc]


def test_issue_changes_status():
    invoice = _invoice()

    invoice.issue()

    assert invoice.status == InvoiceStatus.ISSUED


def test_cancel_changes_status():
    invoice = _invoice()
    invoice.issue()

    invoice.cancel()

    assert invoice.status == InvoiceStatus.CANCELLED


def test_register_partial_payment_changes_status():
    invoice = _invoice(lines=[_line(quantity="2", unit_price="100.00")])
    invoice.issue()

    invoice.register_partial_payment(
        Money(amount=Decimal("50.00"), currency=Currency.DKK)
    )

    assert invoice.status == InvoiceStatus.PARTIALLY_PAID


def test_register_payment_marks_invoice_paid():
    invoice = _invoice(lines=[_line(quantity="2", unit_price="100.00")])
    invoice.issue()

    invoice.register_payment()

    assert invoice.status == InvoiceStatus.PAID


def test_overpayment_is_rejected():
    invoice = _invoice(lines=[_line(quantity="1", unit_price="100.00")])
    invoice.issue()

    with pytest.raises(InvoiceOverpaymentError):
        invoice.register_partial_payment(
            Money(amount=Decimal("150.00"), currency=Currency.DKK)
        )


def test_paid_invoice_cannot_be_changed():
    invoice = _invoice()
    invoice.issue()
    invoice.register_payment()

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.cancel()

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.credit()


def test_cancelled_invoice_cannot_be_paid():
    invoice = _invoice()
    invoice.issue()
    invoice.cancel()

    with pytest.raises(InvoicePaymentError):
        invoice.register_payment()


def test_credited_invoice_is_terminal():
    invoice = _invoice()
    invoice.issue()
    invoice.credit()

    assert invoice.status == InvoiceStatus.CREDITED

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.add_line(_line(description="Extra", quantity="1", unit_price="10.00"))

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.cancel()

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.register_payment()


def test_invalid_transitions():
    invoice = _invoice()

    with pytest.raises(InvoicePaymentError):
        invoice.register_payment()

    invoice.issue()

    with pytest.raises(InvalidInvoiceTransitionError):
        invoice.issue()


def test_negative_line_is_allowed_for_credit_lines():
    invoice = _invoice(
        lines=[
            _line(description="Membership fee", quantity="1", unit_price="100.00"),
            _line(description="Credit adjustment", quantity="1", unit_price="-25.00"),
        ]
    )

    assert invoice.total == Money(amount=Decimal("75.00"), currency=Currency.DKK)


def test_invoice_line_quantity_must_be_greater_than_zero():
    with pytest.raises(InvalidInvoiceLineError):
        InvoiceLine(
            description="Invalid line",
            quantity=Decimal("0"),
            unit_price=Money(amount=Decimal("10.00"), currency=Currency.DKK),
        )
