# MFM Post-Steady-State Phase Control
## N2-D.00 — Evidence Model & Evidence Control

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-D.00-Evidence-Model-and-Evidence-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-D WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-C.00 — Relationship Catalogue Disposition & Consolidation Record  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-D — Evidence Model  
**State:** N2-D.00 — EVIDENCE MODEL ESTABLISHMENT

---

# 1. Purpose

N2-D.00 establishes the controlled evidence model required to support the traceability system defined by N2-A.00 and the entity/relationship vocabulary established by N2-B.00.

The purpose is to define how evidence shall be:

```text
identified
classified
linked
owned
assessed
validated
dated
maintained
retired
```

Evidence is required to support materially significant traceability claims.

N2-D does not create an inventory of all available MFM evidence.

It defines the model and control by which evidence can subsequently be captured and assessed.

---

# 2. Governing Chain

The controlled chain is:

```text
MFM v1.2-Steady-State
        ↓
SC-90 — SERIES CLOSED
        ↓
N1.00 — POST-STEADY-STATE PHASE CHARTER
        ↓
N2.00 — TRACEABILITY CONTROL & SCOPE
        ↓
N2-A.00 — TRACEABILITY MODEL
        ↓
N2-B.00 — ENTITY & RELATIONSHIP CATALOGUE
        ↓
N2-C.00 — RELATIONSHIP CATALOGUE DISPOSITION
        ↓
N2-D.00 — EVIDENCE MODEL
```

N2-A establishes evidence as a first-class component of the traceability model. N2-B establishes the controlled relationship vocabulary. N2-C formally consolidated the separately planned relationship catalogue into N2-B.00.

---

# 3. Evidence Principle

The fundamental rule is:

> **A traceability claim shall be supported by evidence appropriate to the claim's materiality, type and lifecycle.**

Evidence does not automatically prove correctness.

Evidence establishes support for a claim and must therefore be assessed for:

```text
relevance
authority
currency
completeness
consistency
confidence
```

---

# 4. Evidence Model

The canonical evidence model is:

```text
CLAIM
  │
  │ supported by
  ▼
EVIDENCE
  │
  ├── has SOURCE
  ├── has OWNER
  ├── has DATE
  ├── has STATUS
  ├── has CONFIDENCE
  ├── has VALIDITY
  └── has RETENTION / LIFECYCLE
```

The evidence relationship shall remain explicit.

---

# 5. Evidence as a Controlled Object

An evidence record shall be treated as a controlled object.

Minimum conceptual attributes are:

```text
Evidence ID
Evidence Type
Title / Description
Source
Source Owner
Evidence Owner
Date Created
Effective Date
Review Date
Status
Confidence
Validity
Materiality
Lifecycle
Location / Reference
Supported Claim
Related Entity
Related Relationship
```

Not every field must be populated for every evidence item, but mandatory fields shall be determined by evidence materiality and use.

---

# 6. Evidence Types

N2-D establishes the following controlled evidence families:

```text
EV-01 Architecture Evidence
EV-02 Requirement Evidence
EV-03 Governance Evidence
EV-04 Design Evidence
EV-05 Configuration Evidence
EV-06 Implementation Evidence
EV-07 Operational Evidence
EV-08 Security Evidence
EV-09 Test / Validation Evidence
EV-10 Audit / Assurance Evidence
EV-11 Measurement Evidence
EV-12 Decision Evidence
EV-13 Historical Evidence
```

These are evidence classifications, not new architecture entity classes.

---

# 7. EV-01 — Architecture Evidence

Examples include:

```text
Architecture Documents
Architecture Models
Architecture Views
Capability Models
Architecture Principles
Architecture Baselines
```

Purpose:

```text
Support architectural claims
Support architecture-to-capability relationships
Support architecture-to-requirement relationships
```

---

# 8. EV-02 — Requirement Evidence

Examples include:

```text
Business Requirements
Stakeholder Requirements
Architecture Requirements
Solution Requirements
Acceptance Criteria
Requirement Approvals
```

Purpose:

```text
Support requirement identity
Support requirement ownership
Support requirement derivation
Support satisfaction claims
```

---

# 9. EV-03 — Governance Evidence

Examples include:

```text
Policies
Standards
Mandates
Governance Decisions
Approval Records
Authority Records
```

Purpose:

```text
Support governance claims
Support ownership
Support constraints
Support approval status
```

---

# 10. EV-04 — Design Evidence

Examples include:

