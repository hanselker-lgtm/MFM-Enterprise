"""Invoice line alias for membership billing capability.

The capability reuses finance invoice line logic to avoid duplication.
"""

from mfm.domain.finance.invoice_line import InvoiceLine

__all__ = ["InvoiceLine"]
