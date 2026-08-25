# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-119`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-119` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Response Effectiveness Determination |
| Parent | EA-IMETA-PC-RG-118 — Mandatory Post-Closure Regression Response Execution Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory effectiveness-determination layer that determines whether an executed post-closure regression response has actually achieved its required outcome, reduced the relevant consequence, restored required control conditions and produced sufficient evidence to justify continuation, adjustment, escalation, closure or reopening.

## Core Principle
Execution completion proves that authorized actions were performed. Effectiveness proves that those actions achieved the required response outcome. Completion shall never be treated as effectiveness without outcome evidence.

```text
RESPONSE EXECUTED
        ↓
COMPLETION VERIFIED?
├── NO → CONTINUE / CORRECT EXECUTION
└── YES
     ↓
DEFINE REQUIRED OUTCOME
     ↓
MEASURE ACTUAL RESULT
     ↓
COMPARE ACTUAL VS REQUIRED
     ↓
ASSESS CONSEQUENCE REDUCTION
     ↓
ASSESS CONTROL RESTORATION
     ↓
DETERMINE EFFECTIVENESS
├── EFFECTIVE → CONTROLLED TRANSITION
├── PARTIALLY EFFECTIVE → ADJUST / CONTINUE
└── INEFFECTIVE → ESCALATE / REOPEN / ALTERNATE RESPONSE
```

## Effectiveness Quality Test
```text
VALID RESPONSE OBJECTIVE
+
VERIFIED EXECUTION
+
DEFINED SUCCESS CRITERIA
+
VALID MEASUREMENTS
+
BASELINE / TARGET COMPARISON
+
CONSEQUENCE ASSESSMENT
+
CONTROL RESTORATION ASSESSMENT
+
INDEPENDENT ASSURANCE WHERE REQUIRED
+
TRACEABLE EVIDENCE
=
VALID GOVERNED RESPONSE EFFECTIVENESS DETERMINATION
```

## Completion vs Effectiveness vs Resolution
```text
COMPLETION
→ ACTIONS WERE PERFORMED

EFFECTIVENESS
→ ACTIONS ACHIEVED THE REQUIRED RESPONSE OUTCOME

RESOLUTION
→ THE GOVERNED CONDITION HAS BEEN BROUGHT TO AN ACCEPTED RESOLVED STATE
```

## Effectiveness States
```text
F0 — NOT APPLICABLE / NOT REQUIRED
F1 — NOT YET ASSESSABLE
F2 — ASSESSMENT IN PROGRESS
F3 — PARTIALLY EFFECTIVE
F4 — EFFECTIVE
F5 — HIGHLY EFFECTIVE / TARGET EXCEEDED
FX — UNKNOWN / INVALID EVIDENCE
FF — INEFFECTIVE / FAILED
FR — EFFECTIVE FOR CURRENT STATE; CONTINUED MONITORING REQUIRED
```

## Effectiveness Dimensions
| Dimension | Required determination |
|---|---|
| Objective | Required response outcome |
| Target | Required performance state |
| Baseline | Pre-response comparison state |
| Actual Result | Measured post-response state |
| Consequence | Residual consequence |
| Control State | Restored / degraded / unknown |
| Sustainability | Persistence of achieved state |
| Evidence | Supporting evidence |
| Confidence | Confidence in determination |
| Independence | Independent assurance requirement |
| Decision | Continue / close / adjust / reopen |

## Effectiveness Invariants

```text
EFFECTIVENESS SHALL BE ASSESSED AGAINST EXPLICIT RESPONSE OBJECTIVES AND SUCCESS CRITERIA
```

```text
EXECUTION COMPLETION SHALL NOT BE USED AS A SUBSTITUTE FOR EFFECTIVENESS
```

```text
ACTUAL RESULTS SHALL BE COMPARED WITH THE REQUIRED TARGET OR ACCEPTANCE CONDITION
```

