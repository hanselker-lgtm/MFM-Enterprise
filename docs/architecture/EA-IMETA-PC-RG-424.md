# EA-IMETA-PC-RG-424

## CONFIGURATION, BASELINE & STATE-INTEGRITY MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-424 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Configuration, Baseline & State-Integrity Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-423 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how approved, released, deployed and observed states are established, compared, reconciled and protected against unauthorised or unexplained drift |
| Architectural Boundary | Requirement → Approved Baseline → Release → Deployed State → Observed State → Reconciliation → Integrity Decision |

---

# 2. Purpose

EA-IMETA-PC-RG-424 defines the authoritative relationship between what an environment **should be**, what was **approved**, what was **released**, what was **deployed**, and what is **actually observed**.

RG-423 controls change, release and deployment.

RG-424 establishes **state integrity after and across deployment**.

The architecture SHALL distinguish:

```text
APPROVED STATE
= GOVERNED STATE AUTHORISED BY THE APPLICABLE AUTHORITY

BASELINE
= VERSIONED REPRESENTATION OF AN APPROVED CONDITION

RELEASE STATE
= STATE EMBODIED BY AN APPROVED RELEASE

DEPLOYED STATE
= STATE ACTUALLY INTRODUCED INTO A TARGET ENVIRONMENT

OBSERVED STATE
= STATE MEASURED OR DISCOVERED FROM THE ACTUAL ENVIRONMENT

DRIFT
= MATERIAL DIFFERENCE BETWEEN EXPECTED AND OBSERVED STATE

RECONCILIATION
= CONTROLLED PROCESS FOR EXPLAINING, CORRECTING OR ACCEPTING A DIFFERENCE

STATE INTEGRITY
= JUSTIFIED CONFIDENCE THAT THE ACTUAL STATE IS AUTHORISED, TRACEABLE AND WITHIN GOVERNED BOUNDARIES
```

---

# 3. Core Principle

> **The approved state defines what is authorised; the deployed state records what was introduced; the observed state establishes what actually exists; reconciliation determines whether differences are authorised, understood and acceptable.**

The governing chain is:

```text
REQUIREMENT
      ↓
APPROVED CONFIGURATION
      ↓
BASELINE
      ↓
RELEASE
      ↓
DEPLOYMENT
      ↓
OBSERVED STATE
      ↓
STATE COMPARISON
      ↓
DRIFT / NO DRIFT
      ↓
RECONCILIATION
      ↓
ACCEPT / REMEDIATE / ESCALATE
```

---

# 4. State Integrity Object

Every material state-integrity assessment SHALL be represented as a controlled object.

Minimum attributes:

```text
State Integrity ID
Subject
Environment
Baseline ID
Baseline Version
Release ID
Observed State Reference
Comparison Method
Differences
Drift Classification
Risk
Materiality
Evidence
Owner
Reviewer
Decision
Timestamp
Validity
```

---

# 5. Configuration Object

A configuration object represents a governed property of a system, service, process, model or environment.

Minimum attributes MAY include:

```text
Configuration ID
Name
Type
Value / Reference
Owner
Version
Environment
Source
Authority
Effective Time
Classification
Integrity Metadata
```

---

# 6. Configuration Types

Examples:

```text
APPLICATION CONFIGURATION
INFRASTRUCTURE CONFIGURATION
NETWORK CONFIGURATION
SECURITY CONFIGURATION
DATABASE CONFIGURATION
ACCESS CONFIGURATION
POLICY CONFIGURATION
RULE CONFIGURATION
MODEL CONFIGURATION
MONITORING CONFIGURATION
THRESHOLD CONFIGURATION
INTEGRATION CONFIGURATION
WORKFLOW CONFIGURATION
```

---

# 7. Configuration Lifecycle

```text
DEFINED
   ↓
REVIEWED
   ↓
APPROVED
   ↓
BASELINED
   ↓
RELEASED
   ↓
DEPLOYED
   ↓
OBSERVED
   ↓
RECONCILED
```

Alternative states:

