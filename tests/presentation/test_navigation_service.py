from __future__ import annotations

from dataclasses import dataclass

from mfm.presentation.navigation_service import NavigationCategory
from mfm.presentation.navigation_service import NavigationKind
from mfm.presentation.navigation_service import NavigationRoute
from mfm.presentation.navigation_service import NavigationService


@dataclass(frozen=True)
class _LoaderState:
    counter: int = 0


def test_navigation_service_lazy_loads_once_and_tracks_current_route() -> None:
    load_count = {"value": 0}
    service = NavigationService()

    service.register_route(
        NavigationRoute(
            route_id="dashboard.organization",
            label="Organization Dashboard",
            category=NavigationCategory.DASHBOARD,
            kind=NavigationKind.REPORT,
            loader=lambda: load_count.__setitem__("value", load_count["value"] + 1) or {"report": "org"},
        )
    )

    first = service.load("dashboard.organization")
    second = service.load("dashboard.organization")

    assert first == {"report": "org"}
    assert second == {"report": "org"}
    assert load_count["value"] == 1
    assert service.current_route().label == "Organization Dashboard"
    assert service.routes_for_category(NavigationCategory.DASHBOARD)[0].route_id == "dashboard.organization"
