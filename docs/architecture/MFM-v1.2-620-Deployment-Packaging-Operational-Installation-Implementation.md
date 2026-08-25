# MFM v1.2-620 – Deployment, Packaging & Operational Installation Implementation

Version: 1.2

Document ID: MFM-v1.2-620

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for deployment, packaging and operational installation of MaritimForeningsManager (MFM) v1.2.

It follows:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution
- MFM v1.2-550 – Core Services & Domain Logic Implementation
- MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation
- MFM v1.2-570 – GUI, Presentation Layer & User Workflow Implementation
- MFM v1.2-580 – Reporting, Dashboard & Read-Model Implementation
- MFM v1.2-590 – Notifications, Background Jobs & Asynchronous Processing Implementation
- MFM v1.2-600 – Integration, External Services & Adapter Implementation
- MFM v1.2-610 – Testing, Quality Assurance & Release Validation Implementation

The purpose is to define a controlled and repeatable way to package, install, upgrade, configure, validate and operate MFM on supported Windows environments.

The document establishes:

- Deployment Architecture
- Application Packaging
- Windows Installation
- Directory Structure
- Configuration
- Database Initialization
- Database Migration
- User Setup
- File Storage
- Backup Configuration
- Logging
- Desktop Shortcuts
- Versioning
- Upgrade Procedures
- Rollback
- Uninstallation
- Operational Validation
- Support Procedures
- Release Artifacts
- Security
- Recovery
- Deployment Testing

---

# 2. Scope

This document covers:

- Development Build
- Release Build
- Windows Packaging
- Installation
- Configuration
- First Run
- Upgrade
- Rollback
- Uninstallation
- Operational Directories
- Database Deployment
- Document Storage
- Backup Storage
- Logs
- Temporary Files
- Release Validation

---

# 3. Deployment Principle

The MFM deployment should remain simple and appropriate for a small non-profit association.

The preferred model is:

```text
Windows PC

↓

MFM Application

↓

Local / Controlled Database

↓

Controlled Data Directories
```

Avoid unnecessary infrastructure.

---

# 4. Deployment Architecture

A typical installation consists of:

```text
MFM Application

Application Configuration

Database

Document Storage

Backup Storage

Log Storage

Temporary Storage
```

These components should have clearly defined locations.

---

# 5. Application Installation Directory

The application binaries should be installed in a controlled program directory.

Example:

```text
C:\Program Files\MFM\
```

The exact path may be configurable by the installer.

---

# 6. User Data Directory

User-editable data should not normally be stored inside the application installation directory.

Example:

```text
C:\ProgramData\MFM\
```

or an appropriate organization-controlled data location.

---

# 7. Database Location

The database location should be configurable.

Example:

```text
C:\ProgramData\MFM\Data\mfm.db
```

The final path must follow the existing MFM configuration model.

---

# 8. Document Storage

Documents should have a dedicated storage root.

Example:

```text
C:\ProgramData\MFM\Documents\
```

Document storage must remain separate from application binaries.

---

# 9. Backup Storage

Backups should use a separate directory or storage target.

Example:

```text
C:\ProgramData\MFM\Backups\
```

A production backup strategy should preferably include a location independent of the primary database device where practical.

---

# 10. Log Storage

Logs should have a dedicated location.

Example:

```text
C:\ProgramData\MFM\Logs\
```

---

# 11. Temporary Storage

Temporary files should use:

```text
C:\ProgramData\MFM\Temp\
```

or the Windows temporary directory according to the implementation.

Temporary files must be cleaned up where practical.

---

# 12. Directory Ownership

A clear separation should exist:

```text
Program Files
→ Application

ProgramData
→ Application Data

User Profile
→ User Preferences where appropriate
```

---

# 13. Directory Permissions

The application should use the minimum required permissions.

Users should not require unrestricted administrator access merely to operate MFM.

---

# 14. Administrator Rights

Administrator rights may be required for:

- Installation
- Upgrade
- Uninstallation
- Certain maintenance tasks

Normal accounting and membership work should not require Windows administrator privileges.

---

# 15. Installation Package

A release should provide a controlled installation package.

Possible format:

```text
MFM-Setup-x.y.z.exe
```

