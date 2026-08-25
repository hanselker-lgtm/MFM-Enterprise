# EA-IMETA-PC-RG-417

## FINDING, INCIDENT & EXCEPTION MANAGEMENT MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-417 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Finding, Incident & Exception Management Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-416 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define controlled objects and lifecycle processes for findings, incidents, exceptions, ownership, containment, assessment, resolution and closure |
| Architectural Boundary | Detection → Finding/Incident/Exception → Assessment → Containment → Decision → Remediation → Verification → Closure |

---

# 2. Purpose

EA-IMETA-PC-RG-417 defines the controlled management model between detection and remediation.

RG-416 establishes monitoring, observability and early warning.

RG-417 establishes the objects used when a detected condition requires governed action.

The architecture SHALL distinguish:

```text
OBSERVATION
= SOMETHING WAS OBSERVED

FINDING
= A CONDITION REQUIRING GOVERNED ASSESSMENT OR ACTION

INCIDENT
= AN EVENT OR CONDITION REQUIRING INCIDENT RESPONSE

EXCEPTION
= AN AUTHORISED DEPARTURE FROM A REQUIREMENT, CONTROL OR RULE

REMEDIATION
= ACTION TAKEN TO ADDRESS A CONFIRMED CONDITION
```

These objects SHALL not be collapsed into a generic "issue" record.

---

# 3. Core Principle

> **Detection creates visibility; classification creates governance; remediation creates correction; verification creates assurance; closure records completion.**

The lifecycle is:

```text
SIGNAL
   ↓
OBSERVATION
   ↓
CLASSIFICATION
   ↓
FINDING / INCIDENT / EXCEPTION
   ↓
ASSESSMENT
   ↓
CONTAINMENT
   ↓
DECISION
   ↓
REMEDIATION
   ↓
VERIFICATION
   ↓
CLOSURE
```

---

# 4. Finding

A finding identifies a condition that has been assessed as requiring governed follow-up.

Examples:

```text
CONTROL FAILURE
EVIDENCE GAP
POLICY DEVIATION
PROCESS DEVIATION
REGRESSION INDICATOR
DATA QUALITY FAILURE
AUTHORITY VIOLATION
COMPLIANCE GAP
SECURITY WEAKNESS
```

A finding does not automatically mean that an incident has occurred.

---

# 5. Finding Object

Minimum attributes:

```text
Finding ID
Case ID
Source
Detection Reference
Description
Category
Severity
Materiality
Risk
Requirement
Control
Evidence
Owner
Due Date
Status
Created At
Updated At
Decision
Resolution
Closure Authority
Version
```

---

# 6. Finding Lifecycle

```text
OPEN
  ↓
TRIAGED
  ↓
ASSESSED
  ↓
ASSIGNED
  ↓
IN TREATMENT
  ↓
PENDING VERIFICATION
  ↓
VERIFIED
  ↓
CLOSED
```

Alternative paths MAY include:

```text
REJECTED
DUPLICATE
FALSE POSITIVE
ACCEPTED RISK
ESCALATED
SUSPENDED
REOPENED
```

---

# 7. Finding Classification

Findings SHALL be classified by:

```text
TYPE
SEVERITY
MATERIALITY
RISK
SCOPE
SOURCE
CONTROL
REQUIREMENT
```

Classification SHALL be explicit and versioned where material.

---

# 8. Severity

Illustrative:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Severity SHALL be governed by policy.

Severity and materiality SHALL remain distinct.

---

# 9. Severity vs Materiality

A finding may be:

```text
HIGH SEVERITY
BUT
NOT MATERIAL TO THE ACCEPTED STATE
```

or:

```text
LOW NUMERICAL SEVERITY
BUT
MATERIAL BECAUSE A CRITICAL CONTROL IS AFFECTED
```

The architecture SHALL preserve both assessments.

---

# 10. Finding Source

Sources MAY include:

```text
MONITORING
AUDIT
TEST
USER REPORT
INCIDENT
COMPLIANCE REVIEW
SECURITY SYSTEM
AI / AGENT
EXTERNAL PARTY
MANUAL OBSERVATION
```

The original source SHALL remain traceable.

---

# 11. Finding Evidence

Every material finding SHALL reference supporting evidence.

```text
Finding
 ├── Evidence A
 ├── Evidence B
 └── Source
```

Evidence SHALL retain the version and validity applicable to the finding.

---

# 12. Finding Assessment

Assessment SHALL determine:

```text
Is the finding valid?
What happened?
What is affected?
What is the severity?
Is it material?
What is the risk?
Is containment required?
Is an incident required?
Is remediation required?
```

Assessment SHALL be attributable to an authorised actor.

---

# 13. Finding Triage

Triage determines initial treatment.

Possible outcomes:

```text
VALID FINDING
FALSE POSITIVE
DUPLICATE
INFORMATION ONLY
REQUIRES INCIDENT
REQUIRES EXCEPTION
REQUIRES REMEDIATION
ESCALATE
```

Triage SHALL not replace formal assessment where policy requires it.

---

# 14. Duplicate Findings

Duplicate findings SHALL be linked rather than silently deleted.

```text
Finding A
   ↓
DUPLICATE OF
   ↓
Finding B
```

The source evidence of both records SHALL remain traceable.

---

# 15. False Positive

A false positive is a detected condition that, after assessment, does not constitute the governed condition initially suspected.

It SHALL record:

```text
Original Detection
Assessment
Reason
Evidence
Reviewer
Disposition
```

False positives SHALL be useful inputs for monitoring improvement.

---

# 16. Incident

An incident is a condition requiring coordinated response because of actual or potential impact.

Examples:

```text
SECURITY INCIDENT
SERVICE INCIDENT
DATA INCIDENT
COMPLIANCE INCIDENT
MAJOR CONTROL FAILURE
CRITICAL DEPENDENCY FAILURE
```

Incident classification SHALL be governed by policy.

---

# 17. Incident Object

Minimum attributes:

```text
Incident ID
Detection
Start Time
Detection Time
Impact
Scope
Severity
Affected Services
Affected Cases
Containment
Incident Commander / Owner
Status
Communications
Evidence
Root Cause
Recovery
Post-Incident Review
Closure
```

---

# 18. Incident Lifecycle

```text
DETECTED
   ↓
DECLARED
   ↓
CONTAINING
   ↓
INVESTIGATING
   ↓
RECOVERING
   ↓
MONITORING
   ↓
RESOLVED
   ↓
POST-INCIDENT REVIEW
   ↓
CLOSED
```

Critical incidents MAY follow an expedited path.

---

# 19. Incident Declaration

A finding may be promoted to an incident when defined criteria are satisfied.

Example:

```text
Finding
+
Critical Impact
+
Immediate Operational Consequence
        ↓
Incident
```

The promotion rule SHALL be explicit.

---

# 20. Incident Command

Critical incidents SHALL have a designated incident authority.

The role SHALL coordinate:

```text
Containment
Communication
Investigation
Recovery
Escalation
Decision Making
Evidence Preservation
```

Incident command SHALL not automatically grant authority over unrelated business decisions.

---

# 21. Containment

Containment aims to prevent further impact.

Actions MAY include:

```text
ISOLATE
DISABLE
RESTRICT
SUSPEND
ROLL BACK
BLOCK
QUARANTINE
```

Containment SHALL be authorised according to risk and emergency policy.

---

# 22. Containment vs Remediation

The architecture SHALL distinguish:

```text
CONTAINMENT
= LIMIT IMMEDIATE IMPACT

REMEDIATION
= ADDRESS THE UNDERLYING CONDITION
```

Containment does not prove remediation.

---

# 23. Exception

An exception represents an approved departure from an otherwise applicable requirement, control, policy or rule.

