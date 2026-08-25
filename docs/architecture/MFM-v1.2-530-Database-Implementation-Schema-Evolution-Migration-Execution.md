# MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution

Version: 1.2

Document ID: MFM-v1.2-530

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the practical database implementation, schema evolution and migration execution model for MaritimForeningsManager (MFM) v1.2.

It follows:

**MFM v1.2-500 – Architecture Consolidation & Implementation Readiness**

**MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability**

**MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow**

The purpose is to establish a controlled method for changing the MFM database without compromising:

- Data Integrity
- Accounting Integrity
- Referential Integrity
- Existing Data
- Security
- Recoverability
- Upgradeability
- Traceability

The document defines:

- Database Implementation Principles
- Schema Ownership
- Migration Architecture
- Versioning
- Migration Execution
- Validation
- Rollback / Recovery
- Data Transformation
- Indexing
- Constraints
- Testing
- Production Migration
- Emergency Changes
- Migration Evidence

---

# 2. Scope

This document covers:

- SQLite database implementation
- Schema changes
- New tables
- New columns
- Constraints
- Indexes
- Reference data
- Data migrations
- Schema versioning
- Upgrade procedures
- Migration testing
- Recovery
- Production deployment

It applies to both existing MFM v1.0 data and future v1.2 extensions.

---

# 3. Database Architectural Position

The MFM database is the persistence layer for the application.

The authoritative business rules remain in application/domain services.

The architecture is:

```text
GUI

↓

Application Services

↓

Domain Services

↓

Repositories

↓

Database
```

Direct GUI access to business tables is prohibited.

---

# 4. Database Technology

The current MFM architecture uses:

```text
SQLite
```

SQLite remains appropriate for the current small non-profit organizational scale.

A future migration to a server database remains possible if actual requirements justify it.

---

# 5. Database Ownership

Each business table must have a clear owning domain.

Examples:

```text
Accounting

→ Accounting Core

Membership

→ Membership Module

Projects

→ Project Module

Grants

→ Grants Module

Documents

→ Document Module

Security

→ Security Module
```

Cross-cutting tables may be owned by:

- Audit
- Configuration
- Workflow
- Notifications
- System Operations

---

# 6. Authoritative Financial Rule

The following rule is mandatory:

> **Accounting Core is the sole authoritative financial ledger.**

Database implementation must preserve this rule.

No new table may become an alternative source of authoritative accounting transactions.

---

# 7. Financial References

Other domains may contain:

- Budget References
- Grant Amounts
- Forecast Values
- Project Financial Plans
- Reporting Values

These values must have clearly defined semantics.

Where a value represents an actual posted financial transaction, Accounting Core is authoritative.

---

# 8. Schema Versioning

The database must have a clear schema version.

Example:

```text
schema_version = 12
```

The version identifies the structural state of the database.

It is distinct from:

```text
Application Version
```

and:

```text
Document Version
```

---

# 9. Migration History

MFM should maintain a migration history.

A conceptual table is:

```text
schema_migrations

id

migration_id

from_version

to_version

applied_at

execution_status

checksum

duration_ms
```

The exact physical schema may follow the implementation baseline.

---

# 10. Migration Identity

Every migration must have a unique identifier.

Example:

```text
MIG-0012-add-document-retention
```

The identifier should remain stable.

It must not be reused for another migration.

---

# 11. Migration Ordering

Migrations must execute in deterministic order.

Example:

```text
MIG-0010

↓

MIG-0011

↓

MIG-0012

↓

MIG-0013
```

A database must not skip a required migration.

---

# 12. Migration Immutability

An applied migration must not be silently edited.

If a migration contains an error:

```text
Create Corrective Migration
```

rather than modifying historical migration content.

This preserves migration history.

---

# 13. Migration Checksum

Where practical, migrations should have a checksum.

The checksum helps detect:

- Modified Migration Files
- Corrupted Files
- Unexpected Source Changes

