"""Open fiscal year feature facade following Public API Standard."""

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
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearRequest as ServiceRequest
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearResponse as ServiceResponse
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
class OpenFiscalYearRequest:
    fiscal_year_id: UUID

    def validate(self) -> None:
        if not isinstance(self.fiscal_year_id, UUID):
            raise ValidationException("fiscal_year_id must be UUID")


@dataclass(frozen=True, slots=True)
class OpenFiscalYearResponse:
    fiscal_year: FiscalYearResponse


class OpenFiscalYearService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class OpenFiscalYearFeature:
    """Feature facade for fiscal year reopen."""

    def __init__(self, *, service: OpenFiscalYearService) -> None:
        self._service = service

    def execute(self, request: OpenFiscalYearRequest) -> OpenFiscalYearResponse:
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
            raise RepositoryException("Open fiscal year feature failed") from exc

        return OpenFiscalYearResponse(
            fiscal_year=to_feature_fiscal_year_response(service_response.fiscal_year)
        )
