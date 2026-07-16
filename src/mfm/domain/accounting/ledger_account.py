"""Ledger account aggregate for accounting domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.exceptions import DuplicateAccountNumberError
from mfm.domain.accounting.exceptions import InvalidLedgerAccountNameError
from mfm.domain.accounting.exceptions import InvalidLedgerAccountReferenceError
from mfm.domain.accounting.exceptions import LockedLedgerAccountError
from mfm.domain.accounting.normal_balance import NormalBalance


@dataclass(slots=True)
class LedgerAccount(AggregateRoot):
    """Aggregate root representing a chart-of-accounts ledger account."""

    name: str
    account_type: AccountType
    normal_balance: NormalBalance
    active: bool = True
    locked: bool = False
    has_postings: bool = False
    id: UUID = field(default_factory=uuid4)
    _account_number: AccountNumber = field(default_factory=lambda: AccountNumber(""), repr=False)

    _registered_numbers: ClassVar[set[str]] = set()

    def __init__(
        self,
        *,
        account_number: AccountNumber,
        name: str,
        account_type: AccountType,
        normal_balance: NormalBalance,
        active: bool = True,
        locked: bool = False,
        has_postings: bool = False,
        id: UUID | None = None,
    ) -> None:
        self._account_number = account_number
        self.name = name
        self.account_type = account_type
        self.normal_balance = normal_balance
        self.active = active
        self.locked = locked
        self.has_postings = has_postings
        self.id = uuid4() if id is None else id
        self.__post_init__()

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, UUID):
            raise InvalidLedgerAccountReferenceError("id must be a UUID")

        if not isinstance(self._account_number, AccountNumber):
            raise InvalidLedgerAccountReferenceError(
                "account_number must be AccountNumber"
            )

        if self._account_number.value in self._registered_numbers:
            raise DuplicateAccountNumberError("account_number must be unique")
        self._registered_numbers.add(self._account_number.value)

        if not isinstance(self.name, str) or not self.name.strip():
            raise InvalidLedgerAccountNameError("name must be a non-empty string")
        self.name = self.name.strip()

        if not isinstance(self.account_type, AccountType):
            raise InvalidLedgerAccountReferenceError(
                "account_type must be AccountType"
            )

        if not isinstance(self.normal_balance, NormalBalance):
            raise InvalidLedgerAccountReferenceError(
                "normal_balance must be NormalBalance"
            )

    @property
    def account_number(self) -> AccountNumber:
        return self._account_number

    def activate(self) -> None:
        self._assert_mutable()
        self.active = True

    def deactivate(self) -> None:
        self._assert_mutable()
        self.active = False

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def rename(self, *, name: str) -> None:
        self._assert_mutable()
        if not isinstance(name, str) or not name.strip():
            raise InvalidLedgerAccountNameError("name must be a non-empty string")
        self.name = name.strip()

    def can_post(self) -> bool:
        return self.active and not self.locked

    def mark_posted(self) -> None:
        self.has_postings = True

    def _assert_mutable(self) -> None:
        if self.locked:
            raise LockedLedgerAccountError("locked account cannot be changed")