```text
DRAFT
SUPERSEDED
EXPIRED
QUARANTINED
UNAUTHORISED
RETIRED
```

---

# 8. Configuration Authority

Every material configuration SHALL have an identified authority or governing source.

Authority MAY derive from:

```text
Policy
Standard
Architecture
Approved Change
Security Requirement
Regulatory Requirement
Operational Decision
```

---

# 9. Configuration Ownership

Every material configuration SHALL identify:

```text
Business Owner
Technical Owner
Operational Owner
Approval Authority
```

Not every configuration requires four distinct persons, but accountability SHALL remain explicit.

---

# 10. Configuration Version

Material configuration changes SHALL produce a new version.

Historical versions SHALL remain reconstructable.

---

# 11. Configuration Immutability

Approved configuration baselines SHALL be immutable.

Modification SHALL occur through a governed change process.

---

# 12. Baseline Object

A baseline is a controlled representation of an approved state at a defined point in time.

Minimum attributes:

```text
Baseline ID
Scope
Version
Components
Configuration References
Release References
Dependencies
Approval
Effective Time
Expiry
Integrity Metadata
```

---

# 13. Baseline Types

Examples:

```text
ARCHITECTURE BASELINE
CONFIGURATION BASELINE
SECURITY BASELINE
COMPLIANCE BASELINE
PERFORMANCE BASELINE
DATA BASELINE
MODEL BASELINE
RELEASE BASELINE
OPERATIONAL BASELINE
POST-CLOSURE BASELINE
```

---

# 14. Baseline Lifecycle

```text
DRAFT
   ↓
REVIEWED
   ↓
APPROVED
   ↓
ACTIVE
   ↓
SUPERSEDED
   ↓
ARCHIVED
```

---

# 15. Baseline Approval

A baseline SHALL identify:

```text
Criteria
Evidence
Authority
Approval
Version
Effective Time
```

---

# 16. Baseline Scope

A baseline SHALL define:

```text
Included Components
Excluded Components
Environment
Dependencies
Assumptions
Validity
```

---

# 17. Baseline Granularity

Baselines MAY exist at:

```text
ENTERPRISE
DOMAIN
SERVICE
APPLICATION
COMPONENT
ENVIRONMENT
DEVICE
MODEL
DATASET
PROCESS
CONTROL
```

The level SHALL be appropriate to the governance objective.

---

# 18. Baseline Composition

A baseline MAY contain:

```text
Configuration
Versions
Dependencies
Rules
Thresholds
Permissions
Policies
Interfaces
Monitoring
```

---

# 19. Baseline Reference

Every material deployment SHALL reference the baseline against which the deployment is evaluated.

---

# 20. Approved State

The approved state represents the authorised target condition.

```text
APPROVED STATE
      ↓
EXPECTED CONDITION
```

It SHALL not be inferred solely from the actual environment.

---

# 21. Release State

The release state represents the exact artefacts and configuration intended for deployment.

```text
RELEASE
=
APPROVED DEPLOYABLE REPRESENTATION
```

---

# 22. Deployed State

The deployed state represents what the deployment process actually introduced.

It SHALL be recorded independently of the release definition.

---

# 23. Observed State

Observed state represents evidence collected from the environment.

Sources MAY include:

```text
Configuration Discovery
Runtime Inspection
Monitoring
Inventory
Logs
Telemetry
Automated Scanning
Manual Inspection
```

---

# 24. State Comparison

The architecture SHALL support:

```text
APPROVED
   ↔
RELEASE
   ↔
DEPLOYED
   ↔
OBSERVED
```

Differences SHALL be classified.

---

# 25. Comparison Types

Possible comparisons:

```text
APPROVED vs RELEASE
RELEASE vs DEPLOYED
DEPLOYED vs OBSERVED
APPROVED vs OBSERVED
BASELINE vs CURRENT
```

---

# 26. State Difference

A difference SHALL identify:

```text
Object
Expected Value
Actual Value
Source
Timestamp
Severity
Classification
Evidence
```

