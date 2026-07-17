from __future__ import annotations

from datetime import UTC
from datetime import datetime
from pathlib import Path

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

from mfm.application.documents.attach_reference import AttachReferenceUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.get_document import GetDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.documents.update_document_metadata import UpdateDocumentMetadataUseCase
from mfm.application.features.documents import AttachReferenceFeature
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import GetDocumentFeature
from mfm.application.features.documents import GetDocumentRequest
from mfm.application.features.documents import ListDocumentsFeature
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.documents import UpdateDocumentMetadataFeature
from mfm.application.features.onboarding.project_document_registration_feature import (
    ProjectDocumentRegistrationFeature,
)
from mfm.application.features.onboarding.project_document_registration_feature import (
    ProjectDocumentRegistrationRequest,
)
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import GetProjectFeature
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.project_document_registration_workflow import (
    ProjectDocumentRegistrationWorkflow,
)
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectDocumentRegistrationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
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


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "project_document_registration_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def test_project_document_registration_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        uow = SQLiteProjectDocumentRegistrationUnitOfWork(session)

        create_project_feature = CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow))
        get_project_feature = GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow))

        create_document_feature = CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow))
        attach_reference_feature = AttachReferenceFeature(service=AttachReferenceUseCase(unit_of_work=uow))
        update_document_metadata_feature = UpdateDocumentMetadataFeature(
            service=UpdateDocumentMetadataUseCase(unit_of_work=uow)
        )
        get_document_feature = GetDocumentFeature(service=GetDocumentUseCase(unit_of_work=uow))
        list_documents_feature = ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow))

        created_project = create_project_feature.execute(
            CreateProjectRequest(
                project_number="PRJ-WF003-001",
                project_name="WF-003 Project",
                status="ACTIVE",
                priority="HIGH",
                created_at=datetime(2038, 1, 5, 8, 0, tzinfo=UTC),
            )
        )

        workflow = ProjectDocumentRegistrationWorkflow(
            get_project_feature=get_project_feature,
            create_document_feature=create_document_feature,
            attach_reference_feature=attach_reference_feature,
            update_document_metadata_feature=update_document_metadata_feature,
            get_document_feature=get_document_feature,
            list_documents_feature=list_documents_feature,
        )
        feature = ProjectDocumentRegistrationFeature(service=workflow)

        response = feature.execute(
            ProjectDocumentRegistrationRequest(
                project_id=created_project.project.project_id,
                document_number="DOC-WF003-001",
                document_title="Scope Baseline",
                initial_document_type="UNCLASSIFIED",
                classification_document_type="PROJECT_SPECIFICATION",
                document_description="WF-003 end-to-end",
                created_at=datetime(2038, 1, 6, 8, 0, tzinfo=UTC),
            )
        )

        assert response.project_id == created_project.project.project_id
        assert response.classification_document_type == "PROJECT_SPECIFICATION"
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
        )

        persisted_document = get_document_feature.execute(
            GetDocumentRequest(document_id=response.document_id)
        ).document
        assert persisted_document.document_type == "PROJECT_SPECIFICATION"
        assert any(
            ref.target_capability == "PROJECTS"
            and ref.target_aggregate_type == "PROJECT"
            and ref.target_aggregate_id == str(created_project.project.project_id)
            for ref in persisted_document.references
        )

        active_documents = list_documents_feature.execute(ListDocumentsRequest(status="ACTIVE"))
        assert any(item.document_id == response.document_id for item in active_documents.documents)
    finally:
        session.close()
