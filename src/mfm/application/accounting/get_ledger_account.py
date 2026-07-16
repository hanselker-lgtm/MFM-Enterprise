"""Get LedgerAccount use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.accounting.create_ledger_account import LedgerAccountResponse
from mfm.application.accounting.create_ledger_account import to_ledger_account_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.repositories import LedgerAccountRepository


@dataclass(frozen=True, slots=True)
class GetLedgerAccountRequest:
    account_id: UUID

    def validate(self) -> None:
        if not isinstance(self.account_id, UUID):
            raise ValidationException("account_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetLedgerAccountResponse:
    account: LedgerAccountResponse


class GetLedgerAccountUseCase:
    """Load one ledger account through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetLedgerAccountRequest) -> GetLedgerAccountResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: LedgerAccountRepository = uow.ledger_account_repository
                account = repository.get_by_id(request.account_id)
                if account is None:
                    raise BusinessRuleViolation(
                        f"Ledger account {request.account_id} does not exist"
                    )
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get ledger account failed") from exc

        return GetLedgerAccountResponse(account=to_ledger_account_response(account))
