# MFM Post-Steady-State Phase Control

## N4-B — Service & Process Operational Model

**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-B-Service-and-Process-Operational-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent Control:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-A — Operational Scope & Evidence Baseline  
**Upstream Workstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N4-B establishes the controlled **Service & Process Operational Model** for the N4 Operational Architecture workstream.

The purpose is to define how operational services and processes are represented and related to:

```text
Implementation
Service
Process
Owner
Consumer
Control
KPI / KRI
Monitoring
Evidence
Lifecycle
```

N4-B establishes the operational model.

It does not populate the model with unsupported operational instances.

---

# 2. Governing Principle

The operational chain remains:

```text
Canonical Architecture
        ↓
Implementation Architecture
        ↓
Operational Architecture
        ↓
Service
        ↓
Process
        ↓
Owner
```

The existence of an implementation component does not automatically establish an operational service.

Likewise:

```text
Service
≠
Process
```

and:

```text
Process
≠
Operational Effectiveness
```

without appropriate evidence.

---

# 3. Source Baseline

N4-B consumes the completed N4-A baseline:

```text
Operational Domains
= DEFINED

Evidence Classes
= DEFINED

Operational Status Model
= DEFINED

Materiality
= DEFINED

Operational Traceability Depth
= DEFINED

Orphan / Contradiction Controls
= DEFINED

Inherited Conditions
= IDENTIFIED

Evidence Register Baseline
= ESTABLISHED
```

The inherited implementation evidence condition remains:

```text
COND-N2-I-01
Actual named CAN-01 implementation-instance evidence
not established in the controlled source set.
```

N4-B shall preserve the distinction:

```text
NOT ESTABLISHED
≠
DOES NOT EXIST
```

---

# 4. Service Object Model

The controlled operational service object shall support:

```text
Service ID
Service Name
Service Description
Service Type
Service Consumer
Service Owner
Supporting Implementation Elements
Process Relationship
Criticality
Lifecycle
Operational Status
KPI / KRI
Monitoring
Evidence
Materiality
Confidence
```

The object model does not assert that a service instance exists.

---

# 5. Service Types

Potential service classifications include:

```text
Business Service
Application Service
Technical Service
Infrastructure Service
Security Service
Data Service
Integration Service
Support Service
```

The classification shall be evidence-supported.

---

# 6. Service Identity

A service shall be uniquely represented where possible by:

```text
Service ID
Source Repository
Source Identifier
Service Name
Service Context
```

Name alone is insufficient where ambiguity exists.

Potential duplicates shall be treated as an identity issue.

---

# 7. Service Lifecycle

Controlled service lifecycle:

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

A service marked:

```text
IMPLEMENTED
```

shall not automatically be marked:

```text
OPERATIONAL
```

---

# 8. Service Criticality

A material service shall support:

```text
Criticality
Business Impact
Operational Dependency
Recovery Importance
Security Importance
Compliance Importance
```

Criticality states:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

No criticality shall be inferred without supporting evidence.

---

# 9. Service Consumer

Where materially relevant, the model shall identify:

```text
Consumer
Consumer Group
Business Function
Process
Application
External Party
```

The presence of a consumer relationship shall require evidence where it materially affects operational architecture.

---

# 10. Service Owner

A material service should have an identifiable:

```text
Service Owner
```

The owner may be represented as:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
CONFLICTING
```

No owner shall be invented to complete a model record.

---

# 11. Service-to-Implementation Relationship

The primary implementation relationship is:

```text
Implementation Element
        ↓
SUPPORTS / REALIZES
        ↓
Service
```

The relationship shall be assessed independently.

An implementation element may support:

```text
Zero
One
Multiple
```

services depending on evidence.

---

# 12. Service-to-Process Relationship

The primary operational relationship is:

```text
Service
    ↓
DELIVERED THROUGH
    ↓
Process
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

---

# 13. Process Object Model

The controlled process object shall support:

```text
Process ID
Process Name
Process Purpose
Process Type
Service Relationship
Owner
Inputs
Outputs
Dependencies
Controls
KPI / KRI
Monitoring
Lifecycle
Operational Status
Evidence
Materiality
Confidence
```

The object model does not prove that the process operates effectively.

---

# 14. Process Types

Potential process types include:

```text
Core Process
Supporting Process
Management Process
Operational Process
Control Process
Security Process
Service Management Process
Improvement Process
```

Classification shall be evidence-supported.

---

# 15. Process Identity

A process shall support:

```text
Process ID
Source
Source Identifier
Process Name
Process Context
Version
Lifecycle
```

Where duplicate process representations exist, they shall not be silently merged.

---

# 16. Process Lifecycle

Controlled process lifecycle:

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

