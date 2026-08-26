"""Toolbar for project workspace operations and list controls."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QWidget

from mfm.presentation.projects.project_viewmodels import ProjectListFilterViewModel
from mfm.presentation.projects.project_viewmodels import ProjectSortField


class ProjectToolbar(QWidget):
    """Pure view component for project list interaction controls."""

    def __init__(
        self,
        *,
        on_search: Callable[[], None],
        on_refresh: Callable[[], None],
        on_create_project: Callable[[], None],
    ) -> None:
        super().__init__()
        self._on_search = on_search
        self._on_refresh = on_refresh
        self._on_create = on_create_project

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("Søg projekter")
        self._search_input.returnPressed.connect(self._on_search)

        self._status_filter = QComboBox()
        _status_labels = {
            "ALL": "Alle",
            "DRAFT": "Kladde",
            "ACTIVE": "Aktiv",
            "COMPLETED": "Afsluttet",
            "ARCHIVED": "Arkiveret",
        }
        for value, label in _status_labels.items():
            self._status_filter.addItem(label, value)

        self._sort_filter = QComboBox()
        _sort_labels = {
            ProjectSortField.PROJECT_NUMBER: "Projektnummer",
            ProjectSortField.NAME: "Navn",
            ProjectSortField.STATUS: "Status",
            ProjectSortField.PRIORITY: "Prioritet",
            ProjectSortField.CREATED_AT: "Oprettet",
        }
        for field in ProjectSortField:
            self._sort_filter.addItem(_sort_labels.get(field, field.value), field)

        self._order_filter = QComboBox()
        self._order_filter.addItem("Faldende", "DESC")
        self._order_filter.addItem("Stigende", "ASC")

        search_button = QPushButton("Søg")
        search_button.clicked.connect(self._on_search)

        refresh_button = QPushButton("Opdatér")
        refresh_button.setShortcut("F5")
        refresh_button.clicked.connect(self._on_refresh)

        create_button = QPushButton("Opret projekt")
        create_button.clicked.connect(self._on_create)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        layout.addWidget(QLabel("Søg"))
        layout.addWidget(self._search_input, 2)
        layout.addWidget(QLabel("Status"))
        layout.addWidget(self._status_filter)
        layout.addWidget(QLabel("Sortér"))
        layout.addWidget(self._sort_filter)
        layout.addWidget(self._order_filter)
        layout.addWidget(search_button)
        layout.addWidget(refresh_button)
        layout.addWidget(create_button)

    def filters(self, *, page: int = 1, page_size: int = 25) -> ProjectListFilterViewModel:
        sort_field = self._sort_filter.currentData()
        if not isinstance(sort_field, ProjectSortField):
            sort_field = ProjectSortField.CREATED_AT

        return ProjectListFilterViewModel(
            text=self._search_input.text().strip(),
            status=self._status_filter.currentData(),
            sort_by=sort_field,
            descending=self._order_filter.currentData() == "DESC",
            page=page,
            page_size=page_size,
        )
