"""Journal detail view for accounting workspace."""

from __future__ import annotations

from collections.abc import Callable
from uuid import UUID

from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.accounting.accounting_viewmodels import JournalDetailViewModel


class JournalDetailView(QWidget):
    """View-only detail pane for journal read models."""

    def __init__(
        self,
        *,
        on_open_project: Callable[[UUID], None],
        on_open_fiscal_year: Callable[[UUID], None],
    ) -> None:
        super().__init__()
        self._on_open_project = on_open_project
        self._on_open_fiscal_year = on_open_fiscal_year
        self._current_project_id: UUID | None = None
        self._current_fiscal_year_id: UUID | None = None

        self._journal_info = self._build_group("Journal Information")
        self._project_link = self._build_group("Project Linkage")
        self._fiscal_year = self._build_group("Fiscal Year")
        self._posting = self._build_group("Posting Status")
        self._audit = self._build_group("Audit References")
        self._summary = self._build_group("Reporting Summary")

        self._lines = QTableWidget(0, 5)
        self._lines.setHorizontalHeaderLabels(["Account", "Side", "Amount", "Currency", "Description"])

        self._open_project_button = QPushButton("Open Project")
        self._open_project_button.clicked.connect(self._open_project)
        self._open_fiscal_year_button = QPushButton("Open Fiscal Year")
        self._open_fiscal_year_button.clicked.connect(self._open_fiscal_year)

        nav = QHBoxLayout()
        nav.addWidget(self._open_project_button)
        nav.addWidget(self._open_fiscal_year_button)
        nav.addStretch(1)

        layout = QVBoxLayout(self)
        layout.addWidget(self._journal_info)
        layout.addWidget(self._project_link)
        layout.addWidget(self._fiscal_year)
        layout.addWidget(self._posting)
        layout.addWidget(self._audit)
        layout.addWidget(self._summary)
        layout.addWidget(self._lines)
        layout.addLayout(nav)

    def set_view_model(self, vm: JournalDetailViewModel) -> None:
        self._current_project_id = vm.project_link.project_id
        self._current_fiscal_year_id = vm.fiscal_year.fiscal_year_id

        self._set_group(
            self._journal_info,
            {
                "Journal #": vm.journal.journal_number,
                "Posting Date": vm.journal.posting_date.isoformat(),
                "Description": vm.journal.description,
            },
        )
        self._set_group(
            self._project_link,
            {
                "Linked": str(vm.project_link.linked),
                "Project ID": str(vm.project_link.project_id) if vm.project_link.project_id else "",
            },
        )
        self._set_group(
            self._fiscal_year,
            {
                "Fiscal Year": vm.fiscal_year.fiscal_year_label,
                "Fiscal Year ID": str(vm.fiscal_year.fiscal_year_id) if vm.fiscal_year.fiscal_year_id else "",
            },
        )
        self._set_group(self._posting, {"Status": vm.journal.posting_status})
        self._set_group(self._audit, {"References": " | ".join(vm.audit.references)})
        self._set_group(
            self._summary,
            {
                "Health": vm.project_summary.health_indicator or "",
                "Budget": vm.project_summary.budget_status or "",
                "Actual Total": str(vm.project_summary.actual_total) if vm.project_summary.actual_total is not None else "",
                "Variance": str(vm.project_summary.budget_variance) if vm.project_summary.budget_variance is not None else "",
            },
        )

        self._lines.setRowCount(len(vm.lines))
        for row, line in enumerate(vm.lines):
            self._lines.setItem(row, 0, QTableWidgetItem(str(line.account_id)))
            self._lines.setItem(row, 1, QTableWidgetItem(line.side))
            self._lines.setItem(row, 2, QTableWidgetItem(str(line.amount)))
            self._lines.setItem(row, 3, QTableWidgetItem(line.currency))
            self._lines.setItem(row, 4, QTableWidgetItem(line.description or ""))

        self._open_project_button.setEnabled(vm.project_link.project_id is not None)
        self._open_fiscal_year_button.setEnabled(vm.fiscal_year.fiscal_year_id is not None)

    @staticmethod
    def _build_group(title: str) -> QGroupBox:
        group = QGroupBox(title)
        group.setLayout(QFormLayout())
        return group

    @staticmethod
    def _set_group(group: QGroupBox, rows: dict[str, str]) -> None:
        layout = group.layout()
        assert isinstance(layout, QFormLayout)
        while layout.rowCount() > 0:
            layout.removeRow(0)
        for label, value in rows.items():
            layout.addRow(QLabel(label), QLabel(value))

    def _open_project(self) -> None:
        if self._current_project_id is not None:
            self._on_open_project(self._current_project_id)

    def _open_fiscal_year(self) -> None:
        if self._current_fiscal_year_id is not None:
            self._on_open_fiscal_year(self._current_fiscal_year_id)
