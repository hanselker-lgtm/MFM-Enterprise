"""Domain exceptions for the Inventory capability."""


class InventoryError(Exception):
    """Base exception for inventory domain errors."""


class InvalidInventoryItemError(InventoryError):
    """Raised when inventory item aggregate invariants are violated."""


class InvalidInventoryReferenceError(InventoryError):
    """Raised when item reference data is invalid."""


class InvalidInventoryQuantityError(InventoryError):
    """Raised when stock quantity data is invalid."""


class InvalidUnitOfMeasureError(InventoryError):
    """Raised when unit of measure data is invalid."""


class InvalidStockLocationError(InventoryError):
    """Raised when stock location data is invalid."""


class InvalidStockMovementError(InventoryError):
    """Raised when stock movement data is invalid."""


class InvalidInventoryAdjustmentError(InventoryError):
    """Raised when a stock adjustment request is invalid."""


class InvalidInventoryLifecycleError(InventoryError):
    """Raised when inventory item lifecycle transitions are invalid."""


class InsufficientStockError(InventoryError):
    """Raised when an issue would make stock negative."""