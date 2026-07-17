from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.documents import AttachReferenceResponse
from mfm.application.features.documents import CreateDocumentResponse
from mfm.application.features.documents import DocumentReferenceResponse
from mfm.application.features.documents import DocumentResponse
from mfm.application.features.documents import DocumentVersionResponse
from mfm.application.features.documents import GetDocumentResponse
from mfm.application.features.documents import ListDocumentsResponse
from mfm.application.features.documents import UpdateDocumentMetadataResponse
from mfm.application.features.projects import GetProjectResponse
from mfm.application.features.projects import ProjectResponse
from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflow,
)
from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflowRequest,
)
from mfm.application.workflows.project_document_registration_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _State:
    project_id: UUID = uuid4()
    document_id: UUID = uuid4()


class _GetProjectFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("project does not exist")
        _ = request
        return GetProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status="ACTIVE",
                priority="HIGH",
                description=None,
                start_date=None,
                end_date=None,
                created_at=datetime.now(UTC),
                updated_at=None,
                archived_at=None,
                version=1,
                milestones=(),
                activities=(),
                assignments=(),
                references=(),
            )
        )


class _CreateDocumentFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        now = datetime.now(UTC)
        return CreateDocumentResponse(
            document=DocumentResponse(
                document_id=self.state.document_id,
                document_number=request.document_number,
                document_title=request.document_title,
                document_type=request.document_type,
                status=request.status,
                description=request.description,
                created_at=now,
                updated_at=None,
                archived_at=None,
                disposed_at=None,
                version=1,
                versions=(
                    DocumentVersionResponse(
                        version_number=1,
                        storage_key="x",
                        file_name=None,
                        mime_type=None,
                        checksum=None,
                        size_bytes=0,
                        created_at=now,
                    ),
                ),
                references=(),
            )
        )