---

# 27. Drift

Drift occurs when the observed state differs from the approved or governed state.

Drift SHALL be classified as:

```text
EXPECTED
AUTHORISED
TEMPORARY
UNAUTHORISED
UNKNOWN
TOLERATED
MATERIAL
CRITICAL
```

---

# 28. Expected Drift

Some systems naturally change within defined boundaries.

Examples:

```text
Dynamic Runtime Values
Temporary Capacity
Ephemeral Resources
Operational Counters
```

Expected variation SHALL not automatically be treated as integrity failure.

---

# 29. Authorised Drift

Authorised drift occurs where a governed exception or approved operational condition permits deviation.

It SHALL reference:

```text
Authority
Scope
Duration
Condition
```

---

# 30. Temporary Drift

Temporary drift SHALL have:

```text
Start
End
Owner
Reason
Restoration
```

Temporary drift SHALL not become permanent through neglect.

---

# 31. Unauthorised Drift

Unauthorised drift SHALL trigger:

```text
Alert
Investigation
Risk Assessment
Remediation / Reconciliation
```

as appropriate.

---

# 32. Unknown Drift

Where the cause or legitimacy of a difference is unknown:

```text
DRIFT = UNKNOWN
```

Unknown drift SHALL not automatically be accepted.

---

# 33. Material Drift

Material drift SHALL be evaluated against:

```text
Risk
Criticality
Security
Compliance
Reliance
Control
Decision Impact
```

---

# 34. Critical Drift

Critical drift MAY require:

```text
Immediate Containment
Suspension
Rollback
Incident
Escalation
Reassessment
```

---

# 35. Drift Detection

Drift detection MAY be:

```text
CONTINUOUS
SCHEDULED
EVENT-DRIVEN
MANUAL
```

Frequency SHALL be risk-based.

---

# 36. Drift Detection Sources

Sources MAY include:

```text
Configuration Management
Asset Inventory
Runtime Discovery
Security Scanning
Monitoring
Deployment Records
Version Control
Integrity Checks
```

---

# 37. Drift Detection Evidence

Every material drift event SHALL record:

```text
Detection Method
Observed Value
Expected Value
Timestamp
Source
Evidence
```

---

# 38. Drift Thresholds

Thresholds SHALL be governed.

Examples:

```text
VALUE DIFFERENCE
VERSION DIFFERENCE
COUNT DIFFERENCE
TIME DIFFERENCE
PERFORMANCE DIFFERENCE
CONFIGURATION DIFFERENCE
```

---

# 39. Drift Suppression

Suppression MAY be permitted only through governed rules.

Suppression SHALL identify:

```text
Rule
Scope
Reason
Authority
Start
End
```

Silent suppression SHALL be prohibited.

---

# 40. Drift Alerting

Alerts MAY be classified:

```text
INFO
WARNING
HIGH
CRITICAL
```

Severity SHALL reflect impact, not merely detection frequency.

---

# 41. Reconciliation

Reconciliation determines what action should be taken for a difference.

Possible outcomes:

```text
ACCEPT AS AUTHORISED
RESTORE BASELINE
UPDATE BASELINE
CREATE EXCEPTION
REMEDIATE
ROLLBACK
ESCALATE
INVESTIGATE
```

---

# 42. Reconciliation Workflow

```text
DIFFERENCE
   ↓
CLASSIFY
   ↓
ASSESS
   ↓
IDENTIFY CAUSE
   ↓
AUTHORISE RESPONSE
   ↓
CORRECT / ACCEPT
   ↓
VERIFY
   ↓
CLOSE
```

---

# 43. Reconciliation Authority

Reconciliation SHALL require authority appropriate to:

```text
Risk
Materiality
Scope
Security
Compliance
```

---

# 44. Baseline Update

A baseline SHALL only be updated through governed change.

```text
OBSERVED CHANGE
   ↓
IMPACT ASSESSMENT
   ↓
CHANGE APPROVAL
   ↓
NEW BASELINE
```

Observed reality alone does not automatically become the new approved state.

