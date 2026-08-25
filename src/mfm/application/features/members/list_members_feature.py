"""ListMembersFeature: list all registered members with display names."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.features.members.create_member_feature import (
    ApplicationException,
    MemberDTO,
    RepositoryException,
    _to_member_dto,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork


@dataclass(frozen=True, slots=True)
class ListMembersRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListMembersResponse:
    members: tuple[MemberDTO, ...]


class ListMembersFeature:
    """Public application entry point for listing members."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListMembersRequest) -> ListMembersResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                members = uow.member_repository.list()
                dtos = []
                for member in members:
                    contact = uow.contact_repository.get(member.contact_id)
                    display_name = (
                        contact.party.display_name if contact is not None else "(unknown contact)"
                    )
                    dtos.append(_to_member_dto(member, display_name=display_name))
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List members feature failed") from exc

        return ListMembersResponse(members=tuple(dtos))
