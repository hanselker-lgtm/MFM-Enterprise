"""Open FiscalYear use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.accounting.create_fiscal_year import FiscalYearResponse
from mfm.application.accounting.create_fiscal_year import to_fiscal_year_response
from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.repositories import FiscalYearRepository


@dataclass(frozen=True, slots=True)
class OpenFiscalYearRequest:
    fiscal_year_id: UUID

    def validate(self) -> None:
        if not isinstance(self.fiscal_year_id, UUID):
            raise ValidationException("fiscal_year_id must be UUID")


@dataclass(frozen=True, slots=True)
class OpenFiscalYearResponse:
    fiscal_year: FiscalYearResponse


class OpenFiscalYearUseCase:
    """Transition fiscal year lifecycle state to OPEN."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: OpenFiscalYearRequest) -> OpenFiscalYearResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: FiscalYearRepository = uow.fiscal_year_repository
                fiscal_year = repository.get_by_id(request.fiscal_year_id)
                if fiscal_year is None:
                    raise BusinessRuleViolation(
                        f"Fiscal year {request.fiscal_year_id} does not exist"
                    )

                fiscal_year.reopen_year()
                repository.update(fiscal_year)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Open fiscal year failed") from exc

        return OpenFiscalYearResponse(fiscal_year=to_fiscal_year_response(fiscal_year))