An already-applied migration with a changed checksum should trigger a warning or migration failure.

---

# 14. Migration Transaction

Where SQLite permits safe transactional execution, schema changes and data changes should be performed within transactions.

The objective is:

```text
Migration Starts

↓

All Required Changes

↓

Validation

↓

Commit
```

or:

```text
Migration Fails

↓

Rollback
```

Not every SQLite schema operation has identical transactional behavior, so migration code must account for the actual SQLite operation being performed.

---

# 15. Migration Preconditions

Before migration, verify:

- Database Exists
- Database Is Accessible
- Expected Version
- Database Integrity
- Sufficient Storage
- Application Version Compatibility
- Backup Availability

If required preconditions fail, migration must stop.

---

# 16. Backup Before Migration

Production schema migrations should normally be preceded by a verified backup.

Recommended:

```text
Verify Backup

↓

Start Migration

↓

Validate

↓

Complete
```

A migration that materially changes data must not begin without an appropriate recovery path.

---

# 17. Migration Lock

Only one migration process may modify the schema at a time.

The application should prevent concurrent migration attempts.

Example:

```text
Migration Running

↓

Second Startup

↓

Migration Locked

↓

Wait / Exit Safely
```

---

# 18. Application Startup

Startup may follow:

```text
Open Database

↓

Read Schema Version

↓

Compare Application Requirement

↓

Run Required Migrations

↓

Validate

↓

Start Application
```

If migration cannot complete safely, the application should not continue into an incompatible state.

---

# 19. Version Compatibility

The application should know:

- Minimum Supported Schema
- Current Supported Schema
- Required Schema

Example:

```text
Application Requires:
Schema 14

Database:
Schema 12

Action:
Migrate 12 → 13 → 14
```

---

# 20. Downgrade Policy

Automatic database downgrade is not recommended.

If an older application encounters a newer database:

```text
Database Too New

↓

Do Not Modify

↓

Inform Administrator
```

Recovery should use backup or a supported migration strategy.

---

# 21. Schema Change Categories

Database changes may include:

- New Table
- New Column
- Column Modification
- New Constraint
- New Index
- Reference Data
- Data Transformation
- Data Cleanup
- Archive Structure

Each category requires appropriate testing.

---

# 22. New Table

A new table should define:

- Purpose
- Owner
- Primary Key
- Foreign Keys
- Required Fields
- Constraints
- Indexes
- Retention
- Audit Requirements

---

# 23. Primary Keys

Every business table should have a stable primary key.

The key should be:

- Unique
- Non-Ambiguous
- Stable
- Suitable for References

The implementation should follow the established MFM database conventions.

---

# 24. Foreign Keys

Foreign keys should be used where referential integrity requires them.

Examples:

```text
Project

→ Organization
```

```text
Grant

→ Project
```

```text
Document

→ Related Entity
```

The exact relationships follow the domain model.

---

# 25. Referential Integrity

The database should enforce referential integrity where practical.

The application must also validate business rules.

Database constraints and service rules complement each other.

---

# 26. Deletion Policy

Deletion should be carefully controlled.

Where historical or business records must remain:

```text
Active

↓

Archived

↓

Retained
```

may be preferable to physical deletion.

---

# 27. Accounting Deletion

Posted accounting transactions must not be physically deleted as an ordinary correction mechanism.

Corrections should use the established Accounting Core reversal / adjustment model.

---

# 28. Unique Constraints

Unique constraints should protect values that must be unique.

Examples:

- Membership Number
- Account Number where required
- Migration ID
- Certain Reference Numbers

Uniqueness should be enforced at database level where appropriate.

---

# 29. Nullability

Columns should be nullable only when absence is a valid state.

Avoid using NULL merely because a requirement was not decided.

---

# 30. Default Values

Defaults may be used for:

- Status
- Boolean Flags
- Created Timestamp
- Version
- Configuration Values

Defaults must represent valid business semantics.

---

# 31. Status Values

Status values should be controlled.

