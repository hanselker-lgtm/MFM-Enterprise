# EA-IMETA-BUILD-03
# METAMODEL ENGINE

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Previous Build: EA-IMETA-BUILD-02 – Repository & Database
### Implementation Basis: EA-IMETA-IMPLEMENTATION-02 and EA-IMETA-IMPLEMENTATION-03

---

# 1. PURPOSE

EA-IMETA-BUILD-03 defines the physical Metamodel Engine of the EA-IMETA platform.

BUILD-01 established the technical foundation.

BUILD-02 established the authoritative repository and database.

BUILD-03 now defines the semantic engine that determines:

- what an architecture object is
- what type it belongs to
- which attributes it may contain
- which relationships are valid
- which lifecycle states apply
- which classifications are permitted
- which validation rules apply
- how the metamodel itself is governed and versioned

The central principle is:

> THE REPOSITORY STORES ARCHITECTURE INFORMATION; THE METAMODEL ENGINE DEFINES WHAT THAT INFORMATION MEANS.

---

# 2. BUILD-03 SCOPE

BUILD-03 covers:

```text
METAMODEL DEFINITIONS
OBJECT TYPES
ATTRIBUTE DEFINITIONS
RELATIONSHIP TYPES
SEMANTIC RULES
VALIDATION RULES
CARDINALITY
TYPE HIERARCHIES
OBJECT TEMPLATES
LIFECYCLE BINDINGS
CLASSIFICATION BINDINGS
METAMODEL VERSIONING
METAMODEL ACTIVATION
METAMODEL VALIDATION
METAMODEL API
METAMODEL SERVICES
IMPORT VALIDATION
QUERY SUPPORT
METAMODEL TESTING
```

It does not implement the complete workflow engine, graph engine, dashboard layer, AI layer or adaptive engine.

---

# 3. METAMODEL ROLE

The Metamodel Engine sits between repository persistence and business/architecture services.

```text
USER / API / IMPORT
        ↓
METAMODEL ENGINE
        ↓
VALIDATION / SEMANTICS
        ↓
REPOSITORY SERVICES
        ↓
DATABASE
```

The engine prevents the repository from becoming an ungoverned collection of records.

---

# 4. METAMODEL DEFINITION

A metamodel is the formal definition of:

```text
OBJECT TYPES
+
ATTRIBUTES
+
RELATIONSHIPS
+
CONSTRAINTS
+
LIFECYCLES
+
CLASSIFICATIONS
+
SEMANTIC RULES
```

---

# 5. METAMODEL PRINCIPLES

1. The metamodel is explicit.
2. The metamodel is versioned.
3. Definitions are governed.
4. Rules are machine-readable where practical.
5. Invalid structures are rejected.
6. Semantic ambiguity is minimized.
7. Extensions are controlled.
8. Backward compatibility is considered.
9. Changes are auditable.
10. A metamodel version is reproducible.

---

# 6. METAMODEL VERSION

Each metamodel definition shall belong to a version.

Example:

```text
1.0
1.1
2.0
```

Major changes may require a new major version.

Minor compatible extensions may use minor versions.

---

# 7. METAMODEL STATUS

A metamodel version may have:

```text
DRAFT
REVIEW
APPROVED
ACTIVE
SUPERSEDED
RETIRED
```

Only one approved active version should govern a given runtime scope unless explicit multi-version operation is required.

---

# 8. METAMODEL LIFECYCLE

The metamodel itself is governed:

```text
DRAFT
 ↓
REVIEW
 ↓
APPROVED
 ↓
ACTIVE
 ↓
SUPERSEDED
 ↓
RETIRED
```

The workflow engine in BUILD-04 will later enforce approval workflows.

---

# 9. METAMODEL TABLE

Conceptual table:

```text
metamodel
```

Fields:

```text
id
version
name
description
status
is_active
created_at
created_by
approved_at
approved_by
activated_at
activated_by
retired_at
retired_by
```

---

# 10. OBJECT TYPE

The object type is the central semantic classification.

Examples:

```text
STRATEGY
CAPABILITY
VALUE_STREAM
BUSINESS_PROCESS
ORGANIZATION
ROLE
APPLICATION
APPLICATION_SERVICE
DATA_ENTITY
DATA_STORE
TECHNOLOGY
TECHNOLOGY_SERVICE
INTERFACE
INTEGRATION
PROJECT
INITIATIVE
REQUIREMENT
RISK
CONTROL
DECISION
PRINCIPLE
STANDARD
POLICY
```

The catalogue shall remain extensible.

---

# 11. OBJECT TYPE TABLE

Conceptual table:

```text
metamodel_object_type
```

Fields:

```text
id
metamodel_id
code
name
description
parent_type_id
is_abstract
is_assignable
is_active
```

---

