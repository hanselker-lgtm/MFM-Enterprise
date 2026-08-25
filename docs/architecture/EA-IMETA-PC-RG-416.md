# EA-IMETA-PC-RG-416

## MONITORING, OBSERVABILITY & EARLY-WARNING MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-416 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Monitoring, Observability & Early-Warning Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-415 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how operational signals are continuously collected, interpreted, correlated and converted into controlled early-warning, regression and escalation responses |
| Architectural Boundary | Signal → Observation → Baseline → Threshold → Assessment → Alert → Risk → Response |

---

# 2. Purpose

EA-IMETA-PC-RG-416 defines the monitoring and observability architecture required to detect changes that may affect an accepted or closed condition.

RG-415 defines risk, materiality and escalation.

RG-416 defines **how evidence of changing conditions is detected in time to activate those mechanisms**.

The governing distinction is:

```text
MONITORING
= WHAT IS BEING WATCHED

OBSERVABILITY
= WHAT CAN BE UNDERSTOOD FROM SYSTEM BEHAVIOUR

SIGNAL
= RAW OBSERVED INFORMATION

OBSERVATION
= INTERPRETED MEASUREMENT

BASELINE
= APPROVED REFERENCE CONDITION

THRESHOLD
= DEFINED BOUNDARY

ALERT
= CONTROLLED NOTIFICATION OF A CONDITION

EARLY WARNING
= SIGNAL OF A DEVELOPING MATERIAL CONDITION
```

---

# 3. Core Principle

> **Monitoring shall detect; assessment shall interpret; governance shall decide.**

A monitoring signal SHALL not automatically be treated as proof of regression.

The required chain is:

```text
SIGNAL
   ↓
VALIDATE SIGNAL
   ↓
COMPARE BASELINE
   ↓
ASSESS MATERIALITY
   ↓
RISK EVALUATION
   ↓
ALERT / ESCALATION
   ↓
DECISION
```

---

# 4. Monitoring Scope

Monitoring MAY cover:

```text
SYSTEM HEALTH
CONTROL EFFECTIVENESS
DATA QUALITY
SECURITY
COMPLIANCE
PERFORMANCE
AVAILABILITY
INTEGRITY
WORKFLOW
AUTHORITY
EVIDENCE
RISK
DEPENDENCIES
AI / AGENT BEHAVIOUR
```

Each monitored subject SHALL have an explicit purpose.

---

# 5. Monitoring Object

Every material monitoring definition SHALL contain:

```text
Monitor ID
Name
Purpose
Subject
Owner
Signal Source
Metric
Baseline
Threshold
Frequency
Collection Method
Evaluation Rule
Alert Rule
Escalation Rule
Retention
Version
Status
```

---

# 6. Signal

A signal is raw information indicating that something occurred or changed.

Examples:

```text
CPU measurement
Response time
Failed authentication
Control test failure
Evidence expiry
Workflow delay
Data anomaly
Security event
Risk score change
AI output deviation
External dependency failure
```

Signals SHALL retain source and timestamp.

---

# 7. Observation

An observation is a validated interpretation of a signal.

Example:

```text
RAW SIGNAL:
Response time = 4.7 seconds

OBSERVATION:
Response time exceeds normal operating baseline.
```

Observation logic SHALL be versioned where material.

---

# 8. Signal Quality

Signals SHALL be assessed for:

```text
Completeness
Freshness
Accuracy
Source Reliability
Integrity
Availability
Duplication
Ordering
```

A failed monitoring source SHALL not automatically be interpreted as a healthy condition.

---

# 9. Monitoring States

A monitor MAY have:

```text
DEFINED
ACTIVE
PAUSED
DEGRADED
FAILED
SUSPENDED
RETIRED
```

A monitor in FAILED or DEGRADED state SHALL itself be visible to governance.

---

# 10. Monitoring Coverage

The system SHOULD report:

```text
Required Monitors
Active Monitors
Inactive Monitors
Failed Monitors
Degraded Monitors
Unmonitored Critical Areas
Expired Monitors
Coverage Gaps
```

A monitoring dashboard SHALL not imply coverage where no valid monitor exists.

---

# 11. Baseline

A baseline represents the approved reference condition.

Examples:

```text
Approved Configuration
Expected Performance
Accepted Risk Level
Normal Data Pattern
Control Pass Rate
Approved Model Version
Approved Workflow Behaviour
```

A baseline SHALL have:

```text
Baseline ID
Version
Scope
Owner
Effective Period
Source
Approval
```

