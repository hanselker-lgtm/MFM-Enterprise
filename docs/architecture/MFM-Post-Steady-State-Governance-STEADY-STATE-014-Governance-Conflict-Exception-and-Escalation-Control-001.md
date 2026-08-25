# MFM Post-Steady-State Governance

## STEADY-STATE-014 — Governance Conflict, Exception & Escalation Control

**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-014-Governance-Conflict-Exception-and-Escalation-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — GOVERNANCE CONFLICT, EXCEPTION & ESCALATION CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-013 — Governance Access, Accountability & Segregation-of-Duties Control  
**Next Controlled Work Package:** STEADY-STATE-015 — Governance Continuity, Resilience & Recovery Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  

---

# 1. Purpose

STEADY-STATE-014 establishes the controlled mechanism for identifying, classifying, resolving, authorizing, recording, monitoring and escalating governance conflicts, exceptions, authority gaps and unresolved control issues.

The purpose is to prevent unresolved ambiguity from becoming uncontrolled governance practice.

The operating sequence is:

```text
CONFLICT / EXCEPTION / GAP
↓
IDENTIFY
↓
CLASSIFY
↓
ASSESS
↓
ROUTE
↓
DECIDE
↓
AUTHORIZE WHERE REQUIRED
↓
IMPLEMENT / CONTROL
↓
MONITOR
↓
CLOSE / ESCALATE
```

---

# 2. Core Principle

A conflict or exception shall remain visible until it is appropriately resolved, accepted, transferred or escalated.

The following distinctions are mandatory:

```text
ISSUE IDENTIFIED
≠
ISSUE RESOLVED

EXCEPTION REQUESTED
≠
EXCEPTION APPROVED

EXCEPTION APPROVED
≠
EXCEPTION IMPLEMENTED

EXCEPTION IMPLEMENTED
≠
EXCEPTION CLOSED

CONFLICT DISCOVERED
≠
CONFLICT RESOLVED

ESCALATED
≠
DECIDED
```

---

# 3. Scope

STEADY-STATE-014 applies to:

```text
Governance Conflicts
Policy Conflicts
Authority Conflicts
Role Conflicts
Architecture Conflicts
Capability Conflicts
Portfolio Conflicts
Risk Conflicts
Dependency Conflicts
Change Conflicts
Outcome Conflicts
Value Conflicts
Evidence Conflicts
Baseline Conflicts
Access Conflicts
Segregation-of-Duties Conflicts
Exceptions
Waivers
Temporary Deviations
Unresolved Decisions
Authority Gaps
Accountability Gaps
Control Gaps
```

---

# 4. Conflict Definition

A conflict exists where two or more governance positions, requirements, authorities, records, decisions, interests or constraints cannot simultaneously be satisfied without further assessment or decision.

Possible conflict sources:

```text
Requirement vs Requirement
Policy vs Policy
Authority vs Authority
Decision vs Decision
Baseline vs Baseline
Risk vs Objective
Outcome vs Constraint
Architecture vs Capability
Portfolio vs Investment
Dependency vs Schedule
Access vs Segregation of Duties
Evidence vs Evidence
```

---

# 5. Exception Definition

An exception is a formally recognized deviation from an approved requirement, control, baseline, process or governance condition.

An exception shall identify:

```text
Requirement
Deviation
Reason
Risk
Impact
Duration
Owner
Authority
Compensating Control
Review Trigger
Status
```

---

# 6. Waiver Boundary

A waiver shall not silently remove the underlying requirement.

```text
WAIVER
≠
REQUIREMENT DELETED
```

The underlying requirement remains identifiable unless formally changed through the applicable governance process.

---

# 7. Temporary Deviation

A temporary deviation shall define:

```text
Scope
Reason
Start
End / Review Trigger
Risk
Conditions
Compensating Controls
Owner
Authority
Evidence
```

Temporary status shall not become indefinite by inactivity.

---

# 8. Exception Classification

Possible classification:

```text
MINOR
MATERIAL
MAJOR
CRITICAL
EMERGENCY
UNKNOWN
```

