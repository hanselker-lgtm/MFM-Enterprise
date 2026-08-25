# MFM Post-Steady-State Phase Control

## N6-B — Requirement-to-Architecture Traceability

**Control ID:** MFM-Post-Steady-State-Phase-Control-N6-B-Requirement-to-Architecture-Traceability-001  
**Version:** 1.0  
**Status:** ACTIVE — N6-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N6 — Architecture Traceability Matrix  
**Parent:** N6 — Architecture Traceability Matrix  
**Predecessor:** N6-A — Traceability Model & Data Structure  
**Authorization:** N6-B AUTHORIZED  
**Next Work Package:** N6-C — Architecture-to-Implementation Traceability  

---

# 1. Purpose

N6-B establishes the controlled requirement-to-architecture traceability layer.

The purpose is to determine, record and validate the relationships between:

```text
Requirement
    ↓
Capability
    ↓
Architecture Domain
    ↓
Architecture Element
```

The work package shall provide controlled forward and backward traceability without treating a relationship as proof of implementation, operation or effectiveness.

---

# 2. N6-A Dependency

N6-B uses the model established in N6-A:

```text
Object Model
Relationship Vocabulary
Relationship Semantics
Identifiers
Cardinality
Lifecycle
Evidence Classes
Validation States
Matrix Schema
False-Gap Controls
```

N6-B shall not silently redefine the N6-A relationship semantics.

Any material model change shall be explicitly recorded and controlled.

---

# 3. Requirement Traceability Objective

For each material requirement, N6-B seeks to establish:

```text
WHERE DID THE REQUIREMENT COME FROM?
        ↓
WHAT CAPABILITY DOES IT AFFECT?
        ↓
WHICH ARCHITECTURE DOMAIN IS RELEVANT?
        ↓
WHICH ARCHITECTURE ELEMENT ADDRESSES IT?
```

The reverse question is equally important:

```text
WHY DOES THIS ARCHITECTURE ELEMENT EXIST?
        ↓
WHICH CAPABILITY DOES IT SUPPORT?
        ↓
WHICH REQUIREMENT OR SOURCE RATIONALE SUPPORTS IT?
```

---

# 4. Scope

N6-B covers:

```text
Requirement Identification
Requirement Classification
Requirement Source Traceability
Requirement-to-Capability Relationships
Capability-to-Architecture Relationships
Requirement-to-Architecture Relationships
Forward Traceability
Backward Traceability
Coverage Analysis
Orphan Detection
Relationship Validation
Evidence Reference
Traceability Findings
```

N6-B does not perform:

```text
Implementation Traceability
Service Realization Traceability
Operational Effectiveness Assessment
Control Effectiveness Assessment
Architecture Redesign
New Capability Design
```

Those belong to later or separately authorized activities.

---

# 5. Requirement Object Baseline

The N6-A requirement object is:

```text
Requirement ID
Requirement Name
Requirement Statement
Requirement Type
Source
Priority
Owner
Applicability
Status
Lifecycle
Evidence Reference
```

N6-B may add traceability-specific fields:

```text
Capability Relationship
Architecture Relationship
Coverage Status
Traceability Status
Finding Reference
Validation State
```

---

# 6. Requirement Classification

Requirements may be classified as:

```text
Business
Strategic
Regulatory
Contractual
Security
Data
Operational
Architecture
Technology
Risk
Compliance
Service
```

Classification shall be based on the source.

Where classification cannot be established:

```text
UNCLASSIFIED
```

shall be used rather than inventing a category.

---

# 7. Requirement Source

Each material requirement should preserve:

```text
Requirement ID
Source Document
Source Section
Source Location
Source Version
Source Date
Originating Authority
```

The source relationship is essential for backward traceability.

---

# 8. Requirement-to-Capability Relationship

The primary relationship is:

```text
Requirement
    ↓
SATISFIES / SUPPORTS
    ↓
Capability
```

The semantic interpretation must remain controlled.

A capability may:

```text
SATISFY
```

or:

```text
SUPPORT
```

a requirement depending on the actual relationship.

No relationship shall be upgraded from `SUPPORTS` to `SATISFIES` without evidence.

---

# 9. Capability Object Baseline

The N6-A capability object is:

```text
Capability ID
Capability Name
Business Outcome
Description
Owner
Source Requirement
Status
Lifecycle
Evidence Reference
```

N6-B adds:

```text
Requirement Relationship
Architecture Relationship
Coverage State
Validation State
Finding Reference
```

---

# 10. Capability-to-Architecture Relationship

The primary relationship is:

```text
Capability
    ↓
SUPPORTS
    ↓
Architecture Element
```

or, where justified:

```text
Capability
    ↓
SATISFIES
    ↓
Architecture Element
```

The relationship must be supported by source architecture material.

---

# 11. Architecture Domain Relationship

Each capability shall be assessed against applicable architecture domains:

```text
Business
Information
Application
Technology
Security
Data
Integration
AI / Agent
Infrastructure
Service
Operational
```

The relationship may be:

```text
APPLICABLE
NOT APPLICABLE
UNVERIFIED
```

Only materially relevant domains shall be populated.

---

# 12. Architecture Element Relationship

A material architecture element should establish:

```text
Element ID
Element Name
Element Type
Architecture Domain
Description
Owner
Lifecycle
Status
Source
Evidence
```

N6-B establishes upstream traceability:

```text
Requirement
 ↓
Capability
 ↓
Architecture Element
```

---

# 13. Forward Traceability

Forward traceability answers:

```text
Requirement
 ↓
Capability
 ↓
Architecture
```

The expected status is:

```text
TRACEABLE
```

where the relationships are established and validated.

Potential states:

```text
TRACEABLE
PARTIALLY TRACEABLE
UNVERIFIED
NOT APPLICABLE
BROKEN
```

---

# 14. Backward Traceability

Backward traceability answers:

```text
Architecture Element
 ↓
Capability
 ↓
Requirement / Source Rationale
```

Potential states:

```text
TRACEABLE
PARTIALLY TRACEABLE
UNVERIFIED
NO UPSTREAM SOURCE IDENTIFIED
```

`NO UPSTREAM SOURCE IDENTIFIED` is not automatically a defect.

Applicability and evidence must be assessed first.

---

# 15. Requirement Coverage

N6-B shall assess each material requirement:

```text
COVERED
PARTIALLY COVERED
NOT COVERED
UNVERIFIED
NOT APPLICABLE
```

Definitions:

```text
COVERED
A defensible capability/architecture relationship exists.

PARTIALLY COVERED
Only part of the requirement is represented.

NOT COVERED
No applicable architecture relationship has been established.

UNVERIFIED
Available material is insufficient to determine coverage.

NOT APPLICABLE
Requirement is demonstrably outside the assessed architecture scope.
```

---

# 16. Architecture Coverage

N6-B shall assess whether material architecture elements have upstream rationale:

```text
ARCHITECTURE ELEMENT
        ↓
CAPABILITY
        ↓
REQUIREMENT / SOURCE RATIONALE
```

Potential results:

```text
JUSTIFIED
PARTIALLY JUSTIFIED
UNVERIFIED
NO SOURCE IDENTIFIED
```

---

# 17. Orphan Requirement Detection

Potential orphan requirement:

```text
Requirement
    ↓
[NO CAPABILITY RELATIONSHIP]
```

Before classification, N6-B shall assess:

```text
Applicability
Intent
Scope
Evidence
Materiality
```

Possible result:

```text
VALID ORPHAN
UNVERIFIED
NOT APPLICABLE
TRACEABILITY GAP
```

---

# 18. Orphan Capability Detection

Potential orphan capability:

```text
Capability
    ↓
[NO REQUIREMENT / SOURCE RELATIONSHIP]
```

This shall not automatically be treated as invalid.

Potential reasons include:

```text
Strategic capability
Regulatory capability
Emergent capability
Foundational capability
Architecture enablement
Source material incomplete
```

The actual reason must be supported before being recorded.

---

# 19. Orphan Architecture Detection

Potential orphan architecture element:

```text
Architecture Element
    ↓
[NO CAPABILITY / REQUIREMENT / PRINCIPLE RELATIONSHIP]
```

N6-B shall assess whether the element is:

```text
Foundational
Enabling
Technical
Shared
Legacy
Required by external constraint
Unverified
```

No rationale shall be invented.

---

# 20. Relationship Validation

Each relationship shall be assigned:

```text
PROPOSED
ESTABLISHED
VALIDATED
CONDITIONAL
UNVERIFIED
CONFLICTING
SUPERSEDED
RETIRED
```

N6-B shall prefer:

```text
UNVERIFIED
```

where evidence is insufficient.

---

# 21. Evidence Requirement

A material traceability claim should retain:

```text
Source Reference
Evidence Reference
Evidence Class
Validation State
```

Evidence classes remain:

```text
E0 — Conceptual
E1 — Architectural
E2 — Governance / Implementation Model
E3 — Actual Implementation
```

For N6-B:

```text
Architecture Relationship
→ normally E1 or stronger

Actual Implementation Relationship
→ outside N6-B primary scope and requires E3 where claimed
```

