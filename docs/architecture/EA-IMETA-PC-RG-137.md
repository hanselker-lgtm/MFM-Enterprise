# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-137`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-137` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Response Effectiveness Determination |
| Parent | EA-IMETA-PC-RG-136 — Mandatory Post-Closure Regression Response Execution Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory effectiveness-determination layer that determines whether an executed post-closure regression response achieved its defined objective, restored required conditions, reduced or controlled the identified consequence, and produced sufficient evidence to support continued monitoring, resolution, closure, revalidation, reacceptance or further response.

## Core Principle
Execution completion is not effectiveness. Effectiveness shall be determined against the approved response objective, success criteria, expected outcome, restored state and evidence requirements. A response shall not be declared effective merely because actions were performed, systems returned to service, a responsible authority reported completion, or the immediate symptom disappeared.

```text
COMPLETED / SUBSTANTIALLY COMPLETED RESPONSE
        ↓
EFFECTIVENESS CRITERIA APPLICABLE?
├── NO → DEFINE / ESCALATE / REASSESS
└── YES
     ↓
COMPARE
├── RESPONSE OBJECTIVE
├── EXPECTED OUTCOME
├── ACTUAL OUTCOME
├── SUCCESS CRITERIA
├── REQUIRED STATE
├── CONSEQUENCE CONTROL
└── RESIDUAL RISK
     ↓
EVIDENCE SUFFICIENT?
├── NO → INSUFFICIENT / REASSESS
└── YES
     ↓
EFFECTIVE?
├── NO → INEFFECTIVE / PARTIAL / FURTHER RESPONSE
└── YES
     ↓
VERIFY EFFECTIVENESS
     ↓
CONTINUE TO RESOLUTION / CLOSURE / MONITORING
```
## Effectiveness Quality Test
```text
VALID RESPONSE OBJECTIVE
+
DEFINED SUCCESS CRITERIA
+
COMPLETED / MATERIAL RESPONSE ACTIONS
+
VALID BEFORE / AFTER EVIDENCE
+
OUTCOME COMPARISON
+
CONSEQUENCE CONTROL
+
RESIDUAL RISK ASSESSMENT
+
INDEPENDENT / AUTHORIZED VERIFICATION WHERE REQUIRED
=
VALID GOVERNED EFFECTIVENESS DETERMINATION
```
## Execution vs Effectiveness vs Resolution
```text
EXECUTION
→ ACTIONS WERE PERFORMED

EFFECTIVENESS
→ ACTIONS ACHIEVED THE REQUIRED RESPONSE OUTCOME

RESOLUTION
→ THE UNDERLYING REGRESSION / CONDITION IS GOVERNED AS RESOLVED

CLOSURE
→ THE GOVERNED RESPONSE CASE IS FORMALLY CLOSED
```
## Effectiveness States
```text
EF0 — EFFECTIVENESS NOT REQUIRED
EF1 — EFFECTIVENESS ASSESSMENT PENDING
EF2 — EFFECTIVENESS ASSESSMENT IN PROGRESS
EF3 — EFFECTIVENESS CRITERIA NOT SATISFIED
EF4 — EFFECTIVENESS PARTIAL
EF5 — EFFECTIVENESS ACHIEVED
EF6 — EFFECTIVENESS VERIFIED
EF7 — EFFECTIVENESS NOT VERIFIED
EF8 — EFFECTIVENESS FAILED
EF9 — EFFECTIVENESS REQUIRES FURTHER RESPONSE
EF10 — EFFECTIVENESS REQUIRES EXTENDED MONITORING
EF11 — EFFECTIVENESS RECONFIRMATION REQUIRED
EF12 — EFFECTIVENESS SUPERSEDED
EF13 — EFFECTIVENESS REJECTED / REASSESSMENT
EF14 — EFFECTIVENESS INDEPENDENTLY CONFIRMED
EF15 — EFFECTIVENESS CLOSED / HANDED TO RESOLUTION
EFX — UNKNOWN / INSUFFICIENT BASIS
EFS — EFFECTIVENESS ASSESSMENT SUSPENDED
```
## Effectiveness Dimensions
| Dimension | Required determination |
|---|---|
| Objective | Required response outcome |
| Success Criteria | Required performance |
| Expected Outcome | Target state |
| Actual Outcome | Observed result |
| Evidence | Supporting proof |
| Comparison | Expected vs actual |
| Consequence | Controlled consequence |
| Residual Risk | Remaining exposure |
| Stability | Persistence of outcome |
| Verification | Effectiveness confirmation |
| Independence | Independent review where required |
| Reconfirmation | Future confirmation |
| Handover | Resolution / monitoring transition |

