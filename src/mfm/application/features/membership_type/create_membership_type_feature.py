"""CreateMembershipTypeFeature: define a new membership type/category."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.membership_type.list_membership_types_feature import (
    ApplicationException,
    MembershipTypeDTO,
    RepositoryException,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.membership.exceptions import (
    DuplicateMembershipTypeCodeError,
    InvalidMembershipTypeError,
)
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_type import MembershipType


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


@dataclass(frozen=True, slots=True)
class CreateMembershipTypeRequest:
    code: str
    name: str
    category: str = "GENERAL"
    description: str | None = None

    def validate(self) -> None:
        if not isinstance(self.code, str) or not self.code.strip():
            raise ValidationException("code must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        try:
            MembershipCategory(self.category.strip().upper())
        except ValueError as exc:
            raise ValidationException(f"category is invalid: {self.category}") from exc


@dataclass(frozen=True, slots=True)
class CreateMembershipTypeResponse:
    membership_type: MembershipTypeDTO


class CreateMembershipTypeFeature:
    """Public application entry point for defining a membership type."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateMembershipTypeRequest) -> CreateMembershipTypeResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                membership_type = MembershipType(
                    code=request.code,
                    name=request.name,
                    category=MembershipCategory(request.category.strip().upper()),
                    description=request.description,
                )
                uow.membership_type_repository.add(membership_type)
        except InvalidMembershipTypeError as exc:
            raise ValidationException(str(exc)) from exc
        except (DuplicateMembershipTypeCodeError, ValueError) as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Create membership type feature failed") from exc

        return CreateMembershipTypeResponse(
            membership_type=MembershipTypeDTO(
                membership_type_id=membership_type.id,
                code=membership_type.code,
                name=membership_type.name,
                category=membership_type.category.value,
                is_active=membership_type.is_active,
            )
        )
