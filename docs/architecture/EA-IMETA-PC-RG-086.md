# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETECTION-01

## Physical File ID
`EA-IMETA-PC-RG-086`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-086` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETECTION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Comparison and Deviation Detection |
| Parent | EA-IMETA-PC-RG-085 — Mandatory Post-Closure Measurement and Observation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory comparison and deviation-detection layer that evaluates valid post-closure observations against the accepted baseline, identifies material departures from the governed reference state, preserves interpretation context and provides a controlled input to classification, alerting and regression determination.

## Core Principle
A deviation is not automatically a regression. Comparison shall determine whether the current observed state differs from the governed baseline, while deviation detection shall determine whether that difference is genuine, material, explainable and relevant enough to enter the next governance stage.

```text
VALID OBSERVATION
      ↓
SELECT APPLICABLE BASELINE
      ↓
NORMALIZE / ALIGN CONTEXT
      ↓
COMPARE CURRENT STATE WITH BASELINE
      ↓
DEVIATION DETECTED?
├── NO → CONTINUE MONITORING
└── YES
     ↓
VALIDATE DEVIATION
     ↓
MATERIAL / RELEVANT?
├── NO → RECORD / CONTINUE
└── YES → CLASSIFY / ALERT / REGRESSION ASSESSMENT
```

## Comparison Quality Test
```text
VALID CURRENT OBSERVATION
+
VALID BASELINE
+
COMPATIBLE SCOPE
+
CONSISTENT MEASUREMENT SEMANTICS
+
CONTEXT ALIGNMENT
+
DEFINED COMPARISON METHOD
+
DEFINED DEVIATION RULES
+
TRACEABLE RESULT
=
VALID GOVERNED COMPARISON
```

## Comparison vs Deviation vs Regression
```text
COMPARISON
→ WHAT DIFFERENCE EXISTS BETWEEN CURRENT STATE AND BASELINE?

DEVIATION
→ IS THERE A MATERIAL OR RELEVANT DIFFERENCE?

REGRESSION
→ HAS THE GOVERNED POST-CLOSURE STATE DEGRADED IN A WAY THAT REQUIRES GOVERNED RESPONSE?
```

## Deviation State Model
```text
NO DEVIATION
POTENTIAL DEVIATION
DEVIATION DETECTED
DEVIATION VALIDATED
DEVIATION EXPLAINED
DEVIATION IMMATERIAL
DEVIATION MATERIAL
DEVIATION PERSISTENT
DEVIATION RECURRENT
REGRESSION SUSPECTED
REGRESSION CONFIRMED
```

## Comparison and Deviation Invariants

```text
COMPARISON SHALL USE THE APPLICABLE ACCEPTED BASELINE
```

```text
CURRENT OBSERVATION AND BASELINE SHALL HAVE COMPATIBLE SEMANTICS
```

```text
CONTEXT DIFFERENCES SHALL BE CONSIDERED WHERE MATERIAL
```

```text
DEVIATION RULES SHALL BE EXPLICIT
```

```text
NORMAL VARIATION SHALL NOT AUTOMATICALLY BECOME REGRESSION
```

```text
MATERIAL DEVIATIONS SHALL NOT BE SUPPRESSED
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE RELEVANT
```

```text
MISSING DATA SHALL NOT BE TREATED AS ZERO DEVIATION
```

```text
BASELINE CHANGES SHALL NOT RETROACTIVELY ERASE HISTORICAL DEVIATIONS
```

```text
COMPARISON RESULTS SHALL BE TRACEABLE TO SOURCE OBSERVATIONS AND BASELINE VERSION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE DEVIATIONS SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT DEVIATIONS SHALL CONSIDER AUTHORITY, POLICY, DATA, TOOL, AUTONOMY AND BEHAVIOURAL CHANGES
```

```text
EXPLAINABLE DEVIATIONS SHALL STILL BE RECORDED WHERE MATERIAL TO TREND OR GOVERNANCE
```

```text
OUTLIERS SHALL BE INVESTIGATED BEFORE EXCLUSION
```

```text
COMPARISON LOGIC SHALL BE VERSIONED
```

```text
DEVIATION DETECTION SHALL REMAIN INDEPENDENT OF DESIRED OUTCOMES
```

## 1. Comparison Domain — Post-Closure Comparison Deviation Governance

**Control family:** `PCDV-001`

The Post-Closure Comparison Deviation Governance domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-001-01` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-02` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-03` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-04` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-05` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-06` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-001-07` — Establish and maintain the post-closure comparison deviation governance control.
- `PCDV-001-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 2. Comparison Domain — Post-Closure Comparison Deviation Objective

**Control family:** `PCDV-002`

The Post-Closure Comparison Deviation Objective domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-002-01` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-02` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-03` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-04` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-05` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-06` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-002-07` — Establish and maintain the post-closure comparison deviation objective control.
- `PCDV-002-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 3. Comparison Domain — Post-Closure Comparison Deviation Definition

**Control family:** `PCDV-003`

The Post-Closure Comparison Deviation Definition domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-003-01` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-02` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-03` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-04` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-05` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-06` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-003-07` — Establish and maintain the post-closure comparison deviation definition control.
- `PCDV-003-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 4. Comparison Domain — Post-Closure Comparison Deviation Scope

**Control family:** `PCDV-004`

The Post-Closure Comparison Deviation Scope domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-004-01` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-02` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-03` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-04` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-05` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-06` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-004-07` — Establish and maintain the post-closure comparison deviation scope control.
- `PCDV-004-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 5. Comparison Domain — Post-Closure Comparison Deviation Authority

**Control family:** `PCDV-005`

The Post-Closure Comparison Deviation Authority domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-005-01` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-02` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-03` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-04` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-05` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-06` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-005-07` — Establish and maintain the post-closure comparison deviation authority control.
- `PCDV-005-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 6. Comparison Domain — Post-Closure Comparison Deviation Criteria

**Control family:** `PCDV-006`

The Post-Closure Comparison Deviation Criteria domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-006-01` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-02` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-03` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-04` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-05` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-06` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-006-07` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCDV-006-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 7. Comparison Domain — Post-Closure Comparison Deviation Preconditions

