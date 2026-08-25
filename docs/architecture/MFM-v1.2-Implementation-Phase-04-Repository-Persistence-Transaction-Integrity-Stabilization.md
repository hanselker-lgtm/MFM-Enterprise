# MFM v1.2-Implementation-Phase-04
## Repository, Persistence & Transaction Integrity Stabilization

**Version:** 1.2  
**Document ID:** MFM-v1.2-Implementation-Phase-04  
**Status:** Implementation Phase Baseline  
**Phase:** Repository & Persistence Stabilization  
**Document Type:** Implementation Execution Document  

---

# 1. Purpose

This document defines the fourth implementation phase following:

- MFM v1.2-Implementation-Phase-01 – Source Tree, Database & Baseline Validation
- MFM v1.2-Implementation-Phase-02 – Test Foundation, Regression Baseline & Quality Gate
- MFM v1.2-Implementation-Phase-03 – Core Service Stabilization & Domain Boundary Validation

The purpose of this phase is to stabilize the persistence layer of MFM and establish controlled repository, database, transaction and data-integrity behavior before further functional expansion.

The implementation sequence is:

```text
Source / Database Baseline
        ↓
Test Foundation
        ↓
Core Service Stabilization
        ↓
Repository / Persistence Stabilization
        ↓
Controlled Feature Implementation
```

The central objective is:

> **Every persistent business fact must be stored consistently, transactionally and through a controlled persistence boundary.**

---

# 2. Scope

This phase covers:

- Repository architecture
- Repository responsibilities
- Persistence boundaries
- Database connections
- Connection lifecycle
- Query boundaries
- CRUD behavior
- Transaction management
- Commit behavior
- Rollback behavior
- Foreign-key integrity
- Unique constraints
- Check constraints
- Indexes
- Database migrations
- Schema versioning
- Persistence error handling
- Repository testing
- Database integration testing
- Data integrity
- Concurrency
- Optimistic concurrency
- Recovery
- Backup / restore validation
- Seed data
- Test database handling
- Repository quality gates
- Persistence Definition of Ready / Done

This phase does not redesign the MFM domain model.

---

# 3. Persistence Principle

The persistence layer exists to reliably store and retrieve authoritative application data.

It shall not become an uncontrolled location for business rules.

> **Repositories persist data; services and domain logic determine business behavior.**

---

# 4. Persistence Architecture

The preferred structure is:

```text
Presentation
      ↓
Application Service
      ↓
Domain Service
      ↓
Repository Interface
      ↓
Repository Implementation
      ↓
Database
```

The database must not become a direct dependency of the presentation layer.

---

# 5. Repository Responsibility

A repository is responsible for:

- Persistence
- Retrieval
- Query execution
- Mapping between persistence and application structures
- Persistence-related exceptions
- Transaction participation

A repository is not responsible for:

- GUI behavior
- User authorization policy
- Workflow orchestration
- Cross-domain business decisions
- Reporting presentation

---

# 6. Repository Contract

Each material repository should have a clear contract.

The contract should define:

```text
Entity / Aggregate
Create
Read
Update
Delete
Search
Filtering
Ordering
Transactions
Exceptions
```

Where relevant it should also define:

```text
Pagination
Locking
Versioning
Soft Delete
History
```

---

# 7. Repository Interface

Where practical, services should depend on repository abstractions rather than concrete database implementations.

Preferred:

```text
Service
   ↓
Repository Interface
   ↓
Repository Implementation
```

This improves testing and limits infrastructure coupling.

---

# 8. Repository Naming

Repository names should identify their persistence responsibility.

Examples:

```text
MemberRepository
ProjectRepository
GrantRepository
DocumentRepository
AccountRepository
JournalRepository
UserRepository
```

Avoid generic repositories that conceal important domain boundaries.

---

# 9. Generic Repository Risk

A universal repository such as:

```text
GenericRepository
```

should not become the default architecture for every domain.

