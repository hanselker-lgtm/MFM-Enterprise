# EA-IMETA-PC-RG-409

## ACTIVE CONTROL & TEST TRACEABILITY MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-409 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Control, Test & Traceability Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-408 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how active requirements become controls, executable behaviour, tests and auditable evidence |
| Architectural Boundary | Requirement → Control → Implementation → Test → Evidence → Decision |

---

# 2. Purpose

EA-IMETA-PC-RG-409 establishes the control and test traceability model for the consolidated PC-RG architecture.

It closes the gap between:

```text
REQUIREMENT
```

and:

```text
WORKING, TESTABLE, AUDITABLE SYSTEM BEHAVIOUR
```

The governing chain is:

```text
REQUIREMENT
    ↓
CONTROL OBJECTIVE
    ↓
CONTROL
    ↓
IMPLEMENTATION
    ↓
TEST
    ↓
EVIDENCE
    ↓
RESULT
    ↓
DECISION
```

A requirement is not considered implemented merely because it appears in an architecture document.

---

# 3. Architectural Scope

The model applies to the nine active PC-RG responsibilities:

```text
VAL  Validation
VER  Verification
ACC  Acceptance
CLO  Closure
MON  Monitoring
REG  Regression
REM  Remediation
RVA  Revalidation
RAC  Reacceptance
```

It also applies to cross-cutting controls for:

```text
Authority
Evidence
Audit
Security
Compliance
Risk
Accountability
Traceability
Independence
```

---

# 4. Core Control Model

Every material requirement SHALL map through the following chain:

```text
REQ
 │
 ▼
CONTROL OBJECTIVE
 │
 ▼
CONTROL
 │
 ▼
IMPLEMENTATION
 │
 ▼
TEST
 │
 ▼
EVIDENCE
 │
 ▼
RESULT
 │
 ▼
DECISION
```

Missing links SHALL be visible.

Example:

```text
REQ-001
   ↓
CO-001
   ↓
CTRL-001
   ↓
SERVICE-001
   ↓
TEST-001
   ↓
EVID-001
   ↓
PASS
   ↓
CONTROL EFFECTIVE
```

---

# 5. Control Objective

A control objective states what the control must achieve.

Format:

> The system/process SHALL ensure [required outcome] under [defined condition].

Examples:

```text
The system SHALL ensure that only authorised users may approve acceptance.

The system SHALL ensure that a closed case cannot be modified without an auditable reopening action.

The system SHALL ensure that material regression findings create a controlled remediation workflow.
```

A control objective SHALL be testable.

---

# 6. Control Definition

A control defines how the objective is achieved.

Every control SHALL specify:

| Attribute | Required |
|---|---|
| Control ID | Yes |
| Objective | Yes |
| Owner | Yes |
| Trigger | Yes |
| Input | Yes |
| Rule | Yes |
| Action | Yes |
| Output | Yes |
| Evidence | Yes |
| Frequency | Where applicable |
| Authority | Yes |
| Exception | Yes |
| Test Method | Yes |
| Failure Consequence | Yes |

---

# 7. Preventive, Detective and Corrective Controls

Controls SHALL be classified.

```text
PREVENTIVE
```

Stops an invalid action.

```text
DETECTIVE
```

Identifies an invalid state or event.

```text
CORRECTIVE
```

Restores the required state.

Examples:

```text
Preventive:
Unauthorised acceptance action blocked.

Detective:
Monitoring detects a threshold breach.

Corrective:
Regression finding creates remediation workflow.
```

---

# 8. Control Types

Controls may be:

```text
AUTOMATED
MANUAL
SEMI-AUTOMATED
PROCESS
TECHNICAL
ADMINISTRATIVE
DATA
WORKFLOW
AUTHORITY
AUDIT
```

The type SHALL be explicit.

---

# 9. Control Execution Model

```text
TRIGGER
  ↓
PRECONDITION CHECK
  ↓
CONTROL EXECUTION
  ↓
RESULT
  ↓
EVIDENCE
  ↓
STATE / DECISION
```

Failure:

```text
CONTROL FAILURE
  ↓
EXCEPTION
  ↓
ESCALATION
  ↓
CORRECTIVE ACTION
```

---

# 10. Requirement-to-Control Traceability

