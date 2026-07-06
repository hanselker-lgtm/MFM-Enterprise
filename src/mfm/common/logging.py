"""
Application logging.
"""

from pathlib import Path
import logging


def configure_logging(log_file: str, level: str = "INFO") -> None:
    """Configure application logging."""

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, level.upper()),
        format="%(asctime)s %(levelname)s %(name)s : %(message)s",
    )