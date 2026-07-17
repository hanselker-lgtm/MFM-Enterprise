from __future__ import annotations

from mfm.presentation.dashboard.dashboard_controller import DashboardController

from tests.presentation._dashboard_fixtures import dashboard_snapshot


def test_dashboard_controller_maps_snapshot_into_card_views() -> None:
    refresh_count = {"value": 0}
    controller = DashboardController(refresh_callback=lambda: refresh_count.__setitem__("value", refresh_count["value"] + 1))
    controller.set_snapshot(dashboard_snapshot())

    views = controller.card_views()

    assert len(views) == 4
    assert views[0].title == "Organization Dashboard"
    assert views[3].tile_subtitle == "LIMITED_BUDGET_METADATA"

    controller.select("dashboard.project-status")
    controller.refresh()

    assert controller.current_route_id == "dashboard.project-status"
    assert refresh_count["value"] == 1
