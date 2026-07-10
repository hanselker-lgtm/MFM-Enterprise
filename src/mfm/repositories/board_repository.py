"""Board Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization.board import Board


class BoardRepository(ABC):
    """Repository contract for Board aggregates."""

    @abstractmethod
    def add(self, board: Board) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, board_id: UUID) -> Board | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, board: Board) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, board_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, board_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Board]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Board]:
        raise NotImplementedError
