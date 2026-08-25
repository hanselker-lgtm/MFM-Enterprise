# MFM Post-Steady-State Governance

## STEADY-STATE-003 — Governance Signal Intake & Materiality Assessment

**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-003-Governance-Signal-Intake-and-Materiality-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — SIGNAL INTAKE & MATERIALITY CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-002 — Governance Monitoring, Trigger Management & Continuous Review  
**Next Controlled Work Package:** STEADY-STATE-004 — Governance Routing, Assessment & Decision Preparation  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  

---

# 1. Purpose

STEADY-STATE-003 establishes the controlled mechanism by which signals detected through steady-state monitoring are formally received, recorded, classified, screened for materiality and prepared for governance routing.

The operating sequence is:

```text
SIGNAL DETECTED
↓
SIGNAL INTAKE
↓
RECORD
↓
CLASSIFY
↓
MATERIALITY SCREEN
↓
ROUTE / HOLD / CLOSE
```

The control does not itself constitute a decision authority.

---

# 2. Scope

The control applies to signals entering from:

```text
GB-01 Strategic Monitoring
GB-02 Architecture Governance
GB-03 Capability Governance
GB-04 Portfolio Governance
GB-05 Investment Governance
GB-06 Risk Governance
GB-07 Dependency Governance
GB-08 Change Governance
GB-09 Outcome Governance
GB-10 Value Governance
GB-11 Evidence Governance
GB-12 Decision Governance
```

and from relevant external or operational sources.

---

# 3. Signal Intake Principle

The intake mechanism shall preserve the distinction:

```text
Observation
≠
Signal

Signal
≠
Issue

Issue
≠
Material Issue

Material Issue
≠
Governance Failure
```

The intake process records the signal before conclusions are drawn.

---

# 4. Signal Sources

Potential sources include:

```text
Monitoring Records
Strategic Reviews
Architecture Reviews
Capability Reviews
Portfolio Reviews
Investment Reviews
Risk Reviews
Dependency Reviews
Change Records
Outcome Measurements
Value Measurements
Evidence Reviews
Assurance Findings
Condition Reviews
Stakeholder Input
Operational Experience
Regulatory Developments
Technology Developments
Environmental Developments
```

Source credibility shall be assessed where materiality depends upon source reliability.

---

# 5. Intake Record

Each signal shall receive an intake record containing, where available:

```text
Signal ID
Date / Time
Source
Originating Domain
Description
Initial Classification
Initial Materiality
Evidence
Potential Impact
Initial Owner
Status
```

Where information is unavailable:

```text
UNKNOWN
UNVERIFIED
TBD
```

shall be used as appropriate.

No missing information shall be silently invented.

---

# 6. Signal Identification

A signal should identify:

```text
WHAT HAPPENED?
WHEN?
WHERE?
SOURCE?
WHAT CHANGED?
WHY MAY IT MATTER?
WHAT EVIDENCE EXISTS?
```

A signal description should remain factual until assessment establishes otherwise.

---

# 7. Signal Classification

Initial classification may include:

```text
INFORMATION
OBSERVATION
ISSUE
CHANGE
RISK
DEPENDENCY
DECISION
CONDITION
OUTCOME VARIANCE
VALUE VARIANCE
EVIDENCE GAP
GOVERNANCE SIGNAL
```

Where classification is uncertain:

```text
UNKNOWN
```

shall be retained pending assessment.

---

# 8. Materiality Screening

Materiality screening considers:

```text
Strategic Impact
Business Impact
Architecture Impact
Capability Impact
Portfolio Impact
Investment Impact
Risk Impact
Dependency Impact
Outcome Impact
Value Impact
Regulatory Impact
Operational Impact
```

The screening result may be:

```text
NON-MATERIAL
MATERIAL
MAJOR
CRITICAL
UNKNOWN
```

---

# 9. Materiality Principle

Materiality shall be based on the potential significance of the signal, not merely on its source.

Therefore:

```text
Important Source
≠
Automatically Material

Unknown Source
≠
Automatically Non-Material
```

---

# 10. Materiality Factors

Where appropriate, assess:

```text
Magnitude
Duration
Scope
Reversibility
Urgency
Interdependency
Strategic Relevance
Risk Exposure
Regulatory Exposure
Outcome Exposure
Value Exposure
```

---

# 11. Materiality Decision Boundary

The intake control may determine:

```text
CLOSE AS NON-MATERIAL
```

where sufficient evidence supports that classification.

It may also determine:

```text
ROUTE FOR GOVERNANCE ASSESSMENT
```

where the signal is potentially material.

It shall not make a substantive governance decision outside its authority.

---

# 12. Unknown / Unverified Handling

Where evidence is insufficient:

```text
UNKNOWN
```

or:

```text
UNVERIFIED
```

shall be preserved.

The correct response to uncertainty may be:

```text
REQUEST MORE EVIDENCE
```

rather than:

```text
ASSUME MATERIAL
```

or:

```text
ASSUME NON-MATERIAL
```

