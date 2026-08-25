"""Domain exceptions for finance."""


class FinanceError(Exception):
    """Base exception for finance domain errors."""


class InvalidCurrencyError(FinanceError):
    """Raised when a currency value is invalid."""


class InvalidMoneyAmountError(FinanceError):
    """Raised when a money amount is invalid."""


class CurrencyMismatchError(FinanceError):
    """Raised when money values from different currencies are mixed."""


class MoneySerializationError(FinanceError):
    """Raised when money serialization data is invalid."""


class InvalidContingentPlanReferenceError(FinanceError):
    """Raised when contingent plan references are invalid."""


class InvalidContingentPlanAmountError(FinanceError):
    """Raised when contingent plan amount violates business rules."""


class InvalidContingentPlanDatesError(FinanceError):
    """Raised when contingent plan validity dates are inconsistent."""


class OverlappingContingentPlanError(FinanceError):
    """Raised when contingent plan validity periods overlap."""


class MultipleActiveContingentPlansError(FinanceError):
    """Raised when more than one active contingent plan exists."""


class InvalidInvoiceReferenceError(FinanceError):
    """Raised when invoice references are invalid."""


class InvalidInvoiceDatesError(FinanceError):
    """Raised when invoice issue/due dates are inconsistent."""


class InvalidInvoiceLineError(FinanceError):
    """Raised when invoice line values are invalid."""


class EmptyInvoiceError(FinanceError):
    """Raised when an invoice has no lines."""


class InvalidInvoiceTransitionError(FinanceError):
    """Raised when an invoice status transition is invalid."""


class InvoicePaymentError(FinanceError):
    """Raised when invoice payment registration is invalid."""


class InvoiceOverpaymentError(InvoicePaymentError):
    """Raised when payment exceeds outstanding amount."""


class InvalidPaymentReferenceError(FinanceError):
    """Raised when payment references are invalid."""


class InvalidPaymentAmountError(FinanceError):
    """Raised when payment amount violates business rules."""


class InvalidPaymentDatesError(FinanceError):
    """Raised when payment dates are inconsistent with invoice dates."""


class InvalidPaymentTransitionError(FinanceError):
    """Raised when payment status transition is invalid."""