class _AttachReferenceFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("attach failed")
        now = datetime.now(UTC)
        return AttachReferenceResponse(
            document=DocumentResponse(
                document_id=self.state.document_id,
                document_number="DOC-001",
                document_title="Doc",
                document_type="UNCLASSIFIED",
                status="ACTIVE",
                description=None,
                created_at=now,
                updated_at=now,
                archived_at=None,
                disposed_at=None,
                version=2,
                versions=(
                    DocumentVersionResponse(
                        version_number=1,
                        storage_key="x",
                        file_name=None,
                        mime_type=None,
                        checksum=None,
                        size_bytes=0,
                        created_at=now,
                    ),
                ),
                references=(
                    DocumentReferenceResponse(
                        reference_id=uuid4(),
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(self.state.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=now,
                        description="Link",
                    ),
                ),
            )
        )


class _UpdateDocumentMetadataFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        now = datetime.now(UTC)
        return UpdateDocumentMetadataResponse(
            document=DocumentResponse(
                document_id=self.state.document_id,
                document_number="DOC-001",
                document_title=request.document_title or "Doc",
                document_type=request.document_type or "PROJECT_DOCUMENT",
                status="ACTIVE",
                description=request.description,
                created_at=now,
                updated_at=now,
                archived_at=None,
                disposed_at=None,
                version=3,
                versions=(
                    DocumentVersionResponse(
                        version_number=1,
                        storage_key="x",
                        file_name=None,
                        mime_type=None,
                        checksum=None,
                        size_bytes=0,
                        created_at=now,
                    ),
                ),
                references=(
                    DocumentReferenceResponse(
                        reference_id=uuid4(),
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(self.state.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=now,
                        description="Link",
                    ),
                ),
            )
        )


class _GetDocumentFeature:
    def __init__(self, state: _State, *, linked: bool = True) -> None:
        self.state = state
        self.linked = linked

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        references: tuple[DocumentReferenceResponse, ...]
        if self.linked:
            references = (
                DocumentReferenceResponse(
                    reference_id=uuid4(),
                    target_capability="PROJECTS",
                    target_aggregate_type="PROJECT",
                    target_aggregate_id=str(self.state.project_id),
                    exists=True,
                    authorized=True,
                    is_soft_deleted=False,
                    is_archived=False,
                    checked_at=now,
                    description="Link",
                ),
            )
        else:
            references = ()

        return GetDocumentResponse(
            document=DocumentResponse(
                document_id=self.state.document_id,
                document_number="DOC-001",
                document_title="Doc",
                document_type="PROJECT_DOCUMENT",
                status="ACTIVE",
                description=None,
                created_at=now,
                updated_at=now,
                archived_at=None,
                disposed_at=None,
                version=3,
                versions=(
                    DocumentVersionResponse(
                        version_number=1,
                        storage_key="x",
                        file_name=None,
                        mime_type=None,
                        checksum=None,
                        size_bytes=0,
                        created_at=now,
                    ),
                ),
                references=references,
            )
        )


class _ListDocumentsFeature:
    def __init__(self, state: _State, *, include_document: bool = True) -> None:
        self.state = state
        self.include_document = include_document

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        documents: tuple[DocumentResponse, ...]
        if self.include_document:
            documents = (
                DocumentResponse(
                    document_id=self.state.document_id,
                    document_number="DOC-001",
                    document_title="Doc",
                    document_type="PROJECT_DOCUMENT",
                    status="ACTIVE",
                    description=None,
                    created_at=now,
                    updated_at=now,
                    archived_at=None,
                    disposed_at=None,
                    version=3,
                    versions=(
                        DocumentVersionResponse(
                            version_number=1,
                            storage_key="x",
                            file_name=None,
                            mime_type=None,
                            checksum=None,
                            size_bytes=0,
                            created_at=now,
                        ),
                    ),
                    references=(),
                ),
            )
        else:
            documents = ()

        return ListDocumentsResponse(documents=documents)


def _workflow(
    *,
    project_missing: bool = False,
    attach_fail: bool = False,
    linked: bool = True,
    include_document: bool = True,
) -> tuple[ProjectDocumentRegistrationWorkflow, _State]:
    state = _State()
    workflow = ProjectDocumentRegistrationWorkflow(
        get_project_feature=_GetProjectFeature(state, should_fail=project_missing),
        create_document_feature=_CreateDocumentFeature(state),
        attach_reference_feature=_AttachReferenceFeature(state, should_fail=attach_fail),
        update_document_metadata_feature=_UpdateDocumentMetadataFeature(state),
        get_document_feature=_GetDocumentFeature(state, linked=linked),
        list_documents_feature=_ListDocumentsFeature(state, include_document=include_document),
    )
    return workflow, state


def _request(state: _State) -> ProjectDocumentRegistrationWorkflowRequest:
    return ProjectDocumentRegistrationWorkflowRequest(
        project_id=state.project_id,
        document_number="DOC-WF003-001",
        document_title="Project Scope",
        initial_document_type="UNCLASSIFIED",
        classification_document_type="PROJECT_SPECIFICATION",
        document_description="WF-003",
    )


def test_workflow_happy_path() -> None:
    workflow, state = _workflow()

    result = workflow.execute(_request(state))

    assert result.project_id == state.project_id
    assert result.document_id == state.document_id
    assert result.classification_document_type == "PROJECT_SPECIFICATION"
    assert result.completed_steps == (
        "STEP-001",
        "STEP-002",
        "STEP-003",
        "STEP-004",
        "STEP-005",
        "STEP-006",
        "STEP-007",
    )


def test_failure_when_project_missing() -> None:
    workflow, state = _workflow(project_missing=True)

    with pytest.raises(WorkflowExecutionError, match="Verify project exists failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_failure_when_attach_fails() -> None:
    workflow, state = _workflow(attach_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Attach document to project failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-004"


def test_failure_when_link_verification_fails() -> None:
    workflow, state = _workflow(linked=False)

    with pytest.raises(WorkflowExecutionError, match="Document linkage verification failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-006"


def test_failure_when_availability_fails() -> None:
    workflow, state = _workflow(include_document=False)

    with pytest.raises(WorkflowExecutionError, match="Document availability confirmation failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-007"
