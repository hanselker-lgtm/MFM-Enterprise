"""Application service for membership management operations."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


class ApplicationException(Exception):
    """Base exception for membership management service failures."""


class ValidationException(ApplicationException):
    """Raised when service request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class RegisterMembershipRequest:
    member_id: UUID
    membership_type_id: UUID
    start_date: date | None = None

    def validate(self) -> None:
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")
        if not isinstance(self.membership_type_id, UUID):
            raise ValidationException("membership_type_id must be UUID")
        if self.start_date is not None and not isinstance(self.start_date, date):
            raise ValidationException("start_date must be date or None")


@dataclass(frozen=True, slots=True)
class ChangeMembershipStatusRequest:
    membership_id: UUID
    target_status: MembershipStatus
    effective_date: date | None = None

    def validate(self) -> None:
        if not isinstance(self.membership_id, UUID):
            raise ValidationException("membership_id must be UUID")
        if not isinstance(self.target_status, MembershipStatus):
            raise ValidationException("target_status must be MembershipStatus")
        if self.effective_date is not None and not isinstance(self.effective_date, date):
            raise ValidationException("effective_date must be date or None")


@dataclass(frozen=True, slots=True)
class ListMembershipsRequest:
    member_id: UUID
    active_only: bool = False

    def validate(self) -> None:
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")
        if not isinstance(self.active_only, bool):
            raise ValidationException("active_only must be bool")


@dataclass(frozen=True, slots=True)
class MembershipRecordResponse:
    membership_id: UUID
    member_id: UUID
    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    status: str
    start_date: date
    end_date: date | None


class MembershipRepositoryPort(Protocol):
    def add(self, membership: Membership) -> None: ...

    def update(self, membership: Membership) -> None: ...

    def get(self, membership_id: UUID) -> Membership | None: ...

    def list_by_member(self, member_id: UUID) -> list[Membership]: ...

    def member_exists(self, member_id: UUID) -> bool: ...


class MembershipTypeRepositoryPort(Protocol):
    def get(self, membership_type_id: UUID) -> MembershipType | None: ...


class MembershipManagementService:
    """Manage membership lifecycle using repository abstractions."""

    def __init__(
        self,
        *,
        membership_repository: MembershipRepositoryPort,
        membership_type_repository: MembershipTypeRepositoryPort,
    ) -> None:
        self._membership_repository = membership_repository
        self._membership_type_repository = membership_type_repository

    def register_membership(
        self,
        request: RegisterMembershipRequest,
    ) -> MembershipRecordResponse:
        request.validate()

        try:
            if not self._membership_repository.member_exists(request.member_id):
                raise BusinessRuleViolation(
                    f"Member {request.member_id} does not exist"
                )

            membership_type = self._membership_type_repository.get(
                request.membership_type_id
            )
            if membership_type is None:
                raise BusinessRuleViolation(
                    f"Membership type {request.membership_type_id} does not exist"
                )

            membership = Membership(
                member_id=request.member_id,
                membership_type=membership_type,
                start_date=request.start_date or datetime.now(UTC).date(),
            )
            self._membership_repository.add(membership)
            return self._to_response(membership)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Register membership failed") from exc

    def change_membership_status(
        self,
        request: ChangeMembershipStatusRequest,
    ) -> MembershipRecordResponse:
        request.validate()

        try:
            membership = self._membership_repository.get(request.membership_id)
            if membership is None:
                raise BusinessRuleViolation(
                    f"Membership {request.membership_id} does not exist"
                )

            if request.target_status is MembershipStatus.ACTIVE:
                membership.reactivate()
            elif request.target_status is MembershipStatus.SUSPENDED:
                membership.suspend()
            elif request.target_status is MembershipStatus.ENDED:
                membership.end(request.effective_date)
            elif request.target_status is MembershipStatus.EXPIRED:
                membership.expire(request.effective_date)

            self._membership_repository.update(membership)
            return self._to_response(membership)
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Change membership status failed") from exc

    def list_memberships(
        self,
        request: ListMembershipsRequest,
    ) -> tuple[MembershipRecordResponse, ...]:
        request.validate()

        try:
            memberships = self._membership_repository.list_by_member(request.member_id)
            if request.active_only:
                memberships = [
                    membership
                    for membership in memberships
                    if membership.status is MembershipStatus.ACTIVE
                ]
            return tuple(self._to_response(membership) for membership in memberships)
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("List memberships failed") from exc

    @staticmethod
    def _to_response(membership: Membership) -> MembershipRecordResponse:
        return MembershipRecordResponse(
            membership_id=membership.id,
            member_id=membership.member_id,
            membership_type_id=membership.membership_type.id,
            membership_type_code=membership.membership_type.code,
            membership_type_name=membership.membership_type.name,
            status=membership.status.value,
            start_date=membership.start_date,
            end_date=membership.end_date,
        )
