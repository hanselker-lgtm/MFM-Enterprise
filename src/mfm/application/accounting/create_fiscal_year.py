"""Create FiscalYear use case and shared fiscal year DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID
from uuid import uuid4

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.repositories import FiscalYearRepository


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


class CreateFiscalYearUseCase:
    """Create fiscal year aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateFiscalYearRequest) -> CreateFiscalYearResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: FiscalYearRepository = uow.fiscal_year_repository
                fiscal_year = FiscalYear(
                    id=request.fiscal_year_id or uuid4(),
                    year=request.year,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    periods=[to_fiscal_period(item) for item in request.periods],
                    status=FiscalYearStatus(request.status.strip().upper()),
                )
                repository.add(fiscal_year)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create fiscal year failed") from exc

        return CreateFiscalYearResponse(fiscal_year=to_fiscal_year_response(fiscal_year))


def to_fiscal_period(value: FiscalPeriodInput) -> FiscalPeriod:
    return FiscalPeriod(
        number=value.number,
        start_date=value.start_date,
        end_date=value.end_date,
        closed=value.closed,
    )


def to_fiscal_period_response(value: FiscalPeriod) -> FiscalPeriodResponse:
    return FiscalPeriodResponse(
        number=value.number,
        start_date=value.start_date,
        end_date=value.end_date,
        closed=value.closed,
    )


def to_fiscal_year_response(value: FiscalYear) -> FiscalYearResponse:
    return FiscalYearResponse(
        fiscal_year_id=value.id,
        year=value.year,
        start_date=value.start_date,
        end_date=value.end_date,
        status=value.status.value,
        periods=tuple(to_fiscal_period_response(item) for item in value.periods),
    )
