# MFM Post-Steady-State Phase Control

## N4-A — Operational Scope & Evidence Baseline

**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-A-Operational-Scope-and-Evidence-Baseline-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent Control:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Upstream Workstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N4-A establishes the controlled operational scope and evidence baseline for the N4 Operational Architecture workstream.

The purpose is to define:

```text
WHAT
operational realization is in scope

WHICH
services, processes and operational relationships
are material

WHICH
evidence is required

WHICH
operational depth is required

WHICH
conditions are inherited

WHICH
items are explicitly outside scope
```

N4-A therefore establishes the boundary before detailed operational modelling begins.

---

# 2. Governing Principle

N4 begins from the N3 implementation architecture but does not assume that every implementation element is operationally realized.

The controlled relationship is:

```text
Canonical Architecture
        ↓
Implementation Architecture
        ↓
Operational Architecture
```

and, operationally:

```text
Architecture
    ↓
Service
    ↓
Process
    ↓
Owner
    ↓
KPI / KRI
    ↓
Monitoring
    ↓
Incident
    ↓
Problem
    ↓
Change
    ↓
Improvement
```

The existence of an upstream object does not automatically prove the existence of a downstream operational object.

---

# 3. Scope Baseline

N4-A establishes the following primary operational domains:

```text
OA-01 — Service Architecture
OA-02 — Process Architecture
OA-03 — Operational Ownership
OA-04 — KPI / KRI
OA-05 — Monitoring
OA-06 — Incident Management
OA-07 — Problem Management
OA-08 — Change Management
OA-09 — Improvement
OA-10 — Operational Evidence
```

These domains form the controlled N4 assessment boundary.

---

# 4. OA-01 — Service Architecture

N4 shall assess how material implementation capabilities are represented as operational services.

The assessment shall consider:

```text
Service Identity
Service Purpose
Service Consumer
Service Owner
Supporting Implementation Elements
Criticality
Lifecycle
Operational Status
KPI / KRI
Monitoring
Evidence
```

The baseline does not assert that each service currently exists.

---

# 5. OA-02 — Process Architecture

N4 shall assess the operational processes required to deliver material services.

The baseline includes:

```text
Process Identity
Process Purpose
Service Relationship
Process Owner
Inputs
Outputs
Dependencies
Controls
KPI / KRI
Monitoring
Evidence
```

A process description alone does not establish operational effectiveness.

---

# 6. OA-03 — Operational Ownership

N4 shall assess ownership at the level required by materiality.

Potential ownership roles include:

```text
Business Owner
Service Owner
Process Owner
Technical Owner
Operational Owner
Security Owner
```

The baseline shall distinguish:

```text
OWNER ESTABLISHED
OWNER PARTIALLY ESTABLISHED
OWNER NOT ESTABLISHED
OWNER CONFLICTING
```

No owner shall be inferred solely from job titles, architecture roles or organizational assumptions.

---

# 7. OA-04 — KPI / KRI

N4 shall assess material operational measures.

The baseline includes:

```text
KPI
KRI
SLA Measure
Availability
Performance
Capacity
Security
Compliance
Quality
```

Where applicable, each measure shall have:

```text
Definition
Owner
Target
Threshold
Source
Frequency
Service / Process Relationship
Evidence
```

The existence of a metric does not automatically establish active monitoring.

---

# 8. OA-05 — Monitoring

N4 shall assess monitoring relationships for material services and processes.

Potential monitoring objects include:

```text
Metric
Threshold
Alert
Dashboard
Monitoring Source
Monitoring Owner
Escalation
Evidence
```

The baseline shall distinguish:

```text
Monitoring Designed
Monitoring Implemented
Monitoring Operational
Monitoring Evidence Established
```

---

# 9. OA-06 — Incident Management

N4 shall assess the operational relationship between monitored conditions and incident management.

The baseline includes:

```text
Detection
Alert
Incident
Severity
Priority
Owner
Response
Resolution
Evidence
```

The absence of a historical incident record shall not automatically prove absence of incident capability.

