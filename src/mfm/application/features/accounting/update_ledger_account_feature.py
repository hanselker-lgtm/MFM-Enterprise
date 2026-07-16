"""Update ledger account feature facade following Public API Standard."""

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
from mfm.application.accounting.update_ledger_account import (
    UpdateLedgerAccountRequest as ServiceRequest,
)
from mfm.application.accounting.update_ledger_account import (
    UpdateLedgerAccountResponse as ServiceResponse,
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
class UpdateLedgerAccountRequest:
    account_id: UUID
    name: str | None = None
    active: bool | None = None
    locked: bool | None = None

    def validate(self) -> None:
        if not isinstance(self.account_id, UUID):
            raise ValidationException("account_id must be UUID")
        if self.name is not None and (
            not isinstance(self.name, str) or not self.name.strip()
        ):
            raise ValidationException("name must be a non-empty string or None")
        if self.active is not None and not isinstance(self.active, bool):
            raise ValidationException("active must be bool or None")
        if self.locked is not None and not isinstance(self.locked, bool):
            raise ValidationException("locked must be bool or None")


@dataclass(frozen=True, slots=True)
class UpdateLedgerAccountResponse:
    account: LedgerAccountResponse


class UpdateLedgerAccountService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateLedgerAccountFeature:
    """Feature facade for ledger account updates."""

    def __init__(self, *, service: UpdateLedgerAccountService) -> None:
        self._service = service

    def execute(self, request: UpdateLedgerAccountRequest) -> UpdateLedgerAccountResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    account_id=request.account_id,
                    name=request.name,
                    active=request.active,
                    locked=request.locked,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update ledger account feature failed") from exc

        return UpdateLedgerAccountResponse(
            account=to_feature_ledger_account_response(service_response.account)
        )
