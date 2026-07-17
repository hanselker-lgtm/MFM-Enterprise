from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.documents import CreateDocumentResponse
from mfm.application.features.documents import DocumentResponse
from mfm.application.features.documents import ListDocumentsResponse
from mfm.application.features.projects import CreateProjectResponse
from mfm.application.features.projects import ExternalReferenceResponse
from mfm.application.features.projects import GetProjectResponse
from mfm.application.features.projects import ProjectAssignmentResponse
from mfm.application.features.projects import ProjectResponse
from mfm.application.features.projects import UpdateProjectResponse
from mfm.application.features.organization import UpdateOrganizationResponse
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflow,
)
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflowRequest,
)
from mfm.application.workflows.complete_project_creation_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _State:
    organization_id: UUID = uuid4()
    owner_contact_id: UUID = uuid4()
    project_id: UUID = uuid4()
    library_id: UUID = uuid4()
    budget_id: UUID = uuid4()


class _UpdateOrganizationFeature:
    def __init__(self, *, should_fail: bool = False) -> None:
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("org update failed")
        return UpdateOrganizationResponse(
            organization_id=request.organization_id,
            organization_number="ORG-001",
            name="Org",
            status="ACTIVE",
        )


class _CreateProjectFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        _ = request
        return CreateProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status="ACTIVE",
                priority="NORMAL",
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


class _UpdateProjectFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        references = ()
        assignments = ()
        if request.references is not None:
            references = tuple(
                ExternalReferenceResponse(
                    reference_id=uuid4(),
                    reference_type=item.reference_type,
                    external_id=item.external_id,
                    description=item.description,
                    created_at=item.created_at or datetime.now(UTC),
                )
                for item in request.references
            )
        if request.assignments is not None:
            assignments = tuple(
                ProjectAssignmentResponse(
                    assignment_id=uuid4(),
                    organisation_id=item.organisation_id,
                    contact_id=item.contact_id,
                    role=item.role,
                    assigned_from=item.assigned_from,
                    assigned_until=item.assigned_until,
                )
                for item in request.assignments
            )
        return UpdateProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status="ACTIVE",
                priority="NORMAL",
                description=request.description,
                start_date=None,
                end_date=None,
                created_at=datetime.now(UTC),
                updated_at=request.updated_at,
                archived_at=None,
                version=1,
                milestones=(),
                activities=(),
                assignments=assignments,
                references=references,
            )
        )


class _GetProjectFeature:
    def __init__(self, state: _State, *, status: str = "ACTIVE") -> None:
        self.state = state
        self.status = status

    def execute(self, request):
        _ = request
        return GetProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-001",
                project_name="Project",
                status=self.status,
                priority="NORMAL",
                description=None,
                start_date=None,
                end_date=None,
                created_at=datetime.now(UTC),
                updated_at=datetime.now(UTC),
                archived_at=None,
                version=1,
                milestones=(),
                activities=(),
                assignments=(
                    ProjectAssignmentResponse(
                        assignment_id=uuid4(),
                        organisation_id=self.state.organization_id,
                        contact_id=self.state.owner_contact_id,
                        role="OWNER",
                        assigned_from=None,
                        assigned_until=None,
                    ),
                ),
                references=(
                    ExternalReferenceResponse(
                        reference_id=uuid4(),
                        reference_type="ORGANISATION",
                        external_id=self.state.organization_id,
                        description="Owning organization",
                        created_at=datetime.now(UTC),
                    ),
                    ExternalReferenceResponse(
                        reference_id=uuid4(),
                        reference_type="DOCUMENT",
                        external_id=self.state.library_id,
                        description="Project document library",
                        created_at=datetime.now(UTC),
                    ),
                    ExternalReferenceResponse(
                        reference_id=uuid4(),
                        reference_type="DOCUMENT",
                        external_id=self.state.budget_id,
                        description="Project budget container",
                        created_at=datetime.now(UTC),
                    ),
                ),
            )
        )


