# EA-IMETA-REALIZATION-02
# REPOSITORY & DATABASE IMPLEMENTATION

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Previous Realization: EA-IMETA-REALIZATION-01 – Physical System Foundation
### Source Builds: EA-IMETA-BUILD-02 and EA-IMETA-BUILD-10
### Scope: Authoritative Repository and Database Foundation

---

# 1. PURPOSE

EA-IMETA-REALIZATION-02 implements the authoritative persistence foundation of EA-IMETA.

The objective is to establish:

```text
DATABASE
   ↓
REPOSITORY
   ↓
APPLICATION SERVICES
   ↓
DOMAIN
```

The repository is the controlled boundary through which authoritative architecture information is stored, retrieved, versioned and changed.

---

# 2. CORE PRINCIPLE

The central persistence rule is:

> THE DATABASE STORES AUTHORITATIVE STATE; THE REPOSITORY CONTROLS ACCESS TO THAT STATE.

No presentation component, AI component, dashboard, agent or external connector may bypass the repository boundary for authoritative operations.

---

# 3. AUTHORITATIVE STATE

The authoritative state includes:

```text
ARCHITECTURE OBJECTS
RELATIONSHIPS
VERSIONS
CLASSIFICATIONS
OWNERSHIP
LIFECYCLE STATE
GOVERNANCE STATE
AUDIT REFERENCES
```

---

# 4. DATABASE ROLE

The database provides:

```text
PERSISTENCE
TRANSACTIONS
CONSTRAINTS
INDEXING
VERSION STORAGE
AUDIT SUPPORT
MIGRATION SUPPORT
```

It does not contain the complete business meaning of the platform. Semantic rules remain governed by the Metamodel and domain services.

---

# 5. REPOSITORY ROLE

The Repository provides:

```text
CREATE
READ
UPDATE
VERSION
SEARCH
LIST
ARCHIVE
RESTORE
```

through controlled interfaces.

---

# 6. DATABASE TECHNOLOGY

The implementation should use a mature relational database as the authoritative repository.

The initial implementation may use PostgreSQL.

The repository abstraction must avoid coupling domain logic directly to the selected database engine.

---

# 7. DATABASE SCHEMA ORGANIZATION

Logical schema areas:

```text
core
architecture
governance
audit
system
```

Additional schemas may be introduced later.

---

# 8. CORE SCHEMA

The core schema contains common persistence structures.

Examples:

```text
identifiers
tenants
users
roles
permissions
classifications
```

Only structures required by the current implementation should be created.

---

# 9. ARCHITECTURE SCHEMA

The architecture schema contains authoritative architecture objects and relationships.

Conceptually:

```text
architecture_object
architecture_relationship
architecture_version
```

---

# 10. SYSTEM SCHEMA

The system schema contains technical metadata:

```text
migration_metadata
job_metadata
configuration_metadata
system_settings
```

Secrets must not be stored here unless explicitly designed for secure encrypted storage.

---

# 11. AUDIT SCHEMA

The audit schema contains protected audit records.

Conceptually:

```text
audit_event
audit_change
```

---

# 12. GOVERNANCE SCHEMA

Governance persistence supports:

```text
change_request
approval
policy_reference
exception
```

Only the persistence structures required by the governance implementation should be introduced at this stage.

---

# 13. PRIMARY OBJECT MODEL

The repository must support a generic architecture object foundation.

Conceptual object:

```text
architecture_object
```

Core fields:

```text
id
object_type
name
description
status
classification
owner_id
created_at
created_by
updated_at
updated_by
current_version
```

---

# 14. OBJECT IDENTIFIER

Every authoritative object requires a stable identifier.

The identifier must remain stable across versions.

---

# 15. OBJECT TYPE

`object_type` identifies the metamodel type.

Examples may later include:

```text
CAPABILITY
APPLICATION
PROCESS
DATA_OBJECT
TECHNOLOGY
ORGANIZATION
INTERFACE
SERVICE
```

The final list is governed by the Metamodel implementation.

---

# 16. OBJECT STATUS

Initial lifecycle states may include:

```text
DRAFT
ACTIVE
SUSPENDED
RETIRED
ARCHIVED
```

The final lifecycle is governed by the Metamodel and Governance modules.

---

# 17. OBJECT VERSION

