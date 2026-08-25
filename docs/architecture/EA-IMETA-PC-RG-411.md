# EA-IMETA-PC-RG-411

## WORKFLOW & EVENT ORCHESTRATION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-411 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Workflow & Event Orchestration Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-410 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how lifecycle work is initiated, routed, sequenced, executed, escalated and completed |
| Architectural Boundary | Event → Workflow → Task → Decision → State Transition → Event |

---

# 2. Purpose

EA-IMETA-PC-RG-411 defines the workflow and event orchestration architecture for the PC-RG lifecycle.

EA-IMETA-PC-RG-410 defines which state transitions are permitted.

This document defines **how work reaches those transitions**.

The governing distinction is:

```text
STATE MACHINE
= WHAT IS ALLOWED

WORKFLOW
= WHAT WORK MUST HAPPEN

EVENT
= WHAT HAPPENED

ORCHESTRATION
= WHAT HAPPENS NEXT
```

The architecture SHALL keep these concepts separate.

---

# 3. Core Processing Loop

```text
EVENT
  ↓
EVENT VALIDATION
  ↓
WORKFLOW SELECTION
  ↓
TASK CREATION
  ↓
TASK EXECUTION
  ↓
TASK RESULT
  ↓
GUARD / DECISION
  ↓
STATE TRANSITION
  ↓
OUTCOME EVENT
  ↓
NEXT WORKFLOW / MONITORING
```

An event SHALL not automatically change lifecycle state unless a defined transition rule authorises that behaviour.

---

# 4. Event Model

An event represents a fact that has occurred.

Examples:

```text
CaseCreated
ReviewStarted
EvidenceAdded
ValidationCompleted
VerificationCompleted
AcceptanceRequested
AcceptanceGranted
ClosureRequested
MonitoringAlertRaised
ChangeDetected
RegressionConfirmed
RemediationStarted
RemediationCompleted
RevalidationCompleted
ReverificationCompleted
ReacceptanceGranted
SuspensionEntered
RevocationEntered
CaseReopened
```

Events SHALL describe facts, not commands disguised as facts.

---

# 5. Command vs Event

The architecture SHALL distinguish:

```text
COMMAND
"Start validation."

from:

EVENT
"Validation started."
```

A command requests an action.

An event records an outcome or fact.

Recommended pattern:

```text
COMMAND
  ↓
AUTHORISATION
  ↓
WORKFLOW
  ↓
ACTION
  ↓
EVENT
```

---

# 6. Event Structure

Every material event SHALL contain:

| Attribute | Required |
|---|---|
| Event ID | Yes |
| Event Type | Yes |
| Case ID | Yes |
| Subject ID | Yes |
| Source | Yes |
| Actor / Service | Yes |
| Timestamp | Yes |
| Correlation ID | Yes |
| Causation ID | Where applicable |
| State Before | Where applicable |
| State After | Where applicable |
| Payload Reference | Yes |
| Schema Version | Yes |
| Integrity Metadata | Where required |

---

# 7. Event Ordering

Events affecting the same lifecycle case SHALL have an unambiguous ordering mechanism.

The architecture SHOULD support:

```text
Sequence Number
Timestamp
Correlation ID
Causation ID
```

Timestamp alone SHALL not be assumed sufficient where concurrent events are possible.

---

# 8. Event Idempotency

Repeated delivery of the same event SHALL not create unintended duplicate business actions.

Example:

```text
RemediationCompleted
RemediationCompleted
```

The second delivery SHALL be recognised as duplicate where the event identity indicates the same occurrence.

---

# 9. Event Delivery

Events MAY be delivered:

```text
SYNCHRONOUSLY
ASYNCHRONOUSLY
BATCHED
RETRIED
QUEUED
```

The delivery model SHALL be explicit for each event class.

---

# 10. Event Failure

If event processing fails:

```text
EVENT
  ↓
PROCESSING FAILURE
  ↓
RETRY?
 ┌──┴──┐
YES    NO
 │      │
 ▼      ▼
RETRY  DEAD LETTER / ESCALATION
```

Failed processing SHALL not silently disappear.

---

# 11. Workflow Model

A workflow is an ordered set of activities required to achieve a defined lifecycle outcome.

Every workflow SHALL define:

