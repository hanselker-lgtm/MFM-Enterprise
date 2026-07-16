"""Complete Project use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import BusinessRuleViolation
from mfm.application.projects.create_project import ProjectResponse
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import ValidationException
from mfm.application.projects.create_project import to_project_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.exceptions import ProjectError
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.domain.projects.project_status import ProjectStatus


@dataclass(frozen=True, slots=True)
class CompleteProjectRequest:
    project_id: UUID
    completed_at: datetime

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.completed_at, datetime):
            raise ValidationException("completed_at must be datetime")


@dataclass(frozen=True, slots=True)
class CompleteProjectResponse:
    project: ProjectResponse


class CompleteProjectUseCase:
    """Transition project lifecycle state to COMPLETED."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CompleteProjectRequest) -> CompleteProjectResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                project = repository.get(ProjectId(request.project_id))
                if project is None:
                    raise BusinessRuleViolation(
                        f"Project {request.project_id} does not exist"
                    )

                project.change_status(ProjectStatus.COMPLETED, when=request.completed_at)
                repository.update(project)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProjectError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete project failed") from exc

        return CompleteProjectResponse(project=to_project_response(project))
