"""Status bar for the application shell."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    """Minimal status bar with route and feedback labels."""

    def __init__(self) -> None:
        super().__init__()
        self._route_label = QLabel("Ready")
        self._message_label = QLabel("MFM Enterprise")
        self.addPermanentWidget(self._route_label)
        self.addPermanentWidget(self._message_label)

    def set_route(self, route_label: str) -> None:
        self._route_label.setText(route_label)

    def set_message(self, message: str) -> None:
        self._message_label.setText(message)
        self.showMessage(message)