---

# 12. Baseline Integrity

A baseline SHALL not change silently.

Material baseline changes SHALL be:

```text
Identified
Versioned
Approved
Audited
Impact Assessed
```

Changing a baseline may itself constitute a material change.

---

# 13. Baseline Types

Initial catalogue:

```text
CONFIGURATION BASELINE
PERFORMANCE BASELINE
RISK BASELINE
CONTROL BASELINE
DATA BASELINE
SECURITY BASELINE
WORKFLOW BASELINE
AUTHORITY BASELINE
MODEL BASELINE
COMPLIANCE BASELINE
```

---

# 14. Baseline Selection

The monitoring engine SHALL select the applicable baseline based on:

```text
Subject
Scope
Version
Time
Environment
Case
Policy
Risk Context
```

Using the wrong baseline can produce false assurance.

---

# 15. Thresholds

Thresholds SHALL be defined through the policy/rule model in RG-414.

Monitoring SHALL consume approved thresholds rather than inventing them.

Threshold types MAY include:

```text
ABSOLUTE
RELATIVE
RATE
TREND
DURATION
COUNT
PERCENTAGE
STATISTICAL
COMPOSITE
```

---

# 16. Threshold States

A monitored value MAY produce:

```text
NORMAL
WARNING
ACTION
CRITICAL
UNKNOWN
```

Threshold semantics SHALL be explicit.

---

# 17. Boundary Conditions

Thresholds SHALL define boundary behaviour.

Example:

```text
Threshold = 100

99.9  → NORMAL
100.0 → defined boundary outcome
100.1 → ACTION
```

The boundary SHALL not be left to implementation interpretation.

---

# 18. Static Thresholds

Static thresholds use fixed values.

Example:

```text
Failed authentication > 20 / hour
```

Static thresholds are appropriate where the acceptable boundary is stable.

---

# 19. Dynamic Thresholds

Dynamic thresholds MAY use:

```text
Historical Baseline
Rolling Average
Percentile
Seasonality
Trend
Peer Comparison
```

Dynamic thresholds SHALL be explainable and versioned.

---

# 20. Trend Detection

Monitoring SHALL support trends where a single observation is insufficient.

Examples:

```text
Continuous deterioration
Repeated near-threshold values
Increasing failure rate
Increasing remediation age
Declining control effectiveness
```

Trend logic SHALL define its observation window.

---

# 21. Rate-of-Change Detection

The system MAY monitor:

```text
Δ Value / Δ Time
```

or another approved rate measure.

Rapid change may be material even when the absolute value remains below a static threshold.

---

# 22. Anomaly Detection

An anomaly is an observation that differs materially from expected behaviour.

Anomaly detection MAY be:

```text
RULE BASED
STATISTICAL
PATTERN BASED
MODEL BASED
AI ASSISTED
```

An anomaly SHALL not automatically equal a confirmed regression.

---

# 23. AI-Assisted Detection

AI may assist with:

```text
Pattern Detection
Anomaly Classification
Correlation
Trend Identification
Early-Warning Suggestions
```

AI-generated alerts SHALL identify:

```text
Model
Model Version
Input Scope
Detection Method
Timestamp
Confidence / Uncertainty
```

AI detection does not replace governed materiality assessment.

---

# 24. Composite Indicators

Multiple signals MAY be combined.

Example:

```text
Performance degradation
+
Error increase
+
Customer impact
=
Potential material condition
```

Composite rules SHALL identify all contributing signals.

---

# 25. Correlation

Monitoring SHOULD correlate related signals.

Example:

```text
Authentication failures
        +
Identity-service latency
        +
Access denials
        ↓
Potential Identity Dependency Failure
```

Correlation reduces isolated-signal interpretation.

---

# 26. Alert

An alert is a controlled output indicating that a defined monitoring condition has occurred.

An alert SHALL contain:

```text
Alert ID
Monitor ID
Trigger
Observed Value
Expected Value
Severity
Timestamp
Subject
Baseline
Rule
Evidence
Correlation ID
Status
```

---

# 27. Alert Severity

Illustrative:

```text
INFO
WARNING
MAJOR
CRITICAL
```

Severity SHALL be linked to impact and governance consequences.

---

# 28. Alert Lifecycle

```text
RAISED
  ↓
ACKNOWLEDGED
  ↓
ASSESSED
  ↓
CONFIRMED / DISMISSED
  ↓
ACTIONED
  ↓
CLOSED
```

Possible exception:

```text
ESCALATED
```

