"""Project list view for the project workspace."""

from __future__ import annotations

from collections.abc import Callable
from uuid import UUID

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.projects.project_viewmodels import ProjectListViewModel


class ProjectListView(QWidget):
    """View-only project list with pagination controls."""

    def __init__(
        self,
        *,
        on_open_project: Callable[[UUID], None],
        on_page_change: Callable[[int], None],
    ) -> None:
        super().__init__()
        self._on_open_project = on_open_project
        self._on_page_change = on_page_change
        self._item_map: dict[int, UUID] = {}

        self._table = QTableWidget(0, 5)
        self._table.setHorizontalHeaderLabels(["Project #", "Name", "Status", "Priority", "Created"])
        self._table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self._table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._table.itemDoubleClicked.connect(self._open_selected)

        self._page_label = QLabel("Page 1 / 1")
        self._prev_page = QPushButton("Prev")
        self._next_page = QPushButton("Next")
        self._prev_page.clicked.connect(lambda: self._on_page_change(-1))
        self._next_page.clicked.connect(lambda: self._on_page_change(1))

        footer = QHBoxLayout()
        footer.addWidget(self._prev_page)
        footer.addWidget(self._next_page)
        footer.addStretch(1)
        footer.addWidget(self._page_label)

        layout = QVBoxLayout(self)
        layout.addWidget(self._table)
        layout.addLayout(footer)

    def set_view_model(self, vm: ProjectListViewModel) -> None:
        self._table.setRowCount(len(vm.items))
        self._item_map.clear()

        for row, item in enumerate(vm.items):
            self._item_map[row] = item.project_id
            self._set_cell(row, 0, item.project_number)
            self._set_cell(row, 1, item.name)
            self._set_cell(row, 2, item.status)
            self._set_cell(row, 3, item.priority)
            self._set_cell(row, 4, item.created_at.isoformat() if item.created_at is not None else "")

        self._page_label.setText(
            f"Page {vm.pagination.page} / {vm.pagination.total_pages} ({vm.pagination.total_items} total)"
        )
        self._prev_page.setEnabled(vm.pagination.has_previous)
        self._next_page.setEnabled(vm.pagination.has_next)

    def _set_cell(self, row: int, column: int, text: str) -> None:
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self._table.setItem(row, column, item)

    def _open_selected(self) -> None:
        row = self._table.currentRow()
        project_id = self._item_map.get(row)
        if project_id is not None:
            self._on_open_project(project_id)