```text
Design Records
Solution Designs
Technical Designs
Interface Designs
Data Designs
Security Designs
```

Purpose:

```text
Support intended implementation
Support architecture realization
Support design decisions
```

---

# 11. EV-05 — Configuration Evidence

Examples include:

```text
Configuration Records
CMDB Records
Asset Records
Application Inventories
Network Inventories
Identity Records
```

Purpose:

```text
Support existence
Support configuration
Support ownership
Support implementation mapping
```

---

# 12. EV-06 — Implementation Evidence

Examples include:

```text
Deployment Records
Source / Build Records
Release Records
Installed Component Records
Implementation Acceptance Records
```

Purpose:

```text
Support implementation existence
Support architecture realization
Support version and lifecycle status
```

---

# 13. EV-07 — Operational Evidence

Examples include:

```text
Operational Procedures
Runbooks
Service Records
Monitoring Records
Incident Records
Problem Records
Change Records
```

Purpose:

```text
Support operational existence
Support service operation
Support operational ownership
Support lifecycle state
```

---

# 14. EV-08 — Security Evidence

Examples include:

```text
Security Controls
Security Assessments
Access Reviews
Security Test Results
Vulnerability Assessments
Security Monitoring
```

Purpose:

```text
Support security control claims
Support cybersecurity relationships
Support assurance
```

---

# 15. EV-09 — Test / Validation Evidence

Examples include:

```text
Test Results
Acceptance Tests
Validation Records
Verification Records
Performance Tests
Integration Tests
```

Purpose:

```text
Support satisfaction
Support implementation validation
Support relationship validation
```

---

# 16. EV-10 — Audit / Assurance Evidence

Examples include:

```text
Audit Reports
Assurance Reviews
Compliance Assessments
Independent Reviews
Control Assessments
```

Purpose:

```text
Support assurance claims
Support control effectiveness
Support compliance claims
```

---

# 17. EV-11 — Measurement Evidence

Examples include:

```text
KPI Records
KRI Records
Performance Metrics
Availability Records
Capacity Records
Quality Measures
Maturity Measures
Outcome Measures
```

Purpose:

```text
Support measurement claims
Support performance claims
Support value assessment
```

---

# 18. EV-12 — Decision Evidence

Examples include:

```text
Architecture Decisions
Decision Records
Approval Records
Exception Decisions
Risk Acceptance Records
```

Purpose:

```text
Support architectural decisions
Support exceptions
Support rationale
Support accountability
```

---

# 19. EV-13 — Historical Evidence

Historical evidence may include:

```text
Archived Architecture Documents
Historical Configuration Records
Historical Decisions
Historical Operational Records
Historical Photographs / Diagrams where relevant
```

Historical evidence is retained where it materially supports:

```text
historical traceability
decision rationale
lifecycle reconstruction
change analysis
```

Historical evidence does not automatically establish current state.

---

# 20. Evidence Source Status

N2-D adopts the source-availability states already established under N2:

```text
AVAILABLE
UNAVAILABLE
NOT APPLICABLE
UNKNOWN
```

These states shall not be silently converted.

In particular:

```text
UNKNOWN ≠ UNAVAILABLE
UNAVAILABLE ≠ NOT APPLICABLE
```

---

# 21. Evidence Status

Evidence itself shall have a controlled status.

Initial status set:

```text
E1 — IDENTIFIED
E2 — AVAILABLE
E3 — ASSESSED
E4 — VALIDATED
E5 — ACCEPTED
E6 — STALE
E7 — RETIRED
E8 — REJECTED
```

Status describes evidence state, not the truth of the claim.

---

# 22. Evidence Confidence

Confidence represents the degree of confidence that the evidence appropriately supports the associated claim.

Initial confidence scale:

```text
C0 — UNKNOWN
C1 — LOW
C2 — MODERATE
C3 — HIGH
C4 — VERY HIGH
```

Confidence shall be assigned with reference to:

```text
source authority
evidence quality
currency
independence
consistency
validation
```

Confidence is not the same as evidence status.

---

# 23. Evidence Validity

Validity asks whether evidence is currently suitable for the claim it supports.

Validity states:

```text
V1 — VALID
V2 — CONDITIONAL
V3 — EXPIRED
V4 — INVALID
V5 — NOT ASSESSED
```

An evidence item may remain historically useful while no longer being valid for current-state claims.

---

# 24. Evidence Currency

Evidence currency shall be assessed according to the nature of the claim.

Examples:

