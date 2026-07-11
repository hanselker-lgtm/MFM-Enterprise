"""Domain exceptions for Maintenance capability."""


class MaintenanceError(Exception):
    """Base exception for maintenance domain errors."""


class InvalidMaintenanceTargetError(MaintenanceError):
    """Raised when maintenance target data is invalid."""


class InvalidMaintenancePlanStateError(MaintenanceError):
    """Raised when maintenance plan state rules are violated."""


class MaintenanceRequirementNotFoundError(MaintenanceError):
    """Raised when requirement is not found in the plan."""


class DuplicateMaintenanceRequirementError(MaintenanceError):
    """Raised when duplicate requirement invariants are violated."""


class InvalidMaintenanceIntervalError(MaintenanceError):
    """Raised when maintenance interval is invalid."""


class InvalidMaintenanceDueCalculationError(MaintenanceError):
    """Raised when due calculation inputs are invalid."""


class InvalidMaintenanceRequirementError(MaintenanceError):
    """Raised when requirement data or transitions are invalid."""


class InvalidWorkOrderLifecycleError(MaintenanceError):
    """Raised when work order lifecycle transition is invalid."""


class InvalidWorkOrderChronologyError(MaintenanceError):
    """Raised when work order chronology is invalid."""


class InvalidPerformerReferenceError(MaintenanceError):
    """Raised when performer reference is invalid."""
