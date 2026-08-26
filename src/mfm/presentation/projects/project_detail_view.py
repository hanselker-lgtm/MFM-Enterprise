"""Project detail view for operational summaries."""

from __future__ import annotations

from collections.abc import Callable
from uuid import UUID

from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.projects.project_viewmodels import ProjectDetailViewModel


class ProjectDetailView(QWidget):
    """View-only detail pane for project read models."""

    def __init__(
        self,
        *,
        on_navigate_documents: Callable[[UUID], None],
        on_navigate_accounting: Callable[[UUID], None],
    ) -> None:
        super().__init__()
        self._on_navigate_documents = on_navigate_documents
        self._on_navigate_accounting = on_navigate_accounting
        self._current_project_id: UUID | None = None

        self._overview = self._build_group("Oversigt")
        self._status = self._build_group("Status")
        self._budget = self._build_group("Budgetoversigt")
        self._accounting = self._build_group("Bogføringsoversigt")
        self._documents = self._build_group("Dokumentoversigt")
        self._archive = self._build_group("Arkivstatus")

        self._navigate_documents = QPushButton("Gå til Dokumenter")
        self._navigate_documents.clicked.connect(self._go_documents)
        self._navigate_accounting = QPushButton("Gå til Bogføring")
        self._navigate_accounting.clicked.connect(self._go_accounting)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self._navigate_documents)
        nav_layout.addWidget(self._navigate_accounting)
        nav_layout.addStretch(1)

        layout = QVBoxLayout(self)
        layout.addWidget(self._overview)
        layout.addWidget(self._status)
        layout.addWidget(self._budget)
        layout.addWidget(self._accounting)
        layout.addWidget(self._documents)
        layout.addWidget(self._archive)
        layout.addLayout(nav_layout)

    def set_view_model(self, vm: ProjectDetailViewModel) -> None:
        self._current_project_id = vm.overview.project_id

        self._set_group(self._overview, {
            "Projektnr.": vm.overview.project_number,
            "Navn": vm.overview.name,
            "Beskrivelse": vm.overview.description,
        })
        self._set_group(self._status, {
            "Status": vm.status.status,
            "Helbred": vm.status.health_indicator,
            "Klar til afslutning": str(vm.status.ready_for_closure),
        })
        self._set_group(self._budget, {
            "Budgetstatus": vm.budget_summary.budget_status,
            "Kategorier": ", ".join(vm.budget_summary.categories),
            "Planlagt total": str(vm.budget_summary.planned_budget_total),
            "Afvigelse": str(vm.budget_summary.budget_variance),
        })
        self._set_group(self._accounting, {
            "Bogføringsstatus": vm.accounting_summary.accounting_status,
            "Antal posteringer": str(vm.accounting_summary.journal_count),
            "Faktisk total": str(vm.accounting_summary.actual_total),
            "Regnskabsår": str(vm.accounting_summary.fiscal_year),
        })
        self._set_group(self._documents, {
            "Total": str(vm.document_summary.total_documents),
            "Færdiggjort": str(vm.document_summary.finalized_documents),
            "Udestående": str(vm.document_summary.outstanding_documents),
        })
        self._set_group(self._archive, {
            "Arkiv": vm.archive_status.archive_status,
            "Afslutning": vm.archive_status.closure_status,
        })

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
        for key, value in rows.items():
            layout.addRow(QLabel(key), QLabel(value))

    def _go_documents(self) -> None:
        if self._current_project_id is not None:
            self._on_navigate_documents(self._current_project_id)

    def _go_accounting(self) -> None:
        if self._current_project_id is not None:
            self._on_navigate_accounting(self._current_project_id)