```text
Workflow ID
Trigger
Preconditions
Tasks
Dependencies
Decision Points
Timeouts
Escalation
Failure Handling
Completion Criteria
Result Event
```

---

# 12. Workflow Lifecycle

```text
NOT STARTED
    ↓
READY
    ↓
RUNNING
    ↓
WAITING
    ↓
COMPLETING
    ↓
COMPLETED
```

Exception states:

```text
BLOCKED
FAILED
CANCELLED
TIMED OUT
SUSPENDED
```

---

# 13. Workflow Ownership

Every workflow SHALL have:

```text
Workflow Owner
Execution Owner
Decision Authority
Escalation Owner
```

Ownership SHALL remain explicit even when tasks are automated.

---

# 14. Task Model

A workflow SHALL decompose into executable tasks.

Each task SHALL contain:

```text
Task ID
Workflow ID
Task Type
Owner
Required Role
Input
Preconditions
Action
Expected Result
Due Date
Priority
Status
Evidence
Failure Path
Completion Event
```

---

# 15. Task States

```text
CREATED
ASSIGNED
READY
IN PROGRESS
WAITING
BLOCKED
COMPLETED
FAILED
CANCELLED
EXPIRED
```

A task SHALL not be considered completed solely because its deadline passed.

---

# 16. Dependency Model

Tasks may depend on:

```text
Previous Task
Evidence
Decision
External System
Approval
Data Availability
Time Condition
State
```

Dependencies SHALL be explicit.

Example:

```text
Verification Task
     ↓
depends on
     ↓
Validation Completed
+
Required Evidence Present
```

---

# 17. Sequential Workflow

Where order is mandatory:

```text
TASK A
  ↓
TASK B
  ↓
TASK C
```

Task B SHALL not start until the required completion condition for A is satisfied.

---

# 18. Parallel Workflow

Independent tasks MAY execute in parallel.

```text
             ┌── TASK A ──┐
START ───────┼── TASK B ──┼── JOIN
             └── TASK C ──┘
```

The JOIN condition SHALL define exactly which tasks are mandatory.

---

# 19. Conditional Workflow

```text
TASK
 ↓
DECISION
 ├── PATH A
 ├── PATH B
 └── ESCALATE
```

Decision criteria SHALL be explicit and auditable.

---

# 20. Human-in-the-Loop

Where human authority is required:

```text
AUTOMATED PREPARATION
        ↓
HUMAN REVIEW
        ↓
DECISION
        ↓
WORKFLOW CONTINUES
```

Automation SHALL not silently substitute for required human authority.

---

# 21. Validation Workflow

```text
Validation Requested
        ↓
Scope Check
        ↓
Criteria Load
        ↓
Evidence Collection
        ↓
Assessment
        ↓
Validation Decision
        ↓
ValidationCompleted
        ↓
State Transition
```

Possible outcomes:

```text
VALID
INVALID
CONDITIONAL
INCONCLUSIVE
```

---

# 22. Verification Workflow

```text
Verification Requested
        ↓
Validation Result Loaded
        ↓
Method / Evidence Check
        ↓
Independent Review
        ↓
Verification Decision
        ↓
VerificationCompleted
```

Failure SHALL route to the defined correction or revalidation path.

---

# 23. Acceptance Workflow

```text
Acceptance Requested
        ↓
Verify Current State
        ↓
Authority Check
        ↓
Risk Check
        ↓
Conditions Review
        ↓
Acceptance Decision
        ↓
AcceptanceGranted / Rejected
```

---

# 24. Closure Workflow

```text
Closure Requested
        ↓
Open Tasks Check
        ↓
Outstanding Evidence Check
        ↓
Conditions Check
        ↓
Monitoring Plan Check
        ↓
Closure Decision
        ↓
Closed
```

---

# 25. Monitoring Workflow

Monitoring MAY be scheduled or event-driven.

```text
MONITORING SCHEDULE
        ↓
COLLECT SIGNAL
        ↓
COMPARE BASELINE
        ↓
THRESHOLD CHECK
        ↓
NO MATERIAL CHANGE
      OR
REGRESSION ASSESSMENT
```

---

# 26. Regression Workflow

