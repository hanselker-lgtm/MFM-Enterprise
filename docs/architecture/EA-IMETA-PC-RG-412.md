# EA-IMETA-PC-RG-412

## EVIDENCE, AUDIT & TRACEABILITY DATA MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-412 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Evidence, Audit & Traceability Data Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-411 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how evidence, decisions, state changes, events and audit records are represented and linked |
| Architectural Boundary | Source → Evidence → Requirement → Control → Test → Decision → State → Audit |

---

# 2. Purpose

EA-IMETA-PC-RG-412 defines the data architecture required to make PC-RG decisions demonstrable, traceable and reconstructable.

RG-409 established requirement/control/test traceability.

RG-410 established the state machine.

RG-411 established workflow and event orchestration.

RG-412 provides the evidence and audit data model connecting them.

The governing chain is:

```text
SOURCE
  ↓
EVIDENCE
  ↓
REQUIREMENT
  ↓
CONTROL
  ↓
TEST
  ↓
RESULT
  ↓
DECISION
  ↓
STATE
  ↓
EVENT
  ↓
AUDIT
```

---

# 3. Core Principle

> **A decision is only as trustworthy as the evidence, authority, criteria and audit trail that support it.**

The system SHALL preserve enough information to answer:

```text
WHAT was decided?
WHY was it decided?
WHO decided it?
WHEN?
UNDER WHICH AUTHORITY?
USING WHICH EVIDENCE?
AGAINST WHICH CRITERIA?
WHAT STATE RESULTED?
WHAT HAPPENED AFTERWARD?
```

---

# 4. Evidence Is a First-Class Object

Evidence SHALL not be stored only as free text attached to a case.

It SHALL have an identifiable lifecycle.

```text
Evidence
  ↓
Collected
  ↓
Classified
  ↓
Validated
  ↓
Linked
  ↓
Used
  ↓
Retained
  ↓
Expired / Superseded
```

---

# 5. Evidence Object

Minimum conceptual attributes:

| Attribute | Required |
|---|---|
| Evidence ID | Yes |
| Evidence Type | Yes |
| Source | Yes |
| Source Reference | Yes |
| Owner | Yes |
| Collector | Yes |
| Created At | Yes |
| Collected At | Yes |
| Valid From | Where applicable |
| Valid Until | Where applicable |
| Integrity Status | Yes |
| Scope | Yes |
| Classification | Yes |
| Requirement Links | Yes |
| Control Links | Where applicable |
| Test Links | Where applicable |
| Decision Links | Where applicable |
| Case ID | Yes |
| Version | Yes |
| Retention Class | Yes |

---

# 6. Evidence Types

Evidence MAY include:

```text
DOCUMENT
RECORD
DATABASE VALUE
SYSTEM EVENT
AUDIT EVENT
TEST RESULT
SCREENSHOT
LOG
REPORT
MEASUREMENT
EXTERNAL ATTESTATION
USER INPUT
CONFIGURATION
APPROVAL
OBSERVATION
AI/AGENT OUTPUT
```

Evidence type SHALL be explicit.

---

# 7. Evidence Source

Every evidence item SHALL identify its origin.

```text
INTERNAL SYSTEM
USER
EXTERNAL SYSTEM
THIRD PARTY
AUTOMATED SENSOR
AI / AGENT
DOCUMENT REPOSITORY
MANUAL OBSERVATION
```

Where source authenticity is material, source identity SHALL be verifiable.

---

# 8. Evidence Integrity

Evidence SHALL have an integrity status:

```text
UNASSESSED
VALID
QUESTIONED
INVALID
SUPERSEDED
CORRUPTED
EXPIRED
```

Invalid or expired evidence SHALL not silently continue supporting decisions.

---

# 9. Evidence Validity

Evidence may be temporally valid.

```text
VALID FROM
VALID UNTIL
```

The system SHALL support determination of whether evidence was valid at the time of a decision.

This is important where historical decisions are audited after the fact.

---

# 10. Evidence Versioning

