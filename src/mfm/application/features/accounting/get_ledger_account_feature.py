"""Get ledger account feature facade following Public API Standard."""

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
from mfm.application.accounting.get_ledger_account import (
    GetLedgerAccountRequest as ServiceRequest,
)
from mfm.application.accounting.get_ledger_account import (
    GetLedgerAccountResponse as ServiceResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import RepositoryException
from mfm.application.features.accounting.create_journal_feature import ValidationException
from mfm.application.features.accounting.create_ledger_account_feature import (
    LedgerAccountResponse,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    to_feature_ledger_account_response,
)


@dataclass(frozen=True, slots=True)
class GetLedgerAccountRequest:
    account_id: UUID

    def validate(self) -> None:
        if not isinstance(self.account_id, UUID):
            raise ValidationException("account_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetLedgerAccountResponse:
    account: LedgerAccountResponse


class GetLedgerAccountService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetLedgerAccountFeature:
    """Feature facade for ledger account retrieval."""

    def __init__(self, *, service: GetLedgerAccountService) -> None:
        self._service = service

    def execute(self, request: GetLedgerAccountRequest) -> GetLedgerAccountResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(account_id=request.account_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get ledger account feature failed") from exc

        return GetLedgerAccountResponse(
            account=to_feature_ledger_account_response(service_response.account)
        )
