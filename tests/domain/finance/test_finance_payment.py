from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import InvalidPaymentAmountError
from mfm.domain.finance.exceptions import InvalidPaymentDatesError
from mfm.domain.finance.exceptions import InvalidPaymentReferenceError
from mfm.domain.finance.exceptions import InvalidPaymentTransitionError
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_method import PaymentMethod
from mfm.domain.finance.payment_reference import PaymentReference
from mfm.domain.finance.payment_status import PaymentStatus


def _payment(
    *,
    amount: str = "100.00",
    status: PaymentStatus = PaymentStatus.REGISTERED,
    payment_date: date = date(2026, 1, 10),
    method: PaymentMethod = PaymentMethod.BANK_TRANSFER,
    notes: str | None = "Initial note",
):
    return Payment(
        payment_reference=PaymentReference("PAY-2026-0001"),
        invoice_id=uuid4(),
        member_id=uuid4(),
        amount=Money(amount=Decimal(amount), currency=Currency.DKK),
        payment_date=payment_date,
        method=method,
        status=status,
        external_reference=" ext-123 ",
        notes=notes,
        invoice_issue_date=date(2026, 1, 1),
    )


def test_create_payment():
    payment = _payment()

    assert payment.status == PaymentStatus.REGISTERED
    assert payment.payment_reference.value == "PAY-2026-0001"
    assert payment.amount == Money(amount=Decimal("100.00"), currency=Currency.DKK)
    assert payment.external_reference == "ext-123"
    assert payment.notes == "Initial note"
    assert payment.is_confirmed() is False


def test_invalid_amount():
    with pytest.raises(InvalidPaymentAmountError):
        _payment(amount="0.00")


def test_invalid_payment_date_before_invoice_issue_date():
    with pytest.raises(InvalidPaymentDatesError):
        Payment(
            payment_reference=PaymentReference("PAY-2026-0002"),
            invoice_id=uuid4(),
            member_id=uuid4(),
            amount=Money(amount=Decimal("100.00"), currency=Currency.DKK),
            payment_date=date(2025, 12, 31),
            method=PaymentMethod.CASH,
            invoice_issue_date=date(2026, 1, 1),
        )


def test_confirm():
    payment = _payment()

    payment.confirm()

    assert payment.status == PaymentStatus.CONFIRMED
    assert payment.is_confirmed() is True


def test_reject():
    payment = _payment()

    payment.reject()

    assert payment.status == PaymentStatus.REJECTED
    assert payment.is_confirmed() is False


def test_refund_requires_confirmed_payment():
    payment = _payment()

    with pytest.raises(InvalidPaymentTransitionError):
        payment.refund()

    payment.confirm()
    payment.refund()

    assert payment.status == PaymentStatus.REFUNDED


def test_invalid_transitions():
    payment = _payment(status=PaymentStatus.REJECTED)
    with pytest.raises(InvalidPaymentTransitionError):
        payment.confirm()

    payment = _payment(status=PaymentStatus.CONFIRMED)
    with pytest.raises(InvalidPaymentTransitionError):
        payment.reject()

    payment = _payment(status=PaymentStatus.REFUNDED)
    with pytest.raises(InvalidPaymentTransitionError):
        payment.confirm()


def test_change_notes():
    payment = _payment()

    payment.change_notes("  Updated note  ")
    assert payment.notes == "Updated note"

    payment.change_notes(None)
    assert payment.notes is None


def test_payment_methods_enum_values():
    assert PaymentMethod.CASH.value == "CASH"
    assert PaymentMethod.BANK_TRANSFER.value == "BANK_TRANSFER"
    assert PaymentMethod.CREDIT_CARD.value == "CREDIT_CARD"
    assert PaymentMethod.MOBILEPAY.value == "MOBILEPAY"
    assert PaymentMethod.PAYPAL.value == "PAYPAL"
    assert PaymentMethod.OTHER.value == "OTHER"


def test_payment_status_enum_values():
    assert PaymentStatus.REGISTERED.value == "REGISTERED"
    assert PaymentStatus.CONFIRMED.value == "CONFIRMED"
    assert PaymentStatus.REJECTED.value == "REJECTED"
    assert PaymentStatus.REFUNDED.value == "REFUNDED"


def test_references_are_required_and_normalized():
    reference = PaymentReference("  pay-2026-0003  ")
    assert reference.value == "PAY-2026-0003"

    with pytest.raises(InvalidPaymentReferenceError):
        PaymentReference("")


def test_payment_belongs_to_one_invoice_reference():
    with pytest.raises(InvalidPaymentReferenceError):
        Payment(
            payment_reference=PaymentReference("PAY-2026-0004"),
            invoice_id="not-uuid",  # type: ignore[arg-type]
            member_id=uuid4(),
            amount=Money(amount=Decimal("10.00"), currency=Currency.DKK),
            payment_date=date(2026, 1, 2),
            method=PaymentMethod.CASH,
            invoice_issue_date=date(2026, 1, 1),
        )