---

# 45. State Acceptance

A state may be accepted when:

```text
Difference Explained
+
Authority Valid
+
Risk Acceptable
+
Evidence Sufficient
```

---

# 46. State Rejection

A state SHALL be rejected where:

```text
Unauthorised
Materially Unsafe
Non-Compliant
Unsupported
Evidence Insufficient
```

---

# 47. State Quarantine

A suspicious state MAY be quarantined.

Quarantine SHALL define:

```text
Scope
Reason
Owner
Controls
Duration
Exit Criteria
```

---

# 48. State Integrity Decision

The state-integrity decision MAY be:

```text
VALID
VALID WITH CONDITIONS
DRIFT ACCEPTED
INVALID
UNKNOWN
REQUIRES RECONCILIATION
```

---

# 49. State Integrity vs Availability

A system may be available while its configuration is invalid.

```text
AVAILABLE
≠
GOVERNED
```

Availability SHALL not substitute for state integrity.

---

# 50. State Integrity vs Security

A system may be secure against current threats but still violate the approved configuration baseline.

Security and state integrity SHALL remain related but distinct.

---

# 51. State Integrity vs Compliance

Compliance may depend on configuration state.

A configuration difference MAY create a compliance impact even where the system continues to operate.

---

# 52. State Integrity vs Reliability

Operational reliability SHALL not automatically establish configuration integrity.

---

# 53. Configuration Drift and Regression

Drift MAY be a regression signal.

```text
DRIFT
 ↓
ASSESS
 ↓
REGRESSION?
```

---

# 54. Configuration Drift and Findings

Material drift MAY create a finding under RG-417.

---

# 55. Configuration Drift and Incidents

Critical drift MAY create an incident under RG-417.

---

# 56. Configuration Drift and Remediation

RG-418 SHALL govern corrective action where drift requires remediation.

---

# 57. Configuration Drift and Assurance

RG-419 SHALL provide independent assurance where required.

---

# 58. Configuration Drift and Decision

RG-420 SHALL govern decisions regarding:

```text
Acceptance
Suspension
Revocation
Reopening
Closure
```

---

# 59. Configuration Drift and Post-Closure Reliance

RG-421 SHALL identify closed decisions whose continuing reliance may be affected by state drift.

---

# 60. Configuration Drift and Change Impact

RG-422 SHALL identify dependencies and propagation paths affected by state changes.

---

# 61. Configuration Drift and Deployment

RG-423 SHALL provide deployment records for comparison with observed state.

---

# 62. State Integrity Chain

The integrated chain is:

```text
REQUIREMENT
   ↓
APPROVED BASELINE
   ↓
RELEASE
   ↓
DEPLOYMENT
   ↓
OBSERVED STATE
   ↓
DRIFT DETECTION
   ↓
RECONCILIATION
   ↓
ASSURANCE / DECISION
```

---

# 63. Configuration Source of Truth

Every material configuration SHALL identify its authoritative source.

Examples:

```text
Version Control
Configuration Repository
Policy Repository
Approved Database
Authoritative Registry
```

There SHALL be no ambiguity about which source defines the approved value.

---

# 64. Multiple Sources

Where multiple systems represent the same configuration, precedence SHALL be defined.

```text
SOURCE A
   ↓ precedence
SOURCE B
   ↓
OBSERVED
```

Conflicts SHALL be detected.

---

# 65. Source Conflict

If authoritative sources disagree:

```text
SOURCE CONFLICT
   ↓
BLOCK / ESCALATE
```

No arbitrary source SHALL silently win.

---

# 66. Configuration Ownership Conflict

If ownership is unclear:

```text
OWNERSHIP UNKNOWN
   ↓
GOVERNANCE REVIEW
```

---

# 67. Configuration Dependency

Configuration may depend on:

```text
Version
Environment
Hardware
Network
Policy
Secret
Certificate
External Service
```

Dependency context SHALL be preserved.

---

# 68. Configuration Secrets

Secrets SHALL not be exposed in ordinary configuration comparisons.

