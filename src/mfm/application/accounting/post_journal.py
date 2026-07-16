"""Post Journal use case."""

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
from mfm.domain.accounting.repositories import FiscalYearRepository
from mfm.domain.accounting.repositories import JournalRepository


@dataclass(frozen=True, slots=True)
class PostJournalRequest:
    journal_id: UUID

    def validate(self) -> None:
        if not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID")


@dataclass(frozen=True, slots=True)
class PostJournalResponse:
    journal: JournalResponse


class PostJournalUseCase:
    """Post an existing draft journal in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: PostJournalRequest) -> PostJournalResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                journal_repository: JournalRepository = uow.journal_repository
                fiscal_year_repository: FiscalYearRepository = uow.fiscal_year_repository

                journal = journal_repository.get_by_id(request.journal_id)
                if journal is None:
                    raise BusinessRuleViolation(
                        f"Journal {request.journal_id} does not exist"
                    )

                fiscal_year = fiscal_year_repository.get_by_year(journal.posting_date.year)
                if fiscal_year is None:
                    raise BusinessRuleViolation(
                        f"Fiscal year {journal.posting_date.year} does not exist"
                    )

                journal.post_in_fiscal_year(fiscal_year=fiscal_year)
                journal_repository.update(journal)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Post journal failed") from exc

        return PostJournalResponse(journal=to_journal_response(journal))