Every mandatory requirement SHALL have:

```text
≥ 1 CONTROL
```

unless an approved architectural decision records why no control is necessary.

Conversely:

```text
CONTROL WITHOUT REQUIREMENT
```

shall be classified as an architectural or risk-based control and documented accordingly.

---

# 11. Control-to-Test Traceability

Every material control SHALL have:

```text
≥ 1 TEST
```

The test SHALL demonstrate whether the control works, not merely whether the control documentation exists.

Bad test:

```text
"Control description reviewed."
```

Good test:

```text
Attempt unauthorised acceptance.
Expected: action rejected.
Actual: action rejected.
Evidence: audit event + system result.
```

---

# 12. Test Model

Every test SHALL define:

| Field | Required |
|---|---|
| Test ID | Yes |
| Requirement | Yes |
| Control | Yes |
| Preconditions | Yes |
| Test Data | Yes |
| Action | Yes |
| Expected Result | Yes |
| Actual Result | Yes |
| Evidence | Yes |
| Tester | Yes |
| Test Date | Yes |
| Result | Yes |
| Defect | Where applicable |
| Retest | Where applicable |

---

# 13. Test Classes

Tests SHALL be classified.

```text
UNIT
INTEGRATION
WORKFLOW
AUTHORITY
SECURITY
DATA
REGRESSION
USER ACCEPTANCE
CONTROL EFFECTIVENESS
AUDIT
RESILIENCE
PERFORMANCE
```

The correct test class depends on the requirement and control.

---

# 14. Test Result States

```text
NOT RUN
IN PROGRESS
PASS
PASS WITH CONDITIONS
FAIL
BLOCKED
NOT APPLICABLE
INCONCLUSIVE
RETEST REQUIRED
```

"Not run" SHALL never be interpreted as "pass".

---

# 15. Evidence Model

A successful test SHALL produce evidence appropriate to the test type.

Examples:

```text
DATABASE TEST
→ query result / transaction evidence

AUTHORITY TEST
→ actor / permission / decision evidence

WORKFLOW TEST
→ state transition evidence

SECURITY TEST
→ access decision / audit evidence

REGRESSION TEST
→ baseline/current comparison

USER TEST
→ recorded acceptance result
```

---

# 16. Evidence Integrity

Evidence SHALL be:

```text
IDENTIFIABLE
TIMESTAMPED
TRACEABLE
RELEVANT
SUFFICIENT
PROTECTED
RETAINED
```

Where integrity is material, evidence SHALL also support detection of unauthorised modification.

---

# 17. Control Effectiveness

Control effectiveness SHALL be determined from test results.

```text
CONTROL
   ↓
TEST
   ↓
EVIDENCE
   ↓
RESULT
```

Possible outcomes:

```text
EFFECTIVE
EFFECTIVE WITH CONDITIONS
INEFFECTIVE
NOT TESTED
INCONCLUSIVE
```

A documented control is not automatically an effective control.

---

# 18. Defect Model

A failed control or test SHALL create a defect where required.

```text
TEST FAILURE
   ↓
DEFECT
   ↓
SEVERITY
   ↓
OWNER
   ↓
REMEDIATION
   ↓
RETEST
```

Critical failures SHALL block dependent acceptance where the governing risk model requires it.

---

# 19. Traceability Coverage

The architecture SHALL calculate at least:

```text
Requirements with controls
Requirements without controls
Controls with tests
Controls without tests
Tests with evidence
Tests without evidence
Failed controls
Overdue retests
Unresolved critical defects
```

Recommended target:

```text
Mandatory Requirement → Control = 100%
Material Control → Test = 100%
Executed Test → Evidence = 100%
Critical Defect → Owner = 100%
```

---

# 20. Lifecycle Responsibility Mapping

## Validation

```text
VAL Requirement
    ↓
Validation Control
    ↓
Validation Test
    ↓
Validation Evidence
    ↓
Validation Result
```

## Verification

```text
VER Requirement
    ↓
Verification Control
    ↓
Verification Test
    ↓
Verification Evidence
    ↓
Verification Result
```

## Acceptance

```text
ACC Requirement
    ↓
Acceptance Control
    ↓
Authority Test
    ↓
Acceptance Evidence
    ↓
Acceptance Decision
```

## Closure