# 12. OBJECT TYPE HIERARCHY

Object types may inherit from parent types.

Example:

```text
TECHNOLOGY
   ├── OPERATING_SYSTEM
   ├── DATABASE_TECHNOLOGY
   ├── CLOUD_PLATFORM
   └── NETWORK_TECHNOLOGY
```

Inheritance should be controlled and explicit.

---

# 13. ABSTRACT TYPES

An abstract type may define shared semantics without being directly instantiated.

Example:

```text
ARCHITECTURE_COMPONENT
    ├── APPLICATION
    ├── TECHNOLOGY
    └── DATA_COMPONENT
```

`ARCHITECTURE_COMPONENT` may be abstract.

---

# 14. ASSIGNABLE TYPES

Only types marked:

```text
is_assignable = true
```

may normally be assigned to architecture objects.

---

# 15. TYPE CODE

Each type shall have a stable machine-readable code.

Example:

```text
APPLICATION
CAPABILITY
TECHNOLOGY
DATA_ENTITY
```

Codes should not be casually renamed because integrations may depend on them.

---

# 16. OBJECT TYPE METADATA

Each type may define:

```text
display_name
description
icon
color_reference
documentation_uri
owner
classification_default
lifecycle_definition
```

Presentation-specific fields should remain optional.

---

# 17. ATTRIBUTE DEFINITION

Attributes define what information an object type may contain.

Example:

```text
APPLICATION
    name
    description
    business_criticality
    lifecycle
    owner
    vendor
```

---

# 18. ATTRIBUTE TABLE

Conceptual table:

```text
metamodel_attribute
```

Fields:

```text
id
metamodel_id
object_type_id
code
name
description
data_type
is_required
is_unique
is_searchable
default_value
validation_rule
display_order
```

---

# 19. ATTRIBUTE DATA TYPES

Supported conceptual types:

```text
STRING
TEXT
INTEGER
DECIMAL
BOOLEAN
DATE
DATETIME
UUID
ENUM
REFERENCE
MULTI_REFERENCE
JSON
```

Additional types may be introduced through controlled change.

---

# 20. REQUIRED ATTRIBUTES

An attribute may be:

```text
REQUIRED
OPTIONAL
CONDITIONAL
```

Conditional requirements require a validation rule.

---

# 21. UNIQUE ATTRIBUTES

Some attributes may be unique within a type.

Example:

```text
Application reference_id
```

Uniqueness rules must define their scope.

---

# 22. DEFAULT VALUES

Default values may be defined for appropriate attributes.

Defaults shall not hide missing information.

A default such as:

```text
UNKNOWN
```

must not be treated as verified information.

---

# 23. ENUMERATIONS

Controlled value lists should be represented explicitly.

Example:

```text
business_criticality
LOW
MEDIUM
HIGH
CRITICAL
```

---

# 24. ENUM TABLE

Conceptual:

```text
metamodel_enum
metamodel_enum_value
```

Fields may include:

```text
code
label
description
sequence
is_active
```

---

# 25. REFERENCE ATTRIBUTES

A reference attribute points to another governed object.

Example:

```text
Application.owner
→ Organization
```

Reference definitions shall specify the allowed target type.

---

# 26. MULTI-REFERENCE

Some attributes may reference multiple objects.

Example:

```text
Application.supported_capabilities
→ Capability[]
```

The engine shall validate every target.

---

# 27. ATTRIBUTE CARDINALITY

Attribute cardinality may be:

```text
0..1
1..1
0..*
1..*
```

This shall be machine-readable.

---

# 28. ATTRIBUTE VALIDATION

Validation may include:

```text
MIN_LENGTH
MAX_LENGTH
MIN_VALUE
MAX_VALUE
PATTERN
ENUM
REFERENCE_TYPE
CUSTOM_RULE
```

---

# 29. ATTRIBUTE SEMANTICS

The engine should distinguish:

```text
VALUE
REFERENCE
DERIVED VALUE
SYSTEM VALUE
```

Derived values should not be confused with manually maintained values.

---

# 30. DERIVED ATTRIBUTES

A derived attribute may be calculated from other information.

Example:

```text
architecture_risk_score
```

Derived values should record their calculation source or rule.

---

# 31. RELATIONSHIP TYPE

Relationship types define legal semantic connections.

Examples:

```text
SUPPORTS
DEPENDS_ON
IMPLEMENTS
REALIZES
USES
CONSUMES
PROVIDES
OWNS
CONTAINS
GOVERNS
MITIGATES
AFFECTS
REQUIRES
REPLACES
```

---

# 32. RELATIONSHIP TYPE TABLE

Conceptual:

```text
metamodel_relationship_type
```

Fields:

```text
id
metamodel_id
code
name
description
inverse_code
is_directed
is_transitive
is_symmetric
is_active
```