Generic persistence utilities may be useful, but domain repositories should preserve meaningful boundaries.

---

# 10. Connection Management

Database connections shall be created and managed through a controlled mechanism.

The application should avoid uncontrolled connection creation throughout the source tree.

---

# 11. Connection Lifecycle

A connection should follow a predictable lifecycle:

```text
Acquire
 ↓
Use
 ↓
Commit / Rollback
 ↓
Close / Return
```

Connection leaks are persistence defects.

---

# 12. Connection Failure

A connection failure must:

- Be detected
- Be logged appropriately
- Be translated into a controlled persistence error
- Not expose database credentials
- Not silently continue against invalid state

---

# 13. Connection Configuration

Database connection details shall come from controlled configuration.

Hard-coded production database paths, credentials or connection strings should be avoided.

---

# 14. Query Boundary

Database queries shall remain inside the persistence boundary.

Application services should not contain scattered SQL statements.

---

# 15. Parameterized Queries

All dynamic query values shall be parameterized.

String concatenation must not be used to construct SQL from user-controlled input.

---

# 16. SQL Injection Protection

The persistence layer must prevent SQL injection through:

- Parameterized queries
- Controlled query construction
- Input validation
- Restricted database permissions

---

# 17. CRUD Operations

Repositories shall implement only the persistence operations required by the domain.

The baseline operations are:

```text
Create
Read
Update
Delete
```

Where deletion is unsafe or prohibited, the repository shall implement the approved alternative.

---

# 18. Read Operations

Read methods should define:

- Required identifiers
- Optional filters
- Ordering
- Result shape
- Missing-record behavior

---

# 19. Missing Record

A repository must have a defined behavior when a record does not exist.

Possible approaches:

```text
None / Empty Result
NotFound Exception
Optional Result
```

The chosen behavior shall be consistent within the repository contract.

---

# 20. Create Operation

Create operations shall:

- Validate persistence requirements
- Generate or accept controlled identifiers
- Persist required fields
- Respect constraints
- Return a defined result

Business validation remains the responsibility of the service/domain boundary.

---

# 21. Update Operation

Updates shall avoid silent overwrites.

Where concurrency matters, version checks or equivalent controls should be used.

---

# 22. Delete Operation

Deletion must follow domain policy.

Potential strategies include:

```text
Hard Delete
Soft Delete
Archive
Status Change
```

Financial and audit-sensitive records generally require preservation rather than uncontrolled deletion.

---

# 23. Soft Delete

Where soft delete is used, the implementation should define:

- Deleted flag/state
- Deleted date
- Deleted by
- Query behavior
- Restoration policy

---

# 24. Historical Data

Historical records shall not be destroyed merely because they are no longer active.

This is particularly important for:

- Accounting
- Membership history
- Grants
- Documents
- Audit records

---

# 25. Transaction Principle

Transactions shall protect logically atomic operations.

```text
Begin
 ↓
Operation
 ↓
Validate
 ↓
Commit
```

or:

```text
Begin
 ↓
Operation
 ↓
Failure
 ↓
Rollback
```

---

# 26. Commit Authority

The layer coordinating the business operation should control the transaction boundary.

Repositories should participate in transactions rather than independently committing partial operations unless explicitly designed to do so.

---

# 27. Rollback

Rollback must return the database to a consistent state when an atomic operation fails.

---

# 28. Partial State Prevention

The following is prohibited for an atomic workflow:

```text
Step 1 committed
Step 2 failed
Step 3 never executed
```

when the business operation requires all steps to succeed together.

---

# 29. Transaction Nesting

Nested transactions shall be used only where the database and transaction architecture explicitly support them.

Savepoints may be used where appropriate.

---

# 30. Transaction Scope

Transactions should be:

- As short as practical
- Large enough to preserve business atomicity
- Free of unnecessary external network calls
- Free of unnecessary user interaction

---

# 31. External Operations

