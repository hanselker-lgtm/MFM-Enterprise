"""GetOrganizationFeature and ListOrganizationsFeature (read-only lookups)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class OrganizationDTO:
    organization_id: UUID
    organization_number: str
    name: str
    organization_type: str
    status: str


@dataclass(frozen=True, slots=True)
class GetOrganizationRequest:
    organization_id: UUID

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetOrganizationResponse:
    organization: OrganizationDTO


def _to_dto(organization) -> OrganizationDTO:
    return OrganizationDTO(
        organization_id=organization.id.value,
        organization_number=organization.organization_number.value,
        name=organization.name,
        organization_type=organization.organization_type.value,
        status=organization.status.value,
    )


class GetOrganizationFeature:
    """Public application entry point for fetching one organization."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetOrganizationRequest) -> GetOrganizationResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                organization = uow.organization_repository.get_by_id(request.organization_id)
                if organization is None:
                    raise ValidationException(
                        f"Organization {request.organization_id} does not exist"
                    )
                dto = _to_dto(organization)
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Get organization feature failed") from exc

        return GetOrganizationResponse(organization=dto)
