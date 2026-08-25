# MFM Post-Steady-State Phase Control
## N2-G.00 — Gap, Orphan & Traceability Finding Model

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-G.00-Gap-Orphan-and-Traceability-Finding-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-G WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-F.00 — Materiality & Traceability Depth Disposition Record  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-G — Gap & Orphan Model  
**State:** N2-G.00 — GAP / ORPHAN MODEL ESTABLISHMENT

---

# 1. Purpose

N2-G.00 establishes the controlled model for identifying, classifying, assessing, resolving and closing traceability gaps, orphaned objects and related findings.

The purpose is not to prove that the MFM architecture is complete.

The purpose is to determine whether the defined traceability relationships are sufficiently represented for the applicable:

```text
Materiality
Traceability Depth
Evidence
Status
Lifecycle
Scope
```

N2-G therefore provides the diagnostic layer between the traceability model and the later pilot/validation activities.

---

# 2. Governing Chain

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
        ↓
N2-E.00 — TRACEABILITY STATUS & STATE CONTROL
        ↓
N2-F.00 — MATERIALITY / DEPTH DISPOSITION
        ↓
N2-G.00 — GAP, ORPHAN & TRACEABILITY FINDING MODEL
```

N2-G consumes the controls already established by N2-A through N2-F.

It does not create competing status, evidence, materiality or depth vocabularies.

---

# 3. Core Principle

A traceability gap is:

> **A materially required traceability condition that is absent, insufficient, contradictory, stale or otherwise not controlled to the required level.**

An orphan is:

> **An entity, relationship or evidence object that lacks a materially required connection to the controlled traceability model.**

A finding is:

> **A formally recorded condition requiring assessment, action, acceptance or closure.**

---

# 4. Gap vs Orphan vs Finding

These concepts shall remain distinct.

```text
GAP
=
A required traceability condition is missing or insufficient.

ORPHAN
=
An object lacks a required relationship.

FINDING
=
The controlled record of a detected condition.
```

Example:

```text
Implementation exists
        ↓
No architecture relationship
        ↓
ORPHAN / GAP
        ↓
FINDING
```

The finding is the management object.

---

# 5. Gap Model

N2-G establishes the following gap classes:

```text
G01 — Missing Entity
G02 — Missing Relationship
G03 — Missing Evidence
G04 — Insufficient Depth
G05 — Missing Ownership
G06 — Stale Traceability
G07 — Invalid Traceability
G08 — Contradictory Traceability
G09 — Missing Implementation Link
G10 — Missing Operational Link
G11 — Missing Measurement / Value Link
G12 — Validation Gap
```

These are controlled finding classifications.

They are not new architecture entity classes.

---

# 6. G01 — Missing Entity

A required entity is absent from the controlled traceability model.

Examples:

```text
Required Capability
Required Requirement
Required Architecture Element
Required Implementation Element
Required Service
Required Control
```

A missing entity must first be confirmed as genuinely required.

The absence of documentation alone does not prove that an entity is missing.

---

# 7. G02 — Missing Relationship

Both source and target exist, but the required relationship is absent.

Example:

```text
Architecture Element
        ↓
Implementation Element

Required IMPLEMENTS relationship
        ↓
Missing
```

This is one of the primary N2 traceability findings.

---

# 8. G03 — Missing Evidence

A required relationship or claim exists, but appropriate evidence is unavailable or has not been identified.

The evidence states from N2-D remain authoritative.

Possible underlying conditions:

```text
Evidence not identified
Evidence unavailable
Evidence stale
Evidence insufficient
Evidence invalid
```

N2-G records the finding; N2-D governs the evidence semantics.

---

# 9. G04 — Insufficient Depth

The traceability exists but does not reach the required depth.

Example:

```text
Requirement
 ↓
Capability
 ↓
