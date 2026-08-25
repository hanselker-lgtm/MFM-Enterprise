# MFM Post-Steady-State Phase Control

## N4-C — KPI/KRI, Monitoring & Operational Control Assessment

**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-C-KPI-KRI-Monitoring-and-Operational-Control-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-C WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent Control:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-B — Service & Process Operational Model  
**Upstream Workstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N4-C performs the controlled assessment of:

```text
KPI
KRI
SLA / SLO Measures
Operational Metrics
Monitoring
Thresholds
Alerts
Dashboards
Operational Controls
Escalation
Evidence
```

The purpose is to determine whether material operational services and processes have sufficiently established measurement and monitoring relationships.

N4-C does not assume that a KPI, KRI or monitoring capability exists merely because the architecture model defines one.

---

# 2. Governing Principle

The operational control chain is:

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
    ↓
Alert / Threshold
    ↓
Operational Response
```

Each relationship is independently evidence-dependent.

The following transformations are prohibited:

```text
KPI Definition
↓
Active Measurement

Monitoring Design
↓
Operational Monitoring

Alert Definition
↓
Effective Response

Dashboard
↓
Operational Control
```

---

# 3. Source Baseline

N4-C consumes:

```text
N4-A
Operational Scope & Evidence Baseline

N4-B
Service & Process Operational Model
```

The N4-B model establishes the semantics for:

```text
Service
Process
Owner
KPI / KRI
Monitoring
Evidence
Lifecycle
Operational Status
Materiality
Confidence
```

N4-C now assesses the realization of the measurement and monitoring relationships.

---

# 4. Measurement Domains

N4-C assesses:

```text
MC-01 — KPI Architecture
MC-02 — KRI Architecture
MC-03 — SLA / SLO Measurement
MC-04 — Operational Metrics
MC-05 — Thresholds
MC-06 — Monitoring
MC-07 — Alerts
MC-08 — Dashboards / Reporting
MC-09 — Escalation
MC-10 — Operational Control Evidence
```

These are assessment domains, not assertions that corresponding instances exist.

---

# 5. MC-01 — KPI Architecture

A KPI may represent:

```text
Service Performance
Process Performance
Quality
Availability
Capacity
Efficiency
Customer Outcome
Compliance
Financial / Resource Performance
```

A material KPI should establish:

```text
KPI ID
Definition
Purpose
Owner
Target
Threshold
Source
Frequency
Service / Process Relationship
Reporting Context
Evidence
```

---

# 6. KPI Definition vs KPI Realization

N4-C shall distinguish:

```text
KPI Defined
KPI Configured
KPI Measured
KPI Reported
KPI Reviewed
KPI Used for Decision
```

These are separate states.

A definition alone does not establish measurement.

---

# 7. MC-02 — KRI Architecture

A KRI may represent:

```text
Operational Risk
Security Risk
Compliance Risk
Availability Risk
Capacity Risk
Service Risk
Process Risk
```

A material KRI should establish:

```text
KRI ID
Risk Context
Definition
Owner
Threshold
Source
Frequency
Service / Process Relationship
Escalation
Evidence
```

A KRI definition does not establish active risk monitoring.

---

# 8. KRI Realization States

N4-C shall distinguish:

```text
DEFINED
CONFIGURED
MEASURED
MONITORED
REPORTED
ESCALATED
REVIEWED
```

Evidence is required to establish each state where material.

---

# 9. MC-03 — SLA / SLO Measurement

Where applicable, N4-C assesses:

```text
SLA
SLO
Target
Threshold
Measurement Source
Measurement Frequency
Owner
Reporting
Exception Handling
Evidence
```

The existence of an SLA/SLO document does not establish that the target is actively measured.

---

# 10. MC-04 — Operational Metrics

Operational metrics may include:

```text
Availability
Latency
Throughput
Capacity
Error Rate
Quality
Volume
Response Time
Resolution Time
Security Events
Compliance Measures
```

Metric relevance shall be determined by materiality.

---

# 11. Metric Identity

Each material metric should support:

```text
Metric ID
Name
Definition
Unit
Source
Calculation
Frequency
Owner
Threshold
Target
Service / Process Context
Evidence
```

Ambiguous metrics shall be classified as identity or definition issues.

---

# 12. MC-05 — Thresholds

A material measurement may have:

```text
Target
Warning Threshold
Critical Threshold
Tolerance
Escalation Threshold
```

Thresholds shall be evidence-backed.

The existence of a threshold does not automatically establish that it is actively monitored.

---

# 13. MC-06 — Monitoring

Monitoring assessment includes:

```text
Monitoring Object
Source
Metric
Frequency
Threshold
Collection
Storage
Visualization
Alerting
Owner
Evidence
```

N4-C shall distinguish:

```text
Monitoring Designed
Monitoring Configured
Monitoring Active
Monitoring Evidenced
```

---

# 14. Monitoring Status

Controlled monitoring states:

```text
PLANNED
DESIGNED
CONFIGURED
ACTIVE
SUSPENDED
RETIRED
UNKNOWN
```

The transition:

```text
CONFIGURED
↓
ACTIVE
```

requires evidence.

---

# 15. MC-07 — Alerts

Where material, monitoring may generate:

```text
Alert
Notification
Escalation
Incident
```

The alert model may include:

```text
Alert ID
Source
Metric
Threshold
Severity
Recipient
Escalation
Response
Evidence
```

An alert definition does not prove that alerts are actually generated.

---

# 16. Alert-to-Incident Relationship

The controlled relationship is:

```text
Alert
    ↓
