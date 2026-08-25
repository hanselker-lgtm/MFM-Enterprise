# EA-IMETA-IMPLEMENTATION-02
# METAMODEL & REPOSITORY SPECIFICATION

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Previous Phase: EA-IMETA-IMPLEMENTATION-01 – Foundation

---

# 1. PURPOSE

EA-IMETA-IMPLEMENTATION-02 defines the concrete logical and physical foundation for the EA-IMETA architecture repository.

Phase 1 established:

- governance
- initial metamodel
- object catalogue
- relationship catalogue
- identifiers
- lifecycle
- repository baseline
- security baseline

Phase 2 converts those foundations into a concrete repository specification.

The purpose is to define:

- logical data model
- repository entities
- attributes
- primary keys
- foreign keys
- relationships
- audit information
- lifecycle management
- validation
- versioning
- evidence
- access requirements
- repository APIs
- database implementation principles

The central principle is:

> THE EA-IMETA REPOSITORY SHALL PROVIDE ONE TRUSTED, TRACEABLE AND GOVERNED STRUCTURED REPRESENTATION OF THE ENTERPRISE ARCHITECTURE.

---

# 2. SCOPE

This document covers the minimum repository required for the first operational EA-IMETA implementation.

It includes:

1. repository architecture
2. database model
3. core entities
4. metadata
5. relationship model
6. lifecycle
7. audit
8. evidence
9. validation
10. search
11. API requirements
12. security requirements
13. implementation sequence
14. acceptance criteria

It does not yet implement:

- enterprise-wide data population
- advanced analytics
- Knowledge Graph production services
- AI architecture agents
- autonomous actions

Those belong to later implementation phases.

---

# 3. REPOSITORY ARCHITECTURE

The repository shall consist of the following logical layers:

```text
USER / APPLICATION
        ↓
REPOSITORY API
        ↓
APPLICATION SERVICE
        ↓
DOMAIN MODEL
        ↓
RELATIONAL DATA MODEL
        ↓
AUDIT / HISTORY
        ↓
EVIDENCE
```

Optional later layer:

```text
RELATIONAL REPOSITORY
        ↓
KNOWLEDGE GRAPH
```

The relational repository remains the authoritative operational source during the initial implementation.

---

# 4. REPOSITORY PRINCIPLES

## 4.1 Single logical source

The repository shall provide one logical source of truth for governed architecture information.

## 4.2 Stable identity

Object identity shall remain stable throughout the object's lifecycle.

## 4.3 Separation of identity and version

Changing an object does not create a new identity.

## 4.4 Traceability

Material objects and relationships shall be traceable.

## 4.5 Explicit ownership

Governed objects shall have accountable ownership.

## 4.6 Controlled lifecycle

Objects shall follow defined lifecycle states.

## 4.7 Auditability

Material changes shall be auditable.

## 4.8 Extensibility

The repository shall allow additional object types without redesigning the entire system.

## 4.9 Security

Access shall be controlled according to role and classification.

## 4.10 Technology neutrality

The logical model shall remain independent of a specific database vendor.

---

# 5. LOGICAL DATA MODEL

The core model is:

```text
ARCHITECTURE_OBJECT
        |
        +---- OBJECT_METADATA
        |
        +---- OBJECT_VERSION
        |
        +---- OBJECT_RELATIONSHIP
        |
        +---- OBJECT_OWNER
        |
        +---- OBJECT_EVIDENCE
        |
        +---- OBJECT_TAG
        |
        +---- OBJECT_CLASSIFICATION
        |
        +---- OBJECT_LIFECYCLE
```

Governance:

```text
ARCHITECTURE_OBJECT
        |
        +---- DECISION
        +---- REQUIREMENT
        +---- CONTROL
        +---- RISK
        +---- EXCEPTION
```

Transformation:

```text
ARCHITECTURE_OBJECT
        |
        +---- INITIATIVE
        +---- PROGRAM
        +---- PROJECT
        +---- ROADMAP
        +---- BENEFIT
        +---- OUTCOME
```

---

# 6. CORE ENTITY STRATEGY

The repository shall use a hybrid model.

A common `architecture_object` table provides:

- identity
- common metadata
- lifecycle
- ownership
- classification

Domain-specific tables provide specialized attributes.

This avoids two extremes:

### Extreme A – One giant table

Too generic and difficult to validate.

### Extreme B – Completely independent tables

Creates duplication and makes cross-domain traceability difficult.

The recommended model is:

```text
COMMON OBJECT CORE
        +
DOMAIN-SPECIFIC EXTENSIONS
```

---

# 7. CORE TABLE: ARCHITECTURE_OBJECT

## 7.1 Purpose

Stores the common identity and governance information for every architecture object.

## 7.2 Logical structure

```text
architecture_object
-----------------------------
object_id
object_type_id
name
description
owner_id
lifecycle_status_id
classification_id
source_id
confidence_level
created_at
created_by
updated_at
updated_by
version_no
is_active
```

## 7.3 Primary key

```text
object_id
```

## 7.4 Requirements

`object_id` shall never be reused.

---

# 8. OBJECT_TYPE

## 8.1 Purpose

Defines the type of architecture object.

## 8.2 Fields

```text
object_type_id
code
name
description
domain
is_core
is_active
created_at
updated_at
```

## 8.3 Initial values

Examples:

```text
STRATEGY
OBJECTIVE
CAPABILITY
VALUE_STREAM
PROCESS
SERVICE
INFORMATION_OBJECT
DATA_PRODUCT
APPLICATION
APPLICATION_COMPONENT
INTERFACE
API
PLATFORM
TECHNOLOGY
INFRASTRUCTURE_COMPONENT
REQUIREMENT
CONTROL
RISK
DECISION
PRINCIPLE
STANDARD
PATTERN
INITIATIVE
PROGRAM
PROJECT
ROADMAP
BENEFIT
OUTCOME
ARCHITECTURE_STATE
ARCHITECTURE_ASSESSMENT
ARCHITECTURE_OBSERVATION
EVIDENCE
ARCHITECTURE_EXCEPTION
```

AI-specific types are reserved for later phases.

---

# 9. OBJECT DOMAIN EXTENSIONS

Domain-specific tables shall use `object_id` as their primary and foreign key.

Examples:

```text
capability
process
service
application
technology
risk
decision
initiative
```

This allows:

```text
architecture_object.object_id
        =
capability.object_id
```

---

# 10. CAPABILITY ENTITY

## 10.1 Table

```text
capability
```

## 10.2 Fields

```text
object_id
capability_level
business_owner_id
strategic_importance
criticality
maturity_level
target_maturity
```

## 10.3 Purpose

Represents what the enterprise must be able to do.

---

# 11. PROCESS ENTITY

## 11.1 Table

```text
process
```

## 11.2 Fields

```text
object_id
process_level
process_owner_id
process_category
criticality
automation_level
```

---

# 12. SERVICE ENTITY

## 12.1 Table

```text
service
```

## 12.2 Fields

```text
object_id
service_type
service_owner_id
service_level
criticality
availability_target
```

---

# 13. APPLICATION ENTITY

## 13.1 Table

```text
application
```

## 13.2 Fields

```text
object_id
application_type
business_owner_id
technical_owner_id
lifecycle_state
criticality
vendor
version
deployment_model
```

---

# 14. TECHNOLOGY ENTITY

## 14.1 Table

```text
technology
```

## 14.2 Fields

```text
object_id
technology_category
vendor
product
version
technology_lifecycle
technical_owner_id
criticality
```

---

# 15. INFORMATION OBJECT ENTITY

## 15.1 Table

```text
information_object
```

## 15.2 Fields

```text
object_id
information_domain
data_owner_id
sensitivity
criticality
retention_category
```

---

# 16. RISK ENTITY

## 16.1 Table

```text
risk
```

## 16.2 Fields

```text
object_id
risk_category
likelihood
impact
risk_score
risk_owner_id
treatment
residual_risk
review_date
```

---

# 17. REQUIREMENT ENTITY

## 17.1 Table

```text
requirement
```

## 17.2 Fields

```text
object_id
requirement_type
source
priority
mandatory_flag
compliance_domain
```

---

# 18. CONTROL ENTITY

## 18.1 Table

```text
control
```

## 18.2 Fields

```text
object_id
control_type
control_owner_id
control_frequency
effectiveness
test_date
```

---

# 19. DECISION ENTITY

## 19.1 Table

```text
decision
```

## 19.2 Fields

```text
object_id
decision_type
decision_status
decision_authority
decision_date
rationale
```

---

# 20. INITIATIVE ENTITY

## 20.1 Table

```text
initiative
```

## 20.2 Fields

```text
object_id
initiative_type
sponsor_id
priority
investment
start_date
target_date
status
```

---

# 21. OBJECT RELATIONSHIP

## 21.1 Purpose

Stores relationships between architecture objects.

## 21.2 Table

```text
object_relationship
```

## 21.3 Fields

```text
relationship_id
source_object_id
target_object_id
relationship_type_id
relationship_status
confidence_level
effective_from
effective_to
created_at
created_by
updated_at
updated_by
```

## 21.4 Primary key

```text
relationship_id
```

## 21.5 Foreign keys

```text
source_object_id → architecture_object.object_id
target_object_id → architecture_object.object_id
relationship_type_id → relationship_type.relationship_type_id
```

---

# 22. RELATIONSHIP TYPE

## 22.1 Table

```text
relationship_type
```

## 22.2 Fields

```text
relationship_type_id
code
name
description
inverse_name
allowed_source_type
allowed_target_type
is_active
```

## 22.3 Initial relationships

```text
OWNS
SUPPORTS
ENABLES
DEPENDS_ON
IMPLEMENTS
REALIZES
CONSUMES
PRODUCES
CONTAINS
INTEGRATES_WITH
GOVERNED_BY
CONSTRAINED_BY
REPLACES
PRECEDES
FOLLOWS
AFFECTS
MITIGATES
EVIDENCED_BY
```

---

# 23. RELATIONSHIP VALIDATION

Relationships shall be validated against allowed object types.

Example:

```text
CAPABILITY
    supports
SERVICE
```

may be valid.

But:

```text
RISK
    owns
TECHNOLOGY
```

may be invalid depending on the defined semantic model.

The repository shall therefore support relationship validation rules.

---

# 24. OBJECT OWNER

Ownership shall be represented explicitly.

## Table

```text
object_owner
```

## Fields

```text
object_owner_id
object_id
person_or_role_id
ownership_type
effective_from
effective_to
```

Ownership types may include:

```text
ACCOUNTABLE
RESPONSIBLE
STEWARD
TECHNICAL_OWNER
BUSINESS_OWNER
```

---

# 25. ORGANIZATION / PERSON / ROLE

The repository shall distinguish between:

```text
Organization
Person
Role
```

This prevents architecture ownership from being tied permanently to an individual.

## Core tables

```text
organization
person
role
```

A role may remain accountable even when the person changes.

---

# 26. LIFECYCLE

## Table

```text
lifecycle_status
```

## Fields

```text
lifecycle_status_id
code
name
sequence
description
is_terminal
```

Initial states:

```text
DRAFT
REVIEW
APPROVED
ACTIVE
DEPRECATED
RETIRED
```

---

# 27. CLASSIFICATION

## Table

```text
classification
```

## Fields

```text
classification_id
code
name
description
security_level
```

The actual classification vocabulary shall align with enterprise security policy.

---

# 28. SOURCE

## Table

```text
source
```

## Fields

