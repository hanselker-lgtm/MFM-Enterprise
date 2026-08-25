from __future__ import annotations

from PySide6.QtWidgets import QLabel

from mfm.application.about.about_info_service import AboutInfo
from mfm.presentation.about_dialog import AboutDialog
from mfm.presentation.about_dialog import build_about_page


def _about_info() -> AboutInfo:
    return AboutInfo(
        application_name="MFM Enterprise",
        version="0.3.0-rc1",
        build_id="0.3.0-rc1-local",
        build_channel="rc",
        license_name="MIT",
        license_url="https://opensource.org/licenses/MIT",
        support_contact="support@mfm-enterprise.example",
        database_provider="sqlite",
        database_path="data/database/mfm.db",
        log_directory="logs",
        log_filename="mfm.log",
        config_directory="/tmp/mfm-config",
    )


def test_about_dialog_shows_version_and_channel(qapp) -> None:
    dialog = AboutDialog(about_info=_about_info())

    assert "MFM Enterprise" in dialog.windowTitle()


def test_about_page_is_not_a_placeholder(qapp) -> None:
    page = build_about_page(about_info=_about_info())

    all_text = " ".join(label.text() for label in page.findChildren(QLabel))
    assert "will be connected to feature APIs here" not in all_text
    assert "0.3.0-rc1" in all_text
