# EA-IMETA-BUILD-02
# REPOSITORY & DATABASE

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Previous Build: EA-IMETA-BUILD-01 – System Foundation
### Implementation Basis: EA-IMETA-IMPLEMENTATION-02

---

# 1. PURPOSE

EA-IMETA-BUILD-02 defines the physical repository and database foundation of the EA-IMETA platform.

BUILD-01 established the technical runtime foundation.

BUILD-02 now establishes the authoritative persistence layer on which the remaining EA-IMETA capabilities will operate.

The repository is the authoritative structured source for EA-IMETA architecture information.

The central principle is:

> ONE GOVERNED REPOSITORY, ONE CONSISTENT IDENTIFIER MODEL, ONE TRACEABLE SOURCE OF ARCHITECTURE TRUTH.

---

# 2. BUILD-02 SCOPE

BUILD-02 covers:

```text
DATABASE ARCHITECTURE
SCHEMA ORGANIZATION
IDENTIFIERS
ARCHITECTURE OBJECTS
RELATIONSHIPS
OWNERSHIP
LIFECYCLE
CLASSIFICATION
EVIDENCE
TAGS
METADATA
AUDIT FOUNDATION
VERSIONING
REPOSITORY SERVICES
REPOSITORY API
MIGRATIONS
INDEXING
CONSTRAINTS
DATA QUALITY
BACKUP / RESTORE
TEST DATA
REPOSITORY TESTING
```

BUILD-02 does not yet implement the complete metamodel engine, workflow engine, graph engine, AI layer or adaptive engine.

Those capabilities consume the repository established here.

---

# 3. REPOSITORY ROLE

The repository provides:

```text
PERSISTENCE
+
IDENTITY
+
STRUCTURE
+
RELATIONSHIPS
+
OWNERSHIP
+
LIFECYCLE
+
CLASSIFICATION
+
TRACEABILITY
+
AUDIT FOUNDATION
```

It is not merely a collection of database tables.

It is the persistent implementation of the EA-IMETA information foundation.

---

# 4. SOURCE OF TRUTH

For governed architecture objects:

```text
EA-IMETA REPOSITORY
        ↓
AUTHORITATIVE STRUCTURED INFORMATION
```

External systems may provide source information, but imported information must retain source provenance.

---

# 5. SYSTEM OF RECORD VS SOURCE SYSTEM

The repository shall distinguish:

```text
SYSTEM OF RECORD
```

from:

```text
SOURCE SYSTEM
```

A source system may provide data.

EA-IMETA may govern the architecture representation of that data.

---

# 6. REPOSITORY PRINCIPLES

1. Every governed object has a stable identifier.
2. Every relationship has a defined semantic meaning.
3. Every important object has an owner.
4. Lifecycle state is explicit.
5. Classification is explicit where required.
6. Source provenance is retained.
7. Historical changes are traceable.
8. Invalid relationships are prevented where possible.
9. Referential integrity is enforced by the database.
10. Domain rules are enforced by application services.
11. Schema changes are versioned.
12. Deletion is controlled.
13. Auditability is preserved.

---

# 7. DATABASE PLATFORM

The target database is:

```text
PostgreSQL
```

BUILD-02 assumes the connection foundation established in BUILD-01.

---

# 8. DATABASE SCHEMA

The preferred PostgreSQL schema is:

```text
ea_imeta
```

System/migration metadata may remain in the default administrative schema where appropriate.

Domain tables should use the `ea_imeta` namespace unless a later architecture decision defines a stronger separation.

---

# 9. DATABASE NAMING

Use:

```text
snake_case
```

Examples:

```text
architecture_object
object_relationship
lifecycle_state
evidence_record
```

Table names should be singular unless a later database standard explicitly chooses plural naming.

---

# 10. PRIMARY IDENTIFIER

Every governed object shall have a stable technical identifier.

Recommended database type:

```text
UUID
```

The identifier shall not encode business meaning.

Avoid identifiers such as:

```text
APP-001
CAP-001
TECH-001
```

as primary keys.

Business/reference identifiers may exist separately.

---

# 11. PUBLIC REFERENCE ID

A human-readable reference may be stored separately.

Example:

```text
APP-000123
CAP-000045
TECH-000021
```

This is a reference identifier, not the database primary key.

---

# 12. IDENTIFIER PRINCIPLE

