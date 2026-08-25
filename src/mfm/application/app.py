"""
Main application composition root.
"""

from __future__ import annotations

from pathlib import Path

from mfm.application_context import ApplicationContext
from mfm.common.logging import LoggingManager
from mfm.config.manager import ConfigManager


class Application:

    def __init__(self) -> None:
        self.context: ApplicationContext | None = None

    def start(self) -> int:

        # Imported lazily: CompositionRoot pulls in mfm.application.*
        # submodules, and importing those re-enters mfm.application's
        # __init__ (which imports this module) while it is still being
        # loaded, causing a circular import if this were a top-level
        # import instead.
        from mfm.composition_root import CompositionRoot

        config = ConfigManager.load()

        self.context = ApplicationContext(config)

        self.context.logger = LoggingManager.initialize(
            config
        )

        self.context.logger.info(
            "Application started."
        )

        from mfm.runtime_paths import bundled_resource_dir

        project_root = bundled_resource_dir()
        composition_root = CompositionRoot(config=config, project_root=project_root)
        shell = composition_root.build_shell()

        self.context.logger.info("Application shell built; showing main window.")

        return shell.start()