```text
source_id
name
source_type
system_reference
authority_level
last_verified
```

Examples:

```text
Architecture Office
Portfolio System
CMDB
Data Catalog
Security Platform
Project System
Manual Assessment
```

---

# 29. EVIDENCE

## 29.1 Purpose

Provides traceability from architecture information to supporting evidence.

## 29.2 Table

```text
evidence
```

## 29.3 Fields

```text
evidence_id
evidence_type
title
description
source_id
location_reference
confidence_level
created_at
verified_at
verified_by
```

---

# 30. OBJECT EVIDENCE

## Table

```text
object_evidence
```

## Fields

```text
object_evidence_id
object_id
evidence_id
relationship_type
```

This permits one evidence item to support multiple architecture objects.

---

# 31. TAGGING

## Table

```text
tag
```

```text
tag_id
name
description
```

Relationship:

```text
object_tag
----------------
object_id
tag_id
```

Tags may support:

- search
- reporting
- thematic views
- temporary analysis

Tags shall not replace formal object types or relationships.

---

# 32. OBJECT VERSIONING

## Table

```text
object_version
```

## Fields

```text
object_version_id
object_id
version_no
change_type
change_summary
snapshot_reference
created_at
created_by
approved_at
approved_by
```

## 32.1 Version rule

The current object remains available through `architecture_object`.

Historical versions are preserved separately.

---

# 33. AUDIT LOG

## Table

```text
audit_log
```

## Fields

```text
audit_id
entity_type
entity_id
action
old_value_reference
new_value_reference
performed_at
performed_by
reason
correlation_id
```

Actions:

```text
CREATE
UPDATE
DELETE
APPROVE
REJECT
RETIRE
RESTORE
```

---

# 34. SOFT DELETE

Material architecture objects shall not normally be physically deleted.

Instead:

```text
is_active = false
lifecycle = RETIRED
```

Historical traceability shall remain available.

---

# 35. DATABASE NORMALIZATION

The logical relational model shall follow appropriate normalization principles.

Avoid:

- repeated lists in one field
- duplicated ownership
- duplicated relationship definitions
- uncontrolled free-text classifications

Structured relationships should use dedicated tables.

---

# 36. INDEXING

The repository should index at minimum:

```text
object_id
object_type_id
name
owner_id
lifecycle_status_id
classification_id
source_id
created_at
updated_at
```

Relationship indexes:

```text
source_object_id
target_object_id
relationship_type_id
```

---

# 37. SEARCH REQUIREMENTS

Search shall support:

## Exact

```text
EA-BUS-CAP-00001
```

## Name

```text
Customer Onboarding
```

## Type

```text
CAPABILITY
```

## Owner

```text
Architecture
```

## Status

```text
ACTIVE
```

## Combined

```text
ACTIVE + CAPABILITY + Owner
```

---

# 38. TRACEABILITY QUERIES

The repository should support queries such as:

```text
Which applications support this capability?

Which technologies support this application?

Which risks affect this service?

Which initiatives change this capability?

Which requirements govern this application?

Which evidence supports this decision?
```

---

# 39. IMPACT ANALYSIS

The repository shall support:

```text
SELECT OBJECT
      ↓
FOLLOW RELATIONSHIPS
      ↓
IDENTIFY DEPENDENCIES
      ↓
CLASSIFY IMPACT
      ↓
IDENTIFY RISKS
      ↓
IDENTIFY INITIATIVES
```

Impact analysis is one of the most important reasons for maintaining structured relationships.

---

# 40. ARCHITECTURE STATE

The repository shall support explicit architecture states:

```text
CURRENT
TARGET
TRANSITION
PROPOSED
OBSERVED
SCENARIO
```

A single object may have different representations in different architecture states.

---

# 41. BASELINE

## Table

```text
architecture_baseline
```

Fields:

```text
baseline_id
name
description
baseline_type
effective_date
approved_date
approved_by
status
```

## Baseline contents

