from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.accounting import FiscalPeriodResponse
from mfm.application.features.accounting import FiscalYearResponse
from mfm.application.features.accounting import ListFiscalYearsResponse
from mfm.application.features.accounting import SearchJournalsResponse
from mfm.application.features.accounting.create_journal_feature import JournalSearchResultResponse
from mfm.application.features.documents import CreateDocumentResponse
from mfm.application.features.documents import DocumentReferenceResponse
from mfm.application.features.documents import DocumentResponse
from mfm.application.features.documents import DocumentVersionResponse
from mfm.application.features.documents import ListDocumentsResponse
from mfm.application.features.projects import ArchiveProjectResponse
from mfm.application.features.projects import ExternalReferenceResponse
from mfm.application.features.projects import GetProjectResponse
from mfm.application.features.projects import ProjectResponse
from mfm.application.features.projects import UpdateProjectResponse
from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflow,
)
from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflowRequest,
)
from mfm.application.workflows.project_closure_archive_workflow import (
    WorkflowExecutionError,
)


@dataclass
class _State:
    project_id: UUID = uuid4()
    organization_id: UUID = uuid4()
    archive_manifest_id: UUID = uuid4()
    references: tuple[ExternalReferenceResponse, ...] = ()


class _GetProjectFeature:
    def __init__(self, state: _State, *, active: bool = True) -> None:
        self.state = state
        self.active = active

    def execute(self, request):
        _ = request
        return GetProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-WF006-001",
                project_name="WF-006 Project",
                status=("ACTIVE" if self.active else "ON_HOLD"),
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
                references=self.state.references,
            )
        )


class _UpdateProjectFeature:
    def __init__(self, state: _State, *, should_fail: bool = False) -> None:
        self.state = state
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("update failed")
        now = datetime.now(UTC)
        self.state.references = tuple(
            ExternalReferenceResponse(
                reference_id=ref.reference_id or uuid4(),
                reference_type=ref.reference_type,
                external_id=ref.external_id,
                description=ref.description,
                created_at=ref.created_at or now,
            )
            for ref in request.references or ()
        )
        return UpdateProjectResponse(
            project=ProjectResponse(
                project_id=self.state.project_id,
                project_number="PRJ-WF006-001",
                project_name="WF-006 Project",
                status="ARCHIVED",
                priority="HIGH",
                description=None,
                start_date=None,
                end_date=None,
                created_at=now,
                updated_at=now,
                archived_at=now,
                version=2,
                milestones=(),
                activities=(),
                assignments=(),
                references=self.state.references,
            )
        )


class _ArchiveProjectFeature:
    def __init__(self, *, should_fail: bool = False) -> None:
        self.should_fail = should_fail

    def execute(self, request):
        if self.should_fail:
            raise RuntimeError("archive failed")
        return ArchiveProjectResponse(
            project=ProjectResponse(
                project_id=request.project_id,
                project_number="PRJ-WF006-001",
                project_name="WF-006 Project",
                status="ARCHIVED",
                priority="HIGH",
                description=None,
                start_date=None,
                end_date=None,
                created_at=datetime.now(UTC),
                updated_at=datetime.now(UTC),
                archived_at=request.archived_at,
                version=2,
                milestones=(),
                activities=(),
                assignments=(),
                references=(),
            )
        )


class _ListDocumentsFeature:
    def __init__(self, state: _State, *, finalized: bool = True) -> None:
        self.state = state
        self.finalized = finalized

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        return ListDocumentsResponse(
            documents=(
                DocumentResponse(
                    document_id=uuid4(),
                    document_number="DOC-WF006-001",
                    document_title="Completion Report",
                    document_type="PROJECT_REPORT",
                    status=("ACTIVE" if self.finalized else "DRAFT"),
                    description=None,
                    created_at=now,
                    updated_at=now,
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
                    )
                    if self.finalized
                    else (),
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
                            description="project doc",
                        ),
                    ),
                ),
            )
        )


class _CreateDocumentFeature:
    def __init__(self, state: _State) -> None:
        self.state = state

    def execute(self, request):
        _ = request
        now = datetime.now(UTC)
        return CreateDocumentResponse(
            document=DocumentResponse(
                document_id=self.state.archive_manifest_id,
                document_number="ARCHIVE-PRJ-WF006-001",
                document_title="Project Archive Manifest",
                document_type="PROJECT_ARCHIVE_MANIFEST",
                status="ACTIVE",
                description="manifest",
                created_at=now,
                updated_at=None,
                archived_at=None,
                disposed_at=None,
                version=1,
                versions=(
                    DocumentVersionResponse(
                        version_number=1,
                        storage_key="manifest",
                        file_name="manifest.json",
                        mime_type="application/json",
                        checksum="x",
                        size_bytes=0,
                        created_at=now,
                    ),
                ),
                references=(),
            )
        )


