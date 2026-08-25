# EA-IMETA-PC-RG-405

## REGRESSION GOVERNANCE — ARCHITECTURAL CONSOLIDATION & CONTROL MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-405 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Architectural Consolidation |
| Status | Active Baseline |
| Version | 1.0 |
| Supersedes as working pattern | EA-IMETA-PC-RG-001–404 repetitive generation model |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Establish a coherent, non-duplicative architecture for the PC-RG domain |
| Next logical artifact | To be determined from the consolidated dependency model |

---

## 2. Why This Document Exists

EA-IMETA-PC-RG-405 is deliberately different from the preceding RG documents.

The preceding sequence progressively accumulated terms such as validation, verification, acceptance, closure, monitoring, regression, governance, authority, mandate, role, responsibility, accountability, outcome, criteria and conditions without consistently assigning each term a distinct architectural responsibility.

This document stops that pattern.

It does **not** add another governance noun to a title.

It establishes the architecture required to determine:

1. which capabilities actually exist in the RG domain;
2. which responsibilities are distinct;
3. which prior documents are duplicates or variants of the same responsibility;
4. which decisions must exist;
5. which states must exist;
6. which data must be retained;
7. which actors may perform or approve each action;
8. which transitions are permitted;
9. how exceptions are handled;
10. how the model can be implemented and tested.

The governing rule is:

> **One EA document SHALL represent one materially distinct architectural responsibility.**

A new document SHALL NOT be created merely because another governance term can be appended to a title.

---

# 3. Architectural Problem Statement

The existing PC-RG sequence contains a repeated pattern:

```text
DOCUMENT N
   ↓
declares DOCUMENT N-1 as Parent
   ↓
adds one conceptual term
   ↓
repeats Purpose
   ↓
repeats Core Principle
   ↓
repeats control families
   ↓
repeats validation / verification language
   ↓
creates DOCUMENT N+1
```

This creates three architectural risks.

### 3.1 Semantic Duplication

Different documents may express substantially the same responsibility using different terminology.

### 3.2 Traceability Inflation

The number of references increases without a corresponding increase in architectural information.

### 3.3 False Granularity

A long document chain can create the appearance of control depth even where there is only one underlying decision or control.

The architecture SHALL therefore distinguish:

```text
MORE DOCUMENTS
      ≠
MORE CONTROLS
      ≠
MORE ASSURANCE
```

---

# 4. New Architectural Rule

## 4.1 Responsibility Rule

Every PC-RG document SHALL have one primary responsibility.

The responsibility SHALL be expressible as:

> **The system/process shall [verb] [object] under [criteria/authority] and produce [output].**

Examples:

```text
Validate a state against defined criteria.
Verify that validation was performed correctly.
Accept a validated state.
Close a completed lifecycle case.
Monitor a closed state.
Detect regression.
Manage remediation.
Revalidate after material change.
Reaccept after successful revalidation.
```

These are distinct because they produce different decisions or state transitions.

The following are NOT sufficient reasons for separate documents:

```text
"governance"
"assurance"
"authority"
"accountability"
"responsibility"
"outcome"
"conditions"
"mandatory"
"control"
```

unless the term introduces a materially different decision, state, data object, actor responsibility or system behavior.

---

# 5. Canonical PC-RG Lifecycle

The PC-RG architecture SHALL be represented as a lifecycle rather than as an endless title chain.

```text
                 ┌──────────────────────┐
                 │  GOVERNED SUBJECT    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     VALIDATION       │
                 │ Is the state valid? │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    VERIFICATION      │
                 │ Was validation done  │
                 │ correctly?           │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     ACCEPTANCE       │
                 │ Is reliance formally │
                 │ authorised?          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      CLOSURE         │
                 │ Is the lifecycle     │
                 │ formally complete?   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     MONITORING       │
                 │ Has the closed state │
                 │ remained valid?      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     REGRESSION       │
                 │ Has material change  │
                 │ occurred?            │
                 └──────────┬───────────┘
                            │
                    ┌───────┴────────┐
                    │                │
                   NO               YES
                    │                │
                    ▼                ▼
               CONTINUE        REMEDIATION
                                     │
                                     ▼
                               REVALIDATION
                                     │
                                     ▼
                               REACCEPTANCE
                                     │
                                     ▼
                                  CLOSURE
```

This lifecycle is the primary architectural model.

---

# 6. Canonical Responsibilities

