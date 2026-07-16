"""Get fiscal year feature facade following Public API Standard."""

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
from mfm.application.accounting.get_fiscal_year import GetFiscalYearRequest as ServiceRequest
from mfm.application.accounting.get_fiscal_year import GetFiscalYearResponse as ServiceResponse
from mfm.application.features.accounting.create_fiscal_year_feature import FiscalYearResponse
from mfm.application.features.accounting.create_fiscal_year_feature import (
    to_feature_fiscal_year_response,
)
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException


@dataclass(frozen=True, slots=True)
class GetFiscalYearRequest:
    fiscal_year_id: UUID

    def validate(self) -> None:
        if not isinstance(self.fiscal_year_id, UUID):
            raise ValidationException("fiscal_year_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetFiscalYearResponse:
    fiscal_year: FiscalYearResponse


class GetFiscalYearService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetFiscalYearFeature:
    """Feature facade for fiscal year retrieval."""

    def __init__(self, *, service: GetFiscalYearService) -> None:
        self._service = service

    def execute(self, request: GetFiscalYearRequest) -> GetFiscalYearResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(fiscal_year_id=request.fiscal_year_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get fiscal year feature failed") from exc

        return GetFiscalYearResponse(
            fiscal_year=to_feature_fiscal_year_response(service_response.fiscal_year)
        )