Architecture
```

where materiality requires:

```text
Implementation
Operation
```

This is a depth finding, not necessarily a missing relationship at the existing level.

---

# 10. G05 — Missing Ownership

A materially controlled object or relationship lacks required ownership.

Examples:

```text
Capability with no accountable owner
Relationship with no responsible authority
Evidence with no evidence owner
Finding with no finding owner
```

Ownership requirements derive from the existing N2 model.

---

# 11. G06 — Stale Traceability

A relationship or evidence record was previously valid but is no longer sufficiently current.

Examples:

```text
Architecture changed
Implementation changed
Service retired
Owner changed
Configuration changed
```

Staleness does not automatically mean that the historical relationship was incorrect.

---

# 12. G07 — Invalid Traceability

The relationship or claim is determined to be invalid.

Examples:

```text
Wrong source
Wrong target
Wrong relationship type
Unsupported claim
Retired implementation represented as active
```

Invalid traceability requires controlled correction or retirement.

---

# 13. G08 — Contradictory Traceability

Two or more controlled sources produce materially conflicting traceability information.

Examples:

```text
Owner A ≠ Owner B
Architecture Mapping A ≠ Architecture Mapping B
Lifecycle A ≠ Lifecycle B
Dependency Direction A ≠ Dependency Direction B
```

Contradictions require resolution rather than silent selection.

---

# 14. G09 — Missing Implementation Link

Architecture exists and implementation may exist, but the traceability chain does not establish how implementation realizes the architecture.

Typical relationship:

```text
Implementation
    ──IMPLEMENTS──►
Architecture
```

The finding is especially important for M3/M4 objects.

---

# 15. G10 — Missing Operational Link

Implementation exists but operation is not sufficiently traceable.

Example:

```text
Application
 ↓
Service
 ↓
Operation
```

where the operational relationship is materially required but absent.

---

# 16. G11 — Missing Measurement / Value Link

A materially significant traceability chain requires measurement or value representation, but the required link is absent.

Example:

```text
Capability
 ↓
Outcome
 ↓
Value

Measurement link missing
```

This does not mean every capability requires a financial KPI.

The required depth determines applicability.

---

# 17. G12 — Validation Gap

A relationship or chain has sufficient evidence for support but has not completed the required validation.

Example:

```text
Relationship = T3 VERIFIED
Required = T4 VALIDATED
```

This is a validation gap.

---

# 18. Orphan Classes

N2-G establishes:

```text
O01 — Entity Orphan
O02 — Relationship Orphan
O03 — Evidence Orphan
O04 — Measurement Orphan
O05 — Control Orphan
O06 — Implementation Orphan
O07 — Service Orphan
```

An orphan is identified only when the missing connection is materially required.

---

# 19. O01 — Entity Orphan

An entity exists in the catalogue but lacks required relationships.

Examples:

```text
Capability
    ↓
No requirement
No architecture
No relevant outcome
```

The absence of every possible relationship is not required for an orphan finding.

Only materially required relationships count.

---

# 20. O02 — Relationship Orphan

A relationship record exists but its source or target cannot be resolved to a valid controlled entity.

Example:

```text
REL-123
Source = unresolved
Target = ARC-004
```

This is a relationship-integrity problem.

---

# 21. O03 — Evidence Orphan

Evidence exists but has no controlled claim, entity or relationship to which it contributes.

Example:

```text
Evidence
   ↓
No linked claim
No linked entity
No linked relationship
```

It should be assessed before being deleted or retained.

---

# 22. O04 — Measurement Orphan

A measurement exists without a valid measured object.

Example:

```text
KPI-001
   ↓
No service
No capability
No outcome
No value relationship
```

The measurement may still be valid operationally, but its traceability context is incomplete.

---

# 23. O05 — Control Orphan

A control exists without a clearly identified controlled object or purpose.

Example:

```text
Control
   ↓
No controlled asset
No requirement
No risk
No policy relationship
```

This requires assessment.

---

# 24. O06 — Implementation Orphan

An implementation object exists without the required architecture relationship.

Example:

```text
Application
   ↓
