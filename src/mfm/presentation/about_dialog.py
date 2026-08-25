"""About dialog widget for the MFM Enterprise application shell.

Renders the data produced by :class:`mfm.application.about.about_info_service.AboutInfoService`.
Kept free of business logic: the dialog only lays out fields, so it stays
trivially testable via ``AboutInfoService`` on its own.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QTabWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.application.about.about_info_service import AboutInfo


class AboutDialog(QDialog):
    """Production-ready About surface: version, license, support, diagnostics."""

    def __init__(self, *, about_info: AboutInfo, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"About {about_info.application_name}")
        self.setMinimumWidth(420)

        layout = QVBoxLayout(self)

        heading = QLabel(f"<h2>{about_info.application_name}</h2>")
        layout.addWidget(heading)

        tabs = QTabWidget()
        tabs.addTab(self._build_general_tab(about_info), "General")
        tabs.addTab(self._build_diagnostics_tab(about_info), "Diagnostics")
        layout.addWidget(tabs)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self.accept)
        buttons.button(QDialogButtonBox.StandardButton.Close).clicked.connect(self.accept)
        layout.addWidget(buttons)

    def _build_general_tab(self, about_info: AboutInfo) -> QWidget:
        page = QWidget()
        form = QFormLayout(page)
        form.addRow("Version:", QLabel(about_info.version))
        form.addRow("Build:", QLabel(about_info.build_id))
        form.addRow("Channel:", QLabel(about_info.build_channel.upper()))

        license_label = QLabel(
            f'<a href="{about_info.license_url}">{about_info.license_name} License</a>'
        )
        license_label.setOpenExternalLinks(True)
        form.addRow("License:", license_label)

        support_label = QLabel(
            f'<a href="mailto:{about_info.support_contact}">{about_info.support_contact}</a>'
        )
        support_label.setOpenExternalLinks(True)
        support_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        form.addRow("Support:", support_label)
        return page

    def _build_diagnostics_tab(self, about_info: AboutInfo) -> QWidget:
        page = QWidget()
        form = QFormLayout(page)
        form.addRow("Database provider:", QLabel(about_info.database_provider))
        db_path_label = QLabel(about_info.database_path)
        db_path_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        form.addRow("Database path:", db_path_label)

        log_label = QLabel(f"{about_info.log_directory}/{about_info.log_filename}")
        log_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        form.addRow("Log file:", log_label)

        config_label = QLabel(about_info.config_directory)
        config_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        config_label.setWordWrap(True)
        form.addRow("Config directory:", config_label)
        return page


def build_about_page(*, about_info: AboutInfo) -> QWidget:
    """Build the non-modal About page used as the ``administration.about`` route.

    The application shell renders module pages inline rather than as
    dialogs, so the About *route* reuses the same information as
    :class:`AboutDialog` but as a plain page widget.
    """

    page = QWidget()
    layout = QVBoxLayout(page)
    layout.addWidget(QLabel(f"<h2>{about_info.application_name}</h2>"))

    general = QFormLayout()
    general.addRow("Version:", QLabel(about_info.version))
    general.addRow("Build:", QLabel(about_info.build_id))
    general.addRow("Channel:", QLabel(about_info.build_channel.upper()))
    license_label = QLabel(
        f'<a href="{about_info.license_url}">{about_info.license_name} License</a>'
    )
    license_label.setOpenExternalLinks(True)
    general.addRow("License:", license_label)
    support_label = QLabel(
        f'<a href="mailto:{about_info.support_contact}">{about_info.support_contact}</a>'
    )
    support_label.setOpenExternalLinks(True)
    general.addRow("Support:", support_label)
    layout.addLayout(general)

    layout.addWidget(QLabel("<h3>Diagnostics</h3>"))
    diagnostics = QFormLayout()
    diagnostics.addRow("Database provider:", QLabel(about_info.database_provider))
    diagnostics.addRow("Database path:", QLabel(about_info.database_path))
    diagnostics.addRow(
        "Log file:", QLabel(f"{about_info.log_directory}/{about_info.log_filename}")
    )
    diagnostics.addRow("Config directory:", QLabel(about_info.config_directory))
    layout.addLayout(diagnostics)
    layout.addStretch(1)
    return page
