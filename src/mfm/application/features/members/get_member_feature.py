"""GetMemberFeature: fetch a single member by id."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.features.members.create_member_feature import (
    ApplicationException,
    MemberDTO,
    RepositoryException,
    ValidationException,
    _to_member_dto,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


class MemberNotFound(ApplicationException):
    """Raised when the requested member does not exist."""


@dataclass(frozen=True, slots=True)
class GetMemberRequest:
    member_id: UUID

    def validate(self) -> None:
        if not isinstance(self.member_id, UUID):
            raise ValidationException("member_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetMemberResponse:
    member: MemberDTO


class GetMemberFeature:
    """Public application entry point for fetching one member."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetMemberRequest) -> GetMemberResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                member = uow.member_repository.get(request.member_id)
                if member is None:
                    raise MemberNotFound(f"Member {request.member_id} does not exist")

                contact = uow.contact_repository.get(member.contact_id)
                display_name = (
                    contact.party.display_name if contact is not None else "(unknown contact)"
                )
                dto = _to_member_dto(member, display_name=display_name)
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Get member feature failed") from exc

        return GetMemberResponse(member=dto)
