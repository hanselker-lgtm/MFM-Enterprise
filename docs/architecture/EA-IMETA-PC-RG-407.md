# EA-IMETA-PC-RG-407

## PC-RG ACTIVE BASELINE ARCHITECTURE

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-407 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Active Baseline Architecture |
| Status | Proposed Active Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-406 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define the target active PC-RG architecture after consolidation |
| Evidence Boundary | Legacy RG-001–404 remain subject to source-based consolidation |

---

# 2. Purpose

EA-IMETA-PC-RG-407 defines the target active architecture for the PC-RG domain.

It replaces the concept of an indefinitely expanding document chain with a finite set of materially distinct lifecycle responsibilities.

The architecture SHALL be driven by:

```text
RESPONSIBILITY
    ↓
STATE
    ↓
DECISION
    ↓
AUTHORITY
    ↓
EVIDENCE
    ↓
ACTION
    ↓
AUDIT
```

not by document count.

---

# 3. Active Responsibility Model

The target PC-RG architecture contains nine primary lifecycle responsibilities.

| ID | Responsibility | Question | Output |
|---|---|---|---|
| VAL | Validation | Is the current state valid? | Validation Result |
| VER | Verification | Was the validation performed correctly? | Verification Result |
| ACC | Acceptance | May reliance be authorised? | Acceptance Decision |
| CLO | Closure | Is the lifecycle complete? | Closure State |
| MON | Monitoring | Does the accepted state remain valid? | Monitoring Record |
| REG | Regression | Has material deterioration/change occurred? | Regression Finding |
| REM | Remediation | What corrective action is required? | Remediation State |
| RVA | Revalidation | Is the corrected state valid again? | Revalidation Result |
| RAC | Reacceptance | May reliance be restored? | Reacceptance Decision |

These nine responsibilities constitute the proposed active baseline.

---

# 4. Architectural Lifecycle

```text
                    ┌───────────────┐
                    │    SUBJECT    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  VALIDATION   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ VERIFICATION  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  ACCEPTANCE   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    CLOSURE    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  MONITORING   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  REGRESSION   │
                    └───────┬───────┘
                            │
                     ┌──────┴──────┐
                     │             │
                    NO            YES
                     │             │
                     ▼             ▼
                  CONTINUE    REMEDIATION
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
                                CLOSURE
```

---

# 5. Responsibility Boundaries

## 5.1 Validation

Validation determines whether a subject or state satisfies defined criteria.

It SHALL NOT grant reliance authority.

```text
INPUT:
Subject + Criteria + Evidence

OUTPUT:
VALID / INVALID / CONDITIONAL / INCONCLUSIVE
```

---

## 5.2 Verification

Verification determines whether the validation was performed correctly.

It SHALL NOT replace substantive validation.

```text
INPUT:
Validation + Method + Evidence + Authority

OUTPUT:
VERIFIED / NOT VERIFIED / CONDITIONAL / INCONCLUSIVE
```

---

## 5.3 Acceptance

Acceptance determines whether the organisation is authorised to rely on the verified result.

```text
INPUT:
Validation + Verification + Risk + Authority

OUTPUT:
ACCEPTED / REJECTED / CONDITIONAL / SUSPENDED
```

---

## 5.4 Closure

Closure formally completes the current lifecycle.

Closure SHALL confirm:

- required activities complete;
- decisions recorded;
- evidence retained;
- obligations identified;
- conditions recorded;
- monitoring requirements established;
- ownership assigned;
- reopening criteria defined.

```text
OPEN → CLOSURE REVIEW → CLOSED
```

---

## 5.5 Monitoring

Monitoring observes whether the accepted/closed state remains within approved boundaries.

Monitoring SHALL NOT automatically alter the state without a defined trigger.

```text
MONITOR
   ↓
THRESHOLD?
   ├── NO → CONTINUE
   └── YES → ASSESS REGRESSION
```

---

## 5.6 Regression

Regression determines whether a material deviation exists.

```text
BASELINE
+
CURRENT STATE
+
CRITERIA
      ↓
COMPARISON
      ↓
MATERIAL?
```

Result:

```text
NO REGRESSION
REGRESSION
INCONCLUSIVE
```

---

## 5.7 Remediation

Remediation manages correction of an identified regression.

A remediation SHALL contain:

- finding;
- severity;
- owner;
- action;
- target date;
- evidence;
- dependencies;
- verification requirement;
- closure criteria.

An action marked complete is not automatically a successful remediation.

---

## 5.8 Revalidation

Revalidation determines whether the current state is valid after remediation or material change.

```text
REMEDIATION
    ↓
CURRENT STATE
    ↓
CRITERIA
    ↓
EVIDENCE
    ↓
REVALIDATION
```

Result:

```text
VALID
INVALID
CONDITIONAL
INCONCLUSIVE
```

---

## 5.9 Reacceptance

Reacceptance restores authorised reliance after successful revalidation and any required reverification.

```text
REVALIDATED
    +
REVERIFIED
    +
AUTHORITY
    ↓
REACCEPTED
```

---

# 6. State Model

The active lifecycle SHALL use explicit states.

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

Regression branch:

```text
MONITORED
   ↓
REGRESSION SUSPECTED
   ↓
REGRESSION CONFIRMED
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
```

---

# 7. Invalid States

The architecture SHALL distinguish:

```text
INVALID
REJECTED
NOT VERIFIED
SUSPENDED
REVOKED
FAILED
INCONCLUSIVE
REOPENED
```

These states SHALL NOT be collapsed into a generic "not active" status.

---

# 8. Cross-Cutting Capabilities

The following are supporting capabilities rather than automatic lifecycle stages:

```text
AUTHORITY
ACCOUNTABILITY
EVIDENCE
AUDIT
TRACEABILITY
SECURITY
COMPLIANCE
RISK
INDEPENDENCE
NOTIFICATION
REPORTING
```

They support the nine lifecycle responsibilities.

Example:

```text
                 AUTHORITY
                    │
EVIDENCE ──────── VALIDATION ──────── AUDIT
                    │
                 CRITERIA
                    │
                   RISK
```

---

# 9. Canonical Decision Object

Every material lifecycle decision SHALL use a common decision structure.

| Attribute | Required |
|---|---|
| Decision ID | Yes |
| Subject | Yes |
| Lifecycle Case | Yes |
| Trigger | Yes |
| Input State | Yes |
| Criteria | Yes |
| Evidence | Yes |
| Decision Authority | Yes |
| Decision Maker | Yes |
| Decision Date | Yes |
| Decision | Yes |
| Conditions | Where applicable |
| Rationale | Yes |
| Output State | Yes |
| Review / Expiry | Where applicable |
| Audit Trail | Yes |

---

# 10. Canonical Evidence Object

Evidence SHALL be independently identifiable.

```text
Evidence ID
Source
Type
Owner
Created
Collected
Integrity
Scope
Validity Period
Criteria Link
Decision Link
Audit Link
```

Evidence SHALL not be represented solely by free-text statements such as "evidence reviewed".

---

# 11. Authority Model

Authority SHALL be explicit.

```text
PERFORM
REVIEW
VERIFY
APPROVE
ACCEPT
REVOKE
REOPEN
```

Each action SHALL be governed by:

```text
Actor
Role
Permission
Scope
Delegation
Separation-of-Duties
```

---

# 12. Control Model

Controls SHALL map to lifecycle responsibilities.

```text
RISK
 ↓
CONTROL OBJECTIVE
 ↓
CONTROL
 ↓
EXECUTION
 ↓
EVIDENCE
 ↓
TEST
 ↓
RESULT
 ↓
DECISION
```

Repeated prose shall not be counted as separate controls.

---

# 13. Regression Baseline

A monitored object SHALL have an identifiable baseline.

The baseline SHALL contain:

```text
Baseline ID
Accepted State
Criteria Version
Relevant Configuration
Approved Conditions
Dependencies
Risk Profile
Evidence Set
Acceptance Decision
Closure Decision
Effective Date
Review Date
```

A regression comparison without a defined baseline SHALL be considered incomplete unless the governing responsibility explicitly defines an alternative reference.

---

# 14. Regression Detection

Regression detection SHALL distinguish:

```text
CHANGE
from
MATERIAL CHANGE
```

A materiality assessment SHALL consider:

- criteria breach;
- risk increase;
- control degradation;
- dependency failure;
- security impact;
- compliance impact;
- data integrity;
- operational impact;
- loss of authority;
- loss of evidence;
- changed operating context.

---

# 15. Remediation Control

Remediation SHALL follow:

```text
Finding
  ↓
Classification
  ↓
Owner
  ↓
Action Plan
  ↓
Execution
  ↓
Evidence
  ↓
Verification
  ↓
Revalidation
```

No remediation SHALL close solely on self-attestation where independent verification is required.

---

# 16. Revalidation Gate

The revalidation gate SHALL require:

```text
REMEDIATION COMPLETE
+
CURRENT EVIDENCE
+
CURRENT CRITERIA
+
REQUIRED INDEPENDENCE
+
RISK ACCEPTABLE
```

before producing a positive revalidation result.

---

# 17. Reacceptance Gate

Reacceptance SHALL require:

```text
REVALIDATION = VALID
+
REVERIFICATION = VERIFIED
+
AUTHORITY = PRESENT
+
CONDITIONS = ACCEPTED
+
RISK = WITHIN TOLERANCE
```

Only then may reliance be restored.

---

# 18. Closure Gate

Closure SHALL require:

```text
REQUIRED DECISIONS COMPLETE
+
EVIDENCE RETAINED
+
OBLIGATIONS RECORDED
+
CONDITIONS RECORDED
+
MONITORING ESTABLISHED
+
OWNER ASSIGNED
+
REOPENING RULES DEFINED
```

---

# 19. MFM Implementation Model

The target MFM implementation should expose the PC-RG responsibilities as domain capabilities rather than document files.

Conceptually:

```text
PC-RG DOMAIN
│
├── Case Management
├── Validation Service
├── Verification Service
├── Acceptance Service
├── Closure Service
├── Monitoring Service
├── Regression Service
├── Remediation Service
├── Revalidation Service
└── Reacceptance Service
```

Supporting services:

```text
Evidence Service
Decision Service
Authority Service
Audit Service
Workflow Service
Notification Service
Reporting Service
```

---

# 20. Suggested Data Relationships

```text
CASE
 │
 ├── BASELINE
 ├── CRITERIA
 ├── EVIDENCE
 ├── VALIDATION
 │      └── VERIFICATION
 │              └── ACCEPTANCE
 │                      └── CLOSURE
 │                              └── MONITORING
 │                                      └── REGRESSION
 │                                              └── REMEDIATION
 │                                                      └── REVALIDATION
 │                                                              └── REVERIFICATION
 │                                                                      └── REACCEPTANCE
 │
 └── AUDIT EVENTS
```

---

# 21. API / Service Boundary

The eventual implementation SHALL provide domain operations corresponding to real responsibilities.

Illustrative operations:

```text
create_case()
validate_case()
verify_validation()
accept_case()
close_case()
start_monitoring()
record_monitoring_event()
assess_regression()
create_remediation()
verify_remediation()
revalidate_case()
reverify_case()
reaccept_case()
reopen_case()
revoke_acceptance()
```

These operations are architectural candidates, not a commitment to a specific programming language or API framework.

---

# 22. UI Boundary

The UI SHALL represent lifecycle work rather than document jargon.

Recommended navigation:

```text
PC-RG
├── Cases
├── Validation
├── Verification
├── Acceptance
├── Closure
├── Monitoring
├── Regression
├── Remediation
├── Revalidation
├── Reacceptance
└── Audit Trail
```

A user should be able to understand the current lifecycle state without reading a chain of EA document titles.

---

# 23. Reporting

Reports SHALL focus on operational questions.

Examples:

- What is currently validated?
- What is verified?
- What has been accepted?
- What is closed?
- What is being monitored?
- What regressions are open?
- Which remediation actions are overdue?
- Which cases require revalidation?
- Which acceptances are suspended or revoked?
- Which conditions are approaching expiry?

---

# 24. Audit Model

Every state-changing action SHALL create an audit event.

