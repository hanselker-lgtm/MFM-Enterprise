from __future__ import annotations

import ast
from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import UUID

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

from mfm.application.features.projects.archive_project_feature import ArchiveProjectFeature
from mfm.application.features.projects.archive_project_feature import ArchiveProjectRequest
from mfm.application.features.projects.complete_project_feature import CompleteProjectFeature
from mfm.application.features.projects.complete_project_feature import CompleteProjectRequest
from mfm.application.features.projects.create_project_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.projects.create_project_feature import (
    CreateProjectFeature,
)
from mfm.application.features.projects.create_project_feature import (
    CreateProjectRequest,
)
from mfm.application.features.projects.create_project_feature import (
    ExternalReferenceInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectActivityInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectAssignmentInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectMilestoneInput,
)
from mfm.application.features.projects.delete_project_feature import DeleteProjectFeature
from mfm.application.features.projects.delete_project_feature import DeleteProjectRequest
from mfm.application.features.projects.get_project_feature import GetProjectFeature
from mfm.application.features.projects.get_project_feature import GetProjectRequest
from mfm.application.features.projects.update_project_feature import UpdateProjectFeature
from mfm.application.features.projects.update_project_feature import UpdateProjectRequest
from mfm.application.projects.archive_project import ArchiveProjectUseCase
from mfm.application.projects.complete_project import CompleteProjectUseCase
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.delete_project import DeleteProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectsApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)

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
class ProjectsFeatureStack:
    create: CreateProjectFeature
    get: GetProjectFeature
    update: UpdateProjectFeature
    complete: CompleteProjectFeature
    archive: ArchiveProjectFeature
    delete: DeleteProjectFeature


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "projects_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_feature_stack(session: Session) -> ProjectsFeatureStack:
    uow = SQLiteProjectsApplicationUnitOfWork(session)

    return ProjectsFeatureStack(
        create=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        get=GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
        update=UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)),
        complete=CompleteProjectFeature(service=CompleteProjectUseCase(unit_of_work=uow)),
        archive=ArchiveProjectFeature(service=ArchiveProjectUseCase(unit_of_work=uow)),
        delete=DeleteProjectFeature(service=DeleteProjectUseCase(unit_of_work=uow)),
    )


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _milestone(name: str, sequence: int, *, completed: bool = False) -> ProjectMilestoneInput:
    return ProjectMilestoneInput(
        name=name,
        sequence=sequence,
        status="COMPLETED" if completed else "PLANNED",
        due_date=_aware_utc(2030, 1, 20 + sequence, 8),
        completed_date=_aware_utc(2030, 2, 1 + sequence, 8) if completed else None,
    )


def _activity(title: str, *, completed: bool = False) -> ProjectActivityInput:
    return ProjectActivityInput(
        title=title,
        status="COMPLETED" if completed else "ACTIVE",
        priority="HIGH",
        planned_start=_aware_utc(2030, 1, 10, 8),
        planned_finish=_aware_utc(2030, 1, 15, 8),
        actual_start=_aware_utc(2030, 1, 10, 8) if completed else None,
        actual_finish=_aware_utc(2030, 1, 15, 8) if completed else None,
        estimated_hours="16.50",
        actual_hours="16.50" if completed else None,
    )


def _assignment(role: str) -> ProjectAssignmentInput:
    return ProjectAssignmentInput(
        organisation_id=UUID("00000000-0000-0000-0000-00000000DD11"),
        contact_id=UUID("00000000-0000-0000-0000-00000000DD21"),
        role=role,
        assigned_from=_aware_utc(2030, 1, 5, 8),
    )


def _reference(reference_type: str, external_id: UUID) -> ExternalReferenceInput:
    return ExternalReferenceInput(
        reference_type=reference_type,
        external_id=external_id,
        description=f"Linked {reference_type.lower()}",
        created_at=_aware_utc(2030, 1, 6, 8),
    )


