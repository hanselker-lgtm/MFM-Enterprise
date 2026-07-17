"""Menu and navigation widget builders for the application shell."""

from __future__ import annotations

from collections.abc import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QTreeWidget
from PySide6.QtWidgets import QTreeWidgetItem

from mfm.presentation.navigation_service import NavigationCategory
from mfm.presentation.navigation_service import NavigationRoute


class MenuBuilder:
    """Build navigation chrome without embedding business logic."""

    def build_left_navigation(
        self,
        routes: tuple[NavigationRoute, ...],
        on_route_selected: Callable[[str], None],
    ) -> QTreeWidget:
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setRootIsDecorated(True)
        tree.setAnimated(True)

        category_items: dict[NavigationCategory, QTreeWidgetItem] = {}
        for route in routes:
            category_item = category_items.get(route.category)
            if category_item is None:
                category_item = QTreeWidgetItem([route.category.value])
                category_item.setFlags(category_item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
                category_items[route.category] = category_item
                tree.addTopLevelItem(category_item)

            route_item = QTreeWidgetItem([route.label])
            route_item.setData(0, Qt.ItemDataRole.UserRole, route.route_id)
            category_item.addChild(route_item)

        tree.expandAll()

        def handle_activation(item: QTreeWidgetItem, _: int) -> None:
            route_id = item.data(0, Qt.ItemDataRole.UserRole)
            if isinstance(route_id, str):
                on_route_selected(route_id)

        tree.itemActivated.connect(handle_activation)
        return tree

    def build_top_toolbar(
        self,
        routes: tuple[NavigationRoute, ...],
        on_route_selected: Callable[[str], None],
    ) -> QToolBar:
        toolbar = QToolBar("Application")
        toolbar.setMovable(False)

        for route in routes:
            action = QAction(route.label, toolbar)
            action.setData(route.route_id)
            action.triggered.connect(lambda checked=False, route_id=route.route_id: on_route_selected(route_id))
            toolbar.addAction(action)

        return toolbar
