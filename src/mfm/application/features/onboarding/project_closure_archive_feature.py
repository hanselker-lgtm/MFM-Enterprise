"""Feature API entry point for project closure and archive workflow."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflowRequest as ServiceRequest,
)
from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflowResponse as ServiceResponse,
)
from mfm.application.workflows.project_closure_archive_workflow import WorkflowExecutionError


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when workflow business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ProjectClosureArchiveRequest:
    project_id: UUID
    archive_manifest_number: str | None = None
    archive_manifest_title: str = "Project Archive Manifest"
    archived_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if self.archive_manifest_number is not None and (
            not isinstance(self.archive_manifest_number, str)
            or not self.archive_manifest_number.strip()
        ):
            raise ValidationException("archive_manifest_number must be a non-empty string when provided")
        if not isinstance(self.archive_manifest_title, str) or not self.archive_manifest_title.strip():
            raise ValidationException("archive_manifest_title must be a non-empty string")
        if self.archived_at is not None and not isinstance(self.archived_at, datetime):
            raise ValidationException("archived_at must be datetime or None")
        if self.archived_at is not None and self.archived_at.tzinfo is None:
            raise ValidationException("archived_at must be timezone-aware")


@dataclass(frozen=True, slots=True)
class ProjectClosureArchiveResponse:
    project_id: UUID
    archive_manifest_id: UUID
    project_status: str
    closure_status: str
    completed_steps: tuple[str, ...]


class ProjectClosureArchiveService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ProjectClosureArchiveFeature:
    """Feature facade for project closure and archive orchestration."""

    def __init__(self, *, service: ProjectClosureArchiveService) -> None:
        self._service = service

    def execute(self, request: ProjectClosureArchiveRequest) -> ProjectClosureArchiveResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    archive_manifest_number=request.archive_manifest_number,
                    archive_manifest_title=request.archive_manifest_title,
                    archived_at=request.archived_at,
                )
            )
        except WorkflowExecutionError as exc:
            raise BusinessRuleViolation(f"{exc.step}: {exc}") from exc
        except ValueError as exc:
            raise ValidationException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Project closure and archive feature failed") from exc

        return ProjectClosureArchiveResponse(
            project_id=service_response.project_id,
            archive_manifest_id=service_response.archive_manifest_id,
            project_status=service_response.project_status,
            closure_status=service_response.closure_status,
            completed_steps=service_response.completed_steps,
        )
