"""Document detail view for operational summaries."""

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

from mfm.presentation.documents.documents_viewmodels import DocumentDetailViewModel


class DocumentsDetailView(QWidget):
    """View-only detail pane for document read models."""

    def __init__(self, *, on_open_project: Callable[[UUID], None]) -> None:
        super().__init__()
        self._on_open_project = on_open_project
        self._current_project_id: UUID | None = None

        self._overview = self._build_group("Oversigt")
        self._lifecycle = self._build_group("Livscyklus")
        self._versions = self._build_group("Versioner")
        self._references = self._build_group("Referencer")

        self._open_project_button = QPushButton("Åbn projekt")
        self._open_project_button.clicked.connect(self._go_project)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self._open_project_button)
        button_layout.addStretch(1)

        layout = QVBoxLayout(self)
        layout.addWidget(self._overview)
        layout.addWidget(self._lifecycle)
        layout.addWidget(self._versions)
        layout.addWidget(self._references)
        layout.addLayout(button_layout)

    def set_view_model(self, vm: DocumentDetailViewModel) -> None:
        self._current_project_id = vm.project_id
        self._open_project_button.setEnabled(vm.project_id is not None)

        self._set_group(
            self._overview,
            {
                "Dokumentnr.": vm.document_number,
                "Titel": vm.document_title,
                "Type": vm.document_type,
                "Status": vm.status,
                "Beskrivelse": vm.description or "",
            },
        )
        self._set_group(
            self._lifecycle,
            {
                "Oprettet": vm.created_at.isoformat(),
                "Opdateret": vm.updated_at.isoformat() if vm.updated_at is not None else "",
                "Arkiveret": vm.archived_at.isoformat() if vm.archived_at is not None else "",
                "Kasseret": vm.disposed_at.isoformat() if vm.disposed_at is not None else "",
                "Version": str(vm.version),
            },
        )

        latest_version = vm.versions[-1] if vm.versions else None
        self._set_group(
            self._versions,
            {
                "Antal": str(len(vm.versions)),
                "Nyeste version": str(latest_version.version_number) if latest_version is not None else "",
                "Nyeste lagernøgle": latest_version.storage_key if latest_version is not None else "",
            },
        )

        first_reference = vm.references[0] if vm.references else None
        self._set_group(
            self._references,
            {
                "Antal": str(len(vm.references)),
                "Mål": first_reference.target_capability if first_reference is not None else "",
                "Aggregat-ID": first_reference.target_aggregate_id if first_reference is not None else "",
            },
        )

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

    def _go_project(self) -> None:
        if self._current_project_id is not None:
            self._on_open_project(self._current_project_id)
