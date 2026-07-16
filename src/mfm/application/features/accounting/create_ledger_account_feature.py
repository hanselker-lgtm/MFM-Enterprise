"""Create ledger account feature facade following Public API Standard."""

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
from mfm.application.accounting.create_ledger_account import (
    CreateLedgerAccountRequest as ServiceRequest,
)
from mfm.application.accounting.create_ledger_account import (
    CreateLedgerAccountResponse as ServiceResponse,
)
from mfm.application.accounting.create_ledger_account import (
    LedgerAccountResponse as ServiceLedgerAccountResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException


@dataclass(frozen=True, slots=True)
class LedgerAccountResponse:
    account_id: UUID
    account_number: str
    name: str
    account_type: str
    normal_balance: str
    active: bool
    locked: bool
    has_postings: bool


@dataclass(frozen=True, slots=True)
class CreateLedgerAccountRequest:
    account_number: str
    name: str
    account_type: str
    normal_balance: str
    account_id: UUID | None = None
    active: bool = True
    locked: bool = False
    has_postings: bool = False

    def validate(self) -> None:
        if not isinstance(self.account_number, str) or not self.account_number.strip():
            raise ValidationException("account_number must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.account_type, str) or not self.account_type.strip():
            raise ValidationException("account_type must be a non-empty string")
        if not isinstance(self.normal_balance, str) or not self.normal_balance.strip():
            raise ValidationException("normal_balance must be a non-empty string")
        if self.account_id is not None and not isinstance(self.account_id, UUID):
            raise ValidationException("account_id must be UUID or None")
        if not isinstance(self.active, bool):
            raise ValidationException("active must be bool")
        if not isinstance(self.locked, bool):
            raise ValidationException("locked must be bool")
        if not isinstance(self.has_postings, bool):
            raise ValidationException("has_postings must be bool")


@dataclass(frozen=True, slots=True)
class CreateLedgerAccountResponse:
    account: LedgerAccountResponse


class CreateLedgerAccountService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_feature_ledger_account_response(response: ServiceLedgerAccountResponse) -> LedgerAccountResponse:
    return LedgerAccountResponse(
        account_id=response.account_id,
        account_number=response.account_number,
        name=response.name,
        account_type=response.account_type,
        normal_balance=response.normal_balance,
        active=response.active,
        locked=response.locked,
        has_postings=response.has_postings,
    )


class CreateLedgerAccountFeature:
    """Feature facade for ledger account creation."""

    def __init__(self, *, service: CreateLedgerAccountService) -> None:
        self._service = service

    def execute(self, request: CreateLedgerAccountRequest) -> CreateLedgerAccountResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    account_number=request.account_number,
                    name=request.name,
                    account_type=request.account_type,
                    normal_balance=request.normal_balance,
                    account_id=request.account_id,
                    active=request.active,
                    locked=request.locked,
                    has_postings=request.has_postings,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create ledger account feature failed") from exc

        return CreateLedgerAccountResponse(
            account=to_feature_ledger_account_response(service_response.account)
        )
