# EA-IMETA-PC-RG-426

## EXCEPTION, DEVIATION & TEMPORARY-STATE CONTROL MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-426 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Exception, Deviation & Temporary-State Control Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-425 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how legitimate deviations, temporary states and controlled exceptions are authorised, bounded, monitored, reviewed and retired without becoming hidden permanent drift |
| Architectural Boundary | Deviation → Classification → Risk → Authority → Exception → Temporary State → Monitoring → Expiry / Renewal / Remediation → Closure |

---

# 2. Purpose

EA-IMETA-PC-RG-426 defines the governance architecture for conditions that intentionally differ from the approved baseline, control requirement, policy, rule, configuration or expected state.

RG-425 establishes continuous monitoring and reconciliation.

RG-426 establishes **how a known deviation may be governed without being confused with either compliance or uncontrolled drift**.

The architecture SHALL distinguish:

```text
DEVIATION
= A DIFFERENCE BETWEEN EXPECTED AND ACTUAL CONDITION

EXCEPTION
= AN AUTHORISED DEVIATION FROM A DEFINED REQUIREMENT OR CONTROL

TEMPORARY STATE
= AN INTENTIONALLY LIMITED CONDITION WITH A DEFINED LIFETIME

WAIVER
= FORMAL PERMISSION NOT TO APPLY A REQUIREMENT UNDER DEFINED CONDITIONS

TOLERANCE
= A GOVERNED ACCEPTABLE RANGE WITHIN WHICH VARIATION IS PERMITTED

COMPENSATING CONTROL
= AN ALTERNATIVE CONTROL USED TO REDUCE RISK WHEN THE PRIMARY CONTROL IS NOT AVAILABLE OR SUFFICIENT

DRIFT
= AN UNGOVERNED OR UNEXPLAINED DIFFERENCE FROM THE APPROVED STATE
```

---

# 3. Core Principle

> **An exception makes a deviation visible and governed; it does not make the underlying requirement disappear.**

The governing chain is:

```text
DEVIATION
      ↓
DETECTION
      ↓
CLASSIFICATION
      ↓
MATERIALITY / RISK
      ↓
AUTHORITY
      ↓
EXCEPTION DECISION
      ↓
BOUNDARY + EXPIRY
      ↓
CONTINUOUS MONITORING
      ↓
REVIEW
      ↓
REMEDIATE / RENEW / RETIRE
```

---

# 4. Exception Object

Every material exception SHALL be represented as a controlled object.

Minimum attributes:

```text
Exception ID
Subject
Requirement
Deviation
Reason
Scope
Risk
Materiality
Authority
Compensating Controls
Start Time
Expiry Time
Review Date
Owner
Conditions
Monitoring
Evidence
Status
Decision
Closure
```

---

# 5. Deviation Object

A deviation SHALL identify:

```text
Expected State
Actual State
Difference
Source
Time
Scope
Reason
Known / Unknown Status
Impact
```

A deviation does not automatically constitute an exception.

---

# 6. Exception Lifecycle

```text
IDENTIFIED
   ↓
REQUESTED
   ↓
ASSESSED
   ↓
AUTHORISED
   ↓
ACTIVE
   ↓
MONITORED
   ↓
REVIEWED
   ↓
REMEDIATED / EXPIRED / RENEWED
   ↓
CLOSED
```

Alternative states:

```text
REJECTED
SUSPENDED
REVOKED
ESCALATED
CANCELLED
OVERDUE
```

---

# 7. Temporary-State Lifecycle

```text
PLANNED
   ↓
AUTHORISED
   ↓
ACTIVATED
   ↓
OBSERVED
   ↓
REVIEWED
   ↓
RESTORED
```

Alternative:

```text
EXTENDED
REPLACED
ESCALATED
EXPIRED
```

---

# 8. Exception vs Deviation

The system SHALL distinguish:

```text
DEVIATION
= FACTUAL DIFFERENCE

EXCEPTION
= GOVERNED AUTHORISATION OF THAT DIFFERENCE
```

An observed deviation without an approved exception SHALL remain a deviation.