```text
ChangeDetected
      ↓
Create Regression Assessment
      ↓
Load Baseline
      ↓
Load Current State
      ↓
Compare Criteria
      ↓
Materiality Decision
 ┌────┴─────────┐
NO              YES
 │               │
 ▼               ▼
Monitoring    RegressionConfirmed
                 ↓
             Remediation
```

---

# 27. Remediation Workflow

```text
RegressionConfirmed
        ↓
Classify Finding
        ↓
Assign Owner
        ↓
Create Action Plan
        ↓
Execute Correction
        ↓
Collect Evidence
        ↓
Verify Remediation
        ↓
RemediationCompleted
        ↓
Revalidation
```

---

# 28. Revalidation Workflow

```text
Revalidation Requested
        ↓
Load Current State
        ↓
Load Current Criteria
        ↓
Collect Evidence
        ↓
Assessment
        ↓
Result
 ┌──────┼──────────┐
VALID INVALID INCONCLUSIVE
  │       │          │
  ▼       ▼          ▼
Reverify Remediate More Evidence
```

---

# 29. Reverification Workflow

```text
RevalidationCompleted
        ↓
Review Method
        ↓
Review Evidence
        ↓
Review Authority
        ↓
Decision
 ┌──────┴──────┐
VERIFIED      FAILED
   │             │
   ▼             ▼
Reacceptance  Revalidation
```

---

# 30. Reacceptance Workflow

```text
ReverificationCompleted
        ↓
Acceptance Review
        ↓
Risk / Conditions
        ↓
Authorised Decision
 ┌──────┴──────┐
GRANTED       REJECTED
   │             │
   ▼             ▼
Closed /       Restricted
Monitored      Recovery
```

---

# 31. Escalation Model

Escalation SHALL be based on defined conditions.

Examples:

```text
TASK OVERDUE
CONTROL FAILURE
MATERIAL REGRESSION
CRITICAL SECURITY EVENT
COMPLIANCE BREACH
DEPENDENCY FAILURE
DECISION DEADLOCK
INSUFFICIENT EVIDENCE
```

Escalation SHALL identify:

```text
Trigger
Recipient
Time Limit
Required Action
Consequence
```

---

# 32. Timeout Model

Every time-sensitive workflow SHALL define:

```text
Start
Deadline
Warning
Escalation
Expiry
Consequence
```

Timeout SHALL not silently produce success.

Example:

```text
Verification overdue
    ↓
Warning
    ↓
Escalation
    ↓
Workflow blocked
```

---

# 33. SLA Model

Where an SLA exists, the workflow SHALL record:

```text
SLA ID
Start Event
Target
Pause Conditions
Resume Conditions
Breach Condition
Escalation
Result
```

SLA clocks SHALL not be hidden in application code without traceability.

---

# 34. Queue Model

Work queues SHALL support:

```text
Priority
Owner
Role
Due Date
State
Dependency
Risk
Escalation
```

Priority SHALL be governed by explicit rules.

---

# 35. Retry Model

Retryable failures SHALL define:

```text
Retryable?
Maximum Attempts
Delay
Backoff
Idempotency
Escalation
Dead Letter Handling
```

Business decisions SHALL not be blindly retried.

---

# 36. Compensation Model

Where a workflow partially completes and cannot be rolled back:

```text
PARTIAL FAILURE
       ↓
COMPENSATING ACTION
       ↓
CONSISTENT STATE
       ↓
AUDIT
```

Compensation SHALL be explicitly defined for material workflows.

---

# 37. Transaction Boundary

State transitions and their required audit records SHOULD be committed as one logical transaction where technically possible.

Where distributed services are involved:

```text
COMMAND
 ↓
STATE CHANGE
 ↓
EVENT
 ↓
DOWNSTREAM PROCESSING
```

the architecture SHALL provide consistency and recovery mechanisms.

---

# 38. Event Correlation

Related commands, tasks and events SHALL share correlation information.

Example:

```text
Case ID
Workflow ID
Task ID
Command ID
Event ID
Causation ID
```

This permits complete workflow reconstruction.

---

# 39. Event Sourcing Boundary

Full event sourcing is not mandatory.

However, material lifecycle transitions SHALL retain sufficient events to reconstruct:

```text
Previous State
Action
Actor
Decision
New State
```

The implementation may use:

```text
Event Store
Audit Log
Transactional History
```

or an approved combination.

---

