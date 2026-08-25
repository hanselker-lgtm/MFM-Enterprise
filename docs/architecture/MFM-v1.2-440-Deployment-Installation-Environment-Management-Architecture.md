# MFM v1.2-440 – Deployment, Installation & Environment Management Architecture

Version: 1.2

Document ID: MFM-v1.2-440

Status: Functional Expansion

---

# 1. Purpose

This document defines the Deployment, Installation & Environment Management Architecture for MaritimForeningsManager (MFM) v1.2.

The objective is to establish a controlled and repeatable method for:

- Application Installation
- Initial Configuration
- Environment Preparation
- Database Initialization
- Application Upgrades
- Configuration Management
- Deployment Validation
- Uninstallation
- Recovery
- Environment Diagnostics

The architecture is designed for the practical deployment of MFM as a Windows application for a small non-profit organization.

The deployment model shall remain simple and maintainable while providing a clear path toward future server-based deployment if organizational requirements change.

---

# 2. Objectives

The deployment architecture shall provide:

- Repeatable Installation
- Controlled Configuration
- Environment Validation
- Database Initialization
- Upgrade Support
- Version Compatibility
- Installation Verification
- Recovery Procedures
- Diagnostic Information
- Clean Uninstallation
- Environment Separation

---

# 3. Deployment Principles

MFM follows these principles:

- Installation must be predictable.
- Configuration must be explicit.
- User data must not be confused with application files.
- Application upgrades must preserve data.
- Database migrations must be version controlled.
- Installation failures must be recoverable.
- Secrets must not be embedded in application packages.
- Deployment should require minimal technical knowledge.
- Core operation must not depend on external services.

---

# 4. Supported Deployment Model

The primary MFM v1.2 deployment model is:

```text
Windows PC

↓

MFM Application

↓

Local SQLite Database

↓

Document Repository

↓

Backup Repository
```

This model is appropriate for a small association operating primarily from one trusted workstation or controlled local environment.

---

# 5. Application Components

A standard installation may contain:

```text
MFM Application

Database

Document Repository

Configuration

Logs

Temporary Processing Area

Backup Configuration

Migration Information
```

Application binaries and user data should be stored separately.

---

# 6. Installation Structure

A logical installation structure may be:

```text
Application
    └── MFM

Data
    └── Database
    └── Documents
    └── Backups
    └── Logs
```

The exact Windows paths remain implementation-specific.

The architecture must avoid storing important user data only inside a replaceable application directory.

---

# 7. Application Files

Application files include:

- Executables
- Python Runtime or Packaged Runtime
- Application Modules
- Libraries
- Resources
- Icons
- Default Templates

Application files are replaceable during upgrades.

They must not contain the authoritative database or document archive.

---

# 8. User Data

User data includes:

- Database
- Documents
- Archive Files
- Configuration Data where persistent
- Audit History
- Migration History

User data must remain outside the application installation package.

---

# 9. Configuration

Configuration may include:

- Database Location
- Document Repository
- Backup Location
- Organization Information
- Language
- Currency
- Number Formats
- Email Configuration
- Integration Settings
- Security Settings

Sensitive credentials require protected storage.

---

# 10. Environment Types

MFM may use the following environments:

### Development

Used for software development.

### Test

Used for functional and regression testing.

### Staging

Used for release verification where required.

### Production

Used for real organizational data.

Production data must never be used casually in development or testing.

---

# 11. Environment Isolation

Each environment should have:

- Separate Database
- Separate Document Repository
- Separate Configuration
- Separate Logs
- Separate Test Users

External integration credentials should also be environment-specific.

---

# 12. System Requirements

Indicative requirements include:

- Supported Windows Version
- Sufficient RAM
- Sufficient SSD Storage
- User Account with Installation Permission
- Reliable Backup Destination

The exact minimum hardware requirements shall be documented with the production installer.

---

# 13. Pre-Installation Validation

Before installation, the installer or deployment procedure should verify:

- Supported Windows Version
- Available Disk Space
- Required Permissions
- Existing MFM Installation
- Existing Database
- Existing Data Directory
- Application Compatibility

Potential conflicts should be reported before files are changed.

---

# 14. Installation Workflow

```text
Start Installer

↓

Environment Check

↓

Installation Location

↓

Data Location

↓

Install Application

↓

Initialize Configuration

↓

Initialize Database

↓

Create Initial Administrator

↓

Run Validation

↓

Complete Installation
```

The user should receive a clear result at each major step.

---