No IMPLEMENTS / REALIZES relationship
```

This is one of the most important implementation traceability orphan conditions.

---

# 25. O07 — Service Orphan

A service exists but cannot be connected to its supporting implementation, capability, consumer or operational context where those links are materially required.

---

# 26. Finding Record

Every material gap or orphan finding shall be represented by:

```text
Finding ID
Finding Type
Object
Source
Target
Description
Materiality
Required Depth
Current Depth
Current Status
Required Status
Evidence
Owner
Risk
Action
Due / Review Date
Disposition
Closure Evidence
```

---

# 27. Finding Identity

Example:

```text
FND-001
TYPE = G09 Missing Implementation Link
OBJECT = IMP-001
MATERIALITY = M3
REQUIRED DEPTH = D6
CURRENT DEPTH = D5
CURRENT STATUS = T2
REQUIRED STATUS = T4
```

This is an illustrative model example only.

---

# 28. Finding Status

N2-E established the authoritative finding status:

```text
F0 — IDENTIFIED
F1 — ASSESSED
F2 — ACTION REQUIRED
F3 — ACTION IN PROGRESS
F4 — MITIGATED
F5 — ACCEPTED
F6 — CLOSED
F7 — REJECTED / NOT A GAP
```

N2-G adopts this vocabulary.

It does not create a competing finding-status model.

---

# 29. Finding Severity

Severity shall be derived from:

```text
Materiality
Impact
Required Depth
Risk
Dependency Criticality
```

Initial severity:

```text
S1 — LOW
S2 — MODERATE
S3 — HIGH
S4 — CRITICAL
```

Severity is not identical to materiality.

Materiality describes the importance of the object/relationship.

Severity describes the consequence of the detected finding.

---

# 30. Finding Priority

Priority may be:

```text
P1 — IMMEDIATE
P2 — HIGH
P3 — NORMAL
P4 — LOW
```

Priority may consider:

```text
Severity
Business timing
Dependency
Risk
Operational urgency
```

---

# 31. Gap Assessment

A gap shall be assessed against:

```text
Is the relationship actually required?
What materiality applies?
What depth is required?
What evidence is available?
What status is required?
What risk exists?
Who owns resolution?
```

This prevents false gaps.

---

# 32. False Gap

A suspected gap shall be classified as:

```text
F7 — REJECTED / NOT A GAP
```

when assessment demonstrates that:

```text
relationship is not required
OR
depth is not required
OR
object is not applicable
OR
existing traceability already satisfies the requirement
```

The reason shall be recorded.

---

# 33. Gap vs Not Applicable

The distinction is:

```text
GAP
=
Required but absent/insufficient.

NOT APPLICABLE
=
Not required for the defined scope.
```

Not Applicable shall not be treated as a missing traceability condition.

---

# 34. Gap vs Unknown

The distinction is:

```text
UNKNOWN
=
Condition has not yet been determined.

GAP
=
Assessment has determined that a required condition is absent or insufficient.
```

Unknown shall not automatically be recorded as a gap.

---

# 35. Gap vs Unavailable Evidence

Evidence may be known to exist but unavailable.

This should be represented as:

```text
Evidence condition
+
Traceability finding if materially required
```

It should not automatically be converted into:

```text
Architecture defect
```

---

# 36. Orphan Detection Rules

An orphan may be detected when:

```text
Entity exists
AND
Required relationship count = 0
```

or:

```text
Relationship exists
AND
Source / Target cannot be resolved
```

or:

```text
Evidence exists
AND
No supported claim can be identified
```

The detection logic must use materiality and scope.

---

# 37. Required Relationship Matrix

A future repository may define expected relationships by entity class.

Conceptual example:

| Entity | Required / Typical Relationship |
|---|---|
| Capability | Requirement, Architecture, Outcome |
| Requirement | Stakeholder, Capability, Architecture |
| Architecture | Capability, Requirement, Implementation |
| Implementation | Architecture, Service |
| Service | Capability, Implementation, Operation |
| Control | Requirement/Risk/Asset, Evidence |
| Evidence | Claim, Entity or Relationship |
| Measurement | Object measured, Outcome/Value where applicable |

This is a validation model, not a universal mandatory relationship list.

---

# 38. Gap Detection Principle

The system shall not ask:

```text
Does this object have every possible relationship?
```

It shall ask:

```text
Does this object have every materially required relationship for its scope?
```

This is a central anti-overdocumentation rule.

---

# 39. Gap Detection by Depth

If:

```text
Current Depth = D4
Required Depth = D6
```

the finding is:

```text
G04 — Insufficient Depth
```

The system should identify the missing levels:

```text
D5 Evidence
D6 Implementation
```

rather than creating two unrelated gaps.

---

# 40. Gap Detection by Status

If:

```text
Current Status = T2
Required Status = T4
```

the finding may be:

```text
G12 — Validation Gap
```

provided that evidence and scope otherwise support the relationship.

---

# 41. Gap Detection by Ownership

If:

```text
Relationship exists
Evidence exists
Status = T3
Owner = missing
```

the finding is:

```text
G05 — Missing Ownership
```

not:

```text
Missing Relationship
```

---

# 42. Gap Detection by Evidence

If:

```text
Relationship exists
Owner exists
Required depth = D5
Evidence = absent
```

the finding is:

```text
G03 — Missing Evidence
```

---

# 43. Contradiction Detection

A contradiction shall be recorded where controlled information materially conflicts.

Example:

```text
Source A:
Application implements ARC-001

