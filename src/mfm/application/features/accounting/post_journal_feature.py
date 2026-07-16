"""Post journal feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.accounting.create_journal import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)
from mfm.application.accounting.post_journal import PostJournalRequest as ServiceRequest
from mfm.application.accounting.post_journal import PostJournalResponse as ServiceResponse
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import JournalResponse
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException
from mfm.application.features.accounting.create_journal_feature import (
    to_feature_journal_response,
)


@dataclass(frozen=True, slots=True)
class PostJournalRequest:
    journal_id: UUID

    def validate(self) -> None:
        if not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID")


@dataclass(frozen=True, slots=True)
class PostJournalResponse:
    journal: JournalResponse


class PostJournalService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class PostJournalFeature:
    """Feature facade for journal posting."""

    def __init__(self, *, service: PostJournalService) -> None:
        self._service = service

    def execute(self, request: PostJournalRequest) -> PostJournalResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(journal_id=request.journal_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Post journal feature failed") from exc

        return PostJournalResponse(
            journal=to_feature_journal_response(service_response.journal)
        )