Every material change creates a new version where versioning is required.

Conceptual:

```text
architecture_version
```

Fields:

```text
id
object_id
version_number
state
snapshot
created_at
created_by
change_reference
```

---

# 18. VERSION IMMUTABILITY

Accepted historical versions must be immutable.

A correction is represented by a new version or governed correction process.

---

# 19. CURRENT VERSION

The object record may reference the current version:

```text
current_version
```

This reference must remain consistent with version records.

---

# 20. VERSION NUMBER

Use a deterministic version sequence per object.

Example:

```text
1
2
3
4
```

---

# 21. VERSION CONFLICT

Concurrent modifications must not silently overwrite each other.

Use optimistic concurrency control.

---

# 22. OPTIMISTIC CONCURRENCY

A write should verify:

```text
EXPECTED_VERSION
=
CURRENT_VERSION
```

If not:

```text
CONFLICT
```

---

# 23. CONFLICT RESPONSE

The application returns a controlled conflict error.

The user or governing process decides how to resolve it.

---

# 24. RELATIONSHIP MODEL

Conceptual:

```text
architecture_relationship
```

Fields:

```text
id
source_object_id
target_object_id
relationship_type
status
created_at
created_by
```

---

# 25. RELATIONSHIP VALIDATION

Relationships must satisfy:

```text
SOURCE EXISTS
TARGET EXISTS
TYPE IS VALID
DIRECTION IS VALID
CARDINALITY IS VALID
```

according to the Metamodel.

---

# 26. RELATIONSHIP VERSIONING

Where relationship changes are material, they must be versioned or auditable according to the governing metamodel.

---

# 27. REFERENTIAL INTEGRITY

Foreign keys must protect authoritative relationships.

---

# 28. DELETE POLICY

Physical deletion of authoritative architecture objects should be exceptional.

Preferred:

```text
RETIRE
ARCHIVE
```

rather than destructive deletion.

---

# 29. HARD DELETE

Hard deletion requires explicit authorization and must not be available as a normal UI operation for governed architecture objects.

---

# 30. SOFT DELETE

Where applicable, use lifecycle state:

```text
ARCHIVED
```

rather than removing historical information.

---

# 31. CLASSIFICATION

Authoritative objects may carry classification.

Examples:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
```

The final classification model is governed by security and governance requirements.

---

# 32. CLASSIFICATION INHERITANCE

Derived records must not accidentally become less restrictive than their source.

---

# 33. OWNERSHIP

Objects should support an owner reference.

Ownership may be:

```text
PERSON
ROLE
ORGANIZATION
TEAM
```

depending on the implemented identity model.

---

# 34. TENANCY

If multi-tenancy is enabled, authoritative records must contain an explicit tenant boundary.

---

# 35. TENANT ISOLATION

All repository queries must enforce tenant scope where tenancy exists.

---

# 36. REPOSITORY INTERFACE

Conceptual:

```text
ArchitectureRepository
```

Methods:

```text
create()
get()
update()
delete_or_archive()
list()
search()
get_version()
list_versions()
restore()
```

---

# 37. REPOSITORY SERVICE

The repository service is responsible for:

```text
PERSISTENCE
TRANSACTION BOUNDARY
CONCURRENCY
QUERY CONTROL
VERSIONING
```

---

# 38. DOMAIN INDEPENDENCE

Domain code must depend on repository interfaces rather than database-specific classes.

---

# 39. UNIT OF WORK

A Unit of Work abstraction should group related repository changes into one transaction.

Conceptual:

```text
begin()
commit()
rollback()
```

---

# 40. TRANSACTION PRINCIPLE

A governed operation affecting multiple authoritative records should be atomic where business consistency requires it.

---

# 41. TRANSACTION EXAMPLE

```text
CREATE OBJECT
+
CREATE RELATIONSHIP
+
CREATE AUDIT EVENT
```

should commit together where required by the domain operation.

---

# 42. ROLLBACK

If a transaction fails:

```text
ROLLBACK
```

No partial authoritative state may remain.

---

# 43. MIGRATION SYSTEM

All schema evolution is migration-based.

Recommended structure:

```text
migrations/
    0001_initial/
    0002_core/
    0003_architecture/