Do not hold a database transaction open while waiting for:

- Email
- External APIs
- User input
- Long-running file operations

unless explicitly required and designed.

---

# 32. Idempotent Persistence

Persistence operations that may be retried should be designed to prevent duplicate records.

Examples:

```text
Imported Invoice
Imported Payment
External Reference
Document Registration
Migration
```

---

# 33. Unique Constraints

Database uniqueness should protect material identifiers.

Examples:

```text
Invoice Number + Supplier
External Transaction ID
Membership Number
Grant Reference
Document Identifier
User Login
```

The exact constraint depends on the domain.

---

# 34. Foreign Keys

Foreign keys shall be used where relational integrity requires them and where supported by the selected database engine.

---

# 35. Referential Integrity

The database shall prevent invalid references where practical.

Examples:

```text
Invoice → Unknown Customer
Journal Line → Unknown Account
Grant → Unknown Funder
Document Link → Unknown Document
```

---

# 36. Constraint Strategy

Constraints should be enforced at the database layer when the rule is fundamentally structural.

Business rules requiring contextual decisions remain in the service/domain layer.

---

# 37. Check Constraints

Check constraints may enforce structural conditions such as:

```text
Amount >= 0
Status IN allowed states
Required numeric range
```

Business rules that require external context should not be forced into database constraints unnecessarily.

---

# 38. Indexes

Indexes should support:

- Primary key lookups
- Foreign key lookups
- Frequent searches
- Unique identifiers
- Reporting queries where justified

Indexes should not be created indiscriminately.

---

# 39. Index Review

Material indexes should have a known purpose.

Unused or redundant indexes should be reviewed because they increase write cost and database complexity.

---

# 40. Query Performance

Repository queries should be reviewed for:

- Unnecessary full-table scans
- Excessive joins
- N+1 query patterns
- Unbounded result sets
- Missing indexes
- Duplicate queries

Performance optimization must not weaken correctness.

---

# 41. Pagination

Large result sets should support pagination or controlled limits where appropriate.

---

# 42. Ordering

Queries requiring deterministic ordering must specify it explicitly.

Database default ordering must not be relied upon.

---

# 43. Null Handling

Repositories shall define how database NULL values map into application structures.

---

# 44. Data Type Mapping

Database and application types must be mapped deliberately.

Special attention is required for:

```text
Money
Dates
DateTime
Boolean
Enumerations
Identifiers
Text
Binary Data
```

---

# 45. Financial Data

Financial amounts shall use the approved monetary representation.

The persistence layer must not introduce uncontrolled floating-point rounding.

---

# 46. Date and Time Persistence

Date/time fields shall follow the established MFM time-zone and storage policy.

Ambiguous local times must be avoided.

---

# 47. Enumeration Persistence

Enumerated states should use a stable representation.

Changing display text must not silently change stored state identifiers.

---

# 48. Schema Versioning

The database shall have an identifiable schema version.

The version must be:

- Stored
- Queryable
- Validated
- Used by migration logic
- Included in diagnostics

---

# 49. Migration Architecture

Database migrations shall be:

```text
Ordered
Repeatable in principle
Versioned
Traceable
Tested
```

Already-applied migrations must not execute again.

---

# 50. Migration Record

The migration system should record at least:

```text
Migration ID
Version
Applied Date
Status
```

Where appropriate:

```text
Checksum
Execution Duration
Application Version
```

---

# 51. Migration Failure

A failed migration must not leave the application operating against an unknown schema state.

The system shall:

```text
Detect
 ↓
Stop
 ↓
Report
 ↓
Recover / Correct
```

according to the migration strategy.

---

# 52. Fresh Database Test

Every material schema change shall be tested against a fresh database.

The test must verify:

- Database creation
- Schema creation
- Required tables
- Constraints
- Seed data
- Schema version
- Basic application access

---

# 53. Existing Database Upgrade Test

Material migrations shall also be tested against representative existing database states.