## Effectiveness Invariants

```text
EFFECTIVENESS SHALL BE DETERMINED AGAINST THE APPROVED RESPONSE OBJECTIVE AND SUCCESS CRITERIA
```

```text
EXECUTION COMPLETION SHALL NOT BE TREATED AS EFFECTIVENESS
```

```text
SYMPTOM DISAPPEARANCE SHALL NOT BY ITSELF PROVE EFFECTIVENESS
```

```text
THE ACTUAL OUTCOME SHALL BE COMPARED WITH THE EXPECTED OUTCOME OR REQUIRED STATE
```

```text
EVIDENCE SHALL BE SUFFICIENT TO SUPPORT THE EFFECTIVENESS DETERMINATION
```

```text
MATERIAL RESIDUAL RISK SHALL BE IDENTIFIED AND GOVERNED
```

```text
EFFECTIVENESS SHALL CONSIDER WHETHER THE OUTCOME IS STABLE FOR THE REQUIRED PERIOD
```

```text
PARTIAL EFFECTIVENESS SHALL REMAIN DISTINCT FROM FULL EFFECTIVENESS
```

```text
UNVERIFIED EFFECTIVENESS SHALL NOT BE RECORDED AS VERIFIED EFFECTIVENESS
```

```text
FAILED EFFECTIVENESS SHALL TRIGGER FURTHER RESPONSE, REASSESSMENT, ROLLBACK, REOPENING OR OTHER GOVERNED ACTION AS REQUIRED
```

```text
CRITICAL EFFECTIVENESS DETERMINATIONS SHALL USE INDEPENDENT VERIFICATION WHERE REQUIRED
```

```text
SECURITY, RESILIENCE, SAFETY, COMPLIANCE AND DATA EFFECTIVENESS SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT RESPONSE EFFECTIVENESS SHALL CONSIDER BOTH DIRECT OUTCOME AND UNINTENDED SECONDARY EFFECTS
```

```text
EFFECTIVENESS SHALL NOT AUTOMATICALLY ESTABLISH RESOLUTION
```

```text
EFFECTIVENESS SHALL NOT AUTOMATICALLY ESTABLISH CLOSURE
```

```text
RECONFIRMATION SHALL BE REQUIRED WHEN THE OUTCOME MAY DEGRADE OR WHEN GOVERNANCE REQUIRES LONGER OBSERVATION
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

## 1. Effectiveness Domain — Post-Closure Regression Response Effectiveness Governance

**Control family:** `PCREf-001`

The Post-Closure Regression Response Effectiveness Governance domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-001-01` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-02` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-03` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-04` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-05` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-06` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-001-07` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREf-001-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 2. Effectiveness Domain — Post-Closure Regression Response Effectiveness Objective

**Control family:** `PCREf-002`

The Post-Closure Regression Response Effectiveness Objective domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-002-01` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-02` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-03` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-04` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-05` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-06` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-002-07` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREf-002-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 3. Effectiveness Domain — Post-Closure Regression Response Effectiveness Definition

**Control family:** `PCREf-003`

The Post-Closure Regression Response Effectiveness Definition domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-003-01` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-02` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-03` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-04` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-05` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-06` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-003-07` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREf-003-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 4. Effectiveness Domain — Post-Closure Regression Response Effectiveness Scope

**Control family:** `PCREf-004`