A baseline shall identify the relevant:

- objects
- relationships
- versions
- decisions

---

# 42. BASELINE MEMBERSHIP

## Table

```text
baseline_object
```

Fields:

```text
baseline_id
object_id
object_version_no
```

This ensures a baseline references an exact object version.

---

# 43. ARCHITECTURE EXCEPTION

## Table

```text
architecture_exception
```

Fields:

```text
object_id
exception_reason
risk
approval_authority
approved_date
expiry_date
status
remediation
```

An exception shall always have an owner and expiry/review mechanism.

---

# 44. VALIDATION RULE ENGINE

The repository shall support validation rules for:

- required metadata
- valid lifecycle
- ownership
- relationship semantics
- classification
- duplicate IDs
- stale objects

Rules may initially be implemented in application logic.

A formal rules engine can be introduced later.

---

# 45. API SPECIFICATION

The repository shall expose controlled APIs.

## 45.1 Object API

Conceptual operations:

```text
GET /objects
GET /objects/{id}
POST /objects
PUT /objects/{id}
PATCH /objects/{id}
```

## 45.2 Relationship API

```text
GET /objects/{id}/relationships
POST /relationships
DELETE /relationships/{id}
```

## 45.3 Search API

```text
GET /search
```

## 45.4 Impact API

```text
GET /objects/{id}/impact
```

## 45.5 Decision API

```text
GET /decisions
GET /decisions/{id}
```

## 45.6 Evidence API

```text
GET /objects/{id}/evidence
POST /evidence
```

The exact API technology shall be selected during implementation.

---

# 46. API DESIGN PRINCIPLES

APIs shall be:

- versioned
- authenticated
- authorized
- documented
- observable
- auditable

API version example:

```text
/api/v1/
```

---

# 47. ERROR HANDLING

APIs shall return structured errors.

Conceptually:

```text
400 INVALID_REQUEST
401 UNAUTHORIZED
403 FORBIDDEN
404 NOT_FOUND
409 CONFLICT
422 VALIDATION_ERROR
500 INTERNAL_ERROR
```

Errors shall not expose sensitive internal information.

---

# 48. TRANSACTION CONTROL

Changes affecting multiple objects or relationships should be atomic where practical.

Example:

```text
CREATE INITIATIVE
+
CREATE CAPABILITY RELATIONSHIP
+
CREATE OWNER
```

should either complete consistently or fail without leaving an invalid partial state.

---

# 49. CONCURRENCY

The repository should protect against conflicting updates.

Possible approaches:

- optimistic locking
- version number
- update timestamp

Recommended initial approach:

```text
version_no + updated_at
```

---

# 50. SECURITY MODEL

The repository shall support:

```text
USER
  ↓
IDENTITY
  ↓
ROLE
  ↓
PERMISSION
  ↓
OBJECT / DOMAIN
```

Permissions may include:

```text
READ
CREATE
UPDATE
APPROVE
ADMINISTER
```

---

# 51. DOMAIN ACCESS

Where required, access may be restricted by:

- architecture domain
- organization
- classification
- role
- project

The access model shall avoid unnecessary duplication of authorization logic.

---

# 52. BACKUP AND RECOVERY

The repository shall have:

- scheduled backup
- backup validation
- recovery procedure
- restoration testing

Critical architecture information shall not depend on a single storage location.

---

# 53. ENVIRONMENT MODEL

The implementation shall use:

```text
DEV
TEST
PROD
```

Schema changes shall be promoted through controlled deployment.

---

# 54. DATABASE MIGRATION

Database changes shall use version-controlled migrations.

Example:

```text
001_initial_schema
002_add_relationship_confidence
003_add_baseline
004_add_exception
```

Migrations shall be:

- repeatable where practical
- documented
- tested
- reversible where practical

---

# 55. SEED DATA

The initial deployment shall contain controlled seed data for:

- object types
- relationship types
- lifecycle statuses
- classifications
- system roles