The exact packaging technology follows the project implementation.

---

# 16. Package Contents

The installer package should contain:

```text
Application

Required Runtime Dependencies

Configuration Defaults

Database Migration Components

Assets

Version Information
```

Do not include production secrets.

---

# 17. Package Integrity

Release packages should have integrity information.

Where practical:

```text
Checksum

Digital Signature
```

---

# 18. Package Version

The package version must correspond to the application release version.

Example:

```text
MFM 1.2.0
```

---

# 19. Application Version

The application should expose its version in:

- About
- Login / Startup Information where appropriate
- Diagnostics

---

# 20. Database Version

The database schema version must be tracked independently from the application version.

Example:

```text
Application:
1.2.0

Database:
42
```

---

# 21. Compatibility Matrix

Each release should define supported combinations:

```text
Application Version

Database Version

Operating System
```

---

# 22. Windows Support

The supported Windows versions should be explicitly defined in release documentation.

Do not claim support for untested operating system versions.

---

# 23. Installation Workflow

The standard installation sequence is:

```text
Start Installer

↓

Accept License / Terms if applicable

↓

Select Installation Path

↓

Install Application

↓

Create Data Directories

↓

Complete Installation

↓

Launch MFM
```

---

# 24. First Run Workflow

First run should perform controlled initialization:

```text
Start

↓

Load Configuration

↓

Check Data Directory

↓

Check Database

↓

Initialize / Migrate

↓

Create Initial Administrator if required

↓

Open Login / Setup
```

---

# 25. Existing Database Detection

If an existing database is found:

```text
Identify Schema Version

↓

Compare Supported Version

↓

Migrate if Required

↓

Validate
```

Do not blindly overwrite the database.

---

# 26. New Database Detection

For a new installation:

```text
Create Database

↓

Apply Base Schema

↓

Apply Initial Configuration

↓

Create Administrative Setup
```

---

# 27. Initial Administrator

The first installation should provide a controlled way to establish the initial administrator account.

The password must be supplied securely by the administrator.

---

# 28. Initial Password

Do not ship MFM with a universal default administrator password.

---

# 29. First Login

The initial administrator should be required to authenticate before performing normal administration.

---

# 30. Configuration

Configuration should include only operational settings appropriate to the deployment.

Examples:

```text
Database Path

Document Path

Backup Path

Log Level

Email Configuration

Organization Settings
```

---

# 31. Configuration Validation

At startup or configuration save, validate:

```text
Path Exists / Can Be Created

Database Accessible

Storage Writable

Backup Target Accessible

Required Settings Present
```

---

# 32. Configuration Separation

Business data and application configuration should remain conceptually separate.

---

# 33. Secrets

Secrets must not be included in:

- Installer
- Source Repository
- Default Configuration
- Release Notes

---

# 34. Secret Setup

Credentials should be configured during installation or administration using the established secrets mechanism.

---

# 35. Database Initialization

Database initialization must use the existing schema and migration mechanisms.

Do not create a second initialization path in the installer.

---

# 36. Migration Execution

Database migrations should be executed through the MFM migration system.

The installer should invoke the established mechanism rather than duplicate migration logic.

---

# 37. Migration Safety

Before an upgrade migration:

```text
Verified Backup

↓

Migration

↓

Validation
```

---

# 38. Migration Failure

If migration fails:

```text
Stop

↓

Do Not Start Normal Operations

↓

Record Error

↓

Recover / Restore
```

---

# 39. Migration Logging

Migration execution should record:

```text
Previous Version

Target Version

Start

End

Result
```

Technical details should be logged securely.

---

# 40. Database Integrity Check

After installation or upgrade:

```text
Database Open

↓

Schema Validation

↓

Integrity Check

↓

Application Start
```

---

# 41. Document Storage Initialization

The installer or first-run process may create required document directories.

It must not delete existing document content.

---

# 42. Backup Directory Initialization

Backup directories may be created if configured.

Existing backups must not be overwritten automatically.

---

# 43. Log Directory Initialization

The application should create its log directory if necessary.

Failure to create logs should not hide more important startup errors.

---

# 44. File Permissions