Incident
```

where incident creation is required.

Possible states:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
NOT REQUIRED
UNVERIFIED
CONFLICTING
```

---

# 17. MC-08 — Dashboards / Reporting

N4-C may assess:

```text
Dashboard
Report
Operational Review
Management Report
Risk Report
Service Report
```

The assessment shall distinguish:

```text
Dashboard Exists
Data Populates
Data Is Current
Data Is Reviewed
Data Drives Decision
```

A dashboard is not automatically an operational control.

---

# 18. MC-09 — Escalation

Material monitoring conditions may require escalation.

The baseline relationship is:

```text
Threshold
    ↓
Alert
    ↓
Escalation
    ↓
Owner / Response
```

N4-C shall assess:

```text
Escalation Rule
Escalation Owner
Escalation Time
Escalation Evidence
Response
```

---

# 19. MC-10 — Operational Control Evidence

Operational control evidence may include:

```text
Monitoring Logs
Metric Records
KPI Reports
KRI Reports
SLA Reports
Dashboards
Alert Logs
Escalation Records
Operational Reviews
Control Test Results
Audit Evidence
```

Evidence sufficiency shall be assessed rather than assumed.

---

# 20. Measurement Evidence Model

Evidence shall be classified:

```text
E0 — Conceptual
E1 — Architectural
E2 — Governance / Implementation Model
E3 — Actual Implementation Evidence
```

For claims such as:

```text
KPI is actively measured
KRI is actively monitored
Monitoring is active
Alerting operates
Operational control is exercised
```

appropriate E3 evidence is normally required.

---

# 21. Evidence Currency

Measurement and monitoring evidence shall be classified:

```text
CURRENT
RECENT
STALE
HISTORICAL
UNKNOWN
```

Historical reports may establish historical operation but do not automatically establish current operation.

---

# 22. Measurement Sufficiency

N4-C shall evaluate:

```text
Identity
Definition
Source
Calculation
Frequency
Owner
Target
Threshold
Relationship
Evidence
Currency
```

A measurement claim is sufficient only when the relevant required attributes are supported.

---

# 23. Operational Control Model

A material operational control may be represented as:

```text
Objective
    ↓
Control
    ↓
Measurement
    ↓
Monitoring
    ↓
Threshold
    ↓
Alert
    ↓
Response
    ↓
Evidence
```

The model shall distinguish:

```text
CONTROL DESIGNED
CONTROL IMPLEMENTED
CONTROL OPERATING
CONTROL EFFECTIVE
```