def test_e2e_workflow_1_full_projects_lifecycle_with_reopen_persistence(sqlite_session_factory) -> None:
    project_id: UUID | None = None

    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)

        # 1) Create Project
        created = stack.create.execute(
            CreateProjectRequest(
                project_number="PROJ-E2E-001",
                project_name="Harbor Upgrade Program",
                status="ACTIVE",
                priority="HIGH",
                description="Main end-to-end project",
                start_date=_aware_utc(2030, 1, 5, 8),
                end_date=_aware_utc(2030, 3, 31, 8),
                created_at=_aware_utc(2030, 1, 1, 8),
            )
        )
        project_id = created.project.project_id

        # 2) Retrieve Project
        loaded = stack.get.execute(GetProjectRequest(project_id=project_id))
        assert loaded.project.project_number == "PROJ-E2E-001"
        assert loaded.project.status == "ACTIVE"
        assert loaded.project.activities == ()
        assert loaded.project.milestones == ()

        # 3,4,5,6,7) Update Project + add activities/milestones/assignments/references
        updated = stack.update.execute(
            UpdateProjectRequest(
                project_id=project_id,
                project_name="Harbor Upgrade Program - Phase 1",
                description="Execution scope refined",
                priority="URGENT",
                updated_at=_aware_utc(2030, 1, 7, 8),
                activities=(
                    _activity("Civil works"),
                    _activity("Systems commissioning"),
                ),
                milestones=(
                    _milestone("Design approved", 1),
                    _milestone("Execution ready", 2),
                ),
                assignments=(
                    _assignment("Project Manager"),
                    _assignment("Site Lead"),
                ),
                references=(
                    _reference(
                        "PURCHASE_ORDER",
                        UUID("00000000-0000-0000-0000-00000000DD31"),
                    ),
                    _reference(
                        "DOCUMENT",
                        UUID("00000000-0000-0000-0000-00000000DD41"),
                    ),
                ),
            )
        )

        assert updated.project.project_name == "Harbor Upgrade Program - Phase 1"
        assert len(updated.project.activities) == 2
        assert len(updated.project.milestones) == 2
        assert len(updated.project.assignments) == 2
        assert len(updated.project.references) == 2

        persisted_after_add = stack.get.execute(GetProjectRequest(project_id=project_id))
        assert len(persisted_after_add.project.activities) == 2
        assert len(persisted_after_add.project.milestones) == 2
        assert len(persisted_after_add.project.assignments) == 2
        assert len(persisted_after_add.project.references) == 2

        # 8,9) Complete Activities + Complete Milestones
        completed_children = stack.update.execute(
            UpdateProjectRequest(
                project_id=project_id,
                updated_at=_aware_utc(2030, 2, 1, 8),
                activities=tuple(
                    ProjectActivityInput(
                        activity_id=item.activity_id,
                        title=item.title,
                        status="COMPLETED",
                        description=item.description,
                        planned_start=item.planned_start,
                        planned_finish=item.planned_finish,
                        actual_start=item.planned_start,
                        actual_finish=item.planned_finish,
                        priority=item.priority,
                        estimated_hours=item.estimated_hours,
                        actual_hours=item.estimated_hours,
                    )
                    for item in persisted_after_add.project.activities
                ),
                milestones=tuple(
                    ProjectMilestoneInput(
                        milestone_id=item.milestone_id,
                        name=item.name,
                        sequence=item.sequence,
                        status="COMPLETED",
                        description=item.description,
                        due_date=item.due_date,
                        completed_date=_aware_utc(2030, 2, 2 + index, 8),
                    )
                    for index, item in enumerate(persisted_after_add.project.milestones)
                ),
            )
        )

        assert all(item.status == "COMPLETED" for item in completed_children.project.activities)
        assert all(item.status == "COMPLETED" for item in completed_children.project.milestones)

        persisted_completed_children = stack.get.execute(
            GetProjectRequest(project_id=project_id)
        )
        assert all(
            item.status == "COMPLETED"
            for item in persisted_completed_children.project.activities
        )
        assert all(
            item.status == "COMPLETED"
            for item in persisted_completed_children.project.milestones
        )

        # 10) Complete Project
        completed_project = stack.complete.execute(
            CompleteProjectRequest(
                project_id=project_id,
                completed_at=_aware_utc(2030, 2, 10, 8),
            )
        )
        assert completed_project.project.status == "COMPLETED"

        persisted_completed_project = stack.get.execute(GetProjectRequest(project_id=project_id))
        assert persisted_completed_project.project.status == "COMPLETED"

        # 11) Archive Project
        archived = stack.archive.execute(
            ArchiveProjectRequest(
                project_id=project_id,
                archived_at=_aware_utc(2030, 2, 15, 8),
            )
        )
        assert archived.project.status == "ARCHIVED"
        assert archived.project.archived_at == _aware_utc(2030, 2, 15, 8)

        persisted_archived = stack.get.execute(GetProjectRequest(project_id=project_id))
        assert persisted_archived.project.status == "ARCHIVED"
        assert persisted_archived.project.archived_at == _aware_utc(2030, 2, 15, 8)
    finally:
        write_session.close()

    assert project_id is not None

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)

        reopened = stack.get.execute(GetProjectRequest(project_id=project_id))
        assert reopened.project.project_number == "PROJ-E2E-001"
        assert reopened.project.status == "ARCHIVED"
        assert len(reopened.project.activities) == 2
        assert len(reopened.project.milestones) == 2
        assert all(item.status == "COMPLETED" for item in reopened.project.activities)
        assert all(item.status == "COMPLETED" for item in reopened.project.milestones)

        # 12) Delete Project
        deleted = stack.delete.execute(DeleteProjectRequest(project_id=project_id))
        assert deleted.project_id == project_id

        with pytest.raises(BusinessRuleViolation):
            stack.get.execute(GetProjectRequest(project_id=project_id))
    finally:
        read_session.close()


def test_e2e_projects_stack_has_no_inventory_or_procurement_runtime_dependency() -> None:
    module_path = Path(__file__).resolve()
    tree = ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))

    forbidden_prefixes = (
        "mfm.application.features.inventory",
        "mfm.application.features.procurement",
        "mfm.application.inventory",
        "mfm.application.procurement",
        "mfm.infrastructure.persistence.sqlite.sqlite_inventory_repository",
        "mfm.infrastructure.persistence.sqlite.sqlite_purchase_order_repository",
        "mfm.repositories.inventory_repository",
        "mfm.repositories.purchase_order_repository",
    )

    violations: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            imports = [node.module or ""]
        else:
            continue

        for imported in imports:
            if any(
                imported == prefix or imported.startswith(f"{prefix}.")
                for prefix in forbidden_prefixes
            ):
                violations.append(imported)

    assert not violations, f"forbidden cross-capability runtime imports: {violations}"
