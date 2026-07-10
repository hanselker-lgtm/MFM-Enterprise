"""Create Board use case."""

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
from mfm.domain.organization.board import Board
from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId


@dataclass(frozen=True, slots=True)
class BoardMemberInput:
    member_id: UUID
    role: str
    appointed_on: date
    resigned_on: date | None = None
    is_chair: bool = False


@dataclass(frozen=True, slots=True)
class CreateBoardRequest:
    organization_id: UUID
    name: str
    term_start: date
    term_end: date
    members: tuple[BoardMemberInput, ...]

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.term_start, date) or not isinstance(self.term_end, date):
            raise ValidationException("term_start and term_end must be dates")
        if not isinstance(self.members, tuple) or not self.members:
            raise ValidationException("members must be a non-empty tuple")
        if not any(member.is_chair for member in self.members):
            raise ValidationException("board must include at least one chair")


@dataclass(frozen=True, slots=True)
class CreateBoardResponse:
    board_id: UUID
    organization_id: UUID
    name: str


@dataclass(slots=True)
class BoardCreatedEvent(DomainEvent):
    board_id: UUID = field(default_factory=uuid4)
    organization_id: UUID = field(default_factory=uuid4)


class OrganizationRepository(Protocol):
    def get_by_id(self, organization_id: UUID) -> Organization | None: ...


class BoardRepository(Protocol):
    def add(self, board: Board) -> None: ...

    def search(self, text: str) -> list[Board]: ...


class CreateBoardUseCase:
    """Create board aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: CreateBoardRequest) -> CreateBoardResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                organization_repository: OrganizationRepository = uow.organization_repository
                board_repository: BoardRepository = uow.board_repository

                organization = organization_repository.get_by_id(request.organization_id)
                if organization is None:
                    raise BusinessRuleViolation(
                        f"Organization {request.organization_id} does not exist"
                    )

                for existing in board_repository.search(request.name.strip()):
                    if (
                        existing.organization_id.value == request.organization_id
                        and existing.name.casefold() == request.name.strip().casefold()
                        and existing.term_start == request.term_start
                        and existing.term_end == request.term_end
                    ):
                        raise BusinessRuleViolation("Board already exists for organization and term")

                board = Board(
                    organization_id=OrganizationId(request.organization_id),
                    name=request.name,
                    term_start=request.term_start,
                    term_end=request.term_end,
                    members=[
                        BoardMember(
                            member_id=member.member_id,
                            role=member.role,
                            appointed_on=member.appointed_on,
                            resigned_on=member.resigned_on,
                            is_chair=member.is_chair,
                        )
                        for member in request.members
                    ],
                )
                board_repository.add(board)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Create board failed") from exc

        self._dispatcher.dispatch(
            BoardCreatedEvent(
                board_id=board.id,
                organization_id=request.organization_id,
            )
        )

        return CreateBoardResponse(
            board_id=board.id,
            organization_id=request.organization_id,
            name=board.name,
        )
