"""List FiscalYears use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.accounting.create_fiscal_year import FiscalYearResponse
from mfm.application.accounting.create_fiscal_year import to_fiscal_year_response
from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.repositories import FiscalYearRepository


@dataclass(frozen=True, slots=True)
class ListFiscalYearsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListFiscalYearsResponse:
    fiscal_years: tuple[FiscalYearResponse, ...]


class ListFiscalYearsUseCase:
    """List fiscal years with repository-provided deterministic ordering."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListFiscalYearsRequest) -> ListFiscalYearsResponse:
        _ = request

        try:
            with self._unit_of_work as uow:
                repository: FiscalYearRepository = uow.fiscal_year_repository
                fiscal_years = repository.list()
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("List fiscal years failed") from exc

        return ListFiscalYearsResponse(
            fiscal_years=tuple(to_fiscal_year_response(item) for item in fiscal_years)
        )
