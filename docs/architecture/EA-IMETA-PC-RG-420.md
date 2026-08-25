# EA-IMETA-PC-RG-420

## ACCEPTANCE, RELIANCE & CLOSURE DECISION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-420 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Acceptance, Reliance & Closure Decision Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-419 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how assurance evidence is converted into authorised decisions concerning acceptance, reliance, continuation, suspension, rejection and closure |
| Architectural Boundary | Evidence → Assurance → Decision → Acceptance / Rejection → Reliance → State → Closure |

---

# 2. Purpose

EA-IMETA-PC-RG-420 defines the formal decision boundary between assurance and lifecycle status.

RG-419 establishes validation, verification and independent assurance.

RG-420 establishes **how an authorised decision maker converts that assurance into a controlled governance decision**.

The architecture SHALL distinguish:

```text
ASSURANCE
= EVIDENCE-BASED CONFIDENCE

ACCEPTANCE
= AUTHORISED DECISION THAT DEFINED CONDITIONS ARE SATISFIED

RELIANCE
= AUTHORISED USE OF AN ACCEPTED RESULT FOR A DEFINED PURPOSE

CONTINUATION
= DECISION TO KEEP THE CURRENT STATE

SUSPENSION
= TEMPORARY WITHDRAWAL OF RELIANCE OR OPERATING AUTHORITY

REJECTION
= DECISION THAT ACCEPTANCE CRITERIA ARE NOT SATISFIED

CLOSURE
= FORMAL END OF THE GOVERNED CASE OR LIFECYCLE STAGE
```

These outcomes SHALL not be conflated.

---

# 3. Core Principle

> **Evidence supports assurance; assurance supports decision; authority makes acceptance; reliance is conditional on continuing validity; closure records the authorised outcome.**

The governing chain is:

```text
REQUIREMENT
   ↓
EVIDENCE
   ↓
VALIDATION / VERIFICATION
   ↓
ASSURANCE
   ↓
DECISION
   ↓
ACCEPTANCE / REJECTION
   ↓
RELIANCE
   ↓
MONITORING
   ↓
CLOSURE / SUSPENSION / REOPENING
```

---

# 4. Decision Object

Every material governance decision SHALL be represented as a controlled object.

Minimum attributes:

```text
Decision ID
Case ID
Subject
Decision Type
Decision Criteria
Evidence Set
Assurance Reference
Risk
Materiality
Authority
Decision Maker
Decision Date
Effective From
Effective Until
Conditions
Rationale
Outcome
State Impact
Review Trigger
Version
```

---

# 5. Decision Types

Initial catalogue:

```text
ACCEPT
REJECT
CONDITIONALLY ACCEPT
CONTINUE
SUSPEND
REINSTATE
REVOKE
CLOSE
REOPEN
DEFER
ESCALATE
ACCEPT RISK
```

The applicable decision vocabulary SHALL be governed by policy.

---

# 6. Decision Lifecycle

```text
PROPOSED
   ↓
PREPARED
   ↓
REVIEWED
   ↓
AUTHORISED
   ↓
DECIDED
   ↓
PUBLISHED
   ↓
EFFECTIVE
   ↓
MONITORED
   ↓
EXPIRED / CLOSED / REVOKED
```

Alternative paths:

```text
REJECTED
DEFERRED
ESCALATED
SUSPENDED
REOPENED
```

---

# 7. Decision Criteria

A decision SHALL be evaluated against explicit criteria.

Criteria MAY include:

```text
Mandatory Requirements
Acceptance Criteria
Risk Tolerance
Control Status
Evidence Sufficiency
Assurance Outcome
Materiality
Authority
Exception Status
Monitoring Status
```

---

# 8. Mandatory vs Discretionary Criteria

Criteria SHALL be classified as:

```text
MANDATORY
```

or:

```text
DISCRETIONARY
```

Failure of a mandatory criterion SHALL block acceptance unless an explicitly governed exception mechanism applies.

---

# 9. Decision Inputs

