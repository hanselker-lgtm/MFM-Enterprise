"""List fiscal years feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsRequest as ServiceRequest
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsResponse as ServiceResponse
from mfm.application.features.accounting.create_fiscal_year_feature import FiscalYearResponse
from mfm.application.features.accounting.create_fiscal_year_feature import (
    to_feature_fiscal_year_response,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException


@dataclass(frozen=True, slots=True)
class ListFiscalYearsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListFiscalYearsResponse:
    fiscal_years: tuple[FiscalYearResponse, ...]


class ListFiscalYearsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListFiscalYearsFeature:
    """Feature facade for fiscal year listing."""

    def __init__(self, *, service: ListFiscalYearsService) -> None:
        self._service = service

    def execute(self, request: ListFiscalYearsRequest) -> ListFiscalYearsResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List fiscal years feature failed") from exc

        return ListFiscalYearsResponse(
            fiscal_years=tuple(
                to_feature_fiscal_year_response(item)
                for item in service_response.fiscal_years
            )
        )