Comparisons MAY use:

```text
Presence
Reference
Hash
Metadata
```

instead of plaintext values.

---

# 69. Credential State

Material credential configuration SHALL track:

```text
Issuer
Validity
Scope
Expiry
Rotation
Revocation
```

---

# 70. Certificate State

Certificate drift MAY include:

```text
Wrong Certificate
Expired Certificate
Wrong Issuer
Unexpected Key
Wrong Scope
```

---

# 71. Permission State

Access configuration SHALL support comparison of:

```text
Expected Role
Actual Role
Expected Privilege
Actual Privilege
```

Unauthorised privilege expansion SHALL be high priority.

---

# 72. Network State

Network configuration MAY include:

```text
Routes
Ports
Firewall Rules
Endpoints
Segmentation
Certificates
```

---

# 73. Application State

Application configuration MAY include:

```text
Version
Feature Flags
Environment Variables
Runtime Parameters
Dependencies
Endpoints
```

---

# 74. Database State

Database state MAY include:

```text
Schema
Version
Permissions
Configuration
Replication
Backup
Extensions
```

---

# 75. Model State

AI/model state MAY include:

```text
Model Version
Weights / Artefact Reference
Prompt Configuration
Safety Configuration
Tool Permissions
Thresholds
Data Version
Evaluation Baseline
```

---

# 76. Model Drift

Model drift MAY include:

```text
Version Change
Performance Change
Data Drift
Concept Drift
Output Drift
Configuration Drift
```

Material model drift SHALL trigger RG-421 / RG-422 reassessment where applicable.

---

# 77. Policy State

Policy configuration SHALL identify:

```text
Policy Version
Effective Date
Scope
Approval
Superseded Version
```

---

# 78. Rule State

Rules SHALL identify:

```text
Rule ID
Version
Threshold
Scope
Effective Time
Authority
```

---

# 79. Threshold State

Thresholds SHALL be versioned.

Changing a threshold MAY change the behaviour of:

```text
Monitoring
Alerts
Risk
State Transitions
Acceptance
```

---

# 80. Monitoring Configuration

Monitoring itself SHALL be baselined where material.

A disabled monitor may represent a state-integrity failure.

---

# 81. Monitoring Coverage

State-integrity monitoring SHALL identify coverage gaps.

```text
KNOWN STATE
   ↓
MONITORED?
 ┌───┴───┐
YES     NO
 │       │
 ▼       ▼
VALID    GAP
```

---

# 82. Blind State

A blind state is a state for which actual condition cannot currently be established.

Blind states SHALL be visible.

---

# 83. Blind State Risk

Blind state risk SHALL consider:

```text
Criticality
Duration
Reliance
Security
Compliance
Observability
```

---

# 84. State Discovery

Discovery methods MAY include:

```text
API
Agent
Scanner
Inventory
Configuration Query
Manual Inspection
Telemetry
```

---

# 85. Discovery Integrity

Discovery mechanisms themselves SHALL be trusted appropriately.

If discovery is unreliable:

```text
OBSERVED STATE CONFIDENCE ↓
```

---

# 86. State Confidence

State observations MAY carry:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

confidence.

Confidence SHALL be evidence-based.

---

# 87. State Evidence

Material state assessments SHALL retain:

```text
Source
Method
Timestamp
Observed Value
Expected Value
Comparison
Conclusion
```

---

# 88. Snapshot

A state snapshot MAY capture the state at a specific time.

Snapshots SHALL identify:

```text
Snapshot ID
Timestamp
Environment
Scope
Source
Integrity
```

---

# 89. State Timeline

The system SHOULD support:

```text
STATE T0
  ↓
CHANGE
  ↓
STATE T1
  ↓
CHANGE
  ↓
STATE T2
```

This supports historical reconstruction.

---

# 90. State Reconstruction

The architecture SHALL support determining:

```text
What was approved?
What was deployed?
What was observed?
When did drift begin?
What changed?
Who authorised it?
```

---

# 91. State Integrity and Time