```text
RESIDUAL CONSEQUENCE SHALL BE ASSESSED
```

```text
CONTROL RESTORATION SHALL BE ASSESSED SEPARATELY WHERE MATERIAL
```

```text
EFFECTIVENESS SHALL CONSIDER SUSTAINABILITY WHERE TRANSIENT IMPROVEMENT IS INSUFFICIENT
```

```text
UNKNOWN OR INSUFFICIENT EVIDENCE SHALL NOT BE TREATED AS EFFECTIVE
```

```text
PARTIAL EFFECTIVENESS SHALL REMAIN AN ACTIVE GOVERNANCE STATE
```

```text
INEFFECTIVENESS SHALL TRIGGER CONTROLLED CONTINUATION, ADJUSTMENT, ESCALATION OR ALTERNATE RESPONSE
```

```text
HIGH-CONSEQUENCE EFFECTIVENESS MAY REQUIRE INDEPENDENT VERIFICATION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE EFFECTIVENESS SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT EFFECTIVENESS SHALL INCLUDE BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT OUTCOMES WHERE RELEVANT
```

```text
EFFECTIVENESS SHALL NOT BE DECLARED SOLELY BY THE PARTY BENEFITING FROM CLOSURE WHERE INDEPENDENCE IS REQUIRED
```

```text
EFFECTIVENESS SHALL REMAIN TRACEABLE TO THE REGRESSION, CONSEQUENCE AND RESPONSE
```

```text
SHORT-TERM EFFECTIVENESS SHALL NOT AUTOMATICALLY ESTABLISH SUSTAINED EFFECTIVENESS
```

```text
EFFECTIVENESS CRITERIA SHALL BE REVIEWED AFTER FAILED, PARTIAL OR REVERSED RESPONSES
```

## 1. Effectiveness Domain — Post-Closure Regression Response Effectiveness Governance

**Control family:** `PCREFF-001`

The Post-Closure Regression Response Effectiveness Governance domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-001-01` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-02` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-03` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-04` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-05` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-06` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-001-07` — Establish and maintain the post-closure regression response effectiveness governance control.
- `PCREFF-001-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 2. Effectiveness Domain — Post-Closure Regression Response Effectiveness Objective

**Control family:** `PCREFF-002`

The Post-Closure Regression Response Effectiveness Objective domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-002-01` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-02` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-03` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-04` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-05` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-06` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-002-07` — Establish and maintain the post-closure regression response effectiveness objective control.
- `PCREFF-002-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 3. Effectiveness Domain — Post-Closure Regression Response Effectiveness Definition

**Control family:** `PCREFF-003`

The Post-Closure Regression Response Effectiveness Definition domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-003-01` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-02` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-03` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-04` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-05` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-06` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-003-07` — Establish and maintain the post-closure regression response effectiveness definition control.
- `PCREFF-003-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 4. Effectiveness Domain — Post-Closure Regression Response Effectiveness Scope

**Control family:** `PCREFF-004`

The Post-Closure Regression Response Effectiveness Scope domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-004-01` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-02` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-03` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-04` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-05` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-06` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-004-07` — Establish and maintain the post-closure regression response effectiveness scope control.
- `PCREFF-004-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 5. Effectiveness Domain — Post-Closure Regression Response Effectiveness Authority

**Control family:** `PCREFF-005`

The Post-Closure Regression Response Effectiveness Authority domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-005-01` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-02` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-03` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-04` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-05` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-06` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-005-07` — Establish and maintain the post-closure regression response effectiveness authority control.
- `PCREFF-005-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 6. Effectiveness Domain — Post-Closure Regression Response Effectiveness Criteria

**Control family:** `PCREFF-006`

The Post-Closure Regression Response Effectiveness Criteria domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-006-01` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-02` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-03` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-04` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-05` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-06` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-006-07` — Establish and maintain the post-closure regression response effectiveness criteria control.
- `PCREFF-006-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 7. Effectiveness Domain — Post-Closure Regression Response Effectiveness Preconditions

