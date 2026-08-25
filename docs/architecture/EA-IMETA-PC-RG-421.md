# EA-IMETA-PC-RG-421

## POST-CLOSURE SURVEILLANCE & CONTINUING RELIANCE MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-421 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Post-Closure Surveillance & Continuing Reliance Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-420 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how accepted and closed outcomes remain observable, valid, trusted and eligible for continued reliance after formal closure |
| Architectural Boundary | Closure → Surveillance → Validity → Change Detection → Reassessment → Continued Reliance / Suspension / Reopening |

---

# 2. Purpose

EA-IMETA-PC-RG-421 defines the governance model that operates after acceptance and closure.

RG-420 establishes acceptance, reliance and closure decisions.

RG-421 establishes **how the organisation continues to observe the basis for those decisions after closure**.

The architecture SHALL distinguish:

```text
CLOSURE
= FORMAL END OF A GOVERNED LIFECYCLE STAGE

SURVEILLANCE
= CONTROLLED OBSERVATION AFTER CLOSURE

CONTINUING RELIANCE
= CONTINUED AUTHORISED USE WHILE VALIDITY CONDITIONS REMAIN SATISFIED

REASSESSMENT
= CONTROLLED REVIEW WHEN THE BASIS OF RELIANCE MAY HAVE CHANGED

REOPENING
= FORMAL RETURN OF A CLOSED MATTER TO ACTIVE GOVERNANCE
```

Closure SHALL therefore not be interpreted as permanent immunity from change.

---

# 3. Core Principle

> **Closure records the decision reached; surveillance tests whether the basis for that decision remains valid.**

The governing chain is:

```text
ACCEPTED / CLOSED
       ↓
POST-CLOSURE SURVEILLANCE
       ↓
CONTINUING VALIDITY
       ↓
CHANGE / REGRESSION DETECTION
       ↓
REASSESSMENT
       ↓
CONTINUE RELIANCE
   OR
SUSPEND / REVOKE / REOPEN
```

---

# 4. Post-Closure Object

Every material post-closure surveillance programme SHALL be represented as a controlled object.

Minimum attributes:

```text
Surveillance ID
Case ID
Closure Decision
Reliance Scope
Surveillance Objective
Monitored Conditions
Baseline
Indicators
Thresholds
Frequency
Owner
Review Authority
Observation Period
Escalation Rules
Reassessment Triggers
Retention
Version
Status
```

---

# 5. Surveillance Lifecycle

```text
PLANNED
   ↓
ACTIVATED
   ↓
OBSERVING
   ↓
REVIEWED
   ↓
CONTINUED
   ↓
TRIGGERED
   ↓
REASSESSED
   ↓
CONTINUE / SUSPEND / REOPEN
```

Alternative states:

```text
PAUSED
DEGRADED
EXPIRED
CANCELLED
SUPERSEDED
```

---

# 6. Surveillance Objective

The surveillance objective SHALL state what must remain true after closure.

Examples:

```text
Control remains effective.
Residual risk remains within tolerance.
Evidence remains valid.
Required authority remains active.
No material regression occurs.
System remains within approved baseline.
Reliance conditions remain satisfied.
```

---

# 7. Continuing Reliance

Continuing reliance is permitted only while its governing basis remains valid.

The basis MAY include:

```text
Acceptance
Assurance
Evidence
Risk
Controls
Policy
Rules
Configuration
Model
Dependencies
Authority
```

---

# 8. Reliance Validity Chain

```text
ACCEPTANCE
   +
VALID EVIDENCE
   +
VALID AUTHORITY
   +
VALID CONTROLS
   +
ACCEPTABLE RISK
   +
NO MATERIAL REGRESSION
   ↓
CONTINUING RELIANCE
```

Any material failure SHALL trigger reassessment.

---

# 9. Surveillance Scope

Surveillance SHALL define:

```text
Subject
Population
Environment
Dependencies
Controls
Reliance Consumers
Validity Period
Exclusions
```

Scope SHALL be explicit enough to determine what is and is not being watched.

---

# 10. Surveillance Types

Initial catalogue:

```text
RISK SURVEILLANCE
CONTROL SURVEILLANCE
COMPLIANCE SURVEILLANCE
SECURITY SURVEILLANCE
PERFORMANCE SURVEILLANCE
EVIDENCE SURVEILLANCE
AUTHORITY SURVEILLANCE
DEPENDENCY SURVEILLANCE
MODEL SURVEILLANCE
REGRESSION SURVEILLANCE
CONDITION SURVEILLANCE
```

---

# 11. Risk Surveillance

Risk surveillance SHALL monitor:

```text
Residual Risk
Risk Trend
Risk Tolerance
Risk Concentration
New Risk Factors
Risk Treatment
```

Material risk increases SHALL trigger reassessment.

---

# 12. Control Surveillance

Control surveillance MAY monitor:

```text
Control Test Results
Failure Rate
Coverage
Exceptions
Control Changes
Control Ownership
Control Effectiveness
```

A previously effective control may degrade after closure.

---

# 13. Compliance Surveillance

Compliance surveillance SHALL monitor applicable:

```text
Requirements
Obligations
Evidence
Exceptions
Deadlines
Regulatory Changes
```

Changes in obligations may trigger reassessment of previously accepted outcomes.

---

# 14. Security Surveillance

Security surveillance MAY monitor:

```text
Threats
Vulnerabilities
Access
Privileges
Integrity
Incidents
Security Controls
Certificates
Credentials
```

A security event may invalidate continuing reliance.

---

# 15. Performance Surveillance

Performance surveillance MAY monitor:

```text
Latency
Throughput
Error Rate
Availability
Capacity
Service Quality
```

Performance changes SHALL be interpreted against approved baselines.

---

# 16. Evidence Surveillance

Evidence may become invalid after closure.

The system SHALL monitor:

```text
Expiry
Integrity
Source Availability
Staleness
Scope
Validity
Retention
```

Evidence invalidation SHALL be capable of triggering reassessment.

---

# 17. Authority Surveillance

The system SHALL monitor:

```text
Role Validity
Delegation
Approval Authority
Separation of Duties
Expiry
Revocation
Scope Changes
```

Authority loss may invalidate reliance even if the technical condition remains unchanged.

---

# 18. Dependency Surveillance

Critical dependencies SHALL be monitored for:

```text
Availability
Version
Security
Integrity
Contract
Service Level
Change
Ownership
```

Dependency change may trigger reassessment.

---

# 19. Model Surveillance

Where AI/ML is part of the accepted solution, surveillance MAY include:

```text
Model Version
Data Drift
Concept Drift
Performance
Output Distribution
Error Rate
Override Rate
Safety Signals
Tool Behaviour
```

Material model change SHALL trigger reassessment.

---

# 20. Regression Surveillance

Regression surveillance asks:

```text
HAS THE ACCEPTED CONDITION REMAINED WITHIN ITS APPROVED BOUNDARY?
```

It SHALL integrate with RG-416 monitoring.

---

# 21. Surveillance Baseline

The baseline SHALL represent the accepted post-closure condition.

It MAY include:

```text
Configuration
Performance
Risk
Control State
Evidence
Model
Workflow
Authority
```

Baseline version SHALL be retained.

---

# 22. Baseline Drift

Drift occurs when the current condition gradually diverges from the accepted baseline.

Examples:

```text
Performance degradation
Increasing control failures
Growing error rate
Model drift
Risk increase
```

Drift SHALL be assessed before being classified as material regression.

---

# 23. Surveillance Thresholds

Thresholds SHALL be governed by RG-414.

Types MAY include:

```text
ABSOLUTE
RELATIVE
TREND
DURATION
COUNT
RATE
COMPOSITE
```

Threshold changes SHALL be versioned.

---

# 24. Early Warning

Surveillance SHOULD support early warning:

```text
STABLE
   ↓
NEAR THRESHOLD
   ↓
DETERIORATING TREND
   ↓
EARLY WARNING
   ↓
REASSESSMENT
```

Early warning does not automatically revoke reliance.

---

# 25. Surveillance Event

A surveillance event SHALL record:

```text
Event ID
Surveillance ID
Observation
Expected Condition
Actual Condition
Baseline
Threshold
Severity
Timestamp
Evidence
Correlation
Disposition
```

---

# 26. Surveillance Finding

A surveillance event may generate a finding:

```text
SURVEILLANCE EVENT
       ↓
ASSESSMENT
       ↓
FINDING
```

The finding SHALL follow RG-417.

---

# 27. Surveillance Incident

A material event may generate an incident:

```text
SURVEILLANCE EVENT
       ↓
CRITICAL IMPACT
       ↓
INCIDENT
```

Incident handling SHALL follow RG-417.

---

# 28. Surveillance Exception

A continuing condition may require a new exception.

```text
SURVEILLANCE
   ↓
VALIDITY GAP
   ↓
EXCEPTION ASSESSMENT
```

The exception SHALL not silently extend the original acceptance.

---

# 29. Reassessment Trigger

Triggers MAY include:

```text
Material Regression
Risk Above Tolerance
Evidence Invalidity
Authority Expiry
Control Failure
Policy Change
Rule Change
Threshold Change
Model Change
Dependency Change
Security Incident
Compliance Change
Condition Breach
```

---

# 30. Reassessment

Reassessment SHALL determine:

```text
Does acceptance remain valid?
Does reliance remain valid?
Is remediation required?
Is an exception required?
Is suspension required?
Is reopening required?
```

---

# 31. Reassessment Decision

Conceptual logic:

```text
TRIGGER
   ↓
IMPACT ASSESSMENT
   ↓
MATERIAL?
 ┌────┴─────┐
NO          YES
 │           │
 ▼           ▼
CONTINUE   REASSESS
             ↓
      CONTINUE / SUSPEND /
      REVOKE / REOPEN
```

---

# 32. Continue Reliance

Reliance may continue when:

```text
Criteria Remain Satisfied
Risk Within Tolerance
Controls Effective
Evidence Valid
Authority Valid
No Material Regression
```

The continuation decision SHOULD be recorded where material.

---

# 33. Suspension Trigger

Suspension MAY occur when:

```text
Material Uncertainty
Critical Evidence Loss
Risk Above Tolerance
Critical Control Failure
Authority Failure
Serious Incident
```

Suspension SHALL define reinstatement conditions.

---

# 34. Reopening Trigger

Reopening MAY occur when:

```text
Original Condition Recurs
Closure Was Incorrect
New Evidence Invalidates Conclusion
Material Regression
Assurance Failure
Systemic Change
```

---

# 35. Revocation Trigger

Revocation MAY be required when:

```text
Acceptance Basis Permanently Fails
Authority Withdrawn
Requirement No Longer Satisfied
Critical Integrity Failure
Fraud / Manipulation
```

---

# 36. Closure Does Not Equal Immortality

A closed record SHALL remain historically closed unless a governed trigger requires reopening.

The architecture SHALL preserve:

```text
Original Closure
Post-Closure Event
Reassessment
New Decision
```

---

# 37. Surveillance Frequency

Frequency SHALL be risk-based.

Possible models:

```text
CONTINUOUS
EVENT DRIVEN
DAILY
WEEKLY
MONTHLY
QUARTERLY
ANNUAL
```

The frequency SHALL reflect the rate at which validity may change.

---

# 38. Event-Driven Surveillance

Surveillance MAY be triggered by:

```text
Deployment
Policy Change
Rule Change
Model Change
Dependency Change
Incident
Authority Change
Evidence Expiry
```

Event correlation SHALL be preserved.

---

# 39. Periodic Surveillance

Periodic review MAY evaluate:

```text
Risk
Evidence
Controls
Authority
Dependencies
Conditions
Reliance Consumers
```

Periodic review SHALL not merely repeat historical acceptance text.

---

# 40. Surveillance Review

Every material surveillance programme SHALL have a review owner.

Review SHALL evaluate:

```text
Coverage
Signal Quality
Thresholds
Findings
Trends
Open Conditions
Risk
Reliance
```

---

# 41. Surveillance Ownership

Every surveillance object SHALL identify:

```text
Owner
Reviewer
Escalation Authority
```

Where independence is required:

```text
Owner ≠ Reviewer
```

---

# 42. Surveillance Coverage

The system SHOULD report:

```text
Closed Items Under Surveillance
Active Surveillance
Expired Surveillance
Failed Surveillance
Coverage Gaps
High-Risk Unmonitored Items
```

---

# 43. Surveillance Failure

If surveillance fails:

```text
SURVEILLANCE FAILURE
   ↓
VISIBILITY GAP
   ↓
RISK ASSESSMENT
```

Failure SHALL not be interpreted as evidence of stability.

---

# 44. Surveillance Blind Spot

A blind spot exists when the system cannot determine whether a continuing reliance condition remains valid.

Blind spots SHALL be visible to governance.

---

# 45. Compensating Surveillance

Where normal monitoring is unavailable:

```text
AUTOMATED MONITORING
       ↓
FAILURE
       ↓
MANUAL / ALTERNATE MONITORING
```

Compensating surveillance SHALL be time-bound and documented.

---

# 46. Surveillance Data Quality

Surveillance data SHALL be assessed for:

```text
Completeness
Freshness
Accuracy
Integrity
Source Reliability
Consistency
```

Poor data quality SHALL reduce confidence.

---

# 47. Surveillance Evidence

Material surveillance results SHALL produce evidence.

Evidence SHALL include:

```text
Observation
Source
Timestamp
Baseline
Threshold
Method
Result
Disposition
```

---

# 48. Surveillance Evidence Retention

Retention SHALL support:

```text
Trend Analysis
Audit
Incident Reconstruction
Decision Reassessment
Regulatory Review
```

---

# 49. Continuing Reliance Register

A controlled register SHOULD identify:

```text
Reliance ID
Decision
Subject
Consumer
Purpose
Scope
Validity
Conditions
Surveillance
Status
```

---

# 50. Reliance Consumer

Every reliance relationship SHALL identify the consumer where material.

Examples:

```text
Business Function
System
Customer
Management
Regulator
Downstream Decision
```

---

# 51. Reliance Propagation

A decision may be relied upon by downstream decisions.

```text
ACCEPTED RESULT A
      ↓
DOWNSTREAM RELIANCE B
      ↓
DOWNSTREAM DECISION C
```

Material dependencies SHALL be traceable.

---

# 52. Reliance Dependency Graph

The system SHOULD support:

```text
Decision A
 ├──→ Reliance B
 │      └──→ Decision C
 └──→ Reliance D
```

If A becomes invalid, affected downstream reliance SHALL be identified.

---

# 53. Reliance Impact Analysis

When acceptance is suspended/revoked:

```text
ORIGINAL DECISION
   ↓
DEPENDENCY ANALYSIS
   ↓
AFFECTED RELIANCE
   ↓
DOWNSTREAM REASSESSMENT
```

---

# 54. Downstream Notification

Material reliance invalidation SHALL notify affected consumers according to policy.

Notification SHALL include:

```text
Affected Decision
Reason
Effective Time
Required Action
Scope
Authority
```

---

# 55. Reliance Revocation Propagation

Revocation MAY propagate to downstream decisions.

Propagation SHALL be policy-controlled.

The system SHALL avoid uncontrolled cascading state changes.

---

# 56. Surveillance and Risk

RG-415 risk surveillance SHALL provide:

```text
Risk Trend
Tolerance
Materiality
Escalation
```

for continuing reliance.

---

# 57. Surveillance and Monitoring

RG-416 provides:

```text
Signals
Observations
Baselines
Thresholds
Alerts
Early Warnings
```

RG-421 uses these to maintain post-closure visibility.

---

# 58. Surveillance and Findings

RG-417 provides:

```text
Findings
Incidents
Exceptions
```

when surveillance detects conditions requiring governed action.

---

# 59. Surveillance and Remediation

RG-418 provides:

```text
Corrective Action
Preventive Action
Effectiveness
```

when post-closure conditions require correction.

---

# 60. Surveillance and Assurance

RG-419 provides:

```text
Verification
Validation
Independent Assurance
```

when continuing reliance requires renewed confidence.

---

# 61. Surveillance and Decision

RG-420 provides:

