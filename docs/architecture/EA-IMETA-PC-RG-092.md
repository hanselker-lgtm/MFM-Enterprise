# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-EFFECTIVENESS-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-092`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-092` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-EFFECTIVENESS-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Effectiveness Determination |
| Parent | EA-IMETA-PC-RG-091 — Mandatory Post-Closure Response Execution and Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory effectiveness-determination layer that determines whether an executed post-closure response actually achieved its required objective and restored the governed condition to the required state, without confusing action completion with outcome achievement.

## Core Principle
Execution proves that an action occurred. Effectiveness proves that the action produced the required result. Effectiveness shall therefore be determined against explicit outcomes, criteria, evidence, residual deviation and applicable acceptance conditions.

```text
RESPONSE EXECUTED
      ↓
REQUIRED OUTCOME DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → CONTINUE MONITORING / REASSESS
└── YES
     ↓
OUTCOME ACHIEVED?
├── YES → EFFECTIVE
└── NO
     ↓
RESIDUAL DEVIATION?
├── NO → REASSESS CRITERIA / CONTEXT
└── YES → INEFFECTIVE / PARTIALLY EFFECTIVE
     ↓
RESPONSE CONTINUE / MODIFY / REOPEN / ESCALATE
```

## Effectiveness Quality Test
```text
EXECUTED RESPONSE
+
DEFINED REQUIRED OUTCOME
+
VALID SUCCESS CRITERIA
+
SUFFICIENT POST-ACTION EVIDENCE
+
COMPARISON AGAINST REQUIRED STATE
+
RESIDUAL DEVIATION ASSESSMENT
+
AUTHORIZED DETERMINATION
=
VALID GOVERNED EFFECTIVENESS DETERMINATION
```

## Completion vs Effectiveness
```text
EXECUTION COMPLETE
→ THE AUTHORIZED ACTION WAS PERFORMED

EFFECTIVE
→ THE REQUIRED OUTCOME WAS ACHIEVED

PARTIALLY EFFECTIVE
→ SOME REQUIRED OUTCOMES WERE ACHIEVED

INEFFECTIVE
→ THE REQUIRED OUTCOME WAS NOT ACHIEVED
```

## Effectiveness State Model
```text
PENDING
UNDER ASSESSMENT
EVIDENCE INSUFFICIENT
EFFECTIVE
PARTIALLY EFFECTIVE
INEFFECTIVE
UNKNOWN
REASSESSMENT REQUIRED
RESPONSE CONTINUES
REOPENED
ACCEPTED
```

## Effectiveness Invariants

```text
EFFECTIVENESS SHALL BE ASSESSED AGAINST EXPLICIT REQUIRED OUTCOMES
```

```text
EXECUTION COMPLETION SHALL NOT AUTOMATICALLY PRODUCE EFFECTIVENESS
```

```text
EVIDENCE SHALL BE SUFFICIENT FOR THE CONSEQUENCE LEVEL
```

```text
SUCCESS CRITERIA SHALL BE VERSIONED AND TRACEABLE
```

```text
RESIDUAL DEVIATION SHALL BE ASSESSED
```

```text
SECONDARY OR UNINTENDED EFFECTS SHALL BE CONSIDERED WHERE MATERIAL
```

```text
EFFECTIVENESS SHALL BE ATTRIBUTABLE TO AN AUTHORIZED DETERMINATION
```

```text
PARTIAL EFFECTIVENESS SHALL NOT BE REPRESENTED AS FULL EFFECTIVENESS
```

```text
UNKNOWN EFFECTIVENESS SHALL REMAIN UNKNOWN UNTIL SUFFICIENT EVIDENCE EXISTS
```

```text
INEFFECTIVE RESPONSE SHALL NOT BE CLOSED AS SUCCESSFUL
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE EFFECTIVENESS SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT RESPONSE EFFECTIVENESS SHALL CONSIDER BOTH OUTCOME AND CONTROLLED BEHAVIOUR
```

```text
EFFECTIVENESS SHALL CONSIDER SUSTAINABILITY WHERE A TEMPORARY RESULT IS INSUFFICIENT
```

```text
TIME-LAGGED EFFECTS SHALL BE CONSIDERED WHERE REQUIRED
```

```text
REASSESSMENT SHALL BE TRIGGERED WHEN NEW EVIDENCE INVALIDATES THE DETERMINATION
```

```text
EFFECTIVENESS DETERMINATION SHALL PRESERVE THE RESPONSE AND BASELINE HISTORY
```

## 1. Effectiveness Domain — Post-Closure Effectiveness Determination Governance