Material evidence changes SHALL create a new version.

```text
Evidence v1
   ↓
Evidence v2
```

The system SHALL preserve the historical version used by previous decisions.

---

# 11. Evidence Supersession

Superseding evidence SHALL not delete historical evidence.

```text
OLD EVIDENCE
   ↓
SUPERSEDED BY
   ↓
NEW EVIDENCE
```

Both remain traceable.

---

# 12. Evidence Classification

Evidence SHALL support classification such as:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
SENSITIVE
```

Actual classification levels SHALL be governed by the applicable security architecture.

---

# 13. Evidence Access

Access SHALL be controlled by:

```text
Identity
Role
Case Scope
Data Classification
Purpose
Authority
```

Evidence access SHALL itself be auditable where required.

---

# 14. Evidence Collection

Collection SHALL record:

```text
Who
What
When
From Where
How
Under Which Authority
```

Automated collection SHALL identify the collecting service or agent.

---

# 15. Evidence Validation

Evidence validation SHALL consider:

```text
Authenticity
Integrity
Completeness
Relevance
Currency
Scope
Source Reliability
```

Not every evidence type requires the same level of validation.

The required level SHALL be risk-based.

---

# 16. Evidence Binding

Evidence SHALL be linked to the specific object it supports.

Possible links:

```text
Evidence → Requirement
Evidence → Control
Evidence → Test
Evidence → Decision
Evidence → State Transition
Evidence → Workflow Task
Evidence → Regression Finding
Evidence → Remediation
```

Generic "case attachment" SHALL not be the only relationship for material evidence.

---

# 17. Evidence Chain

A material decision should be reconstructable as:

```text
DECISION
   ↓
CRITERIA
   ↓
REQUIREMENTS
   ↓
CONTROLS
   ↓
TESTS
   ↓
EVIDENCE
   ↓
SOURCE
```

Reverse traceability SHALL also be possible.

---

# 18. Decision Object

Every material decision SHALL be represented as a first-class object.

| Attribute | Required |
|---|---|
| Decision ID | Yes |
| Case ID | Yes |
| Decision Type | Yes |
| Subject | Yes |
| Trigger | Yes |
| Input State | Yes |
| Criteria Version | Yes |
| Evidence Set | Yes |
| Authority | Yes |
| Decision Maker | Yes |
| Decision Time | Yes |
| Result | Yes |
| Conditions | Where applicable |
| Rationale | Yes |
| Output State | Yes |
| Review / Expiry | Where applicable |
| Audit Reference | Yes |

---

# 19. Decision Types

Initial catalogue:

```text
VALIDATION
VERIFICATION
ACCEPTANCE
CLOSURE
REGRESSION
REMEDIATION
REVALIDATION
REVERIFICATION
REACCEPTANCE
SUSPENSION
REVOCATION
REOPENING
```

---

# 20. Decision Evidence Set

A decision SHALL identify the evidence set used.

```text
Decision
  ├── Evidence A
  ├── Evidence B
  ├── Evidence C
  └── Criteria
```

The evidence set SHALL be immutable from the historical decision perspective.

New evidence does not retroactively change what was used.

---

# 21. Decision Rationale

Material decisions SHALL record rationale sufficient for later review.

The rationale SHALL distinguish:

```text
FACTS
CRITERIA
ANALYSIS
DECISION
CONDITIONS
```

AI-generated rationale SHALL be identified as such and SHALL not be treated as independent authority.

---

# 22. State Transition Record

Every material transition SHALL create a transition record.

```text
Transition ID
Case ID
From State
To State
Trigger
Actor
Authority
Evidence
Decision
Timestamp
State Machine Version
```

---

# 23. Event Record

Events from RG-411 SHALL be represented independently from state.

```text
Event ID
Event Type
Case ID
Workflow ID
Task ID
Actor / Service
Timestamp
Correlation ID
Causation ID
Payload Reference
Schema Version
```

An event says:

> Something happened.

A state transition says:

> The authoritative lifecycle state changed.

These SHALL remain distinguishable.

---

# 24. Audit Event

Audit records SHALL capture security and governance-relevant actions.

Minimum:

```text
Audit ID
Timestamp
Actor
Role
Action
Object Type
Object ID
Previous Value / State
New Value / State
Authority
Reason
Correlation ID
Source
```

---

# 25. Audit Immutability

Users SHALL not be able to modify or delete historical audit records through normal application functions.

Corrections SHALL be recorded as new audit events.

---

# 26. Audit Reconstruction

The system SHALL support reconstruction of a lifecycle:

```text
CASE CREATED
   ↓
