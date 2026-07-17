"""Toolbar for accounting workspace operations and list controls."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QWidget

from mfm.presentation.accounting.accounting_viewmodels import JournalListFilterViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalSortField


class AccountingToolbar(QWidget):
    """Pure view component for accounting list interaction controls."""

    def __init__(
        self,
        *,
        on_search: Callable[[], None],
        on_refresh: Callable[[], None],
        on_create_journal: Callable[[], None],
        on_post_journal: Callable[[], None],
    ) -> None:
        super().__init__()
        self._on_search = on_search
        self._on_refresh = on_refresh
        self._on_create_journal = on_create_journal
        self._on_post_journal = on_post_journal

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("Search journals")

        self._status_filter = QComboBox()
        self._status_filter.addItems(["ALL", "DRAFT", "POSTED", "REVERSED"])

        self._sort_filter = QComboBox()
        for field in JournalSortField:
            self._sort_filter.addItem(field.value, field)

        self._order_filter = QComboBox()
        self._order_filter.addItems(["DESC", "ASC"])

        search_button = QPushButton("Search")
        search_button.clicked.connect(self._on_search)

        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self._on_refresh)

        create_button = QPushButton("Create Journal")
        create_button.clicked.connect(self._on_create_journal)

        post_button = QPushButton("Post Journal")
        post_button.clicked.connect(self._on_post_journal)

        layout = QHBoxLayout(self)
        layout.addWidget(QLabel("Search"))
        layout.addWidget(self._search_input, 2)
        layout.addWidget(QLabel("Status"))
        layout.addWidget(self._status_filter)
        layout.addWidget(QLabel("Sort"))
        layout.addWidget(self._sort_filter)
        layout.addWidget(self._order_filter)
        layout.addWidget(search_button)
        layout.addWidget(refresh_button)
        layout.addWidget(create_button)
        layout.addWidget(post_button)

    def filters(self, *, page: int = 1, page_size: int = 25) -> JournalListFilterViewModel:
        sort_field = self._sort_filter.currentData()
        if not isinstance(sort_field, JournalSortField):
            sort_field = JournalSortField.POSTING_DATE

        return JournalListFilterViewModel(
            text=self._search_input.text().strip(),
            status=self._status_filter.currentText(),
            sort_by=sort_field,
            descending=self._order_filter.currentText() == "DESC",
            page=page,
            page_size=page_size,
        )