Seed data shall be version controlled.

---

# 56. REPOSITORY QUALITY DASHBOARD

The repository should later provide quality metrics such as:

```text
Object completeness
Ownership coverage
Stale object rate
Duplicate rate
Relationship completeness
Evidence coverage
Lifecycle compliance
```

These metrics belong to later dashboard implementation but the data model shall support them.

---

# 57. PERFORMANCE BASELINE

Initial performance targets should be defined during technical implementation.

The system should support:

- normal interactive search
- object retrieval
- relationship navigation
- common traceability queries

Performance requirements shall be validated using realistic data volumes before production acceptance.

---

# 58. IMPLEMENTATION TECHNOLOGY

The logical specification does not mandate a specific technology.

A suitable implementation may use:

```text
Relational Database
+
Backend Service
+
REST API
+
Web UI
```

The implementation team shall select technology based on:

- security
- maintainability
- cost
- skills
- integration
- scalability
- supportability

The architecture shall avoid unnecessary technology complexity.

---

# 59. RECOMMENDED INITIAL TECHNICAL STACK

For a controlled first implementation, a practical stack could be:

```text
Database:
PostgreSQL

Backend:
Python

API:
FastAPI

Data Validation:
Pydantic

ORM / Data Access:
SQLAlchemy

Migrations:
Alembic

Frontend:
React or server-rendered web UI

Authentication:
Enterprise identity provider where available

Documentation:
OpenAPI
```

This is a recommendation, not a mandatory architecture decision.

The final technology selection shall be recorded as an Architecture Decision Record.

---

# 60. INITIAL DATABASE SCHEMA

The first database release should include at least:

```text
architecture_object
object_type
relationship_type
object_relationship
organization
person
role
object_owner
lifecycle_status
classification
source
evidence
object_evidence
tag
object_tag
object_version
audit_log
architecture_baseline
baseline_object
architecture_exception
```

Domain extensions:

```text
capability
process
service
application
technology
information_object
risk
requirement
control
decision
initiative
```

---

# 61. REPOSITORY PACKAGE STRUCTURE

The implementation repository may use:

```text
repository/
│
├── migrations/
├── models/
├── schemas/
├── services/
├── api/
├── validation/
├── security/
├── tests/
├── seed/
└── docs/
```

---

# 62. TESTING STRATEGY

Testing shall cover:

## Unit tests

Individual functions.

## Integration tests

Database and service interactions.

## API tests

API behavior.

## Validation tests

Metamodel and relationship rules.

## Security tests

Authorization and access control.

## Migration tests

Database upgrade paths.

## Acceptance tests

Business and architecture requirements.

---

# 63. TEST DATA

Test data shall include:

- capabilities
- processes
- applications
- technologies
- risks
- decisions
- initiatives
- relationships

Test data shall represent realistic dependencies.

---

# 64. SAMPLE TRACEABILITY SCENARIO

Example:

```text
Strategy:
Improve Customer Experience

        ↓

Objective:
Reduce onboarding time

        ↓

Capability:
Customer Onboarding

        ↓

Process:
Customer Registration

        ↓

Service:
Digital Onboarding

        ↓

Application:
Customer Portal

        ↓

Technology:
Web Platform

        ↓

Risk:
Platform Availability

        ↓

Control:
Availability Monitoring
```

This demonstrates why the repository must preserve relationships rather than isolated records.

---

# 65. REPOSITORY ACCEPTANCE CRITERIA

Phase 2 shall be considered technically complete when:

```text
[ ] Core schema implemented
[ ] Object types implemented
[ ] Relationship types implemented
[ ] IDs implemented
[ ] Lifecycle implemented
[ ] Ownership implemented
[ ] Audit implemented
[ ] Evidence implemented
[ ] Versioning implemented
[ ] Baseline implemented
[ ] Exception model implemented
[ ] Validation implemented
[ ] Search implemented
[ ] Relationship navigation implemented
[ ] Authentication implemented
[ ] Authorization implemented
[ ] API versioning established
[ ] Database migrations established
[ ] Test suite established
[ ] Backup/recovery procedure defined
```