Avoid arbitrary free-text statuses such as:

```text
active
Active
ACTIVE
currently active
```

Use a controlled domain representation.

---

# 32. Date and Time Storage

Database storage should use a consistent internal representation.

The application is responsible for locale-specific display.

Example display:

```text
17 August 2026
```

The stored value remains standardized.

---

# 33. Currency Storage

Financial amounts must use a representation that avoids inappropriate floating-point behavior.

For Accounting Core, exact monetary handling is mandatory.

The database design must preserve exact financial values.

---

# 34. Accounting Database Model

The accounting schema should support at minimum:

```text
Accounts

Vouchers

Voucher Lines

Periods

Transactions / Ledger Entries

Reversals where applicable

Audit References
```

The exact structure follows the existing Accounting Core implementation.

---

# 35. Accounting Database Rule

Database changes affecting Accounting Core require additional review.

Before release:

- Existing Balances Must Remain Correct
- Historical Transactions Must Remain Accessible
- Posting Must Remain Atomic
- Reversal Must Remain Valid
- Reports Must Remain Consistent

---

# 36. Membership Database

Membership schema may contain:

```text
Members

Membership Status

Membership Categories

Membership History

Contact Information
```

Historical membership changes should not accidentally overwrite required history.

---

# 37. Project Database

Project schema may contain:

```text
Projects

Budgets

Milestones

Tasks

Project References
```

Project budgets do not replace Accounting Core transactions.

---

# 38. Grant Database

Grant schema may contain:

```text
Grant Opportunities

Applications

Awards

Deadlines

Reporting Requirements
```

Actual accounting transactions remain in Accounting Core.

---

# 39. Document Database

Document metadata may contain:

```text
Document ID

File Reference

Checksum

Version

Category

Owner

Related Entity

Retention Class

Archive State
```

The database does not necessarily store the full binary document.

---

# 40. Security Database

Security schema may contain:

```text
Users

Roles

Permissions

Sessions

Authentication Metadata

Security Audit
```

Passwords must not be stored in plaintext.

---

# 41. Audit Database

Audit records should identify:

- User
- Action
- Entity
- Timestamp
- Result
- Correlation ID
- Relevant Context

Audit records should be protected from ordinary modification.

---

# 42. Configuration Database

Configuration data may include:

- Organization Settings
- System Preferences
- Feature Settings
- Retention Rules
- Notification Rules

Secrets should use protected storage rather than ordinary configuration tables where possible.

---

# 43. Indexing

Indexes should be created for common access patterns.

Examples:

```text
Member Number

Member Name

Project Status

Grant Deadline

Document Reference

Audit Timestamp
```

Indexes should be justified by actual queries.

---

# 44. Index Cost

Indexes improve reads but increase:

- Storage
- Write Cost
- Migration Complexity

Avoid creating indexes for every column.

---

# 45. Query Performance

Database implementation should monitor:

- Slow Queries
- Full Table Scans
- Excessive Joins
- Repeated Queries
- Large Result Sets

Optimization should be evidence-based.

---

# 46. Pagination

Large lists should not load unlimited records.

Use controlled retrieval such as:

```text
Page

Limit

Offset / Cursor where appropriate
```

This improves responsiveness.

---

# 47. Search

Search should use appropriate indexes.

For simple MFM datasets, normal indexed queries may be sufficient.

Full-text search should only be introduced when the actual data volume or user requirement justifies it.

---

# 48. SQLite Foreign Keys

SQLite foreign-key enforcement should be explicitly enabled where required by the application.

The application should not assume that declared foreign keys are automatically enforced in every connection.

---

# 49. Connection Management

Database connections should be:

- Created Safely
- Closed Correctly
- Isolated where appropriate
- Configured Consistently

Transactions must not accidentally remain open.

---

# 50. Connection Error Handling

If the database connection fails:

```text
Detect

↓

Log Technical Detail

↓

Show User-Friendly Error

↓

Protect Existing Data
```

