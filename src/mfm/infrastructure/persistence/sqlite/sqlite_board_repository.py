"""SQLite repository for Board aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.board_member_model import BoardMemberModel
from mfm.database.models.board_model import BoardModel
from mfm.domain.organization.board import Board
from mfm.repositories.board_repository import BoardRepository


class SQLiteBoardRepository(BoardRepository):
    """SQLAlchemy-backed repository for Board aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, board: Board) -> None:
        self._session.add(OrganizationMapper.to_orm_board(board))
        self._session.flush()

    def get_by_id(self, board_id: UUID) -> Board | None:
        orm = self._session.scalar(select(BoardModel).where(BoardModel.id == board_id))
        if orm is None:
            return None
        return OrganizationMapper.to_domain_board(orm)

    def update(self, board: Board) -> None:
        orm = self._session.get(BoardModel, board.id)
        if orm is None:
            raise ValueError(f"Board {board.id} does not exist")

        orm.organization_id = board.organization_id.value
        orm.name = board.name
        orm.term_start = board.term_start
        orm.term_end = board.term_end
        orm.status = board.status
        orm.members = [
            BoardMemberModel(
                board_id=board.id,
                member_id=member.member_id,
                role=member.role,
                appointed_on=member.appointed_on,
                resigned_on=member.resigned_on,
                is_chair=member.is_chair,
            )
            for member in board.members
        ]
        self._session.flush()

    def delete(self, board_id: UUID) -> None:
        orm = self._session.get(BoardModel, board_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, board_id: UUID) -> bool:
        return self._session.get(BoardModel, board_id) is not None

    def list(self) -> list[Board]:
        orm_entities = self._session.scalars(select(BoardModel)).all()
        return [OrganizationMapper.to_domain_board(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Board]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(BoardModel).where(
                or_(
                    BoardModel.name.ilike(query),
                )
            )
        ).all()
        return [OrganizationMapper.to_domain_board(orm) for orm in orm_entities]
