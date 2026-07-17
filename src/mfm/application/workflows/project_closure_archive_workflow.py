"""Workflow orchestration for project closure and archive."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import NAMESPACE_URL
from uuid import UUID
from uuid import uuid5

from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.projects import ArchiveProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectRequest


@dataclass(frozen=True, slots=True)
class ProjectClosureArchiveWorkflowRequest:
    project_id: UUID
    archive_manifest_number: str | None = None
    archive_manifest_title: str = "Project Archive Manifest"
    archived_at: datetime | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValueError("project_id must be UUID")
        if self.archive_manifest_number is not None and (
            not isinstance(self.archive_manifest_number, str)
            or not self.archive_manifest_number.strip()
        ):
            raise ValueError("archive_manifest_number must be a non-empty string when provided")
        if not isinstance(self.archive_manifest_title, str) or not self.archive_manifest_title.strip():
            raise ValueError("archive_manifest_title must be a non-empty string")
        if self.archived_at is not None and not isinstance(self.archived_at, datetime):
            raise ValueError("archived_at must be datetime or None")
        if self.archived_at is not None and self.archived_at.tzinfo is None:
            raise ValueError("archived_at must be timezone-aware")


@dataclass(frozen=True, slots=True)
class ProjectClosureArchiveWorkflowResponse:
    project_id: UUID
    archive_manifest_id: UUID
    project_status: str
    closure_status: str
    completed_steps: tuple[str, ...]


class WorkflowExecutionError(Exception):
    """Raised when project closure/archive fails at a specific workflow step."""

    def __init__(self, step: str, message: str) -> None:
        super().__init__(message)
        self.step = step


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class UpdateProjectFeaturePort(Protocol):
    def execute(self, request: UpdateProjectRequest): ...


class ArchiveProjectFeaturePort(Protocol):
    def execute(self, request: ArchiveProjectRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class CreateDocumentFeaturePort(Protocol):
    def execute(self, request: CreateDocumentRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class ProjectClosureArchiveWorkflow:
    """Orchestrates project closure and archiving across Projects/Documents/Accounting."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        update_project_feature: UpdateProjectFeaturePort,
        archive_project_feature: ArchiveProjectFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
        create_document_feature: CreateDocumentFeaturePort,
        search_journals_feature: SearchJournalsFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._update_project = update_project_feature
        self._archive_project = archive_project_feature
        self._list_documents = list_documents_feature
        self._create_document = create_document_feature
        self._search_journals = search_journals_feature
        self._list_fiscal_years = list_fiscal_years_feature

    def execute(
        self,
        request: ProjectClosureArchiveWorkflowRequest,
    ) -> ProjectClosureArchiveWorkflowResponse:
        request.validate()

        completed_steps: list[str] = []

        project_id = self._step_select_project(request.project_id)
        completed_steps.append("STEP-001")

        project = self._step_verify_project_active(project_id)
        completed_steps.append("STEP-002")

        finalized_documents = self._step_verify_required_documents_finalized(project_id)
        completed_steps.append("STEP-003")

        posted_journals = self._step_verify_no_unposted_journals(project_id)
        completed_steps.append("STEP-004")

        self._step_verify_budget_reconciliation_completed(project)
        completed_steps.append("STEP-005")

        archive_manifest_id = self._step_generate_archive_manifest(
            project=project,
            finalized_documents=finalized_documents,
            posted_journals=posted_journals,
            request=request,
        )
        completed_steps.append("STEP-006")

        project_status = self._step_archive_project(project_id=project_id, request=request)
        completed_steps.append("STEP-007")

        closure_status = self._step_mark_project_closed(
            project_id=project_id,
            archive_manifest_id=archive_manifest_id,
        )
        completed_steps.append("STEP-008")

        return ProjectClosureArchiveWorkflowResponse(
            project_id=project_id,
            archive_manifest_id=archive_manifest_id,
            project_status=project_status,
            closure_status=closure_status,
            completed_steps=tuple(completed_steps),
        )

    def _step_select_project(self, project_id: UUID) -> UUID:
        try:
            return project_id
        except Exception as exc:
            raise WorkflowExecutionError("STEP-001", "Select project failed") from exc

    def _step_verify_project_active(self, project_id: UUID):
        try:
            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
            if str(project.status).upper() != "ACTIVE":
                raise WorkflowExecutionError("STEP-002", "Verify project ACTIVE failed")
            return project
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-002", "Verify project ACTIVE failed") from exc

    def _step_verify_required_documents_finalized(self, project_id: UUID):
        try:
            all_documents = self._list_documents.execute(ListDocumentsRequest()).documents
            linked = tuple(
                item
                for item in all_documents
                if any(
                    ref.target_capability == "PROJECTS"
                    and ref.target_aggregate_type == "PROJECT"
                    and ref.target_aggregate_id == str(project_id)
                    for ref in item.references
                )
            )
            if not linked:
                raise WorkflowExecutionError("STEP-003", "Verify required documents finalized failed")

            all_finalized = all(
                str(item.status).upper() == "ACTIVE" and len(item.versions) > 0
                for item in linked
            )
            if not all_finalized:
                raise WorkflowExecutionError("STEP-003", "Verify required documents finalized failed")

            return linked
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-003", "Verify required documents finalized failed") from exc

    def _step_verify_no_unposted_journals(self, project_id: UUID):
        try:
            unposted = self._search_journals.execute(
                SearchJournalsRequest(
                    text=str(project_id),
                    status="DRAFT",
                )
            ).journals
            if unposted:
                raise WorkflowExecutionError(
                    "STEP-004",
                    "Verify no unposted accounting journals remain failed",
                )

            posted = self._search_journals.execute(
                SearchJournalsRequest(
                    text=str(project_id),
                    status="POSTED",
                )
            ).journals
            if not posted:
                raise WorkflowExecutionError(
                    "STEP-004",
                    "Verify no unposted accounting journals remain failed",
                )

            return posted
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError(
                "STEP-004",
                "Verify no unposted accounting journals remain failed",
            ) from exc

    def _step_verify_budget_reconciliation_completed(self, project) -> None:
        try:
            reconciled = any(
                ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper() == "BUDGET_RECONCILIATION:COMPLETED"
                for ref in project.references
            )
            if not reconciled:
                raise WorkflowExecutionError("STEP-005", "Verify budget reconciliation completed failed")
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError(
                "STEP-005",
                "Verify budget reconciliation completed failed",
            ) from exc

    def _step_generate_archive_manifest(
        self,
        *,
        project,
        finalized_documents,
        posted_journals,
        request: ProjectClosureArchiveWorkflowRequest,
    ) -> UUID:
        now = datetime.now(UTC)
        manifest_number = (
            request.archive_manifest_number.strip().upper()
            if request.archive_manifest_number is not None
            else f"ARCHIVE-{project.project_number.strip().upper()}"
        )

        organization_reference = next(
            (
                ref
                for ref in project.references
                if ref.reference_type == "ORGANISATION"
            ),
            None,
        )
        if organization_reference is None:
            raise WorkflowExecutionError("STEP-006", "Generate archive manifest failed")

        fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years
        posting_years = {item.posting_date.year for item in posted_journals}
        fiscal_year = next(
            (item for item in fiscal_years if item.year in posting_years),
            None,
        )
        if fiscal_year is None:
            raise WorkflowExecutionError("STEP-006", "Generate archive manifest failed")

        try:
            created = self._create_document.execute(
                CreateDocumentRequest(
                    document_number=manifest_number,
                    document_title=request.archive_manifest_title,
                    document_type="PROJECT_ARCHIVE_MANIFEST",
                    status="ACTIVE",
                    description=f"Archive manifest for project {project.project_number}",
                    created_at=now,
                    versions=(
                        DocumentVersionInput(
                            version_number=1,
                            storage_key=f"projects/{project.project_id}/archive/{manifest_number}/v1",
                            file_name=f"{manifest_number}.json",
                            mime_type="application/json",
                            checksum="archive-manifest-v1",
                            size_bytes=0,
                            created_at=now,
                        ),
                    ),
                    references=(
                        DocumentReferenceInput(
                            target_capability="PROJECTS",
                            target_aggregate_type="PROJECT",
                            target_aggregate_id=str(project.project_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Archive project root",
                        ),
                        DocumentReferenceInput(
                            target_capability="ORGANIZATION",
                            target_aggregate_type="ORGANISATION",
                            target_aggregate_id=str(organization_reference.external_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Owning organization",
                        ),
                        DocumentReferenceInput(
                            target_capability="ACCOUNTING",
                            target_aggregate_type="FISCAL_YEAR",
                            target_aggregate_id=str(fiscal_year.fiscal_year_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description=f"Fiscal year {fiscal_year.year}",
                        ),
                        DocumentReferenceInput(
                            target_capability="AUDIT",
                            target_aggregate_type="METADATA",
                            target_aggregate_id=now.isoformat(),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description="Workflow=WF-006;Actor=SYSTEM",
                        ),
                    )
                    + tuple(
                        DocumentReferenceInput(
                            target_capability="DOCUMENTS",
                            target_aggregate_type="DOCUMENT",
                            target_aggregate_id=str(item.document_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description=item.document_number,
                        )
                        for item in finalized_documents
                    )
                    + tuple(
                        DocumentReferenceInput(
                            target_capability="ACCOUNTING",
                            target_aggregate_type="JOURNAL",
                            target_aggregate_id=str(item.journal_id),
                            exists=True,
                            authorized=True,
                            is_soft_deleted=False,
                            is_archived=False,
                            checked_at=now,
                            description=item.journal_number,
                        )
                        for item in posted_journals
                    ),
                )
            )
            return created.document.document_id
        except WorkflowExecutionError:
            raise
        except Exception as exc:
            raise WorkflowExecutionError("STEP-006", "Generate archive manifest failed") from exc

    def _step_archive_project(
        self,
        *,
        project_id: UUID,
        request: ProjectClosureArchiveWorkflowRequest,
    ) -> str:
        archived_at = request.archived_at or datetime.now(UTC)
        try:
            archived = self._archive_project.execute(
                ArchiveProjectRequest(
                    project_id=project_id,
                    archived_at=archived_at,
                )
            )
            return archived.project.status
        except Exception as exc:
            raise WorkflowExecutionError("STEP-007", "Archive project failed") from exc

    def _step_mark_project_closed(self, *, project_id: UUID, archive_manifest_id: UUID) -> str:
        now = datetime.now(UTC)
        closure_marker_id = uuid5(
            NAMESPACE_URL,
            f"{project_id}:PROJECT_CLOSURE_STATUS:CLOSED",
        )
        try:
            project = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
            self._upsert_project_references(
                project_id=project_id,
                existing_references=project.references,
                additions=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=closure_marker_id,
                        description="PROJECT_CLOSURE_STATUS:CLOSED",
                        created_at=now,
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=archive_manifest_id,
                        description="PROJECT_ARCHIVE_MANIFEST",
                        created_at=now,
                    ),
                ),
            )
            return "CLOSED"
        except Exception as exc:
            raise WorkflowExecutionError("STEP-008", "Mark project CLOSED failed") from exc

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