An alert SHALL not be considered resolved merely because it was acknowledged.

---

# 29. Alert Deduplication

Repeated identical alerts SHALL be correlated or deduplicated where appropriate.

The system SHALL preserve the underlying evidence.

Example:

```text
100 identical signals
   ↓
1 incident / alert group
   +
100 source events retained
```

---

# 30. Alert Suppression

Suppression MAY be used only under controlled rules.

A suppression SHALL define:

```text
Reason
Scope
Start
End
Authority
Expected Effect
Audit
```

Critical alerts SHALL not be suppressed without explicit authority.

---

# 31. Alert Fatigue

The architecture SHOULD monitor:

```text
Alert Volume
False Positive Rate
Duplicate Rate
Acknowledgement Delay
Escalation Rate
Closure Time
Suppression Volume
```

Excessive alert volume is itself a control-quality issue.

---

# 32. Early Warning

An early warning indicates that a material condition may be developing.

Example:

```text
NORMAL
  ↓
NEAR THRESHOLD
  ↓
TREND DETERIORATION
  ↓
EARLY WARNING
  ↓
MATERIALITY ASSESSMENT
```

Early warning SHALL not automatically change lifecycle state.

---

# 33. Early-Warning Indicators

Examples:

```text
Increasing control failures
Repeated near-threshold events
Growing remediation backlog
Rising evidence expiry
Declining verification success
Increasing authority conflicts
Increasing dependency failures
Model drift indicators
```

---

# 34. Monitoring-to-Risk Relationship

The monitoring engine feeds risk assessment:

```text
MONITOR
  ↓
OBSERVATION
  ↓
MATERIALITY
  ↓
RISK
  ↓
ESCALATION
```

Monitoring SHALL not independently accept or reject risk.

---

# 35. Monitoring-to-Regression Relationship

The regression flow is:

```text
MONITORING SIGNAL
      ↓
CHANGE DETECTED
      ↓
REGRESSION ASSESSMENT
      ↓
MATERIAL?
 ┌────┴─────┐
NO          YES
 │           │
 ▼           ▼
MONITOR    REGRESSION
```

This preserves the distinction between change and material regression.

---

# 36. Monitoring-to-Remediation

Where a confirmed material condition exists:

```text
REGRESSION
   ↓
REMEDIATION
   ↓
REVALIDATION
```

Monitoring SHALL continue as defined during remediation.

---

# 37. Monitoring During Remediation

Remediation SHALL have dedicated monitoring where required.

Examples:

```text
Action Completion
Risk Reduction
Control Recovery
Error Rate
Residual Risk
Recurrence
```

A remediation action marked complete does not automatically restore the monitored baseline.

---

# 38. Post-Reacceptance Monitoring

After reacceptance:

```text
REACCEPTANCE
   ↓
CLOSED
   ↓
MONITORED
```

Enhanced monitoring MAY be required for a defined period.

This SHALL be policy-controlled.

---

# 39. Monitoring Frequency

Frequency SHALL be based on:

```text
Risk
Volatility
Materiality
Operational Need
Cost
Signal Availability
```

Possible frequencies:

```text
REAL TIME
MINUTE
HOURLY
DAILY
WEEKLY
MONTHLY
EVENT DRIVEN
```

---

# 40. Event-Driven Monitoring

Monitoring MAY be triggered by events:

```text
Configuration Change
New Deployment
Authority Change
Security Event
Evidence Expiry
Policy Change
Model Change
Dependency Change
```

Event-driven monitoring SHALL be correlated to the originating event.

---

# 41. Scheduled Monitoring

Scheduled monitors SHALL record:

```text
Schedule
Last Run
Next Run
Result
Failure
Duration
```

A missed scheduled execution SHALL be visible.

---

# 42. Monitoring SLA

Critical monitors MAY have execution SLAs.

Example:

```text
Monitor must execute every 5 minutes.
```

If the monitor misses its SLA:

```text
MONITOR HEALTH FAILURE
```

shall be generated.

---

# 43. Monitor Failure

Monitor failure SHALL not be treated as:

```text
NO PROBLEM
```

Instead:

```text
MONITOR FAILURE
   ↓
VISIBILITY GAP
   ↓
RISK ASSESSMENT
```

Critical monitoring failure may trigger escalation.

---

# 44. Blind Spots

The architecture SHALL support explicit identification of:

```text
UNMONITORED AREA
UNKNOWN SIGNAL
MISSING DATA
FAILED SENSOR
FAILED MONITOR
UNOBSERVABLE CONDITION
```