```

Exact naming may follow the selected migration framework.

---

# 44. MIGRATION RULE

Never manually alter production schema as the normal change mechanism.

---

# 45. MIGRATION VERSION

The application must know which migration version is active.

---

# 46. MIGRATION STARTUP

The application may verify migration state at startup.

Automatic destructive migration is prohibited.

---

# 47. MIGRATION FAILURE

If required migrations are missing or inconsistent:

```text
APPLICATION NOT READY
```

for protected environments.

---

# 48. DATABASE INITIALIZATION

Initial installation shall provide a controlled procedure:

```text
CREATE DATABASE
 ↓
RUN MIGRATIONS
 ↓
CREATE INITIAL ADMIN
 ↓
SEED REQUIRED SYSTEM DATA
 ↓
VERIFY
```

---

# 49. SEED DATA

Only mandatory system/reference data should be seeded automatically.

Demo data must be separate.

---

# 50. DATABASE CONNECTION

The application uses a managed database session/connection layer.

Requirements:

```text
POOL
TIMEOUT
HEALTH CHECK
CLEANUP
```

---

# 51. CONNECTION POOL

Connection pool size must be configurable per environment.

---

# 52. DATABASE TIMEOUT

Queries and transactions must not remain indefinitely active.

---

# 53. DATABASE RETRY

Transient connection failures may be retried under controlled limits.

Do not blindly retry non-idempotent transactions.

---

# 54. INDEXING

Indexes shall support:

```text
OBJECT ID
OBJECT TYPE
STATUS
OWNER
CLASSIFICATION
UPDATED_AT
VERSION
RELATIONSHIP SOURCE
RELATIONSHIP TARGET
```

Only measured or expected access patterns should justify additional indexes.

---

# 55. UNIQUE CONSTRAINTS

Use database constraints to enforce:

```text
STABLE IDENTIFIERS
VERSION UNIQUENESS
REQUIRED BUSINESS KEYS
```

where applicable.

---

# 56. NOT NULL

Required authoritative fields should be protected by database constraints where possible.

---

# 57. CHECK CONSTRAINTS

Use database constraints for simple invariants that must never be violated.

---

# 58. FOREIGN KEYS

Foreign keys must protect references to authoritative entities.

---

# 59. CASCADE POLICY

Cascading deletes must be used cautiously.

For governed architecture objects, destructive cascade is normally prohibited.

---

# 60. DATABASE NORMALIZATION

Authoritative transactional data should remain appropriately normalized.

Denormalized projections belong in dedicated projection/read models where appropriate.

---

# 61. READ MODELS

Dashboard and graph read models may later use optimized structures.

They do not replace authoritative tables.

---

# 62. SEARCH

Repository search must support controlled filters such as:

```text
OBJECT TYPE
NAME
STATUS
OWNER
CLASSIFICATION
VERSION
DATE
```

---

# 63. PAGINATION

List and search APIs must use bounded pagination.

---

# 64. MAXIMUM PAGE SIZE

The platform shall enforce a configurable maximum page size.

---

# 65. SORTING

Sorting must be explicit and deterministic.

---

# 66. FILTER VALIDATION

Search filters must be validated against allowed fields.

No arbitrary SQL fragments may enter the repository API.

---

# 67. SQL INJECTION PROTECTION

Use parameterized queries or ORM/query-builder mechanisms.

Never concatenate untrusted values into SQL.

---

# 68. REPOSITORY ERROR MODEL

Repository errors should map to controlled application errors:

```text
NOT_FOUND
CONFLICT
VALIDATION
DATABASE_UNAVAILABLE
TRANSACTION_FAILED
```

---

# 69. NOT FOUND

A missing object should return a consistent not-found result.

---

# 70. CONFLICT

Version or uniqueness conflicts return a controlled conflict.

---

# 71. DATABASE UNAVAILABLE

The system must fail safely and provide a correlation ID.

---

# 72. AUDIT INTEGRATION

Material repository changes must generate audit information.

---

# 73. AUDIT CONTENT

At minimum:

```text
ACTOR
ACTION
OBJECT
VERSION
TIMESTAMP
RESULT
CORRELATION_ID
```

---

# 74. BEFORE / AFTER

For sensitive or material changes, audit may include controlled before/after information.

Avoid storing secrets in audit.

---

# 75. AUDIT TRANSACTION

Where required, audit and authoritative state change should be committed atomically.

---

# 76. AUDIT FAILURE

If audit is mandatory for an operation and audit persistence fails:

```text
ROLLBACK OPERATION
```

unless an explicitly governed alternative exists.

---

# 77. REPOSITORY EVENTS

Repository operations may publish internal events after successful commit.

Examples:

```text
OBJECT_CREATED
OBJECT_UPDATED
OBJECT_VERSION_CREATED
OBJECT_ARCHIVED
```

---

# 78. EVENT TIMING

Events representing committed state should be emitted only after successful transaction commit.

---

# 79. OUTBOX FOUNDATION

If reliable asynchronous event delivery is required, use an outbox pattern.

Conceptually:

```text
transaction
   ↓
