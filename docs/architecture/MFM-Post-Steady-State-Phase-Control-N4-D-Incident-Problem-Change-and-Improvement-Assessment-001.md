# MFM Post-Steady-State Phase Control

## N4-D — Incident, Problem, Change & Improvement Assessment

**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-D-Incident-Problem-Change-and-Improvement-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-D WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent Control:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-C — KPI/KRI, Monitoring & Operational Control Assessment  
**Upstream Workstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N4-D performs the controlled assessment of the operational feedback and response chain:

```text
Monitoring
    ↓
Incident
    ↓
Problem
    ↓
Change
    ↓
Improvement
    ↓
Measurement
    ↓
Feedback
```

The purpose is to determine whether material operational services and processes have sufficiently established:

```text
Incident Management
Problem Management
Change Management
Improvement
Operational Feedback
Evidence
Ownership
Traceability
```

N4-D does not assume that operational records, processes or feedback loops exist merely because the architecture model defines them.

---

# 2. Governing Principle

The controlled operational feedback loop is:

```text
Condition / Alert
        ↓
Incident
        ↓
Problem
        ↓
Root Cause / Corrective Action
        ↓
Change
        ↓
Improvement
        ↓
Measurement
        ↓
Feedback
```

Not every condition requires every stage.

The applicable chain depends on:

```text
Materiality
Severity
Recurrence
Risk
Operational Impact
Evidence
```

---

# 3. Source Baseline

N4-D consumes:

```text
N4-A
Operational Scope & Evidence Baseline

N4-B
Service & Process Operational Model

N4-C
KPI/KRI, Monitoring & Operational Control Assessment
```

The inherited evidence condition remains:

```text
COND-N3-E.01-01
Actual named CAN-01 implementation-instance evidence
not established in the controlled source set.
```

N4-D shall preserve:

```text
NOT ESTABLISHED
≠
DOES NOT EXIST
```

---

# 4. Assessment Domains

N4-D assesses:

```text
OP-01 — Incident Management
OP-02 — Problem Management
OP-03 — Root Cause / Corrective Action
OP-04 — Change Management
OP-05 — Improvement Management
OP-06 — Operational Feedback
OP-07 — Ownership
OP-08 — Evidence
OP-09 — Traceability
OP-10 — Closure / Effectiveness
```

These are assessment domains, not assertions that corresponding operational instances exist.

---

# 5. OP-01 — Incident Management

N4-D assesses the operational incident capability.

Potential attributes:

```text
Incident ID
Detection Source
Service
Process
Severity
Priority
Owner
Response
Resolution
Escalation
Evidence
Status
```

The model shall distinguish:

```text
Incident Capability Defined
Incident Capability Implemented
Incident Capability Operational
Incident Response Evidenced
```

---

# 6. Incident Lifecycle

Controlled incident lifecycle:

```text
DETECTED
REGISTERED
TRIAGED
ASSIGNED
IN PROGRESS
RESOLVED
CLOSED
REOPENED
CANCELLED
UNKNOWN
```

Lifecycle state requires evidence where used as an operational claim.

---

# 7. Incident-to-Service Relationship

A material incident should establish:

```text
Incident
    ↓
Affected Service
```

Possible relationship states:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
UNVERIFIED
NOT REQUIRED
CONFLICTING
```

An incident without service context may be an operational orphan where the relationship is required.

---

# 8. Incident-to-Process Relationship

Where relevant:

```text
Incident
    ↓
Affected Process
```

The relationship supports impact analysis and operational traceability.

---

# 9. Incident Severity and Priority

N4-D shall distinguish:

```text
Severity
```

from:

```text
Priority
```

Severity describes impact.

Priority describes handling order.

Neither shall be inferred without an established classification basis.

---

# 10. OP-02 — Problem Management

N4-D assesses whether recurring or material incidents connect to problem management.

The relationship is:

```text
Incident
    ↓