---

# 22. Traceability Claim Boundary

N6-B shall not convert:

```text
Architecture Relationship
```

into:

```text
Implementation Relationship
```

or:

```text
Implementation Relationship
```

into:

```text
Operational Effectiveness
```

The chain remains:

```text
TRACEABILITY
→
EVIDENCE
→
VALIDATION
→
EFFECTIVENESS
```

Each step requires appropriate evidence.

---

# 23. Requirement Traceability Matrix

The controlled N6-B matrix is:

| Field | Description |
|---|---|
| Trace ID | Unique relationship ID |
| Requirement ID | Source requirement |
| Requirement Type | Requirement classification |
| Requirement Source | Origin |
| Capability ID | Related capability |
| Architecture Domain | Relevant domain |
| Architecture Element ID | Related architecture element |
| Relationship | Semantic relationship |
| Coverage | Coverage state |
| Validation | Validation state |
| Evidence | Supporting evidence |
| Owner | Traceability owner |
| Lifecycle | Lifecycle state |
| Finding | Related finding |
| Change Reference | Related change |

---

# 24. Requirement-to-Capability Matrix

| Requirement | Relationship | Capability | Status |
|---|---|---|---|
| REQ-* | SATISFIES / SUPPORTS | CAP-* | TBD |

This is a controlled structure.

Actual MFM requirement IDs and capability IDs shall only be populated from authorized source material.

---

# 25. Capability-to-Architecture Matrix

| Capability | Relationship | Architecture Element | Domain | Status |
|---|---|---|---|---|
| CAP-* | SUPPORTS / SATISFIES | ARC-* | TBD | TBD |

---

# 26. End-to-End Requirement Trace

| Requirement | Capability | Architecture | Coverage | Validation |
|---|---|---|---|---|
| REQ-* | CAP-* | ARC-* | TBD | TBD |

The matrix shall preserve both positive and unresolved states.

---

# 27. Traceability Confidence

Where the implementation supports confidence classification, the following may be used:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

Confidence is not a substitute for evidence.

---

# 28. Conflicting Relationships

Where sources provide contradictory relationships:

```text
CONFLICTING
```

shall be recorded.

N6-B shall preserve:

```text
Source A
vs.
Source B
```

until the conflict is resolved by the appropriate authority or evidence.

---

# 29. Requirement Change Impact

A changed requirement may affect:

```text
Requirement
 ↓
Capability
 ↓
Architecture Domain
 ↓
Architecture Element
```

N6-B shall establish this upstream traceability.

Implementation and service impact shall be handled by N6-C.

---

# 30. Requirement Lifecycle

Requirement lifecycle may be:

```text
PROPOSED
DEFINED
APPROVED
ACTIVE
SUPERSEDED
RETIRED
UNKNOWN
```

Lifecycle state shall be supported by source material.

---

# 31. Capability Lifecycle

Capability lifecycle may be:

```text
PROPOSED
DEFINED
APPROVED
ACTIVE
SUPERSEDED
RETIRED
UNKNOWN
```

A capability's existence shall not be inferred from a single architecture component.

---

# 32. Architecture Lifecycle

Architecture element lifecycle may be:

```text
PROPOSED
DEFINED
APPROVED
IMPLEMENTED
ACTIVE
VALIDATED
SUPERSEDED
RETIRED
UNKNOWN
```

N6-B shall not assert `IMPLEMENTED` merely because an architecture element is defined.

---

# 33. Traceability Completeness

N6-B shall distinguish:

```text
MODEL COMPLETE
```

from:

```text
TRACEABILITY DATA COMPLETE
```

and:

```text
TRACEABILITY VALIDATED
```

These are separate states.

---

# 34. Traceability Quality Rules

N6-B shall assess:

```text
Completeness
Correctness
Consistency
Currency
Source Integrity
Relationship Semantics
Lifecycle Accuracy
Evidence Quality
Coverage
```

---

# 35. False-Gap Protection

The following are prohibited:

```text
Missing requirement
→ invented requirement

Missing capability
→ invented capability

Missing relationship
→ assumed relationship

Missing source
→ invented source

Missing evidence
→ synthetic evidence

Unverified coverage
→ automatic failure

Untraceable element
→ automatic invalidity
```

---

# 36. N6-B Findings

Potential finding classes:

```text
N6-B-F01 Requirement Orphan
N6-B-F02 Capability Orphan
N6-B-F03 Architecture Orphan
N6-B-F04 Broken Requirement Chain
N6-B-F05 Broken Capability Chain
N6-B-F06 Conflicting Traceability
N6-B-F07 Missing Source
N6-B-F08 Missing Evidence
N6-B-F09 Invalid Relationship Semantics
N6-B-F10 Lifecycle Inconsistency
N6-B-F11 Coverage Gap
N6-B-F12 Material Traceability Gap
N6-B-F13 Unverified Relationship
```

Not every detection is a finding.

---

# 37. Finding Materiality

Potential findings shall be assessed:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

Factors include:

```text
Business Impact
Strategic Impact
Compliance Impact
Security Impact
Operational Impact
Architecture Impact
Risk
Dependency
Reversibility
```

---

# 38. N5 Condition Carry-Forward

N6-B shall preserve:

```text
COND-N5-01
Authority/accountability remains evidence-based.

COND-N5-02
Decision rights remain evidence-based.

COND-N5-03
Control operation/effectiveness remains evidence-dependent.

COND-N5-04
Compliance status remains evidence-dependent.

COND-N5-05
Assurance conclusions remain evidence-dependent.

COND-N5-06
Organizational implementation remains evidence-dependent.
```

---

# 39. N6-B Deliverables

N6-B shall produce:

```text
D-B01
Requirement Catalogue

D-B02
Requirement Classification

D-B03
Requirement Source Register

D-B04
Requirement-to-Capability Matrix

D-B05
Capability-to-Architecture Matrix

D-B06
Requirement-to-Architecture Matrix

D-B07
Forward Traceability Assessment

D-B08
Backward Traceability Assessment

D-B09
Coverage Assessment

D-B10
Orphan / Broken Chain Register

D-B11
Traceability Findings Register

D-B12
N6-B Completion Recommendation
```

---

# 40. N6-B Completion Criteria

N6-B may be considered complete when:

```text
Material Requirements Identified
AND
Requirement Sources Recorded
AND
Requirement Classification Completed
AND
Requirement-to-Capability Relationships Assessed
AND
Capability-to-Architecture Relationships Assessed
AND
Forward Traceability Assessed
AND
Backward Traceability Assessed
AND
Coverage Assessed
AND
Orphans Assessed
AND
Broken Chains Assessed
AND
Conflicts Assessed
AND
Evidence Boundaries Preserved
AND
N6-C Input Prepared
```

---

# 41. N6-B Current State

```text
N6-B
=
ACTIVE
```

This work package establishes the controlled requirement-to-architecture traceability layer.

Actual population shall remain source-driven and evidence-based.

---

# 42. Next Work Package

Upon N6-B completion:

```text
N6-C
Architecture-to-Implementation Traceability
```

N6-C shall extend the traceability chain:

```text
Architecture
 ↓
Solution
 ↓
Implementation
 ↓
Service
```

N6-C shall not rewrite the N6-A/N6-B model without controlled change.

---

# 43. Current Program State

```text
N2
= CLOSED / N2C-2

N3
= CLOSED / N3C-2

N4
= CLOSED / N4C-2

N5
= CLOSED / N5C-2
  COMPLETE WITH CONDITIONS

N5 CONDITIONS
= ACTIVE CARRY-FORWARD

N6
= AUTHORIZED / ACTIVE

N6.00
= COMPLETED

N6-A
= COMPLETED / MODEL ESTABLISHED

N6-B
= ACTIVE

N6-C
= AUTHORIZED / SCHEDULED

N6-D
= AUTHORIZED / SCHEDULED

N6-E
= AUTHORIZED / SCHEDULED
```

---

# 44. Final N6-B Statement

> **N6-B establishes the controlled requirement-to-architecture traceability layer for the authorized N6 Architecture Traceability Matrix. It assesses requirement sources, requirement classification, requirement-to-capability relationships, capability-to-architecture relationships, forward and backward traceability, coverage, orphan conditions, broken chains, conflicts and evidence boundaries. N6-B does not infer implementation, operational status or effectiveness from architectural traceability. Actual implementation and service traceability remain within N6-C.**

---

# 45. Document Control

**Document:** MFM Post-Steady-State Phase Control — N6-B Requirement-to-Architecture Traceability  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N6-B-Requirement-to-Architecture-Traceability-001  
**Version:** 1.0  
**Status:** ACTIVE — N6-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N6 — Architecture Traceability Matrix  
**Parent:** N6 — Architecture Traceability Matrix  
**Predecessor:** N6-A — Traceability Model & Data Structure  
**Authorization:** N6-B AUTHORIZED  
**Current Work Package:** N6-B  
**Next Work Package:** N6-C — Architecture-to-Implementation Traceability  
**Automatic Scope Expansion:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