The distinction is:

```text
UUID
→ technical identity

REFERENCE ID
→ human/business identity
```

A reference ID may change under controlled governance.

The UUID should remain stable.

---

# 13. CORE OBJECT MODEL

The repository shall support a generic architecture object foundation.

Conceptually:

```text
ARCHITECTURE OBJECT
        │
        ├── TYPE
        ├── NAME
        ├── DESCRIPTION
        ├── OWNER
        ├── LIFECYCLE
        ├── STATUS
        ├── CLASSIFICATION
        ├── SOURCE
        └── METADATA
```

Specific metamodel types are expanded in BUILD-03.

---

# 14. ARCHITECTURE OBJECT TABLE

Conceptual table:

```text
architecture_object
```

Core fields:

```text
id
reference_id
object_type
name
description
status
lifecycle_state_id
owner_id
classification_id
source_system_id
source_reference
created_at
created_by
updated_at
updated_by
```

---

# 15. OBJECT TYPE

`object_type` identifies the metamodel category.

Initial examples:

```text
CAPABILITY
BUSINESS_PROCESS
ORGANIZATION
APPLICATION
DATA_ENTITY
TECHNOLOGY
SERVICE
INTERFACE
PROJECT
RISK
DECISION
PRINCIPLE
STANDARD
```

The authoritative type catalogue belongs to BUILD-03.

---

# 16. OBJECT STATUS

Status represents repository state.

Initial values:

```text
DRAFT
ACTIVE
SUSPENDED
RETIRED
ARCHIVED
```

Status and lifecycle must not be confused.

---

# 17. LIFECYCLE

Lifecycle describes the object's progression through its managed life.

Example:

```text
PROPOSED
PLANNED
ACTIVE
DEPRECATED
RETIRED
```

The lifecycle model is configurable.

---

# 18. LIFECYCLE TABLE

Conceptual table:

```text
lifecycle_state
```

Fields:

```text
id
name
description
sequence
is_initial
is_terminal
is_active
```

---

# 19. LIFECYCLE TRANSITIONS

Transitions shall be governed.

Conceptual table:

```text
lifecycle_transition
```

Fields:

```text
id
from_state_id
to_state_id
transition_name
description
requires_approval
```

BUILD-04 will later add workflow enforcement.

---

# 20. OWNERSHIP

Ownership is mandatory for important governed objects.

Conceptual model:

```text
OBJECT
 ↓
OWNER
 ↓
ORGANIZATION / PERSON / ROLE
```

The repository should support ownership without hard-coding one organizational structure.

---

# 21. OWNER TABLE

Conceptual table:

```text
owner_reference
```

Fields:

```text
id
owner_type
external_reference
name
email
organization_reference
active
```

The final identity integration belongs to later builds.

---

# 22. CLASSIFICATION

Information classification shall be explicit.

Initial levels may include:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
```

Actual organizational classifications shall be configurable.

---

# 23. CLASSIFICATION TABLE

Conceptual table:

```text
classification
```

Fields:

```text
id
code
name
description
sensitivity_level
active
```

---

# 24. SOURCE SYSTEM

External provenance shall be retained.

Conceptual table:

```text
source_system
```

Fields:

```text
id
name
system_type
description
owner_reference
base_url
active
```

---

# 25. SOURCE REFERENCE

Imported or synchronized objects should retain:

```text
source_system_id
source_reference
source_version
source_timestamp
```

This enables reconciliation.

---

# 26. PROVENANCE

The repository should answer:

```text
WHERE DID THIS INFORMATION COME FROM?
WHEN WAS IT RECEIVED?
WHO IMPORTED IT?
WHAT WAS THE SOURCE VERSION?
```

---

# 27. RELATIONSHIP MODEL

Architecture is more than isolated objects.

The repository therefore requires explicit relationships.

Conceptually:

```text
OBJECT A
   ↓
RELATIONSHIP
   ↓
