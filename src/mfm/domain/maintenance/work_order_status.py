"""Work order status enum."""

from enum import Enum


class WorkOrderStatus(str, Enum):
    """Lifecycle state of work order aggregate."""

    PLANNED = "PLANNED"
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
