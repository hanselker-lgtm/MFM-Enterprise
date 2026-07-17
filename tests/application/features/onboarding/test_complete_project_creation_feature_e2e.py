from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.external_reference_model  # noqa: F401
import mfm.database.models.project_activity_model  # noqa: F401
import mfm.database.models.project_assignment_model  # noqa: F401
import mfm.database.models.project_milestone_model  # noqa: F401
import mfm.database.models.project_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.documents import ListDocumentsFeature
from mfm.application.features.onboarding.complete_project_creation_feature import (
    CompleteProjectCreationFeature,
)
from mfm.application.features.onboarding.complete_project_creation_feature import (
    CompleteProjectCreationRequest,
)
from mfm.application.features.organization import CreateOrganizationFeature
from mfm.application.features.organization import CreateOrganizationRequest
from mfm.application.features.organization import UpdateOrganizationFeature
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import GetProjectFeature
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectFeature
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflow,
)
from mfm.database.models.base_model import BaseModel
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_type import OrganizationType
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_organization_repository import (
    SQLiteOrganizationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectCreationApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)

        self.organization_repository = SQLiteOrganizationRepository(self._persistence_uow)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)
        self.document_repository = SQLiteDocumentRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class _FeatureStack:
    create_organization: CreateOrganizationFeature
    update_organization: UpdateOrganizationFeature
    create_project: CreateProjectFeature
    update_project: UpdateProjectFeature
    get_project: GetProjectFeature
    create_document: CreateDocumentFeature
    list_documents: ListDocumentsFeature


@pytest.fixture(autouse=True)
def _clear_class_state() -> None:
    Organization._clear_registry_for_tests()
    try:
        yield
    finally:
        Organization._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "project_creation_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    dispatcher = DomainEventDispatcher()
    uow = SQLiteProjectCreationApplicationUnitOfWork(session)

    return _FeatureStack(
        create_organization=CreateOrganizationFeature(
            service=CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)
        ),
        update_organization=UpdateOrganizationFeature(
            service=UpdateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)
        ),
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        update_project=UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)),
        get_project=GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
        create_document=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        list_documents=ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)),
    )


def test_complete_project_creation_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        created_org = stack.create_organization.execute(
            CreateOrganizationRequest(
                organization_number="ORG-WF002-001",
                name="WF-002 Organization",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )

        workflow = CompleteProjectCreationWorkflow(
            update_organization_feature=stack.update_organization,
            create_project_feature=stack.create_project,
            update_project_feature=stack.update_project,
            get_project_feature=stack.get_project,
            create_document_feature=stack.create_document,
            list_documents_feature=stack.list_documents,
        )
        feature = CompleteProjectCreationFeature(service=workflow)

        response = feature.execute(
            CompleteProjectCreationRequest(
                organization_id=created_org.organization_id,
                organization_owner_contact_id=uuid4(),
                project_number="PRJ-WF002-001",
                project_name="WF-002 Project",
                project_priority="HIGH",
                project_description="Workflow project",
                project_start_date=datetime(2036, 1, 15, 8, 0, tzinfo=UTC),
                project_end_date=datetime(2036, 6, 30, 16, 0, tzinfo=UTC),
                project_created_at=datetime(2036, 1, 10, 8, 0, tzinfo=UTC),
            )
        )

        assert response.project_status == "ACTIVE"
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
        )

        persisted_project = stack.get_project.execute(
            GetProjectRequest(project_id=response.project_id)
        ).project
        assert persisted_project.status == "ACTIVE"
        assert any(
            assignment.organisation_id == created_org.organization_id
            for assignment in persisted_project.assignments
        )

        active_docs = stack.list_documents.execute(ListDocumentsRequest(status="ACTIVE"))
        doc_ids = {item.document_id for item in active_docs.documents}
        assert response.project_document_library_id in doc_ids
        assert response.project_budget_container_id in doc_ids
    finally:
        session.close()
