# EA-IMETA-PC-RG-423

## CHANGE CONTROL, RELEASE & DEPLOYMENT GOVERNANCE MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-423 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Change Control, Release & Deployment Governance Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-422 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define controlled governance from change request through approval, implementation, release, deployment, observation, rollback and closure |
| Architectural Boundary | Change Request → Assessment → Approval → Build → Test → Release → Deployment → Observation → Acceptance / Rollback → Closure |

---

# 2. Purpose

EA-IMETA-PC-RG-423 defines the execution-control architecture for material changes.

RG-422 establishes dependency, impact and propagation analysis.

RG-423 establishes **how approved changes are safely controlled through implementation and release without losing traceability to their governance context**.

The architecture SHALL distinguish:

```text
CHANGE REQUEST
= PROPOSAL TO ALTER A CONTROLLED CONDITION

CHANGE APPROVAL
= AUTHORISED PERMISSION TO IMPLEMENT

RELEASE
= CONTROLLED PACKAGE / VERSION MADE READY FOR DEPLOYMENT

DEPLOYMENT
= ACTUAL INTRODUCTION INTO A TARGET ENVIRONMENT

OBSERVATION
= POST-DEPLOYMENT EVALUATION

ROLLBACK
= CONTROLLED REVERSION OR ALTERNATIVE RECOVERY ACTION

CLOSURE
= FORMAL END OF THE CHANGE LIFECYCLE
```

---

# 3. Core Principle

> **Approval authorises implementation; release authorises a specific artefact; deployment changes the environment; observation establishes actual behaviour; closure records the governed outcome.**

The governing chain is:

```text
CHANGE REQUEST
      ↓
CLASSIFICATION
      ↓
IMPACT / RISK ASSESSMENT
      ↓
AUTHORITY REVIEW
      ↓
APPROVAL
      ↓
IMPLEMENTATION
      ↓
TEST / VERIFICATION
      ↓
RELEASE
      ↓
DEPLOYMENT
      ↓
POST-DEPLOYMENT OBSERVATION
      ↓
ACCEPT / ROLLBACK / REMEDIATE
      ↓
CLOSURE
```

---

# 4. Change Request Object

Every material change SHALL be represented as a controlled request.

Minimum attributes:

```text
Change Request ID
Subject
Requester
Reason
Business / Technical Objective
Scope
Change Type
Risk
Materiality
Dependencies
Impact Assessment
Implementation Plan
Test Plan
Rollback Plan
Release Reference
Deployment Targets
Authority
Schedule
Status
Version
```

---

# 5. Change Request Lifecycle

```text
DRAFT
   ↓
SUBMITTED
   ↓
TRIAGED
   ↓
ASSESSED
   ↓
APPROVED
   ↓
IMPLEMENTING
   ↓
TESTING
   ↓
READY FOR RELEASE
   ↓
RELEASED
   ↓
DEPLOYED
   ↓
OBSERVING
   ↓
ACCEPTED
   ↓
CLOSED
```

Alternative states:

```text
REJECTED
DEFERRED
BLOCKED
CANCELLED
FAILED
ROLLED BACK
REOPENED
```

---

# 6. Change Classification

Changes SHALL be classified by:

```text
TYPE
RISK
MATERIALITY
ENVIRONMENT
URGENCY
DEPENDENCY CRITICALITY
```

Classification SHALL determine required governance depth.

---

# 7. Standard Change

A standard change is a predefined, repeatable change with an approved method and known risk.

Standard changes SHALL have:

```text
Approved Procedure
Defined Preconditions
Known Risk
Defined Validation
Defined Rollback
Authorised Scope
```

A standard label SHALL not remove required controls when actual circumstances differ from the approved pattern.

---

# 8. Normal Change

A normal change requires case-specific assessment and approval.

It SHALL identify:

```text
Impact
Risk
Dependencies
Testing
Release
Deployment
Rollback
Observation
```

---

# 9. Emergency Change

Emergency changes MAY use an expedited process when delay creates unacceptable risk.

Emergency changes SHALL still record:

```text
Trigger
Urgency
Authority
Risk
Scope
Implementation
Evidence
Post-Change Verification
Post-Implementation Review
```

Emergency status SHALL not become a permanent shortcut.

---

# 10. Change Risk

