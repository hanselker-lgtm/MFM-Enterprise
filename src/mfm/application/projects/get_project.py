"""Get Project use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import BusinessRuleViolation
from mfm.application.projects.create_project import ProjectResponse
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import ValidationException
from mfm.application.projects.create_project import to_project_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_repository import ProjectRepository


@dataclass(frozen=True, slots=True)
class GetProjectRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetProjectResponse:
    project: ProjectResponse


class GetProjectUseCase:
    """Load one project through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetProjectRequest) -> GetProjectResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                project = repository.get(ProjectId(request.project_id))
                if project is None:
                    raise BusinessRuleViolation(
                        f"Project {request.project_id} does not exist"
                    )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get project failed") from exc

        return GetProjectResponse(project=to_project_response(project))
