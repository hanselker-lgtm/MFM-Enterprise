# MFM Post-Steady-State Governance

## STEADY-STATE-013 — Governance Access, Accountability & Segregation-of-Duties Control

**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-013-Governance-Access-Accountability-and-Segregation-of-Duties-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — GOVERNANCE ACCESS, ACCOUNTABILITY & SEGREGATION-OF-DUTIES CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-012 — Governance Repository, Record & Evidence Integrity Control  
**Next Controlled Work Package:** STEADY-STATE-014 — Governance Conflict, Exception & Escalation Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  

---

# 1. Purpose

STEADY-STATE-013 establishes the controlled mechanism for determining who may access, create, modify, review, approve, authorize, validate and administer governance information, records and decisions.

The control establishes accountability and appropriate segregation of duties so that governance authority is not silently concentrated in one uncontrolled role.

The operating sequence is:

```text
ROLE
↓
RESPONSIBILITY
↓
AUTHORITY
↓
ACCESS
↓
ACTION
↓
ACCOUNTABILITY
↓
REVIEW
```

---

# 2. Core Principle

Access is not authority.

Authority is not accountability.

The following distinctions are mandatory:

```text
ACCESS
≠
AUTHORITY

AUTHORITY
≠
APPROVAL

APPROVAL
≠
AUTHORIZATION

AUTHORIZATION
≠
IMPLEMENTATION

IMPLEMENTATION
≠
VALIDATION

VALIDATION
≠
ASSURANCE
```

---

# 3. Scope

STEADY-STATE-013 applies to governance activities including:

```text
Signal Intake
Assessment
Recommendation
Decision
Authorization
Action
Implementation
Change
Validation
Outcome
Benefit
Value
Assurance
Record Administration
Baseline Management
Evidence Management
Exception Management
Escalation
```

---

# 4. Governance Roles

Where applicable, governance roles may include:

```text
Signal Owner
Assessment Owner
Recommendation Owner
Decision Authority
Authorization Authority
Implementation Owner
Change Authority
Validation Owner
Outcome Owner
Benefit Owner
Value Owner
Assurance Owner
Record Custodian
Baseline Owner
Evidence Owner
Escalation Authority
```

Roles may be combined where appropriate, provided that conflicts and control risks are assessed.

---

# 5. Responsibility vs Authority

Responsibility means:

```text
ACCOUNTABLE FOR PERFORMING / MANAGING
```

Authority means:

```text
AUTHORIZED TO DECIDE / APPROVE / AUTHORIZE
```

A role may have responsibility without having decision authority.

---

# 6. Accountability

Each material governance action should identify:

```text
Who Performed It?
Who Is Accountable?
Who Authorized It?
Who Validated It?
Who Reviewed It?
```

Where ownership cannot be established:

```text
OWNER = UNVERIFIED
```

shall remain visible.

---

# 7. Access Classes

Access may be classified as:

```text
READ
CREATE
MODIFY
APPROVE
AUTHORIZE
VALIDATE
ADMINISTER
AUDIT / ASSURE
```

Access shall be granted according to legitimate governance need.

---

# 8. Least-Privilege Principle

Access shall be limited to what is necessary for the role.

```text
NEED
+
ROLE
+
AUTHORITY
↓
APPROPRIATE ACCESS
```

Access shall not be granted solely because a person is senior or technically capable.

---

# 9. Access vs Governance Authority

A user may be able to technically access a record without being authorized to:

```text
Approve
Authorize
Change
Validate
Close
Override
```

Technical capability shall not be interpreted as governance authority.

---

# 10. Segregation of Duties

Where material control risk exists, separate:

```text
PROPOSE
vs
APPROVE

APPROVE
vs
AUTHORIZE

AUTHORIZE
vs
IMPLEMENT

IMPLEMENT
vs
VALIDATE

VALIDATE
vs
ASSURE

CREATE RECORD
vs
INDEPENDENTLY REVIEW RECORD
```

The exact separation shall be proportionate to risk and materiality.

---

# 11. Conflicting Duties

Potential conflicts may occur where one role controls too many stages of:

```text
Decision
Authorization
Implementation
Validation
Assurance
```

