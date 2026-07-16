"""Domain exceptions for accounting."""


class AccountingError(Exception):
    """Base exception for accounting domain errors."""


class InvalidJournalReferenceError(AccountingError):
    """Raised when journal references are invalid."""


class InvalidJournalLineError(AccountingError):
    """Raised when a journal line is invalid."""


class InvalidJournalBalanceError(AccountingError):
    """Raised when journal debit and credit totals are not balanced."""


class InvalidJournalTransitionError(AccountingError):
    """Raised when journal status transition is invalid."""


class InvalidLedgerAccountReferenceError(AccountingError):
    """Raised when ledger account references are invalid."""


class InvalidLedgerAccountNameError(AccountingError):
    """Raised when ledger account name is invalid."""


class DuplicateAccountNumberError(AccountingError):
    """Raised when account number already exists."""


class LockedLedgerAccountError(AccountingError):
    """Raised when trying to change a locked ledger account."""


class InvalidChartOfAccountsError(AccountingError):
    """Raised when chart of accounts data is invalid."""


class DuplicateAccountInChartError(AccountingError):
    """Raised when account exists more than once in a chart."""


class LockedChartOfAccountsError(AccountingError):
    """Raised when trying to change a locked chart of accounts."""


class AccountHasPostingsError(AccountingError):
    """Raised when trying to remove account that has postings."""


class InvalidAccountGroupError(AccountingError):
    """Raised when an account group/category value is invalid."""


class InvalidFiscalYearError(AccountingError):
    """Raised when fiscal year data is invalid."""


class InvalidFiscalPeriodError(AccountingError):
    """Raised when fiscal period data is invalid."""


class MultipleOpenFiscalYearsError(AccountingError):
    """Raised when trying to keep more than one fiscal year open."""


class ClosedFiscalPeriodError(AccountingError):
    """Raised when trying to post in a closed fiscal period."""


class InvalidFiscalYearTransitionError(AccountingError):
    """Raised when fiscal year status transition is invalid."""


class DuplicateJournalNumberError(AccountingError):
    """Raised when a journal number is reused within one fiscal year."""
