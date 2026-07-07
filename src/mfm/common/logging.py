"""
Logging configuration.
"""

from __future__ import annotations

import logging

from logging.handlers import RotatingFileHandler

from mfm.common.paths import LOG_DIR


def configure_logging() -> logging.Logger:
    """
    Configure application logging.
    """

    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger("mfm")

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        LOG_DIR / "mfm.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger