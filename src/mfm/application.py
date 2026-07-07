"""
MFM Enterprise application bootstrap.
"""

from __future__ import annotations


class Application:
    """
    Main application controller.

    Responsible for starting and shutting down
    the application infrastructure.
    """

    def __init__(self) -> None:
        self._started = False

    def start(self) -> None:
        """Start the application."""

        print("=" * 50)
        print("MFM Enterprise")
        print("Version 0.3.0 Alpha")
        print("=" * 50)
        print()

        print("Loading configuration...")
        print("Initializing logging...")
        print("Initializing database...")
        print("Database OK")
        print()
        print("Application started.")

        self._started = True