# 40. Notification Model

Notifications SHALL be downstream effects of events.

```text
EVENT
 ↓
NOTIFICATION RULE
 ↓
RECIPIENT
 ↓
MESSAGE
 ↓
DELIVERY
 ↓
DELIVERY RESULT
```

Notification delivery failure SHALL not silently alter the underlying lifecycle state.

---

# 41. Reporting Model

Reports SHALL consume authoritative workflow/state data.

They SHALL not create competing state calculations.

Recommended reports:

```text
Active Workflows
Blocked Tasks
Overdue Tasks
Open Regressions
Remediation Aging
Revalidation Queue
Reacceptance Queue
Escalations
SLA Performance
Workflow Failures
```

---

# 42. Security

Workflow actions SHALL enforce:

```text
Authentication
Authorisation
Role
Scope
Separation of Duties
Audit
```

Direct API access SHALL be subject to the same rules as UI access.

---

# 43. AI and Agent Orchestration

AI/agents may assist with:

```text
Task Preparation
Evidence Classification
Priority Suggestion
Anomaly Detection
Drafting
Routing Recommendation
```

Where agents execute workflow actions, the permitted action scope SHALL be explicit.

```text
AGENT
  ↓
PERMITTED ACTION?
 ├── NO → BLOCK
 └── YES
       ↓
GUARDS
       ↓
ACTION
       ↓
EVENT
```

Agents SHALL not infer authority from workflow context.

---

# 44. Agent Safety Boundary

Agent actions SHALL be classified:

```text
READ
SUGGEST
PREPARE
EXECUTE
APPROVE
```

Only explicitly authorised classes may be automated.

Material acceptance, revocation, reopening or other controlled decisions SHALL require the authority defined by the state machine.

---

# 45. Workflow Observability

Every material workflow SHALL expose:

```text
Current Status
Current Task
Owner
Elapsed Time
Next Action
Blocked By
SLA
Escalation
Last Event
Correlation ID
```

This allows operators to diagnose workflow problems without inspecting source code.

---

# 46. Workflow Audit

Audit SHALL capture:

```text
Workflow Started
Task Created
Task Assigned
Task Completed
Task Failed
Decision Made
State Transitioned
Escalation Raised
Retry Performed
Workflow Completed
Workflow Failed
Workflow Cancelled
```

---

# 47. Failure Taxonomy

Workflow failures SHALL be classified:

```text
DATA FAILURE
AUTHORITY FAILURE
DEPENDENCY FAILURE
TECHNICAL FAILURE
TIMEOUT
SECURITY FAILURE
COMPLIANCE FAILURE
HUMAN ACTION FAILURE
AI/AGENT FAILURE
STATE CONFLICT
DUPLICATE EVENT
```

Each class SHALL have an appropriate recovery path.

---

# 48. Recovery Model

```text
FAILURE
  ↓
CLASSIFY
  ↓
RETRY / COMPENSATE / ESCALATE
  ↓
RECOVER
  ↓
VERIFY
  ↓
CONTINUE
```

If recovery cannot establish a trustworthy state:

```text
SUSPEND / BLOCK / REOPEN
```

---

# 49. Concurrency Control

Concurrent workflow actions SHALL use controlled locking or version checks.

Example:

```text
Task Version = 12

User A submits version 12
User B submits version 12

First accepted
Second rejected as stale
```

This prevents lost updates.

---

# 50. Idempotent Commands

Commands such as:

```text
StartValidation
CompleteRemediation
RequestRevalidation
GrantAcceptance
ReopenCase
```

SHALL be idempotent where repeated delivery is possible.

A repeated command SHALL either:

```text
return existing result
```

or:

```text
be rejected as duplicate
```

without producing unintended duplicate business effects.

---

# 51. Workflow Versioning

Every workflow SHALL have a version.

Changes to:

```text
Tasks
Order
Guards
Timeouts
Escalations
Decision Rules
```

SHALL be version controlled.

Running workflows SHALL retain the applicable version where required.

---

# 52. Migration

When workflow definitions change:

```text
RUNNING WORKFLOW
        ↓
MIGRATION REQUIRED?
   ┌────┴────┐
  NO        YES
   │          │
   ▼          ▼
CONTINUE   CONTROLLED MIGRATION
```