---

# 10. OA-07 — Problem Management

N4 shall assess problem management where operationally material.

The baseline includes:

```text
Problem Identity
Related Incident
Root Cause
Owner
Known Error
Corrective Action
Evidence
Status
```

Root cause shall not be asserted without supporting evidence.

---

# 11. OA-08 — Change Management

N4 shall assess operational change relationships.

The baseline includes:

```text
Change Identity
Reason
Affected Service
Affected Implementation
Risk
Owner
Approval
Implementation
Result
Evidence
```

Operational change management shall remain distinct from canonical architecture change control.

---

# 12. OA-09 — Improvement

N4 shall assess the operational improvement loop:

```text
Finding / Problem
        ↓
Change
        ↓
Improvement
        ↓
Measurement
        ↓
Feedback
```

Improvement shall distinguish:

```text
Planned Improvement
from
Implemented Improvement
from
Demonstrated Improvement
```

---

# 13. OA-10 — Operational Evidence

N4-A establishes the evidence categories required for operational assessment.

Potential evidence includes:

```text
Service Catalogue
Process Documentation
Ownership Records
SLA / KPI Records
KRI Records
Monitoring Records
Incident Records
Problem Records
Change Records
Improvement Records
Operational Procedures
Audit Records
Performance Records
```

The presence of an evidence source does not automatically validate every claim derived from it.

---

# 14. Evidence Hierarchy

N4 inherits the controlled hierarchy:

```text
E0 — Conceptual
E1 — Architectural
E2 — Governance / Implementation Model
E3 — Actual Implementation Evidence
```

For operational claims, E3-level evidence is normally required where the claim concerns actual operational realization.

---

# 15. Operational Evidence Sufficiency

N4 shall distinguish:

```text
Evidence Exists
from
Evidence Is Sufficient
```

Evidence sufficiency shall consider:

```text
Identity
Currency
Relevance
Completeness
Authority
Consistency
Traceability
```

Where evidence is insufficient:

```text
NOT ESTABLISHED
```

shall be used.

---

# 16. Operational Status Model

N4-A establishes the following controlled operational states:

```text
PLANNED
DESIGNED
IMPLEMENTED
OPERATIONAL
SUSPENDED
RETIRED
DECOMMISSIONED
UNKNOWN
```

The state:

```text
IMPLEMENTED
```

shall not automatically be converted to:

```text
OPERATIONAL
```

Operational status requires appropriate evidence.

---

# 17. Operational Materiality

N4 shall classify operational objects according to materiality:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

Materiality determines the required depth of operational assessment.

---

# 18. Operational Traceability Depth

N4 inherits:

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

N4 primarily targets:

```text
D7 — Operational
D8 — Measurement / Value
```

The required depth shall be determined by materiality.

---

# 19. Service Criticality

Where service criticality is material, N4 shall assess:

```text
Criticality
Business Impact
Operational Dependency
Owner
KPI / KRI
Monitoring
Incident
Recovery / Response
Evidence
```

No criticality value shall be invented.

---

# 20. Operational Relationship States

Each material relationship may use:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
NOT REQUIRED
UNVERIFIED
CONFLICTING
```

The relationship state shall be evidence-based.

---

# 21. Service-to-Process Baseline

The baseline relationship is:

```text
Service
    ↓
Process
```

N4 shall determine whether:

```text
Process Required?
Process Identified?
Process Operational?
Process Owner Established?
Evidence Available?
```

---

# 22. Process-to-Owner Baseline

The baseline relationship is:

```text
Process
    ↓
Owner
```

The assessment shall determine:

```text
Owner Identified?
Owner Authorized?
Owner Current?
Ownership Evidence Available?
```

---

# 23. Owner-to-KPI/KRI Baseline

The baseline relationship is:

```text
Owner
    ↓
KPI / KRI
```

N4 shall determine whether the responsible owner is linked to material measures.

---

# 24. KPI/KRI-to-Monitoring Baseline

The baseline relationship is:

```text
KPI / KRI
    ↓