---

# 9. Exception vs Compliance

An approved exception does not mean:

```text
REQUIREMENT = SATISFIED
```

Instead:

```text
REQUIREMENT
   ↓
EXCEPTION
   ↓
AUTHORISED NON-CONFORMANCE / DEVIATION
```

The distinction SHALL remain visible.

---

# 10. Exception vs Risk Acceptance

Risk acceptance may be one component of an exception decision.

It SHALL not automatically authorise every technical or policy deviation.

---

# 11. Exception vs Waiver

A waiver removes or suspends application of a specified requirement within defined authority.

A waiver SHALL have:

```text
Requirement
Scope
Authority
Duration
Conditions
```

---

# 12. Exception vs Tolerance

Tolerance defines an allowed operating range.

Example:

```text
TARGET = 100
TOLERANCE = 95–105
```

A value of 103 may not require an exception.

A value of 110 may require one.

---

# 13. Exception vs Compensating Control

A compensating control may reduce risk while a primary control is unavailable.

```text
PRIMARY CONTROL
      ↓
UNAVAILABLE
      ↓
COMPENSATING CONTROL
      ↓
EXCEPTION / TEMPORARY STATE
```

---

# 14. Exception Classification

Exceptions MAY be classified as:

```text
TECHNICAL
OPERATIONAL
SECURITY
COMPLIANCE
DATA
PROCESS
CONTROL
AUTHORITY
EVIDENCE
DEPENDENCY
CONFIGURATION
MODEL
TEMPORARY
EMERGENCY
```

---

# 15. Exception Materiality

Materiality SHALL consider:

```text
Risk
Scope
Duration
Criticality
Security
Compliance
Reliance
Decision Impact
Control Impact
Propagation Potential
```

---

# 16. Exception Risk

Risk assessment SHALL consider:

```text
Inherent Risk
Residual Risk
Likelihood
Impact
Exposure Duration
Compensating Controls
Uncertainty
```

---

# 17. Exception Authority

Authority SHALL be determined by:

```text
Requirement
Risk
Materiality
Scope
Duration
Environment
```

The exception requester SHALL not automatically be the approving authority.

---

# 18. Separation of Duties

For material exceptions:

```text
REQUESTER
   ≠
APPROVER
```

Where required:

```text
ASSESSOR
   ≠
APPROVER
```

---

# 19. Exception Request

A request SHALL state:

```text
What requirement is affected?
What is different?
Why is it different?
Why is it necessary?
What is the risk?
What controls compensate?
How long will it last?
How will it be monitored?
How will it be resolved?
```

---

# 20. Exception Preconditions

Before approval:

```text
Scope Defined
Risk Assessed
Authority Confirmed
Compensating Controls Identified
Expiry Defined
Monitoring Defined
Owner Assigned
```

---

# 21. Exception Scope

Scope SHALL define:

```text
Object
Environment
Population
Function
Geography where applicable
Time
Dependencies
```

Broad or ambiguous scope SHALL be rejected or refined.

---

# 22. Exception Conditions

Exceptions MAY contain mandatory conditions:

```text
Additional Monitoring
Restricted Access
Reduced Scope
Manual Review
Compensating Control
Enhanced Evidence
Shorter Review Cycle
```

---

# 23. Exception Boundaries

An exception SHALL define what it does NOT permit.

```text
EXCEPTION SCOPE
      ↓
ALLOWED DEVIATION
      ↓
BOUNDARY
      ↓
PROHIBITED DEVIATION
```

---

# 24. Exception Duration

Every temporary or time-bound exception SHALL have:

```text
Start
Expiry
Review Date
```

Permanent exceptions SHOULD be avoided unless explicitly supported by policy.

---

# 25. Exception Expiry

At expiry:

```text
RESTORE
REMEDIATE
RENEW
REASSESS
ESCALATE
```

The system SHALL not silently extend the exception.

---

# 26. Automatic Expiry

Where technically feasible, exceptions SHOULD automatically become inactive at expiry.

Automatic expiry SHALL not cause uncontrolled operational harm; recovery procedures SHALL be defined.