authoritative data
+
outbox event
   ↓
commit
   ↓
publisher
```

---

# 80. OUTBOX PURPOSE

The outbox prevents a successful database transaction from being separated from its required event record.

---

# 81. OUTBOX RETENTION

Outbox retention and cleanup must be governed.

---

# 82. IDEMPOTENT EVENT HANDLING

Consumers should safely handle duplicate delivery.

---

# 83. BACKUP

The database must support scheduled backup according to operational requirements.

---

# 84. BACKUP TYPES

Depending on the selected database platform:

```text
FULL
INCREMENTAL
POINT-IN-TIME
```

may be supported.

---

# 85. BACKUP SECURITY

Backups must be:

```text
ACCESS CONTROLLED
ENCRYPTED WHERE REQUIRED
MONITORED
TESTED
```

---

# 86. RESTORE TEST

A backup is not considered valid until restore has been tested.

---

# 87. RECOVERY TARGETS

Production must define:

```text
RPO
RTO
```

according to operational requirements.

---

# 88. DATABASE MONITORING

Monitor:

```text
CONNECTIONS
QUERY LATENCY
LOCKS
ERRORS
STORAGE
CPU
MEMORY
```

where supported.

---

# 89. SLOW QUERY MONITORING

Long-running queries should be detectable.

---

# 90. LOCK MONITORING

Long-lived locks must be detectable.

---

# 91. TRANSACTION MONITORING

Monitor failed and long-running transactions.

---

# 92. DATA QUALITY

Repository validation must identify:

```text
MISSING REFERENCES
DUPLICATES
INVALID TYPES
INVALID RELATIONSHIPS
VERSION GAPS
```

---

# 93. RECONCILIATION

Repository reconciliation checks authoritative internal consistency.

---

# 94. RECONCILIATION REPORT

Conceptual:

```text
repository_reconciliation_report
```

Contains:

```text
RUN_ID
STARTED_AT
COMPLETED_AT
ERROR_COUNT
WARNING_COUNT
STATUS
```

---

# 95. RECONCILIATION ACTION

Reconciliation should identify problems.

Automatic destructive correction is not permitted without explicit governance.

---

# 96. DATA IMPORT

Imported records must pass:

```text
SCHEMA
METAMODEL
SECURITY
DUPLICATE
REFERENCE
```

validation before becoming authoritative.

---

# 97. IMPORT STAGING

Large or uncertain imports should use a staging area:

```text
IMPORT
 ↓
STAGING
 ↓
VALIDATION
 ↓
REVIEW
 ↓