A decision MAY consume:

```text
Evidence
Assurance
Risk
Materiality
Findings
Incidents
Exceptions
Remediation
Monitoring
Authority
Policy
Rules
```

The source and version of each material input SHALL be retained.

---

# 10. Decision Readiness

A case is decision-ready only when required inputs are available.

Conceptual logic:

```text
REQUIRED INPUTS
      ↓
COMPLETE?
 ┌────┴─────┐
NO          YES
 │           │
 ▼           ▼
BLOCK      DECISION
```

Missing information SHALL not silently become an acceptable result.

---

# 11. Decision Package

A material decision SHOULD use a structured decision package containing:

```text
Executive Summary
Decision Requested
Criteria
Evidence
Assurance
Risk
Materiality
Findings
Exceptions
Conditions
Alternatives
Recommendation
Authority
```

---

# 12. Decision Rationale

Every material decision SHALL have a rationale explaining:

```text
What was decided
Why it was decided
Which evidence supports it
Which criteria were applied
Which risks remain
Which conditions apply
```

Rationale SHALL be understandable independently of the decision maker's memory.

---

# 13. Decision Authority

The authority model from RG-413 SHALL determine:

```text
Who may decide
Decision Limit
Scope
Delegation
Conditions
Expiry
Escalation
```

Authority SHALL be valid at the time of decision.

---

# 14. Delegated Authority

Delegation SHALL define:

```text
Delegator
Delegate
Scope
Limit
Effective Period
Conditions
Revocation
```

A delegate SHALL not exceed the delegated authority.

---

# 15. Authority Validation

Before a decision is recorded:

```text
IDENTITY
   ↓
ROLE
   ↓
AUTHORITY
   ↓
SCOPE
   ↓
VALIDITY
   ↓
DECISION
```

Invalid authority SHALL block the decision.

---

# 16. Acceptance

Acceptance means the authorised decision maker has determined that defined acceptance criteria are satisfied.

Acceptance SHALL identify:

```text
Accepted Subject
Criteria
Evidence
Assurance
Residual Risk
Conditions
Authority
Validity
```

---

# 17. Conditional Acceptance

Conditional acceptance MAY be used where defined conditions remain.

```text
ACCEPTED
   +
CONDITIONS
   ↓
MONITORED RELIANCE
```

Conditions SHALL be:

```text
Specific
Owned
Time-Bound
Measurable
Auditable
```

---

# 18. Acceptance Conditions

Examples:

```text
Enhanced Monitoring
Outstanding Low-Risk Action
Temporary Exception
Additional Review
Observation Period
Restricted Scope
```

A condition that is effectively mandatory for acceptance SHALL not be hidden as a note.

---

# 19. Acceptance vs Risk Acceptance

The architecture SHALL distinguish:

```text
ACCEPTANCE
= SUBJECT MEETS GOVERNED ACCEPTANCE CONDITIONS

RISK ACCEPTANCE
= AUTHORISED DECISION TO TOLERATE RESIDUAL RISK
```

Risk acceptance does not automatically establish compliance or technical acceptance.

---

# 20. Acceptance vs Assurance

Assurance provides confidence.

Acceptance is the governance decision.

```text
ASSURANCE
   ↓
RECOMMENDATION / INPUT
   ↓
AUTHORISED DECISION
   ↓
ACCEPTANCE
```

An assurance provider SHALL not automatically become the acceptance authority.

---

# 21. Rejection

Rejection SHALL record:

```text
Failed Criteria
Evidence
Risk
Materiality
Rationale
Authority
Required Next Action
```

Rejection SHALL not destroy the evidence that supported the decision.

---

# 22. Deferral

Deferral may be used when a decision cannot yet be responsibly made.

It SHALL record:

```text
Reason
Missing Input
Risk
Required Action
Owner
New Decision Date
Authority
```

Deferral SHALL not become an indefinite holding state.

---

# 23. Decision Conditions

Conditions MAY include:

```text
Monitoring
Remediation
Evidence Update
Risk Reduction
Control Improvement
External Approval
Time-Limited Exception
```

Conditions SHALL have lifecycle status.

---

# 24. Condition Monitoring

Every material acceptance condition SHALL be monitored where appropriate.

```text
CONDITION
   ↓
MONITOR
   ↓
SATISFIED / BREACHED / EXPIRED
```

Condition breach MAY trigger:

```text
REVIEW
ESCALATION
SUSPENSION
REOPENING
```

---

# 25. Reliance

Reliance is the authorised use of an accepted outcome.

Examples:

```text
Operational Reliance
Compliance Reliance
Customer Reliance
Decision Reliance
Reporting Reliance
System Reliance
```

Reliance SHALL define purpose and scope.

---

# 26. Reliance Scope

Reliance SHALL specify:

```text
Who May Rely
What May Be Relied Upon
For Which Purpose
For Which Population
For Which Period
Under Which Conditions
```

Acceptance without a defined reliance scope MAY be insufficient for downstream use.

---

# 27. Reliance Conditions

Reliance MAY depend on:

```text
Current Version
Valid Evidence
Active Controls
Current Risk
No Material Regression
Active Authority
No Expired Conditions
```

---

# 28. Reliance Validity

Reliance SHALL not necessarily be permanent.

Validity MAY end because of:

```text
Expiry
Material Change
Regression
Risk Increase
Evidence Invalidation
Authority Expiry
Policy Change
Dependency Change
Model Change
Condition Breach
```

---

# 29. Reliance Revocation

Reliance MAY be revoked when the basis for reliance is no longer valid.

```text
RELIANCE
   ↓
VALIDITY FAILURE
   ↓
REVOKE / SUSPEND
   ↓
REASSESS
```

Revocation SHALL be auditable.

---

# 30. Suspension

Suspension temporarily withdraws reliance or operating status while the underlying condition is assessed.

Suspension SHALL identify:

```text
Trigger
Scope
Start
Authority
Conditions for Reinstatement
Review Date
```

---

# 31. Suspension vs Rejection

```text
SUSPENSION
= TEMPORARY WITHDRAWAL PENDING REVIEW

REJECTION
= ACCEPTANCE CRITERIA NOT SATISFIED
```

The distinction SHALL be preserved.

---

# 32. Reinstatement

Reinstatement SHALL require evidence that the suspension condition has been resolved.

Possible requirements:

```text
Remediation
Verification
Assurance
Risk Reassessment
Authority Approval
```

Reinstatement SHALL create a new decision record rather than silently reversing history.

---

# 33. Revocation

Revocation permanently withdraws a previously granted authority, acceptance or reliance within its defined scope.

Revocation SHALL identify:

```text
Original Decision
Revocation Trigger
Reason
Authority
Effective Time
Affected Reliance
Required Follow-Up
```

---

# 34. Closure

Closure is the formal completion of a governed lifecycle stage.

Closure SHALL require:

```text
Required Criteria Satisfied
Required Evidence Present
Outstanding Conditions Resolved
Residual Risk Addressed
Required Assurance Complete
Authority Confirmed
```

---

# 35. Administrative Closure

Administrative closure SHALL not be used to disguise unresolved material conditions.

If a case is closed for administrative reasons:

```text
Closure Type = ADMINISTRATIVE
```

shall remain explicit.

---

# 36. Closure Outcomes

Possible outcomes:

```text
CLOSED — ACCEPTED
CLOSED — RESOLVED
CLOSED — REJECTED
CLOSED — SUPERSEDED
CLOSED — TRANSFERRED
CLOSED — ACCEPTED RISK
```

Outcome SHALL be explicit.

---

# 37. Closure vs Resolution

The architecture SHALL distinguish:

```text
RESOLUTION
= CONDITION ADDRESSED

CLOSURE
= AUTHORISED GOVERNANCE DECISION THAT THE LIFECYCLE MAY END
```

A resolved technical issue may remain open for assurance or governance purposes.

---

# 38. Closure Verification

