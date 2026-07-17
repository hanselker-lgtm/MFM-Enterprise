"""Invoice alias for membership billing capability.

The capability reuses finance invoice logic to avoid duplication.
"""

from mfm.domain.finance.invoice import Invoice

__all__ = ["Invoice"]
