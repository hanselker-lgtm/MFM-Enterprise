"""Feature API entry point for membership management."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal
from typing import Protocol
from uuid import UUID

from mfm.application.membership.membership_management_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.membership.membership_management_service import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.membership.membership_management_service import (
    ChangeMembershipStatusRequest as ServiceChangeRequest,
)
from mfm.application.membership.membership_management_service import (
    ListMembershipsRequest as ServiceListRequest,
)
from mfm.application.membership.membership_management_service import (
    MembershipRecordResponse,
)
from mfm.application.membership.membership_management_service import (
    RegisterMembershipRequest as ServiceRegisterRequest,
)
from mfm.application.membership.membership_management_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.membership.membership_management_service import (
    ValidationException as ServiceValidationException,
)
from mfm.domain.membership.membership_status import MembershipStatus


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


MembershipOperation = Literal["register", "change-status", "list"]


@dataclass(frozen=True, slots=True)
class ManageMembershipRequest:
    operation: MembershipOperation
    member_id: UUID | None = None
    membership_type_id: UUID | None = None
    membership_id: UUID | None = None
    target_status: MembershipStatus | None = None
    start_date: date | None = None
    effective_date: date | None = None
    active_only: bool = False

    def validate(self) -> None:
        if self.operation not in ("register", "change-status", "list"):
            raise ValidationException("operation must be register, change-status, or list")

        if self.operation == "register":
            if not isinstance(self.member_id, UUID):
                raise ValidationException("member_id must be UUID for register")
            if not isinstance(self.membership_type_id, UUID):
                raise ValidationException("membership_type_id must be UUID for register")
            if self.start_date is not None and not isinstance(self.start_date, date):
                raise ValidationException("start_date must be date or None")

        if self.operation == "change-status":
            if not isinstance(self.membership_id, UUID):
                raise ValidationException("membership_id must be UUID for change-status")
            if not isinstance(self.target_status, MembershipStatus):
                raise ValidationException(
                    "target_status must be MembershipStatus for change-status"
                )
            if self.effective_date is not None and not isinstance(self.effective_date, date):
                raise ValidationException("effective_date must be date or None")

        if self.operation == "list":
            if not isinstance(self.member_id, UUID):
                raise ValidationException("member_id must be UUID for list")
            if not isinstance(self.active_only, bool):
                raise ValidationException("active_only must be bool")


@dataclass(frozen=True, slots=True)
class ManageMembershipResponse:
    memberships: tuple[MembershipRecordResponse, ...]


class MembershipManagementServicePort(Protocol):
    def register_membership(
        self,
        request: ServiceRegisterRequest,
    ) -> MembershipRecordResponse: ...

    def change_membership_status(
        self,
        request: ServiceChangeRequest,
    ) -> MembershipRecordResponse: ...

    def list_memberships(
        self,
        request: ServiceListRequest,
    ) -> tuple[MembershipRecordResponse, ...]: ...


class ManageMembershipFeature:
    """Feature facade for register/change/list membership operations."""

    def __init__(self, *, service: MembershipManagementServicePort) -> None:
        self._service = service

    def execute(self, request: ManageMembershipRequest) -> ManageMembershipResponse:
        request.validate()

        try:
            if request.operation == "register":
                membership = self._service.register_membership(
                    ServiceRegisterRequest(
                        member_id=request.member_id,
                        membership_type_id=request.membership_type_id,
                        start_date=request.start_date,
                    )
                )
                return ManageMembershipResponse(memberships=(membership,))

            if request.operation == "change-status":
                membership = self._service.change_membership_status(
                    ServiceChangeRequest(
                        membership_id=request.membership_id,
                        target_status=request.target_status,
                        effective_date=request.effective_date,
                    )
                )
                return ManageMembershipResponse(memberships=(membership,))

            memberships = self._service.list_memberships(
                ServiceListRequest(
                    member_id=request.member_id,
                    active_only=request.active_only,
                )
            )
            return ManageMembershipResponse(memberships=memberships)
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Manage membership feature failed") from exc
