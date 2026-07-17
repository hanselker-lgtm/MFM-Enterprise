"""Application service for Organization & Roles foundation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.domain.organization_roles.assignment import Assignment
from mfm.domain.organization_roles.board import Board
from mfm.domain.organization_roles.committee import Committee
from mfm.domain.organization_roles.election_period import ElectionPeriod
from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)
from mfm.domain.organization_roles.permission import Permission
from mfm.domain.organization_roles.responsibility import Responsibility
from mfm.domain.organization_roles.role import Role


class ApplicationException(Exception):
    """Base exception for organization roles service failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository access fails."""


@dataclass(frozen=True, slots=True)
class CreateOrganizationRolesFoundationRequest:
    organization_id: UUID
    board_name: str
    role_name: str
    committee_name: str
    committee_mandate: str
    election_period_name: str
    election_starts_on: date
    election_ends_on: date

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if not isinstance(self.board_name, str) or not self.board_name.strip():
            raise ValidationException("board_name must be non-empty string")
        if not isinstance(self.role_name, str) or not self.role_name.strip():
            raise ValidationException("role_name must be non-empty string")
        if not isinstance(self.committee_name, str) or not self.committee_name.strip():
            raise ValidationException("committee_name must be non-empty string")
        if not isinstance(self.committee_mandate, str) or not self.committee_mandate.strip():
            raise ValidationException("committee_mandate must be non-empty string")
        if not isinstance(self.election_period_name, str) or not self.election_period_name.strip():
            raise ValidationException("election_period_name must be non-empty string")
        if not isinstance(self.election_starts_on, date):
            raise ValidationException("election_starts_on must be date")
        if not isinstance(self.election_ends_on, date):
            raise ValidationException("election_ends_on must be date")
        if self.election_ends_on < self.election_starts_on:
            raise ValidationException("election_ends_on cannot be before election_starts_on")


@dataclass(frozen=True, slots=True)
class CreateOrganizationRolesFoundationResponse:
    organization_id: UUID
    role_count: int
    assignment_count: int
    committee_count: int
    board_name: str
    election_period_count: int
    generated_at: datetime


class OrganizationRolesRepositoryPort(Protocol):
    def get(self, organization_id: UUID) -> OrganizationRolesFoundation | None: ...

    def save(self, foundation: OrganizationRolesFoundation) -> None: ...


class OrganizationRolesService:
    """Build and persist independent Organization & Roles foundations."""

    def __init__(self, *, repository: OrganizationRolesRepositoryPort) -> None:
        self._repository = repository

    def create_foundation(
        self,
        request: CreateOrganizationRolesFoundationRequest,
    ) -> CreateOrganizationRolesFoundationResponse:
        request.validate()

        try:
            existing = self._repository.get(request.organization_id)
            foundation = existing or OrganizationRolesFoundation(
                organization_id=request.organization_id
            )

            election_period = ElectionPeriod(
                name=request.election_period_name,
                starts_on=request.election_starts_on,
                ends_on=request.election_ends_on,
            )
            foundation.add_election_period(election_period)

            role = Role(
                name=request.role_name,
                permissions=(
                    Permission.ASSIGN_ROLES,
                    Permission.MANAGE_ELECTIONS,
                    Permission.VIEW_REPORTS,
                ),
                responsibilities=(
                    Responsibility(
                        title="Governance",
                        description="Maintain governance operations for the organization.",
                    ),
                ),
            )
            foundation.add_role(role)

            assignment = Assignment(
                role_id=role.id,
                assignee_id=request.organization_id,
                starts_on=request.election_starts_on,
                ends_on=None,
            )
            foundation.assign_role(assignment)

            committee = Committee(
                name=request.committee_name,
                mandate=request.committee_mandate,
                role_ids=(role.id,),
            )
            foundation.add_committee(committee)

            board = Board(
                name=request.board_name,
                role_ids=(role.id,),
                election_period_id=election_period.id,
            )
            foundation.set_board(board)

            self._repository.save(foundation)

            return CreateOrganizationRolesFoundationResponse(
                organization_id=foundation.organization_id,
                role_count=len(foundation.roles),
                assignment_count=len(foundation.assignments),
                committee_count=len(foundation.committees),
                board_name=(foundation.board.name if foundation.board is not None else ""),
                election_period_count=len(foundation.election_periods),
                generated_at=datetime.now(UTC),
            )
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create organization roles foundation failed") from exc