---

# 33. RELATIONSHIP DIRECTION

Every relationship must define its semantic direction unless explicitly symmetric.

Example:

```text
APPLICATION
    USES
TECHNOLOGY
```

The inverse may be:

```text
TECHNOLOGY
    USED_BY
APPLICATION
```

---

# 34. INVERSE RELATIONSHIP

Where an inverse exists, it should be defined explicitly.

This improves:

```text
querying
navigation
impact analysis
graph projection
```

---

# 35. SYMMETRIC RELATIONSHIPS

A relationship may be symmetric only when meaning is identical in both directions.

Example:

```text
RELATED_TO
```

Symmetry should not be assumed.

---

# 36. TRANSITIVE RELATIONSHIPS

Some relationships may support transitive reasoning.

Example:

```text
CONTAINS
```

But transitivity must be explicitly declared.

---

# 37. RELATIONSHIP CARDINALITY

A relationship definition may specify:

```text
source_min
source_max
target_min
target_max
```

Example:

```text
Capability
1..*
SUPPORTED_BY
Application
0..*
```

---

# 38. ALLOWED SOURCE TYPES

Every relationship type may specify allowed source types.

Example:

```text
SUPPORTS
source:
APPLICATION
```

---

# 39. ALLOWED TARGET TYPES

The same relationship defines allowed target types.

Example:

```text
SUPPORTS
target:
CAPABILITY
```

---

# 40. RELATIONSHIP MATRIX

The engine should support a machine-readable relationship matrix.

Example:

```text
SOURCE              RELATIONSHIP       TARGET
------------------------------------------------
APPLICATION         SUPPORTS           CAPABILITY
APPLICATION         USES               TECHNOLOGY
APPLICATION         STORES             DATA_ENTITY
CAPABILITY          REALIZES           VALUE_STREAM
PROJECT             CHANGES            APPLICATION
CONTROL             MITIGATES          RISK
```

---

# 41. SEMANTIC RULES

A semantic rule determines whether a combination of objects, attributes or relationships is meaningful.

Examples:

```text
APPLICATION must have an owner
RETIRED APPLICATION cannot receive new dependencies
CONTROL must mitigate at least one risk
```

---

# 42. RULE TABLE

Conceptual:

```text
metamodel_rule
```

Fields:

```text
id
metamodel_id
code
name
description
rule_type
severity
expression
is_blocking
is_active
```

---

# 43. RULE TYPES

Initial types:

```text
ATTRIBUTE_RULE
REFERENCE_RULE
RELATIONSHIP_RULE
CARDINALITY_RULE
LIFECYCLE_RULE
CLASSIFICATION_RULE
CONSISTENCY_RULE
```

---

# 44. RULE SEVERITY

Rules may produce:

```text
INFO
WARNING
ERROR
BLOCKING
```

A blocking rule prevents persistence.

---

# 45. VALIDATION RESULT

A validation result should contain:

```text
rule_id
object_id
severity
message
path
status
created_at
```

---

# 46. VALIDATION STATUS

Use:

```text
PASS
WARNING
FAIL
NOT_EVALUATED
```

`NOT_EVALUATED` must not be treated as `PASS`.

---

# 47. VALIDATION ENGINE

The validation engine should operate:

```text
INPUT
 ↓
TYPE VALIDATION
 ↓
ATTRIBUTE VALIDATION
 ↓
REFERENCE VALIDATION
 ↓
RELATIONSHIP VALIDATION
 ↓
SEMANTIC VALIDATION
 ↓
RESULT
```

---

# 48. VALIDATION CONTEXT

Validation may require context:

```text
METAMODEL VERSION
USER
ORGANIZATION
LIFECYCLE STATE
CLASSIFICATION
DATE
SOURCE
```

Context should be explicit.

---

# 49. VALIDATION MODES

Support:

```text
CREATE
UPDATE
IMPORT
PUBLISH
MIGRATION
FULL REVALIDATION
```

Different operations may invoke different rule sets.

---

# 50. CREATE VALIDATION

At create:

```text
TYPE
REQUIRED ATTRIBUTES
DEFAULTS
REFERENCES
CLASSIFICATION
OWNER
```

must be checked.

---

# 51. UPDATE VALIDATION

At update:

```text
CURRENT STATE
NEW STATE
CHANGED ATTRIBUTES
RELATIONSHIPS
LIFECYCLE
```

must be evaluated.

---

# 52. IMPORT VALIDATION

Imports require:

```text
SOURCE VALIDATION
TYPE MAPPING
ATTRIBUTE MAPPING
REFERENCE MATCHING
DUPLICATE CHECK
SEMANTIC VALIDATION
```

---

# 53. PUBLISH VALIDATION

Before an architecture object is published as governed information:

