from __future__ import annotations

from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import UUID

import pytest

from mfm.domain.projects.events import ProjectArchived
from mfm.domain.projects.events import ProjectCreated
from mfm.domain.projects.events import ProjectStatusChanged
from mfm.domain.projects.events import ProjectUpdated
from mfm.domain.projects.exceptions import InvalidProjectError
from mfm.domain.projects.exceptions import InvalidProjectStateError
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.domain.projects.project_status import ProjectStatus


def _dt(year: int, month: int, day: int, hour: int = 8, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _project(
    *,
    status: ProjectStatus = ProjectStatus.DRAFT,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
) -> Project:
    return Project(
        project_number=ProjectNumber("PROJ-001"),
        project_name=ProjectName("Hull restoration"),
        status=status,
        priority=ProjectPriority.NORMAL,
        start_date=start_date,
        end_date=end_date,
    )


def test_project_creation_normalizes_and_emits_created_event() -> None:
    project = _project()
    events = project.pull_events()

    assert project.project_number.value == "PROJ-001"
    assert project.project_name.value == "Hull restoration"
    assert project.status is ProjectStatus.DRAFT
    assert project.created_at is not None
    assert project.created_at.tzinfo is UTC
    assert any(isinstance(event, ProjectCreated) for event in events)


def test_project_rejects_naive_datetime_values() -> None:
    with pytest.raises(InvalidProjectError):
        _project(start_date=datetime(2027, 1, 1, 8, 0))


def test_project_rejects_start_after_end() -> None:
    with pytest.raises(InvalidProjectError):
        _project(
            start_date=_dt(2027, 1, 2, 8),
            end_date=_dt(2027, 1, 1, 8),
        )


def test_project_archived_status_requires_archived_at() -> None:
    with pytest.raises(InvalidProjectStateError):
        _project(status=ProjectStatus.ARCHIVED)


def test_update_details_updates_fields_and_emits_updated_event() -> None:
    project = _project()
    project.pull_events()

    project.update_details(
        project_name="Boiler overhaul",
        description="Class inspection prep",
        priority=ProjectPriority.HIGH,
        start_date=_dt(2027, 2, 1, 9),
        end_date=_dt(2027, 2, 20, 16),
    )
    events = project.pull_events()

    assert project.project_name.value == "Boiler overhaul"
    assert project.description == "Class inspection prep"
    assert project.priority is ProjectPriority.HIGH
    assert project.updated_at is not None
    assert any(isinstance(event, ProjectUpdated) for event in events)


def test_update_details_rejects_invalid_chronology() -> None:
    project = _project()

    with pytest.raises(InvalidProjectError):
        project.update_details(
            start_date=_dt(2027, 3, 10),
            end_date=_dt(2027, 3, 1),
        )


def test_change_status_emits_status_changed_event() -> None:
    project = _project()
    project.pull_events()

    project.change_status(ProjectStatus.PLANNED, when=_dt(2027, 2, 1))
    events = project.pull_events()

    assert project.status is ProjectStatus.PLANNED
    status_events = [event for event in events if isinstance(event, ProjectStatusChanged)]
    assert len(status_events) == 1
    assert status_events[0].previous_status == "DRAFT"
    assert status_events[0].new_status == "PLANNED"


def test_change_status_to_archived_emits_archived_event_and_sets_timestamp() -> None:
    project = _project(status=ProjectStatus.PLANNED)
    project.pull_events()

    archived_at = _dt(2027, 3, 1, 11)
    project.change_status(ProjectStatus.ARCHIVED, when=archived_at)
    events = project.pull_events()

    assert project.status is ProjectStatus.ARCHIVED
    assert project.archived_at == archived_at
    archived_events = [event for event in events if isinstance(event, ProjectArchived)]
    assert len(archived_events) == 1
    assert archived_events[0].archived_at == archived_at


def test_change_status_rejects_invalid_transition() -> None:
    project = _project(status=ProjectStatus.DRAFT)

    with pytest.raises(InvalidProjectStateError):
        project.change_status(ProjectStatus.COMPLETED)


def test_projects_domain_has_no_infrastructure_or_sqlalchemy_imports() -> None:
    projects_dir = Path("src/mfm/domain/projects")
    forbidden_markers = (
        "sqlalchemy",
        "mfm.infrastructure",
        "mfm.database",
    )

    python_files = sorted(projects_dir.glob("*.py"))
    assert python_files, "expected projects domain python files"

    for file_path in python_files:
        content = file_path.read_text(encoding="utf-8").lower()
        for marker in forbidden_markers:
            assert marker not in content, f"forbidden marker '{marker}' found in {file_path}"


def test_project_repository_contract_methods_match_project_aggregate_scope() -> None:
    methods = {
        name
        for name, value in ProjectRepository.__dict__.items()
        if callable(value) and not name.startswith("_")
    }

    expected_methods = {
        "add",
        "update",
        "remove",
        "get",
        "exists",
        "get_by_number",
        "list",
        "search",
        "next_identity",
        "list_by_status",
    }

    assert expected_methods.issubset(methods)


def test_project_id_is_uuid_backed_identity() -> None:
    project = _project()

    assert isinstance(project.id.value, UUID)
