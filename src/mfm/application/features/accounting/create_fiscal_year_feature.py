"""Create fiscal year feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.accounting.create_fiscal_year import (
    CreateFiscalYearRequest as ServiceRequest,
)
from mfm.application.accounting.create_fiscal_year import (
    CreateFiscalYearResponse as ServiceResponse,
)
from mfm.application.accounting.create_fiscal_year import (
    FiscalPeriodInput as ServiceFiscalPeriodInput,
)
from mfm.application.accounting.create_fiscal_year import (
    FiscalPeriodResponse as ServiceFiscalPeriodResponse,
)
from mfm.application.accounting.create_fiscal_year import (
    FiscalYearResponse as ServiceFiscalYearResponse,
)
from mfm.application.accounting.create_journal import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException


@dataclass(frozen=True, slots=True)
class FiscalPeriodInput:
    number: int
    start_date: date
    end_date: date
    closed: bool = False

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.number, int) or isinstance(self.number, bool):
            raise ValidationException(f"{field_name}.number must be integer")
        if not isinstance(self.start_date, date):
            raise ValidationException(f"{field_name}.start_date must be date")
        if not isinstance(self.end_date, date):
            raise ValidationException(f"{field_name}.end_date must be date")
        if not isinstance(self.closed, bool):
            raise ValidationException(f"{field_name}.closed must be bool")


@dataclass(frozen=True, slots=True)
class FiscalPeriodResponse:
    number: int
    start_date: date
    end_date: date
    closed: bool


@dataclass(frozen=True, slots=True)
class FiscalYearResponse:
    fiscal_year_id: UUID
    year: int
    start_date: date
    end_date: date
    status: str
    periods: tuple[FiscalPeriodResponse, ...]


@dataclass(frozen=True, slots=True)
class CreateFiscalYearRequest:
    year: int
    start_date: date
    end_date: date
    periods: tuple[FiscalPeriodInput, ...]
    fiscal_year_id: UUID | None = None
    status: str = "OPEN"

    def validate(self) -> None:
        if not isinstance(self.year, int) or isinstance(self.year, bool):
            raise ValidationException("year must be integer")
        if not isinstance(self.start_date, date):
            raise ValidationException("start_date must be date")
        if not isinstance(self.end_date, date):
            raise ValidationException("end_date must be date")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if self.fiscal_year_id is not None and not isinstance(self.fiscal_year_id, UUID):
            raise ValidationException("fiscal_year_id must be UUID or None")
        if not isinstance(self.periods, tuple):
            raise ValidationException("periods must be tuple")
        if not self.periods:
            raise ValidationException("periods must be non-empty")

        for index, period in enumerate(self.periods):
            period.validate(field_name=f"periods[{index}]")


@dataclass(frozen=True, slots=True)
class CreateFiscalYearResponse:
    fiscal_year: FiscalYearResponse


class CreateFiscalYearService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_fiscal_period_input(value: FiscalPeriodInput) -> ServiceFiscalPeriodInput:
    return ServiceFiscalPeriodInput(
        number=value.number,
        start_date=value.start_date,
        end_date=value.end_date,
        closed=value.closed,
    )


def to_feature_fiscal_period_response(response: ServiceFiscalPeriodResponse) -> FiscalPeriodResponse:
    return FiscalPeriodResponse(
        number=response.number,
        start_date=response.start_date,
        end_date=response.end_date,
        closed=response.closed,
    )


def to_feature_fiscal_year_response(response: ServiceFiscalYearResponse) -> FiscalYearResponse:
    return FiscalYearResponse(
        fiscal_year_id=response.fiscal_year_id,
        year=response.year,
        start_date=response.start_date,
        end_date=response.end_date,
        status=response.status,
        periods=tuple(to_feature_fiscal_period_response(item) for item in response.periods),
    )


class CreateFiscalYearFeature:
    """Feature facade for fiscal year creation."""

    def __init__(self, *, service: CreateFiscalYearService) -> None:
        self._service = service

    def execute(self, request: CreateFiscalYearRequest) -> CreateFiscalYearResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    year=request.year,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    periods=tuple(
                        to_service_fiscal_period_input(item)
                        for item in request.periods
                    ),
                    fiscal_year_id=request.fiscal_year_id,
                    status=request.status,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create fiscal year feature failed") from exc

        return CreateFiscalYearResponse(
            fiscal_year=to_feature_fiscal_year_response(service_response.fiscal_year)
        )
