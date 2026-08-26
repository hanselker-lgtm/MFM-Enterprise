"""Operational documents workspace."""

from __future__ import annotations

from uuid import UUID

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QSplitter
from PySide6.QtWidgets import QTabWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.documents.documents_controller import DocumentsController
from mfm.presentation.documents.documents_detail_view import DocumentsDetailView
from mfm.presentation.documents.documents_list_view import DocumentsListView
from mfm.presentation.documents.documents_toolbar import DocumentsToolbar
from mfm.presentation.documents.documents_viewmodels import CreateDocumentCommandViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListFilterViewModel
from mfm.presentation.documents.documents_viewmodels import RegisterDocumentVersionCommandViewModel


class DocumentsWorkspace(QWidget):
    """Operational workspace for document management."""

    def __init__(self, *, controller: DocumentsController) -> None:
        super().__init__()
        self._controller = controller
        self._current_filters = DocumentListFilterViewModel()

        self._toolbar = DocumentsToolbar(
            on_search=self._handle_search,
            on_refresh=self._handle_refresh,
            on_create_document=self._handle_create_document,
            on_register_version=self._handle_register_version,
            on_archive_document=self._handle_archive_document,
        )
        self._list = DocumentsListView(
            on_open_document=self._handle_open_document,
            on_page_change=self._handle_page_change,
        )
        self._detail = DocumentsDetailView(on_open_project=self._controller.open_project)

        documents_split = QSplitter(Qt.Orientation.Horizontal)
        documents_split.addWidget(self._list)
        documents_split.addWidget(self._detail)
        documents_split.setStretchFactor(0, 2)
        documents_split.setStretchFactor(1, 3)

        tabs = QTabWidget()
        tabs.addTab(documents_split, "Dokumenter")
        tabs.addTab(self._placeholder("Versionstidslinje forbeholdt fremtidig funktionalitet"), "Versioner")
        tabs.addTab(self._placeholder("Referenceanalyse forbeholdt fremtidig funktionalitet"), "Referencer")

        layout = QVBoxLayout(self)
        layout.addWidget(self._toolbar)
        layout.addWidget(tabs)

        self._handle_search()

    def create_detail_dock_widget(self, parent: QMainWindow | None = None) -> QDockWidget:
        """Provide a future-ready detachable detail pane."""
        dock = QDockWidget("Dokumentdetaljer", parent)
        dock.setWidget(self._detail)
        dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea
            | Qt.DockWidgetArea.RightDockWidgetArea
            | Qt.DockWidgetArea.BottomDockWidgetArea
        )
        return dock

    def _handle_search(self) -> None:
        filters = self._toolbar.filters(page=self._current_filters.page, page_size=self._current_filters.page_size)
        self._current_filters = filters
        list_vm = self._controller.load_document_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_refresh(self) -> None:
        list_vm, detail_vm = self._controller.refresh()
        self._list.set_view_model(list_vm)
        if detail_vm is not None:
            self._detail.set_view_model(detail_vm)

    def _handle_open_document(self, document_id: UUID) -> None:
        detail_vm = self._controller.open_document(document_id)
        self._detail.set_view_model(detail_vm)

    def _handle_page_change(self, direction: int) -> None:
        next_page = max(self._current_filters.page + direction, 1)
        filters = DocumentListFilterViewModel(
            text=self._current_filters.text,
            status=self._current_filters.status,
            target_capability=self._current_filters.target_capability,
            sort_by=self._current_filters.sort_by,
            descending=self._current_filters.descending,
            page=next_page,
            page_size=self._current_filters.page_size,
        )
        self._current_filters = filters
        list_vm = self._controller.load_document_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_create_document(self) -> None:
        document_number, ok_number = QInputDialog.getText(self, "Opret dokument", "Dokumentnummer")
        if not ok_number or not document_number.strip():
            return

        document_title, ok_title = QInputDialog.getText(self, "Opret dokument", "Dokumenttitel")
        if not ok_title or not document_title.strip():
            return

        document_type, ok_type = QInputDialog.getText(self, "Opret dokument", "Dokumenttype")
        if not ok_type or not document_type.strip():
            return

        project_id_text, _ = QInputDialog.getText(self, "Opret dokument", "Projekt-ID (valgfrit)")
        project_id = None
        if project_id_text.strip():
            try:
                project_id = UUID(project_id_text.strip())
            except ValueError:
                QMessageBox.warning(self, "Opret dokument", "Ugyldigt projekt-ID")
                return

        created_id = self._controller.create_document(
            CreateDocumentCommandViewModel(
                document_number=document_number.strip(),
                document_title=document_title.strip(),
                document_type=document_type.strip(),
                project_id=project_id,
            )
        )
        QMessageBox.information(self, "Dokument oprettet", f"Dokument oprettet: {created_id}")
        self._handle_refresh()

    def _handle_register_version(self) -> None:
        if self._controller.last_selected_document_id is None:
            QMessageBox.warning(self, "Registrér version", "Intet dokument valgt")
            return

        version_text, ok_version = QInputDialog.getText(self, "Registrér version", "Versionsnummer")
        if not ok_version or not version_text.strip():
            return

        storage_key, ok_storage = QInputDialog.getText(self, "Registrér version", "Lagernøgle")
        if not ok_storage or not storage_key.strip():
            return

        try:
            version_number = int(version_text.strip())
        except ValueError:
            QMessageBox.warning(self, "Registrér version", "Versionsnummer skal være et heltal")
            return

        self._controller.register_document_version(
            RegisterDocumentVersionCommandViewModel(
                document_id=self._controller.last_selected_document_id,
                version_number=version_number,
                storage_key=storage_key.strip(),
            )
        )
        QMessageBox.information(self, "Registrér version", "Version registreret")
        self._handle_refresh()

    def _handle_archive_document(self) -> None:
        if self._controller.last_selected_document_id is None:
            QMessageBox.warning(self, "Arkivér dokument", "Intet dokument valgt")
            return

        self._controller.archive_document(self._controller.last_selected_document_id)
        QMessageBox.information(self, "Arkivér dokument", "Dokument arkiveret")
        self._handle_refresh()

    @staticmethod
    def _placeholder(text: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(text))
        return widget
