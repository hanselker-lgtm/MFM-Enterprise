"""List Projects use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import ProjectResponse
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import to_project_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.project_repository import ProjectRepository


@dataclass(frozen=True, slots=True)
class ListProjectsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListProjectsResponse:
    projects: tuple[ProjectResponse, ...]


class ListProjectsUseCase:
    """List projects with repository-provided deterministic ordering."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListProjectsRequest) -> ListProjectsResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                projects = repository.list()
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List projects failed") from exc

        return ListProjectsResponse(
            projects=tuple(to_project_response(item) for item in projects)
        )
