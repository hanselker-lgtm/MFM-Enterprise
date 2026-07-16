"""Create LedgerAccount use case and shared ledger account DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.application.accounting.create_journal import ApplicationException
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.exceptions import AccountingError
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.repositories import LedgerAccountRepository


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


class CreateLedgerAccountUseCase:
    """Create ledger account aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateLedgerAccountRequest) -> CreateLedgerAccountResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: LedgerAccountRepository = uow.ledger_account_repository
                account = LedgerAccount(
                    id=request.account_id or uuid4(),
                    account_number=AccountNumber(request.account_number),
                    name=request.name,
                    account_type=AccountType(request.account_type.strip().upper()),
                    normal_balance=NormalBalance(request.normal_balance.strip().upper()),
                    active=request.active,
                    locked=request.locked,
                    has_postings=request.has_postings,
                )
                repository.add(account)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except AccountingError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create ledger account failed") from exc

        return CreateLedgerAccountResponse(account=to_ledger_account_response(account))


def to_ledger_account_response(value: LedgerAccount) -> LedgerAccountResponse:
    return LedgerAccountResponse(
        account_id=value.id,
        account_number=value.account_number.value,
        name=value.name,
        account_type=value.account_type.value,
        normal_balance=value.normal_balance.value,
        active=value.active,
        locked=value.locked,
        has_postings=value.has_postings,
    )