Storage directories should permit the application to perform required operations without granting unnecessary system-wide permissions.

---

# 45. Windows User Context

The application should run under the normal Windows user account where practical.

---

# 46. Per-User vs Shared Installation

MFM may use:

```text
Per-Machine Installation

```

with shared application data, or another model defined by deployment requirements.

For a small association, one controlled workstation is a reasonable baseline.

---

# 47. Multi-User Consideration

If multiple Windows users operate the same database:

- File Permissions
- Concurrent Access
- Backup
- User Authentication

must be explicitly validated.

---

# 48. Network Database Consideration

A local SQLite database should not be placed on an unreliable network share without explicit validation.

For the current MFM scale, local controlled storage is preferred.

---

# 49. Desktop Shortcut

The installer may create:

```text
Desktop Shortcut

Start Menu Entry
```

---

# 50. Shortcut Target

The shortcut should launch the installed application executable or controlled launcher.

Do not point directly to development scripts.

---

# 51. Start Menu

The installer should provide an identifiable MFM entry.

Possible:

```text
MaritimForeningsManager
```

---

# 52. Uninstaller

The installation should provide a standard uninstallation mechanism.

---

# 53. Uninstallation Principle

Uninstalling the application must not automatically destroy user business data without explicit confirmation.

---

# 54. Uninstall Options

Where practical:

```text
Remove Application Only

Keep Data

Remove Application and Data
```

The destructive option requires explicit confirmation.

---

# 55. Backup Before Uninstall

Before deleting business data, recommend or require a verified backup.

---

# 56. Upgrade Principle

Upgrades should preserve:

```text
Database

Documents

Backups

Configuration where compatible
```

---

# 57. Upgrade Workflow

```text
Close MFM

↓

Create Verified Backup

↓

Install New Version

↓

Migrate Database

↓

Validate

↓

Start MFM

↓

Smoke Test
```

---

# 58. Running Application Detection

The installer should detect whether MFM is currently running where possible.

The user should be instructed to close it before upgrade.

---

# 59. Upgrade Lock

The installer should not overwrite files currently in use.

---

# 60. Configuration Migration

When configuration changes between versions:

```text
Read Existing

↓

Migrate / Map

↓

Validate

↓

Save
```

---

# 61. Configuration Compatibility

Unknown configuration values should not silently change business behavior.

---

# 62. Upgrade Backup

The pre-upgrade backup should include all data required to recover the deployment.

Depending on scope:

```text
Database

Documents

Configuration

```

---

# 63. Rollback Principle

Rollback should be planned before a high-risk upgrade.

---

# 64. Application Rollback

Application files may be restored to the previous version.

---

# 65. Database Rollback

If a migration cannot be safely reversed:

```text
Restore Pre-Upgrade Database Backup
```

---

# 66. Document Rollback

Document storage should not be modified destructively by normal application upgrades.

---

# 67. Configuration Rollback

Where configuration is migrated, retain a recoverable previous configuration where practical.

---

# 68. Failed Upgrade State

If an upgrade fails:

```text
Do Not Continue Normal Operation

↓

Display Recovery Guidance

↓

Preserve Logs

↓

Assess Database State
```

---

# 69. Recovery Workflow

```text
Stop Application

↓

Secure Current State

↓

Restore Backup if Required

↓

Restore Compatible Application

↓

Validate

↓

Resume
```

---

# 70. Operational Installation Checklist

Before handing over a system:

```text
Application Installed

Database Initialized

Administrator Created

Storage Configured

Backup Configured

Logs Working

Login Tested

Core Modules Tested
```

---

# 71. First-Run Validation

Test:

```text
Login

Dashboard

Members

Accounting

Projects

Grants

Documents

Reports
```

according to the release scope.

---

# 72. Accounting Validation

At minimum:

```text
Open Accounting

Open Chart of Accounts

Create Test / Controlled Voucher if appropriate

Verify Ledger

Verify Report
```

Production validation should avoid creating unwanted accounting entries.

---

# 73. Backup Validation

Verify:

```text
Backup Path

Backup Creation

Backup Verification
```

---

# 74. Restore Validation

Perform restore testing in a controlled test environment.

Do not use destructive restore operations on production merely to perform routine installation validation.