The Post-Closure Regression Response Effectiveness Scope domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-004-01` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-02` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-03` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-04` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-05` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-06` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-004-07` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREf-004-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 5. Effectiveness Domain — Post-Closure Regression Response Effectiveness Authority

**Control family:** `PCREf-005`

The Post-Closure Regression Response Effectiveness Authority domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-005-01` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-02` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-03` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-04` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-05` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-06` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-005-07` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREf-005-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 6. Effectiveness Domain — Post-Closure Regression Response Effectiveness Criteria

**Control family:** `PCREf-006`

The Post-Closure Regression Response Effectiveness Criteria domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-006-01` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-02` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-03` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-04` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-05` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-06` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-006-07` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREf-006-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 7. Effectiveness Domain — Post-Closure Regression Response Effectiveness Preconditions

**Control family:** `PCREf-007`

The Post-Closure Regression Response Effectiveness Preconditions domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-007-01` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-02` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-03` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-04` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-05` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-06` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-007-07` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREf-007-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 8. Effectiveness Domain — Post-Closure Regression Response Effectiveness Evidence

**Control family:** `PCREf-008`

The Post-Closure Regression Response Effectiveness Evidence domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-008-01` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-02` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-03` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-04` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-05` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-06` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-008-07` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREf-008-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 9. Effectiveness Domain — Post-Closure Regression Response Effectiveness Method

**Control family:** `PCREf-009`

The Post-Closure Regression Response Effectiveness Method domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-009-01` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-02` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-03` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-04` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-05` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-06` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-009-07` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREf-009-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 10. Effectiveness Domain — Post-Closure Regression Response Effectiveness Decision

**Control family:** `PCREf-010`

The Post-Closure Regression Response Effectiveness Decision domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-010-01` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-02` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-03` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-04` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-05` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-06` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-010-07` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREf-010-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 11. Effectiveness Domain — Post-Closure Regression Response Effectiveness Accountability

**Control family:** `PCREf-011`

The Post-Closure Regression Response Effectiveness Accountability domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-011-01` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-02` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-03` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-04` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-05` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-06` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-011-07` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREf-011-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 12. Effectiveness Domain — Post-Closure Regression Response Effectiveness Timing

**Control family:** `PCREf-012`

The Post-Closure Regression Response Effectiveness Timing domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-012-01` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-02` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-03` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-04` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-05` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-06` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-012-07` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREf-012-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 13. Effectiveness Domain — Security Post-Closure Regression Response Effectiveness

**Control family:** `PCREf-013`

The Security Post-Closure Regression Response Effectiveness domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-013-01` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-02` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-03` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-04` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-05` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-06` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-013-07` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREf-013-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 14. Effectiveness Domain — Resilience Post-Closure Regression Response Effectiveness

**Control family:** `PCREf-014`

The Resilience Post-Closure Regression Response Effectiveness domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-014-01` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-02` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-03` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-04` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-05` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-06` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-014-07` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREf-014-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 15. Effectiveness Domain — Compliance Post-Closure Regression Response Effectiveness

**Control family:** `PCREf-015`

The Compliance Post-Closure Regression Response Effectiveness domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-015-01` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-02` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-03` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-04` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-05` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-06` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-015-07` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREf-015-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 16. Effectiveness Domain — Data Post-Closure Regression Response Effectiveness

**Control family:** `PCREf-016`

The Data Post-Closure Regression Response Effectiveness domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-016-01` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-02` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-03` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-04` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-05` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-06` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-016-07` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREf-016-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 17. Effectiveness Domain — AI and Agent Post-Closure Regression Response Effectiveness

**Control family:** `PCREf-017`

The AI and Agent Post-Closure Regression Response Effectiveness domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-017-01` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-02` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-03` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-04` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-05` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-06` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-017-07` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREf-017-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 18. Effectiveness Domain — Post-Closure Regression Response Effectiveness Failure

**Control family:** `PCREf-018`

