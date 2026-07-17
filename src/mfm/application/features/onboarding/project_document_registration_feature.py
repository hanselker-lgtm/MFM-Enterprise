"""Feature API entry point for project document registration workflow."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.project_document_registration_workflow import (
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
class ProjectDocumentRegistrationRequest:
    project_id: UUID
    document_number: str
    document_title: str
    initial_document_type: str = "UNCLASSIFIED"
    classification_document_type: str = "PROJECT_DOCUMENT"
    document_description: str | None = None
    created_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.document_number, str) or not self.document_number.strip():
            raise ValidationException("document_number must be a non-empty string")
        if not isinstance(self.document_title, str) or not self.document_title.strip():
            raise ValidationException("document_title must be a non-empty string")
        if not isinstance(self.initial_document_type, str) or not self.initial_document_type.strip():
            raise ValidationException("initial_document_type must be a non-empty string")
        if not isinstance(self.classification_document_type, str) or not self.classification_document_type.strip():
            raise ValidationException("classification_document_type must be a non-empty string")
        if self.document_description is not None and not isinstance(self.document_description, str):
            raise ValidationException("document_description must be string or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValidationException("created_at must be datetime or None")
        if self.created_at is not None and self.created_at.tzinfo is None:
            raise ValidationException("created_at must be timezone-aware")


@dataclass(frozen=True, slots=True)
class ProjectDocumentRegistrationResponse:
    project_id: UUID
    document_id: UUID
    classification_document_type: str
    completed_steps: tuple[str, ...]


class ProjectDocumentRegistrationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ProjectDocumentRegistrationFeature:
    """Feature facade for project document registration orchestration."""

    def __init__(self, *, service: ProjectDocumentRegistrationService) -> None:
        self._service = service

    def execute(self, request: ProjectDocumentRegistrationRequest) -> ProjectDocumentRegistrationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    document_number=request.document_number,
                    document_title=request.document_title,
                    initial_document_type=request.initial_document_type,
                    classification_document_type=request.classification_document_type,
                    document_description=request.document_description,
                    created_at=request.created_at,
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Project document registration feature failed") from exc

        return ProjectDocumentRegistrationResponse(
            project_id=service_response.project_id,
            document_id=service_response.document_id,
            classification_document_type=service_response.classification_document_type,
            completed_steps=service_response.completed_steps,
        )