COMMIT
```

---

# 98. IMPORT FAILURE

Failed imports must not partially corrupt authoritative data.

---

# 99. EXPORT

Exports must respect:

```text
AUTHORIZATION
CLASSIFICATION
TENANCY
AUDIT
```

---

# 100. EXPORT VERSION

An export should identify:

```text
SYSTEM VERSION
SCHEMA VERSION
DATA VERSION
EXPORT TIME
```

---

# 101. SNAPSHOT

A repository snapshot may be generated for:

```text
BASELINE
ARCHIVE
TEST
DISASTER RECOVERY
```

---

# 102. SNAPSHOT INTEGRITY

Snapshots should be verifiable using checksums or equivalent integrity mechanisms.

---

# 103. DATA RETENTION

Retention periods must be governed by:

```text
BUSINESS
LEGAL
REGULATORY
SECURITY
```

requirements.

---

# 104. PURGE

Purge is a controlled operation.

No automated purge may remove protected authoritative records without an approved retention policy.

---

# 105. PRIVACY

Personal data must be minimized and protected according to applicable requirements.

---

# 106. DATABASE ACCESS ROLES

At minimum separate:

```text
APPLICATION
MIGRATION
ADMINISTRATION
READ-ONLY
```

where operationally appropriate.

---

# 107. LEAST PRIVILEGE

The runtime application account must not automatically receive schema administration privileges.

---

# 108. ADMINISTRATION ACCOUNT

Administrative credentials must be separately controlled.

---

# 109. CREDENTIAL ROTATION

Database credentials should support rotation without source code changes.

---

# 110. ENCRYPTION

Production database traffic and backups should use appropriate encryption.

---

# 111. SENSITIVE FIELDS

Sensitive values should be encrypted, tokenized or otherwise protected where required.

---

# 112. NO SECRETS IN DATABASE LOGS

SQL logs and application logs must not expose credentials or secret values.

---

# 113. REPOSITORY API

Initial repository API may expose:

```text
POST   /api/v1/repository/objects
GET    /api/v1/repository/objects/{id}
PUT    /api/v1/repository/objects/{id}
GET    /api/v1/repository/objects/{id}/versions
POST   /api/v1/repository/objects/{id}/archive
POST   /api/v1/repository/search
```

Exact HTTP semantics may be adjusted during implementation.

---

# 114. API AUTHORIZATION

Every repository mutation endpoint must enforce authorization.

---

# 115. API VALIDATION

Object type and fields must be validated before repository write.

---

# 116. API VERSION CONFLICT

Update requests should carry the expected object version.

---

# 117. API RESPONSE

Successful mutation should return:

```text
OBJECT ID
VERSION
STATUS
CORRELATION ID
```

as appropriate.

---

# 118. REPOSITORY SERVICE TESTING

Test:

```text
CREATE
READ
UPDATE
VERSION
ARCHIVE
SEARCH
CONFLICT
TRANSACTION
AUDIT
```

---

# 119. DATABASE TESTING

Test:

```text
MIGRATIONS
CONSTRAINTS
FOREIGN KEYS
INDEXES
TRANSACTIONS
ROLLBACK
BACKUP
RESTORE
```

---

# 120. CONCURRENCY TESTING

Simulate two updates against the same version.

Expected:

```text
ONE SUCCESS
ONE CONFLICT
```

unless the business operation explicitly supports another strategy.

---

# 121. TRANSACTION TEST

Force an error after a multi-table write begins.

Expected:

```text
NO PARTIAL AUTHORITATIVE STATE
```

---

# 122. AUDIT TEST

Create and modify an object.

Expected:

```text
AUTHORITATIVE CHANGE
+
AUDIT EVENT
```

---

# 123. ARCHIVE TEST

Archive an object.

Expected:

```text
OBJECT RETAINED
STATUS = ARCHIVED
HISTORY RETAINED
```

---

# 124. RESTORE TEST

Restore an archived object only through an authorized operation.

---

# 125. IMPORT TEST

Import invalid data.

Expected:

```text
REJECTED
NO AUTHORITATIVE CORRUPTION
```

---

# 126. EXPORT TEST

Export authorized data.

Expected:

```text
CORRECT SCOPE
CORRECT CLASSIFICATION
AUDIT
```

---

# 127. SECURITY TEST

Attempt:

```text
UNAUTHORIZED READ
UNAUTHORIZED WRITE
TENANT CROSSING
CLASSIFICATION BYPASS
```

Expected:

```text
DENIED
AUDITED
```

---

# 128. SQL INJECTION TEST

Attempt injection through:

```text
SEARCH
FILTER
SORT
OBJECT FIELDS
```

Expected:

```text
NO SQL EXECUTION OUTSIDE INTENDED QUERY
```

---

# 129. PERFORMANCE TEST

Establish baseline for:

```text
SINGLE OBJECT READ
SINGLE OBJECT WRITE
SEARCH
VERSION LIST
RELATIONSHIP QUERY
```

---

# 130. LOAD TEST

Test expected repository concurrency.

---

# 131. FAILURE TEST

Stop database connectivity during a request.

Expected:

```text
CONTROLLED ERROR
NO FALSE SUCCESS
CORRELATION ID
```

---

# 132. RECOVERY TEST

Restore database connectivity.

Expected:

```text
APPLICATION RECOVERS
REPOSITORY OPERATIONS RESUME
```

---

# 133. MIGRATION TEST

Execute migrations against a clean database.

Expected:

```text
SUCCESS
SCHEMA VERIFIED
```

---

# 134. UPGRADE MIGRATION TEST

Run migrations against the previous supported schema version.

Expected:

```text
DATA PRESERVED
SCHEMA UPDATED
```

---

# 135. ROLLBACK MIGRATION

Where rollback is technically supported, test it.

Where irreversible migrations exist, provide a documented forward recovery strategy.

---

# 136. REPOSITORY BASELINE

After acceptance establish:

```text
EA-IMETA-REPOSITORY-BASELINE-01
```

including:

```text
SCHEMA
MIGRATIONS
REPOSITORY INTERFACES
CONSTRAINTS
INDEXES
AUDIT
BACKUP
TEST RESULTS
```

---

# 137. REALIZATION-02 ACCEPTANCE MATRIX

```text
[ ] Relational database configured
[ ] Migration framework configured
[ ] Core schema created
[ ] Architecture schema created
[ ] Audit schema created
[ ] Governance persistence foundation created
[ ] Architecture object persistence works
[ ] Object versioning works
[ ] Relationship persistence works
[ ] Optimistic concurrency works
[ ] Transactions work
[ ] Rollback works
[ ] Repository interface works
[ ] Search works
[ ] Pagination works
[ ] Audit integration works
[ ] Outbox foundation works where required
[ ] Backup procedure exists
[ ] Restore procedure tested
[ ] Import validation works
[ ] Export controls work
[ ] Security boundaries work
[ ] SQL injection tests pass
[ ] Performance baseline exists
[ ] Reconciliation exists
[ ] Documentation exists
```

---

# 138. RELEASE GATE

REALIZATION-02 must not progress if:

```text
AUTHORITATIVE DATA CAN BE BYPASSED
VERSIONING IS UNRELIABLE
TRANSACTIONS LEAVE PARTIAL STATE
AUDIT IS UNRELIABLE
DATABASE MIGRATIONS ARE UNCONTROLLED
BACKUP CANNOT BE RESTORED
SECURITY BOUNDARIES FAIL
```

---

# 139. NEXT REALIZATION

The next document should implement the semantic metamodel layer:

```text
EA-IMETA-REALIZATION-03
METAMODEL ENGINE IMPLEMENTATION
```

It will use the repository created here as its authoritative persistence foundation.

---

# 140. REALIZATION-02 PRINCIPLES

1. Database is authoritative persistence.
2. Repository is the controlled access boundary.
3. Domain logic never depends directly on database implementation.
4. Versions are immutable historical records.
5. Concurrent writes must not silently overwrite.
6. Transactions protect consistency.
7. Audit accompanies material change.
8. Imports are validated before commit.
9. Exports respect authorization and classification.
10. Backups are only valid when restore is tested.
11. Destructive deletion is exceptional.
12. Migrations are controlled and versioned.
13. Repository APIs are validated and authorized.
14. Database credentials remain externalized.
15. The Knowledge Graph and AI must consume repository data through governed interfaces.

---

# 141. COMPLETION STATEMENT

EA-IMETA-REALIZATION-02 establishes the physical authoritative repository and database layer.

The platform now has:

```text
PHYSICAL FOUNDATION
        ↓
AUTHORITATIVE DATABASE
        ↓
CONTROLLED REPOSITORY
        ↓
VERSIONED ARCHITECTURE STATE
        ↓
AUDITABLE PERSISTENCE
```

This provides the stable persistence base required by:

```text
METAMODEL
GOVERNANCE
INTEGRATION
KNOWLEDGE GRAPH
DASHBOARD
DECISION SERVICES
AI
ADAPTIVE ARCHITECTURE
```

The next realization phase can therefore focus on meaning and semantic validation rather than persistence infrastructure.

> THE REPOSITORY IS THE GATEWAY TO AUTHORITATIVE ARCHITECTURE STATE; EVERY GOVERNED CHANGE MUST PASS THROUGH IT.

---

# END OF EA-IMETA-REALIZATION-02
## REPOSITORY & DATABASE IMPLEMENTATION
## COMPLETE