```text
CLO Requirement
    ↓
Closure Control
    ↓
Closure Gate Test
    ↓
Closure Evidence
    ↓
Closed State
```

## Monitoring

```text
MON Requirement
    ↓
Monitoring Control
    ↓
Monitoring Test
    ↓
Monitoring Evidence
    ↓
Monitoring Record
```

## Regression

```text
REG Requirement
    ↓
Regression Control
    ↓
Comparison Test
    ↓
Baseline + Current Evidence
    ↓
Regression Finding
```

## Remediation

```text
REM Requirement
    ↓
Remediation Control
    ↓
Action Completion Test
    ↓
Remediation Evidence
    ↓
Remediation State
```

## Revalidation

```text
RVA Requirement
    ↓
Revalidation Control
    ↓
Revalidation Test
    ↓
Current Evidence
    ↓
Revalidation Result
```

## Reacceptance

```text
RAC Requirement
    ↓
Reacceptance Control
    ↓
Authority / Reliance Test
    ↓
Reacceptance Evidence
    ↓
Reacceptance Decision
```

---

# 21. State Transition Testing

Each material state transition SHALL be testable.

Example:

```text
CLOSED
   ↓
REOPEN REQUEST
   ↓
AUTHORITY CHECK
   ↓
REOPEN APPROVED
   ↓
REOPENED
```

Negative test:

```text
CLOSED
   ↓
UNAUTHORISED REOPEN
   ↓
REJECTED
   ↓
AUDIT EVENT
```

---

# 22. Negative Testing

The control model SHALL include negative tests.

Examples:

```text
Unauthorised user
Missing evidence
Expired evidence
Invalid criteria
Conflicting decision
Missing approval
Expired acceptance
Broken dependency
Changed configuration
Corrupted data
Duplicate action
Replay action
Unexpected state
```

A system that only passes positive tests has insufficient control assurance.

---

# 23. Regression Testing

Regression tests SHALL be linked to baseline versions.

```text
BASELINE VERSION
       ↓
CURRENT VERSION
       ↓
TEST SET
       ↓
COMPARISON
       ↓
RESULT
```

Material changes SHALL trigger the applicable regression suite.

---

# 24. Change Impact

Changes SHALL be assessed for affected:

```text
Requirements
Controls
Data
Workflows
Permissions
Tests
Reports
Integrations
Audit
```

The impact assessment SHALL identify whether revalidation or reacceptance is required.

---

# 25. Test Independence

Where independence is required:

```text
CONTROL OWNER ≠ TESTER
```

or the governing architecture SHALL define an approved exception.

The test record SHALL identify the tester and independence status.

---

# 26. AI and Agent Controls

AI-supported controls SHALL be tested for:

```text
Prompt / Instruction
Model Version
Data Input
Tool Access
Permission Scope
Output
Human Review
Decision Boundary
Audit Evidence
Failure Handling
```

AI may execute a control only where explicitly authorised.

---

# 27. AI Negative Testing

AI controls SHALL include tests for:

```text
Incorrect output
Hallucinated evidence
Missing evidence
Prompt manipulation
Unauthorised tool use
Scope escalation
Data leakage
Conflicting instructions
Model/version change
Human override
```

---

# 28. Security Testing

Security controls SHALL test:

```text
Authentication
Authorisation
Least Privilege
Separation of Duties
Data Protection
Audit Integrity
Session Security
Access Revocation
```

Security failures affecting acceptance or reliance SHALL trigger the defined escalation path.

---

# 29. Compliance Testing

Compliance controls SHALL test actual behaviour against applicable obligations.

A policy document alone SHALL not be treated as evidence of compliance.

---

# 30. Audit Traceability

A complete chain SHALL be recoverable:

```text
Requirement
   ↓
Control
   ↓
Implementation
   ↓
Test
   ↓
Evidence
   ↓
Result
   ↓
Decision
   ↓
Audit Event
```

Missing links SHALL be reported as traceability gaps.

---

# 31. Control Catalogue

The active control catalogue SHALL include:

```text
Control ID
Control Name
Objective
Type
Owner
Responsibility
Requirement Links
Risk Links
Implementation
Frequency
Evidence
Test Links
Failure Consequence
Status
Version
```

---

# 32. Test Catalogue