OBJECT B
```

---

# 28. OBJECT RELATIONSHIP TABLE

Conceptual table:

```text
object_relationship
```

Fields:

```text
id
source_object_id
target_object_id
relationship_type_id
description
status
confidence
source_system_id
source_reference
valid_from
valid_to
created_at
created_by
updated_at
updated_by
```

---

# 29. RELATIONSHIP TYPE

Conceptual table:

```text
relationship_type
```

Examples:

```text
SUPPORTS
DEPENDS_ON
IMPLEMENTS
USES
OWNS
CONTAINS
REALIZES
PROVIDES
CONSUMES
GOVERNS
MITIGATES
AFFECTS
```

The complete relationship catalogue belongs to BUILD-03.

---

# 30. RELATIONSHIP SEMANTICS

Relationships shall have defined direction.

Example:

```text
Application A
    SUPPORTS
Capability B
```

This must not silently mean:

```text
Capability B
    SUPPORTS
Application A
```

Direction is part of the relationship meaning.

---

# 31. RELATIONSHIP CONSTRAINTS

The database should enforce:

```text
source_object_id IS NOT NULL
target_object_id IS NOT NULL
relationship_type_id IS NOT NULL
```

Additional semantic validation belongs in application services.

---

# 32. SELF-RELATIONSHIPS

Self-references should be prohibited by default.

Example:

```text
Application A DEPENDS_ON Application A
```

is normally invalid.

Specific exceptions must be explicitly defined.

---

# 33. DUPLICATE RELATIONSHIPS

Duplicate active relationships should normally be prevented.

A unique logical key may be:

```text
source_object
+
target_object
+
relationship_type
```

Historical versions require additional temporal handling.

---

# 34. TEMPORAL VALIDITY

Relationships and important objects may require:

```text
valid_from
valid_to
```

This supports historical and future-state architecture.

---

# 35. CURRENT STATE

A relationship with:

```text
valid_to IS NULL
```

may represent current validity where this convention is adopted.

The exact temporal model will be standardized in BUILD-03.

---

# 36. SOFT DELETE

Governed architecture objects should generally not be physically deleted.

Instead use:

```text
RETIRED
ARCHIVED
```

or another controlled lifecycle state.

---

# 37. HARD DELETE

Hard deletion should be limited to:

```text
technical cleanup
invalid test data
explicitly approved data removal
```

It must never be used casually for governed architecture records.

---

# 38. AUDIT FIELDS

Core tables should include:

```text
created_at
created_by
updated_at
updated_by
```

Where required, additional audit data will be stored separately.

---

# 39. AUDIT RECORD

Conceptual table:

```text
audit_record
```

Fields:

```text
id
timestamp
actor_type
actor_reference
action
entity_type
entity_id
request_id
before_data
after_data
source
```

Sensitive information must be handled according to security policy.

---

# 40. AUDIT ACTIONS

Examples:

```text
CREATE
UPDATE
RETIRE
ARCHIVE
RESTORE
RELATE
UNRELATE
IMPORT
EXPORT
APPROVE
REJECT
```

Approval and rejection become workflow concerns in BUILD-04.

---

# 41. EVIDENCE

Architecture decisions and important objects may require evidence.

Conceptual table:

```text
evidence_record
```

Fields:

```text
id
title
description
evidence_type
source_system_id
source_reference
uri
hash
created_at
created_by
classification_id
```

---

# 42. EVIDENCE PRINCIPLE

Evidence should support:

```text
CLAIM
DECISION
RISK
REQUIREMENT
ARCHITECTURE OBJECT
```

The evidence model must preserve provenance.

---

# 43. OBJECT-EVIDENCE RELATIONSHIP

Conceptual table:

```text
object_evidence
```

Fields:

```text
object_id
evidence_id
relationship_type
```

This allows one evidence item to support multiple architecture objects.

---

# 44. TAGS

Tags provide flexible classification without replacing the formal metamodel.

Conceptual tables:

```text
tag
object_tag
```

Examples:

```text
strategic
critical
cloud
legacy
regulated
migration
```

---

# 45. TAG PRINCIPLE

Tags are:

```text
FLEXIBLE METADATA
```

They are not substitutes for:

```text
OBJECT TYPE
RELATIONSHIP TYPE
LIFECYCLE
CLASSIFICATION
```

---

# 46. CUSTOM METADATA

The repository may need extensible metadata.

BUILD-02 should prepare for:

```text
attribute definitions
attribute values
```

without allowing arbitrary uncontrolled database schema changes.

---

# 47. METADATA TABLES

Conceptual:

```text
attribute_definition
attribute_value
```

BUILD-03 will define the formal metamodel behavior.

---

# 48. JSONB

PostgreSQL `jsonb` may be used for controlled extensibility.

It should not become a replacement for core relational structure.

Use relational columns for:

```text
identity
ownership
lifecycle
classification
relationships
timestamps
```

Use JSONB only for genuinely extensible attributes.

---

# 49. NORMALIZATION

Core repository data should be normalized sufficiently to avoid:

```text
duplicate truth
inconsistent values
update anomalies
```

Denormalized reporting structures may be introduced later.

---

# 50. REFERENTIAL INTEGRITY

Foreign keys should be used for governed relationships.

Example:

```text
object_relationship.source_object_id
→ architecture_object.id
```

---

# 51. DELETE BEHAVIOR

Foreign key delete behavior shall be explicit.

For governed records:

```text
RESTRICT
```

is generally preferred over cascading deletion.

---

# 52. DATABASE CONSTRAINTS

Use constraints for:

```text
NOT NULL
UNIQUE
CHECK
FOREIGN KEY
```

Business rules that require contextual logic belong in application services.

---

# 53. INDEXING

Initial indexes should cover:

```text
reference_id
object_type
status
lifecycle_state_id
owner_id
classification_id
source_system_id
created_at
updated_at
```

---

# 54. RELATIONSHIP INDEXES

The relationship table should index:

```text
source_object_id
target_object_id
relationship_type_id
```

Composite indexes should be added for common graph and impact queries.

---

# 55. SEARCH INDEXES

Text search requirements may use PostgreSQL capabilities initially.

Possible fields:

```text
name
description
reference_id
```

More advanced semantic search belongs to later AI/knowledge phases.

---

# 56. DATABASE PERFORMANCE

Do not optimize prematurely.

First establish:

```text
CORRECTNESS
REFERENTIAL INTEGRITY
TRACEABILITY
```

Then optimize using measured workload.

---

# 57. REPOSITORY SERVICE

The repository service provides controlled operations:

```text
CREATE
READ
UPDATE
RETIRE
ARCHIVE
RESTORE
SEARCH
RELATE
UNRELATE
```

---

# 58. CREATE OBJECT

Create must validate:

```text
object_type
name
owner
classification
lifecycle
source
```

according to the applicable object rules.

---

# 59. UPDATE OBJECT

Updates shall:

```text
validate
authorize
persist
audit
```

Material changes will later trigger workflow rules.

---

# 60. RETIRE OBJECT

Retirement shall be controlled.

It should check:

```text
DEPENDENCIES
ACTIVE RELATIONSHIPS
OPEN RISKS
OPEN PROJECTS
GOVERNANCE REQUIREMENTS
```

Full impact validation belongs to later builds.

---

# 61. SEARCH

Repository search should support:

```text
reference_id
name
object_type
status
owner
classification
tag
source
```

---

# 62. RELATE

Relationship creation shall validate:

```text
source exists
target exists
relationship type exists
relationship allowed
duplicate not active
```

---

# 63. UNRELATE

Unrelating should normally preserve history.

Prefer:

```text
valid_to
status
```

over physical deletion.

---

# 64. REPOSITORY API

Initial API structure:

```text
/api/v1/repository/objects
/api/v1/repository/objects/{id}
/api/v1/repository/relationships
/api/v1/repository/search
```

---

# 65. OBJECT API

Conceptual operations:

```text
GET
POST
PATCH
```

Deletion endpoints should not be exposed by default.

Retirement should use an explicit lifecycle operation.

---

# 66. RELATIONSHIP API

Conceptual operations:

```text
GET relationships
POST relationship
PATCH relationship
```

Relationship deletion should normally mean controlled invalidation rather than physical deletion.

---

# 67. PAGINATION

List endpoints shall use pagination.

Avoid returning unlimited repository contents.

Recommended parameters:

```text
page
page_size
```

or cursor-based pagination for later high-volume use.

---

# 68. SORTING

Search APIs should allow controlled sorting by fields such as:

```text
name
created_at
updated_at
status
```

Sort fields must be allow-listed.

---

# 69. FILTERING

Filtering should be explicit and validated.

Avoid accepting arbitrary SQL expressions through API parameters.

---

# 70. API RESPONSE MODEL

Repository responses should expose:

```text
id
reference_id
object_type
name
description
status
lifecycle
owner
classification
timestamps
```

Internal database implementation details should remain internal.

---

# 71. ETAG / VERSION SUPPORT

The repository should prepare for optimistic concurrency.

A version field may be used:

```text
version_number
```

or equivalent.

---

# 72. OPTIMISTIC CONCURRENCY

If two users modify the same object:

```text
USER A READ v3
USER B READ v3