```text
REQUIRED DATA
VALID REFERENCES
VALID RELATIONSHIPS
OWNER
CLASSIFICATION
LIFECYCLE
```

must meet the applicable quality rules.

---

# 54. METAMODEL QUERY SERVICE

The engine should expose metadata queries such as:

```text
GET OBJECT TYPES
GET TYPE DEFINITION
GET ATTRIBUTES
GET RELATIONSHIP TYPES
GET ALLOWED RELATIONSHIPS
GET VALIDATION RULES
GET METAMODEL VERSION
```

---

# 55. METAMODEL API

Initial API:

```text
/api/v1/metamodel
/api/v1/metamodel/types
/api/v1/metamodel/types/{code}
/api/v1/metamodel/relationships
/api/v1/metamodel/rules
/api/v1/metamodel/versions
```

---

# 56. API SECURITY

Metamodel read operations may be broadly available to authenticated users.

Metamodel write operations must be restricted to authorized governance roles.

---

# 57. METAMODEL WRITE OPERATIONS

Conceptual:

```text
CREATE TYPE
UPDATE TYPE
CREATE ATTRIBUTE
UPDATE ATTRIBUTE
CREATE RELATIONSHIP TYPE
CREATE RULE
CREATE VERSION
SUBMIT FOR REVIEW
ACTIVATE VERSION
RETIRE VERSION
```

Activation should be a governed operation.

---

# 58. ACTIVE METAMODEL

At runtime the engine should resolve:

```text
ACTIVE METAMODEL VERSION
```

before validating objects.

---

# 59. METAMODEL RESOLUTION

The engine should avoid hard-coding every object type in application code.

Prefer:

```text
METAMODEL DEFINITION
        ↓
ENGINE
        ↓
RUNTIME BEHAVIOR
```

---

# 60. METAMODEL CACHE

Metamodel definitions may be cached for performance.

The cache must be invalidated when:

```text
METAMODEL VERSION CHANGES
```

---

# 61. CACHE SAFETY

A stale metamodel cache must not cause an incompatible write to be accepted.

Activation should coordinate cache invalidation.

---

# 62. METAMODEL IMMUTABILITY

An active metamodel version should be immutable.

Changes create a new version.

Example:

```text
v1.0 ACTIVE
     ↓
CHANGE
     ↓
v1.1 DRAFT
```

---

# 63. VERSION COMPATIBILITY

A new metamodel version should declare:

```text
BACKWARD COMPATIBLE
NON-BREAKING
BREAKING
```

as applicable.

---

# 64. MIGRATION BETWEEN METAMODELS

A metamodel migration may require:

```text
OBJECT TRANSFORMATION
ATTRIBUTE TRANSFORMATION
RELATIONSHIP TRANSFORMATION
TYPE MAPPING
DATA QUALITY REVIEW
```

This belongs to controlled migration tooling.

---

# 65. METAMODEL DIFF

The engine should support comparison between versions.

Example:

```text
v1.0
vs
v1.1
```

Output:

```text
ADDED TYPE
REMOVED TYPE
CHANGED ATTRIBUTE
ADDED RELATIONSHIP
CHANGED CARDINALITY
CHANGED RULE
```

---

# 66. METAMODEL IMPACT ANALYSIS

Before activation, the engine should identify affected repository objects.

Example:

```text
ATTRIBUTE BECOMES REQUIRED
        ↓
2,340 OBJECTS AFFECTED
```

Activation should be blocked if required remediation has not been approved.

---

# 67. METAMODEL CHANGE RISK

Changes may be classified:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Examples:

```text
ADD OPTIONAL ATTRIBUTE → LOW

CHANGE CARDINALITY → MEDIUM

REMOVE OBJECT TYPE → HIGH

CHANGE SECURITY CLASSIFICATION RULE → CRITICAL
```

---

# 68. METAMODEL GOVERNANCE

Metamodel changes shall follow:

```text
PROPOSE
 ↓
ANALYZE
 ↓
VALIDATE
 ↓
REVIEW
 ↓
APPROVE
 ↓
ACTIVATE
 ↓
MONITOR
```

BUILD-04 will implement the workflow.

---

# 69. OBJECT TEMPLATES

The engine may provide templates for common object types.

Example:

```text
APPLICATION TEMPLATE
```

with:

```text
required attributes
recommended attributes
default lifecycle
classification
recommended relationships
```

---

# 70. TEMPLATE TABLE

Conceptual:

```text
metamodel_template
```

Fields:

```text
id
metamodel_id
object_type_id
name
description
configuration
is_active
```

---

# 71. TEMPLATE USE

Templates simplify creation but must not bypass validation.

Flow:

```text
TEMPLATE
 ↓
OBJECT DRAFT
 ↓
VALIDATION
 ↓
PERSISTENCE
```

---

# 72. OBJECT TYPE DOCUMENTATION

