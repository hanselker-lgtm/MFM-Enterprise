# EA-IMETA-PC-RG-418

## REMEDIATION, CORRECTIVE ACTION & EFFECTIVENESS MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-418 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Remediation, Corrective Action & Effectiveness Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-417 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how confirmed conditions are planned, corrected, verified, measured for effectiveness and formally closed |
| Architectural Boundary | Finding → Action → Remediation → Verification → Effectiveness → Residual Risk → Closure |

---

# 2. Purpose

EA-IMETA-PC-RG-418 defines the controlled architecture for correcting conditions identified through findings, incidents, exceptions and regression assessment.

RG-417 defines the governed condition.

RG-418 defines **how the condition is corrected and how the organisation proves that the correction actually worked**.

The architecture SHALL distinguish:

```text
CORRECTION
= FIX THE IMMEDIATE CONDITION

CORRECTIVE ACTION
= ADDRESS THE CAUSE OF AN IDENTIFIED CONDITION

PREVENTIVE ACTION
= REDUCE THE POSSIBILITY OF RECURRENCE

REMEDIATION
= CONTROLLED PROGRAMME OF ACTIONS TO RESTORE AN ACCEPTABLE CONDITION

EFFECTIVENESS
= EVIDENCE THAT THE RESPONSE ACHIEVED THE INTENDED RESULT
```

---

# 3. Core Principle

> **Completing an action is not proof that the underlying condition has been corrected.**

The governing chain is:

```text
CONFIRMED CONDITION
       ↓
ROOT CAUSE / CONTRIBUTING FACTORS
       ↓
REMEDIATION PLAN
       ↓
ACTION EXECUTION
       ↓
EVIDENCE
       ↓
VERIFICATION
       ↓
EFFECTIVENESS ASSESSMENT
       ↓
RESIDUAL RISK
       ↓
CLOSURE DECISION
```

---

# 4. Remediation Object

Every material remediation SHALL be represented as a controlled object.

Minimum attributes:

```text
Remediation ID
Finding / Incident / Exception Reference
Problem Statement
Scope
Severity
Risk
Objective
Owner
Plan
Actions
Dependencies
Target Date
Evidence Requirements
Verification Method
Effectiveness Criteria
Residual Risk
Status
Authority
Version
```

---

# 5. Remediation Lifecycle

```text
IDENTIFIED
   ↓
ASSESSED
   ↓
PLANNED
   ↓
APPROVED
   ↓
IN EXECUTION
   ↓
IMPLEMENTED
   ↓
PENDING VERIFICATION
   ↓
EFFECTIVENESS REVIEW
   ↓
ACCEPTED
   ↓
CLOSED
```

Alternative states:

```text
BLOCKED
SUSPENDED
FAILED
REOPENED
CANCELLED
SUPERSEDED
```

---

# 6. Remediation Objective

Every remediation SHALL have a measurable or objectively assessable objective.

Examples:

```text
Restore control effectiveness.
Remove critical vulnerability.
Restore evidence integrity.
Reduce residual risk below tolerance.
Restore required authority separation.
Prevent recurrence of identified root cause.
```

A generic objective such as "fix issue" is insufficient for material remediation.

---

# 7. Problem Statement

The remediation record SHALL distinguish:

```text
Observed Condition
Expected Condition
Gap
Impact
Risk
Scope
```

This prevents the action plan from becoming detached from the original problem.

---

# 8. Scope

Remediation scope SHALL identify:

```text
Affected Case(s)
System(s)
Control(s)
Requirement(s)
Dependency(ies)
Process(es)
Data
Population
Environment
```

Out-of-scope areas SHALL be explicit where relevant.

---

# 9. Root Cause Relationship

Remediation SHALL link to:

```text
Root Cause
Contributing Factors
Failure Mechanism
Control Weakness
```

Where root cause is unknown, the remediation MAY address containment while root-cause investigation continues.

---

# 10. Correction

Correction addresses the immediate condition.

Example:

```text
Broken configuration
   ↓
Restore approved configuration
```

Correction SHALL not automatically be treated as corrective action.

---

# 11. Corrective Action

Corrective action addresses the cause.

Example:

```text
Incorrect configuration repeatedly deployed
   ↓
Change deployment control
```

