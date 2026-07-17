"""Application shell composition for the MFM Enterprise GUI."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard_host import DashboardHost
from mfm.presentation.main_window import MainWindow
from mfm.presentation.menu_builder import MenuBuilder
from mfm.presentation.navigation_service import NavigationCategory
from mfm.presentation.navigation_service import NavigationKind
from mfm.presentation.navigation_service import NavigationRoute
from mfm.presentation.navigation_service import NavigationService
from mfm.presentation.status_bar import StatusBar


ReportLoader = Callable[[], OrganizationDashboardResponse | ActiveProjectsDashboardResponse | ProjectStatusResponse | BudgetVsActualResponse]
WidgetLoader = Callable[[], QWidget]


@dataclass(frozen=True, slots=True)
class ApplicationShellDependencies:
    navigation_service: NavigationService
    dashboard_host: DashboardHost
    menu_builder: MenuBuilder
    status_bar: StatusBar
    main_window: MainWindow


class ApplicationShell:
    """Own the top-level Qt application shell."""

    def __init__(self, dependencies: ApplicationShellDependencies, application: QApplication | None = None) -> None:
        self._dependencies = dependencies
        self._application = application or QApplication.instance() or QApplication([])

    @property
    def main_window(self) -> MainWindow:
        return self._dependencies.main_window

    def start(self) -> int:
        self._dependencies.main_window.show()
        return self._application.exec()


def build_application_shell(
    *,
    report_loaders: dict[str, ReportLoader],
    widget_loaders: dict[str, WidgetLoader] | None = None,
    application: QApplication | None = None,
) -> ApplicationShell:
    navigation_service = NavigationService()
    dashboard_host = DashboardHost()
    menu_builder = MenuBuilder()
    status_bar = StatusBar()

    _register_default_dashboard_routes(navigation_service, dashboard_host, report_loaders)
    _register_default_module_routes(navigation_service, widget_loaders or {})

    main_window = MainWindow(
        navigation_service=navigation_service,
        dashboard_host=dashboard_host,
        menu_builder=menu_builder,
        status_bar=status_bar,
    )

    return ApplicationShell(
        ApplicationShellDependencies(
            navigation_service=navigation_service,
            dashboard_host=dashboard_host,
            menu_builder=menu_builder,
            status_bar=status_bar,
            main_window=main_window,
        ),
        application=application,
    )


def _register_default_dashboard_routes(
    navigation_service: NavigationService,
    dashboard_host: DashboardHost,
    report_loaders: dict[str, ReportLoader],
) -> None:
    navigation_service.register_route(
        NavigationRoute(
            route_id="dashboard.organization",
            label="Organization Dashboard",
            category=NavigationCategory.DASHBOARD,
            kind=NavigationKind.REPORT,
            loader=report_loaders["dashboard.organization"],
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="dashboard.active-projects",
            label="Active Projects",
            category=NavigationCategory.DASHBOARD,
            kind=NavigationKind.REPORT,
            loader=report_loaders["dashboard.active-projects"],
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="dashboard.project-status",
            label="Project Status",
            category=NavigationCategory.DASHBOARD,
            kind=NavigationKind.REPORT,
            loader=report_loaders["dashboard.project-status"],
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="dashboard.budget-vs-actual",
            label="Budget vs Actual",
            category=NavigationCategory.DASHBOARD,
            kind=NavigationKind.REPORT,
            loader=report_loaders["dashboard.budget-vs-actual"],
        )
    )

    _ = dashboard_host


def _register_default_module_routes(
    navigation_service: NavigationService,
    widget_loaders: dict[str, WidgetLoader],
) -> None:
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.organizations",
            label="Organizations",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("operations.organizations", lambda: _placeholder_page("Organizations")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.projects",
            label="Projects",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("operations.projects", lambda: _placeholder_page("Projects")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.documents",
            label="Documents",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("operations.documents", lambda: _placeholder_page("Documents")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.accounting",
            label="Accounting",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("operations.accounting", lambda: _placeholder_page("Accounting")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="administration.settings",
            label="Settings",
            category=NavigationCategory.ADMINISTRATION,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("administration.settings", lambda: _placeholder_page("Settings")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="administration.logs",
            label="Logs",
            category=NavigationCategory.ADMINISTRATION,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("administration.logs", lambda: _placeholder_page("Logs")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="administration.about",
            label="About",
            category=NavigationCategory.ADMINISTRATION,
            kind=NavigationKind.WIDGET,
            loader=widget_loaders.get("administration.about", lambda: _placeholder_page("About")),
        )
    )


def _placeholder_page(title: str) -> QWidget:
    page = QWidget()
    label = QLabel(f"{title} module will be connected to feature APIs here.", page)
    label.setWordWrap(True)
    return page