**Control family:** `PCDV-007`

The Post-Closure Comparison Deviation Preconditions domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-007-01` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-02` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-03` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-04` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-05` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-06` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-007-07` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCDV-007-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 8. Comparison Domain — Post-Closure Comparison Deviation Evidence

**Control family:** `PCDV-008`

The Post-Closure Comparison Deviation Evidence domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-008-01` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-02` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-03` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-04` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-05` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-06` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-008-07` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCDV-008-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 9. Comparison Domain — Post-Closure Comparison Deviation Method

**Control family:** `PCDV-009`

The Post-Closure Comparison Deviation Method domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-009-01` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-02` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-03` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-04` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-05` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-06` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-009-07` — Establish and maintain the post-closure comparison deviation method control.
- `PCDV-009-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 10. Comparison Domain — Post-Closure Comparison Deviation Decision

**Control family:** `PCDV-010`

The Post-Closure Comparison Deviation Decision domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-010-01` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-02` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-03` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-04` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-05` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-06` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-010-07` — Establish and maintain the post-closure comparison deviation decision control.
- `PCDV-010-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 11. Comparison Domain — Post-Closure Comparison Deviation Accountability

**Control family:** `PCDV-011`

The Post-Closure Comparison Deviation Accountability domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-011-01` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-02` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-03` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-04` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-05` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-06` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-011-07` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCDV-011-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 12. Comparison Domain — Post-Closure Comparison Deviation Timing

**Control family:** `PCDV-012`

The Post-Closure Comparison Deviation Timing domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-012-01` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-02` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-03` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-04` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-05` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-06` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-012-07` — Establish and maintain the post-closure comparison deviation timing control.
- `PCDV-012-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 13. Comparison Domain — Security Post-Closure Comparison Deviation

**Control family:** `PCDV-013`

The Security Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-013-01` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-02` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-03` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-04` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-05` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-06` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-013-07` — Establish and maintain the security post-closure comparison deviation control.
- `PCDV-013-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 14. Comparison Domain — Resilience Post-Closure Comparison Deviation

**Control family:** `PCDV-014`

The Resilience Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-014-01` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-02` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-03` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-04` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-05` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-06` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-014-07` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCDV-014-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 15. Comparison Domain — Compliance Post-Closure Comparison Deviation

**Control family:** `PCDV-015`

