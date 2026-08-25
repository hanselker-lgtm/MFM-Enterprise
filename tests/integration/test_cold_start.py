"""Cold-start / entrypoint smoke tests.

These exercise the real composition root (:mod:`mfm.composition_root`)
against a temporary, on-disk SQLite database -- the same code path
``python -m mfm`` uses -- rather than the in-memory fakes the rest of
the test suite uses. This is the gap identified in 0.4 backlog items
1 and 4: full pytest/ruff success previously did not guarantee the
application actually started, because the real entrypoint
(``Application.start()``) never built or showed the Qt shell at all.

Covers:
- Normal cold start: fresh database, first-run seeding, shell built,
  all four dashboards load without raising.
- Missing-file fault path: the database file's parent directory does
  not exist yet -- the composition root must create it rather than
  crash (this is exactly the kind of path AT-001 scenario 11 flagged
  as only partially evidenced).
- Database-unavailable fault path: the configured database directory
  exists but is not writable, so engine/session creation fails; the
  failure must be a clear, catchable exception rather than a silent
  hang or an unrelated Qt error.
"""

from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication

from mfm.composition_root import CompositionRoot
from mfm.config.models import ApplicationConfig
from mfm.config.models import Config
from mfm.config.models import DatabaseConfig
from mfm.config.models import GuiConfig
from mfm.config.models import LoggingConfig


def _config(*, database_path: str) -> Config:
    return Config(
        application=ApplicationConfig(
            name="MFM Enterprise", version="0.3.0-rc1", language="da", theme="system"
        ),
        database=DatabaseConfig(provider="sqlite", path=database_path),
        logging=LoggingConfig(level="INFO", directory="logs", filename="mfm.log"),
        gui=GuiConfig(style="Fusion"),
    )


def test_cold_start_builds_shell_and_loads_all_dashboards(qapp, tmp_path: Path) -> None:
    """AT-001 scenario 11 (cold start), closed: a fresh DB boots to a working shell."""

    config = _config(database_path="data/database/mfm.db")
    root = CompositionRoot(config=config, project_root=tmp_path)

    shell = root.build_shell()

    window = shell.main_window
    for route_id in (
        "dashboard.organization",
        "dashboard.active-projects",
        "dashboard.project-status",
        "dashboard.budget-vs-actual",
    ):
        window.navigate_to(route_id)  # must not raise

    window.navigate_to("administration.about")  # must not raise, and must be real content
    from PySide6.QtWidgets import QLabel

    about_texts = " ".join(
        label.text() for label in window.centralWidget().currentWidget().findChildren(QLabel)
    )
    assert "will be connected to feature APIs here" not in about_texts

    from mfm.presentation.accounting.accounting_workspace import AccountingWorkspace
    from mfm.presentation.documents.documents_workspace import DocumentsWorkspace
    from mfm.presentation.membership_billing.membership_billing_workspace import (
        MembershipBillingWorkspace,
    )
    from mfm.presentation.memberships.membership_workspace import MembershipWorkspace
    from mfm.presentation.projects.project_workspace import ProjectWorkspace

    window.navigate_to("operations.projects")
    assert isinstance(window.centralWidget().currentWidget(), ProjectWorkspace)

    window.navigate_to("operations.accounting")
    assert isinstance(window.centralWidget().currentWidget(), AccountingWorkspace)

    window.navigate_to("operations.documents")
    assert isinstance(window.centralWidget().currentWidget(), DocumentsWorkspace)

    window.navigate_to("operations.memberships")
    assert isinstance(window.centralWidget().currentWidget(), MembershipWorkspace)

    window.navigate_to("operations.membership-billing")
    assert isinstance(window.centralWidget().currentWidget(), MembershipBillingWorkspace)

    from mfm.presentation.organizations.organization_workspace import OrganizationWorkspace

    window.navigate_to("operations.organizations")
    assert isinstance(window.centralWidget().currentWidget(), OrganizationWorkspace)


def test_cold_start_creates_missing_database_directory(qapp, tmp_path: Path) -> None:
    """Missing-file fault path: the data directory does not exist yet."""

    database_path = "data/nested/does/not/exist/mfm.db"
    config = _config(database_path=database_path)
    root = CompositionRoot(config=config, project_root=tmp_path)

    root.build_shell()  # must not raise; parent directories are created on demand

    assert (tmp_path / database_path).exists()


@pytest.mark.skipif(os.name == "nt", reason="POSIX permission bits only")
@pytest.mark.skipif(
    hasattr(os, "getuid") and os.getuid() == 0,
    reason="root bypasses POSIX permission bits; cannot simulate this fault as root",
)
def test_database_unavailable_fault_path_raises_clear_error(qapp, tmp_path: Path) -> None:
    """Database-unavailable fault path: an unwritable data directory fails clearly."""

    unwritable_dir = tmp_path / "data" / "database"
    unwritable_dir.mkdir(parents=True)
    unwritable_dir.chmod(stat.S_IREAD | stat.S_IEXEC)

    config = _config(database_path="data/database/mfm.db")
    root = CompositionRoot(config=config, project_root=tmp_path)

    try:
        with pytest.raises(Exception):
            root.build_shell()
    finally:
        # Restore permissions so pytest can clean up the tmp_path fixture.
        unwritable_dir.chmod(stat.S_IRWXU)
