"""Application service backing the About/diagnostics surface.

Closes 0.4 backlog item 2 (production-ready About surface with
version/build/channel, license reference, support route, and
diagnostics paths).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mfm.config.models import Config


@dataclass(frozen=True, slots=True)
class AboutInfo:
    """Everything the About surface needs to render, with no Qt dependency."""

    application_name: str
    version: str
    build_id: str
    build_channel: str
    license_name: str
    license_url: str
    support_contact: str
    database_provider: str
    database_path: str
    log_directory: str
    log_filename: str
    config_directory: str


class AboutInfoService:
    """Builds :class:`AboutInfo` from application configuration and version metadata."""

    #: Kept centralized so the license reference is consistent wherever it is shown.
    LICENSE_NAME = "MIT"
    LICENSE_URL = "https://opensource.org/licenses/MIT"

    #: Support route for the pilot association. Update via config in future
    #: iterations if multiple associations need distinct support contacts.
    SUPPORT_CONTACT = "support@mfm-enterprise.example"

    def __init__(self, *, config: Config, config_directory: Path) -> None:
        self._config = config
        self._config_directory = config_directory

    def get_about_info(self) -> AboutInfo:
        from mfm.version import __build_channel__
        from mfm.version import __build_id__
        from mfm.version import __version__

        return AboutInfo(
            application_name=self._config.application.name,
            version=__version__,
            build_id=__build_id__,
            build_channel=__build_channel__,
            license_name=self.LICENSE_NAME,
            license_url=self.LICENSE_URL,
            support_contact=self.SUPPORT_CONTACT,
            database_provider=self._config.database.provider,
            database_path=self._config.database.path,
            log_directory=self._config.logging.directory,
            log_filename=self._config.logging.filename,
            config_directory=str(self._config_directory),
        )
