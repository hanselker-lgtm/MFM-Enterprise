"""Open items application service."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.money import Money
from mfm.domain.finance.payment import Payment
from mfm.domain.finance.payment_status import PaymentStatus
from mfm.domain.finance.receivable import Receivable


@dataclass(slots=True)
class OpenItemsRequest:
    member_id: UUID | None = None
    from_date: date | None = None
    to_date: date | None = None


@dataclass(slots=True)
class OpenItemsDTO:
    invoice_number: str
    invoice_date: date
    due_date: date
    original_amount: Money
    paid_amount: Money
    outstanding_amount: Money
    days_overdue: int
    status: str


class InvoiceRepository(Protocol):
    def list(self) -> list[Invoice]: ...


class PaymentRepository(Protocol):
    def list(self) -> list[Payment]: ...


class OpenItemsService:
    """Returns all open invoice items with computed balances and overdue status."""

    def __init__(
        self,
        *,
        invoice_repository: InvoiceRepository,
        payment_repository: PaymentRepository,
    ) -> None:
        self._invoice_repository = invoice_repository
        self._payment_repository = payment_repository

    def list_open_items(self, request: OpenItemsRequest) -> list[OpenItemsDTO]:
        invoices = self._invoice_repository.list()
        payments = self._payment_repository.list()

        filtered_invoices = self._filter_invoices(invoices, request)
        receivables_by_invoice: dict[UUID, Receivable] = {}
        invoice_by_id: dict[UUID, Invoice] = {}

        for invoice in filtered_invoices:
            invoice_by_id[invoice.id] = invoice
            receivables_by_invoice[invoice.id] = Receivable(
                invoice_id=invoice.id,
                member_id=invoice.member_id,
                due_date=invoice.due_date,
                original_amount=invoice.total,
            )

        for payment in payments:
            if payment.status is not PaymentStatus.CONFIRMED:
                continue
            receivable = receivables_by_invoice.get(payment.invoice_id)
            if receivable is None:
                continue
            try:
                receivable.register_payment(payment_id=payment.id, amount=payment.amount)
            except ValueError:
                continue

        as_of_date = request.to_date or datetime.now(UTC).date()

        rows: list[OpenItemsDTO] = []
        for invoice_id, receivable in receivables_by_invoice.items():
            outstanding = receivable.balance()
            if receivable.closed or outstanding.amount <= Decimal("0"):
                continue

            invoice = invoice_by_id[invoice_id]
            days_overdue = max((as_of_date - invoice.due_date).days, 0)
            rows.append(
                OpenItemsDTO(
                    invoice_number=str(invoice.invoice_number),
                    invoice_date=invoice.issue_date,
                    due_date=invoice.due_date,
                    original_amount=receivable.original_amount,
                    paid_amount=receivable.paid_amount,
                    outstanding_amount=outstanding,
                    days_overdue=days_overdue,
                    status="OVERDUE" if days_overdue > 0 else "OPEN",
                )
            )

        rows.sort(key=lambda item: item.due_date)
        return rows

    @staticmethod
    def _filter_invoices(invoices: list[Invoice], request: OpenItemsRequest) -> list[Invoice]:
        filtered = invoices

        if request.member_id is not None:
            filtered = [
                invoice
                for invoice in filtered
                if invoice.member_id == request.member_id
            ]

        if request.from_date is not None:
            filtered = [
                invoice
                for invoice in filtered
                if invoice.issue_date >= request.from_date
            ]

        if request.to_date is not None:
            filtered = [
                invoice
                for invoice in filtered
                if invoice.issue_date <= request.to_date
            ]

        return filtered
