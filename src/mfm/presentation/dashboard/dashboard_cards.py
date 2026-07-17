"""Dashboard card composition for the operational workspace."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.presentation.dashboard.dashboard_widgets import DashboardCard
from mfm.presentation.dashboard.dashboard_widgets import SummaryTile


@dataclass(frozen=True, slots=True)
class DashboardCardView:
    route_id: str
    title: str
    summary: str
    detail: str
    tile_title: str
    tile_value: str
    tile_subtitle: str


def build_dashboard_card(view: DashboardCardView, *, on_open, on_refresh=None) -> DashboardCard:
    return DashboardCard(view.title, view.summary, view.detail, on_open=on_open, on_refresh=on_refresh)


def build_summary_tile(view: DashboardCardView) -> SummaryTile:
    return SummaryTile(view.tile_title, view.tile_value, view.tile_subtitle)