**Control family:** `PCREFF-007`

The Post-Closure Regression Response Effectiveness Preconditions domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-007-01` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-02` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-03` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-04` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-05` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-06` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-007-07` — Establish and maintain the post-closure regression response effectiveness preconditions control.
- `PCREFF-007-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 8. Effectiveness Domain — Post-Closure Regression Response Effectiveness Evidence

**Control family:** `PCREFF-008`

The Post-Closure Regression Response Effectiveness Evidence domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-008-01` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-02` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-03` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-04` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-05` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-06` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-008-07` — Establish and maintain the post-closure regression response effectiveness evidence control.
- `PCREFF-008-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 9. Effectiveness Domain — Post-Closure Regression Response Effectiveness Method

**Control family:** `PCREFF-009`

The Post-Closure Regression Response Effectiveness Method domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-009-01` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-02` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-03` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-04` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-05` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-06` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-009-07` — Establish and maintain the post-closure regression response effectiveness method control.
- `PCREFF-009-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 10. Effectiveness Domain — Post-Closure Regression Response Effectiveness Decision

**Control family:** `PCREFF-010`

The Post-Closure Regression Response Effectiveness Decision domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-010-01` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-02` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-03` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-04` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-05` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-06` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-010-07` — Establish and maintain the post-closure regression response effectiveness decision control.
- `PCREFF-010-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 11. Effectiveness Domain — Post-Closure Regression Response Effectiveness Accountability

**Control family:** `PCREFF-011`

The Post-Closure Regression Response Effectiveness Accountability domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-011-01` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-02` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-03` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-04` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-05` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-06` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-011-07` — Establish and maintain the post-closure regression response effectiveness accountability control.
- `PCREFF-011-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 12. Effectiveness Domain — Post-Closure Regression Response Effectiveness Timing

**Control family:** `PCREFF-012`

The Post-Closure Regression Response Effectiveness Timing domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-012-01` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-02` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-03` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-04` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-05` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-06` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-012-07` — Establish and maintain the post-closure regression response effectiveness timing control.
- `PCREFF-012-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 13. Effectiveness Domain — Security Post-Closure Regression Response Effectiveness

**Control family:** `PCREFF-013`

The Security Post-Closure Regression Response Effectiveness domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-013-01` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-02` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-03` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-04` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-05` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-06` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-013-07` — Establish and maintain the security post-closure regression response effectiveness control.
- `PCREFF-013-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 14. Effectiveness Domain — Resilience Post-Closure Regression Response Effectiveness

**Control family:** `PCREFF-014`

The Resilience Post-Closure Regression Response Effectiveness domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-014-01` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-02` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-03` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-04` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-05` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-06` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-014-07` — Establish and maintain the resilience post-closure regression response effectiveness control.
- `PCREFF-014-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 15. Effectiveness Domain — Compliance Post-Closure Regression Response Effectiveness

**Control family:** `PCREFF-015`

The Compliance Post-Closure Regression Response Effectiveness domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-015-01` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-02` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-03` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-04` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-05` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-06` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-015-07` — Establish and maintain the compliance post-closure regression response effectiveness control.
- `PCREFF-015-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 16. Effectiveness Domain — Data Post-Closure Regression Response Effectiveness

**Control family:** `PCREFF-016`

The Data Post-Closure Regression Response Effectiveness domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-016-01` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-02` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-03` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-04` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-05` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-06` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-016-07` — Establish and maintain the data post-closure regression response effectiveness control.
- `PCREFF-016-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 17. Effectiveness Domain — AI and Agent Post-Closure Regression Response Effectiveness

**Control family:** `PCREFF-017`