Such conflicts shall be assessed rather than automatically prohibited in every case.

---

# 12. Compensating Controls

Where separation is not practical, compensating controls may include:

```text
Independent Review
Secondary Approval
Post-Implementation Review
Periodic Assurance
Evidence Review
Automated Logging
Restricted Administration
Management Oversight
```

The compensating control shall be documented.

---

# 13. Delegated Authority

Delegated authority shall identify:

```text
Delegator
Delegate
Scope
Limit
Conditions
Start
End / Review Trigger
Evidence
```

Delegation does not permanently transfer the underlying governance accountability unless explicitly defined.

---

# 14. Delegation Boundary

The following distinction is mandatory:

```text
DELEGATION
≠
UNCONTROLLED AUTHORITY TRANSFER
```

Delegated authority shall remain traceable.

---

# 15. Temporary Authority

Temporary authority may be established for:

```text
Absence
Emergency
Project Period
Transition
Specialist Review
Critical Event
```

Temporary authority shall have:

```text
Scope
Duration
Conditions
Owner
Review Trigger
```

---

# 16. Emergency Authority

Emergency authority may be used only where the governance framework permits it.

Emergency use shall record:

```text
Reason
Urgency
Authority
Scope
Risk
Action
Evidence
Post-Event Review
```

Emergency authority shall not become a permanent bypass.

---

# 17. Access Lifecycle

Access should follow:

```text
REQUEST
↓
ASSESS
↓
APPROVE
↓
GRANT
↓
REVIEW
↓
MODIFY / REVOKE
```

---

# 18. Access Request

An access request should identify:

```text
Requester
Role
Requested Access
Governance Scope
Business / Governance Need
Duration
Approver
```

---

# 19. Access Approval

Approval should confirm:

```text
Need Exists
Role Is Appropriate
Authority Is Appropriate
Conflict Is Assessed
Scope Is Defined
Duration Is Defined Where Applicable
```

---

# 20. Access Review

Access should be reviewed periodically or upon trigger:

```text
Role Change
Responsibility Change
Authority Change
Organizational Change
Security Event
Governance Change
End of Temporary Assignment
```

---

# 21. Access Revocation

Access shall be revoked or adjusted where:

```text
Role Ends
Responsibility Ends
Authority Ends
Assignment Ends
Need Ends
Conflict Emerges
Governance Baseline Changes
```

---

# 22. Privileged Administration

Administrative access shall receive heightened control where it can alter:

```text
Governance Records
Baselines
Configuration
Authority
Access
Evidence
Audit Logs
```

Privileged actions should be attributable to an identifiable individual or controlled service identity.

---

# 23. Administrative Override

An administrative override shall record:

```text
Override ID
Person / Identity
Reason
Scope
Time
Authority
Action
Evidence
Review
```

Overrides shall not silently alter governance history.

---

# 24. Decision Accountability

Each material decision should preserve:

```text
Decision Maker
Authority
Date
Decision
Rationale
Evidence
Conditions
```

A system operator who records a decision is not necessarily the decision authority.

---

# 25. Authorization Accountability

Each material authorization should preserve:

```text
Authorization Authority
Scope
Conditions
Date
Evidence
Status
```

Technical implementation of authorization does not replace the authoritative authorization record.

---

# 26. Implementation Accountability

Each material implementation should identify:

```text
Implementation Owner
Implementation Authority
Scope
Evidence
Status
Validation Owner
```

---

# 27. Validation Independence

Where validation is material, validation should be sufficiently independent from implementation to provide credible assurance.

Possible independence:

```text
FULL
PARTIAL
LIMITED
UNVERIFIED
```

---

# 28. Assurance Independence

Material assurance should be sufficiently independent from the activity under review.

Independence shall be assessed proportionately to:

```text
Materiality
Risk
Complexity
Governance Importance
```

---

# 29. Record Custodianship

The record custodian is responsible for maintaining:

```text
Record Integrity
Availability
Version
Status
Retention
Retrieval
Access Control
```

Custodianship does not confer authority over the underlying governance decision.

---

# 30. Baseline Ownership

The baseline owner maintains:

