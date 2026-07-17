"""Workflow orchestration for project budget initialization."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import NAMESPACE_URL
from uuid import UUID
from uuid import uuid5

from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import ListLedgerAccountsRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectRequest


@dataclass(frozen=True, slots=True)
class ProjectBudgetInitializationWorkflowRequest:
    project_id: UUID
    fiscal_year: int
    budget_container_name: str = "PROJECT_BUDGET"
    default_budget_categories: tuple[str, ...] = (
        "LABOR",
        "MATERIALS",
        "EQUIPMENT",
        "SERVICES",
        "CONTINGENCY",
    )

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValueError("project_id must be UUID")
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValueError("fiscal_year must be integer >= 2000")
        if not isinstance(self.budget_container_name, str) or not self.budget_container_name.strip():
            raise ValueError("budget_container_name must be a non-empty string")
        if not isinstance(self.default_budget_categories, tuple) or not self.default_budget_categories:
            raise ValueError("default_budget_categories must be a non-empty tuple")

        for index, category in enumerate(self.default_budget_categories):
            if not isinstance(category, str) or not category.strip():
                raise ValueError(
                    f"default_budget_categories[{index}] must be a non-empty string"
                )


@dataclass(frozen=True, slots=True)
class ProjectBudgetInitializationWorkflowResponse:
    project_id: UUID
    budget_container_id: UUID
    budget_category_ids: tuple[UUID, ...]
    fiscal_year_id: UUID
    budget_status: str
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when budget initialization fails at a specific step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class UpdateProjectFeaturePort(Protocol):
    def execute(self, request: UpdateProjectRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class ListLedgerAccountsFeaturePort(Protocol):
    def execute(self, request: ListLedgerAccountsRequest): ...


class ProjectBudgetInitializationWorkflow:
    """Orchestrates project budget setup across Projects and Accounting features."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        update_project_feature: UpdateProjectFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
        list_ledger_accounts_feature: ListLedgerAccountsFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._update_project = update_project_feature
        self._list_fiscal_years = list_fiscal_years_feature
        self._list_ledger_accounts = list_ledger_accounts_feature

    def execute(
        self,
        request: ProjectBudgetInitializationWorkflowRequest,
    ) -> ProjectBudgetInitializationWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        project_id = self._step_select_project(request.project_id)
        completed_steps.append("STEP-001")

        project = self._step_verify_project_exists(project_id)
        completed_steps.append("STEP-002")

        budget_container_id, references = self._step_create_budget_container(
            project_id=project_id,
            existing_references=project.references,
            budget_container_name=request.budget_container_name,
        )
        completed_steps.append("STEP-003")

        budget_category_ids, references = self._step_initialize_default_budget_categories(
            project_id=project_id,
            existing_references=references,
            budget_container_id=budget_container_id,
            categories=request.default_budget_categories,
        )
        completed_steps.append("STEP-004")

        fiscal_year_id, references = self._step_assign_fiscal_year(
            project_id=project_id,
            existing_references=references,
            fiscal_year=request.fiscal_year,
        )
        completed_steps.append("STEP-005")

        self._step_validate_budget_structure(
            project_id=project_id,
            budget_container_id=budget_container_id,
            budget_category_ids=budget_category_ids,
            fiscal_year_id=fiscal_year_id,
        )
        completed_steps.append("STEP-006")

        budget_status = self._step_mark_budget_ready(
            project_id=project_id,
            existing_references=references,
        )
        completed_steps.append("STEP-007")

        return ProjectBudgetInitializationWorkflowResponse(
            project_id=project_id,
            budget_container_id=budget_container_id,
            budget_category_ids=budget_category_ids,
            fiscal_year_id=fiscal_year_id,
            budget_status=budget_status,
            completed_steps=tuple(completed_steps),
        )

    def _step_select_project(self, project_id: UUID) -> UUID:
        try:
            return project_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Select project failed") from exc

    def _step_verify_project_exists(self, project_id: UUID):
        try:
            return self._get_project.execute(GetProjectRequest(project_id=project_id)).project
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Verify project exists failed") from exc

    def _step_create_budget_container(
        self,
        *,
        project_id: UUID,
        existing_references,
        budget_container_name: str,
    ) -> tuple[UUID, tuple]:
        budget_container_id = uuid5(
            NAMESPACE_URL,
            f"{project_id}:PROJECT_BUDGET_CONTAINER:{budget_container_name.strip().upper()}",
        )
        now = datetime.now(UTC)
        try:
            references = self._upsert_project_references(
                project_id=project_id,
                existing_references=existing_references,
                additions=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=budget_container_id,
                        description=f"BUDGET_CONTAINER:{budget_container_name.strip().upper()}",
                        created_at=now,
                    ),
                ),
            )
            return budget_container_id, references
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Create budget container failed") from exc

    def _step_initialize_default_budget_categories(
        self,
        *,
        project_id: UUID,
        existing_references,
        budget_container_id: UUID,
        categories: tuple[str, ...],
    ) -> tuple[tuple[UUID, ...], tuple]:
        now = datetime.now(UTC)
        category_ids = tuple(
            uuid5(
                NAMESPACE_URL,
                f"{budget_container_id}:PROJECT_BUDGET_CATEGORY:{name.strip().upper()}",
            )
            for name in categories
        )

        try:
            references = self._upsert_project_references(
                project_id=project_id,
                existing_references=existing_references,
                additions=tuple(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=category_id,
                        description=f"BUDGET_CATEGORY:{name.strip().upper()}",
                        created_at=now,
                    )
                    for category_id, name in zip(category_ids, categories, strict=True)
                ),
            )
            return category_ids, references
        except Exception as exc:
            raise WorkflowExecutionError(
                "STEP-004",
                "Initialize default budget categories failed",
            ) from exc

    def _step_assign_fiscal_year(
        self,
        *,
        project_id: UUID,
        existing_references,
        fiscal_year: int,
    ) -> tuple[UUID, tuple]:
        now = datetime.now(UTC)
        try:
            fiscal_years = self._list_fiscal_years.execute(
                ListFiscalYearsRequest()
            ).fiscal_years
            matching = [item for item in fiscal_years if item.year == fiscal_year]
            if not matching:
                raise WorkflowExecutionError(
                    "STEP-005",
                    "Assign fiscal year failed",
                )

            selected = next(
                (item for item in matching if str(item.status).upper() == "OPEN"),
                matching[0],
            )

            references = self._upsert_project_references(
                project_id=project_id,
                existing_references=existing_references,
                additions=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=selected.fiscal_year_id,
                        description=f"BUDGET_FISCAL_YEAR:FY{selected.year}",
                        created_at=now,
                    ),
                ),
            )
            return selected.fiscal_year_id, references
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-005", "Assign fiscal year failed") from exc

    def _step_validate_budget_structure(
        self,
        *,
        project_id: UUID,
        budget_container_id: UUID,
        budget_category_ids: tuple[UUID, ...],
        fiscal_year_id: UUID,
    ) -> None:
        try:
            project = self._get_project.execute(
                GetProjectRequest(project_id=project_id)
            ).project

            container_linked = any(
                ref.reference_type == "DOCUMENT"
                and ref.external_id == budget_container_id
                and (ref.description or "").strip().upper().startswith("BUDGET_CONTAINER:")
                for ref in project.references
            )
            if not container_linked:
                raise WorkflowExecutionError(
                    "STEP-006",
                    "Budget structure validation failed",
                )

            category_ids_in_project = {
                ref.external_id
                for ref in project.references
                if ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper().startswith("BUDGET_CATEGORY:")
            }
            if not set(budget_category_ids).issubset(category_ids_in_project):
                raise WorkflowExecutionError(
                    "STEP-006",
                    "Budget structure validation failed",
                )

            fiscal_year_linked = any(
                ref.reference_type == "DOCUMENT"
                and ref.external_id == fiscal_year_id
                and (ref.description or "").strip().upper().startswith("BUDGET_FISCAL_YEAR:")
                for ref in project.references
            )
            if not fiscal_year_linked:
                raise WorkflowExecutionError(
                    "STEP-006",
                    "Budget structure validation failed",
                )

            active_accounts = self._list_ledger_accounts.execute(
                ListLedgerAccountsRequest(active_only=True)
            ).accounts
            if not active_accounts:
                raise WorkflowExecutionError(
                    "STEP-006",
                    "Budget structure validation failed",
                )
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "Validate budget structure failed") from exc

    def _step_mark_budget_ready(self, *, project_id: UUID, existing_references) -> str:
        now = datetime.now(UTC)
        budget_status_id = uuid5(NAMESPACE_URL, f"{project_id}:PROJECT_BUDGET_STATUS:READY")
        try:
            self._upsert_project_references(
                project_id=project_id,
                existing_references=existing_references,
                additions=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=budget_status_id,
                        description="BUDGET_STATUS:READY",
                        created_at=now,
                    ),
                ),
            )
            return "READY"
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Mark budget READY failed") from exc

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
