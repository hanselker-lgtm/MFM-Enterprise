# MFM Post-Steady-State Governance

## STEADY-STATE-005 — Governance Decision & Authorization Control

**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-005-Governance-Decision-and-Authorization-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — DECISION & AUTHORIZATION CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-004 — Governance Routing, Assessment & Decision Preparation  
**Next Controlled Work Package:** STEADY-STATE-006 — Governance Action, Implementation & Change Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  

---

# 1. Purpose

STEADY-STATE-005 establishes the formal control boundary between decision preparation and authorized governance decisions.

The operating sequence is:

```text
DECISION PACKAGE
↓
DECISION READINESS
↓
AUTHORITY CONFIRMATION
↓
DECISION
↓
CONDITIONS
↓
AUTHORIZATION IF REQUIRED
↓
ACTION ROUTING
```

The control preserves the distinction between a recommendation, a decision and an authorization.

---

# 2. Core Principle

The following distinctions are mandatory:

```text
Recommendation
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

Implementation
≠
Validation

Validation
≠
Outcome

Outcome
≠
Value
```

No step may be silently treated as another.

---

# 3. Scope

STEADY-STATE-005 receives decision packages prepared through:

```text
STEADY-STATE-004
```

and routes them through the applicable governance authority.

Relevant domains include:

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

---

# 4. Decision Intake

Each decision package shall retain:

```text
Decision Package ID
Signal ID
Decision ID
Context
Assessment
Evidence
Options
Recommendation
Risks
Dependencies
Conditions
Required Authority
Decision Readiness
Status
```

---

# 5. Decision Readiness Gate

Before a decision is presented, confirm:

```text
Decision Question Clear
AND
Evidence Reviewed
AND
Assumptions Visible
AND
Risks Assessed
AND
Dependencies Assessed
AND
Options Assessed Where Applicable
AND
Recommendation Clear Where Applicable
AND
Authority Identified
AND
Conditions Identified
```

Possible result:

```text
READY
READY WITH CONDITIONS
NOT READY
UNVERIFIED
```

---

# 6. Authority Confirmation

Authority shall be confirmed before a binding decision is treated as valid.

Identify:

```text
Decision Authority
Authorization Authority
Funding Authority
Implementation Authority
Review Authority
Escalation Authority
```

The distinction remains:

```text
Decision Authority
≠
Authorization Authority
≠
Funding Authority
```

Where authority cannot be established:

```text
AUTHORITY = UNVERIFIED
```

The package shall not be represented as approved.

---

# 7. Decision Types

Decisions may include:

```text
STRATEGIC DECISION
ARCHITECTURE DECISION
CAPABILITY DECISION
PORTFOLIO DECISION
INVESTMENT DECISION
RISK DECISION
DEPENDENCY DECISION
CHANGE DECISION
OUTCOME DECISION
VALUE DECISION
GOVERNANCE DECISION
EXCEPTION DECISION
```

The applicable governance authority determines the authoritative decision record.

---

# 8. Decision Outcomes

Possible decision outcomes:

```text
APPROVED
APPROVED WITH CONDITIONS
REJECTED
DEFERRED
RETURNED FOR FURTHER ASSESSMENT
NOT AUTHORIZED
UNVERIFIED
```

A deferred or rejected decision is still a valid governance outcome and shall be recorded.

---

# 9. Decision Record

A material decision shall record:

```text
Decision ID
Decision Date
Decision Question
Decision
Authority
Evidence
Rationale
Conditions
Risks
Dependencies
Review Trigger
Review Date
Status
```

---

# 10. Decision Rationale

The rationale should explain:

```text
Why This Decision?
Why Now?
What Evidence Supports It?
What Alternatives Were Considered?
What Risks Remain?
What Dependencies Remain?
What Conditions Apply?
```

The rationale must not claim evidence that does not exist.

---

# 11. Conditions

Where a decision is conditional, each condition shall identify:

```text
Condition ID
Requirement
Owner
Evidence Required
Due / Review Trigger
Closure Criteria
Status
```

Possible condition states:

```text
ACTIVE
UNDER REVIEW
SATISFIED
TRANSFERRED
SUPERSEDED
CLOSED
UNVERIFIED
```

A conditional approval is not equivalent to unconditional approval.

---

# 12. Authorization Boundary

Where authorization is required, the authorization shall be separately recorded:

```text
Authorization ID
Decision ID
Authority
Scope
Limitations
Conditions
Effective State
Evidence
```

The distinction remains:

```text
Decision
→ establishes what is decided

Authorization
→ permits the authorized action within defined boundaries
```

---

# 13. Funding Boundary

Funding requires its own authority where applicable.

```text
Decision
≠
Funding Approval
```

A decision may authorize direction without authorizing funding.

Funding approval shall therefore retain:

```text
Funding Authority
Funding Scope
Amount / Limit Where Applicable
Conditions
Evidence
```

---

# 14. Implementation Boundary

Implementation authority shall be established separately where required.

```text
Authorization
≠
Implementation Completion
```

Implementation requires:

```text
Implementation Owner
Scope
Dependencies
Risks
Controls
Evidence
Validation
```

---

# 15. Decision Exceptions

Where an exception is requested:

```text
Exception ID
Baseline Requirement
Requested Deviation
Reason
Impact
Risk
Duration
Owner
Authority
Compensating Control
Review Trigger
```

An exception shall not silently modify the baseline.

---

# 16. Escalation

Escalation may be required for:

```text
Authority Conflict
Critical Risk
Critical Dependency
Material Strategic Impact
Material Architecture Impact
Material Outcome Failure
Material Value Variance
Material Evidence Gap
Cross-Domain Conflict
Exception Beyond Delegated Authority
```

Escalation shall identify the receiving authority.

---

# 17. Decision Deferral

A decision may be deferred where:

```text
Evidence Insufficient
Authority Unclear
Material Dependency Unresolved
Risk Requires Further Assessment
Outcome Evidence Incomplete
Value Case Uncertain
```

A deferred decision shall identify:

```text
Reason
Owner
Required Evidence
Review Trigger
Review Authority
```

---

# 18. Decision Rejection

Where a decision is rejected, record:

```text
Decision ID
Rejected Option / Proposal
Authority
Rationale
Evidence
Conditions
Possible Reconsideration Trigger
```

Rejection does not necessarily close the underlying signal or issue.

---

# 19. Decision Reconsideration

A decision may be reconsidered where:

```text
Material New Evidence
Material Change
New Risk
New Dependency
Outcome Failure
Value Variance
Regulatory Change
Authority Change
```

Reconsideration requires a new controlled assessment.

---

# 20. Decision Traceability

The complete chain should remain:

```text
SOURCE
↓
SIGNAL
↓
INTAKE
↓
MATERIALITY
↓
ROUTING
↓
ASSESSMENT
↓
OPTIONS
↓
RECOMMENDATION
↓
DECISION
↓
AUTHORIZATION
↓
ACTION
↓
VALIDATION
↓
OUTCOME
↓
VALUE
```

STEADY-STATE-005 establishes the decision and authorization portion of this chain.

---

# 21. Evidence Boundary

A decision record supports:

```text
Decision Existence
Decision Authority
Decision Rationale
Decision Conditions
```

An authorization record supports:

```text
Authorization Existence
Authorization Scope
Authorization Authority
Authorization Conditions
```

Neither automatically proves:

```text
Implementation Completed
Outcome Achieved
Value Realized
```

Those require subsequent evidence.

---

# 22. Decision Register

| Field | Required |
|---|---|
| Decision ID | YES |
| Decision Package ID | YES |
| Decision Date | YES |
| Decision | YES |
| Authority | YES |
| Evidence | YES WHERE AVAILABLE |
| Rationale | YES |
| Conditions | WHERE APPLICABLE |
| Authorization | WHERE REQUIRED |
| Review Trigger | WHERE APPLICABLE |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL GOVERNANCE DECISIONS
```

No fabricated decisions shall be entered.

---

# 23. Authorization Register

| Field | Required |
|---|---|
| Authorization ID | YES |
| Decision ID | YES |
| Authority | YES |
| Scope | YES |
| Conditions | WHERE APPLICABLE |
| Limitations | WHERE APPLICABLE |
| Effective State | YES |
| Evidence | YES |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL AUTHORIZATIONS
```

---

# 24. Decision Quality

Decision governance shall periodically assess:

```text
Decision Clarity
Authority Accuracy
Evidence Quality
Rationale Quality
Condition Quality
Traceability
Outcome Follow-Through
```

Possible state:

```text
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNVERIFIED
```

---

# 25. Authorization Quality

Authorization governance shall assess:

```text
Authority Correctness
Scope Clarity
Condition Clarity
Limitation Clarity
Traceability
Evidence
```

Possible state:

```text
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNVERIFIED
```

---

# 26. Decision Conflict

Where authorities or governance domains disagree:

```text
Conflict Identified
↓
Evidence Reviewed
↓
Authority Mapped
↓
Conflict Escalated
↓
Authorized Resolution
↓
Decision Recorded
```

The disagreement shall remain visible in the record.

---

# 27. Unauthorized Action

Where action occurs without required authorization:

```text
Unauthorized Action Detected
↓
Record Event
↓
Assess Impact
↓
Assess Risk
↓
Identify Authority
↓
Determine Corrective Action
↓
Validate
```

The event shall not be retroactively represented as authorized without a valid governance decision.

---

# 28. Conditional Authorization

Where authorization is conditional:

```text
Authorization
+
Conditions
```

shall be treated as a combined control state.

The authorization shall not be treated as fully unrestricted.

---

# 29. Review Triggers

A decision or authorization may require review on:

```text
Time Trigger
Material Change
Risk Trigger
Dependency Trigger
Outcome Trigger
Value Trigger
Condition Trigger
Regulatory Trigger
Exception Trigger
```

---

# 30. Governance Record Integrity

Decision and authorization records shall preserve:

```text
Who
What
When
Why
Authority
Evidence
Conditions
Scope
Status
Review Trigger
```

Historical decisions shall not be silently overwritten.

---

# 31. Future Work Package Trigger

A dedicated work package may be considered where:

```text
Decision / Authorization Control Gap Is Material
AND
Dedicated Scope Is Required
AND
Dedicated Deliverables Are Required
AND
Dedicated Completion Criteria Are Required
```

---

# 32. Future Phase Protection

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

# 33. N10 Protection

Mandatory rule:

```text
STEADY-STATE-005
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

# 34. N9 Protection

N9 remains:

```text
CLOSED WITH CONDITIONS
```

A new decision does not automatically reopen N9.

---

# 35. N8 Protection

N8 remains:

```text
CLOSED WITH CONDITIONS
```

No automatic reopening is permitted.

---

# 36. Completion Criteria

STEADY-STATE-005 initial establishment is complete when:

```text
Decision Intake Defined
AND
Decision Readiness Gate Defined
AND
Authority Confirmation Defined
AND
Decision Types Defined
AND
Decision Outcomes Defined
AND
Decision Record Defined
AND
Condition Control Defined
AND
Authorization Boundary Defined
AND
Funding Boundary Defined
AND
Implementation Boundary Defined
AND
Exception Handling Defined
AND
Escalation Defined
AND
Decision Traceability Defined
AND
Decision / Authorization Quality Review Defined
```

Thereafter:

```text
STEADY-STATE-005
= CONTINUOUSLY ACTIVE
```

---

# 37. Current Program State

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

N10
= NOT DEFINED
= NOT AUTHORIZED
```

---

# 38. Next Controlled Work Package

The next controlled work package is:

```text
STEADY-STATE-006
Governance Action, Implementation & Change Control
```

STEADY-STATE-006 shall establish the controlled mechanism by which authorized decisions become governed actions, implementation activities and controlled changes, including implementation ownership, scope, dependencies, risk, evidence and validation.

---

# 39. Final STEADY-STATE-005 Statement

> **STEADY-STATE-005 establishes the formal decision and authorization boundary within steady-state governance. It ensures that decisions are made by the appropriate authority, that authorization is separately controlled where required, and that conditions, scope, limitations, funding authority and implementation authority are explicitly distinguished. A recommendation is not a decision, a decision is not automatically an authorization, and authorization does not prove implementation, outcome or value. N8 and N9 remain CLOSED WITH CONDITIONS, while N10 remains NOT DEFINED and NOT AUTHORIZED.**

---

# 40. Document Control

**Document:** MFM Post-Steady-State Governance — Governance Decision & Authorization Control  
**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-005-Governance-Decision-and-Authorization-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — DECISION & AUTHORIZATION CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-004 — Governance Routing, Assessment & Decision Preparation  
**Next Controlled Work Package:** STEADY-STATE-006 — Governance Action, Implementation & Change Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  
**Automatic N10 Authorization:** PROHIBITED  
**Automatic N9 Reopening:** PROHIBITED  
**Automatic N8 Reopening:** PROHIBITED  
