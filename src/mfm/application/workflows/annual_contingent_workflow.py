"""Annual contingent generation workflow orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.finance.currency import Currency as FinanceCurrency
from mfm.domain.finance.invoice import Invoice
from mfm.domain.finance.invoice_line import InvoiceLine
from mfm.domain.finance.invoice_number import InvoiceNumber
from mfm.domain.finance.money import Money as FinanceMoney
from mfm.domain.membership.membership import Membership


@dataclass(slots=True)
class InvoiceCreatedEvent(DomainEvent):
    invoice_id: UUID = field(default_factory=uuid4)
    member_id: UUID = field(default_factory=uuid4)
    membership_id: UUID = field(default_factory=uuid4)


@dataclass(slots=True)
class SummaryDTO:
    memberships_processed: int = 0
    invoices_created: int = 0
    journals_created: int = 0
    skipped: int = 0
    failed: int = 0


class MembershipRepository(Protocol):
    def list_active(self) -> list[Membership]: ...


class ContingentRepository(Protocol):
    def get_active_for_membership_type(
        self,
        membership_type_id: UUID,
        at_date: date,
    ) -> ContingentPlan | None: ...


class InvoiceRepository(Protocol):
    def add(self, invoice: Invoice) -> None: ...

    def exists_for_member_and_year(self, member_id: UUID, year: int) -> bool: ...


class JournalRepository(Protocol):
    def add(self, journal: JournalEntry) -> None: ...


class FiscalYearRepository(Protocol):
    def ensure_posting_allowed(self, posting_date: date) -> None: ...


class AnnualContingentWorkflow:
    """Generates annual contingent invoices and journal drafts by orchestration only."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, *, run_date: date | None = None) -> SummaryDTO:
        target_date = run_date or datetime.now(UTC).date()
        summary = SummaryDTO()

        with self._unit_of_work as uow:
            membership_repository: MembershipRepository = uow.membership_repository
            contingent_repository: ContingentRepository = uow.contingent_repository
            invoice_repository: InvoiceRepository = uow.invoice_repository
            journal_repository: JournalRepository = uow.journal_repository
            fiscal_year_repository: FiscalYearRepository = uow.fiscal_year_repository

            fiscal_year_repository.ensure_posting_allowed(target_date)

            active_memberships = membership_repository.list_active()
            for membership in active_memberships:
                summary.memberships_processed += 1

                if invoice_repository.exists_for_member_and_year(
                    membership.member_id,
                    target_date.year,
                ):
                    summary.skipped += 1
                    continue

                contingent_plan = contingent_repository.get_active_for_membership_type(
                    membership.membership_type_id,
                    target_date,
                )
                if contingent_plan is None:
                    summary.skipped += 1
                    continue

                unit_price = FinanceMoney(
                    amount=contingent_plan.amount,
                    currency=FinanceCurrency(contingent_plan.currency.value),
                )
                invoice = Invoice(
                    invoice_number=InvoiceNumber(
                        f"INV-{membership.member_id.hex[:8]}-{target_date:%Y}"
                    ),
                    member_id=membership.member_id,
                    issue_date=target_date,
                    due_date=target_date
                    + timedelta(days=contingent_plan.invoice_rule.due_days),
                    lines=[
                        InvoiceLine(
                            description=(
                                f"Annual contingent {target_date.year} - "
                                f"{membership.membership_type.name}"
                            ),
                            quantity=Decimal("1"),
                            unit_price=unit_price,
                        )
                    ],
                )
                invoice_repository.add(invoice)
                summary.invoices_created += 1

                journal = JournalEntry(
                    journal_number=(
                        f"JRN-{membership.member_id.hex[:8]}-{target_date:%Y}"
                    ),
                    posting_date=target_date,
                    description=(
                        f"Annual contingent draft {target_date.year} "
                        f"for member {membership.member_id}"
                    ),
                    reference=str(invoice.invoice_number),
                    lines=[
                        JournalLine(
                            account_id=uuid4(),
                            side=PostingSide.DEBIT,
                            amount=invoice.total,
                            description="Accounts receivable",
                        ),
                        JournalLine(
                            account_id=uuid4(),
                            side=PostingSide.CREDIT,
                            amount=invoice.total,
                            description="Membership contingent revenue",
                        ),
                    ],
                )
                journal_repository.add(journal)
                summary.journals_created += 1

                self._dispatcher.dispatch(
                    InvoiceCreatedEvent(
                        invoice_id=invoice.id,
                        member_id=membership.member_id,
                        membership_id=membership.id,
                    )
                )

            uow.commit()

        return summary
