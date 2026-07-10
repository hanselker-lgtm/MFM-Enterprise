"""Annual contingent generation feature orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
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


class ApplicationException(Exception):
    """Base exception for application-level feature failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class CreateAnnualContingentRequest:
    fiscal_year: int
    billing_date: date
    membership_type_id: UUID | None = None
    dry_run: bool = False

    def validate(self) -> None:
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValidationException("fiscal_year must be an integer >= 2000")
        if not isinstance(self.billing_date, date):
            raise ValidationException("billing_date must be a date")
        if self.membership_type_id is not None and not isinstance(
            self.membership_type_id,
            UUID,
        ):
            raise ValidationException("membership_type_id must be a UUID when provided")


@dataclass(frozen=True, slots=True)
class CreateAnnualContingentResponse:
    processed: int
    invoices_created: int
    journal_drafts_created: int
    skipped: int
    warnings: tuple[str, ...]
    errors: tuple[str, ...]


@dataclass(slots=True)
class InvoiceCreatedEvent(DomainEvent):
    invoice_id: UUID = field(default_factory=uuid4)
    member_id: UUID = field(default_factory=uuid4)
    membership_id: UUID = field(default_factory=uuid4)


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


class AnnualContingentGenerationFeature:
    """Generate annual contingent invoices and journal drafts by orchestration."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(
        self,
        request: CreateAnnualContingentRequest,
    ) -> CreateAnnualContingentResponse:
        request.validate()

        processed = 0
        invoices_created = 0
        journal_drafts_created = 0
        skipped = 0
        warnings: list[str] = []
        errors: list[str] = []
        events_to_dispatch: list[InvoiceCreatedEvent] = []

        try:
            with self._unit_of_work as uow:
                membership_repository: MembershipRepository = uow.membership_repository
                contingent_repository: ContingentRepository = uow.contingent_repository
                invoice_repository: InvoiceRepository = uow.invoice_repository
                journal_repository: JournalRepository = uow.journal_repository
                fiscal_year_repository: FiscalYearRepository = uow.fiscal_year_repository

                try:
                    fiscal_year_repository.ensure_posting_allowed(request.billing_date)
                except Exception as exc:
                    raise BusinessRuleViolation(str(exc)) from exc

                for membership in membership_repository.list_active():
                    if request.membership_type_id is not None and (
                        membership.membership_type_id != request.membership_type_id
                    ):
                        continue

                    processed += 1

                    if invoice_repository.exists_for_member_and_year(
                        membership.member_id,
                        request.fiscal_year,
                    ):
                        skipped += 1
                        warnings.append(
                            (
                                "Invoice already exists for member "
                                f"{membership.member_id} in fiscal year {request.fiscal_year}"
                            )
                        )
                        continue

                    contingent_plan = contingent_repository.get_active_for_membership_type(
                        membership.membership_type_id,
                        request.billing_date,
                    )
                    if contingent_plan is None:
                        skipped += 1
                        warnings.append(
                            (
                                "No active contingent plan for membership "
                                f"{membership.id} at {request.billing_date.isoformat()}"
                            )
                        )
                        continue

                    invoice_amount = FinanceMoney(
                        amount=contingent_plan.amount,
                        currency=FinanceCurrency(contingent_plan.currency.value),
                    )

                    if request.dry_run:
                        invoices_created += 1
                        journal_drafts_created += 1
                        continue

                    invoice = Invoice(
                        invoice_number=InvoiceNumber(
                            f"INV-{membership.member_id.hex[:8]}-{request.fiscal_year}"
                        ),
                        member_id=membership.member_id,
                        issue_date=request.billing_date,
                        due_date=request.billing_date
                        + timedelta(days=contingent_plan.invoice_rule.due_days),
                        lines=[
                            InvoiceLine(
                                description=(
                                    f"Annual contingent {request.fiscal_year} - "
                                    f"{membership.membership_type.name}"
                                ),
                                quantity=Decimal("1"),
                                unit_price=invoice_amount,
                            )
                        ],
                    )
                    invoice_repository.add(invoice)
                    invoices_created += 1

                    journal = JournalEntry(
                        journal_number=(
                            f"JRN-{membership.member_id.hex[:8]}-{request.fiscal_year}"
                        ),
                        posting_date=request.billing_date,
                        description=(
                            f"Annual contingent draft {request.fiscal_year} "
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
                    journal_drafts_created += 1

                    events_to_dispatch.append(
                        InvoiceCreatedEvent(
                            invoice_id=invoice.id,
                            member_id=membership.member_id,
                            membership_id=membership.id,
                        )
                    )

                if not request.dry_run:
                    uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Annual contingent generation failed") from exc

        if not request.dry_run:
            for event in events_to_dispatch:
                self._dispatcher.dispatch(event)

        return CreateAnnualContingentResponse(
            processed=processed,
            invoices_created=invoices_created,
            journal_drafts_created=journal_drafts_created,
            skipped=skipped,
            warnings=tuple(warnings),
            errors=tuple(errors),
        )


class CreateAnnualContingentFeature(AnnualContingentGenerationFeature):
    """Public feature name following the standard naming convention."""


# Backward-compat aliases for transition.
AnnualContingentRequest = CreateAnnualContingentRequest
AnnualContingentResult = CreateAnnualContingentResponse