Examples:

```text
Temporary Control Deviation
Approved SLA Exception
Temporary Evidence Gap
Emergency Process Deviation
Approved Configuration Exception
```

An exception SHALL never be created merely to hide a finding.

---

# 24. Exception Object

Minimum attributes:

```text
Exception ID
Requirement
Control / Rule
Reason
Risk
Scope
Compensating Controls
Owner
Authority
Effective From
Effective Until
Review Date
Conditions
Evidence
Status
Decision
Audit Reference
```

---

# 25. Exception Lifecycle

```text
REQUESTED
   ↓
ASSESSED
   ↓
RISK REVIEW
   ↓
APPROVED
   ↓
ACTIVE
   ↓
REVIEWED
   ↓
EXPIRED / CLOSED
```

Possible outcomes:

```text
REJECTED
REVOKED
ESCALATED
```

---

# 26. Exception Authority

Exception approval SHALL be explicit.

The requester SHALL not automatically be the approving authority.

High-risk exceptions MAY require independent review or multiple approvals.

---

# 27. Exception Duration

Exceptions SHALL be time-bound unless a governing policy explicitly permits otherwise.

```text
ACTIVE
  ↓
EXPIRING
  ↓
EXPIRED
```

Expired exceptions SHALL not silently continue.

---

# 28. Compensating Controls

An exception SHALL identify compensating controls where required.

Example:

```text
CONTROL A UNAVAILABLE
        ↓
EXCEPTION
        +
CONTROL B
        +
ENHANCED MONITORING
```

Compensating controls SHALL be monitored.

---

# 29. Exception Risk

Exception approval SHALL evaluate:

```text
Inherent Risk
Compensating Controls
Residual Risk
Tolerance
Materiality
Duration
Scope
```

Risk above the permitted tolerance SHALL block approval unless a higher authority explicitly permits the defined treatment.

---

# 30. Finding / Incident / Exception Relationship

The objects may interact:

```text
OBSERVATION
   ↓
FINDING
   ├──→ INCIDENT
   ├──→ EXCEPTION
   └──→ REMEDIATION
```

An incident MAY generate multiple findings.

An exception MAY be associated with a finding.

A finding SHALL not be automatically converted to an exception.

---

# 31. Incident and Finding Relationship

An incident may produce:

```text
Root Cause Finding
Control Finding
Security Finding
Compliance Finding
Evidence Finding
Process Finding
```

Each finding SHALL retain its own lifecycle.

---

# 32. Root Cause

Root-cause analysis SHALL distinguish:

```text
SYMPTOM
CONTRIBUTING FACTOR
DIRECT CAUSE
SYSTEMIC CAUSE
ROOT CAUSE
```

A root cause SHALL not be asserted solely from temporal correlation.

---

# 33. Root Cause Evidence

Root-cause conclusions SHALL reference evidence.

Where root cause remains uncertain:

```text
ROOT CAUSE = UNKNOWN / UNDER INVESTIGATION
```

rather than an unsupported assumption.

---

# 34. Corrective Action

Corrective actions SHALL be represented as controlled tasks.

```text
Finding
   ↓
Corrective Action
   ↓
Owner
   ↓
Due Date
   ↓
Evidence
   ↓
Verification
```

---

# 35. Preventive Action

Preventive actions address potential recurrence.

Examples:

```text
Control Enhancement
Monitoring Improvement
Process Change
Training
Architecture Change
Rule Change
Dependency Change
```

Preventive action SHALL be linked to the relevant risk or root cause.

---

# 36. Remediation Integration

RG-417 creates the governed trigger for remediation.

```text
CONFIRMED FINDING
      ↓
REMEDIATION PLAN
      ↓
EXECUTION
      ↓
VERIFICATION
```

Detailed remediation orchestration remains governed by the relevant workflow architecture.

---

# 37. Finding Ownership

Every actionable finding SHALL have:

```text
Owner
Accountability
Due Date
Priority
Authority
```

Ownership changes SHALL be audited.

---

# 38. Due Dates

Due dates SHALL be based on:

```text
Severity
Risk
Materiality
Policy
Operational Impact
```

Critical findings MAY have immediate response requirements.

---

# 39. Overdue Findings

Overdue findings SHALL trigger:

```text
Reminder
Escalation
Risk Reassessment
Management Review
```

depending on severity.

Overdue status SHALL not automatically close or downgrade a finding.

---

# 40. Finding Reopening

A closed finding MAY be reopened when:

```text
Recurrence
Verification Failure
New Evidence
Incorrect Closure
Material Change
New Risk
```

Reopening SHALL be explicit and audited.

---

# 41. Incident Reopening

An incident MAY be reopened if evidence shows:

```text
Condition Recurs
Recovery Was Incomplete
Impact Was Underestimated
Root Cause Was Incorrect
Related Failure Emerges
```

The original incident history SHALL remain intact.

---

# 42. Exception Renewal

An exception SHALL not be renewed automatically unless the policy explicitly allows it.

Renewal SHALL require reassessment of:

```text
Risk
Materiality
Compensating Controls
Duration
Need
Authority
```

---

# 43. Exception Stacking

The system SHOULD detect multiple exceptions affecting the same:

```text
Control
Requirement
Case
System
Dependency
```

Stacked exceptions may create systemic risk.

---

# 44. Exception Concentration

The architecture SHOULD identify:

```text
Repeated Exceptions
Long-Lived Exceptions
Exceptions for Critical Controls
Exceptions by Same Owner
Exceptions on Same Dependency
```

Concentration MAY trigger escalation.

---

# 45. Incident Severity

Incident severity MAY consider:

```text
Impact
Scope
Duration
Urgency
Security
Compliance
Safety
Data
Availability
Decision Integrity
```

Severity SHALL not be determined solely by event count.

---

# 46. Incident Escalation

Incident escalation SHALL follow:

```text
Severity
+
Impact
+
Duration
+
Risk
+
Scope
```

Possible routes:

```text
Operational
Management
Security
Compliance
Executive
External / Regulatory
```

where applicable.

---

# 47. Communications

Material incidents SHALL have controlled communication requirements.

The communication record SHOULD include:

```text
Audience
Message
Time
Sender
Approval
Channel
Status
```

Communication SHALL not expose information beyond authorised scope.

---

# 48. Evidence Preservation

During an incident, relevant evidence SHALL be preserved.

Examples:

```text
Logs
Events
Snapshots
Configuration
Audit Records
Evidence Objects
Messages
Traces
```

Evidence preservation SHALL support later reconstruction.

---

# 49. Chain of Custody

Where evidence integrity is critical, chain of custody SHALL record:

```text
Collected By
Collected At
Source
Transfer
Storage
Access
Analysis
Disposition
```

---

# 50. Incident Timeline

Material incidents SHOULD have a reconstructable timeline:

```text
FIRST SIGNAL
↓
DETECTION
↓
DECLARATION
↓
CONTAINMENT
↓
ESCALATION
↓
RECOVERY
↓
RESOLUTION
↓
REVIEW
```

Timestamps SHALL use an authoritative time source.

---

# 51. Finding Timeline

Findings SHOULD support:

```text
Created
Triaged
Assessed
Assigned
Action Started
Action Completed
Verified
Closed
Reopened
```

---

# 52. Exception Timeline

Exceptions SHALL support:

```text
Requested
Assessed
Approved
Activated
Reviewed
Renewed
Expired
Revoked
Closed
```

---

# 53. Status vs Outcome

The architecture SHALL distinguish:

```text
STATUS
= WHERE THE OBJECT IS IN ITS LIFECYCLE

OUTCOME
= WHAT WAS DECIDED
```

Example:

```text
Finding Status = CLOSED
Outcome = ACCEPTED RISK
```

---

# 54. Closure

Closure SHALL require defined evidence.

A finding SHALL not be closed merely because:

```text
Task = Completed
```

Closure SHALL consider:

```text
Root Cause
Corrective Action
Verification
Residual Risk
Evidence
Conditions
Authority
```

---

# 55. Closure Outcomes

Possible outcomes:

```text
RESOLVED
ACCEPTED RISK
FALSE POSITIVE
DUPLICATE
NO FURTHER ACTION
SUPERSEDED
TRANSFERRED
```

The selected outcome SHALL be explicit.

---

# 56. Incident Closure

Incident closure SHALL require:

```text
Containment Complete
Recovery Complete
Required Evidence Preserved
Impact Assessed
Actions Assigned
Post-Incident Review Required/Completed
Authority Approval
```

---

# 57. Exception Closure

Exception closure SHALL require:

```text
Exception No Longer Needed
Control Restored
Alternative Control Established
Exception Expired
Risk Reassessed
Authority Confirmed
```

---

# 58. Closure Verification

Independent verification SHALL be required where policy or risk demands it.

```text
REMEDIATION OWNER
       ≠
VERIFIER
```

This reinforces RG-413 separation of duties.

---

# 59. Residual Risk

After remediation or incident recovery:

```text
Risk Before
   ↓
Treatment
   ↓
Risk After
```

Residual risk SHALL be reassessed before final closure where material.

---

# 60. Finding Closure and State

Closing a finding does not automatically restore a lifecycle state.

Example:

```text
Finding CLOSED
```

does not automatically mean:

```text
CASE ACCEPTED
```

The state machine SHALL make the final lifecycle decision.

---

# 61. Incident Closure and State

Similarly:

```text
INCIDENT RESOLVED
```

does not automatically mean:

```text
REACCEPTED
```

Revalidation/reverification/reacceptance may still be required.

---

# 62. Exception Closure and State

Ending an exception does not automatically restore the state.

The system SHALL evaluate whether required controls and criteria are satisfied.

---

# 63. Finding Correlation

Findings SHOULD support relationships:

```text
RELATED TO
CAUSED BY
CONTRIBUTES TO
DUPLICATE OF
SUPERSEDES
RESULTS FROM
AFFECTS
```

Relationships SHALL be typed.

---

# 64. Incident Correlation

Incidents MAY be correlated by:

```text
Dependency
Control
Root Cause
Time
Service
Case
Threat
Change
```

Correlation SHALL not merge distinct incidents without controlled authority.

---

# 65. Exception Correlation

Exceptions SHOULD identify related:

```text
Findings
Controls
Requirements
Risks
Dependencies
Compensating Controls
```

---

# 66. Problem Management

Repeated incidents/findings SHOULD support problem management.

```text
Incident A
Incident B
Incident C
   ↓
COMMON PROBLEM
   ↓
SYSTEMIC REMEDIATION
```

Problem management is distinct from individual incident closure.

---

# 67. Recurrence Detection

The architecture SHOULD detect recurrence based on:

```text
Same Control
Same Root Cause
Same Dependency
Same Failure Signature
Same Requirement
```

Recurrence MAY increase severity/materiality.

---

# 68. SLA Management

Finding, incident and exception SLAs SHALL support:

```text
Response Time
Assessment Time
Containment Time
Remediation Time
Verification Time
Closure Time
Review Time
```

SLA breaches SHALL be auditable.

---

# 69. Escalation Integration

RG-415 escalation SHALL consume:

```text
Severity
Risk
Materiality
Age
SLA
Recurrence
Scope
```

The resulting escalation SHALL be recorded as an event.

---

# 70. Monitoring Integration

RG-416 monitoring feeds:

```text
Alerts
Early Warnings
Signals
Observations
```

into RG-417 classification.

