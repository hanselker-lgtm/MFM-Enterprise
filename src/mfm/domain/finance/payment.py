"""Payment aggregate for finance domain."""

from __future__ import annotations

from dataclasses import InitVar
from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.finance.exceptions import InvalidPaymentAmountError
from mfm.domain.finance.exceptions import InvalidPaymentDatesError
from mfm.domain.finance.exceptions import InvalidPaymentReferenceError
from mfm.domain.finance.exceptions import InvalidPaymentTransitionError
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment_method import PaymentMethod
from mfm.domain.finance.payment_reference import PaymentReference
from mfm.domain.finance.payment_status import PaymentStatus


@dataclass(slots=True)
class Payment(AggregateRoot):
    """Aggregate root representing a payment tied to one invoice."""

    payment_reference: PaymentReference
    invoice_id: UUID
    member_id: UUID
    amount: Money
    payment_date: date
    method: PaymentMethod
    status: PaymentStatus = PaymentStatus.REGISTERED
    external_reference: str | None = None
    notes: str | None = None
    id: UUID = field(default_factory=uuid4)
    invoice_issue_date: InitVar[date | None] = None

    def __post_init__(self, invoice_issue_date: date | None) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, UUID):
            raise InvalidPaymentReferenceError("id must be a UUID")

        if not isinstance(self.payment_reference, PaymentReference):
            raise InvalidPaymentReferenceError(
                "payment_reference must be a PaymentReference"
            )

        if not isinstance(self.invoice_id, UUID):
            raise InvalidPaymentReferenceError("invoice_id must be a UUID")

        if not isinstance(self.member_id, UUID):
            raise InvalidPaymentReferenceError("member_id must be a UUID")

        if not isinstance(self.amount, Money):
            raise InvalidPaymentAmountError("amount must be Money")

        if self.amount.amount <= 0:
            raise InvalidPaymentAmountError("amount must be greater than zero")

        if not isinstance(self.payment_date, date):
            raise InvalidPaymentDatesError("payment_date must be a date")

        if invoice_issue_date is not None:
            if not isinstance(invoice_issue_date, date):
                raise InvalidPaymentDatesError("invoice_issue_date must be a date")
            if self.payment_date < invoice_issue_date:
                raise InvalidPaymentDatesError(
                    "payment_date cannot be before invoice issue date"
                )

        if not isinstance(self.method, PaymentMethod):
            raise InvalidPaymentReferenceError("method must be PaymentMethod")

        if not isinstance(self.status, PaymentStatus):
            raise InvalidPaymentReferenceError("status must be PaymentStatus")

        if self.external_reference is not None:
            if not isinstance(self.external_reference, str):
                raise InvalidPaymentReferenceError(
                    "external_reference must be a string"
                )
            normalized_reference = self.external_reference.strip()
            self.external_reference = normalized_reference or None

        if self.notes is not None:
            if not isinstance(self.notes, str):
                raise InvalidPaymentReferenceError("notes must be a string")
            normalized_notes = self.notes.strip()
            self.notes = normalized_notes or None

    def confirm(self) -> None:
        if self.status == PaymentStatus.REJECTED:
            raise InvalidPaymentTransitionError(
                "REJECTED payments cannot be confirmed again"
            )
        if self.status == PaymentStatus.REFUNDED:
            raise InvalidPaymentTransitionError("REFUNDED payments are terminal")
        if self.status == PaymentStatus.CONFIRMED:
            raise InvalidPaymentTransitionError("CONFIRMED payment cannot be changed")
        self.status = PaymentStatus.CONFIRMED

    def reject(self) -> None:
        if self.status == PaymentStatus.CONFIRMED:
            raise InvalidPaymentTransitionError("CONFIRMED payment cannot be changed")
        if self.status == PaymentStatus.REJECTED:
            raise InvalidPaymentTransitionError("payment is already rejected")
        if self.status == PaymentStatus.REFUNDED:
            raise InvalidPaymentTransitionError("REFUNDED payments are terminal")
        self.status = PaymentStatus.REJECTED

    def refund(self) -> None:
        if self.status == PaymentStatus.REFUNDED:
            raise InvalidPaymentTransitionError("payment is already refunded")
        if self.status != PaymentStatus.CONFIRMED:
            raise InvalidPaymentTransitionError(
                "REFUNDED requires previously CONFIRMED payment"
            )
        self.status = PaymentStatus.REFUNDED

    def change_notes(self, notes: str | None) -> None:
        if notes is None:
            self.notes = None
            return

        if not isinstance(notes, str):
            raise InvalidPaymentReferenceError("notes must be a string")

        normalized_notes = notes.strip()
        self.notes = normalized_notes or None

    def is_confirmed(self) -> bool:
        return self.status == PaymentStatus.CONFIRMED
