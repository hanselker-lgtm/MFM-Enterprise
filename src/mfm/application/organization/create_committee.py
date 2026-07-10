"""Create Committee use case."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.organization.create_organization import BusinessRuleViolation
from mfm.application.organization.create_organization import RepositoryException
from mfm.application.organization.create_organization import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId


@dataclass(frozen=True, slots=True)
class CommitteeMemberInput:
    reference_id: UUID
    function_title: str
    joined_at: date
    left_at: date | None = None


@dataclass(frozen=True, slots=True)
class CreateCommitteeRequest:
    organization_id: UUID
    name: str
    purpose: str
    members: tuple[CommitteeMemberInput, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.purpose, str):
            raise ValidationException("purpose must be a string")
        if not isinstance(self.members, tuple):
            raise ValidationException("members must be a tuple")


@dataclass(frozen=True, slots=True)
class CreateCommitteeResponse:
    committee_id: UUID
    organization_id: UUID
    name: str


@dataclass(slots=True)
class CommitteeCreatedEvent(DomainEvent):
    committee_id: UUID = field(default_factory=uuid4)
    organization_id: UUID = field(default_factory=uuid4)


class OrganizationRepository(Protocol):
    def get_by_id(self, organization_id: UUID) -> Organization | None: ...


class CommitteeRepository(Protocol):
    def add(self, committee: Committee) -> None: ...

    def search(self, text: str) -> list[Committee]: ...


class CreateCommitteeUseCase:
    """Create committee aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: CreateCommitteeRequest) -> CreateCommitteeResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                organization_repository: OrganizationRepository = uow.organization_repository
                committee_repository: CommitteeRepository = uow.committee_repository

                organization = organization_repository.get_by_id(request.organization_id)
                if organization is None:
                    raise BusinessRuleViolation(
                        f"Organization {request.organization_id} does not exist"
                    )

                for existing in committee_repository.search(request.name.strip()):
                    if (
                        existing.organization_id.value == request.organization_id
                        and existing.name.casefold() == request.name.strip().casefold()
                    ):
                        raise BusinessRuleViolation("Committee already exists for organization")

                committee = Committee(
                    organization_id=OrganizationId(request.organization_id),
                    name=request.name,
                    purpose=request.purpose,
                    members=[
                        CommitteeMember(
                            reference_id=member.reference_id,
                            function_title=member.function_title,
                            joined_at=member.joined_at,
                            left_at=member.left_at,
                        )
                        for member in request.members
                    ],
                )
                committee_repository.add(committee)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Create committee failed") from exc

        self._dispatcher.dispatch(
            CommitteeCreatedEvent(
                committee_id=committee.id.value,
                organization_id=request.organization_id,
            )
        )

        return CreateCommitteeResponse(
            committee_id=committee.id.value,
            organization_id=request.organization_id,
            name=committee.name,
        )
