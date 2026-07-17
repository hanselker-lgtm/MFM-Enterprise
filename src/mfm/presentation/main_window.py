"""Main application window for the MFM Enterprise shell."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QWidget

from mfm.presentation.dashboard_host import DashboardHost
from mfm.presentation.menu_builder import MenuBuilder
from mfm.presentation.navigation_service import NavigationKind
from mfm.presentation.navigation_service import NavigationService
from mfm.presentation.status_bar import StatusBar


class MainWindow(QMainWindow):
    """Host the application shell chrome and lazily loaded module pages."""

    def __init__(
        self,
        *,
        navigation_service: NavigationService,
        dashboard_host: DashboardHost,
        menu_builder: MenuBuilder,
        status_bar: StatusBar,
    ) -> None:
        super().__init__()
        self.setWindowTitle("MFM Enterprise")
        self._navigation_service = navigation_service
        self._dashboard_host = dashboard_host
        self._menu_builder = menu_builder
        self._status_bar = status_bar
        self._page_stack = QStackedWidget()
        self._page_cache: dict[str, QWidget] = {}

        self._page_stack.addWidget(self._dashboard_host)
        self.setCentralWidget(self._page_stack)
        self.setStatusBar(self._status_bar)

        self._navigation_tree = self._menu_builder.build_left_navigation(
            self._navigation_service.routes(), self.navigate_to
        )
        dock = QDockWidget("Navigation", self)
        dock.setObjectName("navigationDock")
        dock.setWidget(self._navigation_tree)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        toolbar = self._menu_builder.build_top_toolbar(
            self._navigation_service.routes(), self.navigate_to
        )
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        first_route = next(iter(self._navigation_service.routes()), None)
        if first_route is not None:
            self.navigate_to(first_route.route_id)

    def navigate_to(self, route_id: str) -> None:
        route = next((item for item in self._navigation_service.routes() if item.route_id == route_id), None)
        if route is None:
            raise KeyError(f"Unknown route: {route_id}")

        payload = self._navigation_service.load(route_id)
        self.setWindowTitle(f"MFM Enterprise - {route.label}")
        self._status_bar.set_route(route.label)
        self._status_bar.set_message(f"Loaded {route.label}")

        if route.kind == NavigationKind.REPORT:
            self._display_report(route_id)
            return

        self._display_widget(route_id, payload)

    def _display_report(self, route_id: str) -> None:
        self._dashboard_host.show_dashboard(route_id)
        self._page_stack.setCurrentWidget(self._dashboard_host)

    def _display_widget(self, route_id: str, payload: object) -> None:
        if not isinstance(payload, QWidget):
            raise TypeError(f"Route {route_id} did not return a QWidget")

        page = self._page_cache.get(route_id)
        if page is None:
            page = payload
            self._page_cache[route_id] = page
            self._page_stack.addWidget(page)

        self._page_stack.setCurrentWidget(page)