# 15. First-Run Setup

The first application launch may perform:

```text
Environment Validation

↓

Database Check

↓

Configuration Check

↓

Initial Administrator Setup

↓

Organization Setup

↓

Security Configuration

↓

Backup Configuration

↓

Application Ready
```

The first-run process must not silently create unsafe defaults.

---

# 16. Initial Administrator

The first administrator account is created during first-run setup.

Required information may include:

- User Name
- Display Name
- Password
- Organization
- Contact Information where appropriate

The initial administrator must be forced to use a secure password.

---

# 17. Default Organization

For a normal single-organization installation:

```text
Installation

↓

Create Default Organization

↓

Assign Initial Administrator

↓

Continue Setup
```

Multi-organization mode remains optional.

---

# 18. Database Initialization

A new database is initialized using the current schema version.

Initialization includes:

- Tables
- Indexes
- Constraints
- Initial Configuration
- Security Structures
- Audit Structures
- Migration Version

The application must verify schema integrity before becoming operational.

---

# 19. Schema Version

Every production database contains a schema version.

Example:

```text
Application Version: 1.2.x

Database Schema: v12
```

The application must detect incompatible schema versions before performing business operations.

---

# 20. Upgrade Detection

At startup:

```text
Application Version

↓

Database Version

↓

Compare

↓

Same
→ Start

Older
→ Migration Required

Newer / Unsupported
→ Stop Safely
```

The application must never silently downgrade a newer database schema.

---

# 21. Upgrade Workflow

```text
Existing MFM

↓

Pre-Upgrade Validation

↓

Backup

↓

Verify Backup

↓

Install New Application

↓

Run Database Migration

↓

Validate Schema

↓

Validate Data

↓

Start Application

↓

Post-Upgrade Verification
```

The process shall preserve existing business data.

---

# 22. Upgrade Safety

Before an upgrade:

- Verify Backup
- Verify Disk Space
- Verify Application Version
- Verify Database Version
- Verify Migration Compatibility
- Verify Document Repository

If a critical precondition fails, the upgrade should stop before modifying production data.

---

# 23. Database Migration

Database migrations are:

- Versioned
- Ordered
- Tested
- Audited

Example:

```text
Schema v10

↓

Migration 10 → 11

↓

Schema v11

↓

Migration 11 → 12

↓

Schema v12
```

Migration scripts must be included in the release process.

---

# 24. Configuration Migration

Application configuration may require migration between versions.

Examples:

- Renamed Settings
- New Security Options
- New Workflow Settings
- New Reporting Configuration
- New Document Settings

Configuration migration must preserve existing valid settings where possible.

---

# 25. Document Repository Migration

Application upgrades must not automatically move or rewrite documents unless required.

If repository structure changes:

```text
Verify Source

↓

Copy / Transform

↓

Checksum

↓

Verify Destination

↓

Update References

↓

Audit
```

Original files must remain recoverable throughout the process.

---

# 26. Installer Architecture

The installer may provide:

- Application Installation
- Upgrade
- Repair
- Uninstallation

Where appropriate, it may also create:

- Desktop Shortcut
- Start Menu Entry
- File Associations
- Uninstaller Entry

Installation options should remain simple.

---

# 27. Repair Installation

Repair may verify:

- Application Files
- Required Libraries
- Configuration
- Database Connection
- Document Repository Access

Repair must not overwrite or delete user data without explicit authorization.

---

# 28. Uninstallation

Uninstallation shall distinguish between:

### Application Removal

Removes application files.

### Data Removal

Removes database and documents.

Data removal requires explicit confirmation.

The default uninstaller should preserve user data.

---

# 29. Uninstallation Safety

Before removing persistent data:

```text
Warning

↓

Identify Data

↓

Confirm Backup

↓

Explicit User Confirmation

↓

Delete if Authorized

↓

Audit where possible
```

Accidental removal of the document archive or accounting database must be prevented.

---

# 30. Backup During Deployment

Before significant deployment operations:

- Backup Database
- Verify Backup
- Record Backup Timestamp
- Record Application Version
- Record Database Version

For major upgrades, a full backup is mandatory.

---

# 31. Deployment Recovery

If installation fails:

```text
Detect Failure

↓

Stop

↓

Preserve Existing Data

↓

Restore Previous Application if Required

↓

Verify Database

↓

Verify Documents

↓

Restart Previous Version
```

Deployment must never leave a partially migrated production database without a recovery path.

---

# 32. Environment Diagnostics

