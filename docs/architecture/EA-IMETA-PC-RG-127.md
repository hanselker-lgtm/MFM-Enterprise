# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-DEVIATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-127`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-127` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-DEVIATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Monitoring Deviation Determination |
| Parent | EA-IMETA-PC-RG-126 — Mandatory Post-Closure Monitoring Result Comparison Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory deviation-determination layer that decides whether a qualified and compared post-closure monitoring result constitutes a governed deviation from an approved baseline, target, tolerance, threshold or required state, while preserving a strict distinction between deviation and regression.

## Core Principle
A difference is an observation; a deviation is a governed determination that an approved requirement, tolerance, threshold or expected state has not been met. Deviation determination shall be evidence-based, context-aware, traceable and independent of the desired closure status.

```text
QUALIFIED + COMPARED RESULT
        ↓
REFERENCE / REQUIREMENT VALID?
├── NO → DEVIATION UNDETERMINED
└── YES
     ↓
DEVIATION CRITERIA MET?
├── NO → NO GOVERNED DEVIATION
└── YES
     ↓
MAGNITUDE / DURATION / PERSISTENCE
     ↓
MATERIALITY / CONSEQUENCE RELEVANCE
     ↓
DEVIATION STATE
├── MINOR / CONTROLLED
├── MATERIAL
├── CRITICAL
└── UNDETERMINED
     ↓
PASS TO REGRESSION / CONSEQUENCE DETERMINATION
```
## Deviation Quality Test
```text
VALIDATED RESULT
+
QUALIFIED RESULT
+
VALID COMPARISON
+
APPROVED REQUIREMENT / REFERENCE
+
EXPLICIT DEVIATION CRITERIA
+
TRACEABLE DIFFERENCE
+
MATERIALITY ASSESSMENT
+
AUTHORIZED DETERMINATION
=
VALID GOVERNED DEVIATION DETERMINATION
```
## Difference vs Deviation vs Regression
```text
DIFFERENCE
→ MEASURED / ASSESSED RELATIONSHIP

DEVIATION
→ GOVERNED FAILURE TO MEET AN APPROVED REQUIREMENT / TOLERANCE / THRESHOLD

REGRESSION
→ DETERIORATION FROM A PREVIOUSLY ACCEPTED OR RESOLVED STATE
```
## Deviation States
```text
D0 — DEVIATION NOT REQUIRED
D1 — DEVIATION PENDING
D2 — DEVIATION ASSESSMENT IN PROGRESS
D3 — NO DEVIATION
D4 — MINOR / CONTROLLED DEVIATION
D5 — MATERIAL DEVIATION
D6 — CRITICAL DEVIATION
D7 — PERSISTENT DEVIATION
D8 — RECURRENT DEVIATION
D9 — REGRESSION-INDICATING DEVIATION
DX — UNKNOWN / INSUFFICIENT BASIS
DR — REJECTED / REASSESSMENT REQUIRED
DS — SUSPENDED
```
## Deviation Dimensions
| Dimension | Required determination |
|---|---|
| Requirement | Applicable requirement |
| Reference | Approved state |
| Difference | Observed difference |
| Tolerance | Permitted variation |
| Threshold | Trigger boundary |
| Magnitude | Degree |
| Duration | Time span |
| Persistence | Sustained condition |
| Recurrence | Repeated condition |
| Materiality | Decision relevance |
| Consequence | Potential impact |
| Evidence | Supporting evidence |
| Authority | Determination authority |

## Deviation Invariants

```text
DEVIATION SHALL BE DETERMINED ONLY FROM VALIDATED, QUALIFIED AND COMPARABLE EVIDENCE
```

```text
A MEASURED DIFFERENCE SHALL NOT AUTOMATICALLY BECOME A DEVIATION
```

```text
DEVIATION CRITERIA SHALL BE EXPLICIT, APPROVED AND TRACEABLE
```

```text
TOLERANCE AND THRESHOLD SHALL RETAIN THEIR GOVERNED MEANING
```

```text
MATERIALITY SHALL BE ASSESSED WHERE CONSEQUENCE CAN CHANGE THE RESPONSE
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE APPROPRIATE
```

```text
DEVIATION SHALL REMAIN DISTINCT FROM REGRESSION DETERMINATION
```