Closure SHALL reference verification and/or assurance evidence as required.

```text
REMEDIATION
   ↓
VERIFICATION
   ↓
ASSURANCE
   ↓
CLOSURE DECISION
```

---

# 39. Closure Conditions

Conditional closure MAY be permitted only where policy explicitly allows it.

Conditions SHALL be:

```text
Low Risk
Controlled
Monitored
Time-Bound
Owned
```

---

# 40. Reopening

A closed case MAY be reopened because of:

```text
Recurrence
Material New Evidence
Assurance Failure
Control Failure
Risk Increase
Condition Breach
Incorrect Closure
Fraud / Integrity Concern
```

Reopening SHALL preserve the original closure decision.

---

# 41. Decision Supersession

A new decision MAY supersede an earlier decision.

The relationship SHALL be:

```text
Decision A
   ↓
SUPERSEDED BY
   ↓
Decision B
```

Decision A SHALL remain historically valid for the period in which it was effective.

---

# 42. Decision Versioning

Decisions SHALL be immutable as historical records.

Changes SHALL create:

```text
NEW DECISION VERSION / NEW DECISION RECORD
```

rather than silently overwriting the original.

---

# 43. Effective Time

Every material decision SHOULD identify:

```text
Decision Time
Effective From
Effective Until
```

This supports temporal reconstruction.

---

# 44. Retroactive Decisions

Retroactive decisions SHALL be exceptional.

They SHALL identify:

```text
Reason
Authority
Affected Period
Evidence
Impact
```

Retroactivity SHALL not rewrite historical system state without explicit governance.

---

# 45. Temporal Decision Logic

A decision is valid only when:

```text
Decision Date
+
Authority Validity
+
Criteria Version
+
Evidence Validity
```

are consistent with the applicable period.

---

# 46. Decision Precedence

Where decisions conflict, precedence SHALL be governed.

Potential factors:

```text
Authority Level
Specificity
Effective Time
Scope
Policy Priority
Emergency Status
```

No implicit precedence SHALL be assumed.

---

# 47. Conflicting Decisions

The system SHALL detect conflicting decisions.

Example:

```text
Decision A → ACCEPT
Decision B → SUSPEND
Same Subject / Same Period
```

Conflict SHALL trigger controlled resolution.

---

# 48. Decision Resolution

Resolution SHALL identify:

```text
Conflict
Applicable Authority
Precedence Rule
Decision
Rationale
Affected Decisions
```

---

# 49. Decision Dependencies

A decision MAY depend on:

```text
Risk Assessment
Assurance
External Approval
Remediation
Exception
Monitoring
```

Dependencies SHALL be explicit.

---

# 50. Dependency Failure

If a material dependency becomes invalid:

```text
DECISION BASIS INVALID
   ↓
REASSESS
   ↓
CONTINUE / SUSPEND / REVOKE / REOPEN
```

The system SHALL not silently retain reliance.

---

# 51. Decision Conditions and Risk

Acceptance conditions SHALL be evaluated against RG-415 risk tolerances.

Example:

```text
Residual Risk > Tolerance
      ↓
UNCONDITIONAL ACCEPTANCE BLOCKED
```

Possible response:

```text
Remediation
Exception
Escalation
Risk Acceptance
Rejection
```

---

# 52. Decision and Materiality

Materiality SHALL influence the required decision authority and assurance depth.

A material decision SHALL not be reduced to an administrative workflow.

---

# 53. Decision and Monitoring

RG-416 SHALL monitor the continuing validity of decisions.

```text
ACCEPTANCE
   ↓
MONITOR
   ↓
CHANGE DETECTED
   ↓
REASSESS
```

---

# 54. Decision and Finding

A material finding may invalidate the basis of an acceptance decision.

```text
ACCEPTANCE
   ↓
NEW FINDING
   ↓
IMPACT ASSESSMENT
   ↓
CONTINUE / SUSPEND / REOPEN
```

---

# 55. Decision and Incident

