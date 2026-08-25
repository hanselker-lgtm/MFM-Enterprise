"""Domain exceptions for Contingent."""


class ContingentError(Exception):
    """Base exception for contingent domain errors."""


class InvalidContingentReferenceError(ContingentError):
    """Raised when contingent references are invalid."""


class InvalidContingentAmountError(ContingentError):
    """Raised when contingent amount is invalid."""


class InvalidContingentDatesError(ContingentError):
    """Raised when contingent validity dates are invalid."""


class MultipleActiveContingentPlansError(ContingentError):
    """Raised when more than one active contingent plan exists."""


class OverlappingContingentPlanError(ContingentError):
    """Raised when contingent plan validity periods overlap."""


class ContingentPlanNotFoundError(ContingentError):
    """Raised when a contingent plan cannot be found."""
