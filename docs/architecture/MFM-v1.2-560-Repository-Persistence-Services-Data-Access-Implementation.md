# MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation

Version: 1.2

Document ID: MFM-v1.2-560

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for repositories, persistence services and controlled data access in MaritimForeningsManager (MFM) v1.2.

It follows:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution
- MFM v1.2-550 – Core Services & Domain Logic Implementation

The purpose is to establish a clear persistence boundary between business services and the database.

The document defines:

- Repository responsibilities
- Persistence contracts
- Query and command access
- Transactions
- Connection management
- Mapping
- Validation
- Concurrency
- Error translation
- Database integrity
- Performance
- Caching
- Document storage references
- Audit persistence
- Testing
- Migration compatibility
- Security controls
- Implementation patterns

---

# 2. Scope

This document covers persistence for:

- Accounting
- Membership
- Projects
- Grants
- Documents
- Security
- Audit
- Configuration
- Notifications
- Operations

It applies to SQLite persistence and to future persistence implementations if the underlying database technology changes.

---

# 3. Persistence Architectural Position

The persistence boundary is:

```text
GUI

↓

Application Service

↓

Domain Service

↓

Repository Interface

↓

Repository Implementation

↓

Database / File Storage / External Persistence
```

The repository is the controlled persistence gateway.

---

# 4. Repository Principle

Repositories persist and retrieve business data.

They do not become the primary location for business rules.

A repository should answer questions such as:

```text
Get Member

Save Member

Find Active Projects

Get Voucher

Save Grant
```

It should not decide complex business policy such as whether a voucher is allowed to post.

---

# 5. Authoritative Financial Rule

The persistence layer must preserve:

> **Accounting Core is the sole authoritative financial ledger.**

Repositories belonging to Projects, Grants, Reporting or other domains must not create alternative authoritative accounting transaction stores.

---

# 6. Repository Responsibilities

A repository may:

- Load Data
- Save Data
- Update Data
- Archive Data
- Query Data
- Delete Data where permitted
- Map Persistence Models
- Handle Database Constraints

A repository must not:

- Render GUI
- Send Email
- Authorize Users as its primary responsibility
- Decide Business Workflow
- Create Parallel Business Truth

---

# 7. Repository Interfaces

Repositories should expose business-oriented contracts.

Example:

```text
MemberRepository

get_by_id()

get_by_membership_number()

search()

save()

update()

archive()
```

The exact method names follow implementation conventions.

---

# 8. Repository Implementations

A repository interface may have a SQLite implementation:

```text
MemberRepository
        |
        +-- SQLiteMemberRepository
```

This supports controlled future persistence changes.

---

# 9. Repository Abstraction Principle

Do not create abstraction merely for abstraction's sake.

A repository interface is justified when it:

- Protects the service layer
- Improves testing
- Defines a clear persistence contract
- Isolates database technology

---

# 10. Database Access Rule

Business services must not normally execute raw SQL directly.

Preferred:

```text
Service

↓

Repository

↓

SQL
```

This keeps persistence logic centralized.

---

# 11. Direct SQL Exception

Direct SQL may be justified for:

- Migration
- Specialized Reporting Query
- Diagnostic Operation
- Performance-Critical Repository Query

Such usage must remain controlled and documented.

---

# 12. Connection Management

Database connections must be managed consistently.

A connection should:

- Open Safely
- Use Required Configuration
- Enable Required SQLite Features
- Close Correctly
- Not Leak Across Operations

---

# 13. SQLite Connection Initialization

Each connection should establish required settings consistently.

Examples may include:

- Foreign Key Enforcement
- Appropriate Journal Mode
- Busy Timeout
- Transaction Configuration

The exact settings follow the MFM database implementation.

---

# 14. Connection Lifetime

For a small desktop application, a simple controlled connection-per-operation or managed unit-of-work model may be appropriate.

The selected strategy must avoid:

- Leaked Connections
- Long Uncontrolled Transactions
- Cross-User State Leakage

---

# 15. Unit of Work

Where a business operation modifies multiple repositories atomically, a Unit of Work or equivalent transaction coordinator may be used.

Example:

```text
ProjectService

↓

UnitOfWork

├── ProjectRepository
├── TaskRepository
└── AuditRepository

↓

Commit
```

The abstraction should remain lightweight.

---

# 16. Transaction Ownership

The application/service layer should own business transaction boundaries.

Repositories may participate in a transaction but should not independently commit partial business operations.

---

# 17. Repository Commit Rule

Avoid:

```text
Repository A → commit

Repository B → commit

Repository C → commit
```

for one atomic business operation.

Prefer:

```text
Service

↓

Transaction

├── Repository A
├── Repository B
└── Repository C

↓

Commit
```

---

# 18. Accounting Transaction

Accounting persistence requires atomicity.

A posting operation should ensure that all required ledger entries are written together.

Failure must not leave a partial posting.

---

# 19. Repository Queries

Queries should:

- Return Required Data
- Use Parameters
- Use Appropriate Indexes
- Avoid Unnecessary Columns
- Avoid Unbounded Results

---

# 20. Parameterized Queries

All user-derived values must use parameterized SQL.

Unsafe:

```python
sql = "SELECT * FROM members WHERE name = '" + name + "'"
```

Safe:

```text
SELECT ...
WHERE name = ?
```

with parameters supplied separately.

---

# 21. SQL Injection Protection

Repository implementations must not construct SQL from untrusted input.

Dynamic identifiers such as sort columns must be selected from controlled whitelists.

---

# 22. Query Result Mapping

Database rows should be mapped into appropriate domain or persistence objects.

Avoid spreading raw row dictionaries throughout the application.

---

# 23. Mapping Boundary

A conceptual mapping is:

```text
Database Row

↓

Persistence Model

↓

Domain Model

↓

Application Service
```

The exact number of mapping layers may be reduced where the project is small, provided responsibilities remain clear.

---

# 24. Domain Model Independence

Domain services should not depend unnecessarily on:

- SQLite Cursor Objects
- SQL Strings
- Database Row Formats

This keeps business logic testable.

---

# 25. Null Handling

Repositories must explicitly handle NULL values.

Mapping should distinguish:

```text
Missing

Empty

Zero

False

Unknown
```

These are not always equivalent.

---

# 26. Date Mapping

Repositories should convert database date representations into the application's standard date/time representation.

Display formatting belongs outside persistence.

---

# 27. Currency Mapping

Repositories must preserve exact monetary values.

They must not introduce inappropriate floating-point conversion into Accounting Core.

---

# 28. Enumeration Mapping

Controlled statuses should be mapped consistently.

Example:

```text
Database:
ACTIVE

↓

Domain:
MemberStatus.ACTIVE
```

Invalid values should be detected rather than silently accepted.

---

# 29. Primary Key Handling

Repositories should return stable entity identifiers after creation.

The application should not assume that identifiers are reusable.

---

# 30. Foreign Key Handling

Repository operations must respect foreign-key constraints.

If a related entity does not exist:

```text
Save

↓

Constraint Failure

↓

Translate to Meaningful Error
```

---

# 31. Unique Constraint Handling

Database uniqueness errors should be translated into business-meaningful exceptions.

Example:

```text
UNIQUE constraint

↓

DuplicateMemberNumberError
```

The GUI can then provide a useful message.

---

# 32. Persistence Error Model

Persistence errors may include:

```text
DatabaseConnectionError

ConstraintViolationError

TransactionError

ConcurrencyError

MigrationRequiredError

StorageError
```

The exact class hierarchy follows the implementation.

---

# 33. Error Translation

Repositories should translate low-level database failures where useful.

Avoid exposing:

```text
sqlite3.IntegrityError
```

directly to ordinary users.

---

# 34. Not Found Semantics

Repositories should use a consistent approach for missing records.