Source B:
Application implements ARC-002
```

The finding is:

```text
G08 — Contradictory Traceability
```

Resolution must determine whether:

```text
A is correct
B is correct
Both are valid in different contexts
One is historical
Neither is correct
```

---

# 44. Finding Evidence

A finding shall itself be evidence-backed.

The finding should record:

```text
Detection Evidence
Assessment Evidence
Resolution Evidence
Closure Evidence
```

where applicable.

---

# 45. Finding Ownership

Every material finding shall have:

```text
Finding Owner
```

The owner is responsible for:

```text
Assessment
Action
Disposition
Closure
```

Ownership may be transferred through controlled change.

---

# 46. Finding Resolution

Resolution paths are:

```text
R1 — Correct
R2 — Add Missing Relationship
R3 — Add / Obtain Evidence
R4 — Assign Ownership
R5 — Increase Traceability Depth
R6 — Validate
R7 — Retire
R8 — Accept Risk / Exception
R9 — Mark Not Applicable
R10 — Reject Finding
```

---

# 47. Finding Closure

A finding may close when:

```text
Required condition restored
OR
Approved exception exists
OR
Object/relationship retired
OR
Finding formally rejected
OR
Condition confirmed not applicable
```

Closure shall have supporting evidence where material.

---

# 48. Open Finding Control

Open findings shall remain visible until:

```text
F4 MITIGATED
F5 ACCEPTED
F6 CLOSED
F7 REJECTED
```

Documentation of an open finding is not closure.

---

# 49. Finding Aging

Where useful, findings may track:

```text
Created Date
Age
Target Date
Review Date
Escalation Date
```

Aging is a management attribute.

It does not alter severity automatically.

---

# 50. Finding Escalation

Escalation may occur when:

```text
Criticality increases
Target date is exceeded
Risk increases
Dependency becomes critical
Evidence deteriorates
Owner cannot resolve
```

Escalation shall be governed by the appropriate authority.

---

# 51. Risk Integration

A finding may create or increase a risk.

The chain is:

```text
Finding
 ↓
Risk
 ↓
Control / Remediation
 ↓
Evidence
 ↓
Closure
```

A finding is not itself automatically a risk.

---

# 52. Change Integration

A finding may identify a need for architecture or implementation change.

The chain becomes:

```text
Finding
 ↓
Change Request
 ↓
Impact Assessment
 ↓
Approved Change
 ↓
Implementation
 ↓
Verification
 ↓
