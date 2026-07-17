"""Navigation registry and lazy-loading orchestration for the application shell."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Callable


class NavigationCategory(StrEnum):
    DASHBOARD = "Dashboard"
    OPERATIONS = "Operations"
    ADMINISTRATION = "Administration"


class NavigationKind(StrEnum):
    REPORT = "report"
    WIDGET = "widget"


@dataclass(frozen=True, slots=True)
class NavigationRoute:
    route_id: str
    label: str
    category: NavigationCategory
    kind: NavigationKind
    loader: Callable[[], Any]


class NavigationService:
    """Register and lazily resolve navigation routes."""

    def __init__(self) -> None:
        self._routes: dict[str, NavigationRoute] = {}
        self._cache: dict[str, Any] = {}
        self._current_route_id: str | None = None

    def register_route(self, route: NavigationRoute) -> None:
        if route.route_id in self._routes:
            raise ValueError(f"Route {route.route_id} is already registered")
        self._routes[route.route_id] = route

    def routes(self) -> tuple[NavigationRoute, ...]:
        return tuple(self._routes.values())

    def routes_for_category(self, category: NavigationCategory) -> tuple[NavigationRoute, ...]:
        return tuple(route for route in self._routes.values() if route.category == category)

    def current_route(self) -> NavigationRoute | None:
        if self._current_route_id is None:
            return None
        return self._routes.get(self._current_route_id)

    def load(self, route_id: str) -> Any:
        route = self._routes.get(route_id)
        if route is None:
            raise KeyError(f"Unknown route: {route_id}")

        self._current_route_id = route_id
        if route_id not in self._cache:
            self._cache[route_id] = route.loader()
        return self._cache[route_id]

    def is_loaded(self, route_id: str) -> bool:
        return route_id in self._cache
