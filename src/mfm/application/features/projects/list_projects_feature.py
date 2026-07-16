"""List projects feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.features.projects.create_project_feature import (
    ProjectResponse,
)
from mfm.application.features.projects.create_project_feature import (
    RepositoryException,
)
from mfm.application.features.projects.create_project_feature import (
    to_feature_project_response,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.list_projects import ListProjectsRequest as ServiceRequest
from mfm.application.projects.list_projects import ListProjectsResponse as ServiceResponse


@dataclass(frozen=True, slots=True)
class ListProjectsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListProjectsResponse:
    projects: tuple[ProjectResponse, ...]


class ListProjectsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListProjectsFeature:
    """Feature facade for project listing."""

    def __init__(self, *, service: ListProjectsService) -> None:
        self._service = service

    def execute(self, request: ListProjectsRequest) -> ListProjectsResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List projects feature failed") from exc

        return ListProjectsResponse(
            projects=tuple(
                to_feature_project_response(item)
                for item in service_response.projects
            )
        )