MFM should provide an environment diagnostic function.

Diagnostics may include:

- Application Version
- Database Version
- Operating System
- Database Path
- Document Path
- Backup Path
- Storage Availability
- Database Integrity
- Repository Accessibility
- Job Scheduler Status
- Search Index Status

Sensitive configuration values must be masked.

---

# 33. Installation Log

Installation and upgrade processes should produce logs containing:

- Start Time
- Version
- Environment
- Actions
- Warnings
- Errors
- Completion Status

Logs should not contain passwords or secrets.

---

# 34. Deployment Audit

The system should record:

- Installation
- Upgrade
- Database Migration
- Configuration Migration
- Repair
- Uninstallation where technically possible
- Deployment Validation

Deployment records support troubleshooting and governance.

---

# 35. Environment Variables

Environment variables may be used for:

- Development Overrides
- Test Configuration
- Deployment Paths
- External Service Configuration

Production configuration should remain explicit and controlled.

Secrets must not be committed to source control.

---

# 36. Windows Integration

The Windows deployment may support:

- Start Menu
- Desktop Shortcut
- File Associations
- Application Metadata
- Version Information
- Uninstaller

Windows-specific features should not affect the portability of the core business layer unnecessarily.

---

# 37. File Permissions

Application and data directories should have appropriate permissions.

Recommended separation:

```text
Application Files

→ Read / Execute

User Data

→ Controlled Read / Write

Backups

→ Restricted Access
```

The exact Windows ACL strategy depends on the deployment environment.

---

# 38. Shared-Computer Deployment

If several authorized users use the same Windows computer:

- Windows user accounts should remain distinct where practical.
- MFM user authentication remains active.
- Sensitive documents should not be broadly accessible through Windows folders.
- Backup access should be restricted.

MFM authorization remains mandatory even when Windows users share the same machine.

---

# 39. Portable / Test Deployment

A controlled test installation may use a separate data directory:

```text
MFM-Test

↓

Test Database

↓

Test Documents

↓

Test Configuration
```

This allows testing without affecting production data.

Portable deployments must never accidentally point to the production database.

---

# 40. Production Identification

The application should clearly identify production mode.

Possible indicators include:

```text
Environment: PRODUCTION
```

Test installations should clearly indicate:

```text
Environment: TEST
```

This reduces the risk of performing destructive actions against the wrong environment.

---

# 41. Deployment Validation

After installation or upgrade:

```text
Application Starts

✓

Database Opens

✓

User Login

✓

Authorization

✓

Document Access

✓

Accounting Test

✓

Membership Test

✓

Backup Check

✓
```

The validation checklist may be adapted to the release scope.

---

# 42. Smoke Test

A minimal smoke test should verify:

1. Application starts.
2. User can log in.
3. Dashboard opens.
4. Database is accessible.
5. A read operation succeeds.
6. A controlled write operation succeeds.
7. Audit is recorded.
8. Documents can be accessed.
9. Backup configuration is available.

A failed critical smoke test blocks normal production use.

---

# 43. Deployment Package

A release package may contain:

```text
Installer

Release Notes

Migration Notes

Checksum

User Documentation

Administrator Documentation
```

Where necessary:

```text
Database Migration Scripts

Configuration Migration Information
```

---

# 44. Release Artifact Integrity

Each release artifact should have a SHA-256 checksum.

Example:

```text
MFM-1.2.0-Setup.exe

SHA-256:
<checksum>
```

The actual checksum is generated during release packaging.

---

# 45. Version Compatibility

Compatibility must be documented between:

- Application Version
- Database Schema
- Migration Version
- Configuration Version
- Document Repository Version

Unsupported combinations must be rejected clearly.

---

# 46. Rollback

Rollback may involve:

```text
Stop Application

↓

Restore Database Backup

↓

Restore Application Version

↓

Restore Configuration if Required

↓

Verify Documents

↓

Validate

↓

Resume
```

Document rollback is required only if document structure itself was changed.

---

# 47. Post-Deployment Verification

After deployment:

- Review Logs
- Verify Database
- Verify Documents
- Verify Security
- Verify Accounting
- Verify Backup
- Verify Background Jobs
- Verify Integrations where enabled

The deployment is considered complete only after verification.

---

# 48. Deployment Monitoring

For significant upgrades, administrators should monitor:

- Application Errors
- Database Errors
- Failed Jobs
- Integration Errors
- Storage Usage
- User Reports
- Performance

This observation period is especially important after major schema migrations.

---

