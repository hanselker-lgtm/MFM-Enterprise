"""List journals feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.list_journals import ListJournalsRequest as ServiceRequest
from mfm.application.accounting.list_journals import ListJournalsResponse as ServiceResponse
from mfm.application.features.accounting.create_journal_feature import JournalResponse
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import (
    to_feature_journal_response,
)


@dataclass(frozen=True, slots=True)
class ListJournalsRequest:
    pass


@dataclass(frozen=True, slots=True)
class ListJournalsResponse:
    journals: tuple[JournalResponse, ...]


class ListJournalsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListJournalsFeature:
    """Feature facade for journal listing."""

    def __init__(self, *, service: ListJournalsService) -> None:
        self._service = service

    def execute(self, request: ListJournalsRequest) -> ListJournalsResponse:
        _ = request

        try:
            service_response = self._service.execute(ServiceRequest())
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List journals feature failed") from exc

        return ListJournalsResponse(
            journals=tuple(to_feature_journal_response(item) for item in service_response.journals)
        )