```text
NO DEVIATION SHALL NOT BE USED AS EVIDENCE THAT FUTURE REGRESSION IS IMPOSSIBLE
```

```text
UNKNOWN SHALL NOT BE TREATED AS NO DEVIATION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE DEVIATIONS SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT DEVIATIONS SHALL CONSIDER BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT REQUIREMENTS
```

```text
DEVIATION DETERMINATION SHALL NOT BE BIASED TO PRESERVE CASE CLOSURE
```

```text
OVERRIDES SHALL BE EXPLICITLY AUTHORIZED AND TRACEABLE
```

```text
CONFLICTING EVIDENCE SHALL BE RESOLVED OR ESCALATED
```

```text
DEVIATION RECORDS SHALL PRESERVE BOTH THE OBSERVED RESULT AND THE GOVERNED DETERMINATION
```

```text
DEVIATION RULES SHALL BE REVIEWED AFTER FALSE POSITIVES, FALSE NEGATIVES OR SYSTEMATIC MISCLASSIFICATION
```

## 1. Deviation Domain — Post-Closure Monitoring Deviation Governance

**Control family:** `PCMD-001`

The Post-Closure Monitoring Deviation Governance domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-001-01` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-02` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-03` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-04` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-05` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-06` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-001-07` — Establish and maintain the post-closure monitoring deviation governance control.
- `PCMD-001-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 2. Deviation Domain — Post-Closure Monitoring Deviation Objective

**Control family:** `PCMD-002`

The Post-Closure Monitoring Deviation Objective domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-002-01` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-02` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-03` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-04` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-05` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-06` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-002-07` — Establish and maintain the post-closure monitoring deviation objective control.
- `PCMD-002-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 3. Deviation Domain — Post-Closure Monitoring Deviation Definition

**Control family:** `PCMD-003`

The Post-Closure Monitoring Deviation Definition domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-003-01` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-02` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-03` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-04` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-05` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-06` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-003-07` — Establish and maintain the post-closure monitoring deviation definition control.
- `PCMD-003-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 4. Deviation Domain — Post-Closure Monitoring Deviation Scope

**Control family:** `PCMD-004`

The Post-Closure Monitoring Deviation Scope domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-004-01` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-02` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-03` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-04` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-05` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-06` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-004-07` — Establish and maintain the post-closure monitoring deviation scope control.
- `PCMD-004-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 5. Deviation Domain — Post-Closure Monitoring Deviation Authority

**Control family:** `PCMD-005`

The Post-Closure Monitoring Deviation Authority domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-005-01` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-02` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-03` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-04` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-05` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-06` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-005-07` — Establish and maintain the post-closure monitoring deviation authority control.
- `PCMD-005-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 6. Deviation Domain — Post-Closure Monitoring Deviation Criteria

**Control family:** `PCMD-006`

The Post-Closure Monitoring Deviation Criteria domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-006-01` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-02` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-03` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-04` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-05` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-06` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-006-07` — Establish and maintain the post-closure monitoring deviation criteria control.
- `PCMD-006-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 7. Deviation Domain — Post-Closure Monitoring Deviation Preconditions

**Control family:** `PCMD-007`

The Post-Closure Monitoring Deviation Preconditions domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-007-01` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-02` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-03` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-04` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-05` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-06` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-007-07` — Establish and maintain the post-closure monitoring deviation preconditions control.
- `PCMD-007-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 8. Deviation Domain — Post-Closure Monitoring Deviation Evidence

**Control family:** `PCMD-008`

The Post-Closure Monitoring Deviation Evidence domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-008-01` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-02` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-03` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-04` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-05` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-06` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-008-07` — Establish and maintain the post-closure monitoring deviation evidence control.
- `PCMD-008-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 9. Deviation Domain — Post-Closure Monitoring Deviation Method

**Control family:** `PCMD-009`

The Post-Closure Monitoring Deviation Method domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-009-01` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-02` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-03` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-04` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-05` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-06` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-009-07` — Establish and maintain the post-closure monitoring deviation method control.
- `PCMD-009-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 10. Deviation Domain — Post-Closure Monitoring Deviation Decision

**Control family:** `PCMD-010`

The Post-Closure Monitoring Deviation Decision domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-010-01` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-02` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-03` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-04` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-05` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-06` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-010-07` — Establish and maintain the post-closure monitoring deviation decision control.
- `PCMD-010-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 11. Deviation Domain — Post-Closure Monitoring Deviation Accountability