---

# 13. Signal Intake Register

| Field | Required |
|---|---|
| Signal ID | YES |
| Date | YES |
| Source | YES |
| Domain | YES |
| Description | YES |
| Classification | YES |
| Materiality | YES |
| Evidence | WHERE AVAILABLE |
| Owner | WHERE IDENTIFIED |
| Status | YES |

Initial register state:

```text
READY FOR ACTUAL SIGNALS
```

No fabricated signal records shall be entered.

---

# 14. Signal Lifecycle

The standard lifecycle is:

```text
DETECTED
↓
RECEIVED
↓
RECORDED
↓
CLASSIFIED
↓
MATERIALITY SCREENED
↓
ROUTED / HOLD / CLOSED
↓
ASSESSMENT
```

STEADY-STATE-003 ends at the routing boundary unless a non-material signal is legitimately closed.

---

# 15. Routing Preparation

For potentially material signals, prepare:

```text
Signal Summary
Materiality Assessment
Relevant Domain
Potentially Affected Domains
Evidence
Known Owner
Required Authority
Recommended Route
Urgency
```

The recommendation is not itself a decision.

---

# 16. Cross-Domain Screening

A signal shall be screened for impact across:

```text
Strategy
Architecture
Capability
Portfolio
Investment
Risk
Dependency
Change
Outcome
Value
Evidence
Decision
```

A signal may belong to one primary domain while affecting multiple domains.

---

# 17. Primary Domain

Where possible, identify:

```text
Primary Governance Domain
```

and:

```text
Affected Governance Domains
```

If no primary domain can be established:

```text
INTEGRATED GOVERNANCE REVIEW
```

may be appropriate.

---

# 18. Urgency

Initial urgency may be:

```text
ROUTINE
WATCH
URGENT
CRITICAL
UNKNOWN
```

Urgency shall be based on available evidence.

---

# 19. Escalation Preparation

Potential escalation triggers include:

```text
Critical Risk
Critical Dependency
Material Strategic Change
Material Architecture Change
Material Outcome Failure
Material Value Variance
Material Evidence Failure
Authority Conflict
Repeated Governance Deviation
Regulatory Exposure
```

The intake control prepares the escalation; the appropriate authority decides the escalation where required.

---

# 20. Evidence Boundary

Evidence captured at intake supports:

```text
Signal Existence
Signal Source
Initial Context
Initial Materiality Assessment
```

It does not automatically prove:

```text
Root Cause
Governance Failure
Outcome Failure
Value Failure
Control Ineffectiveness
```

Those claims require further assessment.

---

# 21. Decision Boundary

The following distinctions remain mandatory:

```text
Signal Intake
≠
Assessment

Assessment
≠
Decision

Decision
≠
Authorization

Authorization
≠
Funding

Funding
≠
Implementation
```

---

# 22. Condition Intake

Where a signal concerns an existing condition, link it to the condition record:

```text
CLOSE-N9-01 through CLOSE-N9-10
COND-POST-N9-004-01 through COND-POST-N9-004-04
ACT-POST-N9-005-01 through ACT-POST-N9-005-05
```

The intake record shall preserve the relationship.

---

# 23. Risk Signal Intake

Where the signal represents a risk:

```text
Signal ID
→ Risk Record
```

The risk governance process then becomes authoritative for detailed risk assessment.

---

# 24. Dependency Signal Intake

Where the signal represents a dependency:

```text
Signal ID
→ Dependency Record
```

Dependency governance becomes authoritative for detailed dependency management.

---

# 25. Change Signal Intake

Where the signal represents a change:

```text
Signal ID
→ Change Record
```

Change governance becomes authoritative for detailed change assessment and authorization.

---

# 26. Outcome Signal Intake

Where the signal indicates outcome variance:

```text
Signal ID
→ Outcome Record
```

Outcome governance becomes authoritative for detailed outcome assessment.

---

# 27. Value Signal Intake

Where the signal indicates value variance:

```text
Signal ID
→ Value Record
```

Value governance becomes authoritative for detailed value assessment.

---

# 28. Evidence Gap Intake

Where the signal indicates an evidence gap:

```text
Signal ID
→ Evidence Gap Record
```

Evidence governance becomes authoritative for evidence remediation and validation.

---

# 29. Governance Signal Intake

Where the signal indicates potential governance failure:

```text
Signal ID
→ Governance Finding
```

Further assessment is required before confirming governance failure.

---

# 30. Signal Closure

A signal may be closed at intake only where:

```text
NON-MATERIAL
AND
SUFFICIENTLY UNDERSTOOD
AND
NO FURTHER GOVERNANCE ACTION REQUIRED
```

Closure evidence shall be retained.

---

# 31. Signal Hold

A signal may be placed on:

```text
HOLD — INFORMATION REQUIRED
```

where:

```text
Materiality Cannot Yet Be Determined
OR
Source Requires Validation
OR
Impact Requires Clarification
```

A held signal shall have a review requirement.