These are not interchangeable.

---

# 24. Control Effectiveness Boundary

N4-C shall not classify a control as:

```text
EFFECTIVE
```

merely because:

```text
Control Exists
```

Effectiveness requires evidence appropriate to the claim.

---

# 25. KPI / Service Relationship

Where material:

```text
Service
    ↓
KPI
```

shall identify the operational outcome or performance dimension being measured.

Possible states:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
UNVERIFIED
NOT REQUIRED
CONFLICTING
```

---

# 26. KPI / Process Relationship

Where material:

```text
Process
    ↓
KPI
```

shall identify the process performance dimension being measured.

---

# 27. KRI / Risk Relationship

Where material:

```text
Risk
    ↓
KRI
```

shall identify the monitored risk condition.

The existence of a KRI without an identified risk context shall be treated as an incomplete relationship.

---

# 28. Monitoring / Service Relationship

Where material:

```text
Service
    ↓
Monitoring
```

shall identify how service health or performance is observed.

---

# 29. Monitoring / Process Relationship

Where material:

```text
Process
    ↓
Monitoring
```

shall identify how process performance or control conditions are observed.

---

# 30. Measurement / Owner Relationship

A material KPI/KRI should establish:

```text
Measure
    ↓
Owner
```

Owner state:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
NOT ESTABLISHED
CONFLICTING
```

---

# 31. Measurement / Evidence Relationship

Every material operational measurement claim should be traceable to evidence.

Minimum relationship:

```text
Measure
    ↓
Evidence
```

The evidence shall support the specific claim being made.

---

# 32. Monitoring / Evidence Relationship

Monitoring claims require evidence such as:

```text
Configuration
Logs
Monitoring Records
Alerts
Dashboards
Operational Reviews
```

The evidence source must be relevant to the claimed monitoring state.

---

# 33. Operational Control Finding Classes

N4-C may identify:

```text
MCF-01 Missing KPI
MCF-02 Missing KRI
MCF-03 Missing Target
MCF-04 Missing Threshold
MCF-05 Missing Monitoring
MCF-06 Monitoring Not Evidenced
MCF-07 Missing Alert
MCF-08 Missing Escalation
MCF-09 Missing Owner
MCF-10 Missing Evidence
MCF-11 Stale Measurement
MCF-12 Conflicting Measurement
MCF-13 Unverified Measurement
MCF-14 Control Effectiveness Not Established
MCF-15 Measurement Depth Deficiency
```

These are controlled finding classes.

---

# 34. False-Gap Control

The following interpretations are prohibited:

```text
No KPI Record
≠
No Performance Measurement

No Dashboard
≠
No Monitoring

No Alert Record
≠
No Alerting Capability

No Incident
≠
No Operational Response

No Recent Report
≠
No Current Monitoring
```

A genuine gap requires sufficient evidence of required absence.

---

# 35. Orphan Control

Potential measurement or monitoring orphans include:

```text
KPI without Service / Process Context

KRI without Risk Context

Metric without Owner

Threshold without Metric

Monitoring without Metric

Alert without Monitoring Source

Escalation without Alert / Trigger

Dashboard without Defined Data Source
```

These are assessment conditions.

---

# 36. Contradiction Control

Potential contradictions include:

```text
Different KPI Definitions
Different Targets
Different Thresholds
Different Owners
Different Reporting Frequencies
Different Service Criticality
Different Monitoring Status
```

Contradictions require evidence-based resolution or controlled acceptance.

---

# 37. Materiality and Depth

N4-C applies:

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

N4-C primarily assesses:

```text
D7
D8
```

The required depth shall be determined by materiality.

---

# 38. CAN-01 Boundary

The inherited condition remains:

```text
COND-N3-E.01-01
```

The actual named CAN-01 implementation instance remains:

```text
NOT ESTABLISHED IN CONTROLLED SOURCE SET
```

Therefore N4-C shall not assert:

```text
CAN-01 KPI exists
CAN-01 monitoring exists
CAN-01 alerting exists
CAN-01 operational control exists
```

