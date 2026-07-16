"""Create journal feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.accounting.create_journal import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.accounting.create_journal import (
    CreateJournalRequest as ServiceRequest,
)
from mfm.application.accounting.create_journal import (
    CreateJournalResponse as ServiceResponse,
)
from mfm.application.accounting.create_journal import (
    JournalLineInput as ServiceJournalLineInput,
)
from mfm.application.accounting.create_journal import (
    JournalLineResponse as ServiceJournalLineResponse,
)
from mfm.application.accounting.create_journal import (
    JournalResponse as ServiceJournalResponse,
)
from mfm.application.accounting.create_journal import (
    JournalSearchResultResponse as ServiceJournalSearchResultResponse,
)
from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for accounting feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class JournalLineInput:
    account_id: UUID
    side: str
    amount: Decimal | str | int
    currency: str = "DKK"
    description: str | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.account_id, UUID):
            raise ValidationException(f"{field_name}.account_id must be UUID")
        if not isinstance(self.side, str) or not self.side.strip():
            raise ValidationException(f"{field_name}.side must be a non-empty string")
        if isinstance(self.amount, bool) or isinstance(self.amount, float):
            raise ValidationException(f"{field_name}.amount must not be bool/float")
        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValidationException(f"{field_name}.currency must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")


@dataclass(frozen=True, slots=True)
class JournalLineResponse:
    account_id: UUID
    side: str
    amount: Decimal
    currency: str
    description: str | None


@dataclass(frozen=True, slots=True)
class JournalResponse:
    journal_id: UUID
    journal_number: str
    posting_date: date
    description: str
    reference: str | None
    status: str
    version: int
    lines: tuple[JournalLineResponse, ...]


@dataclass(frozen=True, slots=True)
class JournalSearchResultResponse:
    journal_id: UUID
    fiscal_year_id: UUID
    journal_number: str
    posting_date: date
    status: str
    reference: str | None


@dataclass(frozen=True, slots=True)
class CreateJournalRequest:
    journal_number: str
    posting_date: date
    description: str
    lines: tuple[JournalLineInput, ...]
    journal_id: UUID | None = None
    reference: str | None = None
    status: str = "DRAFT"

    def validate(self) -> None:
        if not isinstance(self.journal_number, str) or not self.journal_number.strip():
            raise ValidationException("journal_number must be a non-empty string")
        if not isinstance(self.posting_date, date):
            raise ValidationException("posting_date must be date")
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValidationException("description must be a non-empty string")
        if self.journal_id is not None and not isinstance(self.journal_id, UUID):
            raise ValidationException("journal_id must be UUID or None")
        if self.reference is not None and not isinstance(self.reference, str):
            raise ValidationException("reference must be string or None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if not isinstance(self.lines, tuple):
            raise ValidationException("lines must be tuple")
        if len(self.lines) < 2:
            raise ValidationException("lines must contain at least two entries")

        for index, line in enumerate(self.lines):
            line.validate(field_name=f"lines[{index}]")


@dataclass(frozen=True, slots=True)
class CreateJournalResponse:
    journal: JournalResponse


class CreateJournalService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_journal_line_input(value: JournalLineInput) -> ServiceJournalLineInput:
    return ServiceJournalLineInput(
        account_id=value.account_id,
        side=value.side,
        amount=value.amount,
        currency=value.currency,
        description=value.description,
    )


def to_feature_journal_line_response(response: ServiceJournalLineResponse) -> JournalLineResponse:
    return JournalLineResponse(
        account_id=response.account_id,
        side=response.side,
        amount=response.amount,
        currency=response.currency,
        description=response.description,
    )


def to_feature_journal_response(response: ServiceJournalResponse) -> JournalResponse:
    return JournalResponse(
        journal_id=response.journal_id,
        journal_number=response.journal_number,
        posting_date=response.posting_date,
        description=response.description,
        reference=response.reference,
        status=response.status,
        version=response.version,
        lines=tuple(to_feature_journal_line_response(item) for item in response.lines),
    )


def to_feature_journal_search_result_response(
    response: ServiceJournalSearchResultResponse,
) -> JournalSearchResultResponse:
    return JournalSearchResultResponse(
        journal_id=response.journal_id,
        fiscal_year_id=response.fiscal_year_id,
        journal_number=response.journal_number,
        posting_date=response.posting_date,
        status=response.status,
        reference=response.reference,
    )


class CreateJournalFeature:
    """Feature facade for journal creation."""

    def __init__(self, *, service: CreateJournalService) -> None:
        self._service = service

    def execute(self, request: CreateJournalRequest) -> CreateJournalResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    journal_number=request.journal_number,
                    posting_date=request.posting_date,
                    description=request.description,
                    lines=tuple(to_service_journal_line_input(item) for item in request.lines),
                    journal_id=request.journal_id,
                    reference=request.reference,
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
            raise RepositoryException("Create journal feature failed") from exc

        return CreateJournalResponse(
            journal=to_feature_journal_response(service_response.journal)
        )