```text
Actor
Action
Object
Previous State
New State
Timestamp
Reason
Evidence
Authority
Correlation ID
```

Audit records SHALL be append-only from the business user's perspective.

---

# 25. Separation of Duties

The architecture SHALL support configurable separation of duties.

Examples:

```text
Validator ≠ Verifier
Verifier ≠ Acceptance Authority
Remediation Owner ≠ Independent Verifier
```

Exceptions SHALL require explicit authorised override and audit evidence.

---

# 26. Failure Handling

Failure SHALL be explicit.

```text
VALIDATION FAILURE
→ CORRECTION / REVALIDATION

VERIFICATION FAILURE
→ REWORK / REVERIFICATION

ACCEPTANCE FAILURE
→ REJECTION / ESCALATION

CLOSURE FAILURE
→ REMAIN OPEN

MONITORING FAILURE
→ INVESTIGATION

REGRESSION
→ REMEDIATION

REMEDIATION FAILURE
→ ESCALATION / REOPENING

REVALIDATION FAILURE
→ REMEDIATION / RESTRICTION

REACCEPTANCE FAILURE
→ RELIANCE REMAINS SUSPENDED
```

---

# 27. AI and Agent Considerations

Where AI or agents participate in PC-RG activities, the architecture SHALL distinguish:

```text
AI/AGENT MAY ASSIST
from
AI/AGENT MAY DECIDE
```

AI/agent participation SHALL be governed by:

- approved purpose;
- model/version;
- data scope;
- tools;
- permissions;
- human oversight;
- evidence requirements;
- confidence/uncertainty handling;
- auditability;
- override;
- failure handling.

A system SHALL NOT infer decision authority from automation capability.

---

# 28. Legacy Document Treatment

EA-IMETA-PC-RG-001–404 remain historical/source material until the consolidation matrix has been populated from their actual contents.

This document therefore does NOT assert:

```text
RG-001 = VAL
RG-002 = VER
...
RG-404 = RAC
```

without source evidence.

The target architecture is authoritative for design direction, but legacy disposition remains evidence-dependent.

---

# 29. Active Baseline Candidate

The proposed active architecture is:

```text
EA-IMETA-PC-RG-VAL
EA-IMETA-PC-RG-VER
EA-IMETA-PC-RG-ACC
EA-IMETA-PC-RG-CLO
EA-IMETA-PC-RG-MON
EA-IMETA-PC-RG-REG
EA-IMETA-PC-RG-REM
EA-IMETA-PC-RG-RVA
EA-IMETA-PC-RG-RAC
```

These are logical architecture identities.

Physical file numbering may be assigned later by the registry.

---

# 30. Architecture Acceptance Criteria

The active baseline is acceptable when:

- each responsibility has a unique purpose;
- each responsibility has defined inputs and outputs;
- each responsibility has a state transition;
- authority is defined;
- evidence is defined;
- controls are testable;
- MFM implementation boundaries are identifiable;
- cross-cutting capabilities do not create duplicate lifecycle stages;
- regression can trigger remediation;
- remediation can trigger revalidation;
- revalidation can trigger reacceptance;
- reopening and revocation are controlled;
- legacy traceability is preserved.

---

# 31. Prohibited Pattern

The following pattern is now prohibited for new active PC-RG architecture:

```text
RG-N
  ↓
add buzzword
  ↓
declare RG-N as Parent
  ↓
repeat architecture
  ↓
RG-N+1
```

unless a documented architectural review establishes a genuinely distinct responsibility.

---

# 32. Next Step

The next work item SHALL be evidence-driven.

The consolidation matrix from EA-IMETA-PC-RG-406 SHALL be populated using the actual contents of the legacy documents.

Only after that comparison SHALL the final active physical file set be approved.

Potential next artifact:

> **EA-IMETA-PC-RG-408 — Legacy-to-Active Requirement Traceability Matrix**

This remains conditional on the availability of the source inventory.

---

# 33. Governing Principle

> **The PC-RG architecture is a lifecycle of responsibilities and decisions, not a hierarchy of increasingly elaborate document titles.**

The active baseline SHALL remain finite, testable, implementable and traceable.

# END OF EA-IMETA-PC-RG-407