```text
Acceptance
Reliance
Suspension
Reinstatement
Revocation
Reopening
Closure
```

for post-closure decisions.

---

# 62. Revalidation

Revalidation MAY be required when:

```text
Material Change
Evidence Expiry
Model Change
Policy Change
Long Time Since Assurance
Risk Increase
```

Revalidation SHALL use current criteria.

---

# 63. Reverification

Reverification determines whether the continuing condition still satisfies defined requirements.

It SHALL not simply copy the original verification result.

---

# 64. Renewed Assurance

High-risk continued reliance MAY require renewed independent assurance.

```text
SURVEILLANCE
   ↓
REASSESSMENT
   ↓
RENEWED ASSURANCE
   ↓
RELIANCE DECISION
```

---

# 65. Periodic Reacceptance

Some accepted conditions MAY require periodic reacceptance.

Periodic reacceptance SHALL be a new decision.

Historical acceptance SHALL remain traceable.

---

# 66. Expiry

A surveillance programme MAY expire.

Expiry SHALL trigger:

```text
Review
Renewal
Termination
```

It SHALL not silently remove required monitoring.

---

# 67. Termination

Surveillance MAY terminate when:

```text
Reliance Ends
Subject Retired
Decision Superseded
Risk Removed
Policy No Longer Requires Surveillance
```

Termination SHALL be authorised.

---

# 68. Surveillance Escalation

Escalation triggers MAY include:

```text
Repeated Near-Threshold Events
Critical Monitoring Failure
Material Trend
Risk Increase
Repeated Findings
Condition Breach
Reliance Invalidity
```

---

# 69. Alert Fatigue

Post-closure surveillance SHOULD measure:

```text
Alert Volume
False Positives
Duplicate Alerts
Suppression
Response Time
Escalation Rate
```

Surveillance quality SHALL be reviewed if alert fatigue reduces meaningful detection.

---

# 70. Threshold Governance

Thresholds SHALL remain under RG-414 governance.

Changing thresholds may change:

```text
Detection Sensitivity
Risk
Reliance Confidence
Escalation
```

Threshold changes SHALL undergo impact assessment.

---

# 71. Baseline Change

A post-closure baseline change SHALL be treated as a governed change.

It SHALL identify:

```text
Original Baseline
New Baseline
Reason
Authority
Impact
Affected Reliance
```

---

# 72. Policy Change

A policy change MAY invalidate continuing reliance.

The system SHOULD identify closed decisions affected by the changed requirement.

---

# 73. Rule Change

A rule change MAY alter the interpretation of continuing validity.

Historical decisions SHALL retain the rule version under which they were made.

---

# 74. Model Change

A model version change MAY trigger:

```text
Impact Analysis
Regression Testing
Revalidation
Renewed Assurance
Reliance Review
```

---

# 75. Dependency Change

A material dependency change SHALL trigger impact analysis.

Examples:

```text
Provider Change
Version Change
Architecture Change
Service Level Change
Security Change
Ownership Change
```

---

# 76. Evidence Expiry

If critical evidence expires:

```text
EVIDENCE EXPIRED
   ↓
RELIANCE REVIEW
```

The system SHALL not silently treat expired evidence as current.

---

# 77. Authority Expiry

If authority supporting the original decision expires:

```text
AUTHORITY EXPIRED
   ↓
RELIANCE REVIEW
```

Existing technical state does not compensate for invalid decision authority.

---

# 78. Condition Breach

Acceptance conditions SHALL be monitored.

If breached:

```text
CONDITION BREACH
   ↓
ASSESS
   ↓
CONTINUE / SUSPEND / REOPEN
```

---

# 79. Surveillance and Materiality

A surveillance event SHALL be assessed under RG-415.

The system SHALL distinguish:

```text
NORMAL VARIATION
EARLY WARNING
NON-MATERIAL DEVIATION
MATERIAL REGRESSION
CRITICAL CONDITION
```

---

# 80. Surveillance and Closure

Closure SHALL not eliminate required post-closure surveillance.

Where surveillance is required, it becomes a continuing governance obligation.

---

# 81. Historical Reconstruction