Problem
```

Possible states:

```text
REQUIRED
ESTABLISHED
PARTIALLY ESTABLISHED
NOT REQUIRED
NOT ESTABLISHED
UNVERIFIED
CONFLICTING
```

---

# 11. Problem Object Model

Potential problem attributes:

```text
Problem ID
Related Incident
Service
Process
Description
Root Cause
Known Error
Owner
Corrective Action
Change Relationship
Evidence
Status
```

A problem object does not automatically establish root cause.

---

# 12. Problem Lifecycle

Controlled problem lifecycle:

```text
IDENTIFIED
REGISTERED
INVESTIGATING
ROOT CAUSE ESTABLISHED
KNOWN ERROR
CORRECTIVE ACTION
RESOLVED
CLOSED
REOPENED
CANCELLED
UNKNOWN
```

Each transition requires appropriate evidence where operationally material.

---

# 13. Root Cause Boundary

N4-D shall distinguish:

```text
Suspected Root Cause
```

from:

```text
Evidence-Supported Root Cause
```

The following transformation is prohibited:

```text
Problem Record
↓
Automatic Root Cause
```

---

# 14. OP-03 — Corrective Action

Corrective action may result from:

```text
Incident
Problem
Audit Finding
Risk
Control Failure
Operational Review
Improvement Opportunity
```

The corrective action relationship shall identify:

```text
Source
Action
Owner
Due Date
Target
Evidence
Status
Result
```

---

# 15. Corrective Action Effectiveness

N4-D shall distinguish:

```text
Action Planned
Action Implemented
Action Completed
Action Effective
```

Effectiveness requires evidence.

---

# 16. OP-04 — Change Management

N4-D assesses operational change management.

Potential attributes:

```text
Change ID
Reason
Source Problem / Finding
Affected Service
Affected Process
Affected Implementation
Risk
Owner
Approval
Implementation
Result
Evidence
```

Operational change is distinct from canonical architecture change.

---

# 17. Change Lifecycle

Controlled change lifecycle:

```text
REQUESTED
ASSESSED
APPROVED
SCHEDULED
IMPLEMENTED
VALIDATED
CLOSED
REJECTED
ROLLED BACK
CANCELLED
UNKNOWN
```

Lifecycle claims require evidence.

---

# 18. Change Risk

Material changes may require:

```text
Risk Assessment
Impact Assessment
Dependency Assessment
Security Assessment
Rollback Plan
Approval
Validation
```

The exact depth depends on materiality.

---

# 19. Change-to-Service Relationship

Where material:

```text
Change
    ↓
Affected Service
```

The relationship supports operational impact assessment.

---

# 20. Change-to-Implementation Relationship

Where relevant:

```text
Change
    ↓
Affected Implementation Element
```

This relationship connects N4 operational change back to N3 implementation architecture.

---

# 21. Change vs Architecture Change

N4-D shall preserve:

```text
Operational Change
≠
Canonical Architecture Change
```

A change to an operational configuration or implementation does not automatically alter the canonical architecture.

A material architecture change requires controlled architecture change management.

---

# 22. OP-05 — Improvement Management

N4-D assesses the operational improvement process.

Potential sources:

```text
Incident
Problem
Audit
Risk
KPI
KRI
Operational Review
Customer Feedback
Management Review
Change Outcome
```

Improvement may address:

```text
Performance
Reliability
Security
Quality
Efficiency
Risk
Compliance
Service Experience
```

---

# 23. Improvement Object Model

Potential attributes:

```text
Improvement ID
Source
Objective
Owner
Action
Expected Outcome
Target
Measure
Evidence
Status
Result
```

---

# 24. Improvement Lifecycle

Controlled improvement lifecycle:

```text
IDENTIFIED
ASSESSED
PRIORITIZED
APPROVED
PLANNED
IMPLEMENTED
MEASURED
VALIDATED
CLOSED
CANCELLED
UNKNOWN
```

The transition to:

```text
VALIDATED
```

requires evidence.

---

# 25. Improvement-to-Measurement Relationship

Where material:

```text
Improvement
    ↓
KPI / KRI
```

The relationship should establish whether the intended outcome can be measured.

---

# 26. Improvement Feedback Loop

The preferred operational feedback chain is:

```text
Problem / Finding
        ↓
Improvement
        ↓
Change
        ↓
Measurement
        ↓
Review
        ↓
Further Improvement
```

This is a model relationship.

Actual operation requires evidence.

---

# 27. OP-06 — Operational Feedback

N4-D assesses whether operational information feeds back into:

```text
Service
Process
Control
Implementation
Architecture
Improvement
```

Feedback relationships may include:

```text
Incident → Process
Problem → Service
KPI → Improvement
KRI → Risk Treatment
Change → Architecture
Improvement → Service
```

Each relationship is independently assessed.

---

# 28. Feedback to Architecture

Operational evidence may identify:

```text
Architecture Change Candidate
```

However:

```text
Operational Finding
≠
Automatic Architecture Change
```

Any architecture change remains subject to controlled architecture governance.

---

# 29. OP-07 — Ownership

Material operational objects should establish:

```text
Incident Owner
Problem Owner
Change Owner
Improvement Owner
Service Owner
Process Owner
```

Ownership states:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
CONFLICTING
```