Migration SHALL preserve audit history and business meaning.

---

# 53. MFM Service Boundary

The conceptual implementation should provide:

```text
Workflow Service
Event Service
Task Service
Scheduler
Queue Service
Escalation Service
Notification Service
State Service
Audit Service
```

These services SHALL use the state machine from RG-410 rather than implementing independent state logic.

---

# 54. Suggested Domain Commands

```text
createCase()
startReview()
requestValidation()
completeValidation()
requestVerification()
completeVerification()
requestAcceptance()
grantAcceptance()
requestClosure()
closeCase()
startMonitoring()
recordMonitoringEvent()
assessRegression()
confirmRegression()
startRemediation()
completeRemediation()
requestRevalidation()
completeRevalidation()
requestReverification()
completeReverification()
requestReacceptance()
grantReacceptance()
suspendCase()
revokeAcceptance()
reopenCase()
```

These are architectural operations and SHALL be implemented according to the approved application architecture.

---

# 55. Event Catalogue

Initial event catalogue:

```text
CaseCreated
ReviewStarted
ValidationRequested
ValidationCompleted
VerificationRequested
VerificationCompleted
AcceptanceRequested
AcceptanceGranted
AcceptanceRejected
ClosureRequested
CaseClosed
MonitoringStarted
MonitoringAlertRaised
ChangeDetected
RegressionAssessmentStarted
RegressionConfirmed
RegressionRejected
RemediationStarted
RemediationCompleted
RevalidationRequested
RevalidationCompleted
ReverificationRequested
ReverificationCompleted
ReacceptanceRequested
ReacceptanceGranted
SuspensionEntered
RevocationEntered
CaseReopened
WorkflowFailed
WorkflowEscalated
```

---

# 56. Workflow-to-State Relationship

The workflow SHALL request or prepare transitions.

The state machine SHALL authorise the transition.

```text
WORKFLOW
   ↓
REQUEST TRANSITION
   ↓
STATE MACHINE
   ↓
GUARDS
   ↓
AUTHORISE
   ↓
STATE CHANGE
   ↓
EVENT
```

This separation prevents workflow code from becoming an uncontrolled alternative state engine.

---

# 57. Workflow Completion

A workflow is complete only when:

```text
Required Tasks Complete
+
Required Decisions Complete
+
Required Evidence Present
+
No Blocking Exception
+
Required State Transition Complete
+
Completion Event Recorded
```

---

# 58. Workflow Cancellation

Cancellation SHALL be explicit.

It SHALL record:

```text
Reason
Authority
Current State
Completed Tasks
Outstanding Tasks
Consequences
Audit Event
```

Cancellation SHALL not erase completed work.

---

# 59. Workflow Metrics

The MFM implementation SHOULD report:

```text
Workflow Volume
Completion Rate
Average Duration
Median Duration
Blocked Time
Failure Rate
Retry Rate
Escalation Rate
SLA Breach Rate
Manual Intervention Rate
AI/Agent Intervention Rate
```

Metrics SHALL be calculated from actual workflow events.

---

# 60. Acceptance Criteria

EA-IMETA-PC-RG-411 is accepted when:

- commands and events are distinct;
- workflows have defined triggers and outcomes;
- tasks have owners and dependencies;
- state transitions remain controlled by RG-410;
- retries are safe;
- idempotency is defined;
- concurrency is controlled;
- failures have recovery paths;
- escalation is explicit;
- timeouts are controlled;
- event correlation is available;
- audit reconstruction is possible;
- AI/agent action boundaries are explicit;
- workflow versions are controlled.

---

# 61. Next Step

The next logical artifact is the **PC-RG evidence and audit architecture**, because RG-409 defines traceability and RG-410/411 define state and orchestration, but the architecture now needs a concrete model for how evidence is collected, bound to decisions, retained, protected and independently audited.

Provisional next artifact:

> **EA-IMETA-PC-RG-412 — EVIDENCE, AUDIT & TRACEABILITY DATA MODEL**

This remains a concrete data/control architecture artifact.

---

# 62. Governing Principle

> **Workflows orchestrate work; events record facts; the state machine controls state; authority controls decisions; audit records what happened.**

No single mechanism SHALL silently assume all five responsibilities.

# END OF EA-IMETA-PC-RG-411
