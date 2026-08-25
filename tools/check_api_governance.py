#!/usr/bin/env python3
"""Standalone API governance gate (0.4 backlog item 5).

Runs the Public API Standard architecture checks
(tests/architecture/test_feature_api_architecture.py and
test_dependency_guard.py) as a release-gate command, independent of
however the rest of the test suite is invoked. Exits non-zero on any
violation, so it can be dropped into a CI pipeline or a pre-release
checklist alongside the existing:

    python -m pytest -q
    python -m ruff check .

as:

    python tools/check_api_governance.py

This does not duplicate those tests' logic -- it simply runs them as
a scoped, clearly-named gate so "API governance" has its own pass/fail
signal instead of being invisible inside a full test run.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

GOVERNANCE_TEST_PATHS = (
    "tests/architecture/test_feature_api_architecture.py",
    "tests/architecture/test_dependency_guard.py",
)


def main() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *GOVERNANCE_TEST_PATHS],
        cwd=PROJECT_ROOT,
    )

    if result.returncode == 0:
        print("API governance gate: PASS (export-surface + boundary rules)")
    else:
        print("API governance gate: FAIL -- see failures above", file=sys.stderr)

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