Each type should have machine-readable and human-readable documentation.

Example:

```text
APPLICATION
Purpose
Definition
Required attributes
Optional attributes
Allowed relationships
Lifecycle
Examples
```

---

# 73. METAMODEL CATALOGUE

The platform should provide a catalogue view:

```text
TYPE
DESCRIPTION
ATTRIBUTES
RELATIONSHIPS
RULES
LIFECYCLE
OWNER
VERSION
```

---

# 74. TYPE GOVERNANCE

Every production type should have:

```text
OWNER
DESCRIPTION
PURPOSE
STATUS
VERSION
```

Unknown or undocumented types should not be activated.

---

# 75. CUSTOM TYPES

Organizations may require custom object types.

Custom types must:

```text
USE NAMESPACE
HAVE OWNER
HAVE DESCRIPTION
HAVE VALIDATION
BE VERSIONED
BE GOVERNED
```

---

# 76. NAMESPACE

A custom organization type may use:

```text
CUSTOM.<ORGANIZATION>.<TYPE>
```

to avoid collision with core EA-IMETA types.

---

# 77. CORE VS EXTENSION

The engine shall distinguish:

```text
CORE METAMODEL
EXTENSION METAMODEL
```

Core changes require stronger governance.

---

# 78. EXTENSION COMPATIBILITY

Extensions must declare dependencies on core versions.

Example:

```text
Extension X
requires
EA-IMETA Core >= 1.0 < 2.0
```

---

# 79. METAMODEL PACKAGE

A metamodel version should be exportable as a package containing:

```text
METADATA
TYPE DEFINITIONS
ATTRIBUTES
RELATIONSHIPS
RULES
LIFECYCLES
ENUMERATIONS
TEMPLATES
DOCUMENTATION
VERSION
```

---

# 80. METAMODEL IMPORT

Importing a metamodel package requires:

```text
SCHEMA VALIDATION
VERSION CHECK
DEPENDENCY CHECK
RULE VALIDATION
CONFLICT DETECTION
```

---

# 81. METAMODEL CHECKSUM

A metamodel package may have a checksum to ensure integrity.

Example:

```text
SHA-256
```

The checksum is integrity evidence, not a security authorization mechanism.

---

# 82. METAMODEL REPOSITORY

Metamodel definitions themselves should be stored in the EA-IMETA repository.

This creates:

```text
ARCHITECTURE DATA
+
METAMODEL DATA
```

under the same governance framework.

---

# 83. META-METAMODEL

The engine must have a minimal stable definition of its own metamodel concepts:

```text
METAMODEL
TYPE
ATTRIBUTE
RELATIONSHIP TYPE
RULE
ENUMERATION
TEMPLATE
VERSION
```

This is the meta-metamodel foundation.

---

# 84. META-METAMODEL STABILITY

The meta-metamodel should change rarely.

Changes to it require architecture-level governance.

---

# 85. RULE EXECUTION

Rules may initially be implemented through controlled application code and structured expressions.

Do not allow arbitrary executable code to be stored in the database and executed automatically.

---

# 86. RULE EXPRESSION SECURITY

Expressions must be:

```text
PARSED
VALIDATED
ALLOW-LISTED
SANDBOXED WHERE NECESSARY
```

Never execute arbitrary Python or SQL supplied as a metamodel rule.

---

# 87. RULE PERFORMANCE

Validation rules should be measurable.

Track:

```text
execution_time
result
error
rule_id
```

This supports later optimization.

---

# 88. VALIDATION BATCHES

Large repositories may require batch validation.

Example:

```text
FULL REVALIDATION
```

The engine should support asynchronous execution later without changing rule semantics.

---

# 89. VALIDATION REPORT

A validation report should include:

```text
METAMODEL VERSION
START TIME
END TIME
OBJECTS CHECKED
RULES EXECUTED
FAILURES
WARNINGS
NOT EVALUATED
```

---

# 90. QUALITY SCORE

The engine may calculate:

```text
METAMODEL COMPLIANCE SCORE
```

but the score must never hide individual violations.

---

# 91. OBJECT VALIDITY

An object may be:

```text
VALID
VALID_WITH_WARNINGS
INVALID
UNKNOWN
```

This is separate from lifecycle status.

---

# 92. VALIDITY VS LIFECYCLE

Do not confuse:

```text
ACTIVE
```

with:

```text
VALID
```

An active object may be invalid and require remediation.

---

# 93. TYPE RETIREMENT

A type may be retired.

Existing objects should not automatically disappear.

They must be:

```text
MAPPED
MIGRATED
RETAINED UNDER LEGACY TYPE
```

according to governance.

---

# 94. RELATIONSHIP TYPE RETIREMENT

Retiring a relationship type requires impact analysis.

