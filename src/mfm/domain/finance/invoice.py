"""Invoice aggregate for finance domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.exceptions import EmptyInvoiceError
from mfm.domain.finance.exceptions import InvalidInvoiceDatesError
from mfm.domain.finance.exceptions import InvalidInvoiceLineError
from mfm.domain.finance.exceptions import InvalidInvoiceReferenceError
from mfm.domain.finance.exceptions import InvalidInvoiceTransitionError
from mfm.domain.finance.exceptions import InvoiceOverpaymentError
from mfm.domain.finance.exceptions import InvoicePaymentError
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.invoice_status import InvoiceStatus
from mfm.domain.finance.money import Money


@dataclass(slots=True)
class Invoice(AggregateRoot):
    """Aggregate root for invoice lifecycle and payment state."""

    invoice_number: InvoiceNumber
    member_id: UUID
    issue_date: date
    due_date: date
    lines: list[InvoiceLine]
    status: InvoiceStatus = InvoiceStatus.DRAFT
    id: UUID = field(default_factory=uuid4)
    _paid_amount: Money | None = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, UUID):
            raise InvalidInvoiceReferenceError("id must be a UUID")

        if not isinstance(self.invoice_number, InvoiceNumber):
            raise InvalidInvoiceReferenceError("invoice_number must be InvoiceNumber")

        if not isinstance(self.member_id, UUID):
            raise InvalidInvoiceReferenceError("member_id must be a UUID")

        if not isinstance(self.issue_date, date) or not isinstance(self.due_date, date):
            raise InvalidInvoiceDatesError("issue_date and due_date must be dates")

        if self.due_date < self.issue_date:
            raise InvalidInvoiceDatesError("due_date must be on or after issue_date")

        if not isinstance(self.status, InvoiceStatus):
            raise InvalidInvoiceReferenceError("status must be InvoiceStatus")

        if not isinstance(self.lines, list):
            raise InvalidInvoiceLineError("lines must be a list")

        if len(self.lines) == 0:
            raise EmptyInvoiceError("invoice must have at least one line")

        for line in self.lines:
            if not isinstance(line, InvoiceLine):
                raise InvalidInvoiceLineError("all lines must be InvoiceLine")

        self._assert_line_currencies()
        self._paid_amount = Money(amount=Decimal("0"), currency=self.currency)

    @property
    def currency(self) -> Currency:
        return self.lines[0].unit_price.currency

    @property
    def total(self) -> Money:
        return self.calculate_total()

    def calculate_total(self) -> Money:
        total = Money(amount=Decimal("0"), currency=self.currency)
        for line in self.lines:
            total = total + line.total
        return total

    def add_line(self, line: InvoiceLine) -> None:
        self._assert_modifiable()
        if not isinstance(line, InvoiceLine):
            raise InvalidInvoiceLineError("line must be InvoiceLine")
        if line.unit_price.currency != self.currency:
            raise InvalidInvoiceLineError("line currency must match invoice currency")
        self.lines.append(line)

    def remove_line(self, line: InvoiceLine) -> None:
        self._assert_modifiable()
        if line not in self.lines:
            raise InvalidInvoiceLineError("line does not exist on invoice")
        if len(self.lines) == 1:
            raise EmptyInvoiceError("invoice must have at least one line")
        self.lines.remove(line)

    def issue(self) -> None:
        self._assert_not_terminal()
        if self.status != InvoiceStatus.DRAFT:
            raise InvalidInvoiceTransitionError("Only DRAFT invoices can be issued")
        self.status = InvoiceStatus.ISSUED

    def register_partial_payment(self, amount: Money) -> None:
        self._assert_payable()
        if not isinstance(amount, Money):
            raise InvoicePaymentError("amount must be Money")
        if amount.currency != self.currency:
            raise InvoicePaymentError("payment currency must match invoice currency")
        if amount.amount <= Decimal("0"):
            raise InvoicePaymentError("payment amount must be greater than zero")

        outstanding = self.total - self._paid_amount
        if amount > outstanding:
            raise InvoiceOverpaymentError("payment exceeds outstanding balance")

        self._paid_amount = self._paid_amount + amount

        if self._paid_amount == self.total:
            self.status = InvoiceStatus.PAID
        else:
            self.status = InvoiceStatus.PARTIALLY_PAID

    def register_payment(self) -> None:
        self._assert_payable()
        outstanding = self.total - self._paid_amount
        if outstanding.amount <= Decimal("0"):
            raise InvoicePaymentError("invoice is already fully paid")

        self._paid_amount = self.total
        self.status = InvoiceStatus.PAID

    def cancel(self) -> None:
        self._assert_not_terminal()
        if self.status == InvoiceStatus.PAID:
            raise InvalidInvoiceTransitionError("PAID invoices cannot be changed")
        self.status = InvoiceStatus.CANCELLED

    def credit(self) -> None:
        self._assert_not_terminal()
        if self.status == InvoiceStatus.PAID:
            raise InvalidInvoiceTransitionError("PAID invoices cannot be changed")
        self.status = InvoiceStatus.CREDITED

    def _assert_line_currencies(self) -> None:
        expected_currency = self.lines[0].unit_price.currency
        for line in self.lines[1:]:
            if line.unit_price.currency != expected_currency:
                raise InvalidInvoiceLineError(
                    "all invoice line currencies must match"
                )

    def _assert_not_terminal(self) -> None:
        if self.status == InvoiceStatus.CREDITED:
            raise InvalidInvoiceTransitionError("CREDITED invoices are terminal")

    def _assert_modifiable(self) -> None:
        self._assert_not_terminal()
        if self.status in (InvoiceStatus.PAID, InvoiceStatus.CANCELLED):
            raise InvalidInvoiceTransitionError("Invoice cannot be modified in current status")

    def _assert_payable(self) -> None:
        self._assert_not_terminal()
        if self.status == InvoiceStatus.DRAFT:
            raise InvoicePaymentError("Invoice must be issued before payment")
        if self.status == InvoiceStatus.CANCELLED:
            raise InvoicePaymentError("CANCELLED invoices cannot be paid")
        if self.status == InvoiceStatus.PAID:
            raise InvalidInvoiceTransitionError("PAID invoices cannot be changed")
