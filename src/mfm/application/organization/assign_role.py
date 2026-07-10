"""Assign Role use case."""

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
from mfm.domain.organization.exceptions import ArchivedRoleAssignmentError
from mfm.domain.organization.exceptions import InvalidRoleAssignmentPeriodError
from mfm.domain.organization.exceptions import RoleAssignmentOverlapError
from mfm.domain.organization.role import Role


@dataclass(frozen=True, slots=True)
class AssignRoleRequest:
    role_id: UUID
    assignee_id: UUID
    organization_id: UUID
    valid_from: date
    valid_to: date | None = None

    def validate(self) -> None:
        if not isinstance(self.role_id, UUID):
            raise ValidationException("role_id must be UUID")
        if not isinstance(self.assignee_id, UUID):
            raise ValidationException("assignee_id must be UUID")
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.valid_from, date):
            raise ValidationException("valid_from must be date")
        if self.valid_to is not None and not isinstance(self.valid_to, date):
            raise ValidationException("valid_to must be date or None")
        if self.valid_to is not None and self.valid_to < self.valid_from:
            raise ValidationException("valid_to cannot be before valid_from")


@dataclass(frozen=True, slots=True)
class AssignRoleResponse:
    role_id: UUID
    assignee_id: UUID
    organization_id: UUID


@dataclass(slots=True)
class RoleAssignedEvent(DomainEvent):
    role_id: UUID = field(default_factory=uuid4)
    assignee_id: UUID = field(default_factory=uuid4)
    organization_id: UUID = field(default_factory=uuid4)


class RoleRepository(Protocol):
    def get_by_id(self, role_id: UUID) -> Role | None: ...

    def update(self, role: Role) -> None: ...


class AssignRoleUseCase:
    """Assign role aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: AssignRoleRequest) -> AssignRoleResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: RoleRepository = uow.role_repository

                role = repository.get_by_id(request.role_id)
                if role is None:
                    raise BusinessRuleViolation(f"Role {request.role_id} does not exist")

                role.assign(
                    assignee_id=request.assignee_id,
                    organization_id=request.organization_id,
                    valid_from=request.valid_from,
                    valid_to=request.valid_to,
                )

                repository.update(role)
                uow.commit()
        except (
            RoleAssignmentOverlapError,
            InvalidRoleAssignmentPeriodError,
            ArchivedRoleAssignmentError,
        ) as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Assign role failed") from exc

        self._dispatcher.dispatch(
            RoleAssignedEvent(
                role_id=request.role_id,
                assignee_id=request.assignee_id,
                organization_id=request.organization_id,
            )
        )

        return AssignRoleResponse(
            role_id=request.role_id,
            assignee_id=request.assignee_id,
            organization_id=request.organization_id,
        )