**Control family:** `PCEF-001`

The Post-Closure Effectiveness Determination Governance domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-001-01` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-02` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-03` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-04` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-05` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-06` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-001-07` — Establish and maintain the post-closure effectiveness determination governance control.
- `PCEF-001-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 2. Effectiveness Domain — Post-Closure Effectiveness Determination Objective

**Control family:** `PCEF-002`

The Post-Closure Effectiveness Determination Objective domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-002-01` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-02` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-03` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-04` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-05` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-06` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-002-07` — Establish and maintain the post-closure effectiveness determination objective control.
- `PCEF-002-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 3. Effectiveness Domain — Post-Closure Effectiveness Determination Definition

**Control family:** `PCEF-003`

The Post-Closure Effectiveness Determination Definition domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-003-01` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-02` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-03` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-04` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-05` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-06` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-003-07` — Establish and maintain the post-closure effectiveness determination definition control.
- `PCEF-003-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 4. Effectiveness Domain — Post-Closure Effectiveness Determination Scope

**Control family:** `PCEF-004`

The Post-Closure Effectiveness Determination Scope domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-004-01` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-02` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-03` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-04` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-05` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-06` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-004-07` — Establish and maintain the post-closure effectiveness determination scope control.
- `PCEF-004-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 5. Effectiveness Domain — Post-Closure Effectiveness Determination Authority

**Control family:** `PCEF-005`

The Post-Closure Effectiveness Determination Authority domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-005-01` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-02` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-03` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-04` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-05` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-06` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-005-07` — Establish and maintain the post-closure effectiveness determination authority control.
- `PCEF-005-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 6. Effectiveness Domain — Post-Closure Effectiveness Determination Criteria

**Control family:** `PCEF-006`

The Post-Closure Effectiveness Determination Criteria domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-006-01` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-02` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-03` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-04` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-05` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-06` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-006-07` — Establish and maintain the post-closure effectiveness determination criteria control.
- `PCEF-006-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 7. Effectiveness Domain — Post-Closure Effectiveness Determination Preconditions

**Control family:** `PCEF-007`

The Post-Closure Effectiveness Determination Preconditions domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-007-01` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-02` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-03` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-04` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-05` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-06` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-007-07` — Establish and maintain the post-closure effectiveness determination preconditions control.
- `PCEF-007-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 8. Effectiveness Domain — Post-Closure Effectiveness Determination Evidence

**Control family:** `PCEF-008`

The Post-Closure Effectiveness Determination Evidence domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-008-01` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-02` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-03` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-04` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-05` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-06` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-008-07` — Establish and maintain the post-closure effectiveness determination evidence control.
- `PCEF-008-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 9. Effectiveness Domain — Post-Closure Effectiveness Determination Method

**Control family:** `PCEF-009`

The Post-Closure Effectiveness Determination Method domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-009-01` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-02` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-03` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-04` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-05` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-06` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-009-07` — Establish and maintain the post-closure effectiveness determination method control.
- `PCEF-009-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 10. Effectiveness Domain — Post-Closure Effectiveness Determination Decision

**Control family:** `PCEF-010`

The Post-Closure Effectiveness Determination Decision domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-010-01` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-02` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-03` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-04` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-05` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-06` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-010-07` — Establish and maintain the post-closure effectiveness determination decision control.
- `PCEF-010-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 11. Effectiveness Domain — Post-Closure Effectiveness Determination Accountability

**Control family:** `PCEF-011`

The Post-Closure Effectiveness Determination Accountability domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-011-01` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-02` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-03` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-04` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-05` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-06` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-011-07` — Establish and maintain the post-closure effectiveness determination accountability control.
- `PCEF-011-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 12. Effectiveness Domain — Post-Closure Effectiveness Determination Timing

**Control family:** `PCEF-012`

The Post-Closure Effectiveness Determination Timing domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-012-01` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-02` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-03` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-04` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-05` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-06` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-012-07` — Establish and maintain the post-closure effectiveness determination timing control.
- `PCEF-012-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 13. Effectiveness Domain — Security Post-Closure Effectiveness Determination

**Control family:** `PCEF-013`

The Security Post-Closure Effectiveness Determination domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-013-01` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-02` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-03` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-04` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-05` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-06` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-013-07` — Establish and maintain the security post-closure effectiveness determination control.
- `PCEF-013-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 14. Effectiveness Domain — Resilience Post-Closure Effectiveness Determination

**Control family:** `PCEF-014`

