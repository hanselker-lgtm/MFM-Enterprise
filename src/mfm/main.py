"""
Main application entry point.
"""

from __future__ import annotations

from mfm.application import Application


def main() -> None:
    app = Application()
    app.start()