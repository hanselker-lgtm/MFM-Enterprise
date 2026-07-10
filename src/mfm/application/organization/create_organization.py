"""Create Organization use case."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_type import OrganizationType


class ApplicationException(Exception):
    """Base exception for organization application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


@dataclass(frozen=True, slots=True)
class CreateOrganizationRequest:
    organization_number: str
    name: str
    organization_type: OrganizationType

    def validate(self) -> None:
        if not isinstance(self.organization_number, str) or not self.organization_number.strip():
            raise ValidationException("organization_number must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.organization_type, OrganizationType):
            raise ValidationException("organization_type must be OrganizationType")


@dataclass(frozen=True, slots=True)
class CreateOrganizationResponse:
    organization_id: UUID
    organization_number: str
    name: str


@dataclass(slots=True)
class OrganizationCreatedEvent(DomainEvent):
    organization_id: UUID = field(default_factory=uuid4)
    organization_number: str = ""


class OrganizationRepository(Protocol):
    def add(self, organization: Organization) -> None: ...

    def search(self, text: str) -> list[Organization]: ...


class CreateOrganizationUseCase:
    """Create organization aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: CreateOrganizationRequest) -> CreateOrganizationResponse:
        request.validate()

        number = OrganizationNumber(request.organization_number)
        name = request.name.strip()

        try:
            with self._unit_of_work as uow:
                repository: OrganizationRepository = uow.organization_repository

                for existing in repository.search(number.value):
                    if existing.organization_number.value == number.value:
                        raise BusinessRuleViolation(
                            f"Organization number {number.value} already exists"
                        )

                organization = Organization(
                    organization_number=number,
                    name=name,
                    organization_type=request.organization_type,
                )

                repository.add(organization)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Create organization failed") from exc

        self._dispatcher.dispatch(
            OrganizationCreatedEvent(
                organization_id=organization.id.value,
                organization_number=organization.organization_number.value,
            )
        )

        return CreateOrganizationResponse(
            organization_id=organization.id.value,
            organization_number=organization.organization_number.value,
            name=organization.name,
        )
