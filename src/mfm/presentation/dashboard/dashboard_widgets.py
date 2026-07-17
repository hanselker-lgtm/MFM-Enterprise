"""Reusable widgets for the dashboard workspace."""

from __future__ import annotations

from dataclasses import fields
from decimal import Decimal

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTextBrowser
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class SummaryTile(QWidget):
    """A small, readable metric tile for the dashboard workspace."""

    def __init__(self, title: str, value: str, subtitle: str) -> None:
        super().__init__()
        self._title = QLabel(title)
        self._title.setObjectName("summaryTileTitle")
        self._value = QLabel(value)
        self._value.setObjectName("summaryTileValue")
        self._subtitle = QLabel(subtitle)
        self._subtitle.setObjectName("summaryTileSubtitle")
        self._subtitle.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self._title)
        layout.addWidget(self._value)
        layout.addWidget(self._subtitle)
        layout.addStretch(1)
        self.setObjectName("summaryTile")
        self.setProperty("summaryTile", True)

    def set_value(self, value: str) -> None:
        self._value.setText(value)


class DashboardCard(QWidget):
    """Compact dashboard launcher card with summary and action hooks."""

    def __init__(
        self,
        title: str,
        summary: str,
        detail: str,
        *,
        on_open: callable,
        on_refresh: callable | None = None,
    ) -> None:
        super().__init__()
        self.setObjectName("dashboardCard")
        self.setProperty("dashboardCard", True)

        title_label = QLabel(title)
        title_label.setObjectName("dashboardCardTitle")
        summary_label = QLabel(summary)
        summary_label.setWordWrap(True)
        detail_label = QLabel(detail)
        detail_label.setObjectName("dashboardCardDetail")
        detail_label.setWordWrap(True)

        open_button = QPushButton("Open details")
        open_button.clicked.connect(lambda: on_open())
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(open_button)
        if on_refresh is not None:
            refresh_button = QPushButton("Refresh")
            refresh_button.clicked.connect(lambda: on_refresh())
            buttons_layout.addWidget(refresh_button)
        buttons_layout.addStretch(1)

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(summary_label)
        layout.addWidget(detail_label)
        layout.addLayout(buttons_layout)
        layout.addStretch(1)


class DashboardDetailWidget(QWidget):
    """Reporting-only detail renderer for dataclass DTOs."""

    def __init__(self) -> None:
        super().__init__()
        self._title = QLabel("Dashboard Detail")
        self._title.setObjectName("dashboardDetailTitle")
        self._viewer = QTextBrowser()
        self._viewer.setOpenExternalLinks(False)
        self._viewer.setReadOnly(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self._title)
        layout.addWidget(self._viewer)
        self.setObjectName("dashboardDetailWidget")

    def show_report(self, title: str, report: object) -> None:
        self._title.setText(title)
        self._viewer.setPlainText(self._format_report(report))

    @property
    def rendered_text(self) -> str:
        return self._viewer.toPlainText()

    def _format_report(self, report: object) -> str:
        lines = []
        for field in fields(report):
            value = getattr(report, field.name)
            lines.append(f"{field.name}: {self._format_value(value)}")
        return "\n".join(lines)

    def _format_value(self, value: object) -> str:
        if isinstance(value, tuple):
            return ", ".join(self._format_value(item) for item in value) if value else "(none)"
        if isinstance(value, Decimal):
            return format(value, "f")
        return str(value)