No owner shall be invented.

---

# 30. OP-08 — Evidence

Operational evidence may include:

```text
Incident Records
Problem Records
Root Cause Analysis
Corrective Action Records
Change Records
Approval Records
Implementation Evidence
Validation Records
Improvement Records
Operational Review Records
KPI / KRI Results
Audit Evidence
```

Evidence shall be bound to the claim it supports.

---

# 31. Evidence Sufficiency

Evidence shall be evaluated for:

```text
Identity
Authority
Currency
Relevance
Completeness
Consistency
Traceability
```

Evidence states:

```text
SUFFICIENT
PARTIALLY SUFFICIENT
INSUFFICIENT
CONFLICTING
UNKNOWN
```

---

# 32. OP-09 — Operational Traceability

The core traceability chain is:

```text
Incident
    ↓
Problem
    ↓
Corrective Action
    ↓
Change
    ↓
Improvement
    ↓
KPI / KRI
    ↓
Feedback
```

Not every incident must traverse every stage.

Materiality determines required depth.

---

# 33. Operational Depth

N4-D applies:

```text
D1 — Identity Only
D2 — Context
D3 — Relationship
D4 — Ownership
D5 — Evidence
D6 — Implementation
D7 — Operational
D8 — Measurement / Value
```

N4-D principally assesses:

```text
D7
D8
```

with D6 relationships used where change impacts implementation.

---

# 34. OP-10 — Closure / Effectiveness

N4-D shall distinguish:

```text
Incident Closed
≠
Problem Resolved

Problem Resolved
≠
Root Cause Validated

Change Implemented
≠
Change Effective

Improvement Completed
≠
Improvement Demonstrated
```

Each outcome requires appropriate evidence.

---

# 35. Operational Finding Classes

N4-D may identify:

```text
OPF-01 Missing Incident Relationship
OPF-02 Missing Problem Relationship
OPF-03 Missing Root Cause Evidence
OPF-04 Missing Corrective Action
OPF-05 Missing Change Relationship
OPF-06 Missing Change Evidence
OPF-07 Missing Improvement Relationship
OPF-08 Missing Improvement Evidence
OPF-09 Missing Owner
OPF-10 Missing Operational Evidence
OPF-11 Stale Operational Record
OPF-12 Conflicting Operational Record
OPF-13 Unverified Operational Relationship
OPF-14 Orphaned Operational Object
OPF-15 Effectiveness Not Established
OPF-16 Operational Depth Deficiency
```

These are controlled assessment classes.

---

# 36. False-Gap Control

The following interpretations are prohibited:

```text
No Incident Record
≠
No Incident Capability

No Problem Record
≠
No Problem Management

No Change Record
≠
No Change Capability

No Improvement Record
≠
No Improvement Capability

No Root Cause Record
≠
No Root Cause Analysis

No Evidence of Effectiveness
≠
Proven Ineffectiveness
```

A genuine operational deficiency requires sufficient evidence.

---

# 37. Orphan Control

Potential operational orphans include:

```text
Incident without Service

Problem without Incident / Source

Corrective Action without Source

Change without Target

Improvement without Source

Operational Finding without Owner

Effectiveness Claim without Evidence
```

Orphans shall be assessed according to materiality.

---

# 38. Contradiction Control

Potential contradictions include:

```text
Conflicting Incident Severity
Conflicting Problem Status
Conflicting Root Cause
Conflicting Change Status
Conflicting Change Owner
Conflicting Improvement Status
Conflicting Service Impact
Conflicting Closure Evidence
```

Contradictions require resolution or controlled acceptance.

---

# 39. CAN-01 Boundary

The inherited condition remains:

```text
COND-N3-E.01-01
```

The actual CAN-01 implementation instance remains:

```text
NOT ESTABLISHED IN CONTROLLED SOURCE SET
```

Therefore N4-D shall not assert:

```text
CAN-01 Incident History
CAN-01 Problem History
CAN-01 Change History
CAN-01 Improvement History
```

unless controlled evidence establishes the relevant operational object and relationship.

---

# 40. Operational Feedback Assessment Register

N4-D shall use:

| Assessment ID | Relationship | Required Depth | Evidence | Status | Finding |
|---|---|---|---|---|---|
| N4-D-001 | Incident → Service | D7 | TBD | OPEN | TBD |
| N4-D-002 | Incident → Problem | D7 | TBD | OPEN | TBD |
| N4-D-003 | Problem → Corrective Action | D7 | TBD | OPEN | TBD |
| N4-D-004 | Corrective Action → Change | D7 | TBD | OPEN | TBD |
| N4-D-005 | Change → Implementation | D6/D7 | TBD | OPEN | TBD |
| N4-D-006 | Change → Improvement | D7/D8 | TBD | OPEN | TBD |
| N4-D-007 | Improvement → KPI/KRI | D8 | TBD | OPEN | TBD |
| N4-D-008 | Operational Feedback → Architecture | D7/D8 | TBD | OPEN | TBD |

This is a controlled assessment structure, not evidence that the relationships currently exist.

---

# 41. N4-D Completion Criteria

N4-D may be considered complete when:

```text
Incident Management Assessed
AND
Problem Management Assessed
AND
Root Cause / Corrective Action Assessed
AND
Change Management Assessed
AND
Improvement Management Assessed
AND
Operational Feedback Assessed
AND
Ownership Assessed
AND
Evidence Assessed
AND
Operational Traceability Assessed
AND
Closure / Effectiveness Assessed
AND
Material Findings Identified
AND
False-Gap Control Applied
AND
CAN-01 Boundary Preserved
AND
N4-E Inputs Prepared
```

---

# 42. Expected Outcome

The expected N4-D outcome is:

```text
CONTROLLED INCIDENT ASSESSMENT
+
CONTROLLED PROBLEM ASSESSMENT
+
CONTROLLED CHANGE ASSESSMENT
+
CONTROLLED IMPROVEMENT ASSESSMENT
+
CONTROLLED FEEDBACK ASSESSMENT
+
CONTROLLED FINDINGS
+
N4-E READY
```

The expected outcome is not:

```text
COMPLETE OPERATIONAL INCIDENT INVENTORY
```

or:

```text
PROOF OF EFFECTIVENESS
```

unless supported by evidence.

---

# 43. Anti-Runaway Control

N4-D shall not automatically create:

```text
N4-D.01
N4-D.02
N4-D.03
...
```

unless a materially distinct controlled assessment requires a separate artifact.

The controlled sequence remains:

```text
N4-A
    ↓
N4-B
    ↓
N4-C
    ↓
N4-D
    ↓
N4-E
```

---

# 44. Current State

```text
N2
= CLOSED
N2C-2 — COMPLETE WITH CONDITIONS

N3
= CLOSED
N3C-2 — COMPLETE WITH CONDITIONS

N4
= ACTIVE / AUTHORIZED

N4.00
= COMPLETED / SCOPE ESTABLISHED

N4-A
= COMPLETED / OPERATIONAL SCOPE & EVIDENCE BASELINE

N4-B
= COMPLETED / SERVICE & PROCESS OPERATIONAL MODEL

N4-C
= COMPLETED / KPI-KRI, MONITORING & OPERATIONAL CONTROL ASSESSMENT

N4-D
= ACTIVE / INCIDENT, PROBLEM, CHANGE & IMPROVEMENT ASSESSMENT

N4-E
= NEXT CONTROLLED WORK PACKAGE

N5
= NOT AUTHORIZED
```

---

# 45. Final N4-D Statement

> **N4-D establishes the controlled assessment of the operational incident, problem, corrective action, change, improvement and feedback loop. It distinguishes operational records from operational capability, closure from effectiveness, and change implementation from architecture change. N4-D therefore provides the evidence-controlled operational feedback assessment required before N4-E can validate the complete Operational Architecture workstream.**

---

# 46. Document Control

**Document:** MFM Post-Steady-State Phase Control — N4-D Incident, Problem, Change & Improvement Assessment  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-D-Incident-Problem-Change-and-Improvement-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-D WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-C — KPI/KRI, Monitoring & Operational Control Assessment  
**Upstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N4-D  
**Next Work Package:** N4-E — N4 Validation & Completion Assessment  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N5 Generation:** PROHIBITED  

---

# 47. Terminal Principle

> **Operational architecture is not complete merely because incidents, problems, changes and improvements are defined. N4-D assesses whether the operational feedback loop can be evidenced from condition through response, corrective action, change, improvement and measurement. Where evidence is insufficient, the controlled result remains an evidence condition or unverified state rather than an invented operational failure.**