The AI and Agent Post-Closure Regression Response Effectiveness domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-017-01` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-02` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-03` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-04` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-05` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-06` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-017-07` — Establish and maintain the ai and agent post-closure regression response effectiveness control.
- `PCREFF-017-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 18. Effectiveness Domain — Post-Closure Regression Response Effectiveness Failure

**Control family:** `PCREFF-018`

The Post-Closure Regression Response Effectiveness Failure domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-018-01` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-02` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-03` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-04` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-05` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-06` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-018-07` — Establish and maintain the post-closure regression response effectiveness failure control.
- `PCREFF-018-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 19. Effectiveness Domain — Post-Closure Regression Response Effectiveness Independence

**Control family:** `PCREFF-019`

The Post-Closure Regression Response Effectiveness Independence domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-019-01` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-02` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-03` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-04` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-05` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-06` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-019-07` — Establish and maintain the post-closure regression response effectiveness independence control.
- `PCREFF-019-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## 20. Effectiveness Domain — Post-Closure Regression Response Effectiveness Review and Learning

**Control family:** `PCREFF-020`

The Post-Closure Regression Response Effectiveness Review and Learning domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCREFF-020-01` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-01-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-02` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-02-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-03` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-03-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-04` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-04-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-05` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-05-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-06` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-06-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.
- `PCREFF-020-07` — Establish and maintain the post-closure regression response effectiveness review and learning control.
- `PCREFF-020-07-E` — Preserve objective, target, baseline, actual result, residual consequence, control state, sustainability, confidence, independence and decision evidence.

```text
OBJECTIVE → MEASURE → COMPARE → ASSESS → DETERMINE → CONTINUE / CLOSE / REOPEN
```

## Post-Closure Regression Response Effectiveness Structure

| Element | Required definition |
|---|---|
| Objective | Required response outcome |
| Target | Required acceptance state |
| Baseline | Pre-response state |
| Actual | Measured achieved state |
| Residual Consequence | Remaining impact |
| Control State | Current control condition |
| Sustainability | Persistence requirement |
| Evidence | Supporting evidence |
| Confidence | Determination confidence |
| Decision | Next governance action |

## Post-Closure Regression Response Effectiveness Objective

Determine whether the executed response has achieved the required outcome and reduced or controlled the regression consequence sufficiently to justify the next governed state.

## Post-Closure Regression Response Effectiveness Definition

Effectiveness is the evidence-based determination that executed response actions have achieved the required objective to the degree defined by the applicable success criteria, including any required consequence reduction and control restoration.

## Post-Closure Regression Response Effectiveness Scope

Scope includes immediate, operational, technical, safety, security, resilience, compliance, data, financial, governance and reliance outcomes where relevant.

## Post-Closure Regression Response Effectiveness Authority

Authority shall define who may determine effectiveness, who may independently verify it, who may accept residual risk and who may authorize closure or reopening.

## Post-Closure Regression Response Effectiveness Criteria

Criteria shall define target state, baseline, metrics, thresholds, evidence sufficiency, residual consequence, sustainability and decision consequences.
```text
RESPONSE COMPLETE
↓
TARGET DEFINED
↓
MEASURE ACTUAL
↓
COMPARE
↓
RESIDUAL CONSEQUENCE
↓
CONTROL RESTORED?
↓
EFFECTIVE?
```

## Post-Closure Regression Response Effectiveness Preconditions

Preconditions include verified execution, defined objective, measurable criteria, valid evidence, baseline or equivalent comparison state and appropriate authority.

## Post-Closure Regression Response Effectiveness Evidence

Evidence shall preserve target, baseline, measurements, timestamps, methods, actual result, residual consequence, control state, confidence and independent assurance where applicable.

## Post-Closure Regression Response Effectiveness Method

Methods may include metric comparison, control testing, outcome verification, scenario testing, operational observation, independent assurance and sustained monitoring.
```text
TARGET
↓
MEASURE
↓
COMPARE
↓
VERIFY
↓
ASSESS RESIDUAL RISK
↓
DETERMINE
```

