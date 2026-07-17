"""Workflow orchestration for project accounting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import CreateJournalRequest
from mfm.application.features.accounting import JournalLineInput
from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import PostJournalRequest
from mfm.application.features.accounting.get_journal_feature import GetJournalRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectRequest


@dataclass(frozen=True, slots=True)
class ProjectAccountingWorkflowRequest:
    project_id: UUID
    journal_number: str
    posting_date: date
    transaction_description: str
    debit_account_id: UUID
    credit_account_id: UUID
    amount: Decimal | str | int
    currency: str = "DKK"
    transaction_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValueError("project_id must be UUID")
        if not isinstance(self.journal_number, str) or not self.journal_number.strip():
            raise ValueError("journal_number must be a non-empty string")
        if not isinstance(self.posting_date, date):
            raise ValueError("posting_date must be date")
        if not isinstance(self.transaction_description, str) or not self.transaction_description.strip():
            raise ValueError("transaction_description must be a non-empty string")
        if not isinstance(self.debit_account_id, UUID):
            raise ValueError("debit_account_id must be UUID")
        if not isinstance(self.credit_account_id, UUID):
            raise ValueError("credit_account_id must be UUID")
        if isinstance(self.amount, bool) or isinstance(self.amount, float):
            raise ValueError("amount must not be bool/float")
        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValueError("currency must be a non-empty string")
        if self.transaction_reference is not None and not isinstance(self.transaction_reference, str):
            raise ValueError("transaction_reference must be string or None")


@dataclass(frozen=True, slots=True)
class ProjectAccountingWorkflowResponse:
    project_id: UUID
    journal_id: UUID
    journal_number: str
    journal_status: str
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when project accounting fails at a specific workflow step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class UpdateProjectFeaturePort(Protocol):
    def execute(self, request: UpdateProjectRequest): ...


class CreateJournalFeaturePort(Protocol):
    def execute(self, request: CreateJournalRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class PostJournalFeaturePort(Protocol):
    def execute(self, request: PostJournalRequest): ...


class GetJournalFeaturePort(Protocol):
    def execute(self, request: GetJournalRequest): ...


class ProjectAccountingWorkflow:
    """Orchestrates accounting transaction lifecycle with project traceability."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        update_project_feature: UpdateProjectFeaturePort,
        create_journal_feature: CreateJournalFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
        post_journal_feature: PostJournalFeaturePort,
        get_journal_feature: GetJournalFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._update_project = update_project_feature
        self._create_journal = create_journal_feature
        self._list_fiscal_years = list_fiscal_years_feature
        self._post_journal = post_journal_feature
        self._get_journal = get_journal_feature

    def execute(
        self,
        request: ProjectAccountingWorkflowRequest,
    ) -> ProjectAccountingWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        project_id = self._step_select_project(request.project_id)
        completed_steps.append("STEP-001")

        project = self._step_verify_project_and_budget_ready(project_id)
        completed_steps.append("STEP-002")

        created_journal = self._step_create_accounting_transaction(project_id=project_id, request=request)
        completed_steps.append("STEP-003")

        self._step_validate_fiscal_year_open(posting_date=request.posting_date)
        completed_steps.append("STEP-004")

        posted_journal = self._step_post_journal_entry(journal_id=created_journal.journal_id)
        completed_steps.append("STEP-005")

        self._step_link_transaction_to_project(
            project_id=project_id,
            project_references=project.references,
            journal_id=posted_journal.journal_id,
            journal_number=posted_journal.journal_number,
        )
        completed_steps.append("STEP-006")

        self._step_verify_accounting_integrity(project_id=project_id, journal_id=posted_journal.journal_id)
        completed_steps.append("STEP-007")

        return ProjectAccountingWorkflowResponse(
            project_id=project_id,
            journal_id=posted_journal.journal_id,
            journal_number=posted_journal.journal_number,
            journal_status=posted_journal.status,
            completed_steps=tuple(completed_steps),
        )

    def _step_select_project(self, project_id: UUID) -> UUID:
        try:
            return project_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Select project failed") from exc

    def _step_verify_project_and_budget_ready(self, project_id: UUID):
        try:
            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
            is_budget_ready = any(
                ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper() == "BUDGET_STATUS:READY"
                for ref in project.references
            )
            if not is_budget_ready:
                raise WorkflowExecutionError("STEP-002", "Verify project and budget READY failed")
            return project
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Verify project and budget READY failed") from exc

    def _step_create_accounting_transaction(
        self,
        *,
        project_id: UUID,
        request: ProjectAccountingWorkflowRequest,
    ):
        transaction_reference = (
            request.transaction_reference.strip()
            if request.transaction_reference is not None and request.transaction_reference.strip()
            else None
        )
        journal_reference = (
            f"PROJECT:{project_id}|REF:{transaction_reference}"
            if transaction_reference is not None
            else f"PROJECT:{project_id}"
        )

        try:
            created = self._create_journal.execute(
                CreateJournalRequest(
                    journal_number=request.journal_number,
                    posting_date=request.posting_date,
                    description=request.transaction_description,
                    reference=journal_reference,
                    lines=(
                        JournalLineInput(
                            account_id=request.debit_account_id,
                            side="DEBIT",
                            amount=request.amount,
                            currency=request.currency,
                            description=f"Project {project_id} debit",
                        ),
                        JournalLineInput(
                            account_id=request.credit_account_id,
                            side="CREDIT",
                            amount=request.amount,
                            currency=request.currency,
                            description=f"Project {project_id} credit",
                        ),
                    ),
                )
            )
            return created.journal
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Create accounting transaction failed") from exc

    def _step_validate_fiscal_year_open(self, *, posting_date: date) -> None:
        try:
            fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years
            matched = [
                fiscal_year
                for fiscal_year in fiscal_years
                if fiscal_year.start_date <= posting_date <= fiscal_year.end_date
            ]
            is_open = any(str(item.status).upper() == "OPEN" for item in matched)
            if not is_open:
                raise WorkflowExecutionError("STEP-004", "Validate fiscal year OPEN failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-004", "Validate fiscal year OPEN failed") from exc

    def _step_post_journal_entry(self, *, journal_id: UUID):
        try:
            posted = self._post_journal.execute(PostJournalRequest(journal_id=journal_id))
            return posted.journal
        except Exception as exc:
            raise WorkflowExecutionError("STEP-005", "Post journal entry failed") from exc

    def _step_link_transaction_to_project(
        self,
        *,
        project_id: UUID,
        project_references,
        journal_id: UUID,
        journal_number: str,
    ) -> None:
        now = datetime.now(UTC)
        try:
            self._upsert_project_references(
                project_id=project_id,
                existing_references=project_references,
                additions=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=journal_id,
                        description=f"PROJECT_ACCOUNTING_JOURNAL:{journal_number.strip().upper()}",
                        created_at=now,
                    ),
                ),
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "Link transaction to project failed") from exc

    def _step_verify_accounting_integrity(self, *, project_id: UUID, journal_id: UUID) -> None:
        try:
            journal = self._get_journal.execute(GetJournalRequest(journal_id=journal_id)).journal
            if journal.status != "POSTED":
                raise WorkflowExecutionError("STEP-007", "Accounting integrity verification failed")

            if journal.reference is None or f"PROJECT:{project_id}" not in journal.reference:
                raise WorkflowExecutionError("STEP-007", "Accounting integrity verification failed")

            debit_total = sum(
                line.amount
                for line in journal.lines
                if line.side == "DEBIT"
            )
            credit_total = sum(
                line.amount
                for line in journal.lines
                if line.side == "CREDIT"
            )
            if debit_total != credit_total:
                raise WorkflowExecutionError("STEP-007", "Accounting integrity verification failed")

            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
            linked = any(
                ref.reference_type == "DOCUMENT"
                and ref.external_id == journal_id
                and (ref.description or "").strip().upper().startswith("PROJECT_ACCOUNTING_JOURNAL:")
                for ref in project.references
            )
            if not linked:
                raise WorkflowExecutionError("STEP-007", "Accounting integrity verification failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Verify accounting integrity failed") from exc

    def _upsert_project_references(
        self,
        *,
        project_id: UUID,
        existing_references,
        additions: tuple[ExternalReferenceInput, ...],
    ) -> tuple:
        merged: dict[tuple[str, UUID], ExternalReferenceInput] = {}

        for reference in existing_references:
            key = (
                reference.reference_type.strip().upper(),
                reference.external_id,
            )
            merged[key] = ExternalReferenceInput(
                reference_type=reference.reference_type,
                external_id=reference.external_id,
                description=reference.description,
                created_at=reference.created_at,
                reference_id=reference.reference_id,
            )

        for addition in additions:
            key = (addition.reference_type.strip().upper(), addition.external_id)
            merged[key] = addition

        updated = self._update_project.execute(
            UpdateProjectRequest(
                project_id=project_id,
                references=tuple(merged.values()),
                updated_at=datetime.now(UTC),
            )
        )
        return updated.project.references
