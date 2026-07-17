"""Workflow orchestration for complete organization onboarding."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from datetime import date
from calendar import monthrange
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateLedgerAccountRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import ListLedgerAccountsRequest
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.organization import CreateOrganizationRequest
from mfm.application.features.organization import UpdateOrganizationRequest
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@dataclass(frozen=True, slots=True)
class DefaultLedgerAccountInput:
    account_number: str
    name: str
    account_type: str
    normal_balance: str


@dataclass(frozen=True, slots=True)
class CompleteOrganizationOnboardingWorkflowRequest:
    organization_number: str
    organization_name: str
    organization_type: OrganizationType
    fiscal_year: int
    document_library_number: str | None = None
    document_library_title: str = "Default Organization Library"
    chart_of_accounts: tuple[DefaultLedgerAccountInput, ...] = (
        DefaultLedgerAccountInput(
            account_number="1000-CASH",
            name="Cash",
            account_type="ASSET",
            normal_balance="DEBIT",
        ),
        DefaultLedgerAccountInput(
            account_number="1100-AR",
            name="Accounts Receivable",
            account_type="ASSET",
            normal_balance="DEBIT",
        ),
        DefaultLedgerAccountInput(
            account_number="2000-AP",
            name="Accounts Payable",
            account_type="LIABILITY",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="3000-EQUITY",
            name="Retained Earnings",
            account_type="EQUITY",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="4000-REV",
            name="Operating Revenue",
            account_type="INCOME",
            normal_balance="CREDIT",
        ),
        DefaultLedgerAccountInput(
            account_number="5000-EXP",
            name="Operating Expense",
            account_type="EXPENSE",
            normal_balance="DEBIT",
        ),
    )

    def validate(self) -> None:
        if not isinstance(self.organization_number, str) or not self.organization_number.strip():
            raise ValueError("organization_number must be a non-empty string")
        if not isinstance(self.organization_name, str) or not self.organization_name.strip():
            raise ValueError("organization_name must be a non-empty string")
        if not isinstance(self.organization_type, OrganizationType):
            raise ValueError("organization_type must be OrganizationType")
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValueError("fiscal_year must be integer >= 2000")
        if self.document_library_number is not None and (
            not isinstance(self.document_library_number, str)
            or not self.document_library_number.strip()
        ):
            raise ValueError("document_library_number must be a non-empty string when provided")
        if not isinstance(self.document_library_title, str) or not self.document_library_title.strip():
            raise ValueError("document_library_title must be a non-empty string")
        if not isinstance(self.chart_of_accounts, tuple) or not self.chart_of_accounts:
            raise ValueError("chart_of_accounts must be a non-empty tuple")


@dataclass(frozen=True, slots=True)
class CompleteOrganizationOnboardingWorkflowResponse:
    organization_id: UUID
    organization_status: str
    document_library_id: UUID
    fiscal_year_id: UUID
    ledger_account_ids: tuple[UUID, ...]
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when onboarding fails at a specific workflow step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class CreateOrganizationFeaturePort(Protocol):
    def execute(self, request: CreateOrganizationRequest): ...


class UpdateOrganizationFeaturePort(Protocol):
    def execute(self, request: UpdateOrganizationRequest): ...


class CreateDocumentFeaturePort(Protocol):
    def execute(self, request: CreateDocumentRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class CreateFiscalYearFeaturePort(Protocol):
    def execute(self, request: CreateFiscalYearRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class CreateLedgerAccountFeaturePort(Protocol):
    def execute(self, request: CreateLedgerAccountRequest): ...


class ListLedgerAccountsFeaturePort(Protocol):
    def execute(self, request: ListLedgerAccountsRequest): ...


class CompleteOrganizationOnboardingWorkflow:
    """Orchestrates a full onboarding flow by composing locked capability feature APIs."""

    def __init__(
        self,
        *,
        create_organization_feature: CreateOrganizationFeaturePort,
        update_organization_feature: UpdateOrganizationFeaturePort,
        create_document_feature: CreateDocumentFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
        create_fiscal_year_feature: CreateFiscalYearFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
        create_ledger_account_feature: CreateLedgerAccountFeaturePort,
        list_ledger_accounts_feature: ListLedgerAccountsFeaturePort,
    ) -> None:
        self._create_organization = create_organization_feature
        self._update_organization = update_organization_feature
        self._create_document = create_document_feature
        self._list_documents = list_documents_feature
        self._create_fiscal_year = create_fiscal_year_feature
        self._list_fiscal_years = list_fiscal_years_feature
        self._create_ledger_account = create_ledger_account_feature
        self._list_ledger_accounts = list_ledger_accounts_feature

    def execute(
        self,
        request: CompleteOrganizationOnboardingWorkflowRequest,
    ) -> CompleteOrganizationOnboardingWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        organization_id = self._step_create_organization(request)
        completed_steps.append("STEP-001")

        self._step_initialize_defaults(organization_id)
        completed_steps.append("STEP-002")

        document_library_id = self._step_create_default_document_library(
            organization_id=organization_id,
            request=request,
        )
        completed_steps.append("STEP-003")

        fiscal_year_id = self._step_create_first_fiscal_year(request.fiscal_year)
        completed_steps.append("STEP-004")

        ledger_account_ids = self._step_create_default_chart_of_accounts(request.chart_of_accounts)
        completed_steps.append("STEP-005")

        self._step_run_system_verification(
            fiscal_year=request.fiscal_year,
            document_library_id=document_library_id,
            ledger_account_ids=ledger_account_ids,
        )
        completed_steps.append("STEP-006")

        organization_status = self._step_mark_organization_active(organization_id)
        completed_steps.append("STEP-007")

        return CompleteOrganizationOnboardingWorkflowResponse(
            organization_id=organization_id,
            organization_status=organization_status,
            document_library_id=document_library_id,
            fiscal_year_id=fiscal_year_id,
            ledger_account_ids=ledger_account_ids,
            completed_steps=tuple(completed_steps),
        )

    def _step_create_organization(
        self,
        request: CompleteOrganizationOnboardingWorkflowRequest,
    ) -> UUID:
        try:
            created = self._create_organization.execute(
                CreateOrganizationRequest(
                    organization_number=request.organization_number,
                    name=request.organization_name,
                    organization_type=request.organization_type,
                )
            )
            return created.organization_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Create organization failed") from exc

    def _step_initialize_defaults(self, organization_id: UUID) -> None:
        try:
            self._update_organization.execute(
                UpdateOrganizationRequest(
                    organization_id=organization_id,
                    status=OrganizationStatus.INACTIVE,
                )
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Initialize organization defaults failed") from exc

    def _step_create_default_document_library(
        self,
        *,
        organization_id: UUID,
        request: CompleteOrganizationOnboardingWorkflowRequest,
    ) -> UUID:
        library_number = request.document_library_number or f"LIB-{request.organization_number.strip().upper()}"
        now = datetime.now(UTC)
        try:
            created = self._create_document.execute(
                CreateDocumentRequest(
                    document_number=library_number,
                    document_title=request.document_library_title,
                    document_type="LIBRARY",
                    status="ACTIVE",
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=f"onboarding/{library_number}/v1",
                            file_name="library-index.txt",
                            mime_type="text/plain",
                            checksum="onboarding-initial-version",
                            size_bytes=0,
                            created_at=now,
                        ),
                    ),
                    references=(
                        DocumentReferenceInput(
                            target_capability="ORGANIZATION",
                            target_aggregate_type="ORGANIZATION",
                            target_aggregate_id=str(organization_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Default organization document library",
                        ),
                    ),
                )
            )
            return created.document.document_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Create default document library failed") from exc

    def _step_create_first_fiscal_year(self, fiscal_year: int) -> UUID:
        start_date = date(fiscal_year, 1, 1)
        end_date = date(fiscal_year, 12, 31)
        periods: list[FiscalPeriodInput] = []

        for month in range(1, 13):
            month_end_day = monthrange(fiscal_year, month)[1]
            periods.append(
                FiscalPeriodInput(
                    number=month,
                    start_date=date(fiscal_year, month, 1),
                    end_date=date(fiscal_year, month, month_end_day),
                    closed=False,
                )
            )

        try:
            created = self._create_fiscal_year.execute(
                CreateFiscalYearRequest(
                    year=fiscal_year,
                    start_date=start_date,
                    end_date=end_date,
                    periods=tuple(periods),
                    status="OPEN",
                )
            )
            return created.fiscal_year.fiscal_year_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-004", "Create first fiscal year failed") from exc

    def _step_create_default_chart_of_accounts(
        self,
        chart_of_accounts: tuple[DefaultLedgerAccountInput, ...],
    ) -> tuple[UUID, ...]:
        created_account_ids: list[UUID] = []
        try:
            for account in chart_of_accounts:
                created = self._create_ledger_account.execute(
                    CreateLedgerAccountRequest(
                        account_number=account.account_number,
                        name=account.name,
                        account_type=account.account_type,
                        normal_balance=account.normal_balance,
                    )
                )
                created_account_ids.append(created.account.account_id)
        except Exception as exc:
            raise WorkflowExecutionError("STEP-005", "Create default chart of accounts failed") from exc

        return tuple(created_account_ids)

    def _step_run_system_verification(
        self,
        *,
        fiscal_year: int,
        document_library_id: UUID,
        ledger_account_ids: tuple[UUID, ...],
    ) -> None:
        try:
            documents = self._list_documents.execute(ListDocumentsRequest(status="ACTIVE"))
            if all(item.document_id != document_library_id for item in documents.documents):
                raise WorkflowExecutionError("STEP-006", "Document library verification failed")

            fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest())
            if all(item.year != fiscal_year for item in fiscal_years.fiscal_years):
                raise WorkflowExecutionError("STEP-006", "Fiscal year verification failed")

            accounts = self._list_ledger_accounts.execute(ListLedgerAccountsRequest(active_only=True))
            account_ids = {item.account_id for item in accounts.accounts}
            if any(account_id not in account_ids for account_id in ledger_account_ids):
                raise WorkflowExecutionError("STEP-006", "Ledger account verification failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "System verification failed") from exc

    def _step_mark_organization_active(self, organization_id: UUID) -> str:
        try:
            updated = self._update_organization.execute(
                UpdateOrganizationRequest(
                    organization_id=organization_id,
                    status=OrganizationStatus.ACTIVE,
                )
            )
            return updated.status
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Mark organization ACTIVE failed") from exc