## Post-Closure Regression Response Effectiveness Decision

Decision shall determine F0, F1, F2, F3, F4, F5, FX, FF or FR and the associated continuation, adjustment, closure or reopening action.

## Post-Closure Regression Response Effectiveness Accountability

Accountability shall remain explicit for criteria selection, measurement validity, determination, residual consequence and transition decision.

## Post-Closure Regression Response Effectiveness Timing

Effectiveness shall be assessed when evidence becomes sufficient and again at defined intervals where persistence or regression risk requires sustained confirmation.

## Security Post-Closure Regression Response Effectiveness

Security effectiveness shall consider containment, residual exposure, control restoration, attack-path closure, privilege state and evidence integrity.

## Resilience Post-Closure Regression Response Effectiveness

Resilience effectiveness shall consider service restoration, recovery capability, redundancy, fallback readiness and sustained operating capacity.

## Compliance Post-Closure Regression Response Effectiveness

Compliance effectiveness shall consider restored obligations, completed remediation, evidence sufficiency, reporting and acceptance requirements.

## Data Post-Closure Regression Response Effectiveness

Data effectiveness shall consider integrity, confidentiality, availability, quality, lineage, recovery and downstream decision correctness as relevant.

## AI and Agent Post-Closure Regression Response Effectiveness

AI/agent effectiveness shall assess behavior, authority boundaries, autonomy, tool use, data handling and human oversight outcomes where relevant.
```text
AI / AGENT RESPONSE
↓
BEHAVIOR RESULT
+
AUTHORITY RESULT
+
TOOL RESULT
+
DATA RESULT
+
OVERSIGHT RESULT
↓
EFFECTIVENESS
```

## Post-Closure Regression Response Effectiveness Failure

Failure includes insufficient evidence, invalid metrics, target not achieved, residual consequence remaining material, control not restored, recurrence or inability to sustain the result.
```text
INEFFECTIVE / UNCERTAIN
↓
MATERIAL CONDITION REMAINS?
├── YES → CONTINUE / ADJUST / ESCALATE / REOPEN
└── NO → REASSESS / VERIFY
```

## Post-Closure Regression Response Effectiveness Independence

Independent determination or verification may be required where consequence is high, closure is material, evidence is contested or the executing party has a conflict of interest.

## Post-Closure Regression Response Effectiveness Review and Learning

Reviews shall examine false effectiveness, premature closure, inadequate criteria, weak measurement, recurring regression and responses that appeared effective only temporarily.

## Effectiveness Determination Model
```text
RESPONSE EXECUTED
↓
COMPLETION VERIFIED?
├── NO → CONTINUE / CORRECT EXECUTION
└── YES
     ↓
DEFINE REQUIRED OUTCOME
     ↓
MEASURE ACTUAL RESULT
     ↓
COMPARE ACTUAL VS TARGET
     ↓
ASSESS RESIDUAL CONSEQUENCE
     ↓
ASSESS CONTROL RESTORATION
     ↓
ASSESS SUSTAINABILITY
     ↓
EFFECTIVE?
├── YES → CONTROLLED TRANSITION
├── PARTIAL → ADJUST / CONTINUE
└── NO / UNKNOWN → ESCALATE / REOPEN / ALTERNATE RESPONSE
```

## Effectiveness Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| F0 | Not applicable / not required | Record basis |
| F1 | Not yet assessable | Acquire evidence |
| F2 | Assessment in progress | Continue assessment |
| F3 | Partially effective | Adjust / continue |
| F4 | Effective | Controlled transition |
| F5 | Highly effective / target exceeded | Controlled transition with evidence |
| FX | Unknown / invalid evidence | Treat as unresolved |
| FF | Ineffective / failed | Escalate / alternate response |
| FR | Effective for current state; monitoring required | Continue monitoring |