Existing relationships may remain historical while new relationships are blocked.

---

# 95. ATTRIBUTE RETIREMENT

Retiring an attribute should preserve historical data where required.

The engine may mark it:

```text
DEPRECATED
```

before:

```text
RETIRED
```

---

# 96. DEPRECATION

Deprecation provides a controlled transition period.

```text
ACTIVE
 ↓
DEPRECATED
 ↓
RETIRED
```

---

# 97. METAMODEL TELEMETRY

Track:

```text
VALIDATION COUNT
VALIDATION FAILURE
RULE EXECUTION TIME
TYPE USAGE
ATTRIBUTE USAGE
RELATIONSHIP USAGE
DEPRECATED FEATURE USAGE
```

---

# 98. METAMODEL HEALTH

A metamodel health report should identify:

```text
UNUSED TYPES
ORPHAN TYPES
MISSING DOCUMENTATION
CONFLICTING RULES
UNUSED ATTRIBUTES
INVALID CARDINALITY
DEPRECATED USAGE
```

---

# 99. METAMODEL CONSISTENCY

The engine should verify:

```text
ALL TYPES HAVE VALID OWNERS
ALL REFERENCES POINT TO VALID TYPES
ALL RELATIONSHIPS HAVE VALID SOURCE/TARGET
ALL RULES REFERENCE VALID OBJECTS
ALL ENUMS ARE CONSISTENT
```

---

# 100. CIRCULAR TYPE DEPENDENCIES

Circular dependencies in the metamodel should be detected where they create invalid semantics.

Not all cycles are inherently invalid.

The engine must distinguish:

```text
VALID GRAPH CYCLE
```

from:

```text
INVALID METAMODEL DEPENDENCY CYCLE
```

---

# 101. RELATIONSHIP CONFLICTS

The engine should detect conflicting definitions.

Example:

```text
SUPPORTS
source = APPLICATION
target = CAPABILITY

another definition:
SUPPORTS
source = TECHNOLOGY
target = PERSON
```

unless explicitly versioned or namespaced.

---

# 102. CARDINALITY CONFLICTS

Example:

```text
TYPE RULE:
1 owner required

OBJECT:
0 owners
```

This must fail validation.

---

# 103. CLASSIFICATION RULES

The metamodel may define classification requirements.

Example:

```text
SECURITY_CONTROL
→ minimum classification = INTERNAL
```

Classification policies may also be applied by governance services.

---

# 104. LIFECYCLE BINDING

Object types may bind to lifecycle definitions.

Example:

```text
APPLICATION
→ APPLICATION_LIFECYCLE
```

while:

```text
PROJECT
→ PROJECT_LIFECYCLE
```

---

# 105. LIFECYCLE RULES

Rules may define valid transitions.

Example:

```text
PLANNED → ACTIVE
ACTIVE → DEPRECATED
DEPRECATED → RETIRED
```

Invalid transitions should be rejected.

---

# 106. METAMODEL AND WORKFLOW

BUILD-03 defines:

```text
WHAT IS VALID
```

BUILD-04 defines:

```text
WHO MAY CHANGE IT
WHEN IT MAY CHANGE
WHO MUST APPROVE IT
```

This separation is intentional.

---

# 107. METAMODEL AND KNOWLEDGE GRAPH

BUILD-03 defines graph semantics through:

```text
OBJECT TYPES
RELATIONSHIP TYPES
DIRECTION
CARDINALITY
```

BUILD-06 will project these semantics into the Knowledge Graph.

---

# 108. METAMODEL AND AI

AI services may query the metamodel to understand:

```text
OBJECT TYPE
ATTRIBUTE
RELATIONSHIP
RULE
VALIDITY
```

AI must not infer that an undocumented relationship is valid.

---

# 109. METAMODEL AND IMPORTS

Integration services should use the Metamodel Engine to validate imported data before persistence.

```text
EXTERNAL DATA
 ↓
MAPPING
 ↓
METAMODEL VALIDATION
 ↓
REPOSITORY
```

---

# 110. METAMODEL AND REPORTING

Reports should use metamodel definitions to understand:

```text
TYPE
ATTRIBUTE
RELATIONSHIP
STATUS
```

This supports dynamic reporting.

---

# 111. DYNAMIC UI SUPPORT

The metamodel can later drive dynamic forms.

Example:

```text
TYPE = APPLICATION
        ↓
FORM GENERATED FROM
ATTRIBUTES + RULES
```

This reduces hard-coded UI definitions.

---

# 112. FORM VALIDATION

Dynamic UI validation is not sufficient.

Server-side Metamodel Engine validation remains authoritative.

---

# 113. API SCHEMA GENERATION

Where practical, metamodel definitions may support generated API schemas.

Generated schemas must remain subject to API governance.

---

# 114. METAMODEL TESTING

