"""List ledger accounts feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from mfm.application.accounting.create_journal import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.accounting.create_journal import (
    ValidationException as ServiceValidationException,
)
from mfm.application.accounting.list_ledger_accounts import (
    ListLedgerAccountsRequest as ServiceRequest,
)
from mfm.application.accounting.list_ledger_accounts import (
    ListLedgerAccountsResponse as ServiceResponse,
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
class ListLedgerAccountsRequest:
    active_only: bool = False

    def validate(self) -> None:
        if not isinstance(self.active_only, bool):
            raise ValidationException("active_only must be bool")


@dataclass(frozen=True, slots=True)
class ListLedgerAccountsResponse:
    accounts: tuple[LedgerAccountResponse, ...]


class ListLedgerAccountsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListLedgerAccountsFeature:
    """Feature facade for ledger account listing."""

    def __init__(self, *, service: ListLedgerAccountsService) -> None:
        self._service = service

    def execute(self, request: ListLedgerAccountsRequest) -> ListLedgerAccountsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(active_only=request.active_only)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List ledger accounts feature failed") from exc

        return ListLedgerAccountsResponse(
            accounts=tuple(
                to_feature_ledger_account_response(item)
                for item in service_response.accounts
            )
        )
