"""Search projects feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.features.projects.create_project_feature import (
    ProjectSearchResultResponse,
)
from mfm.application.features.projects.create_project_feature import (
    RepositoryException,
)
from mfm.application.features.projects.create_project_feature import (
    ValidationException,
)
from mfm.application.features.projects.create_project_feature import (
    to_feature_project_search_result_response,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)
from mfm.application.projects.search_projects import SearchProjectsRequest as ServiceRequest
from mfm.application.projects.search_projects import SearchProjectsResponse as ServiceResponse


@dataclass(frozen=True, slots=True)
class SearchProjectsRequest:
    text: str | None = None
    status: str | None = None
    reference_type: str | None = None

    def validate(self) -> None:
        for field_name, value in (
            ("text", self.text),
            ("status", self.status),
            ("reference_type", self.reference_type),
        ):
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValidationException(f"{field_name} must be string or None")
            if not value.strip():
                raise ValidationException(
                    f"{field_name} must be non-empty when provided"
                )


@dataclass(frozen=True, slots=True)
class SearchProjectsResponse:
    projects: tuple[ProjectSearchResultResponse, ...]


class SearchProjectsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class SearchProjectsFeature:
    """Feature facade for project search."""

    def __init__(self, *, service: SearchProjectsService) -> None:
        self._service = service

    def execute(self, request: SearchProjectsRequest) -> SearchProjectsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    text=request.text,
                    status=request.status,
                    reference_type=request.reference_type,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Search projects feature failed") from exc

        return SearchProjectsResponse(
            projects=tuple(
                to_feature_project_search_result_response(item)
                for item in service_response.projects
            )
        )