```text
Current configuration
→ requires current or appropriately recent evidence

Historical decision
→ historical evidence may remain valid

Architecture principle
→ evidence may remain valid for longer periods

Operational status
→ normally requires current operational evidence
```

No universal expiry period is imposed by N2-D.

---

# 25. Evidence Authority

Evidence source authority shall be classified:

```text
A1 — Authoritative System / Record
A2 — Controlled Organizational Record
A3 — Approved Architecture / Governance Record
A4 — Operational Record
A5 — Secondary Source
A6 — Unverified Source
```

The classification shall not be interpreted as an automatic quality score.

Authority and confidence remain separate attributes.

---

# 26. Evidence Independence

Where appropriate, evidence should be assessed for independence.

Possible states:

```text
I0 — Not Assessed
I1 — Same-Source
I2 — Corroborated
I3 — Independent
```

Independence is particularly relevant for:

```text
assurance
audit
security
critical controls
high-materiality relationships
```

---

# 27. Evidence-to-Claim Relationship

The canonical relationship is:

```text
Evidence ──EVIDENCES──► Claim
```

A claim may be:

```text
Entity existence
Relationship existence
Ownership
Implementation
Operation
Control
Compliance
Performance
Value
```

The claim shall remain identifiable.

---

# 28. Evidence-to-Relationship Relationship

Evidence may support a specific relationship:

```text
Evidence
    │
    └──EVIDENCES──►
          Source ──RELATIONSHIP──► Target
```

This is important because evidence may support the relationship itself rather than merely the source or target entity.

---

# 29. Evidence-to-Entity Relationship

Evidence may also support entity existence or attributes:

```text
Evidence ──EVIDENCES──► Entity
```

Examples:

```text
Application Inventory
        ↓
EVIDENCES
        ↓
Application Entity
```

or:

```text
Configuration Record
        ↓
EVIDENCES
        ↓
Application ──USES──► Platform
```

---

# 30. Evidence Granularity

Evidence shall be captured at the smallest useful level.

Where one document supports multiple claims:

```text
One Evidence Record
        ↓
Multiple Evidence Links
```

should normally be preferred over:

```text
Duplicate copies of the same evidence
```

This reduces evidence duplication.

---

# 31. Evidence Bundle

Where a claim requires several pieces of evidence, an evidence bundle may be used.

```text
Evidence Bundle
 ├── Evidence A
 ├── Evidence B
 ├── Evidence C
 └── Assessment
```

The bundle is a logical grouping mechanism.

It is not a new architecture entity class.

---

# 32. Evidence Sufficiency

Evidence sufficiency shall be assessed against:

```text
Claim Type
Materiality
Traceability Depth
Risk
Lifecycle
Required Assurance
```

A low-materiality relationship may require limited evidence.

A critical relationship may require multiple independent sources.

---

# 33. Evidence and Materiality

The minimum evidence requirement shall scale with materiality.

Initial control guidance:

```text
M1 LOW
Basic supporting evidence where available

M2 MODERATE
Identifiable authoritative or controlled evidence

M3 HIGH
Validated evidence normally required

M4 CRITICAL
Validated and, where appropriate, corroborated or independent evidence
```

This complements the N2 depth model.

---

# 34. Evidence and Traceability Depth

Evidence requirements shall support the applicable traceability depth:

```text
D1 — Identity
D2 — Context
D3 — Relationship
D4 — Ownership
D5 — Evidence
D6 — Implementation
D7 — Operation
D8 — Measurement / Value
```

D5 is therefore the minimum level at which evidence itself becomes an explicit traceability requirement.

Higher depths may require evidence supporting implementation, operation or measurement.

---

# 35. Evidence Quality Assessment

An evidence assessment should consider:

```text
Relevance
Authority
Currency
Completeness
Consistency
Independence
Integrity
```

The assessment result shall be recorded where material.

---

# 36. Evidence Integrity

Evidence shall not be altered in a manner that changes its meaning without controlled versioning.

Where a source is externally maintained:

```text
Reference
Retrieval Date
Source Owner
Version / Revision
```

should be recorded where available.

---

# 37. Evidence Ownership

Evidence ownership and entity ownership are distinct.

For example:

```text
Application Owner
≠
Evidence Owner
```

unless explicitly established.

The evidence owner is responsible for maintaining or obtaining the evidence.

---

# 38. Evidence Review

Evidence shall be reviewed when:

```text
Claim materially changes
Source changes
Architecture changes
Implementation changes
Operational state changes
Evidence becomes stale
Control requires periodic review
```

