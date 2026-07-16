"""Journal aggregate module."""

from mfm.domain.accounting.journal_entry import JournalEntry


class Journal(JournalEntry):
    """Named aggregate alias for JournalEntry."""
