"""SQLite repository for Project aggregates."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import cast

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.project_mapper import ProjectMapper
from mfm.database.models.project_model import ProjectModel
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_status import ProjectStatus
from mfm.domain.projects.reference_type import ReferenceType
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectRepository(ProjectRepository):
    """SQLAlchemy-backed repository for Project aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, project: Project) -> None:
        number = project.project_number.value
        if self._session.scalar(
            select(ProjectModel.id).where(ProjectModel.project_number == number)
        ) is not None:
            raise ValueError(f"Project number {number} already exists")

        self._session.add(ProjectMapper.to_orm_project(project))
        self._session.flush()

    def get(self, project_id: ProjectId) -> Project | None:
        normalized_id = self._normalize_project_id(project_id).value
        orm = self._session.scalar(self._base_query().where(ProjectModel.id == normalized_id))
        if orm is None:
            return None
        return ProjectMapper.to_domain_project(orm)

    def update(self, project: Project) -> None:
        existing = self._session.scalar(
            self._base_query().where(ProjectModel.id == project.id.value)
        )
        if existing is None:
            raise ValueError(f"Project {project.id.value} does not exist")

        duplicate = self._session.scalar(
            select(ProjectModel.id).where(
                ProjectModel.project_number == project.project_number.value,
                ProjectModel.id != project.id.value,
            )
        )
        if duplicate is not None:
            raise ValueError(f"Project number {project.project_number.value} already exists")

        if existing.version != project.version:
            raise ValueError(
                f"Project {project.id.value} version conflict: expected {existing.version}, got {project.version}"
            )

        # Replace child collections before merge to avoid stale child rows colliding
        # with unique constraints when ordered child sets are rewritten.
        existing.references.clear()
        self._session.flush()
        existing.activities.clear()
        self._session.flush()
        existing.milestones.clear()
        existing.assignments.clear()
        self._session.flush()

        updated = ProjectMapper.to_orm_project(project)
        updated.version = project.version + 1
        self._session.merge(updated)
        self._session.flush()

    def remove(self, project_id: ProjectId) -> None:
        normalized_id = self._normalize_project_id(project_id).value
        orm = self._session.get(ProjectModel, normalized_id)
        if orm is None:
            raise ValueError(f"Project {normalized_id} does not exist")
        self._session.delete(orm)
        self._session.flush()

    def exists(self, project_id: ProjectId) -> bool:
        normalized_id = self._normalize_project_id(project_id).value
        return self._session.get(ProjectModel, normalized_id) is not None

    def get_by_number(self, project_number: ProjectNumber) -> Project | None:
        normalized = self._normalize_project_number(project_number).value
        orm = self._session.scalar(
            self._base_query().where(ProjectModel.project_number == normalized)
        )
        if orm is None:
            return None
        return ProjectMapper.to_domain_project(orm)

    def list(self, filters: Any | None = None) -> list[Project]:
        query = self._base_query()
        if isinstance(filters, Mapping):
            if "status" in filters and filters["status"] is not None:
                query = query.where(
                    ProjectModel.status == self._normalize_status(filters["status"])
                )

        orm_entities = self._session.scalars(
            query.order_by(ProjectModel.project_number, ProjectModel.project_created_at)
        ).unique().all()
        return [ProjectMapper.to_domain_project(orm) for orm in orm_entities]

    def search(self, criteria: Any) -> list[Any]:
        if isinstance(criteria, str):
            text = criteria.strip()
            filters: dict[str, Any] = {"text": text} if text else {}
        elif isinstance(criteria, Mapping):
            filters = dict(criteria)
        else:
            filters = {}

        query = select(ProjectModel)

        text = str(filters.get("text", "")).strip()
        if text:
            like_pattern = f"%{text}%"
            query = query.where(
                or_(
                    ProjectModel.project_number.ilike(like_pattern),
                    ProjectModel.project_name.ilike(like_pattern),
                    ProjectModel.description.ilike(like_pattern),
                )
            )

        status = filters.get("status")
        if status is not None:
            query = query.where(ProjectModel.status == self._normalize_status(status))

        reference_type = filters.get("reference_type")
        if reference_type is not None:
            normalized_reference_type = (
                reference_type
                if isinstance(reference_type, ReferenceType)
                else ReferenceType(str(reference_type).upper())
            )
            query = query.where(
                ProjectModel.references.any(reference_type=normalized_reference_type)
            )

        entities = self._session.scalars(
            query.order_by(ProjectModel.project_number, ProjectModel.project_created_at)
        ).unique().all()

        return [
            {
                "id": orm.id,
                "project_number": orm.project_number,
                "project_name": orm.project_name,
                "status": orm.status,
                "priority": orm.priority,
            }
            for orm in entities
        ]

    def next_identity(self) -> ProjectId:
        return ProjectId.new()

    def list_by_status(self, status: ProjectStatus) -> list[Project]:
        normalized_status = self._normalize_status(status)
        orm_entities = self._session.scalars(
            self._base_query()
            .where(ProjectModel.status == normalized_status)
            .order_by(ProjectModel.project_number, ProjectModel.project_created_at)
        ).unique().all()
        return [ProjectMapper.to_domain_project(orm) for orm in orm_entities]

    @staticmethod
    def _normalize_project_id(project_id: ProjectId) -> ProjectId:
        if isinstance(project_id, ProjectId):
            return project_id
        return ProjectId(project_id)

    @staticmethod
    def _normalize_project_number(project_number: ProjectNumber | str) -> ProjectNumber:
        if isinstance(project_number, ProjectNumber):
            return project_number
        return ProjectNumber(project_number)

    @staticmethod
    def _normalize_status(status: ProjectStatus | str) -> ProjectStatus:
        if isinstance(status, ProjectStatus):
            return status
        return ProjectStatus(str(status).upper())

    @staticmethod
    def _base_query():
        return select(ProjectModel).options(
            joinedload(ProjectModel.milestones),
            joinedload(ProjectModel.activities),
            joinedload(ProjectModel.assignments),
            joinedload(ProjectModel.references),
        )
