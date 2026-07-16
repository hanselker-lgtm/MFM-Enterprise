"""Chart of accounts aggregate for accounting domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.accounting.account_category import AccountCategory
from mfm.domain.accounting.account_group import AccountGroup
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.exceptions import AccountHasPostingsError
from mfm.domain.accounting.exceptions import DuplicateAccountInChartError
from mfm.domain.accounting.exceptions import InvalidAccountGroupError
from mfm.domain.accounting.exceptions import InvalidChartOfAccountsError
from mfm.domain.accounting.exceptions import LockedChartOfAccountsError
from mfm.domain.accounting.ledger_account import LedgerAccount


@dataclass(slots=True)
class ChartOfAccounts(AggregateRoot):
    """Aggregate root representing a chart of accounts."""

    name: str
    version: str
    active: bool = True
    accounts: list[LedgerAccount] = field(default_factory=list)
    locked: bool = False
    id: UUID = field(default_factory=uuid4)

    _groups_by_account_id: dict[UUID, AccountGroup] = field(
        default_factory=dict, init=False, repr=False
    )
    _categories_by_account_id: dict[UUID, AccountCategory] = field(
        default_factory=dict, init=False, repr=False
    )

    def __post_init__(self) -> None:
        provided_version = self.version
        AggregateRoot.__init__(self)
        self.version = provided_version

        if not isinstance(self.id, UUID):
            raise InvalidChartOfAccountsError("id must be a UUID")

        if not isinstance(self.name, str) or not self.name.strip():
            raise InvalidChartOfAccountsError("name must be a non-empty string")
        self.name = self.name.strip()

        if not isinstance(self.version, str) or not self.version.strip():
            raise InvalidChartOfAccountsError("version must be a non-empty string")
        self.version = self.version.strip()

        if not isinstance(self.accounts, list):
            raise InvalidChartOfAccountsError("accounts must be a list")

        for account in self.accounts:
            if not isinstance(account, LedgerAccount):
                raise InvalidChartOfAccountsError("accounts must contain LedgerAccount")

        self.validate(require_non_empty=False)

    def add_account(
        self,
        account: LedgerAccount,
        *,
        group: AccountGroup | None = None,
        category: AccountCategory | None = None,
    ) -> None:
        self._assert_mutable()
        if not isinstance(account, LedgerAccount):
            raise InvalidChartOfAccountsError("account must be LedgerAccount")

        if account in self.accounts:
            raise DuplicateAccountInChartError("account can only exist once in chart")

        if self.contains(account.account_number):
            raise DuplicateAccountInChartError("account_number must be unique in chart")

        if group is not None and not isinstance(group, AccountGroup):
            raise InvalidAccountGroupError("group must be AccountGroup")

        if category is not None and not isinstance(category, AccountCategory):
            raise InvalidAccountGroupError("category must be AccountCategory")

        self.accounts.append(account)
        if group is not None:
            self._groups_by_account_id[account.id] = group
        if category is not None:
            self._categories_by_account_id[account.id] = category

    def remove_account(self, account_number: AccountNumber) -> None:
        self._assert_mutable()
        account = self.find_account(account_number)
        if account is None:
            raise InvalidChartOfAccountsError("account not found")

        if account.has_postings:
            raise AccountHasPostingsError(
                "account can only be removed if it has never been posted"
            )

        self.accounts.remove(account)
        self._groups_by_account_id.pop(account.id, None)
        self._categories_by_account_id.pop(account.id, None)

    def find_account(self, account_number: AccountNumber) -> LedgerAccount | None:
        if not isinstance(account_number, AccountNumber):
            raise InvalidChartOfAccountsError("account_number must be AccountNumber")

        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def contains(self, account_number: AccountNumber) -> bool:
        return self.find_account(account_number) is not None

    def validate(self, *, require_non_empty: bool = True) -> None:
        if require_non_empty and not self.accounts:
            raise InvalidChartOfAccountsError("chart must contain at least one account")

        seen_numbers: set[AccountNumber] = set()
        seen_ids: set[UUID] = set()
        for account in self.accounts:
            if account.account_number in seen_numbers:
                raise DuplicateAccountInChartError("duplicate account_number in chart")
            if account.id in seen_ids:
                raise DuplicateAccountInChartError("duplicate account in chart")
            seen_numbers.add(account.account_number)
            seen_ids.add(account.id)

    def activate(self) -> None:
        self._assert_mutable()
        self.active = True

    def deactivate(self) -> None:
        self._assert_mutable()
        self.active = False

    def lock(self) -> None:
        self.locked = True

    def _assert_mutable(self) -> None:
        if self.locked:
            raise LockedChartOfAccountsError("locked chart of accounts cannot be changed")
