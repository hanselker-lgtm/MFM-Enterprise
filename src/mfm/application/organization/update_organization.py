"""Update Organization use case."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.organization.create_organization import ApplicationException
from mfm.application.organization.create_organization import BusinessRuleViolation
from mfm.application.organization.create_organization import RepositoryException
from mfm.application.organization.create_organization import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@dataclass(frozen=True, slots=True)
class UpdateOrganizationRequest:
    organization_id: UUID
    organization_number: str | None = None
    name: str | None = None
    organization_type: OrganizationType | None = None
    status: OrganizationStatus | None = None

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if self.organization_number is not None and not self.organization_number.strip():
            raise ValidationException("organization_number cannot be empty")
        if self.name is not None and not self.name.strip():
            raise ValidationException("name cannot be empty")
        if self.organization_type is not None and not isinstance(self.organization_type, OrganizationType):
            raise ValidationException("organization_type must be OrganizationType")
        if self.status is not None and not isinstance(self.status, OrganizationStatus):
            raise ValidationException("status must be OrganizationStatus")


@dataclass(frozen=True, slots=True)
class UpdateOrganizationResponse:
    organization_id: UUID
    organization_number: str
    name: str
    status: OrganizationStatus


@dataclass(slots=True)
class OrganizationUpdatedEvent(DomainEvent):
    organization_id: UUID = field(default_factory=uuid4)


class OrganizationRepository(Protocol):
    def get_by_id(self, organization_id: UUID) -> Organization | None: ...

    def update(self, organization: Organization) -> None: ...

    def search(self, text: str) -> list[Organization]: ...


class UpdateOrganizationUseCase:
    """Update organization aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: UpdateOrganizationRequest) -> UpdateOrganizationResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: OrganizationRepository = uow.organization_repository

                organization = repository.get_by_id(request.organization_id)
                if organization is None:
                    raise BusinessRuleViolation(
                        f"Organization {request.organization_id} does not exist"
                    )

                if request.organization_number is not None:
                    normalized = OrganizationNumber(request.organization_number).value
                    if normalized != organization.organization_number.value:
                        for existing in repository.search(normalized):
                            if (
                                existing.organization_number.value == normalized
                                and existing.id != organization.id
                            ):
                                raise BusinessRuleViolation(
                                    f"Organization number {normalized} already exists"
                                )
                        organization.organization_number = OrganizationNumber(normalized)

                if request.name is not None:
                    organization.rename(request.name)

                if request.organization_type is not None:
                    organization.organization_type = request.organization_type

                if request.status is not None and request.status != organization.status:
                    if request.status is OrganizationStatus.ACTIVE:
                        organization.activate()
                    elif request.status is OrganizationStatus.INACTIVE:
                        organization.deactivate()
                    elif request.status is OrganizationStatus.ARCHIVED:
                        organization.archive()

                repository.update(organization)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Update organization failed") from exc

        self._dispatcher.dispatch(
            OrganizationUpdatedEvent(
                organization_id=organization.id.value,
            )
        )

        return UpdateOrganizationResponse(
            organization_id=organization.id.value,
            organization_number=organization.organization_number.value,
            name=organization.name,
            status=organization.status,
        )