The Post-Closure Regression Response Effectiveness Failure domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-018-01` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-02` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-03` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-04` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-05` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-06` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-018-07` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREf-018-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 19. Effectiveness Domain — Post-Closure Regression Response Effectiveness Independence

**Control family:** `PCREf-019`

The Post-Closure Regression Response Effectiveness Independence domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-019-01` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-02` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-03` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-04` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-05` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-06` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-019-07` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREf-019-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## 20. Effectiveness Domain — Post-Closure Regression Response Effectiveness Review and Learning

**Control family:** `PCREf-020`

The Post-Closure Regression Response Effectiveness Review and Learning domain establishes governed mandatory response-effectiveness requirements.

### Required controls
- `PCREf-020-01` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-01-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-02` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-02-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-03` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-03-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-04` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-04-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-05` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-05-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-06` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-06-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.
- `PCREf-020-07` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREf-020-07-E` — Preserve objective, criteria, expected outcome, actual outcome, evidence, comparison, consequence, residual risk, stability, verification, independence and transition traceability.

```text
EXECUTED RESPONSE → COMPARE OUTCOME → VERIFY EFFECTIVENESS → RESOLUTION / MONITORING
```

## Post-Closure Regression Response Effectiveness Structure

| Element | Required definition |
|---|---|
| Objective | Response objective |
| Criteria | Success criteria |
| Expected Outcome | Target state |
| Actual Outcome | Observed state |
| Evidence | Proof |
| Comparison | Expected vs actual |
| Consequence | Controlled consequence |
| Residual Risk | Remaining exposure |
| Stability | Persistence |
| Verification | Confirmation |
| Independence | Review requirement |
| Reconfirmation | Future confirmation |
| Transition | Resolution / monitoring |

## Post-Closure Regression Response Effectiveness Objective

Determine whether the response achieved its approved objective and whether the resulting condition is sufficiently controlled, stable and evidenced for the next governed state.

## Post-Closure Regression Response Effectiveness Definition

Effectiveness determination is the governed decision that executed response actions achieved the required outcome against defined criteria and evidence.

## Post-Closure Regression Response Effectiveness Scope

Scope includes outcome comparison, success criteria, consequence control, residual risk, stability, verification, independent confirmation and transition to resolution or continued monitoring.

## Post-Closure Regression Response Effectiveness Authority

Authority shall define who may determine, verify, reject, override, independently confirm or reopen an effectiveness determination.

## Post-Closure Regression Response Effectiveness Criteria

Criteria shall define objective, expected outcome, required state, measurable success criteria, acceptable residual risk and required stability period.
```text
EXECUTED RESPONSE
↓
EXPECTED OUTCOME
+
SUCCESS CRITERIA
↓
ACTUAL OUTCOME
↓
COMPARE
↓
EVIDENCE SUFFICIENT?
├── NO → REASSESS
└── YES
     ↓
EFFECTIVE?
├── NO → FURTHER RESPONSE
└── YES → VERIFY
```

## Post-Closure Regression Response Effectiveness Preconditions

Preconditions include completed or materially sufficient response execution, defined objective, success criteria, evidence and outcome comparison method.

## Post-Closure Regression Response Effectiveness Evidence

Evidence shall preserve before/after state, action results, measurements, observations, exceptions, residual risk and verification records.

## Post-Closure Regression Response Effectiveness Method

Methods may include quantitative comparison, qualitative assessment, control verification, test evidence, operational observation, independent review and stability monitoring.
```text
BASELINE / PRE-RESPONSE
↓
RESPONSE OUTCOME
↓
MEASURE
↓
COMPARE
↓
QUALIFY
↓
VERIFY
```

## Post-Closure Regression Response Effectiveness Decision

Decision shall determine EF0, EF1, EF2, EF3, EF4, EF5, EF6, EF7, EF8, EF9, EF10, EF11, EF12, EF13, EF14, EF15, EFX or EFS.

## Post-Closure Regression Response Effectiveness Accountability

Accountability shall remain explicit for evidence sufficiency, comparison, residual risk, verification, independent confirmation and transition recommendation.

## Post-Closure Regression Response Effectiveness Timing

Effectiveness shall be determined promptly after execution where immediate verification is possible, with extended monitoring where stability cannot be established immediately.

