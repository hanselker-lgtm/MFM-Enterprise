"""Feature API entry point for complete project creation workflow."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.complete_project_creation_workflow import (
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
class CompleteProjectCreationRequest:
    organization_id: UUID
    organization_owner_contact_id: UUID
    project_number: str
    project_name: str
    project_priority: str = "NORMAL"
    project_description: str | None = None
    project_start_date: datetime | None = None
    project_end_date: datetime | None = None
    project_created_at: datetime | None = None
    document_library_number: str | None = None
    document_library_title: str = "Default Project Library"
    budget_container_number: str | None = None
    budget_container_title: str = "Project Budget Container"

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.organization_owner_contact_id, UUID):
            raise ValidationException("organization_owner_contact_id must be UUID")
        if not isinstance(self.project_number, str) or not self.project_number.strip():
            raise ValidationException("project_number must be a non-empty string")
        if not isinstance(self.project_name, str) or not self.project_name.strip():
            raise ValidationException("project_name must be a non-empty string")
        if not isinstance(self.project_priority, str) or not self.project_priority.strip():
            raise ValidationException("project_priority must be a non-empty string")
        if self.project_description is not None and not isinstance(self.project_description, str):
            raise ValidationException("project_description must be string or None")
        for field_name, value in (
            ("project_start_date", self.project_start_date),
            ("project_end_date", self.project_end_date),
            ("project_created_at", self.project_created_at),
        ):
            if value is not None and not isinstance(value, datetime):
                raise ValidationException(f"{field_name} must be datetime or None")
            if value is not None and value.tzinfo is None:
                raise ValidationException(f"{field_name} must be timezone-aware")
        if self.document_library_number is not None and (
            not isinstance(self.document_library_number, str)
            or not self.document_library_number.strip()
        ):
            raise ValidationException("document_library_number must be a non-empty string when provided")
        if not isinstance(self.document_library_title, str) or not self.document_library_title.strip():
            raise ValidationException("document_library_title must be a non-empty string")
        if self.budget_container_number is not None and (
            not isinstance(self.budget_container_number, str)
            or not self.budget_container_number.strip()
        ):
            raise ValidationException("budget_container_number must be a non-empty string when provided")
        if not isinstance(self.budget_container_title, str) or not self.budget_container_title.strip():
            raise ValidationException("budget_container_title must be a non-empty string")


@dataclass(frozen=True, slots=True)
class CompleteProjectCreationResponse:
    project_id: UUID
    project_status: str
    organization_id: UUID
    project_document_library_id: UUID
    project_budget_container_id: UUID
    completed_steps: tuple[str, ...]


class CompleteProjectCreationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CompleteProjectCreationFeature:
    """Feature facade for complete project creation orchestration."""

    def __init__(self, *, service: CompleteProjectCreationService) -> None:
        self._service = service

    def execute(self, request: CompleteProjectCreationRequest) -> CompleteProjectCreationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    organization_owner_contact_id=request.organization_owner_contact_id,
                    project_number=request.project_number,
                    project_name=request.project_name,
                    project_priority=request.project_priority,
                    project_description=request.project_description,
                    project_start_date=request.project_start_date,
                    project_end_date=request.project_end_date,
                    project_created_at=request.project_created_at,
                    document_library_number=request.document_library_number,
                    document_library_title=request.document_library_title,
                    budget_container_number=request.budget_container_number,
                    budget_container_title=request.budget_container_title,
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete project creation feature failed") from exc

        return CompleteProjectCreationResponse(
            project_id=service_response.project_id,
            project_status=service_response.project_status,
            organization_id=service_response.organization_id,
            project_document_library_id=service_response.project_document_library_id,
            project_budget_container_id=service_response.project_budget_container_id,
            completed_steps=service_response.completed_steps,
        )