**Control family:** `PCMD-011`

The Post-Closure Monitoring Deviation Accountability domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-011-01` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-02` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-03` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-04` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-05` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-06` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-011-07` — Establish and maintain the post-closure monitoring deviation accountability control.
- `PCMD-011-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 12. Deviation Domain — Post-Closure Monitoring Deviation Timing

**Control family:** `PCMD-012`

The Post-Closure Monitoring Deviation Timing domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-012-01` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-02` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-03` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-04` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-05` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-06` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-012-07` — Establish and maintain the post-closure monitoring deviation timing control.
- `PCMD-012-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 13. Deviation Domain — Security Post-Closure Monitoring Deviation

**Control family:** `PCMD-013`

The Security Post-Closure Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-013-01` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-02` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-03` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-04` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-05` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-06` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-013-07` — Establish and maintain the security post-closure monitoring deviation control.
- `PCMD-013-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 14. Deviation Domain — Resilience Post-Closure Monitoring Deviation

**Control family:** `PCMD-014`

The Resilience Post-Closure Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-014-01` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-02` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-03` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-04` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-05` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-06` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-014-07` — Establish and maintain the resilience post-closure monitoring deviation control.
- `PCMD-014-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 15. Deviation Domain — Compliance Post-Closure Monitoring Deviation

**Control family:** `PCMD-015`

The Compliance Post-Closure Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-015-01` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-02` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-03` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-04` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-05` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-06` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-015-07` — Establish and maintain the compliance post-closure monitoring deviation control.
- `PCMD-015-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 16. Deviation Domain — Data Post-Closure Monitoring Deviation

**Control family:** `PCMD-016`

The Data Post-Closure Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-016-01` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-02` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-03` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-04` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-05` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-06` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-016-07` — Establish and maintain the data post-closure monitoring deviation control.
- `PCMD-016-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 17. Deviation Domain — AI and Agent Post-Closure Monitoring Deviation

**Control family:** `PCMD-017`

The AI and Agent Post-Closure Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-017-01` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-02` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-03` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-04` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-05` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-06` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-017-07` — Establish and maintain the ai and agent post-closure monitoring deviation control.
- `PCMD-017-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 18. Deviation Domain — Post-Closure Monitoring Deviation Failure

**Control family:** `PCMD-018`

The Post-Closure Monitoring Deviation Failure domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-018-01` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-02` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-03` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-04` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-05` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-06` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-018-07` — Establish and maintain the post-closure monitoring deviation failure control.
- `PCMD-018-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 19. Deviation Domain — Post-Closure Monitoring Deviation Independence

**Control family:** `PCMD-019`

The Post-Closure Monitoring Deviation Independence domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-019-01` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-02` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-03` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-04` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-05` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-06` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-019-07` — Establish and maintain the post-closure monitoring deviation independence control.
- `PCMD-019-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## 20. Deviation Domain — Post-Closure Monitoring Deviation Review and Learning

**Control family:** `PCMD-020`

The Post-Closure Monitoring Deviation Review and Learning domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCMD-020-01` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-01-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-02` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-02-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-03` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-03-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-04` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-04-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-05` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-05-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-06` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-06-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.
- `PCMD-020-07` — Establish and maintain the post-closure monitoring deviation review and learning control.
- `PCMD-020-07-E` — Preserve requirement, reference, difference, tolerance, threshold, magnitude, duration, persistence, recurrence, materiality, consequence, evidence and authority traceability.

```text
COMPARE → APPLY CRITERIA → ASSESS MATERIALITY → DETERMINE DEVIATION → ESCALATE IF REQUIRED
```

## Post-Closure Monitoring Deviation Structure

| Element | Required definition |
|---|---|
| Requirement | Applicable requirement |
| Reference | Approved state |
| Difference | Observed difference |
| Tolerance | Permitted variation |
| Threshold | Trigger boundary |
| Magnitude | Degree of difference |
| Duration | Time span |
| Persistence | Sustained condition |
| Recurrence | Repeated condition |
| Materiality | Decision relevance |
| Consequence | Potential impact |

## Post-Closure Monitoring Deviation Objective

Determine whether the compared monitoring condition constitutes a governed failure to meet an approved requirement, tolerance, threshold or required state.