The following responsibilities are currently recognised as materially distinct.

| Responsibility | Core Question | Primary Output |
|---|---|---|
| Validation | Is the subject valid against criteria? | Validation Result |
| Verification | Was the validation correctly performed? | Verification Result |
| Acceptance | May the organisation rely on the result? | Acceptance Decision |
| Closure | Has the lifecycle been formally completed? | Closure State |
| Monitoring | Does the accepted/closed state remain valid? | Monitoring Record |
| Regression Detection | Has a material change occurred? | Regression Finding |
| Remediation | What must be corrected? | Remediation Action |
| Revalidation | Is the corrected/current state valid again? | Revalidation Result |
| Reacceptance | May reliance be restored? | Reacceptance Decision |

These responsibilities form the minimum conceptual model.

---

# 7. Responsibilities That Shall Not Automatically Become Separate Documents

The following are cross-cutting properties rather than standalone lifecycle stages:

- Governance
- Authority
- Mandate
- Role
- Responsibility
- Accountability
- Outcome
- Criteria
- Success
- Conditions
- Compliance
- Assurance
- Independence
- Evidence
- Auditability
- Traceability

They SHALL be represented within the responsibility they govern unless a separate architectural decision demonstrates that they require an independent lifecycle, data object, decision or system capability.

Example:

```text
VALIDATION
 ├── Authority
 ├── Criteria
 ├── Evidence
 ├── Independence
 ├── Accountability
 ├── Decision
 └── Audit Trail
```

rather than:

```text
VALIDATION
 → VALIDATION-GOVERNANCE
 → VALIDATION-AUTHORITY
 → VALIDATION-MANDATE
 → VALIDATION-ROLE
 → VALIDATION-ACCOUNTABILITY
 → ...
```

---

# 8. Standard EA Document Contract

Every future PC-RG document SHALL contain the following architectural contract.

## 8.1 Responsibility

One sentence defining the primary responsibility.

## 8.2 Trigger

The event or condition that starts the responsibility.

## 8.3 Inputs

The data, state and evidence required.

## 8.4 Rules

The criteria and constraints applied.

## 8.5 Authority

Who or what is permitted to make the decision.

## 8.6 Processing

The substantive activity performed.

## 8.7 Decision

The decision that results from the activity.

## 8.8 Output

The resulting state, record or action.

## 8.9 State Transition

The permitted before/after state.

## 8.10 Exceptions

What happens when normal processing fails.

## 8.11 Ownership

Who owns the resulting state.

## 8.12 Dependencies

Which other architectural capabilities are required.

## 8.13 Implementation

How the responsibility maps into MFM processes, services, data and UI.

## 8.14 Testability

How the responsibility can be objectively tested.

---

# 9. Standard State Model

The PC-RG architecture SHALL use explicit states rather than relying on prose.

```text
DRAFT
  │
  ▼
IN REVIEW
  │
  ▼
VALIDATED
  │
  ▼
VERIFIED
  │
  ▼
ACCEPTED
  │
  ▼
CLOSED
  │
  ▼
MONITORED
  │
  ├───────────────┐
  │               │
  ▼               ▼
STABLE        REGRESSION
                  │
                  ▼
             REMEDIATION
                  │
                  ▼
             REVALIDATION
                  │
                  ▼
             REVERIFICATION
                  │
                  ▼
             REACCEPTANCE
                  │
                  ▼
               CLOSED
```

Invalid states SHALL remain explicit:

```text
REJECTED
FAILED
SUSPENDED
REVOKED
REOPENED
INCONCLUSIVE
```

---

# 10. Decision Model

Each material decision SHALL have:

```text
Decision ID
Subject
Trigger
Input State
Criteria
Evidence
Decision Authority
Decision Maker
Decision Date
Decision
Conditions
Rationale
Output State
Expiry / Review Date
Audit Trail
```

A status field alone SHALL NOT constitute a decision record.

---

# 11. Evidence Model

Evidence SHALL be attached to a specific responsibility and decision.

```text
Evidence
   │
   ├── Source
   ├── Timestamp
   ├── Owner
   ├── Integrity
   ├── Relevance
   ├── Scope
   └── Decision Link
```

The architecture SHALL avoid chains where one document merely declares another document's existence as evidence.

---

# 12. Actor and Authority Model

Authority SHALL be modelled independently from document naming.

