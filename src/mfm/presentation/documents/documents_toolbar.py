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
        self._search_input.setPlaceholderText("Søg dokumenter")
        self._search_input.returnPressed.connect(self._on_search)

        self._status_filter = QComboBox()
        _status_labels = {
            "ALL": "Alle",
            "DRAFT": "Kladde",
            "ACTIVE": "Aktiv",
            "ARCHIVED": "Arkiveret",
            "DISPOSED": "Kasseret",
        }
        for value, label in _status_labels.items():
            self._status_filter.addItem(label, value)

        self._target_filter = QComboBox()
        _target_labels = {
            "ALL": "Alle",
            "PROJECTS": "Projekter",
            "ORGANIZATIONS": "Organisationer",
            "ACCOUNTING": "Bogføring",
            "MAINTENANCE": "Vedligehold",
        }
        for value, label in _target_labels.items():
            self._target_filter.addItem(label, value)

        self._sort_filter = QComboBox()
        _sort_labels = {
            DocumentSortField.DOCUMENT_NUMBER: "Dokumentnummer",
            DocumentSortField.CREATED_AT: "Oprettet",
            DocumentSortField.STATUS: "Status",
            DocumentSortField.DOCUMENT_TYPE: "Dokumenttype",
        }
        for field in DocumentSortField:
            self._sort_filter.addItem(_sort_labels.get(field, field.value), field)

        self._order_filter = QComboBox()
        self._order_filter.addItem("Faldende", "DESC")
        self._order_filter.addItem("Stigende", "ASC")

        search_button = QPushButton("Søg")
        search_button.clicked.connect(self._on_search)

        refresh_button = QPushButton("Opdatér")
        refresh_button.setShortcut("F5")
        refresh_button.clicked.connect(self._on_refresh)

        create_button = QPushButton("Opret dokument")
        create_button.clicked.connect(self._on_create_document)

        register_version_button = QPushButton("Registrér version")
        register_version_button.clicked.connect(self._on_register_version)

        archive_button = QPushButton("Arkivér")
        archive_button.clicked.connect(self._on_archive_document)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        layout.addWidget(QLabel("Søg"))
        layout.addWidget(self._search_input, 2)
        layout.addWidget(QLabel("Status"))
        layout.addWidget(self._status_filter)
        layout.addWidget(QLabel("Mål"))
        layout.addWidget(self._target_filter)
        layout.addWidget(QLabel("Sortér"))
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
            status=self._status_filter.currentData(),
            target_capability=self._target_filter.currentData(),
            sort_by=sort_field,
            descending=self._order_filter.currentData() == "DESC",
            page=page,
            page_size=page_size,
        )
