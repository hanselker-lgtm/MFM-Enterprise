"""Dashboard workspace that presents all implemented reporting dashboards."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard.dashboard_cards import DashboardCardView
from mfm.presentation.dashboard.dashboard_cards import build_dashboard_card
from mfm.presentation.dashboard.dashboard_cards import build_summary_tile
from mfm.presentation.dashboard.dashboard_controller import DashboardController
from mfm.presentation.dashboard.dashboard_controller import DashboardSnapshot
from mfm.presentation.dashboard.dashboard_widgets import DashboardDetailWidget


class DashboardWorkspace(QWidget):
    """Presentation workspace for the shell's reporting dashboards."""

    def __init__(self, *, controller: DashboardController) -> None:
        super().__init__()
        self._controller = controller
        self._card_widgets: dict[str, QWidget] = {}
        self._summary_tiles: dict[str, QWidget] = {}
        self._detail_widgets: dict[str, DashboardDetailWidget] = {}

        self._title = QLabel("Dashboards")
        self._title.setObjectName("dashboardWorkspaceTitle")
        self._subtitle = QLabel("Reporting dashboards only. No workflows or repositories are invoked here.")
        self._subtitle.setWordWrap(True)

        self._refresh_button = QPushButton("Refresh dashboards")
        self._refresh_button.clicked.connect(self._controller.refresh)

        header = QHBoxLayout()
        header.addWidget(self._title)
        header.addStretch(1)
        header.addWidget(self._refresh_button)

        self._cards_container = QWidget()
        self._cards_layout = QGridLayout(self._cards_container)
        self._cards_layout.setSpacing(16)

        self._tiles_container = QWidget()
        self._tiles_layout = QGridLayout(self._tiles_container)
        self._tiles_layout.setSpacing(12)

        self._detail_stack = QStackedWidget()
        self._detail_placeholder = QLabel("Select a dashboard card to open its detail view.")
        self._detail_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._detail_stack.addWidget(self._detail_placeholder)

        top_area = QWidget()
        top_layout = QVBoxLayout(top_area)
        top_layout.addLayout(header)
        top_layout.addWidget(self._subtitle)
        top_layout.addWidget(self._tiles_container)
        top_layout.addWidget(self._cards_container)

        layout = QVBoxLayout(self)
        layout.addWidget(top_area)
        layout.addWidget(self._detail_stack, 1)

    def set_reports(
        self,
        *,
        organization_dashboard: OrganizationDashboardResponse,
        active_projects_dashboard: ActiveProjectsDashboardResponse,
        project_status_dashboard: ProjectStatusResponse,
        budget_vs_actual_dashboard: BudgetVsActualResponse,
    ) -> None:
        self._controller.set_snapshot(
            DashboardSnapshot(
                organization_dashboard=organization_dashboard,
                active_projects_dashboard=active_projects_dashboard,
                project_status_dashboard=project_status_dashboard,
                budget_vs_actual_dashboard=budget_vs_actual_dashboard,
            )
        )
        self._rebuild()
        self.show_dashboard("dashboard.organization")

    def refresh(self) -> None:
        self._controller.refresh()

    @property
    def current_route_id(self) -> str | None:
        return self._controller.current_route_id

    def show_dashboard(self, route_id: str) -> None:
        self._controller.select(route_id)
        detail = self._detail_widgets.get(route_id)
        if detail is None:
            return
        self._detail_stack.setCurrentWidget(detail)

    def detail_widget(self, route_id: str) -> DashboardDetailWidget:
        return self._detail_widgets[route_id]

    def _rebuild(self) -> None:
        while self._cards_layout.count():
            item = self._cards_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        while self._tiles_layout.count():
            item = self._tiles_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        while self._detail_stack.count() > 1:
            widget = self._detail_stack.widget(1)
            self._detail_stack.removeWidget(widget)
            widget.setParent(None)

        self._card_widgets.clear()
        self._summary_tiles.clear()
        self._detail_widgets.clear()

        views = self._controller.card_views()
        for index, view in enumerate(views):
            card = build_dashboard_card(view, on_open=lambda route_id=view.route_id: self.show_dashboard(route_id), on_refresh=self.refresh)
            tile = build_summary_tile(view)
            detail = DashboardDetailWidget()

            self._cards_layout.addWidget(card, index // 2, index % 2)
            self._tiles_layout.addWidget(tile, 0, index)
            self._detail_stack.addWidget(detail)

            self._card_widgets[view.route_id] = card
            self._summary_tiles[view.route_id] = tile
            self._detail_widgets[view.route_id] = detail
            detail.show_report(view.title, self._detail_report(view))

    def _detail_report(self, view: DashboardCardView) -> object:
        snapshot = self._controller.snapshot
        if view.route_id == "dashboard.organization":
            return snapshot.organization_dashboard
        if view.route_id == "dashboard.active-projects":
            return snapshot.active_projects_dashboard
        if view.route_id == "dashboard.project-status":
            return snapshot.project_status_dashboard
        if view.route_id == "dashboard.budget-vs-actual":
            return snapshot.budget_vs_actual_dashboard
        raise KeyError(view.route_id)