```text
ACTOR
  │
  ├── Role
  ├── Permission
  ├── Scope
  ├── Separation-of-Duties Constraints
  └── Delegation
```

The architecture SHALL distinguish:

```text
PERFORM
REVIEW
VERIFY
APPROVE
ACCEPT
REVOKE
REOPEN
```

No role shall implicitly acquire authority merely because it authored or owns a document.

---

# 13. Control Model

Controls SHALL be mapped to actual risks and lifecycle transitions.

```text
Risk
  ↓
Control Objective
  ↓
Control
  ↓
Execution
  ↓
Evidence
  ↓
Test
  ↓
Result
  ↓
Decision
```

A repeated list of control-family headings without a distinct control mechanism SHALL not be treated as additional control coverage.

---

# 14. Regression Model

Regression is not simply another governance state.

A regression exists when:

> A previously accepted or closed state no longer satisfies one or more mandatory criteria because of a material change, failure, degradation, loss of evidence, loss of authority, changed dependency, changed risk or other defined invalidating condition.

Regression detection SHALL therefore compare:

```text
BASELINE STATE
      +
CURRENT STATE
      +
CRITERIA
      ↓
DIFFERENCE ANALYSIS
      ↓
MATERIAL?
```

Result:

```text
NO MATERIAL REGRESSION
        OR
REGRESSION FINDING
```

---

# 15. Remediation Model

A regression finding SHALL create a remediation object where correction is required.

```text
Regression Finding
       ↓
Severity
       ↓
Owner
       ↓
Action
       ↓
Target Date
       ↓
Evidence
       ↓
Verification
       ↓
Revalidation
```

Remediation SHALL not be considered complete merely because an action is marked "done".

---

# 16. Revalidation Model

Revalidation SHALL determine whether the current state satisfies the required criteria after a material change or remediation.

```text
REGRESSION / REMEDIATION
        ↓
CURRENT STATE
        ↓
CRITERIA
        ↓
EVIDENCE
        ↓
REVALIDATION
        ↓
VALID / INVALID / CONDITIONAL
```

Revalidation SHALL not automatically imply acceptance.

---

# 17. Acceptance and Reacceptance

Acceptance answers a different question from validation:

```text
VALIDATION:
"Is it valid?"

ACCEPTANCE:
"Are we authorised to rely on it?"
```

Reacceptance is required where a prior acceptance has been invalidated, suspended, revoked or materially affected by a regression.

---

# 18. Closure Model

Closure SHALL be an explicit state transition.

```text
OPEN
  ↓
ALL REQUIRED ACTIVITIES COMPLETE?
  ↓
CLOSURE CHECK
  ↓
CLOSED
```

Closure SHALL preserve:

- unresolved issues;
- conditions;
- outstanding obligations;
- monitoring requirements;
- review dates;
- ownership;
- evidence;
- reopening criteria.

---

# 19. Monitoring Model

Monitoring SHALL have an explicit purpose.

It SHALL answer:

> Does the accepted/closed state remain within its approved boundaries?

Monitoring SHALL define:

- monitored object;
- baseline;
- indicators;
- thresholds;
- frequency;
- evidence source;
- responsible actor;
- escalation;
- regression trigger.

---

# 20. MFM Implementation Boundary

The PC-RG architecture SHALL eventually map to concrete MFM components.

At minimum:

```text
DOMAIN
 ├── Case / Subject
 ├── Lifecycle State
 ├── Validation
 ├── Verification
 ├── Acceptance
 ├── Closure
 ├── Monitoring
 ├── Regression Finding
 ├── Remediation
 ├── Revalidation
 └── Reacceptance
```

Supporting services:

```text
Authority Service
Evidence Service
Decision Service
Audit Service
Notification Service
Workflow Service
Reporting Service
```

The exact implementation SHALL be defined by the corresponding implementation architecture rather than invented inside this consolidation document.

---

# 21. Data Objects

The canonical conceptual data objects are:

```text
Subject
Case
Baseline
Criteria
Evidence
Validation
Verification
Acceptance
Closure
Monitoring Record
Regression Finding
Remediation
Revalidation
Reacceptance
Decision
Condition
Audit Event
```

Each object SHALL have an explicit lifecycle.

---

# 22. Traceability

Traceability SHALL follow the business lifecycle.

