"""Real, database-backed repository for member invoices.

Previously there was no persistence at all for
:class:`mfm.domain.finance.invoice.Invoice` anywhere in the codebase,
which meant the annual contingent billing feature
(:mod:`mfm.application.features.annual_contingent_generation`) could
never actually run -- it had nowhere to save the invoices it creates.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.invoice_mapper import InvoiceMapper
from mfm.database.models.invoice_model import InvoiceModel
from mfm.domain.finance.invoice import Invoice


class SqlAlchemyInvoiceRepository:
    """SQLAlchemy-backed repository for member invoices."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, invoice: Invoice) -> None:
        self._session.add(InvoiceMapper.to_orm(invoice))
        self._session.flush()

    def get(self, invoice_id: UUID) -> Invoice | None:
        model = self._session.get(InvoiceModel, invoice_id)
        if model is None:
            return None
        return InvoiceMapper.to_domain(model)

    def list_for_member(self, member_id: UUID) -> list[Invoice]:
        models = self._session.scalars(
            select(InvoiceModel).where(InvoiceModel.member_id == member_id)
        ).all()
        return [InvoiceMapper.to_domain(model) for model in models]

    def exists_for_member_and_year(self, member_id: UUID, year: int) -> bool:
        # An invoice belongs to fiscal year `year` if it was issued
        # within that calendar year -- matches how invoice numbers are
        # generated (INV-<member>-<fiscal_year>) elsewhere in this
        # feature, keeping the "already billed this year" check simple
        # and independent of the fiscal year's exact start/end dates.
        from datetime import date

        start = date(year, 1, 1)
        end = date(year, 12, 31)
        match = self._session.scalar(
            select(InvoiceModel.id).where(
                InvoiceModel.member_id == member_id,
                InvoiceModel.issue_date >= start,
                InvoiceModel.issue_date <= end,
            )
        )
        return match is not None