Change risk SHALL consider:

```text
Technical Risk
Operational Risk
Security Risk
Compliance Risk
Data Risk
Dependency Risk
Rollback Risk
Propagation Risk
Residual Risk
```

---

# 11. Change Materiality

Material changes MAY require:

```text
Enhanced Impact Analysis
Independent Review
Additional Testing
Formal Assurance
Higher Approval Authority
Controlled Deployment
Extended Observation
Reacceptance
```

---

# 12. Change Authority

RG-413 SHALL determine who may:

```text
Submit
Assess
Approve
Implement
Release
Deploy
Rollback
Accept
Close
```

These authorities SHALL be separately governed where required.

---

# 13. Separation of Duties

For material changes:

```text
REQUESTER
   ≠
APPROVER
```

Where required:

```text
IMPLEMENTER
   ≠
RELEASE APPROVER
   ≠
FINAL ACCEPTANCE AUTHORITY
```

Exceptions SHALL be explicit and risk-controlled.

---

# 14. Change Conflict of Interest

Material conflicts SHALL be identified.

Possible outcomes:

```text
NO CONFLICT
MANAGED
RECUSAL
REASSIGNMENT
ESCALATION
```

---

# 15. Change Impact Assessment

RG-422 SHALL provide:

```text
Dependency Graph
Affected Objects
Propagation Potential
Materiality
Risk
Downstream Decisions
Reliance Impact
```

Change control SHALL not proceed to final approval without required impact analysis.

---

# 16. Change Preconditions

Before implementation, required preconditions MAY include:

```text
Approval
Backup
Baseline
Test Environment
Dependencies Available
Rollback Ready
Monitoring Active
Communication
Maintenance Window
Security Review
```

---

# 17. Preconditions Verification

The system SHALL verify required preconditions before execution.

Failure SHALL result in:

```text
BLOCK
DEFER
REASSESS
```

rather than silent continuation.

---

# 18. Implementation Plan

A material implementation plan SHALL identify:

```text
Steps
Owner
Sequence
Dependencies
Expected Duration
Controls
Verification
Rollback
```

---

# 19. Implementation Sequence

Where sequencing matters:

```text
STEP A
  ↓
STEP B
  ↓
STEP C
```

Dependencies SHALL be enforced.

---

# 20. Parallel Implementation

Independent actions MAY execute in parallel.

Shared dependencies SHALL remain controlled.

---

# 21. Implementation Evidence

Implementation SHALL produce evidence such as:

```text
Command / Activity Log
Configuration
Deployment Record
Version
Timestamp
Operator
Target
Result
```

---

# 22. Environment Control

Changes SHALL identify target environments:

```text
DEVELOPMENT
TEST
STAGING
PRODUCTION
DISASTER RECOVERY
OTHER CONTROLLED ENVIRONMENT
```

Environment transitions SHALL be explicit.

---

# 23. Environment Promotion

Promotion MAY follow:

```text
DEVELOPMENT
   ↓
TEST
   ↓
STAGING
   ↓
PRODUCTION
```

Each promotion SHALL preserve artefact identity.

---

# 24. Promotion Criteria

Promotion SHALL require applicable:

```text
Tests Passed
Evidence Present
Approval Valid
Dependencies Ready
Security Criteria
Rollback Ready
```

---

# 25. Release Object

A release SHALL identify the exact controlled package/version being deployed.

Minimum attributes:

```text
Release ID
Version
Change Request
Artefacts
Dependencies
Build
Tests
Approvals
Security Status
Release Notes
Target Environments
Rollback Package
Integrity Metadata
```

---

# 26. Release Immutability

Once a release is approved, its material contents SHALL be immutable.

Changes to the release SHALL create a new release version.

---

# 27. Release Integrity

Release integrity SHALL support:

```text
Hash / Integrity Metadata
Version
Build Reference
Source Reference
Dependency Versions
Approval
Timestamp
```

---

# 28. Release Qualification

A release SHALL be qualified against:

```text
Functional Tests
Regression Tests
Security Tests
Compatibility
Performance
Configuration
Dependency Versions
```

as applicable.

---

# 29. Release Approval

Release approval SHALL verify:

```text
Correct Artefact
Correct Version
Tests Complete
Required Evidence
Required Authority
Known Risks
Rollback Available
```

