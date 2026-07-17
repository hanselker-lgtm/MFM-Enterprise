"""Workflow orchestration for project document registration."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.documents import AttachReferenceRequest
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import GetDocumentRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.documents import UpdateDocumentMetadataRequest
from mfm.application.features.projects import GetProjectRequest


@dataclass(frozen=True, slots=True)
class ProjectDocumentRegistrationWorkflowRequest:
    project_id: UUID
    document_number: str
    document_title: str
    initial_document_type: str = "UNCLASSIFIED"
    classification_document_type: str = "PROJECT_DOCUMENT"
    document_description: str | None = None
    created_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValueError("project_id must be UUID")
        if not isinstance(self.document_number, str) or not self.document_number.strip():
            raise ValueError("document_number must be a non-empty string")
        if not isinstance(self.document_title, str) or not self.document_title.strip():
            raise ValueError("document_title must be a non-empty string")
        if not isinstance(self.initial_document_type, str) or not self.initial_document_type.strip():
            raise ValueError("initial_document_type must be a non-empty string")
        if not isinstance(self.classification_document_type, str) or not self.classification_document_type.strip():
            raise ValueError("classification_document_type must be a non-empty string")
        if self.document_description is not None and not isinstance(self.document_description, str):
            raise ValueError("document_description must be string or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValueError("created_at must be datetime or None")
        if self.created_at is not None and self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware")


@dataclass(frozen=True, slots=True)
class ProjectDocumentRegistrationWorkflowResponse:
    project_id: UUID
    document_id: UUID
    classification_document_type: str
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when document registration fails at a specific step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class CreateDocumentFeaturePort(Protocol):
    def execute(self, request: CreateDocumentRequest): ...


class AttachReferenceFeaturePort(Protocol):
    def execute(self, request: AttachReferenceRequest): ...


class UpdateDocumentMetadataFeaturePort(Protocol):
    def execute(self, request: UpdateDocumentMetadataRequest): ...


class GetDocumentFeaturePort(Protocol):
    def execute(self, request: GetDocumentRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class ProjectDocumentRegistrationWorkflow:
    """Orchestrates project document registration across Projects and Documents features."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        create_document_feature: CreateDocumentFeaturePort,
        attach_reference_feature: AttachReferenceFeaturePort,
        update_document_metadata_feature: UpdateDocumentMetadataFeaturePort,
        get_document_feature: GetDocumentFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._create_document = create_document_feature
        self._attach_reference = attach_reference_feature
        self._update_document_metadata = update_document_metadata_feature
        self._get_document = get_document_feature
        self._list_documents = list_documents_feature

    def execute(
        self,
        request: ProjectDocumentRegistrationWorkflowRequest,
    ) -> ProjectDocumentRegistrationWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        project_id = self._step_select_project(request.project_id)
        completed_steps.append("STEP-001")

        self._step_verify_project_exists(project_id)
        completed_steps.append("STEP-002")

        document_id = self._step_create_document_metadata(project_id=project_id, request=request)
        completed_steps.append("STEP-003")

        self._step_attach_document_to_project(project_id=project_id, document_id=document_id)
        completed_steps.append("STEP-004")

        self._step_register_document_classification(
            document_id=document_id,
            classification_document_type=request.classification_document_type,
            document_title=request.document_title,
            document_description=request.document_description,
        )
        completed_steps.append("STEP-005")

        self._step_verify_document_linkage(project_id=project_id, document_id=document_id)
        completed_steps.append("STEP-006")

        self._step_confirm_document_availability(document_id=document_id)
        completed_steps.append("STEP-007")

        return ProjectDocumentRegistrationWorkflowResponse(
            project_id=project_id,
            document_id=document_id,
            classification_document_type=request.classification_document_type.strip().upper(),
            completed_steps=tuple(completed_steps),
        )

    def _step_select_project(self, project_id: UUID) -> UUID:
        try:
            return project_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Select project failed") from exc

    def _step_verify_project_exists(self, project_id: UUID) -> None:
        try:
            self._get_project.execute(GetProjectRequest(project_id=project_id))
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Verify project exists failed") from exc

    def _step_create_document_metadata(
        self,
        *,
        project_id: UUID,
        request: ProjectDocumentRegistrationWorkflowRequest,
    ) -> UUID:
        now = request.created_at or datetime.now(UTC)
        try:
            created = self._create_document.execute(
                CreateDocumentRequest(
                    document_number=request.document_number,
                    document_title=request.document_title,
                    document_type=request.initial_document_type,
                    status="ACTIVE",
                    description=request.document_description,
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=f"projects/{project_id}/documents/{request.document_number.strip().upper()}/v1",
                            file_name=f"{request.document_number.strip().upper()}.txt",
                            mime_type="text/plain",
                            checksum="project-document-initial-version",
                            size_bytes=0,
                            created_at=now,
                        ),
                    ),
                )
            )
            return created.document.document_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Create document metadata failed") from exc

    def _step_attach_document_to_project(self, *, project_id: UUID, document_id: UUID) -> None:
        now = datetime.now(UTC)
        try:
            self._attach_reference.execute(
                AttachReferenceRequest(
                    document_id=document_id,
                    reference=DocumentReferenceInput(
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=now,
                        description="Project document linkage",
                    ),
                    attached_at=now,
                )
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-004", "Attach document to project failed") from exc

    def _step_register_document_classification(
        self,
        *,
        document_id: UUID,
        classification_document_type: str,
        document_title: str,
        document_description: str | None,
    ) -> None:
        try:
            self._update_document_metadata.execute(
                UpdateDocumentMetadataRequest(
                    document_id=document_id,
                    document_title=document_title,
                    document_type=classification_document_type,
                    description=document_description,
                    updated_at=datetime.now(UTC),
                )
            )
        except Exception as exc:
            raise WorkflowExecutionError("STEP-005", "Register document classification failed") from exc

    def _step_verify_document_linkage(self, *, project_id: UUID, document_id: UUID) -> None:
        try:
            document = self._get_document.execute(
                GetDocumentRequest(document_id=document_id)
            ).document

            linked = any(
                ref.target_capability == "PROJECTS"
                and ref.target_aggregate_type == "PROJECT"
                and ref.target_aggregate_id == str(project_id)
                for ref in document.references
            )
            if not linked:
                raise WorkflowExecutionError("STEP-006", "Document linkage verification failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "Verify document linkage failed") from exc

    def _step_confirm_document_availability(self, *, document_id: UUID) -> None:
        try:
            active_documents = self._list_documents.execute(ListDocumentsRequest(status="ACTIVE"))
            if all(item.document_id != document_id for item in active_documents.documents):
                raise WorkflowExecutionError("STEP-007", "Document availability confirmation failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Confirm document availability failed") from exc