## Effectiveness Record
| Field | Required |
|---|---|
| Effectiveness ID | Yes |
| Response ID | Yes |
| Objective | Yes |
| Target | Yes |
| Baseline | Yes where available |
| Measurements | Yes |
| Actual Result | Yes |
| Residual Consequence | Yes |
| Control State | Yes |
| Sustainability | Where applicable |
| Confidence | Yes |
| Independent Assurance | Where required |
| Decision | Yes |
| Evidence | Yes |

## Completion Is Not Effectiveness
Execution completion establishes that actions were performed. Effectiveness requires evidence that the required outcome was achieved.
```text
COMPLETED
≠
EFFECTIVE
```

## Target Definition
Targets shall be explicit, measurable where practicable and linked to the response objective and applicable success criteria.

## Baseline
Effectiveness should compare the post-response state against the pre-response condition or another valid reference state. Where a conventional baseline is unavailable, an approved equivalent comparison basis shall be documented.

## Residual Consequence
The determination shall assess what consequence remains after execution, including direct, indirect and second-order impacts where material.

## Control Restoration
Where the response objective includes restoration of a control state, effectiveness shall separately establish whether the control has actually returned to the required condition.

## Sustainability
Temporary improvement shall not automatically be considered sustained effectiveness.
```text
IMMEDIATE RESULT
↓
SUSTAINED RESULT?
├── NO → FR / CONTINUE MONITORING
└── YES → EFFECTIVENESS CONFIRMED
```

## Confidence
Confidence shall reflect evidence quality, measurement reliability, uncertainty and independent assurance requirements.

## Unknown Evidence
Unknown or insufficient evidence is not equivalent to effectiveness.
```text
UNKNOWN
≠
EFFECTIVE
```

## Partial Effectiveness
Partial effectiveness remains an active governance state and shall not be silently rounded up to effective.

## Ineffectiveness
If the response fails to achieve the required outcome, additional, alternate or escalated response shall be considered according to consequence.

## Reopening
Where effectiveness evidence demonstrates that the regression or consequence remains materially unresolved, the governed case shall be continued or reopened rather than closed.

## Independent Verification
High-consequence effectiveness may require independent verification before transition to closure or reliance restoration.

## AI and Agent Effectiveness
AI/agent effectiveness shall not be based solely on internal confidence or self-reported success. External outcome evidence and required human assurance shall be used where applicable.

## Relationship to Resolution
RG-119 establishes whether the response has been effective. The next layer determines whether the underlying governed condition has reached a valid resolution state.
```text
EXECUTION
↓
EFFECTIVENESS
↓
RESOLUTION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure regression response-effectiveness layer beneath response execution and above resolution, closure and reliance restoration. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Effectiveness Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → MANDATORY EFFECTIVENESS DETERMINATION → RESOLUTION → CLOSURE → REACCEPTANCE → RELIANCE RESTORATION → MONITORING CONTINUITY → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION DETERMINATION → AUTHORITY TRANSFER DETERMINATION → RESPONSE EXECUTION DETERMINATION → EFFECTIVENESS DETERMINATION → REOPENING
```

## Complete Effectiveness Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → REACCEPT → RESTORE RELIANCE → MAINTAIN MONITORING → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → ASSESS EFFECTIVENESS → RESOLVE / CONTINUE / REOPEN AS REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-120` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Response Resolution Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION RESPONSE TO HAVE AN EVIDENCE-BASED EFFECTIVENESS DETERMINATION THAT COMPARES THE ACTUAL POST-RESPONSE STATE WITH THE REQUIRED OUTCOME, ASSESSES RESIDUAL CONSEQUENCE, CONTROL RESTORATION AND SUSTAINABILITY, AND DISTINGUISHES EFFECTIVE, PARTIAL, INEFFECTIVE AND UNKNOWN STATES, SO THAT RESPONSE COMPLETION CANNOT BE MISTAKEN FOR SUCCESSFUL CONTROL.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-EFFECTIVENESS-DETERMINATION-01
