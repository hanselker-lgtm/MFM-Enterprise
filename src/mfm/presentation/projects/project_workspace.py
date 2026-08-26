"""Primary project management workspace."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import UUID

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QSplitter
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.projects.project_controller import ProjectController
from mfm.presentation.projects.project_viewmodels import CreateProjectCommandViewModel
from mfm.presentation.projects.project_viewmodels import ProjectListFilterViewModel
from mfm.presentation.projects.project_detail_view import ProjectDetailView
from mfm.presentation.projects.project_list_view import ProjectListView
from mfm.presentation.projects.project_toolbar import ProjectToolbar


class ProjectWorkspace(QWidget):
    """Operational workspace for project management."""

    def __init__(
        self,
        *,
        controller: ProjectController,
        default_organization_id: UUID | None = None,
        default_owner_contact_id: UUID | None = None,
    ) -> None:
        super().__init__()
        self._controller = controller
        self._current_filters = ProjectListFilterViewModel()
        # Fall back to the historical placeholder IDs only when the
        # caller doesn't supply real ones (e.g. older tests). Against a
        # real composition root these are always the seeded
        # organization/owner-contact so "Create Project" actually works.
        self._default_organization_id = default_organization_id or UUID(
            "00000000-0000-0000-0000-000000000001"
        )
        self._default_owner_contact_id = default_owner_contact_id or UUID(
            "00000000-0000-0000-0000-000000000002"
        )

        self._toolbar = ProjectToolbar(
            on_search=self._handle_search,
            on_refresh=self._handle_refresh,
            on_create_project=self._handle_create_project,
        )
        self._list = ProjectListView(
            on_open_project=self._handle_open_project,
            on_page_change=self._handle_page_change,
        )
        self._detail = ProjectDetailView(
            on_navigate_documents=self._controller.navigate_to_documents,
            on_navigate_accounting=self._controller.navigate_to_accounting,
        )

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self._list)
        splitter.addWidget(self._detail)
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)

        layout = QVBoxLayout(self)
        layout.addWidget(self._toolbar)
        layout.addWidget(splitter)

        self._handle_search()

    def create_detail_dock_widget(self, parent: QMainWindow | None = None) -> QDockWidget:
        """Provide a future-ready detachable detail pane."""
        dock = QDockWidget("Projektdetaljer", parent)
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
        list_vm = self._controller.load_project_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_refresh(self) -> None:
        list_vm, detail_vm = self._controller.refresh()
        self._list.set_view_model(list_vm)
        if detail_vm is not None:
            self._detail.set_view_model(detail_vm)

    def _handle_open_project(self, project_id: UUID) -> None:
        detail_vm = self._controller.open_project(project_id)
        self._detail.set_view_model(detail_vm)

    def _handle_page_change(self, direction: int) -> None:
        next_page = max(self._current_filters.page + direction, 1)
        filters = ProjectListFilterViewModel(
            text=self._current_filters.text,
            status=self._current_filters.status,
            sort_by=self._current_filters.sort_by,
            descending=self._current_filters.descending,
            page=next_page,
            page_size=self._current_filters.page_size,
        )
        self._current_filters = filters
        list_vm = self._controller.load_project_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_create_project(self) -> None:
        project_number, ok_number = QInputDialog.getText(self, "Opret projekt", "Projektnummer")
        if not ok_number or not project_number.strip():
            return

        project_name, ok_name = QInputDialog.getText(self, "Opret projekt", "Projektnavn")
        if not ok_name or not project_name.strip():
            return

        organization_id = self._default_organization_id
        owner_contact_id = self._default_owner_contact_id

        created_id = self._controller.create_project(
            CreateProjectCommandViewModel(
                organization_id=organization_id,
                organization_owner_contact_id=owner_contact_id,
                project_number=project_number.strip(),
                project_name=project_name.strip(),
                project_start_date=datetime.now(UTC),
            )
        )
        QMessageBox.information(self, "Projekt oprettet", f"Projekt oprettet: {created_id}")
        self._handle_refresh()