```text
Subject
  ↓
Baseline
  ↓
Criteria
  ↓
Evidence
  ↓
Validation
  ↓
Verification
  ↓
Acceptance
  ↓
Closure
  ↓
Monitoring
  ↓
Regression
  ↓
Remediation
  ↓
Revalidation
  ↓
Reverification
  ↓
Reacceptance
```

This is materially stronger than:

```text
RG-401
  ↓
RG-402
  ↓
RG-403
  ↓
RG-404
  ↓
RG-405
```

where the references themselves provide little information about the underlying business process.

---

# 23. Testability Model

Every responsibility SHALL be testable.

Example:

### Validation Test

Given:

```text
Subject = X
Criteria = C
Evidence = E
```

Expected:

```text
Validation Result = VALID
```

### Verification Test

Given a completed validation:

```text
Validation = V
Evidence = E
Method = M
Authority = A
```

Expected:

```text
Verification Result = VERIFIED
```

### Regression Test

Given:

```text
Baseline = B
Current State = C
Criteria = K
```

Expected:

```text
Regression Finding = TRUE
```

This approach makes the architecture implementable and auditable.

---

# 24. Duplicate Detection Rule

Before creating any future PC-RG document, the author SHALL answer:

1. Does the proposed responsibility already exist?
2. Does it produce a different decision?
3. Does it create a different state?
4. Does it require different authority?
5. Does it operate on a different data object?
6. Does it have different implementation behavior?
7. Can it be independently tested?

If the answer to all seven is NO:

> **A new document SHALL NOT be created.**

---

# 25. Naming Rule

Future filenames SHALL describe the architectural responsibility rather than accumulate concepts.

Preferred:

```text
EA-IMETA-PC-RG-VALIDATION
EA-IMETA-PC-RG-VERIFICATION
EA-IMETA-PC-RG-ACCEPTANCE
EA-IMETA-PC-RG-CLOSURE
EA-IMETA-PC-RG-MONITORING
EA-IMETA-PC-RG-REGRESSION
EA-IMETA-PC-RG-REMEDIATION
EA-IMETA-PC-RG-REVALIDATION
EA-IMETA-PC-RG-REACCEPTANCE
```

Numbered physical files may still be retained for registry and versioning, but the title SHALL communicate function.

---

# 26. Treatment of EA-IMETA-PC-RG-001–404

The existing files SHALL be treated as historical architectural material pending consolidation.

They SHALL NOT automatically be regarded as 404 independent controls.

The consolidation process SHALL classify each existing artifact as one of:

```text
RETAIN
MERGE
REFERENCE
SUPERSEDE
ARCHIVE
DELETE FROM ACTIVE BASELINE
```

No historical document shall be removed merely because it is redundant until its relevant requirements and traceability have been captured.

---

# 27. Immediate Architectural Consequence

EA-IMETA-PC-RG-405 becomes the boundary between:

```text
LEGACY / GENERATED RG CHAIN
            │
            ▼
┌───────────────────────────────┐
│ PC-RG ARCHITECTURAL MODEL     │
│                               │
│ Validation                    │
│ Verification                  │
│ Acceptance                   │
│ Closure                      │
│ Monitoring                   │
│ Regression                   │
│ Remediation                  │
│ Revalidation                │
│ Reacceptance                │
└───────────────────────────────┘
            │
            ▼
IMPLEMENTATION / MFM
```

---

# 28. Acceptance Criteria for This Architecture

EA-IMETA-PC-RG-405 is considered architecturally complete when:

- every PC-RG responsibility has a defined owner;
- each responsibility has a unique purpose;
- inputs and outputs are defined;
- state transitions are explicit;
- decisions are identifiable;
- authority is identifiable;
- evidence is traceable;
- exceptions are defined;
- dependencies are defined;
- MFM implementation boundaries are identified;
- testability is defined;
- duplicate responsibilities can be detected;
- new documents cannot be justified merely by adding terminology.

---

# 29. Governing Principle

> **Architectural depth SHALL come from distinct responsibilities, decisions, states, data, controls and testable behavior — not from the number of documents or the number of words in their titles.**

---

# 30. Next Step

The next artifact SHALL NOT automatically be EA-IMETA-PC-RG-406.

The next step is to build the **PC-RG responsibility inventory and consolidation matrix** from EA-IMETA-PC-RG-001–404 and map each artifact to the canonical lifecycle above.

Only after that inventory has been completed SHALL the next active PC-RG document be assigned.

# END OF EA-IMETA-PC-RG-405