The Compliance Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-015-01` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-02` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-03` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-04` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-05` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-06` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-015-07` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCDV-015-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 16. Comparison Domain — Data Post-Closure Comparison Deviation

**Control family:** `PCDV-016`

The Data Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-016-01` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-02` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-03` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-04` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-05` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-06` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-016-07` — Establish and maintain the data post-closure comparison deviation control.
- `PCDV-016-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 17. Comparison Domain — AI and Agent Post-Closure Comparison Deviation

**Control family:** `PCDV-017`

The AI and Agent Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-017-01` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-02` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-03` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-04` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-05` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-06` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-017-07` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCDV-017-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 18. Comparison Domain — Post-Closure Comparison Deviation Failure

**Control family:** `PCDV-018`

The Post-Closure Comparison Deviation Failure domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-018-01` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-02` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-03` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-04` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-05` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-06` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-018-07` — Establish and maintain the post-closure comparison deviation failure control.
- `PCDV-018-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 19. Comparison Domain — Post-Closure Comparison Deviation Independence

**Control family:** `PCDV-019`

The Post-Closure Comparison Deviation Independence domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-019-01` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-02` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-03` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-04` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-05` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-06` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-019-07` — Establish and maintain the post-closure comparison deviation independence control.
- `PCDV-019-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## 20. Comparison Domain — Post-Closure Comparison Deviation Review and Learning

**Control family:** `PCDV-020`

The Post-Closure Comparison Deviation Review and Learning domain establishes governed mandatory comparison and deviation-detection requirements.

### Required controls
- `PCDV-020-01` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-01-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-02` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-02-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-03` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-03-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-04` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-04-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-05` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-05-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-06` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-06-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.
- `PCDV-020-07` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCDV-020-07-E` — Preserve baseline version, observation, comparison method, context, result, deviation status, validation and decision traceability.

```text
OBSERVE → ALIGN → COMPARE → VALIDATE → DETECT → CLASSIFY
```

## Post-Closure Comparison Deviation Structure

| Element | Required definition |
|---|---|
| Current Observation | Valid observed state |
| Baseline | Accepted reference state |
| Context | Conditions affecting comparison |
| Method | Comparison logic |
| Difference | Calculated or assessed change |
| Deviation Rule | Materiality / significance rule |
| Validation | Confirmation of deviation |
| Outcome | No deviation / deviation / regression input |

## Post-Closure Comparison Deviation Objective

Identify meaningful changes from the accepted post-closure reference state early enough to support classification, alerting and governed response.

## Post-Closure Comparison Deviation Definition

Comparison is the governed evaluation of current observation against baseline. Deviation detection is the governed identification and validation of a relevant difference requiring further interpretation.

## Post-Closure Comparison Deviation Scope

Scope shall identify the systems, services, users, data, decisions, dependencies, environments, measures and boundaries included in comparison.

## Post-Closure Comparison Deviation Authority

Authority shall define ownership of comparison logic, deviation thresholds, exception handling, validation and changes to detection rules.

## Post-Closure Comparison Deviation Criteria

Criteria shall define comparison method, tolerance, materiality, persistence, recurrence, context sensitivity and required validation.

```text
CURRENT OBSERVATION
↓
BASELINE COMPATIBLE?
├── NO → ALIGN / QUALIFY / STOP
└── YES
     ↓
DIFFERENCE PRESENT?
├── NO → NO DEVIATION
└── YES
     ↓
WITHIN TOLERANCE?
├── YES → NORMAL / IMMATERIAL VARIATION
└── NO → VALIDATE DEVIATION
```

## Post-Closure Comparison Deviation Preconditions

Preconditions include valid baseline, valid current observation, compatible measurement semantics, defined comparison logic and available context.

## Post-Closure Comparison Deviation Evidence

Evidence shall preserve both source states, baseline version, observation timestamp, comparison logic, calculations, context, result and validation.

## Post-Closure Comparison Deviation Method

Methods may include threshold comparison, range comparison, trend comparison, rate-of-change analysis, pattern comparison, control-state comparison and multi-dimensional comparison.

```text
BASELINE + CURRENT STATE
↓
ALIGN
↓
COMPARE
↓
APPLY TOLERANCE / RULE
↓
VALIDATE
↓
DEVIATION RESULT
```