---

# 66. PHASE 2 IMPLEMENTATION SEQUENCE

```text
STEP 1
CREATE DATABASE
      ↓
STEP 2
CREATE CORE TABLES
      ↓
STEP 3
CREATE DOMAIN TABLES
      ↓
STEP 4
CREATE RELATIONSHIPS
      ↓
STEP 5
CREATE LIFECYCLE
      ↓
STEP 6
CREATE OWNERSHIP
      ↓
STEP 7
CREATE AUDIT
      ↓
STEP 8
CREATE VALIDATION
      ↓
STEP 9
CREATE API
      ↓
STEP 10
CREATE TESTS
      ↓
STEP 11
LOAD SEED DATA
      ↓
STEP 12
ACCEPT REPOSITORY
```

---

# 67. PHASE 3 INPUT

Once Phase 2 is accepted, Phase 3 shall populate the repository.

Phase 3 shall focus on:

- initial architecture inventory
- capabilities
- processes
- applications
- technologies
- information
- risks
- initiatives
- decisions

Population shall be prioritized by business value and criticality.

---

# 68. IMPORTANT IMPLEMENTATION RULE

Do not populate thousands of objects before the repository model has been tested.

Recommended sequence:

```text
10–20 TEST OBJECTS
       ↓
VALIDATE MODEL
       ↓
50–100 PILOT OBJECTS
       ↓
VALIDATE WORKFLOWS
       ↓
CONTROLLED EXPANSION
```

This reduces rework.

---

# 69. RELATIONSHIP TO PHASE 1

Phase 2 implements the decisions established in Phase 1.

```text
IMPLEMENTATION-01
FOUNDATION
      ↓
IMPLEMENTATION-02
METAMODEL + REPOSITORY
```

Phase 2 shall not silently modify Phase 1.

Any material change shall be recorded in the implementation changelog.

---

# 70. RELATIONSHIP TO MASTER ARCHITECTURE

```text
EA-IMETA-MASTER-01
        ↓
ARCHITECTURE PRINCIPLES
        ↓
IMPLEMENTATION-01
        ↓
IMPLEMENTATION-02
        ↓
ACTUAL REPOSITORY
```

The repository is therefore an implementation of the architecture, not a replacement for it.

---

# 71. FINAL PHASE 2 PRINCIPLES

1. Keep the logical model technology neutral.
2. Use stable identifiers.
3. Separate common metadata from domain-specific attributes.
4. Model relationships explicitly.
5. Preserve history.
6. Make ownership explicit.
7. Make lifecycle explicit.
8. Link material information to evidence.
9. Validate relationships.
10. Keep the repository auditable.
11. Build APIs from the beginning.
12. Avoid premature Knowledge Graph complexity.
13. Avoid premature AI complexity.
14. Test the model before scaling data population.
15. Keep the repository authoritative for governed architecture information.

---

# 72. PHASE 2 COMPLETION STATEMENT

EA-IMETA-IMPLEMENTATION-02 defines the concrete metamodel and repository specification required to begin building the EA-IMETA architecture platform.

The specification establishes:

- core entities
- domain extensions
- identifiers
- metadata
- relationships
- ownership
- lifecycle
- evidence
- versioning
- audit
- baselines
- exceptions
- validation
- search
- API requirements
- security
- database migrations
- testing
- deployment structure

The next phase is therefore not another redesign of the repository.

The next phase is controlled **data population and validation of the implemented model**.

> FIRST BUILD THE MODEL. THEN PROVE THE MODEL WITH REAL DATA. THEN SCALE.

---

# END OF EA-IMETA-IMPLEMENTATION-02
## METAMODEL & REPOSITORY SPECIFICATION
## COMPLETE