A blind spot SHALL be visible to risk governance.

---

# 45. Observability

Observability SHALL provide enough information to understand system behaviour.

Core dimensions:

```text
LOGS
METRICS
TRACES
EVENTS
STATE
DEPENDENCIES
```

Where applicable.

---

# 46. Logs

Logs SHALL support:

```text
Event Time
Actor / Service
Action
Outcome
Correlation ID
Error
Context
```

Logs SHALL not be treated as automatically trustworthy evidence without applicable integrity controls.

---

# 47. Metrics

Metrics SHALL define:

```text
Name
Unit
Source
Collection Frequency
Aggregation
Baseline
Threshold
Owner
Retention
```

---

# 48. Traces

Distributed traces SHOULD support:

```text
Request
Service
Dependency
Latency
Error
Correlation
```

This helps identify systemic failures.

---

# 49. Dependency Monitoring

Critical dependencies SHALL be monitored for:

```text
Availability
Latency
Error Rate
Integrity
Version
Certificate / Credential Status
Capacity
Change
```

---

# 50. Authority Monitoring

The system SHOULD monitor:

```text
Expired Roles
Expired Delegations
Authority Conflicts
SoD Violations
Emergency Access
Privileged Actions
```

Authority degradation may be a material governance condition.

---

# 51. Evidence Monitoring

Evidence monitoring SHALL include:

```text
Expiry
Integrity
Missing Links
Invalid Source
Staleness
Retention
Access Failure
```

---

# 52. Control Monitoring

Control monitoring MAY include:

```text
Control Test Results
Failure Rate
Test Recency
Coverage
Exception Rate
Remediation Aging
```

A declining control health indicator may generate early warning.

---

# 53. Workflow Monitoring

Workflow monitoring SHALL support:

```text
Queue Length
Task Age
Blocked Tasks
Failed Tasks
SLA Breaches
Escalations
Retries
Dead Letters
```

---

# 54. Risk Monitoring

Risk monitoring SHALL support:

```text
Risk Score
Residual Risk
Tolerance Breach
Risk Trend
Risk Concentration
Open Treatment
Overdue Treatment
```

---

# 55. Compliance Monitoring

Compliance monitoring MAY include:

```text
Obligation Status
Evidence Availability
Expiry
Control Status
Exceptions
Findings
```

---

# 56. Security Monitoring

Security monitoring SHALL support applicable:

```text
Authentication
Authorisation
Privilege
Data Access
Integrity
Threat
Audit
Agent Activity
```

---

# 57. AI / Model Monitoring

Where AI is material, monitoring SHOULD include:

```text
Model Version
Input Distribution
Output Distribution
Error Rate
Drift
Override Rate
Human Review Rate
Tool Usage
Permission Violations
Unexpected Behaviour
```

Model monitoring SHALL connect to the change and regression processes.

---

# 58. Model Drift

Model drift MAY be:

```text
DATA DRIFT
CONCEPT DRIFT
PERFORMANCE DRIFT
BEHAVIOURAL DRIFT
```

Material drift SHALL trigger assessment.

---

# 59. Change Detection

Material changes SHALL be detectable across:

```text
Code
Configuration
Data
Policy
Rules
Thresholds
Models
Dependencies
Authorities
Workflows
```

A change registry SHOULD provide the authoritative change reference.

---

# 60. Change Correlation

Monitoring SHOULD correlate observed changes with known changes.

Example:

```text
Deployment D-104
      +
Latency increase
      +
Error increase
      ↓
Potential deployment-related regression
```

Correlation is evidence for assessment, not automatic proof of causation.

---

# 61. Causation

The architecture SHALL distinguish:

```text
CORRELATION
```

from:

```text
CAUSATION
```

A monitoring signal may identify a relationship without proving cause.

Material causation claims SHALL require appropriate evidence.

---

# 62. False Positives

False positives SHALL be recorded.

They SHOULD be analysed to improve:

```text
Thresholds
Rules
Signal Quality
Correlation
Monitoring Coverage
```

Changes SHALL remain governed and auditable.

---

# 63. False Negatives

The architecture SHALL recognise that failure to generate an alert does not prove absence of a condition.

Testing SHALL include scenarios where:

```text
KNOWN MATERIAL CONDITION
```

must generate an alert.

---

# 64. Early-Warning Quality

Early-warning performance SHOULD be assessed through:

```text
Lead Time
Detection Rate
False Positive Rate
False Negative Rate
Time to Acknowledge
Time to Assess
Time to Escalate
```

