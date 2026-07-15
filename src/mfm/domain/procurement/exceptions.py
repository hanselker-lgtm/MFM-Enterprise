"""Domain exceptions for procurement."""


class ProcurementError(Exception):
    """Base exception for procurement domain errors."""


class InvalidPurchaseOrderError(ProcurementError):
    """Raised when purchase order invariants are violated."""


class InvalidPurchaseOrderReferenceError(ProcurementError):
    """Raised when purchase order reference data is invalid."""


class InvalidSupplierReferenceError(ProcurementError):
    """Raised when supplier reference data is invalid."""


class InvalidPurchaseOrderLineError(ProcurementError):
    """Raised when purchase order line data is invalid."""


class InvalidPurchaseReceiptError(ProcurementError):
    """Raised when purchase receipt data is invalid."""


class InvalidPurchaseOrderLifecycleError(ProcurementError):
    """Raised when purchase order lifecycle transitions are invalid."""


class InvalidPurchaseOrderMoneyError(ProcurementError):
    """Raised when purchase order money values are invalid."""


class PurchaseOrderSerializationError(ProcurementError):
    """Raised when purchase order restoration data is invalid."""