USER A UPDATE → v4

USER B UPDATE based on v3
→ CONFLICT
```

The second update should not silently overwrite the first.

---

# 73. IMPORT FOUNDATION

BUILD-02 shall prepare for controlled import.

Import flow:

```text
SOURCE
 ↓
VALIDATE
 ↓
NORMALIZE
 ↓
MATCH
 ↓
CREATE / UPDATE
 ↓
AUDIT
```

---

# 74. IMPORT IDENTIFICATION

Imported objects should use:

```text
source_system
+
source_reference
```

to support reconciliation.

---

# 75. IMPORT DUPLICATES

Potential duplicate objects should be identified before creating new records.

The system may classify:

```text
NEW
MATCHED
POSSIBLE DUPLICATE
CONFLICT
```

Detailed matching belongs to later integration work.

---

# 76. DATA QUALITY

Initial repository quality checks:

```text
MISSING OWNER
MISSING TYPE
MISSING NAME
INVALID LIFECYCLE
INVALID CLASSIFICATION
BROKEN RELATIONSHIP
DUPLICATE REFERENCE
STALE SOURCE
```

---

# 77. DATA QUALITY STATUS

A quality issue should be represented as:

```text
OPEN
ACKNOWLEDGED
IN_REVIEW
RESOLVED
WONT_FIX
```

Detailed quality services belong to later phases.

---

# 78. REPOSITORY VALIDATION

The repository shall validate:

```text
STRUCTURAL VALIDITY
REFERENTIAL VALIDITY
SEMANTIC VALIDITY
DATA QUALITY
```

BUILD-02 focuses primarily on structural and referential validity.

---

# 79. MIGRATION STRATEGY

Every schema change shall be an Alembic migration.

Example sequence:

```text
001_initial_schema
002_lifecycle
003_relationships
004_evidence
```

Actual migration numbers may differ during implementation.

---

# 80. MIGRATION TESTING

Each migration should be tested for:

```text
UPGRADE
DOWNGRADE WHERE SUPPORTED
REPEATABILITY
DATA PRESERVATION
```

Production downgrade procedures must be treated carefully.

---

# 81. SEED DATA

The foundation may include controlled seed data for:

```text
LIFECYCLE STATES
CLASSIFICATIONS
SYSTEM STATUS
RELATIONSHIP TYPES
```

Seed data must be version controlled.

---

# 82. REFERENCE DATA

Reference data shall be distinguishable from user-created data.

This is important for migration and deployment consistency.

---

# 83. DATABASE INITIALIZATION

The documented sequence is:

```text
CREATE DATABASE
 ↓