## Post-Closure Comparison Deviation Decision

Decision shall classify the result as no deviation, potential deviation, validated deviation, explained, immaterial, material, persistent, recurrent or regression input.

```text
DEVIATION
├── EXPLAINED + IMMATERIAL → RECORD / CONTINUE
├── MATERIAL → CLASSIFY / ALERT
├── PERSISTENT → ESCALATE ANALYSIS
└── RECURRENT → REGRESSION ASSESSMENT
```

## Post-Closure Comparison Deviation Accountability

Accountability shall remain explicit for comparison quality, rule maintenance, deviation validation and escalation into the next governance layer.

## Post-Closure Comparison Deviation Timing

Comparison timing shall reflect volatility, materiality, time-to-impact and required sensitivity. Delayed comparison shall be detectable where it creates governance risk.

## Security Post-Closure Comparison Deviation

Security comparison shall detect material changes in access, exposure, configuration, control effectiveness, detection coverage and threat-relevant conditions.

## Resilience Post-Closure Comparison Deviation

Resilience comparison shall detect material changes in availability, recovery, capacity, continuity, dependencies and stability.

## Compliance Post-Closure Comparison Deviation

Compliance comparison shall detect material changes in obligations, controls, evidence, reporting and exception state.

## Data Post-Closure Comparison Deviation

Data comparison shall detect material changes in integrity, quality, access, lineage, retention, authorized use and downstream dependencies.

## AI and Agent Post-Closure Comparison Deviation

AI/agent comparison shall detect material changes in authority, policy, data access, tool usage, autonomy, configuration, behaviour and outcomes.

```text
BASELINE AI / AGENT STATE
+
CURRENT AI / AGENT OBSERVATION
↓
COMPARE AUTHORITY + POLICY + DATA + TOOLS
+
AUTONOMY + CONFIGURATION + BEHAVIOUR + OUTCOMES
↓
DEVIATION
↓
REGRESSION ASSESSMENT
```

## Post-Closure Comparison Deviation Failure

Failure includes incompatible baseline, invalid observation, changed semantics, missing context, broken comparison logic, suppressed deviations or inability to reproduce a result.

```text
COMPARISON FAILURE
↓
CAN DIFFERENCE BE RELIABLY DETERMINED?
├── YES → CONTINUE WITH QUALIFICATION
└── NO → GOVERNANCE GAP / ESCALATE
```

## Post-Closure Comparison Deviation Independence

Independent validation may be required where comparison results materially affect closure, risk acceptance, regulatory status or operational decisions.

## Post-Closure Comparison Deviation Review and Learning

Reviews shall identify false positives, false negatives, threshold weaknesses, baseline drift, context errors, missed persistent deviations and recurring regression patterns.

## Comparison and Deviation Determination Model
```text
VALID OBSERVATION
↓
VALID BASELINE?
├── NO → STOP / CORRECT BASELINE
└── YES
     ↓
SEMANTICS COMPATIBLE?
├── NO → ALIGN / VERSION / QUALIFY
└── YES
     ↓
CONTEXT COMPATIBLE?
├── NO → CONTEXTUALIZE
└── YES
     ↓
COMPARE
↓
DIFFERENCE PRESENT?
├── NO → NO DEVIATION
└── YES
     ↓
WITHIN ACCEPTED VARIATION?
├── YES → IMMATERIAL / NORMAL VARIATION
└── NO
     ↓
VALIDATE
↓
MATERIAL / PERSISTENT / RECURRENT?
├── NO → RECORD / CONTINUE
└── YES → CLASSIFY / ALERT / REGRESSION ASSESSMENT
```

## Deviation Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| No Deviation | Current state consistent with baseline | Continue monitoring |
| Potential Deviation | Difference detected but not validated | Investigate |
| Explained Deviation | Difference has valid context | Record / assess materiality |
| Immaterial Deviation | Difference within governed tolerance | Continue / trend |
| Material Deviation | Relevant difference beyond criteria | Classify / alert |
| Persistent Deviation | Difference remains over required period | Escalate analysis |
| Recurrent Deviation | Difference repeatedly returns | Assess systemic regression |
| Regression Suspected | Material degradation may exist | Enter regression assessment |
| Regression Confirmed | Governed state has materially degraded | Initiate response lifecycle |

