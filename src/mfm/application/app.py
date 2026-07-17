"""
Main application composition root.
"""

from __future__ import annotations

from mfm.application_context import ApplicationContext
from mfm.common.logging import LoggingManager
from mfm.config.manager import ConfigManager


class Application:

    def __init__(self) -> None:
        self.context: ApplicationContext | None = None

    def start(self):

        config = ConfigManager.load()

        self.context = ApplicationContext(config)

        self.context.logger = LoggingManager.initialize(
            config
        )

        self.context.logger.info(
            "Application started."
        )