Validity SHALL consider:

```text
Effective Time
Observation Time
Deployment Time
Approval Time
Expiry Time
```

---

# 92. Temporal Drift

A difference may be legitimate during one period and invalid during another.

Time SHALL therefore be part of drift evaluation.

---

# 93. State Transition

A state transition SHALL identify:

```text
Previous State
New State
Trigger
Authority
Evidence
Timestamp
```

---

# 94. Unauthorised State Transition

Unauthorised transitions SHALL generate:

```text
Alert
Finding / Incident
Risk Assessment
```

as applicable.

---

# 95. State Reconciliation Metrics

The system SHOULD report:

```text
Drift Events
Unauthorised Drift
Unknown Drift
Mean Reconciliation Time
Repeated Drift
Baseline Exceptions
Blind States
State Integrity Failures
```

---

# 96. Drift Trend

Repeated drift in the same area SHALL trigger root-cause analysis.

```text
DRIFT
 ↓
REPEATED
 ↓
SYSTEMIC?
```

---

# 97. Systemic Drift

Systemic drift may indicate:

```text
Weak Change Control
Poor Automation
Incorrect Baseline
Operational Workaround
Inadequate Ownership
Faulty Monitoring
```

Systemic drift SHALL be escalated.

---

# 98. Configuration Debt

Persistent ungoverned configuration differences MAY constitute configuration debt.

Configuration debt SHALL be visible and risk-assessed.

---

# 99. Baseline Debt

A baseline that no longer reflects intended architecture SHALL be reviewed.

The answer SHALL not automatically be to accept drift.

---

# 100. State Integrity Review

Periodic review MAY evaluate:

```text
Baseline Accuracy
Drift
Ownership
Coverage
Monitoring
Exceptions
Reconciliation
```

---

# 101. State Integrity Assurance

High-risk environments MAY require independent assurance of:

```text
Baseline
Discovery
Comparison
Reconciliation
```

---

# 102. Automated State Integrity

Automation MAY perform deterministic comparisons.

It SHALL retain:

```text
Rule Version
Input
Expected State
Observed State
Result
Timestamp
```

---

# 103. AI-Assisted State Analysis

AI MAY assist with:

```text
Difference Classification
Anomaly Detection
Root-Cause Suggestions
Impact Summaries
```

AI conclusions SHALL be distinguishable from deterministic comparison results.

---

# 104. AI State Governance

Material AI-assisted state decisions SHALL retain:

```text
Model
Version
Inputs
Output
Human Review where required
Final Decision
```

---

# 105. State Integrity API Concepts

Illustrative operations:

```text
createBaseline()
approveBaseline()
captureSnapshot()
discoverState()
compareState()
classifyDrift()
createReconciliation()
approveReconciliation()
restoreBaseline()
updateBaseline()
quarantineState()
verifyState()
closeIntegrityEvent()
```

---

# 106. MFM Service Boundary

The conceptual implementation should include:

```text
Configuration Service
Baseline Service
State Discovery Service
State Comparison Service
Drift Detection Service
Reconciliation Service
Integrity Assessment Service
Configuration Source Service
Snapshot Service
```

These integrate with:

```text
Change
Release
Deployment
Dependency
Impact
Risk
Policy
Authority
Evidence
Monitoring
Finding
Incident
Remediation
Assurance
Decision
Reliance
State
Audit
```

---

# 107. Security

Configuration and state-integrity data SHALL be protected against:

```text
Unauthorised Modification
Baseline Manipulation
Drift Concealment
State Spoofing
Evidence Substitution
Privilege Abuse
```

---

# 108. Integrity Protection

Baselines and material state snapshots SHOULD use tamper-evident mechanisms.

---

# 109. Access Control

Access to configuration data SHALL follow:

```text
Least Privilege
Need to Know
Role Separation
Audit
```

---

# 110. Audit

Material state actions SHALL generate audit events:

```text
Baseline Created
Baseline Approved
Configuration Changed
Snapshot Captured
Drift Detected
Drift Accepted
Reconciliation Started
Baseline Restored
Baseline Updated
State Quarantined
Integrity Decision Issued
```