---

# 54. Data Migration

When schema changes require data transformation:

```text
Old Structure
 ↓
Transformation
 ↓
New Structure
 ↓
Validation
```

The original data must be preserved or transformed according to an approved migration plan.

---

# 55. Migration Idempotency

Migration execution should be protected against accidental repeated application.

---

# 56. Seed Data

Required seed data shall be distinguishable from user-created data.

Examples:

```text
System Roles
Default Configuration
Required Accounting Structures
Reference Values
```

---

# 57. Seed Data Safety

Initialization must not overwrite user data with default seed values.

---

# 58. Repository Error Handling

Persistence errors should be translated into meaningful application-level errors.

Examples:

```text
DuplicateRecordError
ForeignKeyError
PersistenceError
ConnectionError
MigrationError
ConcurrencyError
```

---

# 59. Constraint Error Translation

A raw database constraint exception should not normally escape directly into the GUI.

---

# 60. Logging

Repository failures should log enough information to diagnose the problem.

Logs should not contain:

- Passwords
- API secrets
- Full payment credentials
- Unnecessary personal information

---

# 61. Audit

Repositories should not be solely responsible for business audit semantics.

The service/domain boundary should determine which operations require audit evidence.

---

# 62. Audit Metadata

Where required, persistence should preserve:

```text
Created At
Created By
Updated At
Updated By
Version
```

The exact fields depend on the entity.

---

# 63. Concurrency

Concurrent updates must be considered for shared records.

Examples:

```text
Two users update the same member
Two users approve the same item
Two processes allocate the same receipt
Two processes modify the same project
```

---

# 64. Optimistic Concurrency

Where appropriate:

```text
Read Version
 ↓
Modify
 ↓
Update WHERE Version = Original Version
 ↓
Increment Version
```

If zero records are updated, a concurrency conflict exists.

---

# 65. Concurrency Error

Concurrency errors must be distinguishable from generic database failures.

---

# 66. Locking

Database locks may be used where required, but excessive locking should be avoided.

---

# 67. Deadlocks

The implementation should reduce deadlock risk through:

- Consistent update ordering
- Short transactions
- Appropriate indexes
- Controlled transaction scope

---

# 68. Persistence Testing

Repository tests shall cover:

```text
Create
Read
Update
Delete
Search
Duplicate
Foreign Key
Constraint
Transaction
Rollback
Concurrency
Migration
```

where applicable.

---

# 69. Transaction Test

A transaction test shall demonstrate:

```text
Start
 ↓
Write A
 ↓
Write B
 ↓
Failure
 ↓
Rollback
 ↓
A absent
B absent
```

when the operation is atomic.

---

# 70. Commit Test

A successful transaction test shall demonstrate:

```text
Start
 ↓
Write
 ↓
Commit
 ↓
Read
 ↓
Data Present
```

---

# 71. Repository Integration Test

A repository integration test shall exercise the actual database interface rather than only mocked calls.

---

# 72. Database Integrity Test

The test suite should verify:

- Required foreign keys
- Required unique constraints
- Required indexes
- Schema version
- Migration state

---

# 73. Backup Boundary

The database must be included in the MFM backup strategy.

The persistence implementation shall document what is required for a recoverable application state.

---

# 74. Restore Test

A restore test shall verify:

```text
Backup
 ↓
Restore
 ↓
Open Database
 ↓
Validate Schema
 ↓
Validate Data
 ↓
Start Application
```

---

# 75. Recovery Principle

> **A backup that has never been restored and verified is not sufficient evidence of recoverability.**

---

# 76. Test Database Reset

The test database shall support controlled reset or recreation.

Test resets must not affect production databases.

---

# 77. Production Database Protection

Automated tests must contain explicit safeguards against accidentally connecting to production.

---

# 78. Environment Guard

Where possible, the application should identify the environment:

```text
TEST
DEVELOPMENT
STAGING
PRODUCTION
```