---

# 30. Deployment Object

Deployment SHALL identify:

```text
Deployment ID
Release
Target
Environment
Start
End
Operator
Method
Result
Verification
Rollback
Status
```

---

# 31. Deployment Lifecycle

```text
SCHEDULED
   ↓
PREPARED
   ↓
EXECUTING
   ↓
DEPLOYED
   ↓
VERIFYING
   ↓
OBSERVING
   ↓
ACCEPTED
```

Alternative:

```text
FAILED
ROLLED BACK
PARTIALLY DEPLOYED
SUSPENDED
```

---

# 32. Deployment Preconditions

Before deployment:

```text
Release Valid
Approval Valid
Target Available
Dependencies Ready
Monitoring Active
Rollback Ready
```

shall be confirmed.

---

# 33. Deployment Verification

Immediately after deployment, verify:

```text
Version
Availability
Core Function
Dependencies
Security
Configuration
Monitoring
```

---

# 34. Deployment Health Check

Health checks SHALL distinguish:

```text
DEPLOYMENT SUCCESS
```

from:

```text
SYSTEM HEALTHY
```

Deployment completion alone does not prove operational success.

---

# 35. Post-Deployment Observation

Material deployments SHALL have an observation period.

```text
DEPLOY
   ↓
STABILISE
   ↓
OBSERVE
   ↓
ASSESS
```

---

# 36. Observation Criteria

Observation MAY include:

```text
Error Rate
Performance
Availability
Security Signals
Control Results
User Impact
Dependency Health
Regression Signals
```

---

# 37. Observation Baseline

Post-deployment observations SHALL compare against an approved baseline where applicable.

```text
BEFORE
  ↓
CHANGE
  ↓
AFTER
```

---

# 38. Deployment Acceptance

Deployment acceptance SHALL require:

```text
Required Tests
Health Checks
Observation
No Blocking Regression
Required Evidence
Authority
```

---

# 39. Conditional Deployment Acceptance

A deployment MAY be conditionally accepted where policy allows.

Conditions SHALL be:

```text
Specific
Owned
Time-Bound
Monitored
Auditable
```

---

# 40. Rollback

Rollback SHALL be a controlled operation.

It SHALL identify:

```text
Trigger
Authority
Target State
Procedure
Evidence
Verification
Residual Risk
```

---

# 41. Rollback Trigger

Rollback MAY be triggered by:

```text
Critical Failure
Material Regression
Security Event
Unacceptable Performance
Data Integrity Risk
Dependency Failure
Acceptance Condition Breach
```

---

# 42. Automatic Rollback

Automatic rollback MAY be used for predefined conditions.

Rules SHALL be:

```text
Explicit
Tested
Versioned
Authorised
Monitored
```

---

# 43. Rollback Verification

Rollback SHALL be verified.

```text
ROLLBACK COMPLETE
      ≠
SYSTEM RESTORED
```

Restoration requires evidence.

---

# 44. Partial Rollback

Partial rollback SHALL identify:

```text
Reverted Components
Remaining Changes
Affected Dependencies
Residual Risk
Follow-Up
```

---

# 45. Rollback Failure

If rollback fails:

```text
ROLLBACK FAILURE
   ↓
INCIDENT / FINDING
   ↓
CONTAINMENT
   ↓
REMEDIATION
```

as applicable.

---

# 46. Deployment Failure

Deployment failure SHALL preserve:

```text
Attempt
Logs
Artefact
Target
Error
Actions
Outcome
```

---

# 47. Partial Deployment

Partial deployment SHALL be explicitly represented.

```text
TARGET A → DEPLOYED
TARGET B → NOT DEPLOYED
TARGET C → FAILED
```

The system SHALL not represent the change as globally deployed.

---

# 48. Deployment Consistency

Where multiple targets must remain consistent, deployment governance SHALL verify consistency.

---

# 49. Canary Deployment

Canary deployment MAY be used:

```text
SMALL POPULATION
   ↓
OBSERVE
   ↓
EXPAND
```

Expansion SHALL be based on explicit criteria.

---

# 50. Blue/Green Deployment

Blue/green deployment MAY provide:

```text
CURRENT ENVIRONMENT
      ↓
NEW ENVIRONMENT
      ↓
VALIDATE
      ↓
SWITCH
```

