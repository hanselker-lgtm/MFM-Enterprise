from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from mfm.database.mappers.project_mapper import ProjectMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.project_model import ProjectModel
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


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    connection = engine.connect()
    BaseModel.metadata.create_all(connection)
    session = Session(bind=connection)
    session.info["test_connection"] = connection
    session.info["test_engine"] = engine
    return session


def _close_session(session: Session) -> None:
    connection = session.info.pop("test_connection", None)
    engine = session.info.pop("test_engine", None)
    session.close()
    if isinstance(connection, Connection):
        connection.close()
    if isinstance(engine, Engine):
        engine.dispose()


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


def _project(*, project_id: UUID, number: str) -> Project:
    project = Project(
        id=ProjectId(project_id),
        project_number=ProjectNumber(number),
        project_name=ProjectName("Engine overhaul"),
        status=ProjectStatus.PLANNED,
        priority=ProjectPriority.HIGH,
        description="Drydock planning and execution",
        start_date=_aware(2029, 1, 10, 8, 30, offset_hours=1),
        end_date=_aware(2029, 2, 10, 16, 0, offset_hours=1),
        created_at=_aware(2029, 1, 1, 9, 0, offset_hours=1),
        updated_at=_aware(2029, 1, 5, 10, 15, offset_hours=1),
        milestones=[
            ProjectMilestone(
                id=UUID("00000000-0000-0000-0000-00000000E101"),
                name="Docking approved",
                sequence=1,
                status="COMPLETED",
                due_date=_aware(2029, 1, 5, 12, 0, offset_hours=1),
                completed_date=_aware(2029, 1, 4, 14, 0, offset_hours=1),
            )
        ],
        activities=[
            ProjectActivity(
                id=UUID("00000000-0000-0000-0000-00000000E201"),
                title="Prepare drydock",
                status="ACTIVE",
                priority=ProjectPriority.URGENT,
                estimated_hours=Decimal("12.50"),
                actual_hours=Decimal("3.75"),
                planned_start=_aware(2029, 1, 6, 8, 0, offset_hours=1),
                planned_finish=_aware(2029, 1, 7, 17, 0, offset_hours=1),
                actual_start=_aware(2029, 1, 6, 8, 30, offset_hours=1),
            )
        ],
        assignments=[
            ProjectAssignment(
                id=UUID("00000000-0000-0000-0000-00000000E301"),
                organisation_id=UUID("00000000-0000-0000-0000-00000000F101"),
                contact_id=UUID("00000000-0000-0000-0000-00000000F201"),
                role="Project Manager",
                assigned_from=_aware(2029, 1, 2, 8, 0, offset_hours=1),
                assigned_until=_aware(2029, 3, 1, 17, 0, offset_hours=1),
            )
        ],
        references=[
            ExternalReference(
                id=UUID("00000000-0000-0000-0000-00000000E401"),
                reference_type=ReferenceType.PURCHASE_ORDER,
                external_id=UUID("00000000-0000-0000-0000-00000000F301"),
                description="Primary PO",
                created_at=_aware(2029, 1, 3, 9, 30, offset_hours=1),
            )
        ],
    )
    project.version = 3
    project.pull_events()
    return project


def _persist_and_reload(session: Session, project: Project) -> Project:
    orm = ProjectMapper.to_orm_project(project)
    session.add(orm)
    session.commit()
    session.expunge_all()

    loaded = session.get(ProjectModel, project.id.value)
    assert loaded is not None
    return ProjectMapper.to_domain_project(loaded)


def test_project_roundtrip_preserves_header_fields(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-roundtrip-header")
    try:
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000E001"),
            number="PROJ-2029-001",
        )

        restored = _persist_and_reload(session, project)

        assert restored.id == project.id
        assert restored.project_number == project.project_number
        assert restored.project_name == project.project_name
        assert restored.status is ProjectStatus.PLANNED
        assert restored.priority is ProjectPriority.HIGH
        assert restored.description == "Drydock planning and execution"
        assert restored.version == 3
    finally:
        _close_session(session)


def test_project_roundtrip_preserves_children_and_order(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-roundtrip-children")
    try:
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000E002"),
            number="PROJ-2029-002",
        )

        project.activities.append(
            ProjectActivity(
                id=UUID("00000000-0000-0000-0000-00000000E202"),
                title="Inspection report",
                status="PLANNED",
                priority=ProjectPriority.NORMAL,
            )
        )

        restored = _persist_and_reload(session, project)

        assert len(restored.milestones) == 1
        assert restored.milestones[0].sequence == 1
        assert len(restored.activities) == 2
        assert restored.activities[0].title == "Prepare drydock"
        assert restored.activities[1].title == "Inspection report"
        assert len(restored.assignments) == 1
        assert restored.assignments[0].role == "Project Manager"
        assert len(restored.references) == 1
        assert restored.references[0].reference_type is ReferenceType.PURCHASE_ORDER
    finally:
        _close_session(session)


def test_project_archived_roundtrip_preserves_status_and_timestamp(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-roundtrip-archived")
    try:
        archived_at = _aware(2029, 3, 10, 15, 0, offset_hours=1)
        project = Project(
            id=ProjectId(UUID("00000000-0000-0000-0000-00000000E003")),
            project_number=ProjectNumber("PROJ-2029-003"),
            project_name=ProjectName("Archive project"),
            status=ProjectStatus.ARCHIVED,
            priority=ProjectPriority.LOW,
            created_at=_aware(2029, 1, 1, 8, 0, offset_hours=1),
            archived_at=archived_at,
        )
        project.pull_events()

        restored = _persist_and_reload(session, project)

        assert restored.status is ProjectStatus.ARCHIVED
        assert restored.archived_at is not None
        assert restored.archived_at.tzinfo is UTC
    finally:
        _close_session(session)


def test_mapper_restoration_emits_no_false_domain_events(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-restoration-events")
    try:
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000E004"),
            number="PROJ-2029-004",
        )

        restored = _persist_and_reload(session, project)

        assert restored.pull_events() == []
    finally:
        _close_session(session)


def test_timezone_roundtrip_normalizes_header_to_utc(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-timezone")
    try:
        project = _project(
            project_id=UUID("00000000-0000-0000-0000-00000000E005"),
            number="PROJ-2029-005",
        )

        restored = _persist_and_reload(session, project)

        assert restored.created_at is not None
        assert restored.created_at.tzinfo is UTC
        assert restored.start_date is not None
        assert restored.start_date.tzinfo is UTC
        assert restored.updated_at is not None
        assert restored.updated_at.tzinfo is UTC
    finally:
        _close_session(session)


def test_project_metadata_registers_all_project_tables(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "project-metadata")
    try:
        inspector = inspect(session.info["test_connection"])
        tables = set(inspector.get_table_names())

        assert "project" in tables
        assert "project_milestone" in tables
        assert "project_activity" in tables
        assert "project_assignment" in tables
        assert "project_reference" in tables
    finally:
        _close_session(session)


def test_invalid_persistence_state_unknown_status_fails_restore() -> None:
    orm = ProjectModel(
        id=UUID("00000000-0000-0000-0000-00000000E006"),
        project_number="PROJ-2029-006",
        project_name="Invalid status",
        status="UNKNOWN",  # type: ignore[arg-type]
        priority=ProjectPriority.NORMAL,
        project_created_at=_aware(2029, 1, 1, 9, 0),
        version=1,
    )

    with pytest.raises((ValueError, TypeError)):
        ProjectMapper.to_domain_project(orm)