and reject dangerous operations in test environments.

---

# 79. Data Access Security

Database credentials and connection information must be protected.

---

# 80. Least Privilege

Database users should have only the permissions required for their role.

---

# 81. Production Write Protection

Read-only diagnostic tools should not possess production write privileges.

---

# 82. Persistence Monitoring

Material persistence failures should be observable through:

- Application logs
- Error reporting
- Health checks
- Operational diagnostics

---

# 83. Repository Metrics

Useful metrics include:

```text
Query Duration
Transaction Duration
Failure Count
Connection Failures
Deadlocks
Rollback Count
Migration Failures
```

---

# 84. Performance Baseline

A basic persistence performance baseline should be established before optimization.

---

# 85. N+1 Detection

Repeated queries caused by iteration over records should be identified and reviewed.

---

# 86. Bulk Operations

Bulk operations should be used where they materially improve performance without weakening validation or auditability.

---

# 87. Bulk Operation Safety

Bulk operations must define:

- Validation
- Transaction behavior
- Failure handling
- Partial success behavior
- Audit requirements

---

# 88. Repository Refactoring

Repository refactoring shall follow:

```text
Add Test
 ↓
Change Repository
 ↓
Run Regression
 ↓
Validate Data
 ↓
Remove Legacy Path
```

---

# 89. Legacy Persistence

Existing persistence code shall be preserved until its replacement has been validated.

---

# 90. Persistence Technical Debt

Technical debt shall be recorded.

Examples:

```text
Direct SQL in Services
Missing Repository
Duplicated Queries
Missing Constraints
Missing Index
Unclear Transaction Boundary
Raw Database Exceptions
Missing Migration
Missing Test
```

---

# 91. Persistence Defect Register

Each persistence defect should contain:

| Field | Requirement |
|---|---|
| ID | Unique |
| Component | Repository / DB / Migration |
| Severity | P0–P3 |
| Description | Problem |
| Reproduction | Steps |
| Expected | Expected result |
| Actual | Actual result |
| Data Impact | Potential impact |
| Status | Lifecycle |
| Test | Regression test |
| Resolution | Correction |

---

# 92. Data Integrity Gate

The persistence layer passes the integrity gate when:

- Required constraints exist.
- Foreign keys work.
- Unique identifiers are protected.
- Transactions are reliable.
- Rollback is verified.
- Migration state is identifiable.
- Repository tests pass.

---

# 93. Transaction Integrity Gate

The transaction layer passes when:

```text
Atomic Success       ✓
Atomic Failure       ✓
Rollback             ✓
Commit               ✓
Retry Safety         ✓
Concurrency Handling ✓
```

---

# 94. Migration Gate

Migration passes when:

- Fresh database works.
- Existing database upgrade works.
- Migration version is recorded.
- Failure behavior is understood.
- Data integrity is preserved.
- Application startup validates the resulting schema.

---

# 95. Recovery Gate

Recovery passes when:

- Backup exists.
- Backup is restorable.
- Database opens after restore.
- Schema validates.
- Data validates.
- Application starts.

---

# 96. Repository Quality Gate

Repository stabilization passes when:

```text
Repository Contracts       ✓
Connection Management      ✓
Query Boundary             ✓
CRUD Behavior              ✓
Transactions               ✓
Constraints                ✓
Indexes                    ✓
Migrations                 ✓
Error Handling             ✓
Repository Tests            ✓
Recovery Validation        ✓
```

---

# 97. Definition of Ready

A persistence work item is Ready when:

- Repository owner is defined.
- Data model is known.
- Schema impact is known.
- Transaction behavior is defined.
- Constraint requirements are defined.
- Migration impact is defined.
- Test strategy is defined.
- Recovery impact is known.

---

# 98. Definition of Done

A persistence work item is Done when:

```text
Repository Implemented
        ↓
Unit Tested
        ↓
Database Tested
        ↓
Transaction Tested
        ↓
Migration Tested
        ↓
Regression Tested
        ↓
Recovery Considered
        ↓
Documentation Updated
        ↓
Quality Gate Passed
```

---

# 99. Final Persistence Principle

> **Repositories persist authoritative data; they do not become an alternative domain layer.**

---

# 100. Final Transaction Principle

> **Transactions must protect business atomicity and must never leave uncontrolled partial state.**

---

# 101. Final Database Principle

> **The database must enforce structural integrity while business services enforce contextual business rules.**

---

# 102. Final Migration Principle

> **Every schema change must be versioned, tested against fresh and existing databases, and recoverable through a controlled migration process.**

---

# 103. Final Recovery Principle

> **Recoverability must be demonstrated through restoration testing, not assumed from the existence of backups.**

---

# 104. Final Concurrency Principle

> **Concurrent updates must either be safely serialized or explicitly rejected; silent data loss is unacceptable.**

---

# 105. Final Security Principle

> **Database access must follow least privilege and must never expose credentials or uncontrolled production access to test or presentation components.**

---

# 106. Final Implementation Principle

> **Stabilize persistence and transaction integrity before expanding the functional surface of MFM.**

---

# 107. Summary

MFM v1.2-Implementation-Phase-04 establishes the Repository, Persistence and Transaction Integrity Stabilization baseline.

It defines:

- Repository Architecture
- Repository Responsibility
- Repository Contracts
- Repository Interfaces
- Connection Management
- Query Boundaries
- Parameterized Queries
- SQL Injection Protection
- CRUD
- Missing Records
- Create / Update / Delete
- Soft Delete
- Historical Data
- Transactions
- Commit / Rollback
- Partial State Prevention
- Transaction Scope
- Idempotency
- Unique Constraints
- Foreign Keys
- Referential Integrity
- Check Constraints
- Indexes
- Query Performance
- Pagination
- Data Type Mapping
- Financial Precision
- Date / Time Persistence
- Schema Versioning
- Migrations
- Migration Records
- Migration Failure Handling
- Fresh Database Testing
- Existing Database Upgrade Testing
- Data Migration
- Seed Data
- Persistence Error Handling
- Audit Metadata
- Concurrency
- Optimistic Concurrency
- Deadlock Reduction
- Repository Testing
- Transaction Testing
- Database Integration Testing
- Backup / Restore
- Test Database Protection
- Production Database Protection
- Least Privilege
- Persistence Monitoring
- Performance Baselines
- Bulk Operations
- Repository Refactoring
- Persistence Technical Debt
- Persistence Defect Register
- Data Integrity Gate
- Transaction Integrity Gate
- Migration Gate
- Recovery Gate
- Repository Quality Gate
- Definition of Ready
- Definition of Done

---

# 108. Next Implementation Phase

The next document shall be:

**MFM v1.2-Implementation-Phase-05 – GUI Stabilization, Presentation Layer & User Workflow Validation**

It shall establish the controlled stabilization of:

- Main application window
- Navigation
- Presentation architecture
- Forms
- Views
- Controllers / view models where applicable
- User input validation
- Error presentation
- Workflow navigation
- Membership workflows
- Accounting workflows
- Project workflows
- Grant workflows
- Document workflows
- Administration workflows
- User feedback
- Accessibility
- GUI security boundaries
- Presentation testing
- Smoke testing
- User workflow regression
- GUI quality gates

---

# 109. Document Control

**Document:** MFM v1.2-Implementation-Phase-04  
**Version:** 1.2  
**Status:** Implementation Phase Baseline  
**Previous Document:** MFM v1.2-Implementation-Phase-03  
**Next Document:** MFM v1.2-Implementation-Phase-05  
**Primary Transition:** Service Stabilization → Persistence Stabilization  
**Financial Authority:** Accounting Core  
**Principle:** Persistent data must remain consistent, transactional and recoverable