## Post-Closure Monitoring Deviation Definition

Deviation determination is the explicit governed decision that a valid observed condition falls outside an applicable approved requirement or permitted boundary.

## Post-Closure Monitoring Deviation Scope

Scope includes threshold breaches, tolerance exceedances, control failures, requirement breaches, sustained deterioration and recurrent non-conformance indicated by post-closure monitoring.

## Post-Closure Monitoring Deviation Authority

Authority shall define who may determine, reject, override, escalate or independently review a deviation.

## Post-Closure Monitoring Deviation Criteria

Criteria shall define requirement, reference, tolerance, threshold, magnitude, duration, persistence, recurrence and materiality.
```text
COMPARED RESULT
↓
CRITERIA MET?
├── NO → NO GOVERNED DEVIATION
└── YES
     ↓
MAGNITUDE / DURATION / PERSISTENCE
     ↓
MATERIALITY
├── MINOR / CONTROLLED
├── MATERIAL
└── CRITICAL
     ↓
REGRESSION / CONSEQUENCE DETERMINATION
```

## Post-Closure Monitoring Deviation Preconditions

Preconditions include validated result, qualification, valid comparison, approved requirement/reference and applicable deviation criteria.

## Post-Closure Monitoring Deviation Evidence

Evidence shall preserve result, reference, requirement, rule, difference, threshold/tolerance status, materiality assessment, authority and decision.

## Post-Closure Monitoring Deviation Method

Methods may include rule evaluation, threshold assessment, tolerance evaluation, duration analysis, recurrence analysis, trend analysis and expert review.
```text
RESULT → COMPARE → APPLY REQUIREMENT → ASSESS DIFFERENCE → ASSESS MATERIALITY → DETERMINE DEVIATION
```

## Post-Closure Monitoring Deviation Decision

Decision shall determine D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, DX, DR or DS and the associated next action.

## Post-Closure Monitoring Deviation Accountability

Accountability shall remain explicit for criteria, determination quality, overrides, disputed findings and escalation.

## Post-Closure Monitoring Deviation Timing

Deviation determination shall occur before material consequence, alert or response decisions unless a controlled provisional path is authorized.

## Security Post-Closure Monitoring Deviation

Security deviation shall consider access, exposure, control failure, attack-path and security-state requirements.

## Resilience Post-Closure Monitoring Deviation

Resilience deviation shall consider availability, capacity, redundancy, recovery and fallback requirements.

## Compliance Post-Closure Monitoring Deviation

Compliance deviation shall consider applicable obligations, control requirements, reporting periods and evidence sufficiency.

## Data Post-Closure Monitoring Deviation

Data deviation shall consider integrity, quality, lineage, availability, confidentiality and downstream reliance requirements.

## AI and Agent Post-Closure Monitoring Deviation

AI/agent deviation shall consider behavior, authority boundaries, tool use, data handling, autonomy and oversight requirements.
```text
AI / AGENT RESULT
↓
REQUIREMENT / BASELINE
↓
COMPARE
↓
DEVIATION?
↓
REGRESSION / CONSEQUENCE PATH
```

## Post-Closure Monitoring Deviation Failure

Failure includes insufficient evidence, invalid criteria, reference mismatch, conflicting evidence, incorrect materiality or inability to determine deviation reliably.
```text
DEVIATION ASSESSMENT FAILURE
↓
MATERIAL DECISION AFFECTED?
├── YES → REASSESS / INDEPENDENT REVIEW / ESCALATE
└── NO → CORRECT / RECORD
```

## Post-Closure Monitoring Deviation Independence

Independent determination may be required where deviation materially affects reopening, safety, security, compliance, reliance restoration or high-consequence response.

## Post-Closure Monitoring Deviation Review and Learning

Reviews shall examine false positives, false negatives, threshold bias, tolerance drift, requirement ambiguity, evidence gaps and repeated deviation misclassification.

## Deviation Decision Model
```text
COMPARED RESULT
↓
REQUIREMENT VALID?
├── NO → DEVIATION UNDETERMINED
└── YES
     ↓
CRITERIA APPLICABLE?
├── NO → REASSESS / ESCALATE
└── YES
     ↓
TOLERANCE / THRESHOLD BREACHED?
├── NO → NO DEVIATION
└── YES
     ↓
MAGNITUDE / DURATION / PERSISTENCE
     ↓
MATERIALITY / CONSEQUENCE RELEVANCE
     ↓
DEVIATION STATE
├── MINOR / CONTROLLED
├── MATERIAL
├── CRITICAL
├── PERSISTENT
├── RECURRENT
└── REGRESSION-INDICATING
```