class _SearchJournalsFeature:
    def __init__(self, *, has_unposted: bool = False) -> None:
        self.has_unposted = has_unposted

    def execute(self, request):
        if request.status == "DRAFT":
            journals = (
                JournalSearchResultResponse(
                    journal_id=uuid4(),
                    fiscal_year_id=uuid4(),
                    journal_number="JRN-DRAFT-001",
                    posting_date=date(2041, 6, 15),
                    status="DRAFT",
                    reference=request.text,
                ),
            ) if self.has_unposted else ()
            return SearchJournalsResponse(journals=journals)

        return SearchJournalsResponse(
            journals=(
                JournalSearchResultResponse(
                    journal_id=uuid4(),
                    fiscal_year_id=uuid4(),
                    journal_number="JRN-POSTED-001",
                    posting_date=date(2041, 6, 15),
                    status="POSTED",
                    reference=request.text,
                ),
            )
        )


class _ListFiscalYearsFeature:
    def execute(self, request):
        _ = request
        return ListFiscalYearsResponse(
            fiscal_years=(
                FiscalYearResponse(
                    fiscal_year_id=uuid4(),
                    year=2041,
                    start_date=date(2041, 1, 1),
                    end_date=date(2041, 12, 31),
                    status="OPEN",
                    periods=(
                        FiscalPeriodResponse(
                            number=1,
                            start_date=date(2041, 1, 1),
                            end_date=date(2041, 12, 31),
                            closed=False,
                        ),
                    ),
                ),
            )
        )


def _workflow(
    *,
    active: bool = True,
    finalized_docs: bool = True,
    has_unposted: bool = False,
    reconciled: bool = True,
    archive_fail: bool = False,
    close_fail: bool = False,
):
    state = _State(
        references=(
            ExternalReferenceResponse(
                reference_id=uuid4(),
                reference_type="ORGANISATION",
                external_id=uuid4(),
                description="Org",
                created_at=datetime.now(UTC),
            ),
            ExternalReferenceResponse(
                reference_id=uuid4(),
                reference_type="DOCUMENT",
                external_id=uuid4(),
                description=(
                    "BUDGET_RECONCILIATION:COMPLETED" if reconciled else "BUDGET_RECONCILIATION:PENDING"
                ),
                created_at=datetime.now(UTC),
            ),
        )
    )

    workflow = ProjectClosureArchiveWorkflow(
        get_project_feature=_GetProjectFeature(state, active=active),
        update_project_feature=_UpdateProjectFeature(state, should_fail=close_fail),
        archive_project_feature=_ArchiveProjectFeature(should_fail=archive_fail),
        list_documents_feature=_ListDocumentsFeature(state, finalized=finalized_docs),
        create_document_feature=_CreateDocumentFeature(state),
        search_journals_feature=_SearchJournalsFeature(has_unposted=has_unposted),
        list_fiscal_years_feature=_ListFiscalYearsFeature(),
    )
    return workflow, state


def _request(state: _State) -> ProjectClosureArchiveWorkflowRequest:
    return ProjectClosureArchiveWorkflowRequest(project_id=state.project_id)


def test_workflow_happy_path() -> None:
    workflow, state = _workflow()

    response = workflow.execute(_request(state))

    assert response.project_id == state.project_id
    assert response.archive_manifest_id == state.archive_manifest_id
    assert response.project_status == "ARCHIVED"
    assert response.closure_status == "CLOSED"
    assert response.completed_steps == (
        "STEP-001",
        "STEP-002",
        "STEP-003",
        "STEP-004",
        "STEP-005",
        "STEP-006",
        "STEP-007",
        "STEP-008",
    )


def test_failure_when_project_not_active() -> None:
    workflow, state = _workflow(active=False)

    with pytest.raises(WorkflowExecutionError, match="Verify project ACTIVE failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-002"


def test_failure_when_documents_not_finalized() -> None:
    workflow, state = _workflow(finalized_docs=False)

    with pytest.raises(WorkflowExecutionError, match="Verify required documents finalized failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-003"


def test_failure_when_unposted_journals_exist() -> None:
    workflow, state = _workflow(has_unposted=True)

    with pytest.raises(
        WorkflowExecutionError,
        match="Verify no unposted accounting journals remain failed",
    ) as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-004"


def test_failure_when_budget_not_reconciled() -> None:
    workflow, state = _workflow(reconciled=False)

    with pytest.raises(WorkflowExecutionError, match="Verify budget reconciliation completed failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-005"


def test_failure_when_archive_fails() -> None:
    workflow, state = _workflow(archive_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Archive project failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-007"


def test_failure_when_close_marking_fails() -> None:
    workflow, state = _workflow(close_fail=True)

    with pytest.raises(WorkflowExecutionError, match="Mark project CLOSED failed") as exc:
        workflow.execute(_request(state))

    assert exc.value.step == "STEP-008"
