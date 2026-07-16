from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from pathlib import Path
import weakref
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.projects.external_reference import ExternalReference
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_activity import ProjectActivity
from mfm.domain.projects.project_assignment import ProjectAssignment
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_milestone import ProjectMilestone
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_status import ProjectStatus
from mfm.domain.projects.reference_type import ReferenceType
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def _aware(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int = 0,
    *,
    offset_hours: int = 0,
) -> datetime:
    local_tz = timezone(timedelta(hours=offset_hours))
    return datetime(year, month, day, hour, minute, tzinfo=local_tz)


def _project(*, project_id: UUID, number: str, status: ProjectStatus = ProjectStatus.PLANNED) -> Project:
    archived_at = (
        _aware(2030, 4, 1, 12, 0, offset_hours=1)
        if status is ProjectStatus.ARCHIVED
        else None
    )
    project = Project(
        id=ProjectId(project_id),
        project_number=ProjectNumber(number),
        project_name=ProjectName("Dock rehabilitation"),
        status=status,
        priority=ProjectPriority.HIGH,
        description="Rebuild and classify drydock systems",
        start_date=_aware(2030, 1, 10, 8, 0, offset_hours=1),
        end_date=_aware(2030, 3, 10, 16, 0, offset_hours=1),
        created_at=_aware(2030, 1, 1, 9, 0, offset_hours=1),
        updated_at=_aware(2030, 1, 5, 10, 0, offset_hours=1),
        archived_at=archived_at,
        milestones=[
            ProjectMilestone(
                id=uuid4(),
                name="Design approved",
                sequence=1,
                status="COMPLETED",
                due_date=_aware(2030, 1, 15, 12, 0, offset_hours=1),
                completed_date=_aware(2030, 1, 14, 13, 0, offset_hours=1),
            )
        ],
        activities=[
            ProjectActivity(
                id=uuid4(),
                title="Prepare civil works",
                status="ACTIVE",
                priority=ProjectPriority.URGENT,
                estimated_hours=Decimal("42.50"),
                actual_hours=Decimal("10.25"),
                planned_start=_aware(2030, 1, 16, 8, 0, offset_hours=1),
                planned_finish=_aware(2030, 2, 1, 17, 0, offset_hours=1),
                actual_start=_aware(2030, 1, 16, 8, 30, offset_hours=1),
            )
        ],
        assignments=[
            ProjectAssignment(
                id=uuid4(),
                organisation_id=UUID("00000000-0000-0000-0000-00000000BB11"),
                contact_id=UUID("00000000-0000-0000-0000-00000000BB21"),
                role="Project Manager",
                assigned_from=_aware(2030, 1, 2, 8, 0, offset_hours=1),
                assigned_until=_aware(2030, 4, 1, 17, 0, offset_hours=1),
            )
        ],
        references=[
            ExternalReference(
                id=uuid4(),
                reference_type=ReferenceType.PURCHASE_ORDER,
                external_id=UUID("00000000-0000-0000-0000-00000000BB31"),
                description="Main procurement package",
                created_at=_aware(2030, 1, 3, 9, 0, offset_hours=1),
            )
        ],
    )
    project.version = 1
    project.pull_events()
    return project


def test_project_repository_create_read_and_missing(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-add-get.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C001"),
            number="PROJ-REPO-001",
        )

        repository.add(project)
        session.commit()

        loaded = repository.get(project.id)
        assert loaded is not None
        assert loaded.id == project.id
        assert loaded.project_number.value == "PROJ-REPO-001"
        assert loaded.project_name.value == "Dock rehabilitation"

        missing = repository.get(ProjectId(UUID("00000000-0000-0000-0000-00000000C999")))
        assert missing is None
    finally:
        session.close()


def test_project_repository_exists_and_next_identity(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-exists.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C002"),
            number="PROJ-REPO-002",
        )

        repository.add(project)
        session.commit()

        assert repository.exists(project.id) is True
        assert (
            repository.exists(ProjectId(UUID("00000000-0000-0000-0000-00000000C998")))
            is False
        )
        assert isinstance(repository.next_identity(), ProjectId)
    finally:
        session.close()


