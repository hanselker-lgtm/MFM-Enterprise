# EA-IMETA-PC-RG-410

## LIFECYCLE STATE MACHINE & TRANSITION CONTROL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-410 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Lifecycle State Machine & Transition Control |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-409 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define the authoritative lifecycle states, permitted transitions, guards, authorities, consequences and audit requirements for PC-RG |
| Architectural Boundary | State → Trigger → Guard → Authority → Transition → Evidence → Consequence |

---

# 2. Purpose

EA-IMETA-PC-RG-410 defines the formal state machine for the consolidated PC-RG architecture.

The purpose is to remove ambiguity from lifecycle status.

A status SHALL represent a real state of the governed subject and SHALL change only through an authorised transition.

The governing principle is:

> **A state is a controlled condition, not a label.**

---

# 3. Why a State Machine Is Required

Without explicit state transitions, systems can produce contradictory conditions such as:

```text
CLOSED
+
OPEN REMEDIATION
+
ACCEPTED
+
REVOKED
```

at the same time without defining which condition is authoritative.

The state machine establishes:

```text
ONE AUTHORITATIVE CURRENT STATE
+
CONTROLLED TRANSITIONS
+
EXPLICIT EXCEPTIONS
+
AUDITABLE HISTORY
```

---

# 4. Canonical Lifecycle

The primary lifecycle is:

```text
DRAFT
  ↓
IN REVIEW
  ↓
VALIDATED
  ↓
VERIFIED
  ↓
ACCEPTED
  ↓
CLOSED
  ↓
MONITORED
```

Post-closure branch:

```text
MONITORED
    ↓
CHANGE / ALERT
    ↓
REGRESSION ASSESSMENT
    │
    ├── NO MATERIAL REGRESSION → MONITORED
    │
    └── MATERIAL REGRESSION
             ↓
         REGRESSION
             ↓
         REMEDIATION
             ↓
         REVALIDATION
             ↓
         REVERIFICATION
             ↓
         REACCEPTANCE
             ↓
           CLOSED
             ↓
         MONITORED
```

---

# 5. State Definitions

## 5.1 DRAFT

The case exists but has not entered formal review.

Required minimum:

- subject identified;
- owner identified;
- scope defined.

No acceptance or reliance is permitted.

---

## 5.2 IN REVIEW

The case is undergoing formal assessment.

Required:

- criteria identified;
- evidence collection active;
- responsible assessor assigned.

---

## 5.3 VALIDATED

The current state satisfies the applicable validation criteria.

Validation does not itself authorise reliance.

---

## 5.4 VERIFIED

The validation has been independently or appropriately verified according to the governing verification requirements.

Verification does not itself constitute acceptance.

---

## 5.5 ACCEPTED

An authorised decision-maker has approved reliance on the verified result.

Acceptance SHALL include:

- authority;
- decision;
- scope;
- conditions;
- effective period where applicable.

---

## 5.6 CLOSED

The current lifecycle activity has been formally completed.

Closure does not mean the subject can never change.

---

## 5.7 MONITORED

The accepted/closed state is subject to ongoing observation.

Monitoring SHALL define:

- baseline;
- indicators;
- thresholds;
- frequency;
- responsible owner;
- escalation.

---

## 5.8 REGRESSION

A material deviation from the approved baseline has been confirmed.

The state indicates that the prior accepted condition can no longer be relied upon without further action.

---

## 5.9 REMEDIATION

Corrective action is being performed to restore required conditions.

---

## 5.10 REVALIDATION

The corrected/current state is being assessed against applicable criteria.

---

## 5.11 REVERIFICATION

The revalidation result is being checked for correctness and required assurance.

---

## 5.12 REACCEPTANCE

An authorised decision-maker restores reliance following successful revalidation and reverification.

---

# 6. Exceptional States

The state machine SHALL support:

```text
SUSPENDED
REJECTED
REVOKED
FAILED
INCONCLUSIVE
REOPENED
BLOCKED
```

These states SHALL have defined entry and exit conditions.

---

# 7. State Transition Model

