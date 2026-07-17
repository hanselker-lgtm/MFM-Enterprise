"""Feature API entry point for project budget initialization workflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.project_budget_initialization_workflow import (
    WorkflowExecutionError,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when workflow business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ProjectBudgetInitializationRequest:
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
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.fiscal_year, int) or self.fiscal_year < 2000:
            raise ValidationException("fiscal_year must be integer >= 2000")
        if not isinstance(self.budget_container_name, str) or not self.budget_container_name.strip():
            raise ValidationException("budget_container_name must be a non-empty string")
        if not isinstance(self.default_budget_categories, tuple) or not self.default_budget_categories:
            raise ValidationException("default_budget_categories must be a non-empty tuple")

        for index, category in enumerate(self.default_budget_categories):
            if not isinstance(category, str) or not category.strip():
                raise ValidationException(
                    f"default_budget_categories[{index}] must be a non-empty string"
                )


@dataclass(frozen=True, slots=True)
class ProjectBudgetInitializationResponse:
    project_id: UUID
    budget_container_id: UUID
    budget_category_ids: tuple[UUID, ...]
    fiscal_year_id: UUID
    budget_status: str
    completed_steps: tuple[str, ...]


class ProjectBudgetInitializationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ProjectBudgetInitializationFeature:
    """Feature facade for project budget initialization orchestration."""

    def __init__(self, *, service: ProjectBudgetInitializationService) -> None:
        self._service = service

    def execute(self, request: ProjectBudgetInitializationRequest) -> ProjectBudgetInitializationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    fiscal_year=request.fiscal_year,
                    budget_container_name=request.budget_container_name,
                    default_budget_categories=request.default_budget_categories,
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Project budget initialization feature failed") from exc

        return ProjectBudgetInitializationResponse(
            project_id=service_response.project_id,
            budget_container_id=service_response.budget_container_id,
            budget_category_ids=service_response.budget_category_ids,
            fiscal_year_id=service_response.fiscal_year_id,
            budget_status=service_response.budget_status,
            completed_steps=service_response.completed_steps,
        )