Possible approaches:

```text
return None
```

or:

```text
raise NotFoundError
```

The project should select one convention and apply it consistently.

---

# 35. Query vs Command Repository Methods

Repository methods should distinguish:

### Query

```text
get_member()
search_members()
get_balance()
```

### Command / Persistence

```text
save_member()
update_member()
archive_member()
```

This improves readability.

---

# 36. Read-Only Queries

Read-only reporting queries should not modify database state.

This should remain true even when the query is executed from dashboards.

---

# 37. Reporting Repository Rule

Reporting repositories may use specialized read queries.

They must:

- Read authoritative sources
- Not alter business state
- Not create parallel ledgers
- Preserve source provenance

---

# 38. Accounting Repository

The Accounting repository is responsible for persistence of:

- Accounts
- Vouchers
- Voucher Lines
- Ledger Entries
- Period State
- Reversal References

The exact schema follows the Accounting Core implementation.

---

# 39. Accounting Repository Operations

Conceptual operations:

```text
save_voucher()

save_voucher_lines()

post_ledger_entries()

get_voucher()

get_ledger_entries()

get_account_balance()

get_period()

update_period_status()
```

---

# 40. Accounting Repository Integrity

Accounting persistence must protect:

```text
Balanced Entries

Transaction Atomicity

Posted History

Period Restrictions

Reference Integrity
```

Business authorization remains in services.

---

# 41. Accounting Immutability

Posted ledger entries should not be updated as an ordinary editing operation.

Corrections use the established reversal / adjustment model.

---

# 42. Accounting Query Consistency

A balance query must use the same authoritative ledger data used by financial reports.

There must not be separate calculation stores that can diverge.

---

# 43. Membership Repository

Membership repository responsibilities include:

- Members
- Membership Status
- Membership History
- Membership Categories

---

# 44. Membership Repository Operations

Conceptual:

```text
save_member()

get_member()

get_by_membership_number()

search_members()

save_status_change()

get_history()

archive_member()
```

---

# 45. Project Repository

Project repository responsibilities include:

- Projects
- Tasks
- Milestones
- Planning Data
- Project References

---

# 46. Project Repository Operations

Conceptual:

```text
save_project()

get_project()

search_projects()

save_task()

save_milestone()

update_project_status()
```

---

# 47. Project Financial Queries

Project persistence may store planning values.

Actual financial results should be obtained from Accounting Core.

Example:

```text
ProjectRepository

→ Budget Planning

AccountingService

→ Actual Spend
```

---

# 48. Grant Repository

Grant repository responsibilities include:

- Grant Records
- Applications
- Deadlines
- Awards
- Reporting Requirements

---

# 49. Grant Repository Operations

Conceptual:

```text
save_grant()

get_grant()

save_application()

update_application_status()

save_deadline()

save_award()
```

---

# 50. Document Repository

Document persistence is split conceptually:

```text
Document Metadata Repository

+

Document File Storage
```

The database should not be assumed to contain the document binary.

---

# 51. Document Metadata Repository

Responsibilities:

- Document Metadata
- Version Metadata
- Relationship
- Retention
- Hold
- Archive State

---

# 52. Document File Storage

File storage responsibilities:

- Store
- Read
- Verify
- Delete where authorized
- Return File Reference

File storage must not decide business authorization.

---

# 53. Document Consistency

When storing a document:

```text
Store File

↓

Create Metadata

↓

Commit Relationship
```

The implementation must define recovery for a failure between file storage and metadata persistence.

---

# 54. File Orphan Handling

If a file is stored but metadata creation fails:

```text
Orphan File

↓

Detect / Clean Up

```

Cleanup must be safe and must not delete a file that is already referenced elsewhere.

---

# 55. File Missing Handling

If metadata exists but the file is missing:

```text
Document Integrity Error
```

The application should report the problem rather than silently creating a replacement.

---

# 56. Security Repository

Security persistence includes:

- Users
- Roles
- Permissions
- Sessions
- Authentication Metadata

---

# 57. Password Persistence

Repositories must persist only secure password representations.

Plaintext passwords are prohibited.

---

# 58. Security Repository Operations

Conceptual:

```text
get_user()

save_user()

disable_user()

get_roles()

save_role()

get_permissions()

save_permission()

save_session()
```

---

# 59. Audit Repository

Audit repository stores:

- Event ID
- User
- Action
- Entity
- Timestamp
- Result
- Correlation ID

---

# 60. Audit Append Principle

Audit records should normally be append-oriented.

Ordinary users must not update or delete audit history.

---

# 61. Configuration Repository

Configuration persistence may store:

- Organization Settings
- Feature Configuration
- Retention Rules
- Notification Settings

Secrets should not be stored as ordinary configuration values where secure credential storage is available.

---

# 62. Notification Repository

Notification persistence may include:

- Notification
- Queue State
- Attempts
- Delivery Status
- Error State

---

# 63. Job Repository

Background job persistence may include:

```text
Job ID

Type

Status

Created

Started

Completed

Retry Count

Error

Correlation ID
```

---

# 64. Repository Concurrency

Repositories must account for concurrent updates.

A simple optimistic concurrency strategy may use:

```text
entity_version
```

---

# 65. Optimistic Update

Example:

```text
Load Member

version = 5

↓

Edit

↓

Update WHERE id = X AND version = 5

↓

If 0 rows changed

→ Concurrency Conflict
```

---

# 66. Concurrency Conflict

A concurrency conflict should not silently overwrite another user's changes.

The service should report:

```text
The record has changed since you opened it.
Please reload before saving.
```

---

# 67. SQLite Lock Handling

SQLite may return lock or busy conditions.

The implementation may use controlled retry or timeout behavior.

Retries must be bounded.

---

# 68. Transaction Retry

Do not blindly retry a failed business transaction.

Only retry when the failure is known to be transient and the operation remains safe.

---

# 69. Idempotency

Persistence operations supporting retry should be designed carefully.

Examples:

```text
Create Notification

Create Backup Record

Process External Event
```

A retry must not accidentally duplicate a business fact.

---

# 70. Unique Business References

Where duplicate prevention is important, combine:

```text
Application Idempotency

+

Database Unique Constraint
```

This provides stronger protection.

---

# 71. Bulk Operations

Repositories may provide bulk operations for:

- Imports
- Exports
- Archival
- Reporting

Bulk operations must remain controlled and transactional where required.

---

# 72. Bulk Insert

Bulk insertion should:

- Validate Data
- Use Transactions
- Handle Constraint Errors
- Report Results

---

# 73. Import Persistence

Import flow:

```text
Parse

↓

Validate

↓

Preview

↓

Confirm

↓

Repository Transaction

↓

Result
```

Do not insert unvalidated bulk data directly.

---

# 74. Export Persistence

Export queries should:

- Respect Permissions
- Use Filters
- Avoid Unbounded Memory
- Return Stable Results

---

# 75. Pagination

Repositories should support pagination for large result sets.

Example:

```text
search_members(
    filter,
    page,
    page_size
)
```

The exact interface may use another pagination model.

---

# 76. Sorting

Dynamic sorting should use controlled fields.

Never interpolate arbitrary user input into SQL column identifiers.

---

# 77. Filtering

Filters should be represented as structured inputs where practical.

Example:

```text
MemberFilter

status

category

search_text

created_from

created_to
```

---

# 78. Search Performance

Repository search should use appropriate indexes.

If a search becomes slow, inspect actual query plans before adding complexity.

---

# 79. N+1 Query Problem

Avoid repeatedly querying related records in loops.

Prefer:

```text
One appropriate query

or

Controlled batch query
```

when data volume justifies it.

---

# 80. Query Projection

Queries should select only required columns where practical.

Avoid:

```text
SELECT *
```

for large or security-sensitive operations unless justified.