The application must not silently continue with an invalid connection.

---

# 51. Database Integrity Check

MFM should support a database integrity check.

For SQLite this may include appropriate integrity verification.

A failed integrity check should be treated as an operational incident.

---

# 52. Database Repair

Automatic repair must be conservative.

The system should not attempt destructive repair without:

- Backup
- Administrator Authorization
- Clear Recovery Procedure

---

# 53. Schema Inspection

Administration diagnostics may display:

- Database Version
- Application Version
- Table Count
- Migration Version
- Database Size
- Integrity Status

Sensitive information should be excluded.

---

# 54. Data Migration Types

MFM distinguishes:

### Structural Migration

Changes schema structure.

### Data Migration

Transforms existing records.

### Reference Data Migration

Adds or changes controlled reference data.

### Corrective Migration

Repairs a known data problem under controlled conditions.

---

# 55. Structural Migration

Example:

```text
Add retention_class column
```

This is structural.

The migration must define:

- Column Type
- Default / Nullability
- Index Requirement
- Existing Record Handling

---

# 56. Data Migration

Example:

```text
Old Status

"Current"

↓

New Status

"Active"
```

The migration must explicitly transform existing data.

---

# 57. Reference Data Migration

Reference data may include:

- Account Categories
- Membership Categories
- Status Codes
- System Defaults

Reference data must not overwrite organization-specific values unexpectedly.

---

# 58. Corrective Migration

A corrective migration may be required when production data contains an identified defect.

It must include:

- Problem Description
- Selection Criteria
- Transformation
- Validation
- Audit
- Recovery

---

# 59. Migration Validation

After migration verify:

- Schema Version
- Table Structure
- Row Counts where relevant
- Foreign Keys
- Indexes
- Critical Business Data
- Accounting Balances
- Document References

---

# 60. Accounting Migration Validation

Any accounting migration must additionally validate:

```text
Opening Balance

+

Transactions

=

Expected Closing Balance
```

The exact validation method follows the Accounting Core architecture.

---

# 61. Membership Migration Validation

Validate:

- Member Count
- Unique Membership Numbers
- Active Status
- Historical Records
- Contact Data

---

# 62. Project Migration Validation

Validate:

- Project Count
- Status
- Dates
- Budget References
- Tasks
- Relationships

---

# 63. Grant Migration Validation

Validate:

- Grant Count
- Applications
- Deadlines
- Awards
- Project Relationships

---

# 64. Document Migration Validation

Validate:

- Document Count
- File References
- Checksums where applicable
- Metadata
- Version
- Retention
- Archive Status

---

# 65. Security Migration Validation

Validate:

- User Count
- Roles
- Permissions
- Authentication Metadata
- Administrative Access

Never migrate passwords as plaintext.

---

# 66. Migration Logging

Migration execution should record:

- Migration ID
- Start Time
- End Time
- Result
- Duration
- Error if applicable
- Database Version Before
- Database Version After

---

# 67. Migration Output

A successful migration should report:

```text
Migration Completed

From:
12

To:
13

Duration:
2.4 seconds

Result:
SUCCESS
```

---

# 68. Migration Failure Output

A failure should report:

```text
Migration Failed

Migration:
MIG-0013

Database:
Protected

Action:
Recovery Required
```

Technical details belong in logs.

---

# 69. Migration Dry Run

Where practical, migration logic should support validation in a test database before production execution.

Example:

```text
Production Backup

↓

Restore to Test

↓

Run Migration

↓

Validate

↓

Approve Production
```

---

# 70. Production Migration Procedure

Recommended:

```text
1. Notify Users

2. Stop Application Access

3. Verify Backup

4. Verify Database Version

5. Execute Migration

6. Validate Schema

7. Validate Critical Data

8. Start Application

9. Execute Smoke Test

10. Monitor
```

---

# 71. Maintenance Window

Migration should be performed during an appropriate maintenance window when:

- Data transformation is substantial
- Application downtime is required
- Recovery could take time