The corrective action SHALL be linked to the relevant cause.

---

# 12. Preventive Action

Preventive action reduces recurrence probability.

Examples:

```text
New automated test
Additional control
Monitoring improvement
Training
Architecture change
Dependency resilience
Policy update
```

Preventive action SHALL have defined effectiveness criteria.

---

# 13. Action Object

Each action SHALL contain:

```text
Action ID
Type
Description
Owner
Priority
Due Date
Dependencies
Required Evidence
Completion Criteria
Verification Criteria
Status
Completion Date
Version
```

---

# 14. Action Types

Initial catalogue:

```text
CORRECTION
CORRECTIVE
PREVENTIVE
CONTAINMENT
CONTROL ENHANCEMENT
CONFIGURATION CHANGE
CODE CHANGE
PROCESS CHANGE
POLICY CHANGE
TRAINING
MONITORING CHANGE
DEPENDENCY CHANGE
DATA REPAIR
```

---

# 15. Action Dependencies

Actions MAY depend on:

```text
Other Actions
Approvals
Evidence
System Availability
Vendor Input
Change Window
Policy Update
Technical Deployment
```

Dependencies SHALL be explicit.

---

# 16. Action Sequencing

Where sequence matters:

```text
ACTION A
   ↓
ACTION B
   ↓
ACTION C
```

The workflow engine SHALL enforce dependencies.

---

# 17. Parallel Actions

Independent actions MAY execute in parallel.

```text
          ┌→ ACTION A ─┐
REMEDIATION            ├→ VERIFICATION
          └→ ACTION B ─┘
```

Parallel execution SHALL not bypass shared approval or verification requirements.

---

# 18. Action Ownership

Every actionable item SHALL have one accountable owner.

Multiple contributors MAY exist, but accountability SHALL remain unambiguous.

---

# 19. Due Dates

Due dates SHALL consider:

```text
Risk
Severity
Materiality
Business Impact
Regulatory Requirement
Dependency
Implementation Complexity
```

Critical remediation MAY require immediate action.

---

# 20. Remediation Priority

Illustrative:

```text
P1 — CRITICAL
P2 — HIGH
P3 — MEDIUM
P4 — LOW
```

Priority SHALL be derived through controlled policy.

---

# 21. Remediation Approval

Material remediation plans MAY require approval before execution.

Approval SHALL consider:

```text
Scope
Risk
Impact
Approach
Dependencies
Downtime
Security
Evidence
Rollback
```

---

# 22. Change Management Integration

Where remediation changes production systems, it SHALL integrate with controlled change management.

```text
REMEDIATION
   ↓
CHANGE REQUEST
   ↓
CHANGE APPROVAL
   ↓
IMPLEMENTATION
   ↓
POST-CHANGE VERIFICATION
```

Remediation authority does not automatically equal production-change authority.

---

# 23. Emergency Remediation

Emergency remediation MAY be authorised where delay creates unacceptable risk.

Emergency execution SHALL record:

```text
Trigger
Authority
Action
Risk
Reason
Evidence
Rollback
Post-Implementation Review
```

Emergency status SHALL not eliminate later verification.

---

# 24. Rollback

Material technical remediation SHOULD define rollback criteria.

```text
IMPLEMENT
   ↓
FAILURE
   ↓
ROLLBACK
   ↓
STABILISE
   ↓
REASSESS
```

Rollback itself SHALL be auditable.

---

# 25. Evidence Requirements

Every material remediation SHALL define required evidence before execution.

Examples:

```text
Configuration Snapshot
Test Result
Deployment Record
Approval
Screenshot
Log
Measurement
Independent Verification
```

Evidence requirements SHALL be versioned.

---

# 26. Completion vs Verification

The architecture SHALL distinguish:

```text
ACTION COMPLETE
```

from:

```text
ACTION VERIFIED
```

An owner may report completion.

An authorised verifier determines whether the required result has actually been demonstrated.

---

# 27. Verification

Verification SHALL assess:

```text
Was the action performed?
Was it performed correctly?
Did it produce the intended condition?
Is evidence sufficient?
Are required controls restored?
```

Verification method SHALL be defined before closure where practicable.

---