| From | Trigger | Guard | To |
|---|---|---|---|
| DRAFT | Submit | Required data present | IN REVIEW |
| IN REVIEW | Validation complete | Criteria satisfied | VALIDATED |
| IN REVIEW | Validation fails | Material failure | REJECTED |
| VALIDATED | Verification complete | Verification passes | VERIFIED |
| VALIDATED | Verification fails | Material failure | FAILED |
| VERIFIED | Acceptance decision | Authority + criteria satisfied | ACCEPTED |
| VERIFIED | Acceptance rejected | Authorised decision | REJECTED |
| ACCEPTED | Closure | Closure criteria satisfied | CLOSED |
| CLOSED | Monitoring starts | Monitoring plan active | MONITORED |
| MONITORED | Alert | Change detected | REGRESSION ASSESSMENT |
| REGRESSION ASSESSMENT | No material change | Assessment complete | MONITORED |
| REGRESSION ASSESSMENT | Material change | Evidence sufficient | REGRESSION |
| REGRESSION | Remediation starts | Action authorised | REMEDIATION |
| REMEDIATION | Correction complete | Evidence available | REVALIDATION |
| REVALIDATION | Validation passes | Criteria satisfied | REVERIFICATION |
| REVALIDATION | Validation fails | Material failure | REMEDIATION |
| REVERIFICATION | Verification passes | Required assurance met | REACCEPTANCE |
| REVERIFICATION | Verification fails | Material failure | REVALIDATION |
| REACCEPTANCE | Acceptance granted | Authority + risk acceptable | CLOSED |
| Any applicable state | Reopen | Authorised trigger | REOPENED |
| ACCEPTED / MONITORED | Material invalidation | Authorised decision | REVOKED |
| Any applicable state | Suspension trigger | Defined condition | SUSPENDED |

---

# 8. Transition Guard

No transition SHALL occur without its required guard conditions.

A transition guard SHALL define:

```text
Preconditions
Evidence
Criteria
Authority
Dependencies
Risk
Required approvals
```

Example:

```text
VERIFIED → ACCEPTED

GUARDS:
✓ verification result valid
✓ evidence current
✓ acceptance authority present
✓ conditions understood
✓ risk within tolerance
✓ no blocking defect
```

---

# 9. Transition Authority

Each transition SHALL identify an authorised actor.

Minimum authority categories:

```text
CASE OWNER
ASSESSOR
VERIFIER
ACCEPTANCE AUTHORITY
CLOSURE AUTHORITY
MONITORING OWNER
REMEDIATION OWNER
INDEPENDENT REVIEWER
SYSTEM ADMINISTRATOR
```

A technical permission SHALL not automatically create business decision authority.

---

# 10. State Invariants

The system SHALL enforce invariants.

Examples:

```text
ACCEPTED ⇒ VERIFIED
VERIFIED ⇒ VALIDATED
CLOSED ⇒ required closure criteria satisfied
MONITORED ⇒ valid baseline exists
REACCEPTED ⇒ revalidation + reverification successful
REVOKED ⇒ reliance prohibited
SUSPENDED ⇒ reliance restricted according to policy
```

Invalid combinations SHALL be rejected.

---

# 11. State Exclusivity

For a single lifecycle case, exactly one primary lifecycle state SHALL be authoritative.

Supporting sub-states may exist, but they SHALL not create ambiguity about the primary state.

Example:

```text
PRIMARY STATE:
REMEDIATION

SUB-STATE:
Awaiting supplier evidence
```

not:

```text
PRIMARY STATE:
CLOSED + REMEDIATION
```

---

# 12. State History

Every state transition SHALL create an immutable audit event.

Required attributes:

```text
Case ID
Previous State
New State
Trigger
Actor
Authority
Timestamp
Reason
Evidence
Decision ID
Correlation ID
```

---

# 13. Illegal Transition Handling

An illegal transition SHALL be rejected.

Example:

```text
DRAFT → ACCEPTED
```

shall fail because:

```text
VALIDATION missing
VERIFICATION missing
required acceptance evidence missing
```

The failed attempt SHOULD itself be auditable where security or governance risk warrants it.

---

# 14. Rollback

State rollback SHALL not be implemented as silent deletion of history.

Instead:

```text
CURRENT STATE
    ↓
CORRECTIVE TRANSITION
    ↓
NEW STATE
```

Example:

```text
ACCEPTED
    ↓
REVOCATION
    ↓
REVOKED
```

The system SHALL preserve the fact that the case was previously accepted.

