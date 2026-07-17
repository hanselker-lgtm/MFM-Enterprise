"""Workflow orchestration for complete project creation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.organization import UpdateOrganizationRequest
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import ProjectAssignmentInput
from mfm.application.features.projects import UpdateProjectRequest
from mfm.domain.organization.organization_status import OrganizationStatus


@dataclass(frozen=True, slots=True)
class CompleteProjectCreationWorkflowRequest:
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
            raise ValueError("organization_id must be UUID")
        if not isinstance(self.organization_owner_contact_id, UUID):
            raise ValueError("organization_owner_contact_id must be UUID")
        if not isinstance(self.project_number, str) or not self.project_number.strip():
            raise ValueError("project_number must be a non-empty string")
        if not isinstance(self.project_name, str) or not self.project_name.strip():
            raise ValueError("project_name must be a non-empty string")
        if not isinstance(self.project_priority, str) or not self.project_priority.strip():
            raise ValueError("project_priority must be a non-empty string")
        if self.project_description is not None and not isinstance(self.project_description, str):
            raise ValueError("project_description must be string or None")
        if self.project_start_date is not None and not isinstance(self.project_start_date, datetime):
            raise ValueError("project_start_date must be datetime or None")
        if self.project_end_date is not None and not isinstance(self.project_end_date, datetime):
            raise ValueError("project_end_date must be datetime or None")
        if self.project_created_at is not None and not isinstance(self.project_created_at, datetime):
            raise ValueError("project_created_at must be datetime or None")
        if self.project_start_date is not None and self.project_start_date.tzinfo is None:
            raise ValueError("project_start_date must be timezone-aware")
        if self.project_end_date is not None and self.project_end_date.tzinfo is None:
            raise ValueError("project_end_date must be timezone-aware")
        if self.project_created_at is not None and self.project_created_at.tzinfo is None:
            raise ValueError("project_created_at must be timezone-aware")
        if self.document_library_number is not None and (
            not isinstance(self.document_library_number, str)
            or not self.document_library_number.strip()
        ):
            raise ValueError("document_library_number must be a non-empty string when provided")
        if not isinstance(self.document_library_title, str) or not self.document_library_title.strip():
            raise ValueError("document_library_title must be a non-empty string")
        if self.budget_container_number is not None and (
            not isinstance(self.budget_container_number, str)
            or not self.budget_container_number.strip()
        ):
            raise ValueError("budget_container_number must be a non-empty string when provided")
        if not isinstance(self.budget_container_title, str) or not self.budget_container_title.strip():
            raise ValueError("budget_container_title must be a non-empty string")


@dataclass(frozen=True, slots=True)
class CompleteProjectCreationWorkflowResponse:
    project_id: UUID
    project_status: str
    organization_id: UUID
    project_document_library_id: UUID
    project_budget_container_id: UUID
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when project creation onboarding fails at a specific step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class UpdateOrganizationFeaturePort(Protocol):
    def execute(self, request: UpdateOrganizationRequest): ...


class CreateProjectFeaturePort(Protocol):
    def execute(self, request: CreateProjectRequest): ...


class UpdateProjectFeaturePort(Protocol):
    def execute(self, request: UpdateProjectRequest): ...


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class CreateDocumentFeaturePort(Protocol):
    def execute(self, request: CreateDocumentRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class CompleteProjectCreationWorkflow:
    """Orchestrates a complete project creation flow across locked feature APIs."""

    def __init__(
        self,
        *,
        update_organization_feature: UpdateOrganizationFeaturePort,
        create_project_feature: CreateProjectFeaturePort,
        update_project_feature: UpdateProjectFeaturePort,
        get_project_feature: GetProjectFeaturePort,
        create_document_feature: CreateDocumentFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
    ) -> None:
        self._update_organization = update_organization_feature
        self._create_project = create_project_feature
        self._update_project = update_project_feature
        self._get_project = get_project_feature
        self._create_document = create_document_feature
        self._list_documents = list_documents_feature

    def execute(
        self,
        request: CompleteProjectCreationWorkflowRequest,
    ) -> CompleteProjectCreationWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        project_id = self._step_create_project(request)
        completed_steps.append("STEP-001")

        self._step_assign_organization_ownership(
            project_id=project_id,
            organization_id=request.organization_id,
            owner_contact_id=request.organization_owner_contact_id,
        )
        completed_steps.append("STEP-002")

        project_document_library_id = self._step_create_project_document_library(
            project_id=project_id,
            request=request,
        )
        completed_steps.append("STEP-003")

        project_budget_container_id = self._step_initialize_project_budget_container(
            project_id=project_id,
            request=request,
        )
        completed_steps.append("STEP-004")

        self._step_register_project_metadata(
            project_id=project_id,
            organization_id=request.organization_id,
            project_document_library_id=project_document_library_id,
            project_budget_container_id=project_budget_container_id,
            project_description=request.project_description,
        )
        completed_steps.append("STEP-005")

        self._step_run_project_verification(
            project_id=project_id,
            organization_id=request.organization_id,
            project_document_library_id=project_document_library_id,
            project_budget_container_id=project_budget_container_id,
        )
        completed_steps.append("STEP-006")

        project_status = self._step_mark_project_active(project_id)
        completed_steps.append("STEP-007")

        return CompleteProjectCreationWorkflowResponse(
            project_id=project_id,
            project_status=project_status,
            organization_id=request.organization_id,
            project_document_library_id=project_document_library_id,
            project_budget_container_id=project_budget_container_id,
            completed_steps=tuple(completed_steps),
        )

    def _step_create_project(self, request: CompleteProjectCreationWorkflowRequest) -> UUID:
        try:
            created = self._create_project.execute(
                CreateProjectRequest(
                    project_number=request.project_number,
                    project_name=request.project_name,
                    status="ACTIVE",
                    priority=request.project_priority,
                    description=request.project_description,
                    start_date=request.project_start_date,
                    end_date=request.project_end_date,
                    created_at=request.project_created_at,
                )
            )
            return created.project.project_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Create project failed") from exc

    def _step_assign_organization_ownership(
        self,
        *,
        project_id: UUID,
        organization_id: UUID,
        owner_contact_id: UUID,
    ) -> None:
        try:
            # Ensure organization is resolvable through its feature API boundary.
            self._update_organization.execute(
                UpdateOrganizationRequest(
                    organization_id=organization_id,
                    status=OrganizationStatus.ACTIVE,
                )
            )

            self._update_project.execute(
                UpdateProjectRequest(
                    project_id=project_id,
                    assignments=(
                        ProjectAssignmentInput(
                            organisation_id=organization_id,
                            contact_id=owner_contact_id,
                            role="OWNER",
                        ),
                    ),
                    updated_at=datetime.now(UTC),
                )
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Assign organization ownership failed") from exc

    def _step_create_project_document_library(
        self,
        *,
        project_id: UUID,
        request: CompleteProjectCreationWorkflowRequest,
    ) -> UUID:
        number = request.document_library_number or f"PRJ-LIB-{request.project_number.strip().upper()}"
        now = datetime.now(UTC)

        try:
            created = self._create_document.execute(
                CreateDocumentRequest(
                    document_number=number,
                    document_title=request.document_library_title,
                    document_type="PROJECT_LIBRARY",
                    status="ACTIVE",
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=f"projects/{project_id}/library/v1",
                            file_name="project-library-index.txt",
                            mime_type="text/plain",
                            checksum="project-library-initial-version",
                            size_bytes=0,
                            created_at=now,
                        ),
                    ),
                    references=(
                        DocumentReferenceInput(
                            target_capability="PROJECTS",
                            target_aggregate_type="PROJECT",
                            target_aggregate_id=str(project_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Project document library",
                        ),
                    ),
                )
            )
            return created.document.document_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Create project document library failed") from exc

    def _step_initialize_project_budget_container(
        self,
        *,
        project_id: UUID,
        request: CompleteProjectCreationWorkflowRequest,
    ) -> UUID:
        number = request.budget_container_number or f"PRJ-BUD-{request.project_number.strip().upper()}"
        now = datetime.now(UTC)

        try:
            created = self._create_document.execute(
                CreateDocumentRequest(
                    document_number=number,
                    document_title=request.budget_container_title,
                    document_type="PROJECT_BUDGET_CONTAINER",
                    status="ACTIVE",
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=f"projects/{project_id}/budget/v1",
                            file_name="project-budget-container.json",
                            mime_type="application/json",
                            checksum="project-budget-initial-version",
                            size_bytes=2,
                            created_at=now,
                        ),
                    ),
                    references=(
                        DocumentReferenceInput(
                            target_capability="PROJECTS",
                            target_aggregate_type="PROJECT",
                            target_aggregate_id=str(project_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Project budget container",
                        ),
                    ),
                )
            )
            return created.document.document_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-004", "Initialize project budget container failed") from exc

    def _step_register_project_metadata(
        self,
        *,
        project_id: UUID,
        organization_id: UUID,
        project_document_library_id: UUID,
        project_budget_container_id: UUID,
        project_description: str | None,
    ) -> None:
        try:
            self._update_project.execute(
                UpdateProjectRequest(
                    project_id=project_id,
                    description=project_description,
                    references=(
                        ExternalReferenceInput(
                            reference_type="ORGANISATION",
                            external_id=organization_id,
                            description="Owning organization",
                            created_at=datetime.now(UTC),
                        ),
                        ExternalReferenceInput(
                            reference_type="DOCUMENT",
                            external_id=project_document_library_id,
                            description="Project document library",
                            created_at=datetime.now(UTC),
                        ),
                        ExternalReferenceInput(
                            reference_type="DOCUMENT",
                            external_id=project_budget_container_id,
                            description="Project budget container",
                            created_at=datetime.now(UTC),
                        ),
                    ),
                    updated_at=datetime.now(UTC),
                )
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-005", "Register project metadata failed") from exc

    def _step_run_project_verification(
        self,
        *,
        project_id: UUID,
        organization_id: UUID,
        project_document_library_id: UUID,
        project_budget_container_id: UUID,
    ) -> None:
        try:
            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project

            if all(assignment.organisation_id != organization_id for assignment in project.assignments):
                raise WorkflowExecutionError("STEP-006", "Ownership verification failed")

            ref_pairs = {(item.reference_type, item.external_id) for item in project.references}
            required_refs = {
                ("ORGANISATION", organization_id),
                ("DOCUMENT", project_document_library_id),
                ("DOCUMENT", project_budget_container_id),
            }
            if not required_refs.issubset(ref_pairs):
                raise WorkflowExecutionError("STEP-006", "Metadata reference verification failed")

            documents = self._list_documents.execute(ListDocumentsRequest(status="ACTIVE"))
            doc_ids = {item.document_id for item in documents.documents}
            if project_document_library_id not in doc_ids:
                raise WorkflowExecutionError("STEP-006", "Project document library verification failed")
            if project_budget_container_id not in doc_ids:
                raise WorkflowExecutionError("STEP-006", "Project budget container verification failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "Project verification failed") from exc

    def _step_mark_project_active(self, project_id: UUID) -> str:
        try:
            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
            if project.status != "ACTIVE":
                raise WorkflowExecutionError("STEP-007", "Project is not ACTIVE")
            return project.status
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Mark project ACTIVE failed") from exc