The model explicitly separates:

```text
PROCESS DEFINED
```

from:

```text
PROCESS OPERATIONAL
```

---

# 17. Process Inputs and Outputs

Where materially relevant, the process model should establish:

```text
Inputs
Sources
Transformations
Outputs
Consumers
Controls
```

A process description without evidence of actual execution remains a model-level representation.

---

# 18. Process Owner

A material process should establish:

```text
Process Owner
```

The ownership state shall be:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
CONFLICTING
```

Owner identity shall be evidence-backed.

---

# 19. Process Controls

Where required, the process may be related to:

```text
Preventive Control
Detective Control
Corrective Control
Security Control
Compliance Control
Quality Control
```

A control requirement does not automatically establish that the control operates effectively.

---

# 20. Service-to-Process Traceability

N4-B establishes the minimum traceability:

```text
Service
    ↓
Process
```

For material services, the model may extend to:

```text
Service
    ↓
Process
    ↓
Owner
    ↓
KPI / KRI
    ↓
Monitoring
```

The actual depth is determined by materiality.

---

# 21. Process-to-Owner Traceability

The minimum ownership chain is:

```text
Process
    ↓
Owner
```

Where ownership is not established:

```text
Owner
= NOT ESTABLISHED
```

This shall become a controlled finding where ownership is materially required.

---

# 22. Service-to-KPI/KRI Traceability

Where material:

```text
Service
    ↓
KPI / KRI
```

The measure shall have a defined relationship to service performance, risk or control objectives.

---

# 23. Process-to-KPI/KRI Traceability

Where material:

```text
Process
    ↓
KPI / KRI
```

The relationship shall identify what aspect of the process is measured.

A KPI without a clear subject shall be treated as an incomplete operational relationship.

---

# 24. Evidence Binding

Each material service and process object shall support:

```text
Evidence ID
Evidence Source
Evidence Class
Evidence Date / Version
Evidence Currency
Evidence Sufficiency
```

Evidence shall be bound to the claim it supports.

A single generic document shall not automatically support every service/process attribute.

---

# 25. Operational Effectiveness Boundary

N4-B deliberately separates:

```text
Service Defined
Service Implemented
Service Operational
Service Effective
```

and:

```text
Process Defined
Process Implemented
Process Operational
Process Effective
```

Effectiveness requires evidence beyond object existence.

---

# 26. Operational Evidence Classification

Evidence sufficiency shall use:

```text
SUFFICIENT
PARTIALLY SUFFICIENT
INSUFFICIENT
CONFLICTING
UNKNOWN
```

Evidence currency:

```text
CURRENT
RECENT
STALE
HISTORICAL
UNKNOWN
```

---

# 27. Confidence Model

Service and process relationships may use:

```text
CONFIRMED
HIGH
MEDIUM
LOW
UNCONFIRMED
```

Confidence does not replace evidence.

---

# 28. Materiality

Service and process objects shall support:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

Materiality determines the required operational traceability depth.

---

# 29. Operational Depth

N4-B applies:

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

The primary N4 targets are:

```text
D7 — Operational
D8 — Measurement / Value
```

where material.

---

# 30. Service Record

Minimum controlled service record:

| Field | Requirement |
|---|---|
| Service ID | Required |
| Service Name | Required |
| Service Type | Required |
| Description | Conditional |
| Consumer | Conditional |
| Service Owner | Required where material |
| Supporting Implementation | Required where material |
| Process Relationship | Required where material |
| Criticality | Required |
| Lifecycle | Required |
| Operational Status | Required |
| Evidence | Required where operational claim is made |
| Materiality | Required |
| Confidence | Required |
| Status | Required |

---

# 31. Process Record

Minimum controlled process record:

| Field | Requirement |
|---|---|
| Process ID | Required |
| Process Name | Required |
| Process Type | Required |
| Purpose | Conditional |
| Service Relationship | Required where material |
| Process Owner | Required where material |
| Inputs / Outputs | Conditional |
| Controls | Conditional |
| KPI / KRI | Conditional |
| Monitoring | Conditional |
| Lifecycle | Required |
| Operational Status | Required |
| Evidence | Required where operational claim is made |
| Materiality | Required |
| Confidence | Required |
| Status | Required |

---

# 32. Service Relationship Record

Minimum relationship record:

```text
Relationship ID
Source Service
Relationship Type
Target Object
Evidence ID
Status
Materiality
Confidence
Owner / Steward
Finding
Disposition
```

---

# 33. Process Relationship Record

Minimum process relationship record:

```text
Relationship ID
Source Process
Relationship Type
Target Object
Evidence ID
Status
Materiality
Confidence
Owner / Steward
Finding
Disposition
```

---

# 34. Operational Orphan Rules

Potential service orphan:

```text
Service
+
No Required Process
```

Potential process orphan:

```text
Process
+
No Required Service Context
```

Potential ownership orphan:

```text
Material Service / Process
+
No Required Owner
```

Potential evidence orphan:

```text
Operational Claim
+
No Supporting Evidence
```

Orphans are findings, not automatic architecture defects.

---

# 35. Operational Contradiction Rules

Potential contradictions:

```text
Two Service Owners