---

# 15. Reopening

Reopening SHALL be an explicit transition.

```text
CLOSED
   ↓
REOPEN REQUEST
   ↓
AUTHORITY CHECK
   ↓
REOPENED
```

The reopening record SHALL contain:

- reason;
- authority;
- scope;
- affected requirements;
- affected controls;
- required reassessment;
- target closure conditions.

---

# 16. Suspension

Suspension is temporary restriction.

```text
ACCEPTED / MONITORED
        ↓
SUSPENSION TRIGGER
        ↓
SUSPENDED
```

Suspension SHALL define:

```text
what is prohibited;
what remains permitted;
who may lift suspension;
evidence required;
expiry/review;
escalation.
```

---

# 17. Revocation

Revocation is stronger than suspension.

```text
ACCEPTED
    ↓
MATERIAL INVALIDATION
    ↓
REVOKED
```

Revocation SHALL invalidate reliance within its defined scope.

Restoration SHALL require:

```text
REVALIDATION
+
REVERIFICATION
+
REACCEPTANCE
```

unless a formally approved alternative exists.

---

# 18. Inconclusive State

INCONCLUSIVE SHALL be used where available evidence cannot support a valid decision.

It SHALL NOT be interpreted as:

```text
VALID
```

or:

```text
INVALID
```

without further evidence.

---

# 19. Regression Assessment State

A monitoring event does not automatically equal regression.

The architecture SHALL distinguish:

```text
CHANGE DETECTED
        ↓
ASSESS MATERIALITY
        ↓
NO MATERIAL REGRESSION
        OR
MATERIAL REGRESSION
```

This prevents unnecessary remediation while ensuring material changes are not ignored.

---

# 20. Materiality Criteria

Materiality MAY be triggered by:

- mandatory criterion breach;
- significant risk increase;
- security degradation;
- compliance breach;
- control failure;
- dependency failure;
- evidence invalidation;
- material configuration change;
- data integrity issue;
- operating context change;
- loss of required authority;
- unacceptable performance degradation.

Thresholds SHALL be configurable by applicable domain policy.

---

# 21. Remediation State Machine

```text
REGRESSION
    ↓
REMEDIATION OPEN
    ↓
ACTION ASSIGNED
    ↓
ACTION IN PROGRESS
    ↓
ACTION COMPLETE
    ↓
REMEDIATION VERIFIED
    ↓
REVALIDATION
```

An action marked COMPLETE SHALL not automatically mean the remediation is successful.

---

# 22. Revalidation State Machine

```text
REVALIDATION REQUESTED
        ↓
EVIDENCE COLLECTION
        ↓
ASSESSMENT
        ↓
RESULT
   ┌────┼─────────┐
   ▼    ▼         ▼
VALID INVALID INCONCLUSIVE
   │      │         │
   ▼      ▼         ▼
REVERIFY REMEDIATE MORE EVIDENCE
```

---

# 23. Reverification State Machine

```text
REVALIDATED
    ↓
REVERIFICATION
    ↓
METHOD / EVIDENCE / AUTHORITY CHECK
    ↓
VERIFIED?
 ┌──┴──┐
YES    NO
 │      │
 ▼      ▼
REACCEPT REVALIDATE
```

---

# 24. Reacceptance State Machine

```text
REVERIFIED
    ↓
REACCEPTANCE REVIEW
    ↓
AUTHORITY
+
RISK
+
CONDITIONS
    ↓
DECISION
 ┌──┴──────┐
 ▼         ▼
ACCEPTED   REJECTED
```

---

# 25. Conditions

A state may be conditional.

A conditional state SHALL record:

```text
Condition ID
Description
Owner
Due Date
Evidence
Monitoring
Consequence
Review Date
```

Expired or breached conditions SHALL trigger the defined response.

---

# 26. Expiry

Where a state or decision has an expiry date:

```text
ACTIVE
  ↓
EXPIRING
  ↓
EXPIRED
```

Expiry SHALL not be silently renewed.

Renewal SHALL be an explicit authorised decision.

---

# 27. Dependencies

A state SHALL identify critical dependencies.

If a dependency fails:

```text
DEPENDENCY FAILURE
       ↓
MATERIAL?
   ┌───┴───┐
  NO      YES
   │        │
   ▼        ▼
MONITOR  SUSPEND /
         REGRESSION
```