Classification shall consider:

```text
Impact
Risk
Duration
Scope
Reversibility
Strategic Importance
Authority
Regulatory Impact
Outcome Impact
Value Impact
```

---

# 9. Conflict Classification

Possible conflict states:

```text
LOCAL
CROSS-DOMAIN
MATERIAL
SYSTEMIC
CRITICAL
UNVERIFIED
```

A conflict may be reclassified as evidence improves.

---

# 10. Authority Conflict

Where two authorities claim incompatible decision rights:

```text
AUTHORITY CONFLICT
↓
IDENTIFY AUTHORITIES
↓
REVIEW AUTHORITY BASIS
↓
ASSESS HIERARCHY / SCOPE
↓
ROUTE
↓
DECIDE
↓
RECORD
```

No party shall resolve a material authority conflict solely by asserting its own authority.

---

# 11. Policy / Rule Conflict

Where governance rules conflict:

```text
CONFLICT IDENTIFIED
↓
IDENTIFY CONTROLLING BASELINES
↓
ASSESS SCOPE
↓
ASSESS MATERIALITY
↓
ROUTE TO APPROPRIATE AUTHORITY
↓
DECIDE
↓
UPDATE BASELINE IF REQUIRED
```

---

# 12. Evidence Conflict

Where evidence sources disagree:

```text
CONFLICT IDENTIFIED
↓
PROVENANCE REVIEW
↓
SOURCE QUALITY REVIEW
↓
TIME / SCOPE REVIEW
↓
INDEPENDENCE REVIEW WHERE REQUIRED
↓
RESOLVE / RETAIN AS UNRESOLVED
```

An unresolved evidence conflict shall remain visible.

---

# 13. Conflict of Interest

Where a participant has a material personal, organizational or decision-related conflict that may affect impartiality:

```text
CONFLICT IDENTIFIED
↓
DECLARE
↓
ASSESS
↓
RESTRICT / REASSIGN / COMPENSATE
↓
RECORD
```

The applicable organizational policies and legal requirements remain controlling.

---

# 14. Conflict Materiality

Materiality may consider:

```text
Financial Impact
Strategic Impact
Risk
Regulatory Impact
Safety / Operational Impact
Architecture Impact
Capability Impact
Reputational Impact
Outcome Impact
Value Impact
Scope
Duration
Reversibility
```

---

# 15. Exception Assessment

An exception assessment should consider:

```text
Why Is Deviation Required?
What Requirement Is Affected?
What Is the Risk?
What Is the Impact?
What Alternatives Exist?
Can the Requirement Be Met Another Way?
What Compensating Controls Exist?
How Long Is the Exception Needed?
Who Owns It?
Who Authorizes It?
How Will It Be Reviewed?
```

---

# 16. Exception Decision

Possible outcomes:

```text
APPROVED
APPROVED WITH CONDITIONS
REJECTED
DEFERRED
WITHDRAWN
EXPIRED
UNVERIFIED
```

---

# 17. Exception Conditions

Conditions may include:

```text
Additional Control
Additional Evidence
Reduced Scope
Shorter Duration
Additional Review
Independent Validation
Risk Acceptance
Compensating Control
Mandatory Remediation
```

Conditions shall be tracked independently.

---

# 18. Exception Register

| Field | Required |
|---|---|
| Exception ID | YES |
| Requirement | YES |
| Deviation | YES |
| Reason | YES |
| Risk | YES |
| Impact | YES |
| Duration | YES |
| Owner | YES |
| Authority | YES |
| Conditions | WHERE APPLICABLE |
| Compensating Control | WHERE APPLICABLE |
| Review Trigger | YES |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL EXCEPTION RECORDS
```

---

# 19. Conflict Register

| Field | Required |
|---|---|
| Conflict ID | YES |
| Type | YES |
| Parties / Sources | YES |
| Issue | YES |
| Evidence | YES |
| Materiality | YES |
| Risk | YES |
| Authority | WHERE APPLICABLE |
| Decision | WHERE RESOLVED |
| Conditions | WHERE APPLICABLE |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL CONFLICT RECORDS
```