The active test catalogue SHALL include:

```text
Test ID
Test Name
Requirement Links
Control Links
Test Class
Preconditions
Data
Procedure
Expected Result
Actual Result
Evidence
Tester
Independence
Result
Defect
Retest
Version
```

---

# 33. Control Health

The MFM implementation SHOULD calculate control health using:

```text
PASS RATE
+
RECENCY
+
FAILURE SEVERITY
+
OPEN DEFECTS
+
TEST COVERAGE
+
EVIDENCE QUALITY
```

The calculation SHALL be defined transparently rather than hidden in an unexplained score.

---

# 34. Control Failure Consequences

Control failures SHALL map to consequences.

```text
MINOR
→ corrective action

SIGNIFICANT
→ remediation + retest

MATERIAL
→ revalidation / restriction

CRITICAL
→ suspend acceptance / revoke reliance / reopen
```

The actual threshold SHALL be determined by the applicable risk model.

---

# 35. Exception Model

Every control SHALL define:

```text
Normal Path
Exception
Detection
Escalation
Authority
Resolution
Evidence
Closure
```

Exceptions SHALL not silently bypass controls.

---

# 36. Traceability Matrix

The master active matrix SHALL use:

| Requirement | Objective | Control | Implementation | Test | Evidence | Result | Decision | Audit |
|---|---|---|---|---|---|---|---|---|
| REQ-… | CO-… | CTRL-… | IMP-… | TEST-… | EVID-… | PASS/FAIL | DEC-… | AUD-… |

Every mandatory requirement SHALL be traceable across the complete chain.

---

# 37. Coverage Rules

Coverage SHALL be measured separately for:

```text
Requirement Coverage
Control Coverage
Implementation Coverage
Test Coverage
Evidence Coverage
Decision Coverage
Audit Coverage
```

A single "coverage %" SHALL not hide missing categories.

---

# 38. Definition of Done

A control is complete when:

```text
Requirement linked
+
Objective defined
+
Control implemented
+
Owner assigned
+
Test defined
+
Test executed
+
Evidence retained
+
Result recorded
+
Failure path defined
```

A control is not complete merely because it is documented.

---

# 39. Architecture Governance

Changes to this model SHALL require:

```text
Impact Assessment
Requirement Impact
Control Impact
Test Impact
Data Impact
Security Impact
Audit Impact
Approval
```

Material changes SHALL trigger applicable regression analysis.

---

# 40. MFM Implementation Roadmap

The model should be implemented in phases.

### Phase 1 — Data Foundation

```text
Requirement
Control
Test
Evidence
Decision
Audit
```

### Phase 2 — Lifecycle

```text
Validation
Verification
Acceptance
Closure
```

### Phase 3 — Post-Closure

```text
Monitoring
Regression
Remediation
```

### Phase 4 — Recovery

```text
Revalidation
Reverification
Reacceptance
Reopening
```

### Phase 5 — Analytics

```text
Coverage
Control Health
Defect Trends
Regression Trends
Audit Reporting
```

---

# 41. Acceptance Criteria

EA-IMETA-PC-RG-409 is accepted as the active control/test model when:

- every mandatory requirement can map to a control;
- every material control can map to a test;
- executed tests produce evidence;
- results produce explicit states or decisions;
- failures create defined consequences;
- state transitions are testable;
- negative testing exists;
- regression testing is baseline-aware;
- authority and independence are testable;
- AI-assisted controls have explicit boundaries;
- audit traceability is complete.

---

# 42. Next Step

The next architecture artifact SHOULD define the **PC-RG lifecycle state machine and transition rules**, because the control/test model now requires a formal state-transition authority.

Provisional next artifact:

> **EA-IMETA-PC-RG-410 — LIFECYCLE STATE MACHINE & TRANSITION CONTROL**

This remains a functional architecture artifact, not another terminology layer.

---

# 43. Governing Principle

> **A control only has architectural value when it changes or protects real system behaviour and can be objectively tested.**

The PC-RG architecture SHALL therefore measure assurance through:

```text
REQUIREMENTS
→ CONTROLS
→ IMPLEMENTATION
→ TESTS
→ EVIDENCE
→ RESULTS
→ DECISIONS
```

not through document volume.

# END OF EA-IMETA-PC-RG-409