---

# 65. Detection Lead Time

Lead time is:

```text
MATERIAL CONDITION
      ↑
      │
EARLY WARNING
      │
      ↓
DETECTION LEAD TIME
```

Longer useful lead time may improve governance response.

---

# 66. Alert-to-Action

The architecture SHOULD measure:

```text
Signal
 ↓
Alert
 ↓
Acknowledgement
 ↓
Assessment
 ↓
Escalation
 ↓
Action
```

Time spent at each stage SHALL be observable for critical monitoring.

---

# 67. Monitoring Ownership

Every monitor SHALL have an owner responsible for:

```text
Purpose
Availability
Thresholds
Review
False Positives
Coverage
Retirement
```

Ownership SHALL remain clear even when collection is automated.

---

# 68. Monitor Review

Monitors SHALL be reviewed:

```text
On Schedule
After Material Incident
After False-Negative Event
After Threshold Change
After System Change
After Risk Change
```

---

# 69. Monitor Versioning

Monitor definitions SHALL be versioned.

Changes to:

```text
Signal
Metric
Baseline
Threshold
Frequency
Rule
Alert
Escalation
```

SHALL create a controlled version change.

---

# 70. Monitoring Change Impact

A monitor change SHALL identify affected:

```text
Risks
Alerts
Regression Detection
Controls
Cases
Reports
SLAs
Escalations
```

---

# 71. Data Retention

Monitoring data retention SHALL balance:

```text
Audit Need
Trend Analysis
Forensics
Cost
Privacy
Regulation
```

Aggregated data SHALL not replace raw evidence where raw evidence is required for reconstruction.

---

# 72. Data Integrity

Monitoring data SHALL protect against:

```text
Loss
Alteration
Duplication
Reordering
Timestamp Manipulation
Unauthorised Deletion
```

---

# 73. Time Synchronisation

Material monitoring systems SHALL use a consistent authoritative time source.

Time differences SHALL be understood when correlating:

```text
Signals
Events
Logs
Traces
Audit
State Transitions
```

---

# 74. Monitoring Security

Monitoring infrastructure itself SHALL be protected.

Attackers may attempt to:

```text
Disable Monitoring
Alter Thresholds
Suppress Alerts
Delete Evidence
Spoof Signals
Manipulate Time
```

These threats SHALL be included in security testing.

---

# 75. Alert Routing

Alerts SHALL route according to:

```text
Severity
Scope
Risk
Owner
Time
Authority
```

Critical alerts SHALL not depend on a single individual where continuity requires redundancy.

---

# 76. Escalation Integration

Monitoring integrates with RG-415:

```text
ALERT
 ↓
MATERIALITY
 ↓
RISK
 ↓
ESCALATION
```

Escalation rules SHALL remain authoritative in the risk/policy architecture.

---

# 77. Workflow Integration

Monitoring events integrate with RG-411:

```text
MONITORING EVENT
      ↓
WORKFLOW
      ↓
ASSESSMENT TASK
      ↓
DECISION
```

---

# 78. State Integration

Monitoring integrates with RG-410 through controlled transitions:

```text
MONITORING
   ↓
CHANGE DETECTED
   ↓
REGRESSION ASSESSMENT
   ↓
STATE MACHINE
```

Monitoring SHALL not directly mutate state without the defined state transition.

---

# 79. Evidence Integration

Monitoring outputs SHALL create evidence where appropriate:

```text
Signal
 ↓
Observation
 ↓
Evidence
 ↓
Assessment
```

Evidence SHALL preserve source, timestamp and context.

---

# 80. Audit Integration

Material monitoring actions SHALL generate audit records:

```text
Monitor Changed
Threshold Changed
Alert Raised
Alert Suppressed
Escalation Triggered
Monitoring Failed
```

---

# 81. MFM Service Boundary

The conceptual implementation should include:

```text
Monitoring Service
Signal Collection Service
Metric Service
Baseline Service
Threshold Service
Alert Service
Correlation Service
Observability Service
Early-Warning Service
```

These integrate with:

```text
Risk
Policy
Workflow
State
Evidence
Audit
```

services.

---

# 82. API Concepts

Illustrative operations:

```text
registerMonitor()
activateMonitor()
pauseMonitor()
recordSignal()
createObservation()
evaluateThreshold()
createAlert()
acknowledgeAlert()
assessAlert()
suppressAlert()
correlateSignals()
createEarlyWarning()
getMonitorHealth()
getMonitoringCoverage()
```

