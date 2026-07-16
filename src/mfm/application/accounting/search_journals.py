"""Search Journals use case."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import JournalSearchResultResponse
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.accounting.create_journal import to_journal_search_result_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.repositories import JournalRepository


@dataclass(frozen=True, slots=True)
class SearchJournalsRequest:
    text: str | None = None
    status: str | None = None
    fiscal_year: int | None = None

    def validate(self) -> None:
        for field_name, value in (
            ("text", self.text),
            ("status", self.status),
        ):
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValidationException(f"{field_name} must be string or None")
            if not value.strip():
                raise ValidationException(
                    f"{field_name} must be non-empty when provided"
                )

        if self.fiscal_year is not None and (
            not isinstance(self.fiscal_year, int) or isinstance(self.fiscal_year, bool)
        ):
            raise ValidationException("fiscal_year must be integer or None")


@dataclass(frozen=True, slots=True)
class SearchJournalsResponse:
    journals: tuple[JournalSearchResultResponse, ...]


class SearchJournalsUseCase:
    """Search journals through repository projection queries."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: SearchJournalsRequest) -> SearchJournalsResponse:
        request.validate()

        criteria: dict[str, Any] = {}
        if request.text is not None:
            criteria["text"] = request.text.strip()
        if request.status is not None:
            criteria["status"] = request.status.strip()
        if request.fiscal_year is not None:
            criteria["fiscal_year"] = request.fiscal_year

        try:
            with self._unit_of_work as uow:
                repository: JournalRepository = uow.journal_repository
                rows = repository.search(criteria)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Search journals failed") from exc

        return SearchJournalsResponse(
            journals=tuple(to_journal_search_result_response(row) for row in rows)
        )