## Deviation Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| D0 | Not required | Record basis |
| D1 | Pending | Assess |
| D2 | Assessment in progress | Complete determination |
| D3 | No deviation | Continue monitoring |
| D4 | Minor / controlled | Correct / observe |
| D5 | Material | Escalate / govern |
| D6 | Critical | Immediate governed response |
| D7 | Persistent | Investigate / escalate |
| D8 | Recurrent | Assess systemic issue |
| D9 | Regression-indicating | Enter regression determination |
| DX | Unknown / insufficient | Do not treat as no deviation |
| DR | Rejected / reassessment required | Correct / review |
| DS | Suspended | Restore determination |

## Deviation Record
| Field | Required |
|---|---|
| Deviation ID | Yes |
| Comparison ID | Yes |
| Requirement | Yes |
| Reference | Yes |
| Result | Yes |
| Difference | Yes |
| Tolerance | Where applicable |
| Threshold | Where applicable |
| Magnitude | Yes |
| Duration | Where applicable |
| Persistence | Where applicable |
| Recurrence | Where applicable |
| Materiality | Yes where applicable |
| Consequence Relevance | Yes where applicable |
| Deviation State | Yes |
| Authority | Yes |
| Evidence | Yes |

## Difference Is Not Deviation
A difference becomes a deviation only when the approved deviation criteria are met.
```text
DIFFERENCE
↓
CRITERIA
↓
DEVIATION
```

## Deviation Is Not Regression
A deviation can exist without being a regression. Regression requires deterioration from the relevant previously accepted or resolved state.
```text
DEVIATION
≠
REGRESSION
```

## No Deviation Is Not Zero Risk
A determination of no deviation means the approved criteria are not currently met; it does not eliminate future regression risk.
```text
NO DEVIATION
≠
ZERO FUTURE RISK
```

## Unknown Deviation
Insufficient evidence shall result in unknown/undetermined handling rather than an automatic no-deviation conclusion.
```text
UNKNOWN
≠
NO DEVIATION
```

## Materiality
Materiality shall consider consequence, scope, duration, recurrence, exposure, control dependency and downstream reliance where relevant.

## Persistence and Recurrence
Persistent or recurrent deviations shall receive explicit treatment because repeated minor deviations may indicate a material systemic condition.

## Threshold and Tolerance Governance
Threshold and tolerance values shall be version-controlled, approved and linked to the intended governance action.

## Regression-Indicating Deviation
D9 indicates that deviation evidence may represent deterioration from a previously accepted or resolved state. Final regression determination remains a separate governed decision.

## AI and Agent Deviation
AI/agent deviations shall consider whether the observed behavior violates approved authority, tool, data, safety or oversight constraints.

## Relationship to Regression Determination
RG-127 supplies governed deviation outcomes to the subsequent regression-determination layer.
```text
VALIDATION → QUALIFICATION → COMPARISON → DEVIATION → REGRESSION DETERMINATION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure monitoring deviation-determination layer beneath result comparison and above regression, consequence and response determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, result qualification, result validation, monitoring execution, monitoring activation, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Deviation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → MANDATORY DEVIATION DETERMINATION → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Deviation Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → ASSESS PERSISTENCE / RECURRENCE → DETERMINE REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-128` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE MONITORING DIFFERENCE TO BE ASSESSED AGAINST AN APPROVED REQUIREMENT, TOLERANCE, THRESHOLD OR REQUIRED STATE BEFORE IT IS DETERMINED TO BE A GOVERNED DEVIATION, WITH MAGNITUDE, DURATION, PERSISTENCE, RECURRENCE, MATERIALITY AND CONSEQUENCE RELEVANCE EXPLICITLY CONSIDERED, AND WITH DEVIATION KEPT DISTINCT FROM REGRESSION SO THAT NO SINGLE COMPARISON CAN SILENTLY BECOME A REGRESSION OR REOPENING DECISION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-DEVIATION-DETERMINATION-01