A material incident MAY trigger review of affected decisions and reliance.

The system SHOULD identify all decisions potentially affected by an incident.

---

# 56. Decision and Exception

Acceptance MAY depend on an active exception.

The system SHALL track:

```text
Acceptance
   ↓
Exception
```

If the exception expires, the acceptance basis SHALL be reassessed.

---

# 57. Decision and Remediation

Conditional acceptance MAY depend on remediation.

```text
ACCEPTANCE CONDITION
   ↓
REMEDIATION
   ↓
VERIFICATION
   ↓
CONDITION SATISFIED
```

---

# 58. Decision and Assurance

RG-419 provides assurance input.

The decision record SHALL retain:

```text
Assurance ID
Assurance Version
Conclusion
Conditions
Limitations
Assurance Date
```

---

# 59. Decision Package Integrity

The decision package SHALL identify all material evidence and references used.

No material input SHALL be silently omitted from the decision record.

---

# 60. Decision Transparency

The level of explanation SHALL be proportional to:

```text
Risk
Materiality
Impact
Audience
Regulatory Requirement
```

Critical decisions SHALL have sufficient rationale for independent reconstruction.

---

# 61. Human Decision

Where policy requires human authority, automation SHALL prepare but not silently decide.

```text
AUTOMATED PREPARATION
      ↓
HUMAN REVIEW
      ↓
AUTHORISED DECISION
```

---

# 62. Automated Decision

Automated decisions MAY be used only where policy explicitly permits them.

The system SHALL record:

```text
Decision Rule
Rule Version
Inputs
Result
Authority Model
Timestamp
```

---

# 63. AI-Assisted Decision

AI MAY support:

```text
Recommendation
Evidence Summarisation
Risk Analysis
Conflict Detection
Decision Drafting
```

AI SHALL not silently exercise authority it has not been granted.

---

# 64. AI Decision Controls

Material AI-assisted decisions SHOULD preserve:

```text
Model
Model Version
Prompt / Instruction Context where appropriate
Inputs
Output
Human Review
Final Decision Maker
Overrides
```

---

# 65. Override

A decision override SHALL record:

```text
Original Recommendation
Override Decision
Reason
Authority
Evidence
Time
Impact
```

Override SHALL not erase the original recommendation.

---

# 66. Four-Eyes Decision

Critical decisions SHOULD require two-person approval where policy/risk requires.

```text
DECISION PREPARER
      ↓
DECISION REVIEWER
      ↓
AUTHORITY
      ↓
FINAL DECISION
```

---

# 67. Decision Escalation

Decisions SHALL escalate when:

```text
Risk Above Authority Limit
Materiality Above Limit
Conflict Exists
Evidence Inconclusive
Assurance Not Available
Exception Expired
Critical Incident
Authority Unclear
```

---

# 68. Decision Deadline

Decision requests MAY have deadlines.

Overdue decisions SHALL trigger:

```text
Reminder
Escalation
Risk Review
```

The system SHALL not auto-approve merely because a deadline expires.

---

# 69. Decision Expiry

Time-limited decisions SHALL expire according to defined conditions.

Expiry SHALL trigger:

```text
Review
Renewal
Suspension
Revalidation
```

---

# 70. Renewal

Renewal SHALL be a new governed decision.

It SHALL reassess:

```text
Current Evidence
Current Risk
Current Criteria
Current Authority
Current Monitoring
Changes Since Previous Decision
```

---

# 71. Reliance Renewal

Reliance renewal SHALL not assume that historical acceptance remains valid indefinitely.

Current conditions SHALL be evaluated.

---

# 72. Closure Review

Before closure:

```text
Open Findings = acceptable?
Open Incidents = none / controlled?
Exceptions = resolved / authorised?
Remediation = effective?
Assurance = sufficient?
Risk = acceptable?
Conditions = satisfied?
```

The exact criteria SHALL be policy-controlled.

---

# 73. Decision Quality

Decision quality SHOULD be assessed through:

```text
Evidence Sufficiency
Criteria Completeness
Authority Validity
Risk Awareness
Assurance Quality
Outcome Accuracy
Post-Decision Stability
```

---

# 74. Post-Decision Review

High-risk decisions SHOULD receive post-decision review.

Review MAY assess:

```text
Was decision correct?
Did assumptions hold?
Did conditions remain valid?
Did unexpected impacts occur?
Was reliance appropriate?
```

---

# 75. Decision Effectiveness

A decision is effective when:

```text
Intended Governance Outcome
+
Stable Validity
+
Acceptable Risk
+
No Material Uncontrolled Regression
```

Effectiveness SHALL be monitored where appropriate.

---

# 76. Decision Failure

If a decision proves incorrect:

```text
DECISION FAILURE
   ↓
IMPACT ASSESSMENT
   ↓
SUSPEND / REVOKE / REOPEN
   ↓
REASSESS
```

The original decision SHALL remain historically traceable.

---

# 77. Decision Learning

Decision outcomes SHOULD feed:

```text
Risk Models
Policy
Rules
Thresholds
Assurance Planning
Monitoring
Training
```

Changes SHALL follow governance.

---

# 78. Decision Audit

Material decisions SHALL create audit events:

```text
Decision Prepared
Decision Reviewed
Decision Approved
Decision Published
Decision Effective
Decision Suspended
Decision Revoked
Decision Renewed
Decision Reopened
Decision Closed
```

---

# 79. Decision Data Model

Core entities:

```text
Decision
DecisionCriteria
DecisionInput
DecisionPackage
Acceptance
Reliance
Condition
Suspension
Reinstatement
Revocation
ClosureDecision
DecisionReview
DecisionOverride
```

Relationships:

```text
Evidence
 ↓
Assurance
 ↓
Decision
 ├── Acceptance
 ├── Reliance
 ├── Conditions
 ├── Suspension
 └── Closure
```

---

# 80. MFM Service Boundary

The conceptual implementation should include:

```text
Decision Service
Acceptance Service
Reliance Service
Condition Service
Suspension Service
Reinstatement Service
Revocation Service
Closure Service
Decision Review Service
Decision Package Service
```

These integrate with:

```text
Policy
Rules
Risk
Materiality
Monitoring
Finding
Incident
Exception
Remediation
Assurance
Authority
Evidence
Workflow
State
Audit
```

services.

---

# 81. API Concepts

Illustrative operations:

```text
prepareDecision()
validateDecisionReadiness()
evaluateDecisionCriteria()
requestApproval()
approveDecision()
rejectDecision()
acceptSubject()
createReliance()
suspendReliance()
reinstateReliance()
revokeReliance()
renewDecision()
closeCase()
reopenDecision()
```

These are architectural concepts, not implementation-specific commitments.

---

# 82. Decision Reporting

The system SHOULD support:

```text
Current Accepted Items
Conditional Acceptances
Suspended Items
Rejected Items
Expiring Decisions
Reliance Dependencies
Overdue Decisions
Decisions by Authority
Decisions Above Risk Threshold
Reopened Decisions
```

---

# 83. Decision Register

A controlled decision register SHOULD provide:

```text
Decision ID
Subject
Outcome
Authority
Effective Period
Risk
Conditions
Reliance
Status
```

The register SHALL be historically reconstructable.

---

# 84. Reliance Register

A reliance register MAY track:

```text
Reliance ID
Decision
Consumer
Purpose
Scope
Effective Period
Conditions
Status
Revocation
```

---

# 85. Closure Register

Closure records SHOULD include:

```text
Closure ID
Subject
Closure Type
Evidence
Assurance
Residual Risk
Authority
Date
Conditions
Outcome
```

---

# 86. Security

Decision and acceptance records SHALL be protected against:

```text
Unauthorised Approval
Authority Spoofing
Decision Modification
Evidence Substitution
Unauthorised Disclosure
Retroactive Manipulation
```

---

# 87. Integrity

Historical decision records SHALL be immutable or tamper-evident.

