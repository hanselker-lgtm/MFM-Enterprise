from __future__ import annotations

from pathlib import Path

from mfm.application.about.about_info_service import AboutInfoService
from mfm.config.models import ApplicationConfig
from mfm.config.models import Config
from mfm.config.models import DatabaseConfig
from mfm.config.models import GuiConfig
from mfm.config.models import LoggingConfig


def _config() -> Config:
    return Config(
        application=ApplicationConfig(
            name="MFM Enterprise", version="0.3.0-rc1", language="da", theme="system"
        ),
        database=DatabaseConfig(provider="sqlite", path="data/database/mfm.db"),
        logging=LoggingConfig(level="INFO", directory="logs", filename="mfm.log"),
        gui=GuiConfig(style="Fusion"),
    )


def test_about_info_reports_version_build_and_channel() -> None:
    service = AboutInfoService(config=_config(), config_directory=Path("/tmp/mfm-config"))

    info = service.get_about_info()

    assert info.application_name == "MFM Enterprise"
    assert info.version == "0.3.0-rc1"
    assert info.build_channel == "rc"
    assert info.build_id


def test_about_info_reports_license_and_support_route() -> None:
    service = AboutInfoService(config=_config(), config_directory=Path("/tmp/mfm-config"))

    info = service.get_about_info()

    assert info.license_name == "MIT"
    assert info.license_url.startswith("https://")
    assert "@" in info.support_contact


def test_about_info_reports_diagnostics_paths() -> None:
    service = AboutInfoService(config=_config(), config_directory=Path("/tmp/mfm-config"))

    info = service.get_about_info()

    assert info.database_provider == "sqlite"
    assert info.database_path == "data/database/mfm.db"
    assert info.log_directory == "logs"
    assert info.log_filename == "mfm.log"
    assert info.config_directory == "/tmp/mfm-config"