# 28. Independent Verification

High-risk remediation SHALL use independent verification where required.

Preferred:

```text
REMEDIATION OWNER
       ≠
VERIFIER
```

This reinforces the separation-of-duties model in RG-413.

---

# 29. Verification Outcomes

Possible outcomes:

```text
VERIFIED
NOT VERIFIED
PARTIALLY VERIFIED
INCONCLUSIVE
FAILED
REQUIRES REWORK
```

---

# 30. Effectiveness

Effectiveness asks:

> Did the remediation solve the actual problem and reduce the relevant risk sufficiently?

It SHALL go beyond confirmation that a task was completed.

---

# 31. Effectiveness Criteria

Criteria MAY include:

```text
Control Restored
Failure No Longer Reproduces
Risk Reduced
Threshold Restored
No Recurrence
Performance Restored
Evidence Integrity Restored
Authority Separation Restored
Compliance Condition Satisfied
```

---

# 32. Effectiveness Measurement

Effectiveness SHOULD use objective measures.

Example:

```text
Before:
Failure Rate = 8%

After:
Failure Rate = 0.4%

Required:
< 1%

Result:
EFFECTIVE
```

---

# 33. Baseline Comparison

Effectiveness SHALL compare:

```text
BEFORE
   ↓
REMEDIATION
   ↓
AFTER
```

The baseline used SHALL be identified.

---

# 34. Observation Period

Some remediation cannot be considered effective immediately.

An effectiveness observation period MAY be defined:

```text
IMPLEMENTATION
   ↓
STABILISATION
   ↓
OBSERVATION PERIOD
   ↓
EFFECTIVENESS DECISION
```

---

# 35. Recurrence Test

Where recurrence is relevant, effectiveness SHALL include monitoring for recurrence.

Example:

```text
No recurrence for defined period
```

The period SHALL be policy-controlled.

---

# 36. Partial Effectiveness

A remediation MAY produce partial improvement.

Example:

```text
Risk:
20 → 8

Tolerance:
≤ 5

Result:
IMPROVED BUT NOT EFFECTIVE
```

The system SHALL distinguish improvement from successful remediation.

---

# 37. Failed Remediation

If remediation fails:

```text
REMEDIATION FAILED
   ↓
RISK REASSESSMENT
   ↓
ESCALATION
   ↓
NEW / REVISED REMEDIATION
```

Failure SHALL not be hidden by administrative closure.

---

# 38. Remediation Reopening

A completed remediation MAY be reopened because of:

```text
Recurrence
Verification Failure
New Evidence
Insufficient Effectiveness
New Dependency
Changed Risk
Incorrect Root Cause
```

Historical actions SHALL remain recorded.

---

# 39. Remediation Closure

Closure SHALL require:

```text
All Required Actions Complete
+
Required Evidence Present
+
Verification Complete
+
Effectiveness Criteria Satisfied
+
Residual Risk Acceptable
+
Required Authority Approval
```

---

# 40. Residual Risk

After remediation:

```text
INHERENT RISK
    ↓
CONTROLS
    ↓
REMEDIATION
    ↓
RESIDUAL RISK
```

Residual risk SHALL be compared to the applicable tolerance.

---

# 41. Risk Acceptance

If residual risk remains above normal tolerance, closure SHALL require an explicit authorised risk decision where policy permits.

This SHALL not be disguised as remediation effectiveness.

---

# 42. Exception Integration

If remediation cannot fully restore the required condition:

```text
REMEDIATION
   ↓
RESIDUAL GAP
   ↓
EXCEPTION REQUEST
```

The exception SHALL be governed by RG-417.

---

# 43. Monitoring Integration

RG-416 monitoring SHALL support effectiveness measurement.

```text
REMEDIATION
   ↓
MONITOR
   ↓
OBSERVE
   ↓
COMPARE BASELINE
   ↓
EFFECTIVENESS
```

Monitoring SHALL continue for the defined observation period.

---

# 44. Finding Integration

RG-417 findings SHALL remain open until closure criteria are satisfied.

```text
FINDING
   ↓
REMEDIATION
   ↓
VERIFICATION
   ↓
EFFECTIVENESS
   ↓
FINDING CLOSURE
```

---