---

# 75. Logging Validation

Confirm:

```text
Application Starts

↓

Log Created

↓

Expected Events Recorded
```

---

# 76. Error Reporting Validation

Cause a safe controlled error and verify that:

```text
User Gets Safe Message

Technical Log Contains Diagnostic Detail
```

---

# 77. Installation Test Matrix

Test:

```text
Fresh Install

Upgrade

Reinstall

Uninstall

Recovery
```

---

# 78. Fresh Installation Test

Verify:

```text
No Existing Data

↓

Install

↓

Initialize

↓

Login

↓

Operate
```

---

# 79. Upgrade Installation Test

Verify:

```text
Existing Test Data

↓

Backup

↓

Upgrade

↓

Migration

↓

Validation

↓

Data Preserved
```

---

# 80. Reinstallation Test

Verify that reinstalling the application does not unintentionally destroy business data.

---

# 81. Uninstallation Test

Verify:

```text
Application Removed

Business Data Preserved when selected
```

---

# 82. Recovery Installation Test

Verify that a backup can be restored into a clean environment and the application can operate.

---

# 83. Packaging Test

Verify the release package contains:

```text
Application

Dependencies

Installer

Version Information

Required Assets
```

---

# 84. Package Exclusion Test

Verify that the release package does not contain:

```text
Production Database

Production Documents

Secrets

Developer Credentials

Debug Artifacts
```

---

# 85. Installer Security

The installer should be obtained from a trusted release source.

Where available, use digital signatures.

---

# 86. Installer Privileges

Request Windows elevation only when necessary.

---

# 87. Installation Logging

The installer should provide useful logs for installation failures.

---

# 88. Installation Failure

If installation fails:

```text
Do Not Leave an Unusable Partial Installation

↓

Rollback Installer Changes where possible

↓

Provide Error
```

---

# 89. Application Startup Failure

If the installed application cannot start:

```text
Show Clear Message

↓

Log Diagnostic Detail

↓

Provide Recovery Guidance
```

---

# 90. Configuration Backup

Configuration that is necessary for recovery should be included in the operational backup strategy where appropriate.

Secrets should be backed up only through a secure mechanism.

---

# 91. Data Directory Migration

If a future release changes the data directory:

```text
Detect Old Location

↓

Validate

↓

Move / Reference

↓

Verify

↓

Update Configuration
```

Never silently lose data.

---

# 92. Storage Migration

Large document storage migrations should be performed as controlled maintenance jobs where necessary.

---

# 93. Storage Migration Validation

Verify:

```text
File Count

References

Checksums where used

Read Access
```

---

# 94. Backup Migration

If backup locations change:

```text
Preserve Existing Backups

↓

Configure New Location

↓

Test New Backup

↓

Verify
```

---

# 95. Log Rotation

Logs should have a controlled retention or rotation strategy.

Avoid unlimited growth.

---

# 96. Disk Space

Operational monitoring should consider:

```text
Database Size

Document Storage

Backup Storage

Log Storage
```

---

# 97. Low Disk Space

If disk space becomes critically low:

```text
Notify Administrator

↓

Prevent Unsafe Operations where necessary

↓

Free / Extend Storage
```

Do not silently continue until writes fail unpredictably.

---

# 98. Application Update Notification

Where implemented, MFM may notify administrators of available approved updates.

Do not automatically install updates without a controlled policy.

---

# 99. Update Verification

An update should be verified before installation.

Possible:

```text
Version

Checksum

Signature
```

---

# 100. Offline Deployment

MFM should support installation from a local installer package without requiring permanent Internet connectivity, where the implementation permits.

---

# 101. Dependency Availability

If the installer requires external dependencies, the release package or documented prerequisite process must make this explicit.

---

# 102. Release Artifact Set

A release should contain:

```text
Installer

Release Notes

Version Information

Migration Notes

Backup / Recovery Notes
```

---

# 103. Operational Documentation

The release should include concise operational instructions for:

```text
Start

Login

Backup

Restore

Upgrade

Support
```

---

# 104. Administrator Handover

The administrator should receive:

```text
Installed Version

Database Location

Document Location

Backup Location

Administrative Account

Recovery Procedure
```