---

# 111. Failure Handling

If state discovery fails:

```text
STATE UNKNOWN
   ↓
VISIBILITY GAP
   ↓
RISK ASSESSMENT
```

The system SHALL not assume the approved state remains present.

---

# 112. Discovery Failure

Repeated discovery failure SHALL be treated as a governance concern where observability is material.

---

# 113. Baseline Corruption

If the baseline is suspected to be corrupted:

```text
BASELINE INVALID
   ↓
QUARANTINE
   ↓
RESTORE TRUSTED VERSION
   ↓
REASSESS
```

---

# 114. State Conflict

If approved, deployed and observed states conflict:

```text
APPROVED
   ≠
DEPLOYED
   ≠
OBSERVED
```

the conflict SHALL be explicitly assessed.

---

# 115. Unknown State

Where actual state cannot be determined:

```text
STATE = UNKNOWN
```

Unknown state SHALL trigger risk-based treatment.

---

# 116. Testing

The architecture SHALL test:

```text
Baseline Creation
Baseline Approval
Configuration Versioning
Release Comparison
Deployment Comparison
Observed State
Drift Detection
Authorised Drift
Unauthorised Drift
Unknown Drift
Reconciliation
Rollback
Baseline Update
State Snapshot
State Reconstruction
```

---

# 117. Negative Testing

The system SHALL verify:

```text
Unapproved baseline → BLOCK
Unauthorised configuration → FLAG
Unknown state → NOT VALID
Expired baseline → REVIEW
Silent baseline update → BLOCK
Suppressed drift without authority → BLOCK
Missing observation → VISIBILITY GAP
Conflicting sources → ESCALATE
Wrong release → DRIFT
Wrong version → DRIFT
Unauthorised privilege → HIGH-PRIORITY DRIFT
```

---

# 118. Scenario Testing

Representative scenarios:

```text
Clean deployment
Expected runtime drift
Authorised temporary drift
Unauthorised configuration change
Unknown state
Expired certificate
Unexpected privilege expansion
Wrong application version
Model upgrade
Threshold change
Monitoring disabled
Baseline corruption
Rollback
Partial deployment
Multiple authoritative sources
Repeated configuration drift
Post-closure drift affecting reliance
```

---

# 119. Acceptance Criteria

EA-IMETA-PC-RG-424 is accepted when:

- approved, release, deployed and observed states are distinct;
- baselines are versioned and governed;
- material configurations have ownership and authority;
- state comparisons are supported;
- drift is classified;
- authorised, temporary, unauthorised and unknown drift are distinguished;
- reconciliation is controlled;
- baseline changes require governed change;
- blind states are visible;
- state confidence is represented;
- state history can be reconstructed;
- configuration, model, policy, rule, threshold and monitoring states are supported;
- secrets are protected;
- AI-assisted analysis is governed;
- discovery failure does not imply healthy state;
- historical baselines remain reconstructable;
- integration with RG-421 through RG-423 is maintained;
- negative tests prevent silent state corruption and unauthorised drift.

---

# 120. Next Step

The next logical artifact is the **PC-RG integrity monitoring, reconciliation and continuous control model**, because RG-424 establishes the authoritative state and baseline model, while the architecture now needs to define how state integrity is continuously monitored, how deviations are correlated and how automated and human controls maintain the approved state over time.

Provisional next artifact:

> **EA-IMETA-PC-RG-425 — CONTINUOUS INTEGRITY MONITORING & RECONCILIATION CONTROL MODEL**

This will establish the continuous-control layer above configuration, baseline and state integrity.

---

# 121. Governing Principle

> **The approved state defines what is authorised; the observed state defines what is real; the difference between them must be visible; and reconciliation must be governed rather than improvised.**

The PC-RG architecture SHALL therefore preserve a continuous, auditable relationship between intended state, released state, deployed state and observed state.

# END OF EA-IMETA-PC-RG-424