# 45. Incident Integration

Incident recovery may generate remediation.

```text
INCIDENT
   ↓
RECOVERY
   ↓
ROOT CAUSE
   ↓
CORRECTIVE ACTION
   ↓
EFFECTIVENESS
```

Incident resolution does not eliminate corrective-action obligations.

---

# 46. Exception Integration

An active exception MAY require remediation to remove the exception condition.

```text
EXCEPTION ACTIVE
   ↓
REMEDIATION
   ↓
CONTROL RESTORED
   ↓
EXCEPTION CLOSED
```

---

# 47. Policy Integration

Remediation may require changes to:

```text
Policy
Rule
Criteria
Threshold
Control
Workflow
```

Such changes SHALL follow controlled change management.

---

# 48. Rule Change Impact

If remediation modifies a rule:

```text
RULE CHANGE
   ↓
IMPACT ANALYSIS
   ↓
REGRESSION TEST
   ↓
APPROVAL
   ↓
ACTIVATION
```

Historical decisions SHALL remain based on their original rule versions.

---

# 49. Monitoring Change Impact

If remediation changes monitoring:

```text
MONITOR CHANGE
   ↓
COVERAGE IMPACT
   ↓
THRESHOLD REVIEW
   ↓
REGRESSION TEST
```

A monitoring change SHALL not be used to make an undesirable condition disappear from reporting.

---

# 50. Effectiveness and Independence

The person declaring remediation complete SHOULD not be the sole person deciding that effectiveness has been demonstrated for high-risk cases.

This is a practical application of RG-413.

---

# 51. Evidence Chain

The complete remediation chain SHALL be reconstructable:

```text
FINDING
  ↓
ROOT CAUSE
  ↓
ACTION
  ↓
IMPLEMENTATION
  ↓
EVIDENCE
  ↓
VERIFICATION
  ↓
EFFECTIVENESS
  ↓
RISK
  ↓
CLOSURE
```

---

# 52. Action Evidence

Action evidence SHALL prove what was done.

Examples:

```text
Change Record
Deployment Record
Configuration Snapshot
Test Output
Approval
Work Order
```

Action evidence alone does not prove effectiveness.

---

# 53. Effectiveness Evidence

Effectiveness evidence SHALL prove the resulting condition.

Examples:

```text
Successful Test
Monitoring Data
Independent Assessment
Repeated Stable Measurements
Control Test
Risk Reassessment
```

---

# 54. Before/After Evidence

Where material, the evidence set SHOULD include:

```text
PRE-REMEDIATION
+
IMPLEMENTATION
+
POST-REMEDIATION
```

This supports causal and effectiveness assessment.

---

# 55. Causal Confidence

Effectiveness assessment SHALL distinguish:

```text
OBSERVED IMPROVEMENT
```

from:

```text
PROVEN REMEDIATION EFFECT
```

Where multiple changes occurred simultaneously, causal attribution may require additional analysis.

---

# 56. Effectiveness Confidence

An effectiveness assessment MAY include:

```text
HIGH
MEDIUM
LOW
INCONCLUSIVE
```

The confidence rating SHALL not replace the underlying evidence.

---

# 57. Effectiveness Failure

If evidence is insufficient:

```text
EFFECTIVENESS = INCONCLUSIVE
```

not:

```text
EFFECTIVENESS = PASS
```

Further observation or verification SHALL be required.

---

# 58. Remediation Dependencies

A remediation may depend on:

```text
Vendor
System Release
Infrastructure
Policy Approval
Training
Data Migration
External Authority
```

Dependencies SHALL be monitored.

---

# 59. Dependency Failure

If a dependency fails:

```text
REMEDIATION BLOCKED
   ↓
RISK REASSESSMENT
   ↓
ESCALATION
```

The remediation due date SHALL not be silently reset.

---

# 60. Remediation SLA

Remediation SLAs SHALL support:

```text
Acknowledgement
Planning
Implementation
Verification
Effectiveness
Closure
```

SLA breach SHALL trigger appropriate escalation.

---

# 61. Remediation Aging

The system SHOULD report:

```text
Days Open
Days Since Action
Days Awaiting Verification
Days Awaiting Effectiveness
Overdue Duration
```

