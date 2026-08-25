"""Resolve filesystem paths for both development and packaged (frozen) runs.

When running from source (``python -m mfm``), everything lives under
the project checkout and can be read/written there freely.

When running as a packaged desktop build (PyInstaller), that's no
longer true: the executable's own directory is often read-only
(e.g. installed under Program Files on Windows) and, for a
--onefile build, the extraction directory is temporary and wiped
between runs. So packaged builds split paths in two:

- Bundled resources (default.toml, the Alembic migration scripts,
  alembic.ini) are read-only and ship inside the package.
- User data (the SQLite database, logs, user.toml overrides) must
  live in a writable, per-user, OS-appropriate location and persist
  across runs and app upgrades.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def is_frozen() -> bool:
    """True when running from a PyInstaller-packaged build."""

    return bool(getattr(sys, "frozen", False))


def bundled_resource_dir() -> Path:
    """Directory containing read-only bundled resources.

    In a frozen build this is PyInstaller's extraction/bundle
    directory (``sys._MEIPASS`` for --onefile, the executable's
    directory for --onedir). In development it's the project root.
    """

    if is_frozen():
        meipass = getattr(sys, "_MEIPASS", None)
        if meipass:
            return Path(meipass)
        return Path(sys.executable).resolve().parent

    # src/mfm/runtime_paths.py -> mfm -> src -> project root
    return Path(__file__).resolve().parents[2]


def user_data_dir(app_name: str = "MFM Enterprise") -> Path:
    """Writable, per-user, OS-appropriate directory for app data.

    Only used for frozen builds; development runs keep using the
    project checkout so `git status` stays predictable for
    contributors. Created on first access if it doesn't exist.
    """

    if not is_frozen():
        return Path(__file__).resolve().parents[2]

    if sys.platform == "win32":
        base = os.environ.get("APPDATA") or str(Path.home() / "AppData" / "Roaming")
        path = Path(base) / app_name
    elif sys.platform == "darwin":
        path = Path.home() / "Library" / "Application Support" / app_name
    else:
        base = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local" / "share")
        path = Path(base) / app_name.lower().replace(" ", "-")

    path.mkdir(parents=True, exist_ok=True)
    return path