class _CreateDocumentFeature:
    def __init__(self, state: _State) -> None:
        self.state = state
        self.calls = 0

    def execute(self, request):
        now = datetime.now(UTC)
        document_id = self.state.library_id if self.calls == 0 else self.state.budget_id
        self.calls += 1
        return CreateDocumentResponse(
            document=DocumentResponse(
                document_id=document_id,
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
                versions=(),
                references=(),
            )
        )


class _ListDocumentsFeature:
    def __init__(self, state: _State, *, include_budget: bool = True) -> None:
        self.state = state
        self.include_budget = include_budget

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        docs = [
            DocumentResponse(
                document_id=self.state.library_id,
                document_number="PRJ-LIB-PRJ-001",
                document_title="Library",
                document_type="PROJECT_LIBRARY",
                status="ACTIVE",
                description=None,
                created_at=now,
                updated_at=None,
                archived_at=None,
                disposed_at=None,
                version=1,
                versions=(),
                references=(),
            )
        ]
        if self.include_budget:
            docs.append(
                DocumentResponse(
                    document_id=self.state.budget_id,
                    document_number="PRJ-BUD-PRJ-001",
                    document_title="Budget",
                    document_type="PROJECT_BUDGET_CONTAINER",
                    status="ACTIVE",
                    description=None,
                    created_at=now,
                    updated_at=None,
                    archived_at=None,
                    disposed_at=None,
                    version=1,
                    versions=(),
                    references=(),
                )
            )

        return ListDocumentsResponse(documents=tuple(docs))


def _workflow(
    *,
    organization_fail: bool = False,
    project_status: str = "ACTIVE",
    include_budget_document: bool = True,
) -> tuple[CompleteProjectCreationWorkflow, _State]:
    state = _State()

    workflow = CompleteProjectCreationWorkflow(
        update_organization_feature=_UpdateOrganizationFeature(should_fail=organization_fail),
        create_project_feature=_CreateProjectFeature(state),
        update_project_feature=_UpdateProjectFeature(state),
        get_project_feature=_GetProjectFeature(state, status=project_status),
        create_document_feature=_CreateDocumentFeature(state),
        list_documents_feature=_ListDocumentsFeature(state, include_budget=include_budget_document),
    )
    return workflow, state


def _request(state: _State) -> CompleteProjectCreationWorkflowRequest:
    return CompleteProjectCreationWorkflowRequest(
        organization_id=state.organization_id,
        organization_owner_contact_id=state.owner_contact_id,
        project_number="PRJ-001",
        project_name="Project",
        project_priority="HIGH",
        project_description="WF-002",
    )


def test_workflow_happy_path() -> None:
    workflow, state = _workflow()

    response = workflow.execute(_request(state))

    assert response.project_id == state.project_id
    assert response.project_status == "ACTIVE"
    assert response.project_document_library_id == state.library_id
    assert response.project_budget_container_id == state.budget_id
    assert response.completed_steps == (
        "STEP-001",
        "STEP-002",
        "STEP-003",
        "STEP-004",
        "STEP-005",
        "STEP-006",
        "STEP-007",
    )


def test_workflow_failure_assign_organization_ownership() -> None:
    workflow, state = _workflow(organization_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Assign organization ownership failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_workflow_failure_verification_when_budget_missing() -> None:
    workflow, state = _workflow(include_budget_document=False)

    with pytest.raises(WorkflowExecutionError, match="Project budget container verification failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-006"


def test_workflow_failure_when_project_not_active() -> None:
    workflow, state = _workflow(project_status="PLANNED")

    with pytest.raises(WorkflowExecutionError, match="Project is not ACTIVE") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-007"


def test_request_validation_rejects_naive_datetime() -> None:
    workflow, state = _workflow()

    with pytest.raises(ValueError, match="timezone-aware"):
        workflow.execute(
            CompleteProjectCreationWorkflowRequest(
                organization_id=state.organization_id,
                organization_owner_contact_id=state.owner_contact_id,
                project_number="PRJ-001",
                project_name="Project",
                project_priority="HIGH",
                project_start_date=datetime(2035, 1, 1, 8, 0),
            )
        )