CREATE SCHEMA
 ↓
RUN MIGRATIONS
 ↓
LOAD REFERENCE DATA
 ↓
VERIFY
```

---

# 84. BACKUP

Repository backup must include:

```text
DATABASE
MIGRATION STATE
CONFIGURATION REFERENCE
```

Secrets must be handled separately.

---

# 85. RESTORE TEST

A database backup is accepted only after successful restore testing.

The test should verify:

```text
OBJECTS
RELATIONSHIPS
AUDIT
REFERENCE DATA
```

---

# 86. DATA RETENTION

Retention rules shall be configurable and governed.

Governed architecture history should not be removed merely to reduce database size.

---

# 87. ARCHIVE

Archived data may be moved to lower-cost storage only if:

```text
TRACEABILITY
RETRIEVAL
AUDIT
```

remain available.

---

# 88. SECURITY

Database access shall follow least privilege.

Application users should not receive unrestricted administrative database privileges.

---

# 89. DATABASE ROLES

At minimum consider:

```text
application_runtime
migration_runner
read_only_reporting
administration
```

The exact implementation depends on deployment architecture.

---

# 90. ENCRYPTION

Use encryption:

```text
IN TRANSIT
AT REST
```

where supported by the deployment environment and security policy.

---

# 91. SENSITIVE DATA

The repository may contain sensitive architecture information.

Therefore:

```text
CLASSIFICATION
+
AUTHORIZATION
+
AUDIT
```

must eventually govern access.

---

# 92. REPOSITORY ACCESS MODEL

Conceptual authorization:

```text
USER
 ↓