---

# 27. Exception Renewal

Renewal SHALL be a new governance decision.

It SHALL consider:

```text
Original Reason
Current Risk
Previous Duration
Monitoring Results
Remediation Progress
Changed Dependencies
Changed Requirements
```

---

# 28. Exception Age

Exception age SHALL be visible.

Long-lived exceptions SHALL receive enhanced scrutiny.

---

# 29. Exception Debt

Repeated or long-lived exceptions MAY constitute exception debt.

Exception debt SHALL be measured and risk-assessed.

---

# 30. Exception Stacking

Multiple exceptions affecting the same object SHALL be identified.

```text
EXCEPTION A
+
EXCEPTION B
+
EXCEPTION C
=
COMPOUND RISK
```

Individually acceptable exceptions may become materially risky in combination.

---

# 31. Exception Dependency

Exceptions MAY depend on:

```text
Control
System
Person
Vendor
Policy
Technology
Temporary Condition
```

Dependencies SHALL be traceable.

---

# 32. Exception Propagation

RG-422 SHALL identify downstream objects affected by an exception.

```text
EXCEPTION
   ↓
DEPENDENCY
   ↓
CONTROL
   ↓
DECISION
   ↓
RELIANCE
```

---

# 33. Exception Impact on Decisions

An exception MAY invalidate or condition an existing decision.

RG-420 SHALL govern reassessment.

---

# 34. Exception Impact on Reliance

Where continuing reliance depends on a control affected by an exception:

```text
EXCEPTION
   ↓
CONTROL DEGRADATION
   ↓
RELIANCE REVIEW
```

RG-421 SHALL govern the outcome.

---

# 35. Exception Impact on Closure

A closed case may require reopening where a material exception demonstrates that the conditions supporting closure no longer hold.

---

# 36. Exception Monitoring

Every material exception SHALL have monitoring appropriate to its risk.

Monitoring MAY include:

```text
Configuration
Performance
Security
Compliance
Duration
Usage
Scope
Compensating Control
```

---

# 37. Exception Health

Exception status MAY be:

```text
HEALTHY
AT RISK
OVERDUE
BREACHED
SUSPENDED
EXPIRED
```

---

# 38. Exception Breach

An exception is breached when its conditions are exceeded.

Example:

```text
APPROVED LIMIT = 10 USERS
ACTUAL = 15 USERS
```

The breach SHALL trigger reassessment.

---

# 39. Exception Breach Response

Possible responses:

```text
CONTAIN
RESTORE
SUSPEND
REVOKE
REMEDIATE
ESCALATE
INCIDENT
```

---

# 40. Exception Revocation

An exception MAY be revoked because of:

```text
Increased Risk
Breach
Changed Requirement
Changed Dependency
Security Event
Loss of Authority
Failed Compensation
```

---

# 41. Exception Suspension

Suspension MAY temporarily prevent reliance on an exception while retaining its historical record.

---

# 42. Emergency Exception

Emergency exceptions MAY be used where immediate action is necessary.

They SHALL retain:

```text
Reason
Authority
Scope
Risk
Compensation
Post-Event Review
```

---

# 43. Emergency Exception Review

Emergency exceptions SHALL undergo retrospective review.

The review SHALL determine:

```text
Was emergency status justified?
Was scope appropriate?
Was risk controlled?
Is further action required?
```

---

# 44. Temporary State

A temporary state is an intentionally different operating condition.

Examples:

```text
Maintenance Mode
Emergency Configuration
Temporary Access
Temporary Routing
Temporary Control
Temporary Threshold
Temporary Process
```

---

# 45. Temporary State Definition

Every temporary state SHALL define:

```text
Normal State
Temporary State
Trigger
Duration
Owner
Controls
Exit Criteria
Restoration Method
```

---

# 46. Temporary State Activation

Activation SHALL be authorised according to risk.

The system SHALL record:

```text
Who
What
When
Why
Authority
```

---

# 47. Temporary State Observation

Temporary states SHALL be monitored for:

```text
Scope
Duration
Risk
Unexpected Behaviour
Exit Conditions
```