These are architectural concepts, not implementation-specific commitments.

---

# 83. Monitoring Health

The system SHOULD expose a monitor-health score or status based on explicit factors:

```text
Execution Recency
Signal Availability
Data Quality
Threshold Validity
Baseline Validity
Processing Success
Alert Delivery
```

The scoring method SHALL be transparent.

---

# 84. Critical Monitoring Failure

A critical monitor failure MAY trigger:

```text
WARNING
RISK ASSESSMENT
ESCALATION
SUSPENSION
```

depending on the importance of the visibility it provides.

The response SHALL be risk-based.

---

# 85. Monitoring Continuity

Critical monitoring SHALL have continuity arrangements.

Examples:

```text
Redundant Collector
Secondary Data Source
Failover
Backfill
Manual Monitoring
Alternate Alert Route
```

---

# 86. Backfill

When monitoring is temporarily unavailable, backfill MAY reconstruct missing observations.

Backfilled data SHALL be marked as such.

It SHALL not be represented as real-time observation.

---

# 87. Unknown State

When monitoring cannot establish the actual condition:

```text
UNKNOWN
```

shall remain an explicit state.

Unknown SHALL not automatically be interpreted as:

```text
NORMAL
```

---

# 88. Manual Monitoring

Manual monitoring MAY be used as a compensating control.

It SHALL define:

```text
Owner
Frequency
Method
Evidence
Escalation
Duration
Review
```

---

# 89. Monitoring Exceptions

Exceptions SHALL define:

```text
Reason
Scope
Duration
Authority
Compensating Control
Review
Expiry
```

---

# 90. Testing

Monitoring SHALL be tested for:

```text
Normal Condition
Warning Threshold
Action Threshold
Critical Threshold
Boundary
Signal Loss
Data Corruption
Duplicate Signal
Delayed Signal
Out-of-Order Signal
False Positive
Known Material Condition
Monitor Failure
Alert Failure
Suppression
Recovery
```

---

# 91. Synthetic Monitoring

Critical services MAY use synthetic transactions.

Synthetic tests SHALL identify:

```text
Synthetic Test ID
Target
Frequency
Expected Result
Observed Result
Evidence
```

Synthetic monitoring SHALL be distinguishable from real user activity.

---

# 92. Chaos / Resilience Testing

Where appropriate, monitoring resilience MAY be tested by controlled failure scenarios:

```text
Dependency Failure
Collector Failure
Network Failure
Database Failure
Alert Route Failure
Clock Skew
```

Testing SHALL remain within approved operational boundaries.

---

# 93. Security Negative Testing

The monitoring architecture SHALL verify that:

```text
Unauthorised threshold change → BLOCK
Unauthorised suppression → BLOCK
Signal tampering → DETECT
Audit deletion → BLOCK / DETECT
Collector impersonation → DETECT
```

---

# 94. AI Monitoring Tests

AI monitoring SHALL test:

```text
Model Change
Drift
Unexpected Output
Tool Misuse
Permission Escalation
False Classification
Alert Suppression
Prompt Manipulation
```

---

# 95. Acceptance Criteria

EA-IMETA-PC-RG-416 is accepted when:

- monitoring, observability, signals and alerts are distinct;
- baselines are explicit and versioned;
- thresholds are governed by policy/rule logic;
- signal quality is assessed;
- monitor failures create visibility-risk awareness;
- early warnings are distinguishable from confirmed regressions;
- alerts have controlled lifecycle;
- alert suppression is governed;
- trend and anomaly detection are supported;
- critical dependencies are monitored;
- AI/model monitoring is addressed;
- monitoring changes have impact analysis;
- unknown conditions remain explicit;
- monitoring integrates with risk, workflow, state, evidence and audit;
- positive and negative monitoring tests exist.

---

# 96. Next Step

The next logical artifact is the **PC-RG incident, finding and exception management model**, because monitoring can now detect and raise conditions, while the architecture needs a controlled object for turning those conditions into findings, incidents, exceptions, ownership and resolution.

Provisional next artifact:

> **EA-IMETA-PC-RG-417 — FINDING, INCIDENT & EXCEPTION MANAGEMENT MODEL**

This will establish the controlled operational object between detection and remediation.

---

# 97. Governing Principle

> **Monitoring provides visibility, observability provides understanding, early warning provides lead time, and governance determines the response.**

The PC-RG architecture SHALL never treat absence of an alert as proof that no material condition exists.

# END OF EA-IMETA-PC-RG-416
