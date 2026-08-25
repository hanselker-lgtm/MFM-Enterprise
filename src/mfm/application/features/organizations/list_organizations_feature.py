"""ListOrganizationsFeature: list all registered organizations."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.organizations.get_organization_feature import (
    ApplicationException,
    OrganizationDTO,
    RepositoryException,
    _to_dto,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


@dataclass(frozen=True, slots=True)
class ListOrganizationsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListOrganizationsResponse:
    organizations: tuple[OrganizationDTO, ...]


class ListOrganizationsFeature:
    """Public application entry point for listing organizations."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListOrganizationsRequest) -> ListOrganizationsResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                organizations = uow.organization_repository.list()
                dtos = tuple(_to_dto(org) for org in organizations)
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List organizations feature failed") from exc

        return ListOrganizationsResponse(organizations=dtos)