---

# 48. Temporary State Exit

Exit SHALL be explicit:

```text
RESTORED
SUPERSEDED
EXTENDED
FAILED
ESCALATED
```

---

# 49. Temporary State Expiry

Expiry SHALL trigger a defined action.

No temporary state SHALL remain active solely because nobody closed it.

---

# 50. Temporary State Restoration

Restoration SHALL be verified against the approved baseline.

```text
TEMPORARY STATE
      ↓
RESTORE
      ↓
BASELINE COMPARISON
      ↓
VERIFICATION
```

---

# 51. Temporary State Failure

If restoration fails:

```text
RESTORATION FAILURE
   ↓
DRIFT
   ↓
RISK ASSESSMENT
   ↓
REMEDIATION / INCIDENT
```

---

# 52. Controlled Deviation

A controlled deviation SHALL contain:

```text
Reason
Boundary
Authority
Duration
Risk
Monitoring
Compensation
Exit
```

---

# 53. Uncontrolled Deviation

An unexplained deviation SHALL remain:

```text
UNCONTROLLED
```

until assessed.

It SHALL not inherit the legitimacy of a nearby exception.

---

# 54. Exception Inheritance

Exceptions SHALL not automatically propagate to other objects.

```text
EXCEPTION A
   ≠
EXCEPTION B
```

unless explicit inheritance is governed.

---

# 55. Exception Scope Expansion

Expanding an exception scope SHALL be treated as a material change where appropriate.

---

# 56. Exception Transfer

An exception may not automatically transfer to:

```text
New Owner
New System
New Environment
New Version
New Dependency
```

Transfer SHALL require review.

---

# 57. Exception Supersession

A new exception MAY supersede an older exception.

Historical records SHALL remain intact.

---

# 58. Exception Cancellation

An exception MAY be cancelled before expiry.

Cancellation SHALL record:

```text
Reason
Authority
Effective Time
Final State
```

---

# 59. Exception Closure

Closure SHALL require:

```text
Deviation Resolved / Validly Accepted
Compensating Controls Removed or Retained as Approved
Evidence Present
Residual Risk Assessed
Authority
```

---

# 60. Closure vs Expiry

Expiry is a lifecycle event.

Closure is a governed conclusion.

An expired exception SHALL still require closure processing.

---

# 61. Exception Evidence

Material exception records SHALL retain:

```text
Request
Assessment
Approval
Conditions
Monitoring
Breaches
Reviews
Renewals
Closure
```

---

# 62. Evidence Integrity

Exception evidence SHALL be protected against:

```text
Deletion
Modification
Backdating
Scope Manipulation
Approval Spoofing
```

---

# 63. Exception Audit Trail

Audit events MAY include:

```text
Exception Requested
Exception Assessed
Exception Approved
Exception Activated
Exception Breached
Exception Renewed
Exception Suspended
Exception Revoked
Exception Expired
Exception Closed
```

---

# 64. Exception Register

The system SHOULD maintain:

```text
Active Exceptions
Expiring Exceptions
Overdue Exceptions
High-Risk Exceptions
Breached Exceptions
Emergency Exceptions
Long-Lived Exceptions
```

---

# 65. Exception Dashboard

The dashboard SHOULD display:

```text
Exception Count
High-Risk
Overdue
Expiring
Breached
Suspended
Renewal Due
Compensating Controls
```

---

# 66. Exception Metrics

Possible measures:

```text
Exception Volume
Exception Age
Average Duration
Renewal Rate
Breach Rate
Emergency Rate
Exception Debt
Closure Time
```

---

# 67. Exception Trend

Increasing exception volume MAY indicate:

```text
Weak Architecture
Poor Change Management
Control Failure
Unrealistic Requirements
Resource Constraints
Systemic Risk
```

Trend analysis SHALL be performed where material.

---

# 68. Exception Concentration

The system SHOULD identify:

```text
Many Exceptions
   ↓
One System / Control / Owner
```

Such concentration MAY indicate systemic weakness.

---

# 69. Compensating Control Object

Every material compensating control SHALL identify:

```text
Control Objective
Scope
Owner
Frequency
Evidence
Effectiveness
Expiry
```

---

# 70. Compensating Control Effectiveness

Compensating controls SHALL be evaluated for:

```text
Coverage
Strength
Reliability
Independence
Duration
Residual Risk
```

---

# 71. Compensating Control Failure

Failure SHALL trigger:

```text
Exception Breach
Risk Reassessment
Escalation
Alternative Control
```

---

# 72. Compensating Control Independence

Where feasible, compensating controls SHOULD not depend on the same failed component as the primary control.

---

# 73. Exception Risk Aggregation

The system SHOULD support aggregate analysis:

```text
EXCEPTION A
+
EXCEPTION B
+
CONTROL FAILURE
=
AGGREGATE RISK
```

---

# 74. Exception and Change

Changes creating or modifying exceptions SHALL follow RG-423.

---

# 75. Exception and Baseline

Exceptions SHALL reference the relevant RG-424 baseline.

---

# 76. Exception and Monitoring

RG-425 SHALL continuously monitor material exception conditions.

---

# 77. Exception and Dependency

RG-422 SHALL identify propagation and dependency impact.

---

# 78. Exception and Assurance

RG-419 SHALL provide independent assurance where required.

---

# 79. Exception and Risk

RG-415 SHALL provide risk assessment and tolerance.

---

# 80. Exception and Policy

RG-414 SHALL define which requirements may be excepted and by whom.

---

# 81. Exception and Authority

RG-413 SHALL define approval authority.

---

# 82. Exception and Evidence

RG-412 SHALL provide evidence traceability.

---

# 83. Exception and Workflow

RG-411 SHALL govern lifecycle state transitions.

---

# 84. Exception and Decision

RG-420 SHALL govern acceptance, suspension, revocation and closure decisions.

---

# 85. Exception and Post-Closure Reliance

RG-421 SHALL determine whether a continuing reliance relationship remains valid.

---

# 86. MFM Data Model

Core entities:

```text
Exception
Deviation
TemporaryState
Waiver
Tolerance
CompensatingControl
ExceptionCondition
ExceptionReview
ExceptionBreach
ExceptionRenewal
ExceptionClosure
```

Relationships:

```text
Requirement
   ↓
Deviation
   ↓
Exception
   ↓
Conditions
   ↓
Monitoring
   ↓
Review
   ↓
Remediation / Renewal / Closure
```

---

# 87. MFM Service Boundary

The conceptual implementation should include:

```text
Exception Service
Deviation Service
Temporary State Service
Waiver Service
Tolerance Service
Compensating Control Service
Exception Review Service
Exception Breach Service
Exception Lifecycle Service
```

These integrate with:

```text
Policy
Authority
Risk
Dependency
Impact
Change
Baseline
Monitoring
Finding
Incident
Remediation
Assurance
Decision
Reliance
Evidence
State
Audit
```

---

# 88. API Concepts

Illustrative operations:

```text
createException()
assessException()
approveException()
activateException()
monitorException()
recordBreach()
renewException()
suspendException()
revokeException()
expireException()
closeException()

createTemporaryState()
activateTemporaryState()
restoreTemporaryState()
verifyTemporaryState()

createCompensatingControl()
testCompensatingControl()
retireCompensatingControl()
```

These are architectural concepts, not implementation-specific commitments.

---

# 89. Automated Exception Monitoring

Automation MAY detect:

```text
Expiry
Scope Breach
Condition Breach
Missing Evidence
Missing Review
Compensating Control Failure
```

---

# 90. Automated Renewal

Automatic renewal SHOULD be prohibited for material exceptions unless explicitly authorised by policy.

A renewal is a governance decision.

---

# 91. AI-Assisted Exception Analysis

AI MAY assist with:

```text
Risk Summaries
Exception Clustering
Duplicate Detection
Dependency Identification
Renewal Recommendations
```

AI SHALL not silently approve exceptions.

---

# 92. AI Exception Approval

Final approval SHALL remain attributable to authorised governance unless policy explicitly permits bounded automation.