VALIDATION
   ↓
VERIFICATION
   ↓
ACCEPTANCE
   ↓
CLOSURE
   ↓
MONITORING
   ↓
REGRESSION
   ↓
REMEDIATION
   ↓
REVALIDATION
   ↓
REACCEPTANCE
```

Each step SHALL be linked to evidence and authority as applicable.

---

# 27. Correlation Model

The following identifiers SHALL support cross-service tracing:

```text
Case ID
Workflow ID
Task ID
Command ID
Event ID
Decision ID
Transition ID
Evidence ID
Audit ID
Correlation ID
Causation ID
```

A single business operation should be traceable across these identifiers.

---

# 28. Traceability Graph

The conceptual model is a graph:

```text
                REQUIREMENT
                 /       \
                /         \
          CONTROL         CRITERIA
             |               |
            TEST             |
             |               |
          EVIDENCE ──────────┘
             |
          DECISION
             |
        STATE TRANSITION
             |
           EVENT
             |
           AUDIT
```

This graph SHALL support both forward and backward navigation.

---

# 29. Forward Traceability

Starting from a requirement:

```text
Requirement
 ↓
Control
 ↓
Implementation
 ↓
Test
 ↓
Evidence
 ↓
Decision
 ↓
State
```

---

# 30. Backward Traceability

Starting from a decision:

```text
Decision
 ↓
Evidence
 ↓
Test
 ↓
Control
 ↓
Requirement
 ↓
Source
```

This is essential for audit and impact analysis.

---

# 31. Evidence Sufficiency

Evidence sufficiency SHALL be assessed against:

```text
RELEVANCE
+
COMPLETENESS
+
CURRENCY
+
AUTHENTICITY
+
INTEGRITY
+
INDEPENDENCE
```

The required threshold SHALL depend on the decision risk.

---

# 32. Evidence Independence

Where independent evidence is required, the source SHALL be separate from the party whose performance is being assessed.

Example:

```text
CONTROL OWNER
      ≠
INDEPENDENT TESTER
```

unless an approved exception exists.

---

# 33. Evidence Conflicts

Conflicting evidence SHALL be explicit.

```text
Evidence A → VALID
Evidence B → CONTRADICTORY
```

The decision workflow SHALL not silently select one source.

Conflict resolution SHALL record:

```text
Conflict
Assessment
Authority
Resolution
Rationale
```

---

# 34. Missing Evidence

Missing mandatory evidence SHALL result in:

```text
EVIDENCE GAP
```

and may produce:

```text
BLOCKED
INCONCLUSIVE
FAILED
SUSPENDED
```

depending on the governing decision rule.

---

# 35. Evidence Expiry

Where evidence expires:

```text
VALID
  ↓
EXPIRING
  ↓
EXPIRED
```

Expiry SHALL trigger applicable monitoring, revalidation or escalation.

---

# 36. Audit Retention

Retention SHALL be defined by:

```text
Record Type
Regulatory Requirement
Business Requirement
Risk
Contractual Requirement
Security Requirement
```

The system SHALL distinguish:

```text
ACTIVE RETENTION
ARCHIVED
LEGAL HOLD
DESTRUCTION ELIGIBLE
```

---

# 37. Legal / Compliance Hold

Where records are subject to a hold:

```text
NORMAL RETENTION
      ↓
