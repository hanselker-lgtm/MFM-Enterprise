# Versioning Policy

## Purpose

Define one consistent versioning policy for MFM Enterprise release artifacts and runtime metadata.

## Version Format

MFM Enterprise uses semantic versioning with pre-release channels:
- MAJOR.MINOR.PATCH
- Optional pre-release suffix: -alphaN, -rcN

Examples:
- 0.3.0-alpha1
- 0.3.0-rc1
- 0.3.0

## Source Of Truth

Primary source:
- pyproject.toml -> project.version

Mirrors that must match before release:
- src/mfm/version.py -> __version__
- RELEASE_NOTES.md -> release header
- CHANGELOG.md -> latest release entry

## Channel Rules

- alpha: internal development and capability-lock milestones.
- rc: release-candidate hardening and controlled validation.
- stable: production release for end users.

Promotion path:
- alphaN -> rc1 -> stable

## Version Bump Rules

- PATCH: documentation-only fixes, bug fixes with no contract break.
- MINOR: backward-compatible functionality additions.
- MAJOR: incompatible contract or behavior changes.

## Release Integrity Checks

Before creating a release tag:
1. Ensure version values are identical in all required files.
2. Ensure changelog top entry matches target release version/date.
3. Ensure release notes header matches target release version/date.
4. Run required validation gates.

## Tagging Convention

- Git tag format: vMAJOR.MINOR.PATCH[-channelN]
- Examples:
  - v0.3.0-rc1
  - v0.3.0

## Non-Goals

- This policy does not define business feature scope.
- This policy does not replace deployment environment approvals.