Test categories:

```text
TYPE TESTS
ATTRIBUTE TESTS
RELATIONSHIP TESTS
CARDINALITY TESTS
RULE TESTS
LIFECYCLE TESTS
VERSION TESTS
MIGRATION TESTS
API TESTS
```

---

# 115. TYPE TEST

Verify:

```text
valid type accepted
unknown type rejected
retired type handled correctly
abstract type not instantiated
```

---

# 116. ATTRIBUTE TEST

Verify:

```text
required accepted when present
missing required rejected
invalid data type rejected
invalid enum rejected
reference target validated
```

---

# 117. RELATIONSHIP TEST

Verify:

```text
allowed relationship accepted
invalid source rejected
invalid target rejected
cardinality enforced
duplicate prevented
```

---

# 118. RULE TEST

Each blocking rule should have:

```text
positive test
negative test
boundary test
```

---

# 119. VERSION TEST

Verify:

```text
draft version isolated
active version immutable
new version can be activated
old version becomes superseded
objects remain traceable to governing version
```

---

# 120. METAMODEL ROLLBACK

Activation of a new metamodel version should have a documented rollback strategy.

Rollback may mean:

```text
REACTIVATE PREVIOUS VERSION
```

rather than deleting the new version.

---

# 121. METAMODEL AUDIT

Record:

```text
WHO CREATED
WHO MODIFIED
WHO APPROVED
WHO ACTIVATED
WHEN
WHY
```

---

# 122. METAMODEL CHANGE REQUEST

Every material metamodel change should have a change record.

Minimum:

```text
CHANGE ID
REQUESTER
RATIONALE
IMPACT
VERSION
STATUS
DECISION
```

---

# 123. METAMODEL SECURITY

Only authorized governance administrators may:

```text
CREATE METAMODEL VERSION
MODIFY DEFINITIONS
ACTIVATE VERSION
RETIRE VERSION
```

Read access may be broader.

---

# 124. METAMODEL ACCESS

The access model should distinguish:

```text
VIEW
PROPOSE
EDIT
REVIEW
APPROVE
ACTIVATE
RETIRE
```

---

# 125. METAMODEL OBSERVABILITY

Metrics:

```text
ACTIVE METAMODEL VERSION
VALIDATION RATE
VALIDATION ERROR RATE
RULE EXECUTION TIME
METAMODEL CHANGES
FAILED ACTIVATIONS
```

---

# 126. METAMODEL ERROR HANDLING

Errors should distinguish:

```text
TYPE_NOT_FOUND
ATTRIBUTE_NOT_FOUND
RELATIONSHIP_NOT_ALLOWED
CARDINALITY_VIOLATION
RULE_VIOLATION
METAMODEL_VERSION_ERROR
METAMODEL_CONFLICT
```

---

# 127. METAMODEL CACHE FAILURE

If metamodel cache loading fails:

```text
DO NOT ACCEPT UNKNOWN RULE SET
```

The service should fail safely or use a known-good active version.

---

# 128. FAIL-SAFE PRINCIPLE

The Metamodel Engine must never silently accept an object because validation was unavailable.

The system should choose:

```text
BLOCK
or
EXPLICITLY MARK NOT VALIDATED
```

according to operation policy.

---

# 129. PERFORMANCE

The engine should optimize common operations:

```text
TYPE LOOKUP
ATTRIBUTE LOOKUP
RELATIONSHIP LOOKUP
RULE LOOKUP
VALIDATION
```

Caching is allowed but must remain consistent with the active version.

---

# 130. SCALABILITY

The engine should support repositories ranging from:

```text
HUNDREDS
THOUSANDS
HUNDREDS OF THOUSANDS
```

of objects without changing semantic design.

Actual performance targets require measured workloads.

---

# 131. BUILD-03 DELIVERABLES

BUILD-03 shall produce:

1. metamodel persistence
2. metamodel versioning
3. object type catalogue
4. type hierarchy
5. attribute definitions
6. enumeration definitions
7. relationship definitions
8. cardinality model
9. semantic rules
10. validation engine
11. lifecycle bindings
12. classification bindings
13. object templates
14. metamodel query service
15. metamodel API
16. metamodel diff
17. impact analysis
18. metamodel package export/import foundation
19. metamodel audit
20. metamodel telemetry
21. metamodel tests
22. documentation catalogue
23. BUILD-03 acceptance report

---

# 132. BUILD-03 ACCEPTANCE CRITERIA

BUILD-03 is accepted when:

```text
[ ] Metamodel can be created
[ ] Metamodel can be versioned
[ ] Draft and active states work
[ ] Active version is immutable
[ ] Object types can be defined
[ ] Type hierarchy works
[ ] Abstract types work
[ ] Attributes can be defined
[ ] Data types are validated
[ ] Enumerations work
[ ] References are validated
[ ] Relationship types can be defined
[ ] Source/target constraints work
[ ] Cardinality is validated
[ ] Semantic rules execute
[ ] Blocking violations prevent invalid writes
[ ] Validation results are recorded
[ ] Lifecycle bindings work
[ ] Classification rules work
[ ] Templates work
[ ] Metamodel API works
[ ] Version comparison works
[ ] Impact analysis works
[ ] Metamodel changes are audited
[ ] Automated tests pass
```

---

# 133. QUALITY GATE

BUILD-03 must pass:

```text
SEMANTIC
    ↓
VALIDATION
    ↓
VERSIONING
    ↓
GOVERNANCE
    ↓
OPERATIONAL
```

---

# 134. SEMANTIC GATE

Verify:

```text
types
attributes
relationships
cardinality
inheritance
rules
```

---

# 135. VALIDATION GATE

Verify:

```text
valid input
invalid input
boundary conditions
reference integrity
semantic violations
```

---

# 136. VERSIONING GATE

Verify:

```text
draft
review
approval
activation
immutability
supersession
rollback
```

---

# 137. GOVERNANCE GATE

Verify:

```text
permissions
audit
change requests
approval boundaries
activation control
```

---

# 138. OPERATIONAL GATE

Verify:

```text
performance
logging
metrics
cache behavior
failure handling
recovery
```

---

# 139. BUILD-03 RISKS

Known risks:

```text
OVER-GENERALIZATION
RULE COMPLEXITY
METAMODEL LOCK-IN
VERSION EXPLOSION
PERFORMANCE
AMBIGUOUS SEMANTICS
UNCONTROLLED CUSTOMIZATION
```

---

# 140. RISK MITIGATION

Use:

```text
SMALL CORE
+
CONTROLLED EXTENSIONS
+
EXPLICIT SEMANTICS
+
VERSIONING
+
IMPACT ANALYSIS
+
TESTING
+
GOVERNANCE
```

---

# 141. CRITICAL DESIGN DECISION

The Metamodel Engine must not become a general-purpose programming language.

It defines architecture semantics.

It does not become an unrestricted rule-execution platform.

---

# 142. CRITICAL SECURITY DECISION

No metamodel rule may execute arbitrary source code.

The system must use controlled expressions and predefined rule capabilities.

---

# 143. CRITICAL VERSION DECISION

An active metamodel is immutable.

Changes always create a new version.

This guarantees reproducibility of architecture validation.

---

# 144. CRITICAL TRACEABILITY DECISION

Every validated architecture object should be traceable to the metamodel version used for validation where required.

Conceptually:

```text
OBJECT
 ↓
VALIDATED AGAINST
 ↓
METAMODEL VERSION
```

---

# 145. CRITICAL SEMANTIC DECISION

A relationship is not valid merely because two objects exist.

It is valid only when:

```text
SOURCE TYPE
+
RELATIONSHIP TYPE
+
TARGET TYPE
+
CARDINALITY
+
RULES
```

permit the relationship.

---

# 146. CRITICAL EXTENSION DECISION

Custom extensions are allowed, but they must remain:

```text
NAMESPACED
VERSIONED
OWNED
DOCUMENTED
VALIDATED
GOVERNED
```

---

# 147. FINAL BUILD-03 PRINCIPLES

1. The metamodel defines architecture meaning.
2. The repository remains the persistence foundation.
3. Object types are explicit.
4. Attributes are governed.
5. Relationships are semantic first-class objects.
6. Cardinality is machine-readable.
7. Rules are explicit and controlled.
8. Active metamodel versions are immutable.
9. Changes create new versions.
10. Impact analysis precedes activation.
11. Validation failures are visible.
12. Unknown is never silently treated as valid.
13. Custom extensions are governed.
14. Arbitrary executable rules are prohibited.
15. Metamodel changes are audited.
16. Metamodel versions are reproducible.
17. The engine remains modular and testable.
18. Workflow controls who may change the metamodel.
19. The metamodel supports future graph, AI and adaptive capabilities.
20. Semantic correctness takes priority over convenience.

---

# 148. BUILD-03 COMPLETION STATEMENT

EA-IMETA-BUILD-03 establishes the semantic engine that gives the repository its architectural meaning.

The build now progresses from:

```text
TECHNICAL FOUNDATION
        ↓
REPOSITORY
        ↓
METAMODEL
```

The next phase will govern how these architecture definitions and objects are changed, reviewed, approved and controlled.

Therefore:

> THE REPOSITORY STORES THE TRUTH; THE METAMODEL DEFINES ITS MEANING; GOVERNANCE CONTROLS ITS CHANGE.

---

# END OF EA-IMETA-BUILD-03
## METAMODEL ENGINE
## COMPLETE