## Comparison Record
| Field | Required |
|---|---|
| Comparison ID | Yes |
| Baseline ID / Version | Yes |
| Observation ID | Yes |
| Comparison Method Version | Yes |
| Context | Yes where material |
| Difference | Yes |
| Tolerance / Criteria | Yes |
| Validation Status | Yes |
| Deviation Status | Yes |
| Materiality | Where applicable |
| Persistence / Recurrence | Where applicable |
| Decision | Yes |

## Context Alignment
Comparison shall account for legitimate context differences such as workload, operating mode, maintenance, environment, configuration, user population or dependency state where those differences affect interpretation.

## Normal Variation
Normal variation shall be explicitly characterized where possible. The existence of variation does not remove the obligation to detect material changes outside the governed range.

## Persistence
Where a single observation is insufficient to establish material regression, persistence criteria shall define how long or how often a deviation must remain before escalation.

## Recurrence
Repeated deviations shall be evaluated for systemic regression even where individual deviations appear short-lived.

```text
ONE DEVIATION
↓
PERSISTENT?
├── NO → CONTINUE / RECORD
└── YES → ESCALATE

REPEATED DEVIATIONS
↓
RECURRENT?
├── NO → CONTINUE
└── YES → REGRESSION ASSESSMENT
```

## Threshold and Tolerance Integrity
Comparison thresholds shall be versioned and governed. Thresholds shall not be changed retroactively to erase previously detected material deviations.

## Baseline Change Interaction
When a baseline changes, historical comparison results shall remain linked to the baseline version that was valid at the time. A new baseline shall not rewrite history.

## Semantic Drift
Changes in measure definitions, units, instrumentation or processing shall be detected because semantic drift can create false deviations or hide real ones.

## Missing Observation Interaction
Missing observations shall not be interpreted as equality with baseline. If comparison cannot be performed reliably, the result shall be explicitly qualified.

```text
MISSING CURRENT DATA
≠
CURRENT STATE = BASELINE
```

## Explainable Deviations
An explainable deviation shall still be recorded when material to trend analysis, future learning or governance assurance.

## Outlier Handling
Outliers shall be investigated before exclusion. Exclusion rules shall be explicit, versioned and traceable.

## AI and Agent Deviation Integrity
AI/agent deviations shall distinguish between model changes, configuration changes, policy changes, data changes, tool changes, authority changes and behavioural changes where those dimensions are material.

## Comparison Anti-Gaming
Comparison logic shall not be manipulated by selective windows, selective measures, favorable baselines, hidden exclusions, retroactive threshold changes or suppression of inconvenient results.

## Relationship to Classification
RG-086 identifies and validates deviation. The subsequent classification layer determines consequence, severity and required governance response.

```text
COMPARE
↓
DEVIATION
↓
VALIDATE
↓
CLASSIFY
↓
ALERT / RESPONSE AS REQUIRED
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure comparison and deviation-detection layer beneath measurement and observation and above classification, alerting and regression response. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Deviation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → BASELINE → POST-CLOSURE MEASUREMENT / OBSERVATION → COMPARISON → MANDATORY DEVIATION DETECTION → CLASSIFICATION → ALERTING → ACKNOWLEDGEMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → POST-CLOSURE TRANSITION → REGRESSION DETECTION → REOPENING
```

## Complete Comparison Chain
```text
BASELINE → OBSERVE → VALIDATE → ALIGN → COMPARE → DETECT DEVIATION → VALIDATE DEVIATION → CLASSIFY → ALERT → ACKNOWLEDGE → RESPOND → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-087` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Deviation Classification and Consequence Determination

## Final Principle
EA-IMETA SHALL REQUIRE POST-CLOSURE COMPARISON AND DEVIATION DETECTION TO USE VALID OBSERVATIONS, THE CORRECT BASELINE VERSION, COMPATIBLE MEASUREMENT SEMANTICS, RELEVANT CONTEXT AND EXPLICIT DEVIATION RULES, SO THAT NORMAL VARIATION IS NOT MISTAKEN FOR REGRESSION AND MATERIAL DEGRADATION CANNOT BE HIDDEN THROUGH THRESHOLD MANIPULATION, SELECTIVE DATA OR UNCONTROLLED BASELINE CHANGE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETECTION-01