Rollback SHALL remain available.

---

# 51. Phased Deployment

Phased deployment SHALL identify:

```text
Phase
Population
Criteria
Observation
Go / No-Go
```

---

# 52. Deployment Gates

Gates MAY include:

```text
APPROVAL GATE
TEST GATE
SECURITY GATE
RELEASE GATE
DEPLOYMENT GATE
OBSERVATION GATE
ACCEPTANCE GATE
```

Each gate SHALL have explicit entry and exit criteria.

---

# 53. Gate Failure

A failed gate SHALL result in:

```text
BLOCK
REWORK
REASSESS
ROLLBACK
ESCALATE
```

depending on the condition.

---

# 54. Change Freeze

A controlled freeze MAY prevent deployment during defined periods.

Freeze exceptions SHALL require explicit authority.

---

# 55. Maintenance Window

Deployments MAY be constrained to approved windows.

Window overruns SHALL trigger escalation.

---

# 56. Communication

Material changes SHALL provide controlled communications where required:

```text
Planned
Start
Impact
Completion
Failure
Rollback
Recovery
```

Communication SHALL not replace technical evidence.

---

# 57. Stakeholder Notification

Stakeholders MAY include:

```text
Operations
Security
Compliance
Management
Customers
Service Owners
External Parties
```

Notification scope SHALL follow policy.

---

# 58. Change Documentation

Change records SHALL remain complete after closure.

The record SHOULD include:

```text
Request
Impact
Approval
Implementation
Release
Deployment
Observation
Rollback
Acceptance
Closure
```

---

# 59. Change Closure

Change closure SHALL require:

```text
Implementation Complete
Required Verification
Observation Complete
Known Issues Resolved / Governed
Evidence Present
Final Decision
Authority
```

---

# 60. Change Closure vs Release Closure

A release may be closed while the broader change remains under observation.

These lifecycle objects SHALL remain distinct.

---

# 61. Change Closure vs Incident Closure

A change may be closed while an incident caused by the change remains open.

The relationship SHALL remain traceable.

---

# 62. Change Closure vs Remediation

A change may be the corrective action for a finding.

Closure of the change does not automatically close the remediation.

Effectiveness SHALL still be assessed.

---

# 63. Change Reopening

A closed change MAY be reopened because of:

```text
Regression
Unexpected Impact
Evidence Failure
Incorrect Closure
Security Event
New Dependency
```

---

# 64. Change Supersession

A new change MAY supersede an earlier change.

Historical records SHALL remain intact.

---

# 65. Change Expiry

Some changes may be temporary.

Temporary changes SHALL have:

```text
Start
End
Expiry Action
Owner
```

Expiry SHALL trigger restoration, review or renewal.

---

# 66. Temporary Change

Temporary changes SHALL not become permanent through administrative neglect.

Expiration SHALL be monitored.

---

# 67. Configuration Drift

After deployment, actual configuration SHALL be compared to approved configuration.

Unexpected drift SHALL generate:

```text
Finding
Alert
Reconciliation
```

as appropriate.

---

# 68. Release Drift

The deployed artefact SHALL remain identifiable.

If deployed version differs from approved release:

```text
RELEASE DRIFT
   ↓
ASSESS
   ↓
BLOCK / REMEDIATE / ACCEPT
```

---

# 69. Unauthorised Change

Unauthorised change SHALL be detectable.

```text
ACTUAL STATE
      ≠
APPROVED STATE
```

shall trigger investigation.

---

# 70. Change Detection

RG-416 monitoring SHALL detect:

```text
Unexpected Deployment
Configuration Drift
Version Drift
Performance Regression
Security Signals
```

---

# 71. Change Impact Integration

RG-422 SHALL provide:

```text
Dependency Context
Affected Objects
Propagation
Risk
```

before and after implementation.

---

# 72. Post-Closure Integration

RG-421 SHALL monitor closed decisions affected by changes.

---

# 73. Finding Integration

RG-417 SHALL manage material change-related findings.

---

# 74. Incident Integration

RG-417 SHALL manage change-related incidents.

---

# 75. Remediation Integration

RG-418 SHALL manage corrective and preventive actions arising from change failure.

---

# 76. Assurance Integration

RG-419 SHALL provide independent assurance where required.

