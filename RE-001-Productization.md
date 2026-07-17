# RE-001 Productization Assessment

Date: 2026-07-17
Scope: Determine what is required before MFM Enterprise can be distributed to end users.
Constraint: Assessment only. No feature additions or behavioral changes.

## Current Status

Overall status: NOT READY for end-user distribution.

Quality gates at code level are strong (tests and lint are green), but productization essentials for installation, packaging, operations, supportability, and release governance are incomplete.

### Requirement Status Matrix

| Area | Current status | Evidence | Distribution readiness |
|---|---|---|---|
| Installation | No end-user installation guide | `README.md` currently contains only product description text | Missing |
| Packaging | Python package metadata exists, but no distributable/installer process documented | `pyproject.toml` has build-system/project metadata; no wheel/installer release SOP doc found | Partial |
| Versioning | Multiple version sources are inconsistent | `pyproject.toml` = `0.3.0-alpha1`, `src/mfm/version.py` = `0.3.0-alpha1`, `config/default.toml` = `0.3.0-alpha`, `CHANGELOG.md` top entries are `v0.6.0-alpha`/`v0.5.0-alpha` | Missing |
| Configuration | Runtime loader expects one schema; environment TOMLs use another schema | `src/mfm/config/manager.py` + `src/mfm/config/models.py` expect `database.provider/path`, `logging.directory/filename`, `gui.style`; `config/development.toml` and `config/production.toml` use `database.engine/...` and `logging.file` | Missing |
| Logging | Rotating file logging exists | `src/mfm/common/logging.py` initializes logger, file rotation and console handler | Partial |
| Database deployment | Basic initialization exists; production migration path is declared but not provisioned | `src/mfm/database/initialize.py` states production must use Alembic; no Alembic config/scripts found; `migrations/` folder is empty | Missing |
| Backup | No operational backup procedure/tooling found | No backup runbook/scripts for end-user operations | Missing |
| Restore | No operational restore procedure/tooling found | Restore appears only as internal/domain test semantics, not operator runbook | Missing |
| Upgrade strategy | No documented app/database upgrade process for users | No version-to-version upgrade/migration SOP found | Missing |
| Crash handling | No global crash/exception handling strategy at app shell boundary | `src/mfm/main.py` and `src/mfm/application/app.py` show no global exception hook, crash reporter, or fatal error UX path | Missing |
| Support information | No support channel/SLA/contact details found for end users | No support section in README/About docs | Missing |
| License | Declared as MIT in package metadata, but repository license file absent | `pyproject.toml` has MIT; `LICENSE/` directory is empty | Missing |
| About dialog | About route exists, but currently placeholder page, not product support/legal metadata | `src/mfm/presentation/application_shell.py` route `administration.about` uses placeholder loader | Missing |
| Release notes | Internal baseline/review docs exist, but no end-user release notes format/process found | `docs/Releases/RELEASE-001-baseline.md`, `docs/Releases/RELEASE-002-baseline.md`, RC reports exist but are governance artifacts | Partial |
| CHANGELOG | Present but not aligned to current release/version stream | `CHANGELOG.md` entries do not align with current package/app versioning state | Partial |

## Missing Items

### Critical

1. Configuration contract mismatch across runtime and environment files
- End-user builds risk startup/config failures because runtime schema and shipped environment TOMLs do not match.

2. No production migration framework in repository
- Production path explicitly requires Alembic, but no Alembic configuration or migration chain is available.

3. No backup and restore operating procedure
- No documented or scripted mechanism to protect and recover user data for deployed installations.

4. No upgrade strategy (application + schema + rollback)
- No controlled method for moving existing user installations between released versions.

### High

1. Versioning inconsistency across package, app config, and changelog stream
- Release artifacts cannot be reliably identified or audited by operators/end users.

2. License distribution gap
- MIT is declared in metadata, but no distributed license file is present in repository license directory.

3. About dialog not productized
- No visible product identity/support/legal/build details in-app for end-user support scenarios.

4. No installation and packaging runbook for end users
- No documented steps for install/upgrade/uninstall on supported targets.

### Medium

1. Crash handling and fatal-error UX are not defined
- No global uncaught exception handling policy/reporting path.

2. Logging is implemented but lacks operational policy documentation
- Retention/export/privacy guidance and operator troubleshooting procedure are missing.

3. Release notes process is internal-governance oriented
- Need user-facing release-note template that communicates features, fixes, known issues, and upgrade notes.

### Low

1. README is too minimal for distribution
- Product description exists, but no operational guidance.

2. Support information is not surfaced
- No contact point, support expectations, or issue-reporting channel documented.

## Recommended Release Plan

### Phase 1 - Distribution Baseline (Blockers)

1. Establish single source of truth for versioning
- Align `pyproject.toml`, `src/mfm/version.py`, config version fields, release tags, and CHANGELOG format.

2. Normalize configuration contract
- Make all shipped TOML profiles conform to runtime schema used by `ConfigManager` and `Config` models.

3. Implement migration baseline
- Add Alembic project scaffolding, baseline migration, and release-time migration command documentation.

4. Define backup/restore SOP
- Provide operator-grade runbooks for backup frequency, verification, restore rehearsal, and rollback points.

5. Define upgrade strategy
- Publish upgrade path per release including pre-checks, migration execution, data backup precondition, and rollback criteria.

### Phase 2 - End-user Product Readiness

1. Publish installation and packaging guide
- Supported OS/runtime matrix, install prerequisites, first-run setup, and uninstall/update instructions.

2. Productize About and support surfaces
- Add app version/build hash, license reference, support contacts, diagnostic info, and log location visibility.

3. Finalize license and legal artifacts
- Include repository/distribution license file and ensure package/distribution metadata consistency.

4. Add user-facing release notes template
- Standard sections: what changed, migration notes, known issues, support impact.

### Phase 3 - Operational Hardening

1. Add crash-handling policy
- Global exception hook, fatal-error UI path, safe shutdown behavior, and incident correlation IDs.

2. Logging policy and retention controls
- Document retention, rotation limits, PII constraints, and support bundle workflow.

3. Release checklist automation
- Pre-release gating for version consistency, migration presence, license presence, and release-note completeness.

## Productization Verdict

Distribution decision: NO-GO.

Rationale:
- Code-quality gates pass, but critical productization controls (config coherence, migrations, backup/restore, and upgrades) are not yet release-complete for end users.