```text
MONITOR
 ↓
ALERT
 ↓
FINDING / INCIDENT / EXCEPTION ASSESSMENT
```

---

# 71. Policy Integration

RG-414 rules determine:

```text
Finding Classification
Incident Trigger
Exception Eligibility
Severity
Materiality
Closure Criteria
```

---

# 72. Authority Integration

RG-413 determines:

```text
Who may classify
Who may approve exceptions
Who may declare incidents
Who may close findings
Who may accept residual risk
Who may reopen
```

---

# 73. Evidence Integration

RG-412 provides:

```text
Evidence
Decision
Audit
Traceability
```

for all material finding/incident/exception actions.

---

# 74. Workflow Integration

RG-411 orchestrates:

```text
Triage
Assessment
Containment
Remediation
Verification
Closure
```

RG-417 defines the governed objects those workflows operate upon.

---

# 75. MFM Data Model

Core entities:

```text
Finding
FindingAssessment
Incident
IncidentTimeline
Exception
ExceptionAssessment
ContainmentAction
CorrectiveAction
PreventiveAction
RootCause
ClosureDecision
```

Relationships:

```text
Observation
   ↓
Finding / Incident / Exception
   ↓
Assessment
   ↓
Action
   ↓
Verification
   ↓
Closure
```

---

# 76. MFM Service Boundary

The conceptual implementation should include:

```text
Finding Service
Incident Service
Exception Service
Triage Service
Containment Service
Root Cause Service
Action Service
Closure Service
Problem Management Service
```

These integrate with:

```text
Monitoring
Risk
Policy
Authority
Evidence
Workflow
State
Audit
```

services.

---

# 77. API Concepts

Illustrative operations:

```text
createFinding()
triageFinding()
assessFinding()
createIncident()
declareIncident()
containIncident()
createException()
assessException()
approveException()
createAction()
verifyResolution()
closeFinding()
closeIncident()
closeException()
reopenFinding()
reopenIncident()
renewException()
```

These are architectural concepts, not implementation-specific commitments.

---

# 78. Search and Reporting

The system SHOULD support queries such as:

```text
Show all open critical findings.

Show findings affecting control C.

Show incidents caused by dependency D.

Show active exceptions for requirement R.

Show overdue findings.

Show repeated findings by root cause.

Show all closed findings reopened in the last period.

Show all expired exceptions.

Show all incidents associated with a specific deployment.
```

---

# 79. Dashboard

The dashboard SHOULD expose:

```text
Open Findings
Critical Findings
Open Incidents
Active Exceptions
Overdue Actions
Expiring Exceptions
Repeated Conditions
Top Root Causes
Risk Above Tolerance
SLA Breaches
```

---

# 80. Audit

Material actions SHALL generate audit records:

```text
Finding Created
Classification Changed
Incident Declared
Containment Applied
Exception Approved
Exception Renewed
Risk Accepted
Action Completed
Finding Closed
Finding Reopened
Incident Closed
```

---

# 81. Security

Access SHALL be controlled by:

```text
Identity
Role
Permission
Scope
Case
Classification
Authority
```

Incident and security evidence may require additional restrictions.

---

# 82. Data Integrity

The architecture SHALL protect:

```text
Finding History
Incident Timeline
Exception History
Evidence Links
Closure Decisions
Audit Records
```

Historical records SHALL not be silently overwritten.

---

# 83. Versioning

Material changes to:

```text
Finding Classification
Severity
Materiality
Risk
Exception Terms
Closure Criteria
```

SHALL be versioned or historically auditable.

---

# 84. Privacy

Finding and incident records MAY contain sensitive operational information.

The system SHALL support:

```text
Least Privilege
Purpose Limitation
Controlled Disclosure
Retention
Access Audit
```

---

# 85. Data Retention

Retention SHALL be defined for:

```text
Findings
Incidents
Exceptions
Evidence
Actions
Audit
Communications
```

Legal/compliance holds SHALL override normal destruction where applicable.