Two Process Owners

Conflicting Service Criticality

Conflicting Service Lifecycle

Conflicting Process Lifecycle

Conflicting Service-to-Process Relationship

Conflicting KPI Context
```

Resolution requires:

```text
Evidence
OR
Controlled Acceptance
```

---

# 36. Planned vs Operational

The following transformations are prohibited:

```text
Service Catalogue
↓
OPERATIONAL

Process Document
↓
EFFECTIVE

Implementation Record
↓
OPERATIONAL SERVICE
```

Each transition requires evidence.

---

# 37. N3 Dependency

N4-B shall use N3 implementation relationships where relevant:

```text
Implementation Element
        ↓
Service
```

However:

```text
Implementation Element
≠
Service
```

unless the service relationship is established.

---

# 38. CAN-01 Boundary

CAN-01 remains subject to:

```text
COND-N2-I-01
```

and:

```text
COND-N3-E.01-01
```

The actual named CAN-01 implementation instance remains:

```text
NOT ESTABLISHED IN CONTROLLED SOURCE SET
```

Therefore N4-B shall not create an operational CAN-01 service as a factual implementation.

The model may define how such a service would be represented if evidence becomes available.

---

# 39. Operational Evidence Boundary

N4-B distinguishes:

```text
Service Model
≠
Actual Service

Process Model
≠
Actual Operational Process

Operational Relationship
≠
Operational Effectiveness
```

Evidence is required to cross these boundaries.

---

# 40. N4-B Completion Criteria

N4-B may be considered complete when:

```text
Service Object Model Defined
AND
Process Object Model Defined
AND
Service Identity Defined
AND
Process Identity Defined
AND
Service Lifecycle Defined
AND
Process Lifecycle Defined
AND
Ownership Model Defined
AND
Service / Process Relationship Model Defined
AND
Evidence Binding Defined
AND
Materiality / Confidence Defined
AND
Operational Depth Defined
AND
Orphan / Contradiction Rules Defined
AND
CAN-01 Evidence Boundary Preserved
AND
N4-C Inputs Prepared
```

---

# 41. Expected Outcome

The expected N4-B outcome is:

```text
CONTROLLED SERVICE MODEL
+
CONTROLLED PROCESS MODEL
+
CONTROLLED OWNERSHIP MODEL
+
CONTROLLED OPERATIONAL RELATIONSHIPS
+
CONTROLLED EVIDENCE BINDING
+
N4-C READY
```

The expected outcome is not:

```text
COMPLETE OPERATIONAL SERVICE INVENTORY
```

---

# 42. Anti-Runaway Control

N4-B shall not automatically create:

```text
N4-B.01
N4-B.02
N4-B.03
...
```

unless a materially distinct controlled event requires a separate artifact.

The controlled sequence remains:

```text
N4-A
    ↓
N4-B
    ↓
N4-C
```

---

# 43. Current State

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
= ACTIVE / SERVICE & PROCESS OPERATIONAL MODEL

N4-C
= NEXT CONTROLLED WORK PACKAGE

N4-D
= NOT STARTED

N4-E
= NOT STARTED

N5
= NOT AUTHORIZED
```

---

# 44. Final N4-B Statement

> **N4-B establishes the controlled Service & Process Operational Model for N4. It defines service and process identity, lifecycle, ownership, consumer relationships, implementation relationships, operational relationships, evidence binding, materiality, confidence, operational depth and orphan/contradiction controls. It deliberately separates service/process models from actual operational realization and effectiveness, preserving the evidence boundary inherited from N2 and N3.**

---

# 45. Document Control

**Document:** MFM Post-Steady-State Phase Control — N4-B Service & Process Operational Model  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-B-Service-and-Process-Operational-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-A — Operational Scope & Evidence Baseline  
**Upstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N4-B  
**Next Work Package:** N4-C — KPI/KRI, Monitoring & Operational Control Assessment  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N5 Generation:** PROHIBITED  

---

# 46. Terminal Principle

> **An operational service/process model defines the controlled semantic structure through which operational realization can be represented; it does not prove that a service or process is operationally active or effective. N4-B therefore establishes the model required for N4-C to assess measurement, monitoring and operational control using evidence rather than assumption.**
