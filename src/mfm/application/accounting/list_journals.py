"""List Journals use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import JournalResponse
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import to_journal_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.repositories import JournalRepository


@dataclass(frozen=True, slots=True)
class ListJournalsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListJournalsResponse:
    journals: tuple[JournalResponse, ...]


class ListJournalsUseCase:
    """List journals with repository-provided deterministic ordering."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListJournalsRequest) -> ListJournalsResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                repository: JournalRepository = uow.journal_repository
                journals = repository.list()
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List journals failed") from exc

        return ListJournalsResponse(
            journals=tuple(to_journal_response(item) for item in journals)
        )
