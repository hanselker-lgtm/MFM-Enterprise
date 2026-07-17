# Upgrade Procedure

## Purpose

Define controlled upgrade steps for MFM Enterprise release candidates and future stable releases.

## Upgrade Principles

1. Always back up data before upgrade.
2. Never upgrade without a rollback path.
3. Keep application and schema versions aligned.
4. Validate critical workflows after upgrade.

## Pre-Upgrade Checklist

1. Confirm target version and release notes.
2. Confirm backup completed and checksum verified.
3. Confirm maintenance window and operator ownership.
4. Confirm current version and config snapshot captured.

## Upgrade Steps

1. Stop application.
2. Perform mandatory pre-upgrade backup.
3. Deploy new application version artifacts.
4. Apply database migration procedure for target version.
5. Start application.
6. Execute post-upgrade smoke validation.

## Post-Upgrade Validation

Minimum validation:
- Application starts and logs initialization success.
- Core modules load: Organizations, Projects, Documents, Accounting.
- Key read/write workflows operate without runtime errors.
- No critical errors in logs.

## Rollback Procedure

Trigger rollback when:
- Application fails to start.
- Critical workflows fail.
- Data integrity concerns appear.

Rollback steps:
1. Stop upgraded application.
2. Restore pre-upgrade backup.
3. Re-deploy previous known-good version.
4. Validate basic operations.
5. Record incident and root-cause entry.

## Notes On Database Migrations

- Production paths should use migration tooling and tracked revision history.
- If migration tooling is not yet provisioned in repository, do not perform unmanaged schema changes in release environments.