Aging is a risk indicator, not merely an administrative metric.

---

# 62. Remediation Backlog

The architecture SHOULD identify:

```text
Open Remediations
Critical Backlog
Overdue Backlog
Blocked Backlog
Repeated Remediations
High-Risk Owners
Systemic Remediations
```

---

# 63. Remediation Concentration

Multiple actions may address the same root cause.

```text
Action A
Action B
Action C
   ↓
ROOT CAUSE X
```

This may indicate that systemic remediation is preferable.

---

# 64. Systemic Remediation

Systemic remediation addresses common causes across multiple cases.

Examples:

```text
Common Control Redesign
Shared Dependency Replacement
Architecture Change
Common Policy Change
Central Monitoring Enhancement
```

Systemic remediation SHOULD be preferred where it provides durable risk reduction.

---

# 65. Preventive Effectiveness

Preventive actions SHALL be assessed against recurrence indicators.

Example:

```text
Recurring failures before = 12 / quarter
After preventive action = 0 / quarter
```

The observation period SHALL be sufficient for the risk context.

---

# 66. Training Effectiveness

Where training is used as remediation, completion alone SHALL not prove effectiveness.

Effectiveness MAY require:

```text
Assessment
Behavioural Observation
Error Reduction
Control Test
Follow-up Review
```

---

# 67. Process Change Effectiveness

Process changes SHALL be assessed using:

```text
Compliance Rate
Cycle Time
Error Rate
Control Performance
User Adoption
Recurrence
```

---

# 68. Technical Change Effectiveness

Technical remediation MAY require:

```text
Functional Test
Performance Test
Security Test
Regression Test
Availability Test
Monitoring
```

---

# 69. Security Remediation

Security remediation SHALL consider:

```text
Vulnerability Removed
Exposure Reduced
Control Restored
Detection Improved
Residual Risk
Recurrence
```

Closure SHALL follow applicable security authority requirements.

---

# 70. Data Remediation

Data remediation SHALL verify:

```text
Accuracy
Completeness
Integrity
Consistency
Lineage
Downstream Impact
```

Correcting one record does not prove the systemic data issue is resolved.

---

# 71. AI / Agent Remediation

AI-related remediation MAY include:

```text
Prompt Change
Model Change
Guardrail
Permission Reduction
Tool Restriction
Training Data Change
Human Review
Monitoring Enhancement
Model Replacement
```

Effectiveness SHALL be tested against the relevant failure mode.

---

# 72. Model Remediation

A model change SHALL include:

```text
Model Version
Baseline
Evaluation Set
Performance
Safety Tests
Regression Tests
Deployment
Monitoring
Rollback
```

---

# 73. MFM Data Model

Core entities:

```text
Remediation
Action
CorrectiveAction
PreventiveAction
ContainmentAction
RootCause
EffectivenessAssessment
Verification
ResidualRiskAssessment
ClosureDecision
```

Relationships:

```text
Finding
  ↓
Remediation
  ↓
Actions
  ↓
Evidence
  ↓
Verification
  ↓
Effectiveness
  ↓
Risk
  ↓
Closure
```

---

# 74. MFM Service Boundary

The conceptual implementation should include:

```text
Remediation Service
Action Service
Corrective Action Service
Preventive Action Service
Root Cause Service
Verification Service
Effectiveness Service
Residual Risk Service
Closure Service
```

These integrate with:

```text
Finding
Incident
Exception
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

# 75. API Concepts

Illustrative operations:

```text
createRemediation()
createAction()
assignAction()
approveRemediation()
startAction()
completeAction()
verifyAction()
assessEffectiveness()
assessResidualRisk()
reopenRemediation()
closeRemediation()
```

These are architectural concepts, not implementation-specific commitments.

---

# 76. Workflow Integration

RG-411 SHALL orchestrate:

```text
Plan
Approval
Execution
Evidence Collection
Verification
Effectiveness Review
Closure
```

RG-418 defines the controlled business objects and criteria.

---

# 77. State Integration

Remediation results SHALL be submitted to the state machine.

```text
REMEDIATION COMPLETE
   ↓
VERIFICATION
   ↓
EFFECTIVENESS
   ↓
