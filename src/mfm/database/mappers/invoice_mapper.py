"""Mapper between Invoice domain objects and ORM models."""

from __future__ import annotations

from mfm.database.models.invoice_model import InvoiceLineModel
from mfm.database.models.invoice_model import InvoiceModel
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.invoice_status import InvoiceStatus
from mfm.domain.finance.money import Money


class InvoiceMapper:
    """Translates between the Invoice aggregate and its ORM rows."""

    @staticmethod
    def to_orm(invoice: Invoice) -> InvoiceModel:
        model = InvoiceModel(
            id=invoice.id,
            invoice_number=invoice.invoice_number.value,
            member_id=invoice.member_id,
            issue_date=invoice.issue_date,
            due_date=invoice.due_date,
            status=invoice.status.value,
        )
        model.lines = [
            InvoiceLineModel(
                line_order=index,
                description=line.description,
                quantity=line.quantity,
                unit_price_amount=line.unit_price.amount,
                unit_price_currency=line.unit_price.currency.value,
            )
            for index, line in enumerate(invoice.lines)
        ]
        return model

    @staticmethod
    def to_domain(model: InvoiceModel) -> Invoice:
        return Invoice(
            id=model.id,
            invoice_number=InvoiceNumber(model.invoice_number),
            member_id=model.member_id,
            issue_date=model.issue_date,
            due_date=model.due_date,
            status=InvoiceStatus(model.status),
            lines=[
                InvoiceLine(
                    description=line.description,
                    quantity=line.quantity,
                    unit_price=Money(
                        amount=line.unit_price_amount,
                        currency=Currency(line.unit_price_currency),
                    ),
                )
                for line in model.lines
            ],
        )