Small safe migrations may require only brief interruption.

---

# 72. Migration Duration

Migration performance should be measured.

If migration becomes slow:

- Investigate Query Plan
- Batch Data Changes
- Use Appropriate Indexes
- Avoid Unnecessary Full-Table Operations

---

# 73. Large Data Transformation

For larger transformations:

```text
Identify Records

↓

Process in Batches

↓

Validate Each Batch

↓

Commit Safely

↓

Continue
```

The exact approach depends on transactional requirements.

---

# 74. Partial Failure

If a data migration can partially fail, the implementation must define recovery.

Options include:

- Full Transaction Rollback
- Batch Rollback
- Checkpoint / Resume
- Restore from Backup

The safest practical method should be selected.

---

# 75. Migration Idempotency

Where possible, migrations should safely detect whether a transformation has already occurred.

Example:

```text
Column Exists?

Yes → Skip Structural Creation

No → Create
```

However, blindly skipping a migration is not acceptable when data transformation still requires validation.

---

# 76. Migration Preconditions

Examples:

```text
Expected Schema Version

Expected Table Exists

Expected Column Exists / Does Not Exist

Required Data Condition

Backup Verified
```

Failure of a precondition should stop the migration.

---

# 77. Post-Migration Validation

Post-migration validation should include:

```text
Schema

↓

Constraints

↓

Indexes

↓

Data

↓

Accounting

↓

Security

↓

Documents

↓

Application Startup
```

---

# 78. Migration Testing Matrix

| Test | Purpose |
|---|---|
| Clean Database | Verify new schema |
| Previous Version | Verify upgrade |
| Multiple Versions Behind | Verify sequential migrations |
| Existing Data | Verify preservation |
| Invalid State | Verify safe failure |
| Interrupted Migration | Verify recovery |
| Large Dataset | Verify performance |
| Accounting Data | Verify financial integrity |
| Documents | Verify references |
| Security | Verify access |

---

# 79. Migration Test Database

Migration tests should use copies or fixtures.

Production data must not be used as a casual test environment.

---

# 80. Backup Verification

A backup used for migration recovery should be verified.

Verification may include:

- File Exists
- File Readable
- Database Opens
- Integrity Check
- Expected Version

A backup that cannot be restored is not a reliable recovery asset.

---

# 81. Recovery Procedure

If migration fails:

```text
Stop Application

↓

Protect Failed Database

↓

Record Migration Error

↓

Assess State

↓

Restore Backup if Required

↓

Validate Restored Database

↓

Correct Migration

↓

Test Again
```

Do not repeatedly run an unknown failed migration against production.

---

# 82. Failed Migration Preservation

The failed database should be preserved where useful for investigation.

Do not overwrite the only evidence of the failure before diagnosis.

---

# 83. Emergency Migration

Emergency migrations may be required to address:

- Data Integrity
- Security
- Critical Production Defect

They require:

- Administrator Approval
- Backup
- Controlled Execution
- Validation
- Documentation

---

# 84. Direct Production SQL

Direct production SQL should be avoided.

If emergency direct SQL is unavoidable:

- Backup First
- Review SQL
- Record Operator
- Record Time
- Record Reason
- Validate Result
- Document Follow-Up Migration

---

# 85. Schema Documentation

The database documentation should identify:

- Tables
- Columns
- Relationships
- Constraints
- Indexes
- Ownership
- Retention
- Audit

The documentation should be updated when schema meaning changes.

---

# 86. Schema Naming

Database names should be:

- Consistent
- Descriptive
- Stable

Avoid ambiguous names such as:

```text
data
info
misc
temp
```

for permanent business structures.

---

# 87. Temporary Tables

Temporary tables may be used for controlled processing.

They should:

- Have Clear Purpose
- Have Predictable Lifecycle
- Not Become Hidden Permanent Storage
- Be Cleaned Up Safely

---

# 88. Derived Data

Derived data may include:

- Search Index
- Dashboard Cache
- Report Cache
- OCR Text
- Notification Status

Derived data must be reconstructible where practical.

It must not replace authoritative business data.

---

# 89. Cache Recovery

If a cache is lost:

```text
Authoritative Data

↓

Rebuild Cache
```

The system should not treat cache loss as business-data loss.

---

# 90. Database and Document Store

MFM may use:

```text
SQLite

+

Document Repository
```

The database stores document metadata and references.

The document repository stores file content.

The two systems must maintain consistent references.

---

# 91. Document Consistency

If a document file is missing:

```text
Metadata Exists

File Missing
```

the system should identify the inconsistency.

It must not silently create a fake document.

---

# 92. Referential Cleanup

When a record is archived, linked documents should be handled according to document lifecycle rules.

Do not automatically delete documents merely because the parent record is archived unless policy explicitly requires it.

---

# 93. Database Security

Database files should be protected through:

- Operating System Permissions
- Controlled Application Access
- Secure Backup
- Restricted Administrative Access

Additional encryption may be considered where required by the organization's risk profile.

---

# 94. SQLite File Protection

The production database file should not be exposed as an ordinary shared writable file to unauthorized users.

Concurrent access should occur through controlled application use.

---

# 95. Database Backup and WAL

If SQLite journaling modes such as WAL are used, backup procedures must account for associated database files and safe backup semantics.

The backup implementation must produce a consistent recoverable database.

---

# 96. Database Size

Administrators should be able to monitor database size.

Unexpected growth may indicate:

- Logs
- Audit
- Cache
- Failed Jobs
- Documents
- Data Retention Issues

---

# 97. Maintenance

Routine database maintenance may include:

- Integrity Check
- Backup
- Index Review
- Size Review
- Migration Review
- Cleanup of Approved Temporary Data

Maintenance must not alter authoritative data unexpectedly.

---

# 98. Vacuum / Optimization

SQLite maintenance operations such as vacuuming should be treated as maintenance tasks.

Before execution:

- Backup
- Confirm Sufficient Storage
- Consider Application Downtime
- Verify Result

---

# 99. Database Monitoring

Operational monitoring may track:

```text
Database Version

Database Size

Integrity Status

Migration Status

Backup Status

Last Successful Check
```

---

# 100. Performance Monitoring

Useful database metrics include:

- Query Duration
- Migration Duration
- Database Size
- Large Query Frequency
- Failed Queries

The initial implementation should remain simple.

---

# 101. Data Integrity Rules

The database implementation must protect:

- Referential Integrity
- Uniqueness
- Required Values
- Transaction Atomicity
- Accounting Integrity
- Document References
- Security Relationships

---

# 102. Data Integrity Incident

If integrity is suspected:

```text
Stop Risky Operations

↓

Preserve Database

↓

Backup / Copy

↓

Run Diagnostics

↓

Assess

↓

Recover / Correct

↓

Validate
```

Do not continue normal destructive operations while integrity is uncertain.

---

# 103. Migration Governance

Migration files should be reviewed according to risk.

High-risk migrations include:

- Accounting Changes
- Data Deletion
- Large Transformations
- Security Changes
- Relationship Changes

---

# 104. Migration Review Checklist

Before approval:

```text
Purpose                  ✓

Owner                    ✓

Version                  ✓

Preconditions            ✓

Schema Changes           ✓

Data Changes             ✓

Constraints              ✓

Indexes                  ✓

Backup Requirement       ✓

Validation               ✓

Recovery                 ✓

Tests                    ✓
```

---

# 105. Migration Definition of Ready

A migration is Ready when:

- Purpose Is Clear
- Target Schema Is Defined
- Source State Is Known
- Data Transformation Is Defined
- Validation Is Defined
- Recovery Is Defined
- Tests Exist

---

# 106. Migration Definition of Done

A migration is Done when:

- Code Exists
- Test Passes
- Schema Version Updates
- Existing Data Is Validated
- Recovery Has Been Considered
- Documentation Is Updated