The system SHALL be able to reconstruct:

```text
Original Acceptance
Original Closure
Surveillance Period
Events
Findings
Reassessments
Suspensions
Reinstatements
Revocations
Reopenings
```

---

# 82. Audit

Material surveillance events SHALL generate audit records:

```text
Surveillance Activated
Threshold Changed
Baseline Changed
Event Raised
Finding Created
Reliance Suspended
Reliance Reinstated
Decision Reopened
Surveillance Closed
```

---

# 83. Security

Surveillance systems SHALL be protected against:

```text
Signal Manipulation
Threshold Manipulation
Alert Suppression
Evidence Deletion
Unauthorised Disablement
```

---

# 84. Integrity

Post-closure surveillance records SHALL be immutable or tamper-evident.

Corrections SHALL preserve historical records.

---

# 85. Privacy

Surveillance SHALL follow:

```text
Least Privilege
Purpose Limitation
Data Minimisation
Retention
Controlled Disclosure
```

---

# 86. Continuity

Critical post-closure surveillance SHALL have continuity arrangements.

Examples:

```text
Redundant Monitoring
Alternate Data Source
Manual Surveillance
Backup Alert Route
```

---

# 87. Manual Surveillance

Manual surveillance SHALL identify:

```text
Owner
Method
Frequency
Evidence
Duration
Escalation
```

Manual monitoring shall not become an indefinite unmanaged workaround.

---

# 88. Testing

Post-closure surveillance SHALL test:

```text
Stable Condition
Threshold Breach
Trend Detection
Evidence Expiry
Authority Expiry
Control Failure
Dependency Change
Policy Change
Rule Change
Model Change
Monitoring Failure
Reliance Suspension
Reinstatement
Reopening
```

---

# 89. Negative Testing

The system SHALL verify:

```text
Surveillance failure ≠ healthy state
Expired evidence ≠ valid evidence
Expired authority ≠ valid authority
Missing monitoring data ≠ normal condition
Threshold change ≠ silent update
Closed case ≠ immune from reassessment
Reliance expiry ≠ continued reliance
Unverified change ≠ accepted continuation
```

---

# 90. Scenario Testing

Representative scenarios:

```text
Stable post-closure case
Early-warning trend
Critical control degradation
Evidence expiry
Authority revocation
Dependency replacement
Policy change
Model upgrade
Repeated minor findings
Material regression
Reliance suspension
Successful reinstatement
Closure followed by recurrence
Downstream reliance impact
```

---

# 91. Acceptance Criteria

EA-IMETA-PC-RG-421 is accepted when:

- post-closure surveillance is explicitly defined;
- continuing reliance has a validity basis;
- surveillance objects have controlled lifecycle;
- risk, control, evidence, authority and dependency surveillance are supported;
- regression surveillance is integrated with monitoring;
- reassessment triggers are explicit;
- suspension, revocation and reopening are distinct;
- downstream reliance can be identified;
- material invalidation can propagate through reliance relationships;
- evidence and authority expiry are detected;
- policy, rule, threshold and model changes can trigger impact analysis;
- renewed assurance/revalidation are supported;
- surveillance failure creates a visibility-gap condition;
- historical closure remains reconstructable;
- negative tests prevent false assurance;
- post-closure governance integrates with RG-414 through RG-420.

---

# 92. Next Step

The next logical artifact is the **PC-RG dependency, change-impact and propagation model**, because RG-421 establishes continuing reliance and identifies that changes in policy, rules, models, dependencies and accepted conditions can affect downstream decisions.

Provisional next artifact:

> **EA-IMETA-PC-RG-422 — DEPENDENCY, CHANGE-IMPACT & PROPAGATION MODEL**

This will define how a change is traced from its origin through affected controls, decisions, reliance relationships and closed cases.

---

# 93. Governing Principle

> **Closure ends a lifecycle stage, not the need for truth. Surveillance maintains visibility, continuing reliance remains conditional, and material change can reopen governance.**

The PC-RG architecture SHALL therefore preserve a controlled relationship between every closed decision and the continuing conditions upon which that decision remains trustworthy.

# END OF EA-IMETA-PC-RG-421