---

# 77. Decision Integration

RG-420 SHALL govern:

```text
Approval
Acceptance
Conditional Acceptance
Rejection
Rollback Decision
Closure
```

---

# 78. Change Risk Integration

RG-415 SHALL provide:

```text
Risk
Materiality
Tolerance
Escalation
```

---

# 79. Policy Integration

RG-414 SHALL define:

```text
Change Classes
Approval Rules
Testing Requirements
Release Criteria
Emergency Rules
Closure Criteria
```

---

# 80. Authority Integration

RG-413 SHALL determine:

```text
Approval Authority
Deployment Authority
Rollback Authority
Acceptance Authority
Closure Authority
```

---

# 81. Evidence Integration

RG-412 SHALL provide traceability for:

```text
Change
Approval
Release
Deployment
Test
Observation
Rollback
Closure
```

---

# 82. Workflow Integration

RG-411 SHALL orchestrate:

```text
Submission
Assessment
Approval
Execution
Release
Deployment
Observation
Rollback
Closure
```

---

# 83. State Integration

Change actions SHALL not directly bypass the lifecycle state machine.

```text
CHANGE RESULT
   ↓
STATE EVALUATION
   ↓
TRANSITION
```

---

# 84. MFM Data Model

Core entities:

```text
ChangeRequest
ChangeAssessment
ChangeApproval
Implementation
Release
ReleaseArtifact
Deployment
DeploymentTarget
DeploymentObservation
Rollback
ChangeClosure
ChangeCondition
ChangeGate
```

Relationships:

```text
ChangeRequest
   ↓
Approval
   ↓
Implementation
   ↓
Release
   ↓
Deployment
   ↓
Observation
   ↓
Acceptance / Rollback
   ↓
Closure
```

---

# 85. MFM Service Boundary

The conceptual implementation should include:

```text
Change Control Service
Release Service
Deployment Service
Gate Service
Rollback Service
Observation Service
Change Closure Service
Configuration Reconciliation Service
```

These integrate with:

```text
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

services.

---

# 86. API Concepts

Illustrative operations:

```text
createChangeRequest()
submitChange()
assessChange()
approveChange()
prepareImplementation()
createRelease()
approveRelease()
deployRelease()
verifyDeployment()
startObservation()
triggerRollback()
verifyRollback()
acceptDeployment()
closeChange()
reopenChange()
```

These are architectural concepts, not implementation-specific commitments.

---

# 87. Change Dashboard

The system SHOULD display:

```text
Pending Changes
High-Risk Changes
Changes Awaiting Approval
Releases Ready
Active Deployments
Failed Deployments
Rollbacks
Changes Under Observation
Overdue Changes
Unauthorised Changes
```

---

# 88. Release Dashboard

The system SHOULD display:

```text
Release Version
Change
Status
Test Status
Approval
Deployment Status
Known Issues
Rollback Availability
```

---

# 89. Deployment Dashboard

The system SHOULD display:

```text
Target
Release
Version
Status
Start
Duration
Health
Errors
Rollback Status
Observation
```

---

# 90. Change Metrics

The system SHOULD report:

```text
Change Success Rate
Change Failure Rate
Rollback Rate
Emergency Change Rate
Unauthorised Change Rate
Mean Time to Deploy
Mean Time to Recover
Post-Change Incident Rate
Post-Change Regression Rate
Change Closure Time
```

---

# 91. Release Metrics

Possible measures:

```text
Release Failure Rate
Defect Escape Rate
Rollback Rate
Release Cycle Time
Test Pass Rate
Emergency Release Rate
```

---

# 92. Deployment Metrics

Possible measures:

```text
Deployment Success
Partial Deployment
Failed Deployment
Rollback
Observation Failure
Mean Deployment Duration
```

---

# 93. Change Quality

Change quality SHOULD be assessed through:

```text
First-Time Success
Regression Frequency
Rollback Frequency
Incident Frequency
Evidence Completeness
Approval Quality
Impact Prediction Accuracy
```

---

# 94. Impact Prediction Accuracy

The architecture SHOULD compare:

```text
PREDICTED IMPACT
      vs