LEGAL / COMPLIANCE HOLD
      ↓
DESTRUCTION BLOCKED
```

Release of the hold SHALL be separately authorised and audited.

---

# 38. Data Integrity Controls

Evidence, decisions and audit records SHALL be protected against:

```text
Unauthorised Modification
Deletion
Reordering
Untracked Replacement
Corruption
Unauthorised Disclosure
```

Technical controls may include:

```text
Access Control
Hashing
Digital Signatures
Append-Only Storage
Versioning
Encryption
Integrity Checks
```

---

# 39. Privacy and Data Minimisation

Only evidence required for the governed purpose SHALL be retained.

The architecture SHALL support:

```text
Purpose Limitation
Least Privilege
Retention Limits
Access Logging
Controlled Export
```

Sensitive data SHALL not be duplicated unnecessarily across evidence records.

---

# 40. Export and Audit Package

The system SHOULD be able to generate an audit package containing:

```text
Case
Current State
State History
Decisions
Criteria
Evidence Index
Controls
Tests
Results
Workflow History
Events
Audit Trail
Conditions
Exceptions
```

The package SHALL preserve identifiers and relationships.

---

# 41. Audit Package Integrity

An exported audit package SHOULD contain:

```text
Package ID
Creation Time
Scope
Source System
Included Record IDs
Version Information
Integrity Metadata
```

The package SHALL not be mistaken for the authoritative source unless explicitly designated.

---

# 42. AI and Agent Evidence

AI/agent-generated material SHALL record:

```text
Agent ID
Model
Model Version
Prompt / Instruction Reference
Input Data Reference
Tool Calls
Output
Timestamp
Human Reviewer
Decision Use
```

AI output SHALL be distinguished from independently verified evidence.

---

# 43. AI Evidence Reliability

AI output SHALL not automatically qualify as authoritative evidence.

Where AI output informs a material decision:

```text
AI OUTPUT
   ↓
HUMAN / CONTROLLED VALIDATION
   ↓
ACCEPTED EVIDENCE
```

unless a separately approved architecture explicitly authorises automated use.

---

# 44. Data Model

Core conceptual entities:

```text
Case
Requirement
Criteria
Control
Test
Evidence
Decision
StateTransition
Event
Workflow
Task
AuditEvent
Condition
Exception
```

Relationships:

```text
Case
 ├── Requirements
 ├── Controls
 ├── Tests
 ├── Evidence
 ├── Decisions
 ├── StateTransitions
 ├── Events
 ├── Workflows
 ├── Tasks
 └── AuditEvents
```

---

# 45. Referential Integrity

Material references SHALL not point to deleted objects.

If an object is superseded:

```text
OLD ID
 ↓
SUPERSEDED BY
 ↓
NEW ID
```

Historical relationships SHALL remain resolvable.

---

# 46. Data Versioning

The following SHALL support versioning:

```text
Criteria
Requirement
Control
Test
Evidence
Workflow
State Machine
Decision Schema
Event Schema
```

Historical decisions SHALL retain the versions applicable when they were made.

---

# 47. Temporal Queries

The system SHOULD support questions such as:

```text
What was the state on date X?
Which evidence supported the decision on date X?
Which criteria version was active?
Who held authority?
Which controls were in effect?
```

This requires temporal traceability.

---

# 48. Audit Query Examples

The architecture SHALL support:

```text
Show all decisions made by actor X.

Show all acceptance decisions supported by evidence Y.

Show all cases affected by control C.

Show all decisions using criteria version V.

Show all regressions caused by dependency D.

Show all cases with expired evidence.

Show all state transitions performed under a specific authority.
```

---

# 49. Data Quality Rules

The system SHALL detect:

```text
Orphan Evidence
Orphan Decision
Missing Authority
Missing Criteria
Missing Evidence
Invalid State Reference
Broken Audit Link
Duplicate Event
Conflicting State
Expired Evidence Used
```

Material data-quality failures SHALL be escalated.

---

# 50. Event / Audit Relationship

Not every event is necessarily an audit event.

```text
EVENT
= business fact