Sensitive credentials should be transferred securely, not written into ordinary documentation.

---

# 105. Support Information

The application should expose enough information for support:

```text
Application Version

Database Version

Installation Location

Data Location
```

Do not expose secrets.

---

# 106. Diagnostic Package

Where practical, administrators may generate a diagnostic package containing:

```text
Version

Schema Version

Configuration Summary

Recent Logs

Job Status
```

Sensitive information must be filtered.

---

# 107. Diagnostic Security

Diagnostic exports must not contain:

```text
Passwords

Tokens

Secrets

Unnecessary Personal Data
```

---

# 108. Operational Health Check

A simple health check may verify:

```text
Application

Database

Storage

Backup Configuration

Background Worker
```

---

# 109. Installation and Accounting Authority

Deployment procedures must never create a second accounting database merely because installation or testing requires it.

Production accounting remains in the authoritative Accounting Core database.

---

# 110. Production Data Separation

Test and development installations must use separate:

```text
Database

Documents

Backups

Configuration
```

from production.

---

# 111. Environment Identification

Where multiple environments exist, clearly identify:

```text
Development

Test

Production
```

---

# 112. Production Warning

Administrative or maintenance screens should clearly identify production where confusion could cause destructive action.

---

# 113. Release Environment Validation

Before production installation verify:

```text
Correct Package

Correct Version

Correct Environment

Verified Backup

Required Configuration
```

---

# 114. Operational Maintenance

Routine maintenance may include:

```text
Backup Verification

Log Cleanup

Temporary File Cleanup

Database Integrity Check

Job Cleanup
```

---

# 115. Maintenance Scheduling

Maintenance should be scheduled to minimize disruption.

---

# 116. Maintenance Failure

A maintenance failure should be recorded and communicated to administrators.

---

# 117. Installation Security Review

Before release verify:

```text
Installer Permissions

File Permissions

Secrets

Database Location

Backup Security

Log Security
```

---

# 118. Deployment Definition of Ready

A release is Ready for deployment when:

- Package Built
- Tests Passed
- Migration Tested
- Backup Strategy Verified
- Installation Tested
- Upgrade Tested
- Recovery Tested
- Release Documentation Complete

---

# 119. Deployment Definition of Done

Deployment is Done when:

- Installed
- Migrated
- Configured
- Validated
- Smoke Tested
- Backup Verified
- Administrator Handover Complete

---

# 120. Installation Release Gate

Before release:

```text
Fresh Install

Upgrade

Reinstall

Uninstall

Recovery

Security

Configuration

Data Preservation
```

must be validated.

---

# 121. Production Release Gate

Production deployment additionally requires:

```text
Verified Production Backup

Correct Environment

Approved Release

Migration Readiness

Recovery Plan

Administrator Availability
```

---

# 122. Rollback Gate

Before upgrade, verify:

```text
Backup Exists

Backup Is Readable

Rollback Version Available

Recovery Procedure Known
```

---

# 123. Final Deployment Principle

> **Deployment must preserve the application's data, configuration and authoritative business state while making installation and upgrades repeatable.**

---

# 124. Final Operational Principle

> **Normal users should be able to operate MFM without Windows administrator privileges or technical knowledge of the underlying implementation.**

---

# 125. Final Financial Deployment Principle

> **Deployment, migration, backup and restore procedures must preserve Accounting Core as the sole authoritative financial ledger.**

---

# 126. Summary

MFM v1.2-620 establishes the Deployment, Packaging and Operational Installation implementation baseline.

It defines:

- Deployment Architecture
- Windows Packaging
- Installation
- First Run
- Database Initialization
- Migration
- Configuration
- File Storage
- Backup
- Logging
- Desktop Integration
- Upgrades
- Rollback
- Uninstallation
- Recovery
- Operational Validation
- Release Artifacts
- Security
- Support
- Environment Separation

The central rule remains:

> **Deployment is an operational mechanism; it must not introduce a parallel source of business truth.**

And:

> **Accounting Core remains the sole authoritative financial ledger.**

---

# 127. Next Document

**MFM v1.2-630 – Operations, Monitoring & Support Implementation**

---

# END OF DOCUMENT
