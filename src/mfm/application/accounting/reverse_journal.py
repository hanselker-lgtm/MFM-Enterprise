"""Reverse Journal use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import JournalResponse
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.accounting.create_journal import to_journal_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.repositories import JournalRepository


@dataclass(frozen=True, slots=True)
class ReverseJournalRequest:
    journal_id: UUID

    def validate(self) -> None:
        if not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID")


@dataclass(frozen=True, slots=True)
class ReverseJournalResponse:
    journal: JournalResponse


class ReverseJournalUseCase:
    """Reverse an existing posted journal in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ReverseJournalRequest) -> ReverseJournalResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: JournalRepository = uow.journal_repository
                journal = repository.get_by_id(request.journal_id)
                if journal is None:
                    raise BusinessRuleViolation(
                        f"Journal {request.journal_id} does not exist"
                    )

                journal.reverse()
                repository.update(journal)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Reverse journal failed") from exc

        return ReverseJournalResponse(journal=to_journal_response(journal))