AUDIT EVENT
= governance/security record of an action or change
```

A material business event MAY generate an audit record.

The two concepts SHALL not be collapsed.

---

# 51. Evidence / Attachment Relationship

A file attachment is not automatically evidence.

It becomes evidence when:

```text
Source
Context
Purpose
Validity
Integrity
Relationship
```

are established.

---

# 52. MFM Implementation Boundary

The conceptual implementation should include:

```text
Evidence Service
Decision Service
Audit Service
Traceability Service
Retention Service
Export Service
Integrity Service
```

These services SHALL integrate with:

```text
Workflow Service
State Service
Control/Test Service
Authority Service
```

---

# 53. API Concepts

Illustrative operations:

```text
createEvidence()
validateEvidence()
linkEvidence()
supersedeEvidence()
recordDecision()
recordTransition()
recordEvent()
recordAuditEvent()
getTraceability()
createAuditPackage()
placeRetentionHold()
releaseRetentionHold()
```

These are architectural operations, not implementation-specific commitments.

---

# 54. Security Boundary

All evidence and audit APIs SHALL enforce:

```text
Authentication
Authorisation
Scope
Purpose
Least Privilege
Audit
```

Privileged administrative access SHALL itself be audited.

---

# 55. Performance and Scale

The architecture SHALL account for potentially large volumes of:

```text
Events
Audit Records
Evidence Metadata
Test Results
Monitoring Records
```

Indexes and retention policies SHALL support efficient retrieval without compromising historical integrity.

---

# 56. Failure Handling

Evidence service failure SHALL not silently produce a successful decision.

Examples:

```text
Evidence Save Failure
→ Decision blocked or transaction compensated

Audit Write Failure
→ State transition blocked where audit is mandatory

Traceability Link Failure
→ Record incomplete / exception raised

Export Failure
→ Audit package marked incomplete
```

---

# 57. Backup and Recovery

Evidence and audit data SHALL have defined:

```text
Backup
Recovery
Retention
Integrity Verification
Disaster Recovery
```

Recovery SHALL preserve relationship integrity.

---

# 58. Monitoring

The evidence/audit architecture SHOULD monitor:

```text
Missing Evidence
Expired Evidence
Integrity Failures
Broken Links
Audit Write Failures
Retention Exceptions
Unauthorised Access
Export Failures
Data Quality Failures
```

---

# 59. Test Model

Tests SHALL verify:

```text
Evidence creation
Evidence validation
Evidence versioning
Evidence expiry
Decision traceability
State traceability
Audit immutability
Access control
Temporal reconstruction
Export integrity
AI evidence labelling
```

---

# 60. Acceptance Criteria

EA-IMETA-PC-RG-412 is accepted when:

- evidence is a first-class object;
- material decisions reference evidence sets;
- state transitions reference decisions and authority;
- events and audit events remain distinguishable;
- forward and backward traceability work;
- evidence versions are preserved;
- expired/invalid evidence is controlled;
- audit records are protected;
- historical reconstruction is possible;
- retention and legal hold are supported;
- AI-generated evidence is explicitly identified;
- referential integrity is enforced;
- audit packages are reproducible.

---

# 61. Next Step

The next logical artifact is the **PC-RG authority, roles and separation-of-duties model**, because the data model now records authority but does not yet define the authoritative permission architecture in sufficient detail.

Provisional next artifact:

> **EA-IMETA-PC-RG-413 — AUTHORITY, ROLES & SEPARATION-OF-DUTIES MODEL**

This will define who may perform, review, verify, approve, revoke and reopen each lifecycle action.

---

# 62. Governing Principle

> **Evidence proves, decisions determine, state records the result, events record facts, and audit preserves accountability.**

The PC-RG architecture SHALL preserve these distinctions so that every material outcome can be reconstructed and challenged on evidence rather than assumed from status labels.

# END OF EA-IMETA-PC-RG-412