Finding Closure
```

N2-G does not authorize architectural change itself.

---

# 53. Historical Findings

Historical findings may be retained where useful.

They may be marked:

```text
Lifecycle = ARCHIVED
Status = F6 CLOSED
```

Historical closure does not imply that the current architecture has the same state.

---

# 54. Finding Reporting

A future traceability report may show:

```text
Total Findings
Open Findings
Critical Findings
Findings by Type
Findings by Capability
Findings by Owner
Findings by Materiality
Findings by Severity
Findings by Age
Findings by Status
```

These are reporting capabilities.

---

# 55. Pilot

The preferred pilot remains:

```text
CAN-01 — Enterprise Integration
```

The pilot shall deliberately test:

```text
At least one missing relationship
At least one missing evidence condition
At least one orphan
At least one ownership gap
At least one insufficient-depth condition
At least one validation gap
```

If such cases naturally exist, they shall be used.

Artificial defects shall not be introduced into the production baseline merely to demonstrate the model.

---

# 56. Pilot Questions

The pilot shall determine:

```text
Can gaps be distinguished from unknown conditions?
Can gaps be distinguished from not-applicable conditions?
Can orphans be detected reliably?
Can false gaps be rejected?
Can findings be linked to materiality?
Can required depth be determined?
Can findings be evidence-backed?
Can findings be assigned to owners?
Can findings be resolved without changing architecture unnecessarily?
Can findings be closed with evidence?
Can historical findings be retained?
```

---

# 57. N2-G Completion Criteria

N2-G may close when:

```text
Gap model established
AND
Orphan model established
AND
Finding model established
AND
Gap classifications established
AND
Orphan classifications established
AND
Finding status reused from N2-E
AND
Materiality reused from N2-A
AND
Depth reused from N2-A
AND
Evidence controls reused from N2-D
AND
Resolution model established
AND
Closure rules established
AND
Pilot requirements established
AND
No material gap/orphan-model defect remains
AND
N2 Workstream Authority approves closure
```

---

# 58. N2-G Closure State

The formal closure state is:

```text
N2-G-SC-90 — GAP / ORPHAN MODEL CLOSED
```

Closure means the diagnostic model is established.

It does not mean that all MFM traceability gaps have been resolved.

---

# 59. Relationship to N2-H

N2-H is the pilot traceability work package.

N2-G provides the diagnostic mechanism used during the pilot:

```text
Traceability
      ↓
Gap / Orphan Detection
      ↓
Finding
      ↓
Resolution / Acceptance
      ↓
Validation
```

---

# 60. Relationship to N2-I

N2-I shall validate whether:

```text
Gaps are detected correctly
Orphans are detected correctly
False gaps are rejected
Findings are managed correctly
Closure is reliable
```

N2-G therefore provides one of the principal validation surfaces for N2.

---

# 61. Relationship to N2-J

N2-J is the final N2 completion assessment.

N2-J should assess:

```text
Open findings
Unresolved critical gaps
Accepted exceptions
Traceability coverage
Pilot results
Validation results
```

N2-G therefore provides inputs to N2-J but does not perform final N2 closure.

---

# 62. Anti-Runaway Control

N2-G shall not create:

```text
N2-G.01
N2-G.02
N2-G.03
...
```

merely because additional gap categories can be imagined.

A new gap class requires:

```text
Distinct semantic condition
+
Material need
+
Existing-class insufficiency
+
Impact assessment
+
Approval
```

---

# 63. Final N2-G Finding

> **N2-G.00 establishes the controlled diagnostic model for traceability gaps, orphaned objects and associated findings. It distinguishes missing or insufficient traceability from unknown conditions, non-applicability and architecture defects, while reusing the authoritative status, evidence, materiality and depth models established by N2-E, N2-D and N2-A. The model provides the required diagnostic foundation for the N2 pilot and subsequent validation.**

---

# 64. Final N2-G Principle

> **A gap exists only when a materially required traceability condition is demonstrably absent, insufficient, contradictory or invalid; the absence of information alone shall never be treated as proof of a gap.**

---

# 65. Final N2-G Anti-Runaway Principle

> **The gap model shall diagnose what matters, not catalogue every imperfection. New gap classes require a materially distinct condition that cannot be represented by the existing controlled model.**

---

# 66. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2-G.00 Gap, Orphan & Traceability Finding Model  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-G.00-Gap-Orphan-and-Traceability-Finding-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-G WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-F.00 — Materiality & Traceability Depth Disposition Record  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-G — Gap & Orphan Model  
**Inherited Baseline:** MFM v1.2-Steady-State SC-90 Closure Baseline  
**Canonical Capabilities:** 8  
**Gap Classes:** 12  
**Orphan Classes:** 7  
**Finding Statuses:** 8 (inherited from N2-E)  
**Severity Levels:** 4  
**Priority Levels:** 4  
**Resolution Paths:** 10  
**Pilot:** CAN-01 Enterprise Integration — RECOMMENDED / PENDING VALIDATION  
**N2-G Completion Gate:** REQUIRED  
**Automatic Successor Generation:** PROHIBITED  
**Closure State:** N2-G-SC-90 — GAP / ORPHAN MODEL CLOSED
