"""Toolbar for documents workspace operations and list controls."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QWidget

from mfm.presentation.documents.documents_viewmodels import DocumentListFilterViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentSortField


class DocumentsToolbar(QWidget):
    """Pure view component for document list interaction controls."""

    def __init__(
        self,
        *,
        on_search: Callable[[], None],
        on_refresh: Callable[[], None],
        on_create_document: Callable[[], None],
        on_register_version: Callable[[], None],
        on_archive_document: Callable[[], None],
    ) -> None:
        super().__init__()
        self._on_search = on_search
        self._on_refresh = on_refresh
        self._on_create_document = on_create_document
        self._on_register_version = on_register_version
        self._on_archive_document = on_archive_document

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("Search documents")

        self._status_filter = QComboBox()
        self._status_filter.addItems(["ALL", "DRAFT", "ACTIVE", "ARCHIVED", "DISPOSED"])

        self._target_filter = QComboBox()
        self._target_filter.addItems(["ALL", "PROJECTS", "ORGANIZATIONS", "ACCOUNTING", "MAINTENANCE"])

        self._sort_filter = QComboBox()
        for field in DocumentSortField:
            self._sort_filter.addItem(field.value, field)

        self._order_filter = QComboBox()
        self._order_filter.addItems(["DESC", "ASC"])

        search_button = QPushButton("Search")
        search_button.clicked.connect(self._on_search)

        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self._on_refresh)

        create_button = QPushButton("Create Document")
        create_button.clicked.connect(self._on_create_document)

        register_version_button = QPushButton("Register Version")
        register_version_button.clicked.connect(self._on_register_version)

        archive_button = QPushButton("Archive")
        archive_button.clicked.connect(self._on_archive_document)

        layout = QHBoxLayout(self)
        layout.addWidget(QLabel("Search"))
        layout.addWidget(self._search_input, 2)
        layout.addWidget(QLabel("Status"))
        layout.addWidget(self._status_filter)
        layout.addWidget(QLabel("Target"))
        layout.addWidget(self._target_filter)
        layout.addWidget(QLabel("Sort"))
        layout.addWidget(self._sort_filter)
        layout.addWidget(self._order_filter)
        layout.addWidget(search_button)
        layout.addWidget(refresh_button)
        layout.addWidget(create_button)
        layout.addWidget(register_version_button)
        layout.addWidget(archive_button)

    def filters(self, *, page: int = 1, page_size: int = 25) -> DocumentListFilterViewModel:
        sort_field = self._sort_filter.currentData()
        if not isinstance(sort_field, DocumentSortField):
            sort_field = DocumentSortField.CREATED_AT

        return DocumentListFilterViewModel(
            text=self._search_input.text().strip(),
            status=self._status_filter.currentText(),
            target_capability=self._target_filter.currentText(),
            sort_by=sort_field,
            descending=self._order_filter.currentText() == "DESC",
            page=page,
            page_size=page_size,
        )