STATE DECISION
```

Remediation services SHALL not directly bypass state governance.

---

# 78. Authority Integration

RG-413 SHALL determine who may:

```text
Approve Remediation
Execute Critical Action
Verify Action
Assess Effectiveness
Accept Residual Risk
Close Remediation
Reopen Remediation
```

---

# 79. Policy Integration

RG-414 SHALL define:

```text
Remediation Criteria
Due Dates
Risk Thresholds
Effectiveness Rules
Closure Rules
Exception Conditions
```

---

# 80. Risk Integration

RG-415 SHALL provide:

```text
Risk
Tolerance
Materiality
Escalation
Residual Risk
```

for remediation governance.

---

# 81. Monitoring Integration

RG-416 SHALL provide:

```text
Baseline
Observation
Trend
Recurrence
Early Warning
Effectiveness Signals
```

---

# 82. Evidence Integration

RG-412 SHALL provide:

```text
Evidence
Traceability
Decision Record
Audit
Retention
```

for remediation.

---

# 83. Finding Integration

RG-417 SHALL provide:

```text
Finding
Incident
Exception
Original Condition
Closure Relationship
```

---

# 84. Metrics

The system SHOULD report:

```text
Remediation Completion Rate
On-Time Rate
Overdue Rate
Verification Failure Rate
Effectiveness Rate
Reopen Rate
Recurrence Rate
Mean Time to Remediate
Mean Time to Verify
Mean Time to Effective Closure
Residual Risk Reduction
```

---

# 85. Effectiveness KPIs

Key measures MAY include:

```text
% Effective on First Verification
% Reopened
% Recurring
Risk Reduction %
Control Improvement %
Time to Stable State
```

Metrics SHALL distinguish administrative completion from effective resolution.

---

# 86. Testing

The architecture SHALL test:

```text
Action Creation
Dependencies
Approval
Execution
Completion
Verification
Effectiveness
Residual Risk
Closure
Reopening
Recurrence
SLA
Exception
Rollback
```

---

# 87. Negative Testing

The system SHALL verify:

```text
Completed action ≠ verified action
Verified action ≠ effective remediation
Effective remediation ≠ automatic closure without authority
Missing evidence → no effectiveness PASS
Risk above tolerance → closure blocked or escalated
Self-verification → blocked where independence required
Expired approval → action blocked
Failed verification → remediation remains open
```

---

# 88. Scenario Testing

Representative scenarios:

```text
Simple corrective action
Critical security remediation
Failed remediation
Partial improvement
Repeated recurrence
Systemic remediation
Exception-dependent remediation
Emergency remediation
AI model remediation
Dependency-blocked remediation
False root cause
Insufficient effectiveness evidence
```

---

# 89. Acceptance Criteria

EA-IMETA-PC-RG-418 is accepted when:

- correction, corrective action, preventive action and remediation are distinct;
- remediation has an explicit lifecycle;
- every material action has an owner and completion criteria;
- action completion is distinct from verification;
- effectiveness is separately assessed;
- before/after evidence can be linked;
- residual risk is reassessed;
- exception integration is supported;
- remediation failure causes reassessment/escalation;
- recurrence can reopen remediation;
- systemic remediation is supported;
- AI/model remediation is governed;
- authority, evidence, risk, monitoring and workflow are integrated;
- closure requires appropriate effectiveness and authority;
- negative tests prevent administrative closure without demonstrated resolution.

---

# 90. Next Step

The next logical artifact is the **PC-RG verification, validation and independent assurance model**, because RG-418 establishes remediation effectiveness but the architecture now needs a formal assurance layer defining how evidence is independently evaluated before a corrected condition can regain trusted status.

Provisional next artifact:

> **EA-IMETA-PC-RG-419 — VERIFICATION, VALIDATION & INDEPENDENT ASSURANCE MODEL**

This will strengthen the boundary between performing remediation and establishing independent confidence that the remediation is valid and effective.

---

# 91. Governing Principle

> **An action is complete when it is performed, a remediation is effective when the intended condition is demonstrated, and a case is ready for closure only when evidence, verification, residual risk and authority support the decision.**

The PC-RG architecture SHALL therefore never equate task completion with successful remediation.

# END OF EA-IMETA-PC-RG-418
