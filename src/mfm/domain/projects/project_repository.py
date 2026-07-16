"""Repository contract for projects."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any

from mfm.domain.projects.project import Project
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_status import ProjectStatus


class ProjectRepository(ABC):
    """Repository contract for persisting Project aggregates."""

    @abstractmethod
    def add(self, project: Project) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, project: Project) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, project_id: ProjectId) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, project_id: ProjectId) -> Project | None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, project_id: ProjectId) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_number(self, project_number: ProjectNumber) -> Project | None:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: Any | None = None) -> list[Project]:
        raise NotImplementedError

    @abstractmethod
    def search(self, criteria: Any) -> list[Any]:
        raise NotImplementedError

    @abstractmethod
    def next_identity(self) -> ProjectId:
        raise NotImplementedError

    @abstractmethod
    def list_by_status(self, status: ProjectStatus) -> list[Project]:
        raise NotImplementedError