ROLE / PERMISSION
 ↓
OBJECT / DOMAIN
 ↓
ACTION
```

Detailed RBAC/ABAC is implemented in later governance/security work.

---

# 93. DATABASE TEST SUITE

Tests should cover:

```text
CREATE OBJECT
READ OBJECT
UPDATE OBJECT
RETIRE OBJECT
CREATE RELATIONSHIP
INVALID RELATIONSHIP
DUPLICATE RELATIONSHIP
FOREIGN KEY
CLASSIFICATION
LIFECYCLE
AUDIT
CONCURRENCY
```

---

# 94. API TEST SUITE

API tests should cover:

```text
POST object
GET object
PATCH object
GET collection
SEARCH
POST relationship
INVALID INPUT
NOT FOUND
CONFLICT
```

---

# 95. NEGATIVE TESTING

The system must prove that invalid operations fail safely.

Examples:

```text
missing required field
invalid UUID
unknown object type
unknown lifecycle
unknown classification
self relationship
duplicate relationship
unauthorized write
```

---

# 96. PERFORMANCE BASELINE

BUILD-02 should establish a baseline for:

```text
object creation
object retrieval
search
relationship retrieval
relationship creation
```

No production performance target should be invented without workload evidence.

---

# 97. REPOSITORY HEALTH

A basic repository health check should report:

```text
DATABASE CONNECTIVITY
MIGRATION VERSION
OBJECT COUNT
RELATIONSHIP COUNT
FAILED QUALITY CHECKS
```

---

# 98. REPOSITORY STATISTICS

Statistics may include:

```text
objects by type
objects by lifecycle
objects by status
relationships by type
objects by source
objects by classification
```

These become inputs to later dashboards.

---

# 99. TRACEABILITY

Each repository object should ultimately be traceable to:

```text
SOURCE
OWNER
LIFECYCLE
RELATIONSHIPS
EVIDENCE
AUDIT
```

where applicable.

---

# 100. REPOSITORY AND KNOWLEDGE GRAPH

BUILD-02 stores the authoritative structured relationship model.

BUILD-06 may project or synchronize this data into a graph representation.

Therefore:

```text
DATABASE
→ authoritative persistence

KNOWLEDGE GRAPH
→ connected analysis representation
```

The graph must not silently become a competing source of truth.

---

# 101. REPOSITORY AND AI

AI services introduced later shall consume governed repository information.

AI must not directly modify repository data without authorized service operations.

The preferred chain is:

```text
AI
 ↓
APPLICATION SERVICE
 ↓
REPOSITORY
 ↓
DATABASE
```

---

# 102. REPOSITORY AND WORKFLOW

BUILD-04 will introduce workflow controls around material changes.

BUILD-02 provides the persistence required to record:

```text
DRAFT
APPROVED
RETIRED
```

and associated history.

---

# 103. REPOSITORY AND AUDIT

Repository changes shall be auditable.

The minimum requirement is to identify:

```text
WHO
WHAT
WHEN
```

Detailed governance adds:

```text
WHY
APPROVAL
EVIDENCE
```

---

# 104. DOMAIN OBJECT CATEGORIES

The repository foundation should be capable of storing:

```text
STRATEGY
CAPABILITY
VALUE STREAM
BUSINESS PROCESS
ORGANIZATION
ROLE
APPLICATION
SERVICE
DATA
TECHNOLOGY
INTERFACE
PROJECT
INITIATIVE
RISK
CONTROL
DECISION
PRINCIPLE
STANDARD
REQUIREMENT
```

The formal definitions belong to BUILD-03.

---

# 105. OBJECT EXTENSIBILITY

The architecture must allow additional object types without redesigning the entire database.

This is one reason to separate:

```text
object identity
object type
object attributes
```

---

# 106. METAMODEL PREPARATION

BUILD-02 establishes the generic persistence primitives needed by BUILD-03:

```text
OBJECT
TYPE
ATTRIBUTE
RELATIONSHIP
RELATIONSHIP TYPE
LIFECYCLE
CLASSIFICATION
OWNER
SOURCE
EVIDENCE
```

---

# 107. REPOSITORY SERVICE BOUNDARY

Later components must use repository services rather than direct SQL wherever practical.

```text
DOMAIN / SERVICE
        ↓
