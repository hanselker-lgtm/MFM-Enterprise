"""ListMembershipTypesFeature: list configured membership types."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class MembershipTypeDTO:
    membership_type_id: UUID
    code: str
    name: str
    category: str
    is_active: bool


@dataclass(frozen=True, slots=True)
class ListMembershipTypesRequest:
    active_only: bool = False


@dataclass(frozen=True, slots=True)
class ListMembershipTypesResponse:
    membership_types: tuple[MembershipTypeDTO, ...]


class ListMembershipTypesFeature:
    """Public application entry point for listing membership types."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListMembershipTypesRequest) -> ListMembershipTypesResponse:
        try:
            with self._unit_of_work as uow:
                membership_types = uow.membership_type_repository.list()
        except Exception as exc:
            raise RepositoryException("List membership types feature failed") from exc

        if request.active_only:
            membership_types = [mt for mt in membership_types if mt.is_active]

        return ListMembershipTypesResponse(
            membership_types=tuple(
                MembershipTypeDTO(
                    membership_type_id=mt.id,
                    code=mt.code,
                    name=mt.name,
                    category=mt.category.value,
                    is_active=mt.is_active,
                )
                for mt in membership_types
            )
        )
