"""Delete Project use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import BusinessRuleViolation
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_repository import ProjectRepository


@dataclass(frozen=True, slots=True)
class DeleteProjectRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


@dataclass(frozen=True, slots=True)
class DeleteProjectResponse:
    project_id: UUID


class DeleteProjectUseCase:
    """Delete one project aggregate by identifier."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: DeleteProjectRequest) -> DeleteProjectResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                project_id = ProjectId(request.project_id)
                project = repository.get(project_id)
                if project is None:
                    raise BusinessRuleViolation(
                        f"Project {request.project_id} does not exist"
                    )

                repository.remove(project_id)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Delete project failed") from exc

        return DeleteProjectResponse(project_id=request.project_id)
