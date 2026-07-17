"""Payment alias for membership billing capability.

The capability reuses finance payment logic to avoid duplication.
"""

from mfm.domain.finance.payment import Payment

__all__ = ["Payment"]
