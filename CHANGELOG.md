# Changelog

All notable changes to this project are documented in this file.

Format:
- Semantic versioning style tags.
- Sections: Added, Changed, Fixed, Docs, Quality.

## [0.3.0-rc1] - 2026-07-17

First public release-candidate preparation milestone.

### Docs
- Added release notes baseline in RELEASE_NOTES.md.
- Added versioning policy in docs/releases/VERSIONING.md.
- Added backup/restore runbook in docs/releases/BACKUP_RESTORE.md.
- Added installation procedure in docs/releases/INSTALLATION.md.
- Added upgrade procedure in docs/releases/UPGRADE.md.
- Added release checklist in docs/releases/RELEASE_CHECKLIST.md.

### Changed
- Consolidated release-governance documentation for distribution readiness.

### Quality
- Release-preparation validation requires:
	- python -m pytest -q
	- python -m ruff check .

## [0.3.0-alpha1] - 2026-07-17

Baseline application/package version in current repository metadata.

### Added
- Consolidated RC assessment reports and baseline verification artifacts for architecture, API, UI consistency, and end-to-end validation.

### Quality
- Repository validation baseline reported as green in latest RC assessments.

