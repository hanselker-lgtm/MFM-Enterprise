# RC-003 Build Release Candidate Report

Date: 2026-07-17
Target version: 0.3.0-rc1
Scope: Release engineering only. No business functionality added.

## Summary

RC build artifacts were generated for 0.3.0-rc1, with dependency freezing and reproducibility evidence captured.

Primary outputs:
- Installable wheel and source distribution for 0.3.0-rc1.
- Alpha baseline wheel for upgrade verification.
- Build manifest and dependency manifest.

## Task Outcomes

1. Update version to 0.3.0-rc1
- Completed.
- Updated release version markers in package/runtime/config files.

2. Freeze dependencies
- Completed.
- Dependency manifest created at build/RC-003-Dependency-Manifest.txt.

3. Produce reproducible build
- Completed.
- Rebuilt wheel hash matched initial wheel hash.

4. Generate distributable package(s)
- Completed.
- Artifacts produced:
  - dist/rc1/mfm_enterprise-0.3.0rc1-py3-none-any.whl
  - dist/rc1/mfm_enterprise-0.3.0rc1.tar.gz

5. Verify clean installation
- Completed.
- Clean install verification reported version 0.3.0rc1.

6. Verify upgrade from alpha
- Completed.
- Alpha artifact (0.3.0a1) installed and upgraded to rc1 in isolated environment.

7. Verify backup compatibility
- Completed.
- SQLite file backup/restore compatibility check executed with preserved baseline state.

8. Verify startup from clean environment
- Completed (smoke).
- Startup smoke validation used short-lived process launch check for no immediate crash.

9. Execute full regression tests
- Completed.
- python -m pytest -q passed.

10. Update RELEASE_NOTES if required
- Completed.
- RELEASE_NOTES.md retained RC content and is aligned with RC build context.

## Artifact Evidence

- Wheel SHA256: C04957B9D2C52E977B60A76DF712995B018E150F7A45C4881CF56AAFB1CB1665
- Rebuilt wheel SHA256: C04957B9D2C52E977B60A76DF712995B018E150F7A45C4881CF56AAFB1CB1665
- Sdist SHA256: 8B358FBBFA0B46C6FA56B4A0C6B9633DB8DCFFDA9EE32A5C74D1DD3EE132AD8C

Reproducibility verdict:
- Wheel reproducibility confirmed for repeated build under pinned SOURCE_DATE_EPOCH.

## Deliverables

- Build artifact(s): dist/alpha, dist/rc1, dist/rc1-rebuild
- Build manifest: build/RC-003-Build-Manifest.json
- Dependency manifest: build/RC-003-Dependency-Manifest.txt
- Build report: RC-003-Build-Report.md