---

# 93. Exception Security

Exception records SHALL be protected against:

```text
Unauthorised Approval
Scope Expansion
Expiry Manipulation
Evidence Deletion
Privilege Abuse
```

---

# 94. Exception Privacy

Exception records may contain sensitive operational information.

Access SHALL follow:

```text
Least Privilege
Need to Know
Purpose Limitation
Audit
```

---

# 95. Failure Handling

If the exception system becomes unavailable:

```text
NEW MATERIAL EXCEPTIONS
   ↓
BLOCK / MANUAL GOVERNANCE
```

Existing critical exceptions SHALL retain monitoring.

---

# 96. Manual Fallback

Manual exception handling SHALL define:

```text
Approved Form
Authority
Evidence
Duration
Review
Entry into System
```

---

# 97. Exception System Recovery

After recovery:

```text
Manual Records
   ↓
System Registration
   ↓
Reconciliation
   ↓
Audit Verification
```

---

# 98. Exception Testing

The architecture SHALL test:

```text
Request
Assessment
Approval
Activation
Monitoring
Breach
Renewal
Suspension
Revocation
Expiry
Closure
Temporary State
Restoration
Compensating Control
```

---

# 99. Negative Testing

The system SHALL verify:

```text
No authority → BLOCK
No expiry for temporary exception → BLOCK
Scope undefined → BLOCK
Compensating control missing → ESCALATE
Expired exception → INACTIVE
Expired exception used → ALERT
Scope breach → BREACH
Renewal without reassessment → BLOCK
Exception inheritance without authority → BLOCK
Exception after owner removal → REVIEW
Temporary state without exit criteria → BLOCK
Silent exception extension → BLOCK
```

---

# 100. Scenario Testing

Representative scenarios:

```text
Low-risk temporary deviation
High-risk security exception
Emergency exception
Temporary access
Temporary configuration
Policy waiver
Control failure with compensation
Exception breach
Expired exception
Renewal
Revocation
Compensating control failure
Multiple stacked exceptions
Exception affecting closed decision
Exception affecting continuing reliance
Temporary state restoration failure
Unknown deviation
Systemic exception growth
```

---

# 101. Acceptance Criteria

EA-IMETA-PC-RG-426 is accepted when:

- deviation and exception are explicitly distinguished;
- exceptions are authorised, scoped and time-bound where appropriate;
- temporary states have defined entry and exit criteria;
- waivers and tolerances are distinct concepts;
- compensating controls are governed;
- exception risk and materiality are assessed;
- separation of duties is supported;
- scope expansion and transfer require governance;
- exception stacking and aggregate risk are visible;
- breaches are detected;
- expiry and renewal are controlled;
- silent renewal is prevented;
- long-lived exception debt is measurable;
- exceptions integrate with change, baseline, monitoring, dependency and impact governance;
- decisions and post-closure reliance are reassessed where necessary;
- AI-assisted exception analysis cannot silently approve exceptions;
- historical evidence and audit trails are preserved;
- negative tests prevent unauthorised or indefinite exceptions.

---

# 102. Next Step

The next logical artifact is the **PC-RG exception closure, remediation and lessons-learned governance model**, because RG-426 defines how deviations are authorised and controlled, while the architecture now needs to establish how exceptions are permanently eliminated, formally accepted, converted into changes, or closed with retained organisational learning.

Provisional next artifact:

> **EA-IMETA-PC-RG-427 — EXCEPTION REMEDIATION, CLOSURE & LESSONS-LEARNED MODEL**

This will establish the controlled transition from temporary deviation to restored baseline, permanent policy decision, or formally accepted residual condition.

---

# 103. Governing Principle

> **An exception is not a bypass of governance; it is governance applied to a deviation. Every exception therefore requires a defined boundary, accountable authority, monitored duration, explicit outcome and preserved evidence.**

The PC-RG architecture SHALL ensure that temporary states remain temporary, deviations remain visible, compensating controls remain effective, and exceptions cannot silently become permanent uncontrolled drift.

# END OF EA-IMETA-PC-RG-426