---

# 81. Sensitive Data Queries

Repositories should not load sensitive fields unless the caller requires them.

Examples:

- Password Hash
- Credential Metadata
- Confidential Documents

---

# 82. Data Minimization

Persistence services should retrieve only what is required for the use case.

This reduces:

- Memory
- Exposure
- Accidental Logging
- Processing Cost

---

# 83. Cache Boundary

Caches must remain outside authoritative persistence.

A cache may store:

- Read Results
- Dashboard Data
- Reference Data

It must be rebuildable where practical.

---

# 84. Accounting Cache

Accounting values must remain traceable to Accounting Core.

A cached balance must have:

- Source
- Timestamp
- Refresh Strategy

---

# 85. Reference Data Cache

Stable reference data may be cached safely.

Examples:

- Membership Categories
- Status Definitions
- Static Configuration

Cache invalidation must be defined.

---

# 86. Persistence Security

Repositories must:

- Use Parameterized SQL
- Protect Sensitive Data
- Enforce Appropriate Access
- Avoid Secret Logging
- Use Controlled File Paths

---

# 87. Database Permissions

The application database file should be protected at operating-system level.

Normal users should not receive independent database write access.

---

# 88. Repository Audit

Repositories do not normally create business audit events themselves.

The service layer should determine which business actions require audit.

Persistence may record technical diagnostics where needed.

---

# 89. Repository Testing

Every repository should have tests for:

- Create
- Read
- Update
- Archive / Delete where allowed
- Constraints
- Missing Data
- Transactions
- Mapping
- Error Translation

---

# 90. Accounting Repository Testing

At minimum:

```text
Voucher Persistence

Line Persistence

Ledger Persistence

Period State

Reversal References

Transaction Rollback

Constraint Handling
```

---

# 91. Membership Repository Testing

At minimum:

```text
Member Create

Unique Membership Number

Update

Status History

Archive

Search

Pagination
```

---

# 92. Project Repository Testing

At minimum:

```text
Project Create

Task

Milestone

Status

Budget Planning

Relationships
```

---

# 93. Grant Repository Testing

At minimum:

```text
Grant Create

Application

Deadline

Award

Status

Relationships
```

---

# 94. Document Repository Testing

At minimum:

```text
Metadata

Version

Retention

Hold

Archive

Reference Integrity
```

---

# 95. Security Repository Testing

At minimum:

```text
User

Role

Permission

Session

Password Representation

Disable
```

---

# 96. Audit Repository Testing

Test:

- Append
- Query
- Correlation
- Timestamp
- Protected History

---

# 97. Integration Repository Testing

External persistence adapters should test:

- Success
- Timeout
- Invalid Response
- Authentication Failure
- Retry
- Duplicate Prevention

---

# 98. Test Database

Repository tests should use isolated test databases.

A test must not depend on production data.

---

# 99. Database Fixture

Fixtures should create only required data.

Example:

```text
Create Account

Create Member

Create Project
```

rather than loading a large unrelated database.

---

# 100. Repository Test Isolation

Each test should leave the database in a predictable state.

Options include:

- Transaction Rollback
- Fresh Test Database
- Controlled Fixture Reset

---

# 101. Migration Compatibility

Repository tests should run against the supported schema version.

Migration tests should separately verify upgrades.

---

# 102. Schema Contract

Repositories depend on schema contracts.

When schema changes:

```text
Migration

+

Repository Update

+

Tests
```

must be considered together.

---

# 103. Repository Change Workflow

A repository change should follow:

```text
Requirement

↓

Schema Review

↓

Migration if Required

↓

Repository Change

↓

Service Change if Required

↓

Tests

↓

Regression
```

---

# 104. Repository Refactoring

Refactoring should preserve:

- Contract
- Data
- Business Behavior
- Performance where required

Large persistence refactors should include additional regression tests.

---

# 105. Repository Performance

Measure before optimizing.

Important indicators:

- Query Duration
- Number of Queries
- Rows Returned
- Database Lock Duration
- Migration Impact

---

# 106. Index Selection

Indexes should be based on actual access patterns.

Typical candidates:

```text
Primary Keys

Foreign Keys

Unique Business Keys

Frequently Filtered Fields

Common Search Fields
```

---

# 107. Index Maintenance

Unused or redundant indexes should be reviewed.

The goal is not maximum index count.

The goal is appropriate performance.

---

# 108. Transaction Size

Transactions should be as small as practical while preserving business atomicity.

Long transactions may cause:

- SQLite Locks
- Poor Responsiveness
- Increased Failure Scope

---

# 109. Long-Running Queries

Long queries should not block the GUI unnecessarily.

Use background jobs for operations that genuinely require significant processing.

---

# 110. Repository and Background Jobs

Background jobs should call repository contracts rather than duplicate database logic.

---

# 111. Persistence Diagnostics

Administration diagnostics may provide:

- Database Version
- Connection Status
- Integrity Status
- Database Size
- Migration Status
- Backup Status

Sensitive details must be excluded.

---

# 112. Integrity Check

The database should support an integrity check.

A failed check is an operational incident.

Repositories must not attempt automatic destructive repair.

---

# 113. Backup Interaction

Backup should operate on a consistent database state.

The backup service owns backup execution.

Repositories provide persistence but do not independently create production backups.

---

# 114. Restore Interaction

After restore:

```text
Database

↓

Migration Check

↓

Integrity Check

↓

Repository Smoke Tests

↓

Application Startup
```

---

# 115. Repository Recovery

If a repository detects severe persistence inconsistency:

```text
Stop Risky Operation

↓

Raise Persistence Error

↓

Log

↓

Protect Data

↓

Recover / Diagnose
```

---

# 116. Data Access and Security

Data access must respect authorization context.

Services should not call a repository with broader access than the use case requires.

---

# 117. Privileged Repository Access

Repository access itself is an internal technical capability.

Security enforcement remains at the service boundary.

This prevents a repository from becoming the only security barrier.

---

# 118. Data Access and Personal Data

Repositories should minimize unnecessary retrieval of personal information.

Examples:

```text
Dashboard Member Count

→ Count only

not

→ Load all member contact data
```

---

# 119. Data Access and Documents

A document listing should normally return metadata.

The actual file should be loaded only when authorized and required.

---

# 120. Data Access and Reporting

Reports may require specialized queries.

These should remain read-only and traceable to authoritative source tables.

---

# 121. Financial Reporting Queries

Financial reports should use Accounting Core repository/query services.

They must not reconstruct accounting truth from project or grant tables.

---

# 122. Budget Reporting

Budget reports may combine:

```text
Project Budget

+

Accounting Actuals
```

The source of each value must remain identifiable.

---

# 123. Grant Financial Reporting

Grant reports may combine:

```text
Grant Award

+

Eligible Project Information

+

Accounting Actuals
```

Actuals remain authoritative in Accounting Core.

---

# 124. Repository Contracts and API Stability

Internal repository contracts should change deliberately.

If a contract changes:

- Update Implementations
- Update Tests
- Update Services
- Update Documentation

---

# 125. Repository Documentation

Important repositories should document:

- Purpose
- Owned Data
- Methods
- Transaction Expectations
- Error Behavior
- Security Assumptions

---

# 126. Persistence Naming Standards

Recommended:

```text
MemberRepository

ProjectRepository

GrantRepository

DocumentRepository

AccountingRepository
```

Implementations may use:

```text
SQLiteMemberRepository
```

where the technology-specific name is useful.

---

# 127. Avoid Generic Repository

Avoid creating one giant:

```text
GenericRepository
```

that hides all domain semantics.

Domain-specific repositories are usually clearer for MFM.

---

# 128. Generic Helpers

Generic helpers may still be used for:

- Connection Management
- Query Execution
- Mapping Utilities
- Pagination

