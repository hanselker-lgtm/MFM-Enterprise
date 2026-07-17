"""Presentation layer package for the MFM Enterprise application shell."""

from mfm.presentation.application_shell import ApplicationShell
from mfm.presentation.application_shell import build_application_shell
from mfm.presentation.dashboard_host import DashboardHost
from mfm.presentation.main_window import MainWindow
from mfm.presentation.menu_builder import MenuBuilder
from mfm.presentation.navigation_service import NavigationCategory
from mfm.presentation.navigation_service import NavigationKind
from mfm.presentation.navigation_service import NavigationRoute
from mfm.presentation.navigation_service import NavigationService
from mfm.presentation.status_bar import StatusBar

__all__ = [
    "ApplicationShell",
    "DashboardHost",
    "MainWindow",
    "MenuBuilder",
    "NavigationCategory",
    "NavigationKind",
    "NavigationRoute",
    "NavigationService",
    "StatusBar",
    "build_application_shell",
]
