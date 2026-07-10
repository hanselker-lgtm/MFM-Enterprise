"""Register Volunteer use case."""

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
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.volunteer import VolunteerCertificate
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_skill import VolunteerSkill


@dataclass(frozen=True, slots=True)
class VolunteerCertificateInput:
    name: str
    expires_at: date | None = None


@dataclass(frozen=True, slots=True)
class RegisterVolunteerRequest:
    contact_id: UUID
    member_id: UUID | None
    is_available: bool
    max_hours_per_week: int
    preferred_days: tuple[str, ...]
    skills: tuple[str, ...]
    certificates: tuple[VolunteerCertificateInput, ...]
    joined_at: date

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")
        if self.member_id is not None and not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID or None")
        if not isinstance(self.is_available, bool):
            raise ValidationException("is_available must be bool")
        if not isinstance(self.max_hours_per_week, int) or self.max_hours_per_week < 0:
            raise ValidationException("max_hours_per_week must be non-negative integer")
        if not isinstance(self.preferred_days, tuple):
            raise ValidationException("preferred_days must be tuple")
        if not isinstance(self.skills, tuple):
            raise ValidationException("skills must be tuple")
        if not isinstance(self.certificates, tuple):
            raise ValidationException("certificates must be tuple")
        if not isinstance(self.joined_at, date):
            raise ValidationException("joined_at must be date")


@dataclass(frozen=True, slots=True)
class RegisterVolunteerResponse:
    volunteer_id: UUID
    contact_id: UUID


@dataclass(slots=True)
class VolunteerRegisteredEvent(DomainEvent):
    volunteer_id: UUID = field(default_factory=uuid4)
    contact_id: UUID = field(default_factory=uuid4)


class VolunteerRepository(Protocol):
    def add(self, volunteer: Volunteer) -> None: ...

    def list(self) -> list[Volunteer]: ...


class RegisterVolunteerUseCase:
    """Register volunteer aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: RegisterVolunteerRequest) -> RegisterVolunteerResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VolunteerRepository = uow.volunteer_repository

                for existing in repository.list():
                    if existing.contact_id == request.contact_id:
                        raise BusinessRuleViolation(
                            f"Volunteer for contact {request.contact_id} already exists"
                        )

                volunteer = Volunteer(
                    contact_id=request.contact_id,
                    member_id=request.member_id,
                    availability=VolunteerAvailability(
                        is_available=request.is_available,
                        max_hours_per_week=request.max_hours_per_week,
                        preferred_days=request.preferred_days,
                    ),
                    skills=[VolunteerSkill(name) for name in request.skills],
                    certificates=[
                        VolunteerCertificate(
                            name=certificate.name,
                            expires_at=certificate.expires_at,
                        )
                        for certificate in request.certificates
                    ],
                    joined_at=request.joined_at,
                )

                repository.add(volunteer)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Register volunteer failed") from exc

        self._dispatcher.dispatch(
            VolunteerRegisteredEvent(
                volunteer_id=volunteer.id.value,
                contact_id=volunteer.contact_id,
            )
        )

        return RegisterVolunteerResponse(
            volunteer_id=volunteer.id.value,
            contact_id=volunteer.contact_id,
        )
