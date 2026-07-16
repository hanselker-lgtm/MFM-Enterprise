"""Search Projects use case."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import ProjectSearchResultResponse
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import ValidationException
from mfm.application.projects.create_project import to_project_search_result_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.project_repository import ProjectRepository


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


class SearchProjectsUseCase:
    """Search projects through repository projection queries."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: SearchProjectsRequest) -> SearchProjectsResponse:
        request.validate()

        criteria: dict[str, Any] = {}
        if request.text is not None:
            criteria["text"] = request.text.strip()
        if request.status is not None:
            criteria["status"] = request.status.strip()
        if request.reference_type is not None:
            criteria["reference_type"] = request.reference_type.strip()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                rows = repository.search(criteria)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Search projects failed") from exc

        return SearchProjectsResponse(
            projects=tuple(
                to_project_search_result_response(row)
                for row in rows
            )
        )