---

# 20. Escalation Definition

Escalation occurs when an issue cannot be appropriately resolved at the current governance level or exceeds defined authority, materiality or risk thresholds.

Escalation is a routing mechanism.

```text
ESCALATION
≠
DECISION
```

---

# 21. Escalation Triggers

Escalation may be triggered by:

```text
Authority Gap
Authority Conflict
Critical Risk
Material Risk
Systemic Conflict
Unresolved Material Exception
Repeated Exception
Expired Exception
Material Outcome Failure
Material Value Failure
Evidence Integrity Failure
Baseline Conflict
Regulatory Conflict
Unresolved Accountability Gap
Critical Dependency
```

---

# 22. Escalation Levels

Possible levels:

```text
LOCAL
FUNCTIONAL
CROSS-DOMAIN
SENIOR GOVERNANCE
EXECUTIVE
EMERGENCY
```

The applicable level shall be determined by materiality, authority and risk.

---

# 23. Escalation Record

Each material escalation should identify:

```text
Escalation ID
Trigger
Issue
Evidence
Materiality
Risk
Current Authority
Requested Authority
Options
Recommendation
Decision
Conditions
Status
```

---

# 24. Escalation Completeness

An escalation should contain sufficient information to allow the receiving authority to make an informed decision.

At minimum:

```text
Problem
Evidence
Impact
Risk
Options
Recommendation
Decision Required
Deadline / Trigger
```

---

# 25. Escalation Without Decision

Where an escalation has occurred but no decision has yet been made:

```text
ESCALATED — DECISION PENDING
```

shall remain the status.

It shall not be represented as resolved.

---

# 26. Escalation Timeout

Where an escalation remains unresolved beyond an appropriate period:

```text
TIMEOUT / STALE ESCALATION
```

shall trigger reassessment.

Possible actions:

```text
FOLLOW-UP
RE-ESCALATE
INTERIM CONTROL
RISK ACCEPTANCE
DECISION
CLOSE
```

---

# 27. Interim Control

Where an unresolved issue creates material exposure, an interim control may be established.

It shall identify:

```text
Risk
Scope
Control
Owner
Duration
Authority
Review Trigger
```

An interim control shall not silently become the permanent baseline.

---

# 28. Exception Expiry

When an exception reaches its expiry or review trigger:

```text
EXPIRY / REVIEW
↓
ASSESS
↓
CLOSE
RENEW WITH AUTHORIZATION
REPLACE
ESCALATE
```

Automatic renewal is prohibited unless explicitly defined by the applicable governance policy.

---

# 29. Repeated Exceptions

Repeated exceptions shall be assessed for systemic causes:

```text
FIRST EXCEPTION
↓
REPEATED EXCEPTION
↓
PATTERN
↓
SYSTEMIC CONTROL GAP
↓
IMPROVEMENT
```

Repeated exceptions may indicate that the underlying baseline requires review.

---

# 30. Exception Debt

Exception debt may arise where:

```text
Multiple Active Exceptions
Long-Running Exceptions
Repeated Renewals
Overlapping Exceptions
Unresolved Conditions
Expired Exceptions
```

Exception debt shall be monitored where material.

---

# 31. Conflict Resolution

Resolution may include:

```text
RECONCILIATION
PRIORITIZATION
AUTHORITY DECISION
BASELINE CHANGE
RISK ACCEPTANCE
EXCEPTION
REASSIGNMENT
SCOPE CHANGE
REQUIREMENT CHANGE
```

The selected resolution shall be recorded.

---

# 32. Unresolved Conflict

If no resolution is available:

```text
UNRESOLVED
```

shall remain visible.

The record shall contain:

```text
Known Facts
Unknowns
Risks
Current Controls
Owner
Next Review Trigger
Escalation Status
```

---

# 33. Conflict Closure

A conflict may be closed when:

```text
Resolution Defined
AND
Required Authority Confirmed
AND
Required Actions Completed
AND
Conditions Captured
AND
Evidence Captured
AND
Residual Risk Assessed
```

---

# 34. Exception Closure

An exception may be closed when:

```text
Deviation Ends
OR
Requirement Is Formally Changed
OR
Exception Is Replaced
AND
Required Evidence Exists
AND
Residual Risk Is Addressed
AND
Authority Accepts Closure
```

---

# 35. Escalation Closure

An escalation may be closed when:

```text
Decision Made
AND
Decision Recorded
AND
Authority Confirmed
AND
Conditions Recorded
AND
Required Actions Assigned
```

---

# 36. Conflict / Exception Evidence

Material conflict and exception records should retain:

```text
Source
Evidence
Decision
Authority
Conditions
Risk
Review
Closure
```

---

# 37. Governance Conflict Quality

The mechanism shall periodically assess:

```text
Detection
Classification
Routing
Decision Timeliness
Resolution Quality
Exception Discipline
Escalation Quality
Recurring Conflicts
Expired Exceptions
```

Possible state:

```text
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNVERIFIED
```

---

# 38. Escalation Quality

Assess:

```text
Correct Routing
Completeness
Timeliness
Authority
Decision Quality
Traceability
Follow-Through
```

---

# 39. Exception Quality

Assess:

```text
Clear Requirement
Clear Deviation
Materiality
Risk
Duration
Authority
Conditions
Compensating Controls
Review
Closure
```

---

# 40. Systemic Conflict Detection

A systemic conflict may be indicated where:

```text
Repeated Similar Conflicts
+
Shared Root Cause
```

or:

```text
Multiple Domains
+
Same Governance Weakness
```

or:

```text
Repeated Exceptions
+
Same Requirement
```

Such patterns shall be routed to STEADY-STATE-010 for learning and improvement where appropriate.

---

# 41. Relationship to STEADY-STATE-009

STEADY-STATE-009 assures governance effectiveness.

STEADY-STATE-014 provides a controlled operational mechanism for:

```text
Conflict
Exception
Escalation
Resolution
```

Findings from STEADY-STATE-014 may feed assurance.

---

# 42. Relationship to STEADY-STATE-010

Material recurring conflicts and exceptions may generate:

```text
LESSON
↓
IMPROVEMENT OPPORTUNITY
↓
ASSESSMENT
↓
CONTROLLED CHANGE
```

through STEADY-STATE-010.

---

# 43. Relationship to STEADY-STATE-011

Where resolution requires a baseline change:

```text
CONFLICT / EXCEPTION
↓
DECISION
↓
AUTHORIZED BASELINE CHANGE
↓
STEADY-STATE-011
```

The conflict record shall remain linked to the baseline change.

---

# 44. Relationship to STEADY-STATE-012

Conflict, exception and escalation records shall maintain:

```text
Record Identity
Evidence
Provenance
Status
Retention
Traceability
```

through STEADY-STATE-012.

---

# 45. Relationship to STEADY-STATE-013

Where resolution affects:

```text
Authority
Access
Role
Accountability
Segregation of Duties
```

the relevant controls of STEADY-STATE-013 shall apply.

---

# 46. Future Work Package Trigger

A dedicated work package may be considered where:

```text
Conflict / Exception / Escalation Gap Is Material
AND
Dedicated Scope Is Required
AND
Dedicated Deliverables Are Required
AND
Dedicated Completion Criteria Are Required
```

---

# 47. Future Phase Protection

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

# 48. N10 Protection

Mandatory rule:

```text
STEADY-STATE-014
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

# 49. N9 Protection

N9 remains:

```text
CLOSED WITH CONDITIONS
```

Conflict, exception or escalation activity does not automatically reopen N9.

---

# 50. N8 Protection

N8 remains:

```text
CLOSED WITH CONDITIONS
```

No automatic reopening is permitted.

---

# 51. Completion Criteria

STEADY-STATE-014 initial establishment is complete when:

```text
Conflict Definition Defined
AND
Exception Definition Defined
AND
Waiver Boundary Defined
AND
Temporary Deviation Defined
AND
Conflict Classification Defined
AND
Exception Classification Defined
AND
Materiality Defined
AND
Exception Assessment Defined
AND
Exception Decision States Defined
AND
Escalation Definition Defined
AND
Escalation Triggers Defined
AND
Escalation Levels Defined
AND
Escalation Record Defined
AND
Interim Control Defined
AND
Exception Expiry Defined
AND
Repeated Exception Control Defined
AND
Conflict Resolution Defined
AND
Unresolved Conflict Defined
AND
Closure Criteria Defined
```

Thereafter:

```text
STEADY-STATE-014
= CONTINUOUSLY ACTIVE
```

---

# 52. Current Program State

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

STEADY-STATE-004
= ACTIVE
  ROUTING, ASSESSMENT & DECISION PREPARATION CONTROL

STEADY-STATE-005
= ACTIVE
  DECISION & AUTHORIZATION CONTROL

STEADY-STATE-006
= ACTIVE
  ACTION, IMPLEMENTATION & CHANGE CONTROL

STEADY-STATE-007
= ACTIVE
  IMPLEMENTATION VALIDATION, EVIDENCE & OUTCOME CONTROL

STEADY-STATE-008
= ACTIVE
  OUTCOME, VALUE & BENEFITS REALIZATION CONTROL

STEADY-STATE-009
= ACTIVE
  CONTINUOUS ASSURANCE, EFFECTIVENESS & GOVERNANCE PERFORMANCE CONTROL

STEADY-STATE-010
= ACTIVE
  GOVERNANCE LEARNING, IMPROVEMENT & SYSTEM EVOLUTION CONTROL

STEADY-STATE-011
= ACTIVE
  GOVERNANCE BASELINE, CONFIGURATION & CHANGE INTEGRITY CONTROL

STEADY-STATE-012
= ACTIVE
  GOVERNANCE REPOSITORY, RECORD & EVIDENCE INTEGRITY CONTROL

STEADY-STATE-013
= ACTIVE
  GOVERNANCE ACCESS, ACCOUNTABILITY & SEGREGATION-OF-DUTIES CONTROL

STEADY-STATE-014
= ACTIVE
  GOVERNANCE CONFLICT, EXCEPTION & ESCALATION CONTROL

N10
= NOT DEFINED
= NOT AUTHORIZED
```

---

# 53. Next Controlled Work Package

The next controlled work package is:

```text
STEADY-STATE-015
Governance Continuity, Resilience & Recovery Control
```

STEADY-STATE-015 shall establish the controlled mechanism for maintaining governance continuity during disruption, loss of key personnel, unavailable systems, evidence loss, major incidents and other conditions that could impair normal governance operation.

---

# 54. Final STEADY-STATE-014 Statement

> **STEADY-STATE-014 establishes the controlled mechanism for governance conflicts, exceptions and escalations. It ensures that deviations from approved governance remain explicit, time-bounded where appropriate, risk-assessed, authorized and traceable. It prevents escalation from being confused with decision, exception approval from being confused with requirement removal, and unresolved issues from disappearing into operational practice. Repeated conflicts and exceptions can feed the controlled learning and improvement mechanism. N8 and N9 remain CLOSED WITH CONDITIONS, while N10 remains NOT DEFINED and NOT AUTHORIZED.**

---

# 55. Document Control

**Document:** MFM Post-Steady-State Governance — Governance Conflict, Exception & Escalation Control  
**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-014-Governance-Conflict-Exception-and-Escalation-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — GOVERNANCE CONFLICT, EXCEPTION & ESCALATION CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-013 — Governance Access, Accountability & Segregation-of-Duties Control  
**Next Controlled Work Package:** STEADY-STATE-015 — Governance Continuity, Resilience & Recovery Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  
**Automatic N10 Authorization:** PROHIBITED  
**Automatic N9 Reopening:** PROHIBITED  
**Automatic N8 Reopening:** PROHIBITED  
