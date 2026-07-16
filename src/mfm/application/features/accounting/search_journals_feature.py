"""Search journals feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)
from mfm.application.accounting.search_journals import SearchJournalsRequest as ServiceRequest
from mfm.application.accounting.search_journals import SearchJournalsResponse as ServiceResponse
from mfm.application.features.accounting.create_journal_feature import (
    JournalSearchResultResponse,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException
from mfm.application.features.accounting.create_journal_feature import (
    to_feature_journal_search_result_response,
)


@dataclass(frozen=True, slots=True)
class SearchJournalsRequest:
    text: str | None = None
    status: str | None = None
    fiscal_year: int | None = None

    def validate(self) -> None:
        for field_name, value in (("text", self.text), ("status", self.status)):
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValidationException(f"{field_name} must be string or None")
            if not value.strip():
                raise ValidationException(f"{field_name} must be non-empty when provided")

        if self.fiscal_year is not None and (
            not isinstance(self.fiscal_year, int) or isinstance(self.fiscal_year, bool)
        ):
            raise ValidationException("fiscal_year must be integer or None")


@dataclass(frozen=True, slots=True)
class SearchJournalsResponse:
    journals: tuple[JournalSearchResultResponse, ...]


class SearchJournalsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class SearchJournalsFeature:
    """Feature facade for journal search."""

    def __init__(self, *, service: SearchJournalsService) -> None:
        self._service = service

    def execute(self, request: SearchJournalsRequest) -> SearchJournalsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    text=request.text,
                    status=request.status,
                    fiscal_year=request.fiscal_year,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Search journals feature failed") from exc

        return SearchJournalsResponse(
            journals=tuple(
                to_feature_journal_search_result_response(item)
                for item in service_response.journals
            )
        )