---

# 107. Production Migration Definition of Done

A production migration is complete when:

- Backup Verified
- Migration Completed
- Schema Validated
- Critical Data Validated
- Application Starts
- Smoke Test Passes
- Migration Result Recorded

---

# 108. Traceability

Each migration should trace:

```text
Requirement

↓

Architecture

↓

Backlog Task

↓

Migration

↓

Test

↓

Release
```

Example:

```text
REQ-DOC-014

↓

MFM v1.2-470

↓

TASK-510-09-02

↓

MIG-0014

↓

Lifecycle Migration Test

↓

Release 1.2.x
```

---

# 109. Migration Release Notes

Release notes should identify:

- Migration IDs
- Schema Version
- Data Transformations
- Expected Downtime
- Backup Requirement
- Validation

---

# 110. User Communication

If migration requires downtime, users should receive:

- Maintenance Time
- Expected Duration
- Expected Impact
- Completion Notice

---

# 111. Administrator Communication

Administrators should receive migration-specific instructions where required.

These may include:

- Backup Location
- Migration Command
- Expected Version
- Validation Procedure
- Recovery Procedure

---

# 112. Migration Automation

Migration should ultimately be automated through the application or controlled deployment process.

Manual SQL execution should not be the normal upgrade mechanism.

---

# 113. Migration Tooling

The implementation may use a simple internal migration runner.

A complex third-party migration framework is not required unless project scale justifies it.

---

# 114. Migration Runner Responsibilities

The migration runner should:

1. Open Database
2. Validate Version
3. Acquire Migration Lock
4. Verify Preconditions
5. Execute Migration
6. Validate
7. Record Migration
8. Release Lock
9. Report Result

---

# 115. Migration Runner Failure

If the runner fails:

```text
Record Error

↓

Protect Database

↓

Release Lock Safely

↓

Return Failure

↓

Require Recovery / Review
```

The runner must not report success when validation has failed.

---

# 116. Database Test Automation

The CI/test process should include:

- Clean Schema Creation
- Sequential Migrations
- Existing Database Upgrade
- Integrity Checks
- Critical Data Tests

---

# 117. Migration Compatibility Matrix

The project should maintain a compatibility matrix:

| Application | Minimum Schema | Required Schema |
|---|---:|---:|
| MFM 1.0 | Defined Baseline | v1.0 Schema |
| MFM 1.2 | v1.0 Baseline | v1.2 Schema |

Exact numeric schema versions are implementation values and must be maintained by the migration system.

---

# 118. Future Database Migration

If MFM eventually moves from SQLite to another database:

```text
Existing Domain Model

↓

Repository Abstraction

↓

Migration / Data Export

↓

New Database

↓

Validation
```

Business services should not require major redesign solely because the persistence technology changes.

---

# 119. Database Portability

Portability should not be pursued at the expense of simplicity.

SQLite-specific optimizations are acceptable when:

- Documented
- Tested
- Isolated where practical

---

# 120. Database Implementation Principle

The database should be:

```text
Reliable

Consistent

Understandable

Recoverable

Traceable
```

It should not become an independent business-rule engine.

---

# 121. Final Architectural Rule

The database persists business truth.

The domain services define business behavior.

The repositories control persistence access.

The migration system controls schema evolution.

These responsibilities must remain distinct.

---

# 122. Summary

MFM v1.2-530 establishes the database implementation and migration execution baseline.

It provides:

- Schema Versioning
- Migration History
- Migration Ordering
- Migration Validation
- Backup Before Migration
- Recovery
- Data Transformation
- Referential Integrity
- Indexing
- Performance Controls
- Database Security
- Production Migration
- Emergency Migration
- Traceability

The fundamental rule remains:

> **Database changes must preserve existing business truth and must never create a second authoritative financial ledger.**

Accounting Core remains the sole authoritative financial ledger.

---

# 123. Next Document

**MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution**

---

# END OF DOCUMENT
