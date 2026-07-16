"""List LedgerAccounts use case."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.accounting.create_ledger_account import LedgerAccountResponse
from mfm.application.accounting.create_ledger_account import to_ledger_account_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.repositories import LedgerAccountRepository


@dataclass(frozen=True, slots=True)
class ListLedgerAccountsRequest:
    active_only: bool = False

    def validate(self) -> None:
        if not isinstance(self.active_only, bool):
            raise ValidationException("active_only must be bool")


@dataclass(frozen=True, slots=True)
class ListLedgerAccountsResponse:
    accounts: tuple[LedgerAccountResponse, ...]


class ListLedgerAccountsUseCase:
    """List ledger accounts through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListLedgerAccountsRequest) -> ListLedgerAccountsResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: LedgerAccountRepository = uow.ledger_account_repository
                if request.active_only:
                    accounts = repository.list_active()
                else:
                    accounts = repository.list()
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("List ledger accounts failed") from exc

        return ListLedgerAccountsResponse(
            accounts=tuple(to_ledger_account_response(item) for item in accounts)
        )