Monitoring
```

N4 shall distinguish:

```text
Defined
Configured
Active
Measured
Reported
```

---

# 25. Monitoring-to-Incident Baseline

The baseline relationship is:

```text
Monitoring
    ↓
Incident
```

N4 shall assess whether operational thresholds and alerts connect to incident handling where required.

---

# 26. Incident-to-Problem Baseline

The baseline relationship is:

```text
Incident
    ↓
Problem
```

N4 shall determine whether recurring or material incidents require problem management.

---

# 27. Problem-to-Change Baseline

The baseline relationship is:

```text
Problem
    ↓
Change
```

N4 shall assess whether corrective action requires controlled change.

---

# 28. Change-to-Improvement Baseline

The baseline relationship is:

```text
Change
    ↓
Improvement
```

N4 shall assess whether material changes have measurable operational outcomes where required.

---

# 29. Operational Orphan Categories

N4-A establishes these potential orphan classes:

```text
ORPHAN-S
Service without required Process

ORPHAN-P
Process without required Owner

ORPHAN-M
KPI / KRI without operational context

ORPHAN-MON
Monitoring without defined target

ORPHAN-I
Incident without service/process context

ORPHAN-PR
Problem without incident/root-cause context

ORPHAN-C
Change without controlled target

ORPHAN-IMP
Improvement without source finding/problem
```

These are assessment categories, not pre-existing findings.

---

# 30. Operational Contradiction Categories

Potential contradictions include:

```text
CON-SO
Conflicting Service Owners

CON-PO
Conflicting Process Owners

CON-KPI
Conflicting KPI Definitions

CON-KRI
Conflicting KRI Definitions

CON-MON
Conflicting Monitoring Thresholds

CON-CRIT
Conflicting Criticality

CON-CHG
Conflicting Change Ownership
```

Each contradiction requires evidence-based assessment.

---

# 31. False-Gap Control

The following rules are mandatory:

```text
No Evidence
≠
No Operation

No Record
≠
No Capability

No KPI
≠
No Service

No Incident
≠
No Incident Capability

No Problem
≠
No Problem Management

No Change Record
≠
No Change Capability
```

A genuine operational gap requires evidence that:

```text
The capability or relationship is required
AND
the required operational state is absent.
```

---

# 32. Inherited Conditions

N4 inherits the following controlled conditions:

```text
COND-N2-I-01
Actual named CAN-01 implementation-instance evidence
not established in the controlled source set.

COND-N3-E.01-01
Same implementation evidence condition
carried forward through N3 closure.
```

N4 shall reference these conditions where they materially affect operational traceability.

N4 shall not create duplicate findings solely because the same condition is inherited.

---

# 33. CAN-01 Operational Boundary

Until actual implementation-instance evidence is established:

```text
CAN-01
= OPERATIONAL REALIZATION NOT ESTABLISHED
```

This shall not be interpreted as:

```text
CAN-01
= NOT OPERATIONAL
```

The correct controlled state remains:

```text
NOT ESTABLISHED IN CONTROLLED SOURCE SET
```

---

# 34. N4 Evidence Register Baseline

N4-A establishes the following evidence register structure:

| Evidence ID | Domain | Object / Relationship | Evidence Class | Currency | Sufficiency | Status |
|---|---|---|---|---|---|---|
| N4-EV-001 | Service | Service Identity | E2/E3 | TBD | TBD | OPEN |
| N4-EV-002 | Process | Process Identity | E2/E3 | TBD | TBD | OPEN |
| N4-EV-003 | Ownership | Owner Relationship | E2/E3 | TBD | TBD | OPEN |
| N4-EV-004 | KPI/KRI | Measure Definition | E2/E3 | TBD | TBD | OPEN |
| N4-EV-005 | Monitoring | Monitoring Relationship | E3 | TBD | TBD | OPEN |
| N4-EV-006 | Incident | Incident Capability | E3 | TBD | TBD | OPEN |
| N4-EV-007 | Problem | Problem Capability | E3 | TBD | TBD | OPEN |
| N4-EV-008 | Change | Change Capability | E3 | TBD | TBD | OPEN |
| N4-EV-009 | Improvement | Improvement Loop | E3 | TBD | TBD | OPEN |

The table is a baseline structure, not evidence that the listed evidence currently exists.

---

# 35. Operational Scope Exclusions

Unless separately authorized, N4-A does not authorize:

```text
New Capability Creation
Canonical Architecture Redesign
Uncontrolled Process Redesign
Automatic Service Creation
Automatic Organizational Restructuring
Automatic Tool Procurement
Automatic System Changes
Automatic N5 Creation
```

---

# 36. Relationship to N3

N4 shall use N3 as an upstream architectural source.

The controlled chain is:

```text
N3 Implementation Element
        ↓