The Resilience Post-Closure Effectiveness Determination domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-014-01` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-02` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-03` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-04` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-05` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-06` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-014-07` — Establish and maintain the resilience post-closure effectiveness determination control.
- `PCEF-014-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 15. Effectiveness Domain — Compliance Post-Closure Effectiveness Determination

**Control family:** `PCEF-015`

The Compliance Post-Closure Effectiveness Determination domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-015-01` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-02` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-03` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-04` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-05` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-06` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-015-07` — Establish and maintain the compliance post-closure effectiveness determination control.
- `PCEF-015-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 16. Effectiveness Domain — Data Post-Closure Effectiveness Determination

**Control family:** `PCEF-016`

The Data Post-Closure Effectiveness Determination domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-016-01` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-02` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-03` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-04` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-05` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-06` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-016-07` — Establish and maintain the data post-closure effectiveness determination control.
- `PCEF-016-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 17. Effectiveness Domain — AI and Agent Post-Closure Effectiveness Determination

**Control family:** `PCEF-017`

The AI and Agent Post-Closure Effectiveness Determination domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-017-01` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-02` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-03` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-04` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-05` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-06` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-017-07` — Establish and maintain the ai and agent post-closure effectiveness determination control.
- `PCEF-017-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 18. Effectiveness Domain — Post-Closure Effectiveness Determination Failure

**Control family:** `PCEF-018`

The Post-Closure Effectiveness Determination Failure domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-018-01` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-02` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-03` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-04` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-05` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-06` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-018-07` — Establish and maintain the post-closure effectiveness determination failure control.
- `PCEF-018-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 19. Effectiveness Domain — Post-Closure Effectiveness Determination Independence

**Control family:** `PCEF-019`

The Post-Closure Effectiveness Determination Independence domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-019-01` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-02` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-03` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-04` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-05` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-06` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-019-07` — Establish and maintain the post-closure effectiveness determination independence control.
- `PCEF-019-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## 20. Effectiveness Domain — Post-Closure Effectiveness Determination Review and Learning

**Control family:** `PCEF-020`

The Post-Closure Effectiveness Determination Review and Learning domain establishes governed mandatory effectiveness-determination requirements.

### Required controls
- `PCEF-020-01` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-01-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-02` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-02-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-03` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-03-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-04` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-04-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-05` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-05-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-06` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-06-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.
- `PCEF-020-07` — Establish and maintain the post-closure effectiveness determination review and learning control.
- `PCEF-020-07-E` — Preserve required outcome, criteria, evidence, comparison, residual deviation, determination, authority and reassessment traceability.

```text
EXECUTE → MEASURE → COMPARE → DETERMINE → REASSESS
```

## Post-Closure Effectiveness Determination Structure

| Element | Required definition |
|---|---|
| Response | Executed intervention |
| Objective | Required outcome |
| Criteria | Success conditions |
| Evidence | Post-action evidence |
| Comparison | Actual vs required state |
| Residual Deviation | Remaining gap |
| Determination | Effectiveness result |
| Authority | Authorized decision-maker |
| Reassessment | Future validation |

## Post-Closure Effectiveness Determination Objective

Determine whether the executed response achieved the required outcome and whether the condition is sufficiently restored to support the next governed lifecycle state.

## Post-Closure Effectiveness Determination Definition

Effectiveness determination is the evidence-based decision that an executed response achieved, partially achieved, failed to achieve or cannot yet be shown to have achieved the required outcome.

## Post-Closure Effectiveness Determination Scope

Scope shall include the response objective, affected state, success criteria, evidence period, residual conditions, dependencies and downstream consequences.

## Post-Closure Effectiveness Determination Authority

Authority shall define who may determine effectiveness, accept partial effectiveness, declare unknown status, require further action and authorize closure or reopening.

## Post-Closure Effectiveness Determination Criteria

Criteria shall define required outcomes, thresholds, tolerances, sustainability, time windows, residual deviation and unacceptable side effects.

```text
RESPONSE COMPLETE
↓
REQUIRED OUTCOME ACHIEVED?
├── YES → CHECK SUSTAINABILITY / SIDE EFFECTS
└── NO
     ↓
PARTIAL ACHIEVEMENT?
├── YES → PARTIALLY EFFECTIVE
└── NO → INEFFECTIVE
     ↓