unless appropriate evidence establishes those claims.

---

# 39. Assessment Register

N4-C shall use the following minimum assessment structure:

| Assessment ID | Subject | Type | Required Depth | Evidence | Status | Finding |
|---|---|---|---|---|---|---|
| N4-C-001 | Service | KPI | D8 | TBD | OPEN | TBD |
| N4-C-002 | Service | KRI | D8 | TBD | OPEN | TBD |
| N4-C-003 | Service | Monitoring | D7 | TBD | OPEN | TBD |
| N4-C-004 | Monitoring | Alert | D7 | TBD | OPEN | TBD |
| N4-C-005 | Alert | Escalation | D7 | TBD | OPEN | TBD |
| N4-C-006 | Control | Effectiveness | D8 | TBD | OPEN | TBD |

This is a controlled assessment structure, not evidence that these items currently exist.

---

# 40. N4-C Completion Criteria

N4-C may be considered complete when:

```text
KPI Model Assessed
AND
KRI Model Assessed
AND
SLA / SLO Measurement Assessed
AND
Operational Metrics Assessed
AND
Thresholds Assessed
AND
Monitoring Assessed
AND
Alerts Assessed
AND
Dashboards / Reporting Assessed
AND
Escalation Assessed
AND
Operational Control Evidence Assessed
AND
Material Findings Identified
AND
False-Gap Control Applied
AND
CAN-01 Evidence Boundary Preserved
AND
N4-D Inputs Prepared
```

---

# 41. Expected Outcome

The expected N4-C outcome is:

```text
CONTROLLED MEASUREMENT ASSESSMENT
+
CONTROLLED MONITORING ASSESSMENT
+
CONTROLLED OPERATIONAL CONTROL ASSESSMENT
+
CONTROLLED EVIDENCE BOUNDARY
+
CONTROLLED FINDINGS
+
N4-D READY
```

The expected outcome is not:

```text
COMPLETE KPI / KRI INVENTORY
```

or:

```text
PROOF OF OPERATIONAL EFFECTIVENESS
```

unless supported by evidence.

---

# 42. Anti-Runaway Control

N4-C shall not automatically create:

```text
N4-C.01
N4-C.02
N4-C.03
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
= COMPLETED / SERVICE & PROCESS OPERATIONAL MODEL

N4-C
= ACTIVE / KPI-KRI, MONITORING & OPERATIONAL CONTROL ASSESSMENT

N4-D
= NEXT CONTROLLED WORK PACKAGE

N4-E
= NOT STARTED

N5
= NOT AUTHORIZED
```

---

# 44. Final N4-C Statement

> **N4-C establishes the controlled assessment of KPI, KRI, measurement, monitoring, alerting, escalation and operational control realization. It distinguishes definitions from active operation and control design from control effectiveness, applies evidence and materiality controls, and preserves the false-gap principle. N4-C therefore provides the controlled assessment basis for N4-D without asserting operational effectiveness that has not been evidenced.**

---

# 45. Document Control

**Document:** MFM Post-Steady-State Phase Control — N4-C KPI/KRI, Monitoring & Operational Control Assessment  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N4-C-KPI-KRI-Monitoring-and-Operational-Control-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — N4-C WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N4 — Operational Architecture  
**Parent:** N4.00 — Operational Architecture Scope, Charter and Work Package Control  
**Predecessor:** N4-B — Service & Process Operational Model  
**Upstream:** N3 — Implementation Architecture  
**N3 Closure:** N3-SC-90 — CLOSED  
**N3 Completion:** N3C-2 — COMPLETE WITH CONDITIONS  
**N4 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N4-C  
**Next Work Package:** N4-D — Incident, Problem, Change & Improvement Assessment  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N5 Generation:** PROHIBITED  

---

# 46. Terminal Principle

> **A KPI, KRI, monitoring definition or control model is not evidence of operational realization. N4-C therefore assesses the transition from defined measurement and monitoring structures to evidenced operational control, while preserving the distinction between design, implementation, operation and effectiveness.**
