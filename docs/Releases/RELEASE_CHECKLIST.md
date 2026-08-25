# Release Checklist

## Purpose

Provide a single checklist for preparing and publishing a public release candidate.

## Version And Artifact Integrity

- [ ] Version in pyproject.toml is set to target release.
- [ ] src/mfm/version.py matches target release.
- [ ] RELEASE_NOTES.md header matches target release.
- [ ] CHANGELOG.md top entry matches target release/date.

## Documentation Readiness

- [ ] docs/releases/VERSIONING.md reviewed.
- [ ] docs/releases/INSTALLATION.md reviewed.
- [ ] docs/releases/BACKUP_RESTORE.md reviewed.
- [ ] docs/releases/UPGRADE.md reviewed.

## About Dialog Requirements Review

- [ ] About dialog includes product name.
- [ ] About dialog includes semantic version.
- [ ] About dialog includes build identifier.
- [ ] About dialog includes release channel.
- [ ] About dialog includes license summary/reference.
- [ ] About dialog includes support contact route.
- [ ] About dialog includes diagnostics pointers (config/log/database paths).

Note:
- Current repository state uses a placeholder About route in the shell and requires follow-up implementation before public stable release.

## Data Protection And Upgrade Controls

- [ ] Backup performed before candidate publication.
- [ ] Restore drill validated for current release cycle.
- [ ] Upgrade path documented and dry-run completed.
- [ ] Rollback plan documented and executable.

## Quality Gates

- [ ] python -m pytest -q passes.
- [ ] python -m ruff check . passes.

## Release Governance

- [ ] Working tree is clean for release cut.
- [ ] Release commit/tag planned and approved.
- [ ] Release notes approved by release owner.
- [ ] Final GO/NO-GO decision recorded.