They must not erase domain boundaries.

---

# 129. Repository Anti-Patterns

Avoid:

### SQL in GUI

### SQL in Domain Objects

### Business Rules in Repository

### Hidden Commits

### Silent Error Swallowing

### Generic Data Bucket

### Parallel Financial Ledger

---

# 130. Example Correct Persistence Flow

```text
User

↓

MembershipService.update_member()

↓

Authorization

↓

Business Validation

↓

MemberRepository.update()

↓

Database

↓

AuditService

↓

Result
```

---

# 131. Example Accounting Persistence Flow

```text
User

↓

AccountingService.post_voucher()

↓

Validation

↓

AccountingRepository

↓

Atomic Ledger Transaction

↓

Commit

↓

Audit

↓

Result
```

---

# 132. Example Reporting Flow

```text
Dashboard

↓

ReportingService

↓

AccountingQueryService

↓

AccountingRepository

↓

Read-only Query

↓

Dashboard Model
```

No financial state is modified.

---

# 133. Example Document Persistence Flow

```text
DocumentService

↓

Authorization

↓

DocumentRepository

+

FileStorage

↓

Metadata + File

↓

Audit
```

---

# 134. Repository Definition of Ready

A repository change is Ready when:

- Data Owner Is Known
- Schema Is Known
- Query / Command Contract Is Defined
- Transaction Requirement Is Defined
- Error Cases Are Known
- Tests Are Planned

---

# 135. Repository Definition of Done

A repository change is Done when:

- Implementation Complete
- Parameterized SQL Used
- Mapping Complete
- Constraints Handled
- Tests Pass
- Transaction Behavior Verified
- Documentation Updated

---

# 136. Production Persistence Gate

Before release verify:

```text
Schema Compatible

Migrations Tested

Repositories Tested

Accounting Integrity Tested

Backup Verified

Restore Tested

Security Reviewed

Performance Acceptable
```

---

# 137. Persistence Traceability

The persistence layer should trace:

```text
Requirement

↓

Architecture

↓

Service

↓

Repository Contract

↓

Repository Implementation

↓

Database Schema

↓

Migration

↓

Test

↓

Release
```

---

# 138. Small-Association Principle

The persistence layer should remain practical.

MFM does not require:

- Distributed Databases
- Database Clusters
- Complex ORM Infrastructure
- Microservices Persistence
- Heavy Data Platforms

unless future requirements justify them.

SQLite and a controlled repository layer remain appropriate for the current scale.

---

# 139. Future Database Portability

If MFM later moves to another database:

```text
Domain Services

↓

Repository Contracts

↓

New Repository Implementation

↓

New Database
```

The goal is to limit impact on business logic.

---

# 140. Final Persistence Principles

MFM persistence must be:

```text
Controlled

Consistent

Secure

Testable

Recoverable

Traceable
```

The repository layer protects the application from persistence details without hiding important data behavior.

---

# 141. Final Financial Persistence Principle

The most important boundary is:

> **Only Accounting Core repositories may persist authoritative accounting ledger transactions.**

Project, Grant, Reporting and Dashboard persistence may store their own domain information and planning values, but must not persist a competing authoritative financial ledger.

---

# 142. Summary

MFM v1.2-560 establishes the repository and persistence implementation baseline.

It defines:

- Repository Contracts
- SQLite Implementations
- Connection Management
- Transactions
- Unit of Work
- Mapping
- Constraints
- Error Translation
- Concurrency
- Pagination
- Performance
- Caching
- Document Storage
- Audit Persistence
- Repository Testing
- Security
- Recovery
- Traceability

The implementation principle remains:

> **Business services own business behavior; repositories own persistence access; the database protects structural integrity.**

And:

> **Accounting Core remains the sole authoritative financial ledger.**

---

# 143. Next Document

**MFM v1.2-570 – GUI, Presentation Layer & User Workflow Implementation**

---

# END OF DOCUMENT
