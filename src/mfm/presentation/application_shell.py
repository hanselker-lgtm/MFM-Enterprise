"""Application shell composition for the MFM Enterprise GUI."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.contact_communication_summary_dto import (
    ContactCommunicationSummaryResponse,
)
from mfm.application.reporting.models.membership_billing_summary_dto import (
    MembershipBillingSummaryResponse,
)
from mfm.application.reporting.models.events_activities_summary_dto import (
    EventsActivitiesSummaryResponse,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryResponse,
)
from mfm.application.reporting.models.membership_summary_dto import MembershipSummaryResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.organization_roles_summary_dto import (
    OrganizationRolesSummaryResponse,
)
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard_host import DashboardHostSnapshotLoader
from mfm.presentation.dashboard_host import DashboardHost
from mfm.presentation.main_window import MainWindow
from mfm.presentation.menu_builder import MenuBuilder
from mfm.presentation.navigation_service import NavigationCategory
from mfm.presentation.navigation_service import NavigationKind
from mfm.presentation.navigation_service import NavigationRoute
from mfm.presentation.navigation_service import NavigationService
from mfm.presentation.status_bar import StatusBar


ReportLoader = Callable[
    [],
    OrganizationDashboardResponse
    | ActiveProjectsDashboardResponse
    | ProjectStatusResponse
    | BudgetVsActualResponse
    | MembershipSummaryResponse
    | OrganizationRolesSummaryResponse
    | ContactCommunicationSummaryResponse
    | MembershipBillingSummaryResponse
    | EventsActivitiesSummaryResponse
    | DocumentArchiveSummaryResponse,
]
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
    projects_workspace_loader: WidgetLoader | None = None,
    memberships_workspace_loader: WidgetLoader | None = None,
    organization_roles_workspace_loader: WidgetLoader | None = None,
    contact_communication_workspace_loader: WidgetLoader | None = None,
    membership_billing_workspace_loader: WidgetLoader | None = None,
    events_activities_workspace_loader: WidgetLoader | None = None,
    document_archive_workspace_loader: WidgetLoader | None = None,
    documents_workspace_loader: WidgetLoader | None = None,
    accounting_workspace_loader: WidgetLoader | None = None,
    application: QApplication | None = None,
) -> ApplicationShell:
    navigation_service = NavigationService()
    dashboard_host = DashboardHost(
        snapshot_loader=DashboardHostSnapshotLoader(
            organization_dashboard=report_loaders["dashboard.organization"],
            active_projects_dashboard=report_loaders["dashboard.active-projects"],
            project_status_dashboard=report_loaders["dashboard.project-status"],
            budget_vs_actual_dashboard=report_loaders["dashboard.budget-vs-actual"],
        )
    )
    menu_builder = MenuBuilder()
    status_bar = StatusBar()

    _register_default_dashboard_routes(navigation_service, dashboard_host, report_loaders)
    _register_default_module_routes(
        navigation_service,
        widget_loaders or {},
        projects_workspace_loader=projects_workspace_loader,
        memberships_workspace_loader=memberships_workspace_loader,
        organization_roles_workspace_loader=organization_roles_workspace_loader,
        contact_communication_workspace_loader=contact_communication_workspace_loader,
        membership_billing_workspace_loader=membership_billing_workspace_loader,
        events_activities_workspace_loader=events_activities_workspace_loader,
        document_archive_workspace_loader=document_archive_workspace_loader,
        documents_workspace_loader=documents_workspace_loader,
        accounting_workspace_loader=accounting_workspace_loader,
    )

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
    *,
    projects_workspace_loader: WidgetLoader | None = None,
    memberships_workspace_loader: WidgetLoader | None = None,
    organization_roles_workspace_loader: WidgetLoader | None = None,
    contact_communication_workspace_loader: WidgetLoader | None = None,
    membership_billing_workspace_loader: WidgetLoader | None = None,
    events_activities_workspace_loader: WidgetLoader | None = None,
    document_archive_workspace_loader: WidgetLoader | None = None,
    documents_workspace_loader: WidgetLoader | None = None,
    accounting_workspace_loader: WidgetLoader | None = None,
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
            loader=projects_workspace_loader
            or widget_loaders.get("operations.projects", lambda: _placeholder_page("Projects")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.memberships",
            label="Memberships",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=memberships_workspace_loader
            or widget_loaders.get(
                "operations.memberships",
                lambda: _placeholder_page("Memberships"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.organization-roles",
            label="Organization Roles",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=organization_roles_workspace_loader
            or widget_loaders.get(
                "operations.organization-roles",
                lambda: _placeholder_page("Organization Roles"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.contact-communication",
            label="Contact Communication",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=contact_communication_workspace_loader
            or widget_loaders.get(
                "operations.contact-communication",
                lambda: _placeholder_page("Contact Communication"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.membership-billing",
            label="Membership Billing",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=membership_billing_workspace_loader
            or widget_loaders.get(
                "operations.membership-billing",
                lambda: _placeholder_page("Membership Billing"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.events-activities",
            label="Events Activities",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=events_activities_workspace_loader
            or widget_loaders.get(
                "operations.events-activities",
                lambda: _placeholder_page("Events Activities"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.document-archive",
            label="Document Archive",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=document_archive_workspace_loader
            or widget_loaders.get(
                "operations.document-archive",
                lambda: _placeholder_page("Document Archive"),
            ),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.documents",
            label="Documents",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=documents_workspace_loader
            or widget_loaders.get("operations.documents", lambda: _placeholder_page("Documents")),
        )
    )
    navigation_service.register_route(
        NavigationRoute(
            route_id="operations.accounting",
            label="Accounting",
            category=NavigationCategory.OPERATIONS,
            kind=NavigationKind.WIDGET,
            loader=accounting_workspace_loader
            or widget_loaders.get("operations.accounting", lambda: _placeholder_page("Accounting")),
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
