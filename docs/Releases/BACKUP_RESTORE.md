# Backup And Restore Strategy

## Purpose

Define minimum operational controls for protecting and recovering MFM Enterprise data in release-candidate and production-like environments.

## Scope

Applies to:
- SQLite deployments (current default profile).
- Future production deployments that use managed database engines.

## Backup Strategy

### Minimum Backup Types

1. Pre-upgrade backup (mandatory)
- Take a full backup immediately before any application or schema upgrade.

2. Daily scheduled backup
- Capture at least one full backup per 24h period.

3. On-demand backup
- Allow operator-triggered backup before high-risk maintenance operations.

### SQLite Baseline Procedure

For SQLite file-based environments:
1. Stop application write traffic.
2. Copy database file to timestamped backup location.
3. Record checksum for integrity verification.
4. Record app version + config profile with backup metadata.

Minimum metadata:
- backup_id
- timestamp_utc
- app_version
- database_path
- checksum
- operator

### Retention

Recommended baseline retention:
- Daily backups: 14 days
- Weekly backups: 8 weeks
- Pre-release and pre-upgrade backups: keep until release sign-off + rollback window closure

## Restore Strategy

### Restore Preconditions

1. Incident or rollback decision approved.
2. Correct backup artifact identified and checksum verified.
3. Target runtime version and config are known.

### SQLite Restore Procedure

1. Stop application.
2. Preserve current database file as emergency snapshot.
3. Replace database file with selected backup.
4. Validate file permissions and path configuration.
5. Start application in verification mode.
6. Run smoke checks on key workflows.

### Post-Restore Validation

Minimum checks:
- Application starts without fatal errors.
- Organization, Projects, Documents, and Accounting basic reads succeed.
- Recent expected records are present.
- Log file contains no restore-related fatal errors.

## Testing And Drill Frequency

- Perform restore drill at least once per release-candidate cycle.
- Document drill result, duration, and any gaps.

## Roles

- Release owner: authorizes pre-release backups.
- Operator: executes backup/restore steps.
- QA owner: validates restored system behavior.

## Known Gaps

- Repository does not yet ship automated backup tooling scripts.
- This runbook defines operational policy until automation is added.