REPOSITORY INTERFACE
        ↓
DATABASE IMPLEMENTATION
```

This preserves replaceability.

---

# 108. NO DIRECT DATABASE ACCESS FROM UI

The UI shall never access PostgreSQL directly.

The correct path is:

```text
UI
 ↓
API
 ↓
APPLICATION SERVICE
 ↓
REPOSITORY
 ↓
DATABASE
```

---

# 109. NO DIRECT DATABASE ACCESS FROM AI

AI and agents shall not receive unrestricted database credentials.

The correct path is:

```text
AI / AGENT
 ↓
AUTHORIZED TOOL
 ↓
APPLICATION SERVICE
 ↓
REPOSITORY
 ↓
DATABASE
```

---

# 110. DATABASE CHANGE GOVERNANCE

A database change must identify:

```text
WHY
WHAT
IMPACT
MIGRATION
ROLLBACK
TEST
OWNER
```

---

# 111. SCHEMA VERSION

The application should expose the active migration/schema version for operational diagnostics.

---

# 112. DATA MODEL DOCUMENTATION

The repository shall document:

```text
TABLES
COLUMNS
KEYS
RELATIONSHIPS
INDEXES
CONSTRAINTS
ENUMERATIONS
```

An ERD should be generated or maintained as the schema evolves.

---

# 113. ENTITY RELATIONSHIP MODEL

Initial conceptual ERD:

```text
ARCHITECTURE_OBJECT
        │
        ├───────────────< OBJECT_RELATIONSHIP >───────────────┐
        │                                                      │
        ├── LIFECYCLE_STATE                                   │
        ├── CLASSIFICATION                                    │
        ├── OWNER_REFERENCE                                    │
        └── SOURCE_SYSTEM                                     │
                                                               │
                                                               └── ARCHITECTURE_OBJECT

ARCHITECTURE_OBJECT
        │
        └───────────────< OBJECT_EVIDENCE >── EVIDENCE_RECORD

ARCHITECTURE_OBJECT
        │
        └───────────────< OBJECT_TAG >──────── TAG
```

This is the foundation, not the final complete metamodel.

---

# 114. DATABASE SCHEMA EVOLUTION

The schema shall evolve incrementally:

```text
BUILD-02
→ repository primitives

BUILD-03
→ formal metamodel

BUILD-04
→ workflow/governance persistence

BUILD-05
→ integration persistence

BUILD-06
→ graph support

BUILD-07
→ analytics/decision persistence

BUILD-08
→ AI/agent persistence

BUILD-09
→ adaptive persistence
```

---

# 115. BUILD-02 DELIVERABLES

BUILD-02 shall produce:

1. PostgreSQL schema
2. `ea_imeta` schema namespace
3. architecture object persistence
4. identifier model
5. lifecycle model
6. classification model
7. ownership foundation
8. source-system model
9. relationship model
10. evidence model
11. tag model
12. metadata extension foundation
13. audit foundation
14. repository service
15. repository API
16. migrations
17. indexes
18. constraints
19. reference data
20. repository tests
21. API tests
22. database documentation
23. ERD
24. backup/restore verification
25. BUILD-02 acceptance report

---

# 116. BUILD-02 ACCEPTANCE CRITERIA

BUILD-02 is accepted when:

```text
[ ] PostgreSQL database is operational
[ ] ea_imeta schema exists
[ ] migrations execute successfully
[ ] reference data is loaded
[ ] architecture object can be created
[ ] architecture object can be retrieved
[ ] architecture object can be updated
[ ] architecture object can be retired
[ ] relationships can be created
[ ] invalid relationships are rejected
[ ] duplicate active relationships are prevented
[ ] lifecycle is persisted
[ ] classification is persisted
[ ] ownership is persisted
[ ] source provenance is persisted
[ ] evidence can be linked
[ ] tags can be linked
[ ] audit foundation records changes
[ ] API endpoints operate
[ ] pagination operates
[ ] search operates
[ ] concurrency protection operates
[ ] backup succeeds
[ ] restore succeeds
[ ] automated tests pass
```

---

# 117. BUILD-02 QUALITY GATE

The repository must pass four gates:

```text
STRUCTURAL
    ↓
