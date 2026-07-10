"""Create board feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.organization.create_board import BoardMemberInput as ServiceBoardMemberInput
from mfm.application.organization.create_board import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.organization.create_board import CreateBoardRequest as ServiceRequest
from mfm.application.organization.create_board import CreateBoardResponse as ServiceResponse
from mfm.application.organization.create_board import CreateBoardUseCase
from mfm.application.organization.create_organization import RepositoryException as ServiceRepositoryException
from mfm.application.organization.create_organization import ValidationException as ServiceValidationException


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


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


class CreateBoardService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateBoardFeature:
    """Feature facade for board creation with standardized API behavior."""

    def __init__(self, *, service: CreateBoardService) -> None:
        self._service = service

    def execute(self, request: CreateBoardRequest) -> CreateBoardResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    name=request.name,
                    term_start=request.term_start,
                    term_end=request.term_end,
                    members=tuple(
                        ServiceBoardMemberInput(
                            member_id=member.member_id,
                            role=member.role,
                            appointed_on=member.appointed_on,
                            resigned_on=member.resigned_on,
                            is_chair=member.is_chair,
                        )
                        for member in request.members
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create board feature failed") from exc

        return CreateBoardResponse(
            board_id=service_response.board_id,
            organization_id=service_response.organization_id,
            name=service_response.name,
        )
