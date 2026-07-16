"""Get Journal use case."""

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
from mfm.domain.accounting.repositories import JournalRepository


@dataclass(frozen=True, slots=True)
class GetJournalRequest:
    journal_id: UUID

    def validate(self) -> None:
        if not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetJournalResponse:
    journal: JournalResponse


class GetJournalUseCase:
    """Load one journal through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetJournalRequest) -> GetJournalResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: JournalRepository = uow.journal_repository
                journal = repository.get_by_id(request.journal_id)
                if journal is None:
                    raise BusinessRuleViolation(
                        f"Journal {request.journal_id} does not exist"
                    )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get journal failed") from exc

        return GetJournalResponse(journal=to_journal_response(journal))
