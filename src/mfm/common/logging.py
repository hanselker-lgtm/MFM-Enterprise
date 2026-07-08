"""
Logging management for MFM Enterprise.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from mfm.config.models import Config


class LoggingManager:
    """Central logging manager for the application."""

    _initialized = False

    @classmethod
    def initialize(cls, config: Config) -> logging.Logger:

        if cls._initialized:
            return logging.getLogger("mfm")

        log_directory = Path(config.logging.directory)
        log_directory.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("mfm")
        logger.setLevel(getattr(logging, config.logging.level.upper()))

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        file_handler = RotatingFileHandler(
            log_directory / config.logging.filename,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.handlers.clear()
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        cls._initialized = True

        logger.info("Logging initialized")

        return logger

    @staticmethod
    def get_logger(name: str | None = None) -> logging.Logger:

        if name:
            return logging.getLogger(name)

        return logging.getLogger("mfm")