## Security Post-Closure Regression Response Effectiveness

Security effectiveness shall consider containment, eradication, control restoration, evidence integrity, recurrence risk and residual exposure.

## Resilience Post-Closure Regression Response Effectiveness

Resilience effectiveness shall consider service restoration, continuity objectives, recovery integrity, dependency stability and recurrence risk.

## Compliance Post-Closure Regression Response Effectiveness

Compliance effectiveness shall consider restored compliance, evidence sufficiency, control operation, reporting obligations and residual exposure.

## Data Post-Closure Regression Response Effectiveness

Data effectiveness shall consider integrity, confidentiality, availability, lineage, access control, recovery and downstream consistency.

## AI and Agent Post-Closure Regression Response Effectiveness

AI/agent effectiveness shall evaluate intended outcome, unintended effects, policy adherence, authority compliance, tool behavior, data effects and recurrence risk.
```text
AI / AGENT RESPONSE
↓
INTENDED OUTCOME
+
UNINTENDED EFFECTS
+
POLICY / AUTHORITY COMPLIANCE
↓
COMPARE
↓
VERIFY EFFECTIVENESS
```

## Post-Closure Regression Response Effectiveness Failure

Failure includes insufficient outcome, unstable outcome, residual material risk, recurrence, evidence deficiency, verification failure or unintended consequence.
```text
EFFECTIVENESS FAILURE
↓
MATERIAL?
├── YES → FURTHER RESPONSE / REOPEN / ESCALATE
└── NO → CORRECT / MONITOR / REASSESS
```

## Post-Closure Regression Response Effectiveness Independence

Independent confirmation shall be used where consequence, governance, safety, security, compliance or conflict of interest requires independent assurance.

## Post-Closure Regression Response Effectiveness Review and Learning

Reviews shall examine false effectiveness, premature closure, inadequate criteria, weak evidence, residual risk, unstable outcomes and recurrence.

## Effectiveness Decision Model
```text
COMPLETED / MATERIAL RESPONSE
↓
DEFINE / CONFIRM OBJECTIVE + SUCCESS CRITERIA
↓
COMPARE EXPECTED VS ACTUAL
↓
EVIDENCE SUFFICIENT?
├── NO → ASSESSMENT PENDING / REASSESS
└── YES
     ↓
CONSEQUENCE CONTROLLED?
├── NO → INEFFECTIVE / FURTHER RESPONSE
└── YES
     ↓
RESIDUAL RISK ACCEPTABLE?
├── NO → FURTHER RESPONSE / ESCALATE
└── YES
     ↓
OUTCOME STABLE?
├── NO → EXTENDED MONITORING / RECONFIRMATION
└── YES
     ↓
VERIFY EFFECTIVENESS
     ↓
HANDOVER TO RESOLUTION / CONTINUED MONITORING
```

## Effectiveness Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| EF0 | Not required | Record basis |
| EF1 | Assessment pending | Gather evidence |
| EF2 | Assessment in progress | Compare / qualify |
| EF3 | Criteria not satisfied | Further response |
| EF4 | Partial effectiveness | Correct / monitor |
| EF5 | Achieved | Verify |
| EF6 | Verified | Transition |
| EF7 | Not verified | Reassess / obtain evidence |
| EF8 | Failed | Further response / reopen |
| EF9 | Further response required | Reactivate response |
| EF10 | Extended monitoring required | Monitor stability |
| EF11 | Reconfirmation required | Revalidate outcome |
| EF12 | Superseded | Preserve record |
| EF13 | Rejected / reassessment | Correct / review |
| EF14 | Independently confirmed | Continue governed transition |
| EF15 | Closed / handed to resolution | Resolution governance |
| EFX | Unknown | Do not assume effectiveness |
| EFS | Suspended | Restore assessment |