---

# 32. Signal Reopening

A closed or held signal may be reconsidered when:

```text
New Evidence
Material Change
New Impact
Repeated Occurrence
Escalation
Condition Change
```

Reconsideration does not automatically reopen N9.

---

# 33. Intake Quality

The intake mechanism shall periodically assess:

```text
Completeness
Accuracy
Timeliness
Classification Quality
Materiality Quality
Routing Quality
Duplicate Detection
Traceability
```

Possible state:

```text
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNVERIFIED
```

---

# 34. Duplicate Signals

Where multiple signals describe the same event:

```text
Primary Signal
+
Linked / Duplicate Signals
```

shall be used where appropriate.

No material signal shall be lost merely because a duplicate exists.

---

# 35. Signal Traceability

Each material signal should be traceable:

```text
SOURCE
↓
SIGNAL
↓
CLASSIFICATION
↓
MATERIALITY
↓
ROUTING
↓
ASSESSMENT
↓
DECISION
↓
ACTION
↓
EVIDENCE
↓
OUTCOME
```

STEADY-STATE-003 is responsible for the traceability up to the routing boundary.

---

# 36. Future Work Package Trigger

A dedicated work package may be considered where:

```text
Signal Intake Gap Is Material
AND
Dedicated Scope Is Required
AND
Dedicated Deliverables Are Required
AND
Dedicated Completion Criteria Are Required
```

---

# 37. Future Phase Protection

A future phase requires separate:

```text
Need
Scope
Objectives
Boundaries
Risks
Dependencies
Evidence Requirements
Readiness
Authority
Authorization
```

---

# 38. N10 Protection

Mandatory rule:

```text
STEADY-STATE-003
≠
N10 AUTHORIZATION
```

Current state:

```text
N10
= NOT DEFINED
= NOT AUTHORIZED
```

---

# 39. N9 Protection

N9 remains:

```text
CLOSED WITH CONDITIONS
```

Signal intake does not reopen N9.

Any reopening requires a separate controlled assessment and authorization.

---

# 40. N8 Protection

N8 remains:

```text
CLOSED WITH CONDITIONS
```

No automatic reopening is permitted.

---

# 41. Completion Criteria

STEADY-STATE-003 initial establishment is complete when:

```text
Signal Sources Defined
AND
Intake Record Defined
AND
Classification Defined
AND
Materiality Screening Defined
AND
Unknown / Unverified Handling Defined
AND
Cross-Domain Screening Defined
AND
Routing Preparation Defined
AND
Evidence Boundary Defined
AND
Closure / Hold Rules Defined
AND
Traceability Defined
AND
Quality Review Defined
```

Thereafter:

```text
STEADY-STATE-003
= CONTINUOUSLY ACTIVE
```

---

# 42. Current Program State

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

N6
= CLOSED / N6C-2
  COMPLETE WITH CONDITIONS

N7
= CLOSED / N7C-2
  COMPLETE WITH CONDITIONS

N8
= CLOSED WITH CONDITIONS

N9
= CLOSED WITH CONDITIONS

POST-N9 TRANSITION
= CLOSED WITH CONDITIONS

STEADY-STATE-001
= ACTIVE
  CONTINUOUS GOVERNANCE OPERATING CHARTER

STEADY-STATE-002
= ACTIVE
  CONTINUOUS MONITORING CONTROL

STEADY-STATE-003
= ACTIVE
  SIGNAL INTAKE & MATERIALITY CONTROL

N10
= NOT DEFINED
= NOT AUTHORIZED
```

---

# 43. Next Controlled Work Package

The next controlled work package is:

```text
STEADY-STATE-004
Governance Routing, Assessment & Decision Preparation
```

STEADY-STATE-004 shall take materially relevant signals from the controlled intake boundary and prepare them for structured governance assessment, decision formulation and appropriate authority routing.

---

# 44. Final STEADY-STATE-003 Statement

> **STEADY-STATE-003 establishes the controlled intake boundary for governance signals. It ensures that detected signals are recorded, classified, screened for materiality, checked for cross-domain impact and prepared for appropriate routing without prematurely converting observations into issues or issues into governance failures. The control preserves uncertainty where evidence is insufficient and maintains traceability from source through routing. It remains continuously active and does not authorize N8, N9 reopening or N10.**

---

# 45. Document Control

**Document:** MFM Post-Steady-State Governance — Governance Signal Intake & Materiality Assessment  
**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-003-Governance-Signal-Intake-and-Materiality-Assessment-001  
**Version:** 1.0  
**Status:** ACTIVE — SIGNAL INTAKE & MATERIALITY CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-002 — Governance Monitoring, Trigger Management & Continuous Review  
**Next Controlled Work Package:** STEADY-STATE-004 — Governance Routing, Assessment & Decision Preparation  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  
**Automatic N10 Authorization:** PROHIBITED  
**Automatic N9 Reopening:** PROHIBITED  
**Automatic N8 Reopening:** PROHIBITED  