```text
Baseline Identity
Version
Effective State
Change History
Authority
Reconciliation
```

Baseline ownership does not automatically confer authority to change the baseline.

---

# 31. Evidence Ownership

The evidence owner maintains:

```text
Source
Provenance
Integrity
Availability
Validation Status
Retention
```

Evidence ownership does not automatically determine governance conclusions.

---

# 32. Role Conflict Assessment

Potential conflicts shall be assessed using:

```text
Materiality
Risk
Authority
Access
Control Dependency
Independence Requirement
Compensating Controls
```

Possible result:

```text
ACCEPTABLE
ACCEPTABLE WITH CONDITIONS
REQUIRES SEPARATION
UNVERIFIED
```

---

# 33. Accountability Gap

Where no accountable owner can be identified:

```text
ACCOUNTABILITY GAP
```

shall be recorded and routed for resolution.

---

# 34. Authority Gap

Where no valid authority can be identified:

```text
AUTHORITY GAP
```

shall be recorded.

No unauthorized decision shall be created to fill the gap.

---

# 35. Access Gap

Where required governance access is unavailable:

```text
ACCESS GAP
```

shall be assessed for operational and governance impact.

Access gaps shall not automatically justify broad unrestricted access.

---

# 36. Access Conflict

Where access creates a material conflict:

```text
CONFLICT IDENTIFIED
↓
ASSESS
↓
RESTRICT / SEPARATE / COMPENSATE
↓
APPROVE
↓
REVIEW
```

---

# 37. Role Change

When a role changes:

```text
ROLE CHANGE
↓
RESPONSIBILITY REVIEW
↓
AUTHORITY REVIEW
↓
ACCESS REVIEW
↓
CONFLICT REVIEW
↓
UPDATE
```

---

# 38. Organizational Change

Material organizational change shall trigger review of:

```text
Roles
Responsibilities
Authority
Delegations
Access
Segregation of Duties
Accountability
Escalation
```

---

# 39. Access / Authority Register

| Field | Required |
|---|---|
| Identity / Role | YES |
| Responsibility | YES |
| Authority | YES WHERE APPLICABLE |
| Access Class | YES |
| Scope | YES |
| Delegation | WHERE APPLICABLE |
| Conditions | WHERE APPLICABLE |
| Start / End | WHERE APPLICABLE |
| Review Date | YES |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL GOVERNANCE ACCESS RECORDS
```

---

# 40. Role & Responsibility Register

| Field | Required |
|---|---|
| Role ID | YES |
| Role Name | YES |
| Responsibility | YES |
| Authority | YES WHERE APPLICABLE |
| Accountability | YES |
| Segregation Requirement | WHERE APPLICABLE |
| Owner | YES |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL GOVERNANCE ROLE RECORDS
```

---

# 41. Segregation-of-Duties Register

| Field | Required |
|---|---|
| SoD ID | YES |
| Activity A | YES |
| Activity B | YES |
| Conflict | YES |
| Materiality | YES |
| Risk | YES |
| Required Separation | YES WHERE APPLICABLE |
| Compensating Control | WHERE APPLICABLE |
| Authority | WHERE APPLICABLE |
| Status | YES |

Initial state:

```text
READY FOR ACTUAL SOD RECORDS
```

---

# 42. Access Review Quality

The access-control mechanism shall periodically assess:

```text
Least Privilege
Role Accuracy
Authority Accuracy
Access Currency
Segregation of Duties
Delegation Integrity
Privileged Access
Review Completion
```

Possible state:

```text
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNVERIFIED
```

---

# 43. Accountability Quality

Accountability governance shall assess:

```text
Ownership Clarity
Decision Attribution
Authorization Attribution
Implementation Ownership
Validation Independence
Assurance Independence
Record Custodianship
Evidence Ownership
```

---

# 44. SoD Quality

Segregation-of-duties governance shall assess:

```text
Conflict Identification
Risk Assessment
Separation
Compensating Controls
Review
Exception Handling
```

---

# 45. Access / Authority Incident

A material incident may include:

```text
Unauthorized Access
Unauthorized Decision
Unauthorized Authorization
Unauthorized Baseline Change
Unauthorized Evidence Modification
Unattributed Action
Privilege Misuse
SoD Failure
```

The incident shall be routed through the appropriate governance and assurance mechanisms.

---

# 46. Accountability Traceability

The complete accountability chain should remain:

```text
ROLE
↓
RESPONSIBILITY
↓
AUTHORITY
↓
ACCESS
↓
ACTION
↓
RECORD
↓
REVIEW
↓
ASSURANCE
```

---

# 47. Future Work Package Trigger

A dedicated work package may be considered where:

```text
Access / Accountability Gap Is Material
AND
Dedicated Scope Is Required
AND
Dedicated Deliverables Are Required
AND
Dedicated Completion Criteria Are Required
```

---

# 48. Future Phase Protection

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

# 49. N10 Protection

Mandatory rule:

```text
STEADY-STATE-013
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

# 50. N9 Protection

N9 remains:

```text
CLOSED WITH CONDITIONS
```

Access or accountability changes do not automatically reopen N9.

---

# 51. N8 Protection

N8 remains:

```text
CLOSED WITH CONDITIONS
```

No automatic reopening is permitted.

---

# 52. Completion Criteria

STEADY-STATE-013 initial establishment is complete when:

```text
Governance Roles Defined
AND
Responsibility / Authority Distinction Defined
AND
Accountability Defined
AND
Access Classes Defined
AND
Least Privilege Defined
AND
Segregation of Duties Defined
AND
Compensating Controls Defined
AND
Delegated Authority Defined
AND
Temporary / Emergency Authority Defined
AND
Access Lifecycle Defined
AND
Privileged Administration Defined
AND
Decision Accountability Defined
AND
Validation Independence Defined
AND
Assurance Independence Defined
AND
Role Conflict Assessment Defined
AND
Access / Authority Registers Defined
```

Thereafter:

```text
STEADY-STATE-013
= CONTINUOUSLY ACTIVE
```

---

# 53. Current Program State

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

N10
= NOT DEFINED
= NOT AUTHORIZED
```

---

# 54. Next Controlled Work Package

The next controlled work package is:

```text
STEADY-STATE-014
Governance Conflict, Exception & Escalation Control
```

STEADY-STATE-014 shall establish the controlled mechanism for identifying, classifying, resolving, authorizing, tracking and escalating governance conflicts, exceptions and unresolved authority or control issues.

---

# 55. Final STEADY-STATE-013 Statement

> **STEADY-STATE-013 establishes the controlled access, accountability and segregation-of-duties mechanism for steady-state governance. It distinguishes technical access from governance authority, approval from authorization, responsibility from accountability, and implementation from validation and assurance. It controls delegated and temporary authority, privileged administration, role conflicts and access lifecycle, while ensuring that material governance actions remain attributable to identifiable roles and authorities. N8 and N9 remain CLOSED WITH CONDITIONS, while N10 remains NOT DEFINED and NOT AUTHORIZED.**

---

# 56. Document Control

**Document:** MFM Post-Steady-State Governance — Governance Access, Accountability & Segregation-of-Duties Control  
**Control ID:** MFM-Post-Steady-State-Governance-STEADY-STATE-013-Governance-Access-Accountability-and-Segregation-of-Duties-Control-001  
**Version:** 1.0  
**Status:** ACTIVE — GOVERNANCE ACCESS, ACCOUNTABILITY & SEGREGATION-OF-DUTIES CONTROL  
**Date:** 18 August 2026  
**State:** STEADY-STATE CONTINUOUS GOVERNANCE  
**Predecessor:** STEADY-STATE-012 — Governance Repository, Record & Evidence Integrity Control  
**Next Controlled Work Package:** STEADY-STATE-014 — Governance Conflict, Exception & Escalation Control  
**N8 State:** CLOSED WITH CONDITIONS  
**N9 State:** CLOSED WITH CONDITIONS  
**N10 State:** NOT DEFINED / NOT AUTHORIZED  
**Automatic N10 Authorization:** PROHIBITED  
**Automatic N9 Reopening:** PROHIBITED  
**Automatic N8 Reopening:** PROHIBITED  
