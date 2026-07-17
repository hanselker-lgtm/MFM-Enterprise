# MFM Enterprise Release Notes

Release: 0.3.0-rc1 (public release candidate)
Date: 2026-07-17
Status: Release preparation complete; candidate publication pending final release checklist sign-off.

## Summary

This release candidate focuses on distribution readiness and release governance.
No business functionality was added in this release-preparation milestone.

Primary outcomes:
- Release documentation baseline established.
- Versioning, installation, backup/restore, and upgrade procedures documented.
- About dialog requirements reviewed for release supportability.
- Release checklist formalized for repeatable candidate publication.

## Scope Of This Candidate

In scope:
- Release artifacts and operational documentation.
- Public release process and readiness controls.

Out of scope:
- Domain behavior changes.
- New end-user business features.
- Architectural refactors.

## Quality Gates

Validation commands for this milestone:
- python -m pytest -q
- python -m ruff check .

Expected result at release-preparation sign-off:
- Full test suite passes.
- Ruff passes with no violations.

## Known Limitations

- About page in the application shell is still a placeholder route and requires implementation in a later productization milestone.
- Operational migration tooling is documented as required for production, but repository migration scaffolding remains a separate execution step.

## About Dialog Review Summary

The About dialog for public distribution must include:
- Product name and semantic version.
- Build identifier (commit hash or build number).
- Release channel (alpha, rc, stable).
- License summary and full license reference path.
- Support contact information and issue reporting channel.
- Runtime diagnostics shortcut (config path, log path, database path).

Current state:
- Navigation route exists for About.
- Production-ready About content is not yet implemented.

## Upgrade Impact

- No business data model changes are introduced by RE-002 documentation work.
- Standard pre-upgrade safety controls (backup and rollback readiness) remain mandatory for all candidate promotions.

## Support

This release candidate is intended for controlled validation.
Support operations should follow the procedures in:
- docs/releases/INSTALLATION.md
- docs/releases/BACKUP_RESTORE.md
- docs/releases/UPGRADE.md
- docs/releases/RELEASE_CHECKLIST.md