def test_project_repository_update_persists_aggregate_roundtrip(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-update.sqlite"
    first_session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(first_session))
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C003"),
            number="PROJ-REPO-003",
        )

        repository.add(project)
        first_session.commit()

        loaded = repository.get(project.id)
        assert loaded is not None
        loaded.update_details(
            project_name="Dock rehabilitation phase 2",
            description="Updated plan",
            priority=ProjectPriority.URGENT,
            updated_at=_aware(2030, 1, 20, 8, 0, offset_hours=1),
        )
        loaded.activities.append(
            ProjectActivity(
                id=UUID("00000000-0000-0000-0000-00000000AA22"),
                title="Mechanical fit-out",
                status="PLANNED",
                priority=ProjectPriority.HIGH,
                estimated_hours=Decimal("80.00"),
            )
        )

        repository.update(loaded)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(second_session))
        restored = repository.get(ProjectId(UUID("00000000-0000-0000-0000-00000000C003")))

        assert restored is not None
        assert restored.project_name.value == "Dock rehabilitation phase 2"
        assert restored.description == "Updated plan"
        assert restored.priority is ProjectPriority.URGENT
        assert len(restored.activities) == 2
        assert restored.activities[1].title == "Mechanical fit-out"
        assert restored.version == 2
        assert restored.created_at is not None and restored.created_at.tzinfo is UTC
    finally:
        second_session.close()


def test_project_repository_remove_and_notfound_handling(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-remove.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C004"),
            number="PROJ-REPO-004",
        )
        repository.add(project)
        session.commit()

        repository.remove(project.id)
        session.commit()

        assert repository.get(project.id) is None

        with pytest.raises(ValueError):
            repository.remove(project.id)
    finally:
        session.close()


def test_project_repository_list_and_status_filter(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-list.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))

        planned = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C005"),
            number="PROJ-REPO-A",
            status=ProjectStatus.PLANNED,
        )
        active = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C006"),
            number="PROJ-REPO-B",
            status=ProjectStatus.ACTIVE,
        )
        archived = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C007"),
            number="PROJ-REPO-C",
            status=ProjectStatus.ARCHIVED,
        )

        for entity in (active, archived, planned):
            repository.add(entity)
        session.commit()

        listed = repository.list()
        assert [item.project_number.value for item in listed] == [
            "PROJ-REPO-A",
            "PROJ-REPO-B",
            "PROJ-REPO-C",
        ]

        active_only = repository.list(filters={"status": "ACTIVE"})
        assert [item.project_number.value for item in active_only] == ["PROJ-REPO-B"]

        archived_only = repository.list_by_status(ProjectStatus.ARCHIVED)
        assert [item.project_number.value for item in archived_only] == ["PROJ-REPO-C"]
    finally:
        session.close()


def test_project_repository_search_returns_projections(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-search.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))

        first = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C008"),
            number="PROJ-SEARCH-001",
            status=ProjectStatus.PLANNED,
        )
        second = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C009"),
            number="PROJ-SEARCH-002",
            status=ProjectStatus.ACTIVE,
        )
        second.references.append(
            ExternalReference(
                reference_type=ReferenceType.DOCUMENT,
                external_id=UUID("00000000-0000-0000-0000-00000000BB51"),
                description="Design dossier",
                created_at=_aware(2030, 1, 7, 9, 0, offset_hours=1),
            )
        )

        repository.add(first)
        repository.add(second)
        session.commit()

        text_hits = repository.search("SEARCH-001")
        assert len(text_hits) == 1
        assert text_hits[0]["project_number"] == "PROJ-SEARCH-001"

        active_hits = repository.search({"status": "ACTIVE"})
        assert [row["project_number"] for row in active_hits] == ["PROJ-SEARCH-002"]

        ref_hits = repository.search({"reference_type": "DOCUMENT"})
        assert [row["project_number"] for row in ref_hits] == ["PROJ-SEARCH-002"]
    finally:
        session.close()


def test_project_repository_duplicate_and_notfound_and_version_conflict(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-errors.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(session))
        first = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C010"),
            number="PROJ-REPO-DUP",
        )
        duplicate = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C011"),
            number="PROJ-REPO-DUP",
        )

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(duplicate)

        missing = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C012"),
            number="PROJ-REPO-MISSING",
        )
        with pytest.raises(ValueError):
            repository.update(missing)

        stale = repository.get(first.id)
        assert stale is not None
        stale.version = 0
        with pytest.raises(ValueError):
            repository.update(stale)
    finally:
        session.close()


def test_project_repository_defers_commit_to_unit_of_work(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-project-repository-rollback.sqlite"
    first_session = _new_session(db_path)
    try:
        uow = UnitOfWork(first_session)
        repository = SQLiteProjectRepository(uow)
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000C013"),
            number="PROJ-REPO-ROLLBACK",
        )

        repository.add(project)
        uow.rollback()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteProjectRepository(UnitOfWork(second_session))
        assert repository.get(ProjectId(UUID("00000000-0000-0000-0000-00000000C013"))) is None
    finally:
        second_session.close()