RESIDUAL DEVIATION MATERIAL?
├── YES → CONTINUE / REOPEN / ESCALATE
└── NO → ACCEPT EFFECTIVENESS
```

## Post-Closure Effectiveness Determination Preconditions

Preconditions include completed or sufficiently observed response actions, defined outcome criteria, available evidence, comparison baseline and appropriate authority.

## Post-Closure Effectiveness Determination Evidence

Evidence shall preserve before-state, response actions, after-state, measurements, observations, criteria version, comparison, residual deviation and determination rationale.

## Post-Closure Effectiveness Determination Method

Methods may include before/after comparison, threshold testing, control verification, outcome measurement, trend analysis, sampling, independent validation and sustained observation.

```text
BEFORE STATE
↓
RESPONSE
↓
AFTER STATE
↓
COMPARE TO REQUIRED STATE
↓
ASSESS RESIDUAL DEVIATION
↓
DETERMINE EFFECTIVENESS
```

## Post-Closure Effectiveness Determination Decision

Decision shall explicitly state effective, partially effective, ineffective, unknown or reassessment required and identify the consequence for the response lifecycle.

```text
EFFECTIVENESS
├── EFFECTIVE → ACCEPT / CONTINUE MONITORING
├── PARTIAL → MODIFY / CONTINUE
├── INEFFECTIVE → REOPEN / ESCALATE
└── UNKNOWN → GATHER EVIDENCE / REASSESS
```

## Post-Closure Effectiveness Determination Accountability

Accountability shall remain explicit for the determination, evidence sufficiency, interpretation of criteria and resulting lifecycle decision.

## Post-Closure Effectiveness Determination Timing

Effectiveness shall be determined within a period appropriate to the response and the time required for the outcome to become observable. Temporary improvement shall not be treated as durable effectiveness where persistence matters.

## Security Post-Closure Effectiveness Determination

Security effectiveness shall consider whether exposure, vulnerability, unauthorized access or control degradation was actually reduced and remains controlled.

## Resilience Post-Closure Effectiveness Determination

Resilience effectiveness shall consider recovery, stability, capacity, continuity and dependency performance after response execution.

## Compliance Post-Closure Effectiveness Determination

Compliance effectiveness shall consider whether the applicable obligation and control condition is restored and supported by sufficient evidence.

## Data Post-Closure Effectiveness Determination

Data effectiveness shall consider integrity, quality, access, confidentiality, lineage, retention and authorized-use outcomes.

## AI and Agent Post-Closure Effectiveness Determination

AI/agent effectiveness shall consider both required outcome and whether the response remained within authority, policy, data, tool and autonomy boundaries.

```text
AI / AGENT RESPONSE
↓
OUTCOME ACHIEVED?
+
CONTROL BOUNDARIES RESPECTED?
↓
EFFECTIVENESS DETERMINATION
```

## Post-Closure Effectiveness Determination Failure

Failure includes insufficient evidence, ambiguous criteria, false positive effectiveness, temporary recovery mistaken for durable recovery, residual material deviation or conflicting measurements.

```text
DETERMINATION FAILURE
↓
SAFE TO ACCEPT?
├── YES → QUALIFIED ACCEPTANCE
└── NO → REASSESS / CONTINUE / ESCALATE
```

## Post-Closure Effectiveness Determination Independence

Independent validation may be required for high-consequence conditions, disputed results, conflicts of interest, irreversible effects or material acceptance decisions.

## Post-Closure Effectiveness Determination Review and Learning

Reviews shall identify ineffective responses, misleading criteria, evidence gaps, premature closure, recurring residual deviations and opportunities to improve response design.

## Effectiveness Determination Model
```text
RESPONSE EXECUTED
↓
OUTCOME CRITERIA VALID?
├── NO → GOVERNANCE GAP
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → GATHER / CONTINUE MONITORING
└── YES
     ↓
ACTUAL STATE MEETS REQUIRED STATE?
├── YES → CHECK DURABILITY + SIDE EFFECTS
└── NO
     ↓
PARTIAL ACHIEVEMENT?
├── YES → PARTIALLY EFFECTIVE
└── NO → INEFFECTIVE
     ↓