N4 Service
        ↓
N4 Process
        ↓
N4 Operational Control
```

Where the relationship cannot be established:

```text
UNVERIFIED
```

shall be used.

---

# 37. N4-A Completion Criteria

N4-A may be considered complete when:

```text
Operational Domains Defined
AND
Operational Evidence Classes Defined
AND
Operational Status Model Defined
AND
Materiality Model Defined
AND
Operational Depth Defined
AND
Service / Process Boundary Defined
AND
Ownership Boundary Defined
AND
Monitoring / Incident / Problem / Change / Improvement Boundary Defined
AND
Inherited Conditions Identified
AND
Evidence Register Baseline Established
AND
Scope Exclusions Defined
AND
N4-B Inputs Prepared
```

---

# 38. Expected Outcome

The expected N4-A outcome is:

```text
CONTROLLED OPERATIONAL SCOPE
+
CONTROLLED EVIDENCE BASELINE
+
CONTROLLED OPERATIONAL DEPTH
+
CONTROLLED MATERIALITY
+
CONTROLLED INHERITED CONDITIONS
+
N4-B READY
```

The expected outcome is not:

```text
COMPLETE OPERATIONAL INVENTORY
```

---

# 39. Anti-Runaway Control

N4-A shall not automatically create:

```text
N4-A.01
N4-A.02
N4-A.03
...
```

unless a materially distinct evidence-baseline event requires a separate artifact.

The controlled sequence remains:

```text
N4.00
    ↓
N4-A
    ↓
N4-B
```

---

# 40. Current State

```text
N2
= CLOSED
N2C-2 — COMPLETE WITH CONDITIONS

N3
= CLOSED
N3C-2 — COMPLETE WITH CONDITIONS

N4
= ACTIVE
N4 AUTHORIZED

N4.00
= COMPLETED / SCOPE ESTABLISHED

N4-A
= ACTIVE / OPERATIONAL SCOPE & EVIDENCE BASELINE

N4-B
= NEXT CONTROLLED WORK PACKAGE

N4-C
= NOT STARTED

N4-D
= NOT STARTED

N4-E
= NOT STARTED

N5
= NOT AUTHORIZED
```

---

# 41. Final N4-A Statement

> **N4-A establishes the controlled operational boundary for Operational Architecture. It defines the services, processes, ownership, measurement, monitoring, incident, problem, change and improvement domains to be assessed, together with the evidence hierarchy, operational states, materiality and operational traceability depth. N4-A does not assume that operational realization exists; it establishes the evidence-controlled basis from which N4-B may build the Operational Service and Process Model.**

---

# 42. Document Control

**Document:** MFM Post-Steady-State Phase Control — N4-A Operational Scope & Evidence Baseline  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-A-Operational-Scope-and-Evidence-Baseline-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Upstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N4-A  
**Next Work Package:** N4-B — Service & Process Operational Model  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N5 Generation:** PROHIBITED  

---

# 43. Terminal Principle

> **N4 begins with operational scope and evidence definition, not with assumed operational inventory. The purpose of N4-A is to establish exactly what must be demonstrated before service, process, ownership, measurement and operational-control relationships can be assessed as operationally realized.**