---

# 28. Security State Controls

Security-relevant state transitions SHALL enforce:

```text
Authentication
Authorisation
Least Privilege
Separation of Duties
Session Validity
Audit
```

A user shall not bypass lifecycle guards through direct data manipulation.

---

# 29. Data Integrity

State changes SHALL be transactional.

The system SHALL prevent:

```text
STATE UPDATED
+
AUDIT EVENT FAILED
```

where this would create an untraceable business transition.

Where distributed architecture prevents atomicity, compensating controls SHALL preserve consistency.

---

# 30. Concurrency

Concurrent transitions SHALL be controlled.

Example:

```text
User A → ACCEPT
User B → REVOKE
```

The system SHALL prevent lost updates and SHALL establish deterministic conflict handling.

Recommended controls:

```text
version number
optimistic locking
transaction boundary
conflict detection
```

---

# 31. Idempotency

Repeat requests SHALL not create unintended duplicate transitions.

Example:

```text
REOPEN request submitted twice
```

shall not produce two independent reopening events.

The system SHALL identify duplicate commands where appropriate.

---

# 32. API State Enforcement

Lifecycle APIs SHALL enforce state rules server-side.

A UI restriction alone is insufficient.

Example:

```text
POST /accept
```

must verify:

```text
current_state == VERIFIED
+
authority
+
required evidence
+
risk
```

before changing the state.

---

# 33. UI State Enforcement

The UI SHALL display:

```text
Current State
Available Actions
Blocked Actions
Reason for Block
Required Evidence
Required Authority
Conditions
Expiry
```

Blocked actions SHOULD explain why they are unavailable.

---

# 34. Reporting State

Reports SHALL use the authoritative state machine.

The system SHALL not calculate status independently in multiple reports.

```text
ONE STATE MODEL
      ↓
ALL REPORTS
```

This prevents contradictory dashboards.

---

# 35. Notifications

State transitions MAY generate notifications.

Examples:

```text
REGRESSION CONFIRMED
REMEDIATION OVERDUE
REVALIDATION REQUIRED
ACCEPTANCE EXPIRING
SUSPENSION ENTERED
REVOCATION ENTERED
REACCEPTANCE REQUIRED
```

Notifications SHALL not themselves constitute state transitions.

---

# 36. AI and Agent Transitions

AI/agents SHALL not bypass state guards.

Where an agent proposes a transition:

```text
AGENT PROPOSAL
      ↓
VALIDATION
      ↓
AUTHORITY
      ↓
SYSTEM TRANSITION
```

The architecture SHALL record whether the transition was:

```text
HUMAN INITIATED
AI ASSISTED
AI PROPOSED
AUTOMATED
```

Decision authority SHALL remain explicitly governed.

---

# 37. State Machine Testing

Every permitted transition SHALL have at least one positive test.

Every prohibited critical transition SHALL have at least one negative test.

Example:

```text
VERIFIED → ACCEPTED
Positive: authorised acceptance succeeds.

VERIFIED → CLOSED
Negative: direct closure rejected.

DRAFT → ACCEPTED
Negative: rejected.

REVOKED → ACCEPTED
Negative: rejected until required recovery lifecycle completes.
```

---

# 38. Transition Test Matrix

| Transition | Positive Test | Negative Test | Evidence |
|---|---|---|---|
| DRAFT → IN REVIEW | Required data present | Missing required data | Audit + state |
| IN REVIEW → VALIDATED | Criteria satisfied | Criteria failure | Validation record |
| VALIDATED → VERIFIED | Verification passes | Verification fails | Verification record |
| VERIFIED → ACCEPTED | Authority valid | Unauthorised actor | Decision + audit |
| ACCEPTED → CLOSED | Closure criteria met | Outstanding closure item | Closure record |
| CLOSED → MONITORED | Monitoring active | No monitoring plan | Monitoring record |
| MONITORED → REGRESSION | Material change | Non-material change | Assessment |
| REGRESSION → REMEDIATION | Action authorised | No owner | Remediation record |
| REMEDIATION → REVALIDATION | Correction evidenced | Missing evidence | Revalidation request |
| REVALIDATION → REVERIFICATION | Valid result | Invalid result | Revalidation evidence |
| REVERIFICATION → REACCEPTANCE | Verified | Not verified | Verification record |
| REACCEPTANCE → CLOSED | Acceptance granted | Acceptance rejected | Decision |