OBSERVED IMPACT
```

Differences SHALL inform future impact models.

---

# 95. Continuous Improvement

Change outcomes SHOULD feed:

```text
Policy
Rules
Testing
Monitoring
Dependency Models
Risk Models
Training
```

Improvements SHALL be governed changes themselves.

---

# 96. Security

Change and release systems SHALL protect against:

```text
Unauthorised Deployment
Artefact Substitution
Approval Spoofing
Privilege Abuse
Rollback Manipulation
Audit Deletion
```

---

# 97. Release Integrity

Release artefacts SHALL support integrity verification.

A mismatch SHALL block deployment or trigger defined emergency handling.

---

# 98. Deployment Identity

Deployment actions SHALL be attributable to:

```text
Person
Service Account
Automation
Agent
```

Automated identities SHALL have controlled authority.

---

# 99. AI / Agent Deployment

Where AI agents can initiate or execute changes:

```text
Agent Identity
Scope
Permissions
Approval
Action Log
Tool Calls
Target
Result
```

shall be recorded.

AI SHALL not exceed granted change authority.

---

# 100. Automated Deployment

Automation MAY execute approved deployment workflows.

Automation SHALL not infer approval from:

```text
Time Expiry
Missing Response
System Availability
```

unless explicitly authorised by policy.

---

# 101. Emergency Automation

Emergency automation SHALL be restricted to predefined scenarios and tested procedures.

---

# 102. Testing

The architecture SHALL test:

```text
Change Submission
Classification
Impact Assessment
Approval
Implementation
Release
Promotion
Deployment
Health Check
Observation
Rollback
Partial Deployment
Canary
Phased Deployment
Closure
Reopening
```

---

# 103. Negative Testing

The system SHALL verify:

```text
No approval → BLOCK
Invalid authority → BLOCK
Wrong release version → BLOCK
Missing rollback → BLOCK where mandatory
Failed tests → BLOCK
Inactive monitoring → BLOCK for required changes
Unauthorised deployment → BLOCK / ALERT
Release modification after approval → INVALIDATE
Partial deployment → NOT GLOBAL SUCCESS
Rollback failure → ESCALATE
Expired approval → BLOCK
Emergency flag without emergency criteria → BLOCK
```

---

# 104. Scenario Testing

Representative scenarios:

```text
Normal change
Standard change
High-risk change
Emergency change
Security patch
Database change
Configuration change
Policy change
Rule change
Model deployment
Canary deployment
Blue/green deployment
Failed deployment
Partial deployment
Rollback
Rollback failure
Concurrent changes
Unauthorised change
Post-deployment regression
Temporary change expiry
```

---

# 105. Acceptance Criteria

EA-IMETA-PC-RG-423 is accepted when:

- change requests have controlled lifecycle;
- standard, normal and emergency changes are distinguished;
- authority and separation of duties are enforced;
- impact analysis from RG-422 is mandatory where applicable;
- implementation is separated from approval;
- releases identify immutable artefacts;
- deployment is a distinct lifecycle object;
- environment promotion is controlled;
- deployment verification is distinct from deployment completion;
- post-deployment observation is supported;
- rollback is controlled and verifiable;
- partial deployment is represented accurately;
- canary, phased and blue/green patterns are supported;
- temporary changes have expiry;
- configuration/release drift can be detected;
- unauthorised changes are detectable;
- AI/automated deployment is governed;
- findings, incidents, remediation, assurance, decisions and reliance integrate;
- historical change records are preserved;
- negative tests prevent unauthorised or incomplete deployment;
- closure requires evidence and governed decision.

---

# 106. Next Step

The next logical artifact is the **PC-RG configuration, baseline and state-integrity model**, because RG-423 controls how releases are deployed, while the architecture now needs to define how the approved configuration and actual deployed state are continuously compared and reconciled.

Provisional next artifact:

> **EA-IMETA-PC-RG-424 — CONFIGURATION, BASELINE & STATE-INTEGRITY MODEL**

This will establish the authoritative relationship between approved state, released state, deployed state and observed state.

---

# 107. Governing Principle

> **A change is governed from request to closure; a release is a controlled artefact; a deployment changes the environment; observation determines actual behaviour; and rollback is itself a governed change.**

The PC-RG architecture SHALL therefore maintain complete traceability between what was approved, what was released, what was deployed, what actually occurred and what final governance decision was made.

# END OF EA-IMETA-PC-RG-423