---

# 86. Failure Handling

If the finding/incident/exception service is unavailable:

```text
DETECTION
   ↓
PENDING / QUEUED
   ↓
RETRY
   ↓
RECOVERY
```

Critical incident records SHALL have an approved continuity mechanism.

---

# 87. Queue Integrity

Queued findings/incidents SHALL preserve:

```text
Ordering
Timestamp
Source
Correlation
Priority
Idempotency
```

Duplicate processing SHALL be prevented.

---

# 88. Idempotency

Creating or promoting the same detection twice SHALL not create uncontrolled duplicate governed objects.

Operations SHALL support idempotency where appropriate.

---

# 89. Notification

Notifications SHALL be generated from governed events.

Examples:

```text
Critical Finding Created
Incident Declared
Exception Expiring
Action Overdue
Risk Above Tolerance
Verification Failed
Finding Reopened
```

Notification is not itself proof that the recipient acted.

---

# 90. Escalation Failure

If escalation delivery fails:

```text
DELIVERY FAILURE
   ↓
RETRY
   ↓
ALTERNATE ROUTE
   ↓
CRITICAL ESCALATION
```

Critical escalation SHALL not depend on a single notification channel.

---

# 91. Testing

The architecture SHALL test:

```text
Finding Creation
Finding Triage
False Positive
Duplicate
Incident Promotion
Exception Approval
Exception Expiry
Containment
Remediation
Verification
Closure
Reopening
Recurrence
SLA Breach
Escalation
Audit
Access Control
```

---

# 92. Negative Testing

The system SHALL verify:

```text
Unauthorised closure → BLOCK
Expired exception → BLOCK
Self-approval → BLOCK
Missing evidence → BLOCK / REVIEW
Unknown root cause → NOT INVENTED
Closed finding without verification → BLOCK
Incident closure without required review → BLOCK
Exception without risk assessment → BLOCK
```

---

# 93. Scenario Testing

Representative scenarios:

```text
Minor monitoring finding
Critical security incident
Repeated control failure
Evidence invalidation
Temporary policy exception
Exception expiry
Remediation failure
Recurrence after closure
False positive
Duplicate finding
Systemic dependency failure
AI-generated anomaly
```

---

# 94. Acceptance Criteria

EA-IMETA-PC-RG-417 is accepted when:

- findings, incidents and exceptions are distinct objects;
- each has an explicit lifecycle;
- severity and materiality are distinct;
- findings can promote to incidents under governed rules;
- exceptions are time-bound and authorised;
- compensating controls are supported;
- containment and remediation are distinct;
- root-cause analysis is evidence-based;
- ownership and due dates are explicit;
- recurrence and concentration are detectable;
- closure requires appropriate verification;
- reopening is controlled;
- SLA and escalation are integrated;
- monitoring, risk, policy, authority, evidence, workflow and state are integrated;
- audit and historical integrity are preserved;
- negative tests prevent unauthorised or unsupported closure.

---

# 95. Next Step

The next logical artifact is the **PC-RG remediation and corrective-action management model**, because RG-417 establishes findings, incidents and exceptions as governed objects, while the architecture now needs to define how corrective and preventive actions are planned, executed, evidenced, verified and measured for effectiveness.

Provisional next artifact:

> **EA-IMETA-PC-RG-418 — REMEDIATION, CORRECTIVE ACTION & EFFECTIVENESS MODEL**

This will establish the controlled bridge from identified condition to demonstrably effective resolution.

---

# 96. Governing Principle

> **A finding identifies a governed condition, an incident coordinates response to impact, an exception authorises a controlled deviation, remediation addresses the condition, verification establishes effectiveness, and closure records the authorised outcome.**

The PC-RG architecture SHALL preserve these distinctions so that an item cannot disappear merely because it has been acknowledged, assigned or administratively closed.

# END OF EA-IMETA-PC-RG-417