Corrections SHALL use controlled supersession or amendment mechanisms.

---

# 88. Retention

Decision records SHALL be retained according to:

```text
Decision Importance
Risk
Regulation
Contract
Audit
Legal Requirements
```

---

# 89. Failure Handling

If the decision service is unavailable:

```text
DECISION PENDING
   ↓
NO ACCEPTANCE
   ↓
RECOVERY / MANUAL GOVERNED PROCESS
```

Technical failure SHALL never create implicit acceptance.

---

# 90. Continuity

Critical decision processes MAY require:

```text
Alternate Authority
Manual Decision Procedure
Backup System
Emergency Approval Route
```

Emergency decisions SHALL be reconciled into the authoritative system.

---

# 91. Emergency Decisions

Emergency decisions SHALL record:

```text
Trigger
Urgency
Authority
Decision
Risk
Scope
Duration
Follow-Up
```

Emergency status SHALL not eliminate later review.

---

# 92. Testing

The decision architecture SHALL test:

```text
Decision Readiness
Mandatory Criteria
Authority
Conditional Acceptance
Rejection
Deferral
Suspension
Reinstatement
Revocation
Closure
Reopening
Expiry
Renewal
Conflicting Decisions
Override
AI Assistance
Automated Decision
```

---

# 93. Negative Testing

The system SHALL verify:

```text
Missing mandatory criterion → BLOCK
Invalid authority → BLOCK
Expired evidence → BLOCK / REVIEW
Expired exception → BLOCK
Inconclusive assurance → NO UNQUALIFIED ACCEPTANCE
Risk above authority limit → ESCALATE
Conflicting decision → RESOLUTION REQUIRED
Expired acceptance → NO CONTINUED RELIANCE
Unauthorised override → BLOCK
Deadline expiry → NO AUTO-ACCEPTANCE
```

---

# 94. Scenario Testing

Representative scenarios:

```text
Normal acceptance
Conditional acceptance
Rejected acceptance
High-risk acceptance
Temporary exception
Assurance inconclusive
Critical incident after acceptance
Evidence invalidation
Decision expiry
Reliance suspension
Reinstatement after remediation
Conflicting authorities
Emergency decision
AI-assisted recommendation
Post-closure recurrence
```

---

# 95. Acceptance Criteria

EA-IMETA-PC-RG-420 is accepted when:

- decision and assurance are distinct;
- acceptance and risk acceptance are distinct;
- reliance has explicit scope and validity;
- suspension, revocation and rejection are distinct;
- closure is an authorised governance outcome;
- decision criteria are explicit;
- mandatory criteria cannot be silently bypassed;
- authority is validated;
- conditional acceptance is controlled;
- decision dependencies are explicit;
- expiry and renewal are supported;
- reopening preserves historical decisions;
- conflicting decisions are detected;
- automated and AI-assisted decisions are governed;
- monitoring can invalidate or trigger reassessment;
- decision records are immutable or tamper-evident;
- negative tests prevent implicit or unauthorised acceptance;
- all relevant architecture layers are integrated.

---

# 96. Next Step

The next logical artifact is the **PC-RG post-closure surveillance and continuing-reliance model**, because RG-420 establishes acceptance and reliance, while the architecture now needs to define how accepted decisions remain valid after closure and how continuing monitoring can trigger reassessment without destroying historical closure.

Provisional next artifact:

> **EA-IMETA-PC-RG-421 — POST-CLOSURE SURVEILLANCE & CONTINUING RELIANCE MODEL**

This will establish the controlled lifecycle after formal acceptance and closure.

---

# 97. Governing Principle

> **Acceptance authorises reliance under defined conditions; reliance remains valid only while its basis remains valid; closure ends a governed lifecycle stage but does not erase historical responsibility; material change, regression, invalid evidence or risk increase can require reassessment.**

The PC-RG architecture SHALL therefore treat closure as a controlled decision point—not as the disappearance of governance.

# END OF EA-IMETA-PC-RG-420