REFERENTIAL
    ↓
SECURITY
    ↓
OPERATIONAL
```

---

# 118. STRUCTURAL GATE

Verify:

```text
schema
tables
columns
constraints
indexes
migrations
```

---

# 119. REFERENTIAL GATE

Verify:

```text
foreign keys
relationships
ownership
source references
evidence links
```

---

# 120. SECURITY GATE

Verify:

```text
least privilege
classification
authorization boundary
no secrets in database scripts
audit
```

---

# 121. OPERATIONAL GATE

Verify:

```text
backup
restore
health
migration
logging
monitoring
performance baseline
```

---

# 122. BUILD-02 RISKS

Known risks:

```text
OVER-GENERIC OBJECT MODEL
PREMATURE METAMODEL COMPLEXITY
POOR IDENTIFIER DESIGN
UNCONTROLLED JSONB
MISSING AUDIT
WEAK RELATIONSHIP SEMANTICS
DATABASE COUPLING
POOR MIGRATION DISCIPLINE
```

---

# 123. RISK MITIGATION

Mitigation:

```text
STABLE CORE PRIMITIVES
+
FORMAL METAMODEL IN BUILD-03
+
UUID IDENTITY
+
CONTROLLED EXTENSIBILITY
+
AUDIT
+
RELATIONSHIP CATALOGUE
+
REPOSITORY ABSTRACTION
+
VERSIONED MIGRATIONS
```

---

# 124. CRITICAL DESIGN DECISION

The database should not attempt to encode every future EA-IMETA rule immediately.

BUILD-02 establishes a stable persistence foundation.

BUILD-03 will formalize the metamodel.

This separation prevents the database from becoming an unmaintainable monolith.

---

# 125. CRITICAL REPOSITORY RULE

The repository is authoritative for governed architecture information, but it is not necessarily authoritative for every operational fact in the enterprise.

Where another system is the operational system of record:

```text
SOURCE SYSTEM
→ operational truth

EA-IMETA
→ architecture representation + governance context
```

The distinction must remain explicit.

---

# 126. CRITICAL HISTORY RULE

Architecture history shall be preserved where required.

Do not destroy historical state merely because a newer version exists.

The platform must support:

```text
CURRENT
+
HISTORICAL
+
FUTURE
+
SCENARIO
```

as later capabilities mature.

---

# 127. CRITICAL RELATIONSHIP RULE

Relationships are first-class architecture information.

They must be:

```text
TYPED
DIRECTED
OWNED WHERE REQUIRED
TRACEABLE
TEMPORALLY VALID
AUDITABLE
```

---

# 128. CRITICAL DATA QUALITY RULE

The repository shall never silently convert:

```text
UNKNOWN
```

into:

```text
KNOWN
```

Missing data must remain identifiable as missing.

---

# 129. FINAL BUILD-02 PRINCIPLES

1. Establish one governed repository.
2. Use stable technical identifiers.
3. Separate technical IDs from human reference IDs.
4. Make relationships first-class.
5. Preserve source provenance.
6. Preserve history.
7. Control lifecycle.
8. Control classification.
9. Record ownership.
10. Enforce referential integrity.
11. Version all schema changes.
12. Keep extensibility controlled.
13. Separate repository services from database implementation.
14. Never allow UI direct database access.
15. Never allow AI direct unrestricted database access.
16. Treat audit as distinct from ordinary logging.
17. Test backup and restore.
18. Build quality checks from the beginning.
19. Keep the repository authoritative for governed architecture information.
20. Prepare the repository for the formal metamodel in BUILD-03.

---

# 130. BUILD-02 COMPLETION STATEMENT

EA-IMETA-BUILD-02 establishes the authoritative repository and database foundation for the EA-IMETA platform.

The physical build now progresses from:

```text
TECHNICAL FOUNDATION
```

to:

```text
GOVERNED ARCHITECTURE INFORMATION
```

The next build will define how the repository understands architecture objects, types, attributes and semantics.

Therefore:

> BUILD THE REPOSITORY AS THE FOUNDATION OF ARCHITECTURE TRUTH; BUILD THE METAMODEL AS THE LANGUAGE THAT GIVES THAT TRUTH MEANING.

---

# END OF EA-IMETA-BUILD-02
## REPOSITORY & DATABASE
## COMPLETE
