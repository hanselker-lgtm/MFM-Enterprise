"""Update LedgerAccount use case."""

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
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.repositories import LedgerAccountRepository


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


class UpdateLedgerAccountUseCase:
    """Update mutable ledger account details."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: UpdateLedgerAccountRequest) -> UpdateLedgerAccountResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: LedgerAccountRepository = uow.ledger_account_repository
                account = repository.get_by_id(request.account_id)
                if account is None:
                    raise BusinessRuleViolation(
                        f"Ledger account {request.account_id} does not exist"
                    )

                if request.name is not None:
                    account.rename(name=request.name)
                if request.active is True:
                    account.activate()
                elif request.active is False:
                    account.deactivate()

                if request.locked is True:
                    account.lock()
                elif request.locked is False:
                    account.unlock()

                repository.update(account)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update ledger account failed") from exc

        return UpdateLedgerAccountResponse(account=to_ledger_account_response(account))