# 49. Maintenance Mode

Major migrations may use maintenance mode.

Maintenance mode prevents ordinary users from making changes while migration is running.

Example:

```text
Maintenance Mode

↓

Users Cannot Modify Data

↓

Migration

↓

Validation

↓

Maintenance Mode Off
```

For a single-user desktop installation, maintenance mode may simply mean closing the application.

---

# 50. Environment Configuration Review

Before production release, verify:

- Production Database
- Production Document Repository
- Production Backup Location
- Organization
- Security Settings
- Email Settings
- Integration Profiles
- Environment Indicator

Test settings must never remain active in production.

---

# 51. Deployment Security

Deployment security includes:

- Trusted Installation Source
- Verified Release Artifact
- Restricted Installer Access
- Secure Credentials
- Controlled Configuration
- Backup Before Upgrade
- Audit of Administrative Actions

Administrators should verify release checksums where appropriate.

---

# 52. Performance Considerations

Installation and upgrades should minimize:

- Unnecessary File Copies
- Repeated Database Operations
- Full Document Reprocessing
- Unnecessary Index Rebuilds

Long-running operations should provide progress information.

---

# 53. Large Database Deployment

For large databases:

```text
Preflight

↓

Backup

↓

Migration

↓

Validation

↓

Optimization

↓

Application Start
```

The migration process should report progress and estimated stages where practical.

---

# 54. Large Document Repository Deployment

Large document repositories require special consideration.

The upgrade should:

- Avoid unnecessary file movement.
- Verify available storage.
- Process indexes asynchronously where possible.
- Preserve original files.
- Verify repository references.

Document integrity has priority over deployment speed.

---

# 55. Environment Health

The environment health indicator may summarize:

```text
Application      ✓

Database         ✓

Documents        ✓

Backup           ✓

Jobs             ✓

Search           ✓

Integrations     ✓
```

Warnings should be actionable.

---

# 56. Troubleshooting

Common deployment problems include:

### Application Will Not Start

Check:

- Version
- Runtime
- Configuration
- Permissions
- Logs

### Database Migration Failed

Check:

- Backup
- Migration Log
- Schema Version
- Disk Space
- Database Integrity

### Documents Unavailable

Check:

- Repository Path
- Permissions
- Storage Availability
- Document Configuration

### Backup Failed

Check:

- Destination
- Permissions
- Disk Space
- Backup Configuration

---

# 57. Support Bundle

Authorized administrators may create a diagnostic support bundle containing:

- Application Version
- Database Version
- Environment Information
- Sanitized Logs
- Migration Status
- Configuration Summary
- Health Results

The bundle must exclude:

- Passwords
- API Secrets
- Authentication Tokens
- Unnecessary Personal Data

---

# 58. Testing

Deployment testing includes:

- Clean Installation
- First Run
- Upgrade
- Repair
- Uninstallation
- Database Migration
- Configuration Migration
- Document Repository
- Backup / Restore
- Environment Diagnostics
- Production Smoke Test

Each major release should pass installation and upgrade testing before publication.

---

# 59. Future Deployment Models

Future MFM versions may support:

- Central Server Deployment
- PostgreSQL
- Application Server
- Web Client
- API Server
- Containerized Deployment
- Cloud Hosting
- Central Document Storage

The current service architecture should allow these options to evolve without changing the fundamental domain ownership model.

---

# 60. Governance

Deployment shall remain controlled but practical.

The organization should maintain:

- One Production Installation
- Clearly Identified Test Environment where needed
- Regular Backups
- Documented Upgrade Procedure
- Documented Recovery Procedure
- Release Records

Complex deployment infrastructure should only be introduced when justified by actual operational requirements.

---

# 61. Summary

The Deployment, Installation & Environment Management Architecture provides MFM v1.2 with a controlled framework for installing, upgrading, repairing and operating the application safely.

It establishes:

- Installation Standards
- Environment Separation
- Configuration Management
- Database Initialization
- Upgrade Procedures
- Migration Controls
- Deployment Validation
- Recovery
- Diagnostics
- Uninstallation Safety

The central principle is:

> **Application files may be replaced; authoritative user data must be preserved, validated and recoverable.**

The deployment architecture also preserves the core MFM rule:

> **Deployment changes the software environment, not the ownership of business truth.**

Accounting Core remains the sole authoritative financial ledger.

---

# Next Document

**MFM v1.2-450 – Operational Monitoring, Maintenance & Support Architecture**

---

# END OF DOCUMENT