## Effectiveness Record
| Field | Required |
|---|---|
| Effectiveness ID | Yes |
| Execution ID | Yes |
| Objective | Yes |
| Success Criteria | Yes |
| Expected Outcome | Yes |
| Actual Outcome | Yes |
| Evidence | Yes |
| Comparison | Yes |
| Consequence | Yes |
| Residual Risk | Yes |
| Stability | Where applicable |
| Verification | Yes |
| Independent Review | Where required |
| Reconfirmation | Where required |
| Effectiveness State | Yes |
| Transition Decision | Yes |
| Audit Trail | Yes |

## Execution Is Not Effectiveness
An action can be completed without achieving its objective.
```text
EXECUTION COMPLETE
≠
EFFECTIVE
```

## Effectiveness Is Not Resolution
A response can be effective against an immediate objective while the broader underlying condition still requires resolution work or monitoring.
```text
EFFECTIVE
≠
RESOLVED
```

## Effectiveness Is Not Closure
Effectiveness is an outcome determination. Closure is a separate governance decision based on the full case and applicable closure criteria.
```text
EFFECTIVE
≠
CLOSED
```

## Outcome Comparison
Effectiveness requires comparison between the expected outcome and actual outcome using the applicable measures, observations or evidence.

## Residual Risk
Residual risk shall be explicit. An effective response may still require continued monitoring where residual exposure remains material or stability is not yet demonstrated.

## Stability
Where outcomes can regress, effectiveness shall include a stability period or defined monitoring requirement.

## Partial Effectiveness
Partial effectiveness shall not be silently promoted to full effectiveness.

## Independent Confirmation
Where required, independent confirmation shall be performed by an actor with appropriate independence and authority.

## Reconfirmation
Material degradation, changed assumptions or defined time-based conditions shall trigger reconfirmation.

## Further Response
Failure to demonstrate effectiveness shall return the case to an appropriate response state rather than allowing closure by default.

## AI and Agent Effectiveness
AI/agent effectiveness shall include unintended behavior and secondary effects, not only the direct target outcome.

## Relationship to Resolution
RG-137 supplies verified effectiveness to the subsequent resolution-determination layer.
```text
RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression response-effectiveness layer beneath response execution and above resolution determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, qualification, validation, deviation, regression determination, regression classification, consequence determination, alert determination, notification determination, acknowledgement determination, response initiation, authority transfer, response execution, resolution, closure, monitoring activation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Effectiveness Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → MANDATORY RESPONSE EFFECTIVENESS DETERMINATION → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → DEVIATION DETERMINATION → REGRESSION DETERMINATION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Effectiveness Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ISSUE ALERT → DETERMINE NOTIFICATION → ISSUE NOTIFICATION → DELIVER → DETERMINE ACKNOWLEDGEMENT → VALIDATE ACTOR / TIMING / COMPLETENESS → ACKNOWLEDGE → ACCEPT / ASSIGN → DETERMINE RESPONSE INITIATION → AUTHORIZE → ASSIGN → ACTIVATE → VERIFY → DETERMINE AUTHORITY TRANSFER → IDENTIFY RECEIVER → PACKAGE STATE → ACCEPT → VERIFY → ACTIVATE RECEIVING AUTHORITY → DETERMINE EXECUTION → AUTHORIZE ACTION → EXECUTE → OBSERVE → VERIFY → ADJUST / ESCALATE / ROLLBACK / STOP → COMPLETE → DETERMINE EFFECTIVENESS → VERIFY → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-138` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Resolution Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION RESPONSE TO BE EVALUATED AGAINST AN EXPLICIT RESPONSE OBJECTIVE, SUCCESS CRITERIA, EXPECTED OUTCOME, ACTUAL OUTCOME, EVIDENCE, CONSEQUENCE CONTROL, RESIDUAL RISK AND REQUIRED STABILITY, WITH EXECUTION COMPLETION NEVER TREATED AS EFFECTIVENESS, PARTIAL OR UNVERIFIED EFFECTIVENESS NEVER SILENTLY PROMOTED TO FULL EFFECTIVENESS, AND FAILED OR UNSTABLE EFFECTIVENESS RETURNING THE CASE TO FURTHER RESPONSE, REASSESSMENT OR EXTENDED MONITORING AS GOVERNED.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01