Review frequency shall therefore be determined by claim and materiality rather than a universal calendar.

---

# 39. Evidence Retirement

Evidence may be retired when:

```text
Source is superseded
Claim is retired
Evidence is invalidated
Architecture element is retired
Retention requirement expires
```

Retirement shall preserve historical traceability where required.

---

# 40. Missing Evidence

Missing evidence shall be recorded explicitly.

The following states shall remain distinct:

```text
Evidence exists and is available
Evidence is known to exist but unavailable
Evidence has not been identified
Evidence is not applicable
Evidence is unknown
```

A missing evidence condition is a traceability gap.

It is not automatically an architecture defect.

---

# 41. Evidence Gap Types

N2-D establishes:

```text
EG-01 Missing Evidence
EG-02 Evidence Unavailable
EG-03 Evidence Not Identified
EG-04 Evidence Stale
EG-05 Evidence Invalid
EG-06 Evidence Insufficient
EG-07 Evidence Contradictory
EG-08 Evidence Ownership Missing
EG-09 Evidence Source Unclear
EG-10 Evidence Validation Missing
```

These are evidence-control findings.

---

# 42. Contradictory Evidence

Where evidence sources conflict:

```text
Evidence A
    ↘
     Claim
    ↗
Evidence B
```

the conflict shall be recorded.

The system shall not silently select one source.

Resolution should consider:

```text
Authority
Currency
Scope
Independence
Source quality
Governance authority
```

---

# 43. Evidence and Contradictory Relationships

If evidence conflicts with an existing relationship:

```text
Evidence Conflict
        ↓
Relationship Review
        ↓
Traceability Finding
        ↓
Controlled Resolution
```

N2 shall not silently modify the canonical architecture.

Any material architecture change must enter controlled change management.

---

# 44. Evidence and Orphans

An evidence item without a supported claim or controlled relationship is potentially an orphan.

Example:

```text
Evidence
   ↓
No Claim
No Entity
No Relationship
```

This should be investigated.

It does not automatically justify creating a new entity or relationship.

---

# 45. Evidence Provenance

Where practical, evidence provenance should capture:

```text
Origin
Source System
Source Owner
Creation Date
Modification Date
Retrieval Date
Version
Transformation
Reviewer
```

Provenance requirements shall scale with materiality.

---

# 46. Evidence Transformation

If evidence is transformed:

```text
Original Source
      ↓
Extraction
      ↓
Normalization
      ↓
Traceability Record
```

the transformation shall be recorded where it could affect interpretation.

The derived record shall not be confused with the original evidence.

---

# 47. Evidence Duplication Control

Duplicate evidence records should be avoided.

Where the same source supports multiple claims:

```text
Single controlled evidence item
        ↓
Multiple evidence relationships
```

is preferred.

A duplicate shall only be created when it represents materially different evidence context.

---

# 48. Evidence Repository Readiness

A future traceability repository should be capable of storing:

```text
Evidence ID
Evidence Type
Description
Source
Source Owner
Evidence Owner
Claim
Entity
Relationship
Created Date
Effective Date
Review Date
Status
Confidence
Validity
Authority
Materiality
Lifecycle
Reference
```

N2-D does not prescribe a technical database.

---

# 49. Evidence Assessment Record

A material evidence assessment should contain:

```text
Evidence ID
Assessment Date
Reviewer
Claim
Materiality
Authority
Currency
Completeness
Consistency
Independence
Confidence
Validity
Disposition
Comments
```

---

# 50. Evidence Acceptance

Evidence may be accepted when:

```text
Source is sufficiently identified
AND
Evidence is relevant
AND
Evidence is sufficiently authoritative
AND
Evidence is sufficiently current
AND
Evidence is consistent with available information
AND
Required validation has been performed
```

The exact threshold depends on materiality.

---

# 51. Evidence Rejection

Evidence may be rejected where:

```text
Source cannot be established
Evidence is demonstrably invalid
Evidence does not support the claim
Evidence is materially misleading
Evidence conflicts with authoritative evidence without resolution
```

Rejected evidence may remain historically recorded as rejected.

---

# 52. Evidence Lifecycle

The controlled lifecycle is:

```text
IDENTIFIED
    ↓
AVAILABLE
    ↓
ASSESSED
    ↓
VALIDATED
    ↓
ACCEPTED
    ↓
STALE / RETIRED
```

An evidence item may move to:

```text
REJECTED
```

at any assessment point where it fails the acceptance criteria.

---

# 53. Evidence Change Control

Changes to the evidence model require:

```text
Change Request
 ↓
Evidence Semantic Assessment
 ↓
Existing Model Review
 ↓
Impact Assessment
 ↓
Architecture Authority
 ↓
Approval
 ↓
Version Update
```

The evidence model shall not evolve through uncontrolled additions.

---

# 54. N2-D Pilot

The preferred pilot remains:

```text
CAN-01 — Enterprise Integration
```

The pilot shall test whether evidence can be associated with:

```text
Capability
Requirement
Architecture
Implementation
Service
Control
Relationship
Ownership
```

and whether the evidence states can be applied consistently.

---

# 55. N2-D Pilot Questions

The pilot shall answer:

```text
Can the source be identified?
Can the evidence be uniquely identified?
Can the supported claim be identified?
Can evidence support a relationship directly?
Can ownership be recorded?
Can currency be assessed?
Can authority be assessed?
Can confidence be assessed?
Can validity be assessed?
Can evidence gaps be detected?
Can contradictory evidence be detected?
Can historical evidence be retained without confusing current state?
```

---

# 56. N2-D Completion Criteria

N2-D may close when:

```text
Evidence model established
AND
Evidence types established
AND
Evidence status established
AND
Confidence model established
AND
Validity model established
AND
Authority model established
AND
Evidence-to-claim relationship established
AND
Evidence gap types established
AND
Evidence lifecycle established
AND
Evidence change control established
AND
Pilot readiness established
AND
No material evidence-model defect remains
AND
N2 Workstream Authority approves closure
```

---

# 57. N2-D Closure State

The formal closure state is:

```text
N2-D-SC-90 — EVIDENCE MODEL CLOSED
```

Closure means the evidence-control model is established.

It does not mean that all MFM evidence has been collected.

---

# 58. Anti-Runaway Control

N2-D shall not create:

```text
N2-D.01
N2-D.02
N2-D.03
...
```

merely to add more evidence categories.

The evidence model shall remain compact.

New evidence classes or controls require demonstrated material need.

---

# 59. Relationship to N2-E

The next planned semantic function is:

```text
N2-E — Traceability Status
```

However, N2-D has already defined evidence status.

Therefore N2-E shall not duplicate:

```text
Evidence Status
```

N2-E, if separately authorized, must focus on the broader status of traceability relationships and findings.

This distinction shall be preserved.

---

# 60. Relationship to N2-F

N2-A and N2-D already establish:

```text
Materiality
Traceability Depth
Evidence Requirements
```

Therefore N2-F shall be assessed for consolidation or refinement before a separate document is generated.

A planned work package is not automatically a document requirement.

---

# 61. Final N2-D Finding

> **N2-D.00 establishes the controlled evidence model for MFM Post-Steady-State traceability. It defines evidence as a controlled object linked explicitly to claims, entities and relationships, with controlled source status, evidence status, confidence, validity, authority, materiality, lifecycle and gap handling. The model supports implementation-oriented traceability while preserving the distinction between evidence, claim validity and architectural authority.**

---

# 62. Final N2-D Principle

> **Evidence shall support a specific traceability claim and shall be assessed according to its relevance, authority, currency, completeness, consistency and required level of assurance. Evidence existence alone shall never be treated as proof of correctness.**

---

# 63. Final N2-D Anti-Runaway Principle

> **Evidence modelling shall improve the reliability of traceability, not create an ever-expanding evidence taxonomy. New evidence categories or controls shall be introduced only when a material requirement cannot be satisfied by the existing model.**

---

# 64. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2-D.00 Evidence Model & Evidence Control  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-D.00-Evidence-Model-and-Evidence-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-D WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-C.00 — Relationship Catalogue Disposition & Consolidation Record  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-D — Evidence Model  
**Inherited Baseline:** MFM v1.2-Steady-State SC-90 Closure Baseline  
**Canonical Capabilities:** 8  
**Evidence Families:** 13  
**Evidence Statuses:** 8  
**Confidence Levels:** 5  
**Validity States:** 5  
**Evidence Gap Types:** 10  
**Pilot:** CAN-01 Enterprise Integration — RECOMMENDED / PENDING VALIDATION  
**N2-D Completion Gate:** REQUIRED  
**Automatic Successor Generation:** PROHIBITED  
**Closure State:** N2-D-SC-90 — EVIDENCE MODEL CLOSED