MATERIAL RESIDUAL DEVIATION?
├── YES → CONTINUE / REOPEN / ESCALATE
└── NO → ACCEPT EFFECTIVENESS
```

## Effectiveness Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Pending | Determination not complete | Continue assessment |
| Evidence Insufficient | Evidence cannot support decision | Gather evidence |
| Effective | Required outcome achieved | Accept / monitor |
| Partially Effective | Some required outcomes achieved | Modify / continue |
| Ineffective | Required outcome not achieved | Reopen / escalate |
| Unknown | Cannot yet determine | Monitor / reassess |
| Reassessment Required | New evidence changes basis | Reassess |
| Response Continues | Further action required | Continue response |
| Reopened | Closed state invalidated | Re-enter response lifecycle |
| Accepted | Effectiveness formally accepted | Proceed to next lifecycle state |

## Effectiveness Record
| Field | Required |
|---|---|
| Effectiveness ID | Yes |
| Condition ID | Yes |
| Response ID | Yes |
| Objective | Yes |
| Criteria Version | Yes |
| Evidence Period | Yes |
| Before State | Yes |
| After State | Yes |
| Comparison | Yes |
| Residual Deviation | Yes |
| Side Effects | Where material |
| Sustainability | Where relevant |
| Determination | Yes |
| Authority | Yes |
| Rationale | Yes |
| Reassessment Trigger | Where applicable |

## Required Outcome Integrity
The required outcome must be explicit enough to determine whether the response succeeded. Vague outcomes such as 'issue handled' are insufficient for material governance decisions.

## Criteria Versioning
The criteria used to determine effectiveness shall be identifiable and versioned so that later review can reconstruct why the result was accepted.

## Before / After Comparison
Effectiveness shall normally compare the relevant state before response with the resulting state after response and with the required target state.

```text
BEFORE STATE
↓
RESPONSE
↓
AFTER STATE
↓
REQUIRED STATE
↓
COMPARISON
```

## Residual Deviation
A response may be effective while a small immaterial residual deviation remains, but that residual condition shall be explicit and governed. A material residual deviation prevents full effectiveness.

## Partial Effectiveness
Partial effectiveness shall be treated as a distinct state and shall not be represented as full success.

## Temporary Effectiveness
If the condition temporarily improves and then returns, the initial determination may require reassessment and can become a regression signal.

## Sustainability
Where the required outcome must persist, effectiveness shall include an appropriate observation period rather than relying solely on immediate post-action measurements.

## Side Effects
Effectiveness shall consider whether the response introduced material secondary effects. A response that solves the original issue while creating a more severe condition shall not be accepted as fully effective.

## Unknown Effectiveness
Unknown is a valid governed state when evidence is insufficient. It shall not be converted to effective merely because no failure has yet been observed.

## False Positive Effectiveness
A determination shall be challenged where evidence shows measurement error, incomplete scope, incorrect baseline, misleading criteria or unobserved downstream consequences.

## Reassessment
New evidence may require the effectiveness determination to change. The original determination remains preserved as historical evidence.

```text
EFFECTIVE
↓
NEW MATERIAL EVIDENCE?
├── NO → CONTINUE
└── YES
     ↓
DETERMINATION STILL VALID?
├── YES → CONTINUE
└── NO → REASSESS / REOPEN
```

## AI and Agent Effectiveness
AI/agent responses require both outcome effectiveness and control effectiveness. A successful outcome achieved through unauthorized autonomy, prohibited tool use or policy violation shall not be treated as fully effective.

## Effectiveness Anti-Gaming
Effectiveness shall not be declared to close a case, improve performance metrics, avoid escalation or restore apparent compliance without evidence supporting the required outcome.

## Relationship to Resolution
Effectiveness determines whether the response achieved the required outcome. Resolution determines whether the underlying condition can proceed toward closure under the applicable lifecycle rules.

```text
EXECUTE
↓
DETERMINE EFFECTIVENESS
↓
EFFECTIVE?
├── YES → RESOLUTION / ACCEPTANCE PATH
└── NO → CONTINUE / MODIFY / REOPEN
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure effectiveness-determination layer beneath response execution and above resolution, closure and subsequent reliance restoration. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Effectiveness Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → ASSESSMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → MANDATORY EFFECTIVENESS DETERMINATION → RESOLUTION → CLOSURE → POST-CLOSURE TRANSITION → BASELINE → MONITORING → COMPARISON → DEVIATION DETECTION → REGRESSION → REOPENING
```

## Complete Effectiveness Chain
```text
BASELINE → OBSERVE → COMPARE → DETECT DEVIATION → VALIDATE → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → INITIATE RESPONSE → ESCALATE → TRANSFER AUTHORITY → EXECUTE → CONTROL → OBSERVE EFFECTS → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-093` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Resolution Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE RESPONSE TO BE JUDGED AGAINST EXPLICIT REQUIRED OUTCOMES, SUCCESS CRITERIA AND SUFFICIENT EVIDENCE, WITH RESIDUAL DEVIATION, SUSTAINABILITY, SIDE EFFECTS AND UNCERTAINTY CONSIDERED, SO THAT COMPLETION OF AN ACTION CANNOT BE MISTAKEN FOR EFFECTIVENESS AND INEFFECTIVE OR UNPROVEN RESPONSES CANNOT BE CLOSED AS SUCCESSFUL.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-EFFECTIVENESS-DETERMINATION-01