---

# 39. State Metrics

The system SHOULD report:

```text
Cases by state
Average time in state
Blocked transitions
Failed transitions
Reopened cases
Suspended cases
Revoked cases
Regression rate
Remediation duration
Revalidation failure rate
Reacceptance failure rate
Expired conditions
Expired acceptances
```

Metrics SHALL be calculated from state history.

---

# 40. Audit and Forensics

The state history SHALL allow reconstruction of:

```text
WHO
DID WHAT
WHEN
FROM WHICH STATE
TO WHICH STATE
WHY
UNDER WHICH AUTHORITY
USING WHICH EVIDENCE
WITH WHICH DECISION
```

A current-state field alone is insufficient for audit reconstruction.

---

# 41. State Retention

Historical state transitions SHALL be retained according to applicable retention requirements.

Deleting history SHALL not be used to correct a mistaken transition.

Corrections SHALL create new auditable events.

---

# 42. Configuration and Versioning

The state machine itself SHALL be versioned.

Changes to:

```text
States
Transitions
Guards
Authorities
Materiality Rules
Required Evidence
```

SHALL be controlled changes.

Existing cases SHALL retain the applicable state-machine version where required.

---

# 43. Backward Compatibility

Changes to the state machine SHALL consider existing cases.

A migration plan SHALL exist when:

```text
OLD STATE
```

has no direct equivalent in the new model.

Migration SHALL preserve historical meaning.

---

# 44. MFM Data Model

The conceptual lifecycle record SHALL include:

```text
Case ID
Current State
State Version
Previous State
State Entered At
State Owner
State Conditions
State Expiry
Baseline ID
Decision ID
Authority
Version
```

State history SHALL be stored separately or in an append-only event structure.

---

# 45. Event Model

Recommended events:

```text
CaseCreated
ReviewStarted
Validated
VerificationCompleted
Accepted
Closed
MonitoringStarted
ChangeDetected
RegressionConfirmed
RemediationStarted
RemediationCompleted
RevalidationCompleted
ReverificationCompleted
Reaccepted
Suspended
Revoked
Reopened
```

Events SHALL contain sufficient context to reconstruct the lifecycle.

---

# 46. Failure and Recovery

A failed transition SHALL not leave the case in an undefined state.

```text
TRANSITION ATTEMPT
       ↓
SUCCESS → NEW STATE
       OR
FAILURE → ORIGINAL STATE + FAILURE EVENT
```

Where partial execution is unavoidable, compensating recovery SHALL be defined.

---

# 47. Governance Rules

No user, service or agent SHALL:

- directly assign an arbitrary lifecycle state;
- bypass mandatory guards;
- erase state history;
- approve without required authority;
- close a case with mandatory unresolved blockers;
- restore reliance without required recovery steps.

Emergency overrides SHALL require explicit authority and audit evidence.

---

# 48. Acceptance Criteria

EA-IMETA-PC-RG-410 is accepted when:

- every active state has a definition;
- every permitted transition has a trigger;
- every material transition has guards;
- authority is explicit;
- invalid transitions are rejected;
- state history is auditable;
- positive and negative tests exist;
- concurrency is controlled;
- APIs enforce state rules;
- UI reflects the authoritative state;
- AI/agents cannot bypass state controls;
- migration/versioning rules exist;
- recovery from failed transitions is defined.

---

# 49. Next Step

The next logical artifact is the **PC-RG event and workflow orchestration model**, because the state machine now defines what transitions are allowed, while orchestration must define how those transitions are initiated, sequenced, queued, escalated and completed.

Provisional next artifact:

> **EA-IMETA-PC-RG-411 — WORKFLOW & EVENT ORCHESTRATION MODEL**

This remains a concrete functional architecture artifact.

---

# 50. Governing Principle

> **Every material lifecycle state SHALL have an explicit meaning, every material transition SHALL have a defined authority and guard, and every state change SHALL be reconstructable from evidence and audit history.**

The PC-RG architecture therefore treats state as controlled system behaviour rather than descriptive text.

# END OF EA-IMETA-PC-RG-410
