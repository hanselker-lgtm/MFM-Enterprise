# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-CLOSURE-MANDATORY-POST-CLOSURE-MONITORING-MANDATORY-REGRESSION-DETECTION-01

## Physical File ID
`EA-IMETA-PC-RG-023`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-023` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-CLOSURE-MANDATORY-POST-CLOSURE-MONITORING-MANDATORY-REGRESSION-DETECTION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Regression Detection |
| Parent | EA-IMETA-PC-RG-022 — Mandatory Post-Closure Monitoring |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-regression-detection layer defining how post-closure observations are evaluated to identify recurrence, deterioration, control degradation, changed assumptions, boundary violations or other evidence that the closed state may no longer remain valid.

## Core Principle
Regression detection is the decision layer between post-closure observation and governed reopening. It shall distinguish normal variation from meaningful deterioration and shall provide sufficient evidence, sensitivity and traceability to prevent an invalid closed state from remaining accepted merely because the original closure was once valid.

```text
POST-CLOSURE OBSERVATION
      ↓
BASELINE / EXPECTED STATE
      ↓
COMPARE / CORRELATE / ANALYSE
      ↓
NORMAL / WARNING / SUSPECTED REGRESSION / CONFIRMED REGRESSION / UNKNOWN
      ↓
CLASSIFY MATERIALITY
      ↓
ALERT / ESCALATE / REOPEN / REASSESS
```

## Regression Detection Quality Test
```text
DEFINED CLOSED STATE
+
KNOWN REGRESSION MODES
+
RELEVANT INDICATORS
+
VALID BASELINE
+
SUFFICIENT SENSITIVITY
+
SUFFICIENT EVIDENCE
+
CORRELATION / CONTEXT
+
CLASSIFICATION
+
REOPENING PATH
=
VALID GOVERNED REGRESSION DETECTION
```

## Regression Detection Status Model
```text
NOT REQUIRED
DEFINED
READY
ACTIVE
NORMAL
WARNING
REGRESSION SUSPECTED
REGRESSION CONFIRMED
REGRESSION MATERIAL
REGRESSION IMMATERIAL
UNKNOWN
FALSE POSITIVE
DETECTION FAILED
REOPENED
UNDER REVIEW
SUPERSEDED
```

## Regression Detection Invariants

```text
EVERY MATERIAL CLOSED STATE SHALL HAVE A DOCUMENTED REGRESSION-DETECTION DETERMINATION
```

```text
KNOWN REGRESSION MODES SHALL BE IDENTIFIED WHERE PRACTICABLE
```

```text
REGRESSION DETECTION SHALL BE LINKED TO THE ACTUAL CLOSURE BASIS AND REQUIRED STATE
```

```text
NORMAL VARIATION SHALL NOT BE MISCLASSIFIED AS MATERIAL REGRESSION WITHOUT GOVERNED CRITERIA
```

```text
MATERIAL REGRESSION SHALL NOT BE MISCLASSIFIED AS NORMAL VARIATION TO PRESERVE CLOSURE
```

```text
DETECTION SENSITIVITY SHALL BE APPROPRIATE TO MATERIALITY AND REQUIRED DETECTION TIME
```

```text
BASELINES SHALL BE VERSIONED AND SHALL PRESERVE HISTORICAL STATE
```

```text
CORRELATION SHALL ADD CONTEXT WITHOUT HIDING INDIVIDUAL MATERIAL SIGNALS
```

```text
UNKNOWN OBSERVABILITY SHALL NOT BE TREATED AS PROOF OF NO REGRESSION
```

```text
DETECTION RESULTS SHALL BE TRACEABLE TO OBSERVATIONS, RULES, BASELINES AND CLASSIFICATION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE REGRESSION SHALL RECEIVE APPROPRIATE DETECTION RIGOR
```

```text
AI AND AGENT REGRESSION DETECTION SHALL INCLUDE RELEVANT AUTHORITY, POLICY, TOOL, DATA, AUTONOMY AND BEHAVIOURAL CHANGES
```

```text
MATERIAL REGRESSION SHALL TRIGGER THE DEFINED ALERT, ESCALATION, REOPENING OR REASSESSMENT PATH
```

```text
FALSE POSITIVES AND FALSE NEGATIVES SHALL BE REVIEWED FOR SYSTEMIC IMPROVEMENT
```

```text
HISTORICAL REGRESSION DETECTIONS SHALL REMAIN PRESERVED FOR TRACEABILITY AND LEARNING
```

## 1. Detection Domain — Regression Detection Governance

**Control family:** `PCRD-001`

The Regression Detection Governance domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-001-01` — Establish and maintain the regression detection governance control.
- `PCRD-001-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-02` — Establish and maintain the regression detection governance control.
- `PCRD-001-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-03` — Establish and maintain the regression detection governance control.
- `PCRD-001-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-04` — Establish and maintain the regression detection governance control.
- `PCRD-001-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-05` — Establish and maintain the regression detection governance control.
- `PCRD-001-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-06` — Establish and maintain the regression detection governance control.
- `PCRD-001-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-001-07` — Establish and maintain the regression detection governance control.
- `PCRD-001-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 2. Detection Domain — Regression Detection Objective

**Control family:** `PCRD-002`

The Regression Detection Objective domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-002-01` — Establish and maintain the regression detection objective control.
- `PCRD-002-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-02` — Establish and maintain the regression detection objective control.
- `PCRD-002-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-03` — Establish and maintain the regression detection objective control.
- `PCRD-002-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-04` — Establish and maintain the regression detection objective control.
- `PCRD-002-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-05` — Establish and maintain the regression detection objective control.
- `PCRD-002-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-06` — Establish and maintain the regression detection objective control.
- `PCRD-002-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-002-07` — Establish and maintain the regression detection objective control.
- `PCRD-002-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 3. Detection Domain — Regression Detection Definition

**Control family:** `PCRD-003`

The Regression Detection Definition domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-003-01` — Establish and maintain the regression detection definition control.
- `PCRD-003-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-02` — Establish and maintain the regression detection definition control.
- `PCRD-003-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-03` — Establish and maintain the regression detection definition control.
- `PCRD-003-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-04` — Establish and maintain the regression detection definition control.
- `PCRD-003-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-05` — Establish and maintain the regression detection definition control.
- `PCRD-003-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-06` — Establish and maintain the regression detection definition control.
- `PCRD-003-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-003-07` — Establish and maintain the regression detection definition control.
- `PCRD-003-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 4. Detection Domain — Regression Detection Scope

**Control family:** `PCRD-004`

The Regression Detection Scope domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-004-01` — Establish and maintain the regression detection scope control.
- `PCRD-004-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-02` — Establish and maintain the regression detection scope control.
- `PCRD-004-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-03` — Establish and maintain the regression detection scope control.
- `PCRD-004-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-04` — Establish and maintain the regression detection scope control.
- `PCRD-004-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-05` — Establish and maintain the regression detection scope control.
- `PCRD-004-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-06` — Establish and maintain the regression detection scope control.
- `PCRD-004-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-004-07` — Establish and maintain the regression detection scope control.
- `PCRD-004-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 5. Detection Domain — Regression Detection Authority

**Control family:** `PCRD-005`

The Regression Detection Authority domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-005-01` — Establish and maintain the regression detection authority control.
- `PCRD-005-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-02` — Establish and maintain the regression detection authority control.
- `PCRD-005-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-03` — Establish and maintain the regression detection authority control.
- `PCRD-005-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-04` — Establish and maintain the regression detection authority control.
- `PCRD-005-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-05` — Establish and maintain the regression detection authority control.
- `PCRD-005-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-06` — Establish and maintain the regression detection authority control.
- `PCRD-005-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-005-07` — Establish and maintain the regression detection authority control.
- `PCRD-005-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 6. Detection Domain — Regression Detection Criteria

**Control family:** `PCRD-006`

The Regression Detection Criteria domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-006-01` — Establish and maintain the regression detection criteria control.
- `PCRD-006-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-02` — Establish and maintain the regression detection criteria control.
- `PCRD-006-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-03` — Establish and maintain the regression detection criteria control.
- `PCRD-006-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-04` — Establish and maintain the regression detection criteria control.
- `PCRD-006-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-05` — Establish and maintain the regression detection criteria control.
- `PCRD-006-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-06` — Establish and maintain the regression detection criteria control.
- `PCRD-006-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-006-07` — Establish and maintain the regression detection criteria control.
- `PCRD-006-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 7. Detection Domain — Regression Detection Indicators

**Control family:** `PCRD-007`

The Regression Detection Indicators domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-007-01` — Establish and maintain the regression detection indicators control.
- `PCRD-007-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-02` — Establish and maintain the regression detection indicators control.
- `PCRD-007-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-03` — Establish and maintain the regression detection indicators control.
- `PCRD-007-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-04` — Establish and maintain the regression detection indicators control.
- `PCRD-007-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-05` — Establish and maintain the regression detection indicators control.
- `PCRD-007-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-06` — Establish and maintain the regression detection indicators control.
- `PCRD-007-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-007-07` — Establish and maintain the regression detection indicators control.
- `PCRD-007-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 8. Detection Domain — Regression Detection Baseline

**Control family:** `PCRD-008`

The Regression Detection Baseline domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-008-01` — Establish and maintain the regression detection baseline control.
- `PCRD-008-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-02` — Establish and maintain the regression detection baseline control.
- `PCRD-008-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-03` — Establish and maintain the regression detection baseline control.
- `PCRD-008-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-04` — Establish and maintain the regression detection baseline control.
- `PCRD-008-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-05` — Establish and maintain the regression detection baseline control.
- `PCRD-008-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-06` — Establish and maintain the regression detection baseline control.
- `PCRD-008-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-008-07` — Establish and maintain the regression detection baseline control.
- `PCRD-008-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 9. Detection Domain — Regression Detection Sensitivity

**Control family:** `PCRD-009`

The Regression Detection Sensitivity domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-009-01` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-02` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-03` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-04` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-05` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-06` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-009-07` — Establish and maintain the regression detection sensitivity control.
- `PCRD-009-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 10. Detection Domain — Regression Detection Evidence

**Control family:** `PCRD-010`

The Regression Detection Evidence domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-010-01` — Establish and maintain the regression detection evidence control.
- `PCRD-010-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-02` — Establish and maintain the regression detection evidence control.
- `PCRD-010-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-03` — Establish and maintain the regression detection evidence control.
- `PCRD-010-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-04` — Establish and maintain the regression detection evidence control.
- `PCRD-010-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-05` — Establish and maintain the regression detection evidence control.
- `PCRD-010-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-06` — Establish and maintain the regression detection evidence control.
- `PCRD-010-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-010-07` — Establish and maintain the regression detection evidence control.
- `PCRD-010-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 11. Detection Domain — Regression Detection Correlation

**Control family:** `PCRD-011`

The Regression Detection Correlation domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-011-01` — Establish and maintain the regression detection correlation control.
- `PCRD-011-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-02` — Establish and maintain the regression detection correlation control.
- `PCRD-011-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-03` — Establish and maintain the regression detection correlation control.
- `PCRD-011-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-04` — Establish and maintain the regression detection correlation control.
- `PCRD-011-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-05` — Establish and maintain the regression detection correlation control.
- `PCRD-011-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-06` — Establish and maintain the regression detection correlation control.
- `PCRD-011-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-011-07` — Establish and maintain the regression detection correlation control.
- `PCRD-011-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 12. Detection Domain — Regression Detection Classification

**Control family:** `PCRD-012`

The Regression Detection Classification domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-012-01` — Establish and maintain the regression detection classification control.
- `PCRD-012-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-02` — Establish and maintain the regression detection classification control.
- `PCRD-012-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-03` — Establish and maintain the regression detection classification control.
- `PCRD-012-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-04` — Establish and maintain the regression detection classification control.
- `PCRD-012-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-05` — Establish and maintain the regression detection classification control.
- `PCRD-012-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-06` — Establish and maintain the regression detection classification control.
- `PCRD-012-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-012-07` — Establish and maintain the regression detection classification control.
- `PCRD-012-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 13. Detection Domain — Security Regression Detection

**Control family:** `PCRD-013`

The Security Regression Detection domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-013-01` — Establish and maintain the security regression detection control.
- `PCRD-013-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-02` — Establish and maintain the security regression detection control.
- `PCRD-013-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-03` — Establish and maintain the security regression detection control.
- `PCRD-013-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-04` — Establish and maintain the security regression detection control.
- `PCRD-013-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-05` — Establish and maintain the security regression detection control.
- `PCRD-013-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-06` — Establish and maintain the security regression detection control.
- `PCRD-013-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-013-07` — Establish and maintain the security regression detection control.
- `PCRD-013-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 14. Detection Domain — Resilience Regression Detection

**Control family:** `PCRD-014`

The Resilience Regression Detection domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-014-01` — Establish and maintain the resilience regression detection control.
- `PCRD-014-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-02` — Establish and maintain the resilience regression detection control.
- `PCRD-014-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-03` — Establish and maintain the resilience regression detection control.
- `PCRD-014-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-04` — Establish and maintain the resilience regression detection control.
- `PCRD-014-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-05` — Establish and maintain the resilience regression detection control.
- `PCRD-014-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-06` — Establish and maintain the resilience regression detection control.
- `PCRD-014-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-014-07` — Establish and maintain the resilience regression detection control.
- `PCRD-014-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 15. Detection Domain — Compliance Regression Detection

**Control family:** `PCRD-015`

The Compliance Regression Detection domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-015-01` — Establish and maintain the compliance regression detection control.
- `PCRD-015-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-02` — Establish and maintain the compliance regression detection control.
- `PCRD-015-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-03` — Establish and maintain the compliance regression detection control.
- `PCRD-015-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-04` — Establish and maintain the compliance regression detection control.
- `PCRD-015-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-05` — Establish and maintain the compliance regression detection control.
- `PCRD-015-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-06` — Establish and maintain the compliance regression detection control.
- `PCRD-015-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-015-07` — Establish and maintain the compliance regression detection control.
- `PCRD-015-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 16. Detection Domain — Data Regression Detection

**Control family:** `PCRD-016`

The Data Regression Detection domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-016-01` — Establish and maintain the data regression detection control.
- `PCRD-016-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-02` — Establish and maintain the data regression detection control.
- `PCRD-016-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-03` — Establish and maintain the data regression detection control.
- `PCRD-016-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-04` — Establish and maintain the data regression detection control.
- `PCRD-016-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-05` — Establish and maintain the data regression detection control.
- `PCRD-016-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-06` — Establish and maintain the data regression detection control.
- `PCRD-016-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-016-07` — Establish and maintain the data regression detection control.
- `PCRD-016-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 17. Detection Domain — AI and Agent Regression Detection

**Control family:** `PCRD-017`

The AI and Agent Regression Detection domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-017-01` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-02` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-03` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-04` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-05` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-06` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-017-07` — Establish and maintain the ai and agent regression detection control.
- `PCRD-017-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 18. Detection Domain — Regression Detection Failure

**Control family:** `PCRD-018`

The Regression Detection Failure domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-018-01` — Establish and maintain the regression detection failure control.
- `PCRD-018-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-02` — Establish and maintain the regression detection failure control.
- `PCRD-018-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-03` — Establish and maintain the regression detection failure control.
- `PCRD-018-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-04` — Establish and maintain the regression detection failure control.
- `PCRD-018-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-05` — Establish and maintain the regression detection failure control.
- `PCRD-018-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-06` — Establish and maintain the regression detection failure control.
- `PCRD-018-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-018-07` — Establish and maintain the regression detection failure control.
- `PCRD-018-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 19. Detection Domain — Regression Detection Escalation

**Control family:** `PCRD-019`

The Regression Detection Escalation domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-019-01` — Establish and maintain the regression detection escalation control.
- `PCRD-019-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-02` — Establish and maintain the regression detection escalation control.
- `PCRD-019-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-03` — Establish and maintain the regression detection escalation control.
- `PCRD-019-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-04` — Establish and maintain the regression detection escalation control.
- `PCRD-019-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-05` — Establish and maintain the regression detection escalation control.
- `PCRD-019-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-06` — Establish and maintain the regression detection escalation control.
- `PCRD-019-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-019-07` — Establish and maintain the regression detection escalation control.
- `PCRD-019-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## 20. Detection Domain — Regression Detection Review and Learning

**Control family:** `PCRD-020`

The Regression Detection Review and Learning domain establishes governed mandatory-regression-detection requirements for post-closure control.

### Required controls
- `PCRD-020-01` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-01-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-02` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-02-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-03` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-03-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-04` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-04-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-05` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-05-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-06` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-06-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.
- `PCRD-020-07` — Establish and maintain the regression detection review and learning control.
- `PCRD-020-07-E` — Preserve observation, baseline, detection rule, context, classification, evidence, decision and disposition traceability.

```text
OBSERVE → DETECT → CLASSIFY → ALERT / REOPEN / REASSESS
```

## Regression Detection Structure

| Element | Required definition |
|---|---|
| Closed State | State being protected |
| Regression Mode | Known or hypothesized deterioration path |
| Indicator | Observable signal |
| Baseline | Expected state |
| Rule | Detection logic |
| Sensitivity | Ability to detect meaningful change |
| Context | Relevant surrounding conditions |
| Classification | Materiality and confidence |
| Evidence | Supporting observations |
| Action Path | Alert / escalation / reopening / reassessment |

## Regression Detection Objective

The objective is to detect evidence that the closed state has materially deteriorated, recurred, changed or otherwise ceased to satisfy the assumptions and conditions under which closure was granted.

## Regression Detection Definition

Regression detection is the controlled identification and classification of deviation from an accepted post-closure state that may invalidate closure, reliance or the underlying resolution.

## Regression Detection Scope

Scope shall identify the closed condition, relevant dependencies, indicators, environments, users, data and boundaries that can demonstrate regression.

## Regression Detection Authority

Authority shall define who owns detection rules, who may classify materiality, who can trigger reopening and who can authorize changes to detection logic.

## Regression Detection Criteria

Criteria shall distinguish normal variation, warning, suspected regression, confirmed regression and material regression.

```text
OBSERVATION
↓
EXPECTED STATE?
├── YES → NORMAL
└── NO
     ↓
MEANINGFUL DEVIATION?
├── NO → VARIATION / RECORD
└── YES → SUSPECTED REGRESSION
             ↓
          EVIDENCE SUFFICIENT?
          ├── NO → UNKNOWN / INVESTIGATE
          └── YES → CONFIRMED REGRESSION
```

## Regression Detection Indicators

Indicators shall represent observable consequences of regression modes identified during resolution and closure. Leading indicators shall be used where they materially improve detection time.

## Regression Detection Baseline

The baseline shall represent the approved post-closure state and shall retain enough context to distinguish genuine regression from legitimate environmental change.

## Regression Detection Sensitivity

Sensitivity shall be calibrated to detect material regression without generating uncontrolled noise. Changes to sensitivity shall be governed and tested.

```text
MATERIALITY + REGRESSION RISK + DETECTION WINDOW
↓
REQUIRED SENSITIVITY
↓
RULE / THRESHOLD DESIGN
```

## Regression Detection Evidence

Detection evidence shall preserve the observation, timestamp, source, baseline version, rule version, context and classification rationale.

## Regression Detection Correlation

Correlated observations may strengthen confidence in regression detection, identify patterns or reduce false positives. Correlation shall not suppress a mandatory material signal.

## Regression Detection Classification

Detection results shall distinguish confidence and materiality.

```text
NORMAL
WARNING
SUSPECTED REGRESSION
CONFIRMED REGRESSION
MATERIAL REGRESSION
UNKNOWN
FALSE POSITIVE
```

## Security Regression Detection

Detect recurrence or deterioration of security controls, access conditions, exposure, vulnerabilities, incidents and security boundaries underlying closure.

## Resilience Regression Detection

Detect recurrence or deterioration of availability, recovery, capacity, dependency, continuity and resilience conditions underlying closure.

## Compliance Regression Detection

Detect recurrence or emergence of non-conformance, control failure, contractual breach or regulatory exposure after closure.

## Data Regression Detection

Detect recurrence or deterioration of integrity, quality, completeness, lineage, access, retention and authorized-use conditions underlying closure.

## AI and Agent Regression Detection

Detect material changes in AI/agent authority, policy adherence, tool usage, data usage, autonomy, output behaviour and safety boundaries.

```text
CLOSED AI / AGENT STATE
↓
OBSERVE
↓
BOUNDARY CHANGE / VIOLATION?
├── NO → CONTINUE
└── YES → CLASSIFY → ALERT / REOPEN / SUSPEND / ESCALATE
```

## Regression Detection Failure

Failure to detect a material regression within the required detection window is itself a control failure and shall trigger impact assessment and governance response.

```text
DETECTION FAILURE
↓
IDENTIFY MISSED WINDOW
↓
PROTECT REQUIRED STATE
↓
RESTORE DETECTION
↓
ASSESS WHETHER REOPENING / REASSESSMENT IS REQUIRED
```

## Regression Detection Escalation

Escalation shall occur when regression is confirmed or material, confidence is sufficient to indicate significant risk, detection is repeatedly inconclusive, or the impact exceeds local authority.

## Regression Detection Review and Learning

Detection performance shall be reviewed for false positives, false negatives, missed scenarios, weak indicators, poor sensitivity, baseline defects and recurring regression patterns.

## Regression Detection Determination Model
```text
OBSERVATION AVAILABLE?
├── NO → UNKNOWN / DETECTION GAP
└── YES
     ↓
COMPARE WITH VALID BASELINE
├── NO BASELINE → GOVERNANCE GAP
└── YES
     ↓
MEANINGFUL DEVIATION?
├── NO → NORMAL / VARIATION
└── YES
     ↓
EVIDENCE / CONTEXT SUFFICIENT?
├── NO → SUSPECTED / UNKNOWN / INVESTIGATE
└── YES
     ↓
MATERIALITY THRESHOLD MET?
├── NO → NON-MATERIAL REGRESSION / MONITOR
└── YES → MATERIAL REGRESSION → ALERT / ESCALATE / REOPEN / REASSESS
```

## Regression Detection Record
| Field | Required |
|---|---|
| Detection ID | Yes |
| Closure ID | Yes |
| Monitoring ID | Yes |
| Regression Mode | Yes |
| Indicator | Yes |
| Observation Timestamp | Yes |
| Source | Yes |
| Baseline Version | Yes |
| Rule Version | Yes |
| Context | Where applicable |
| Classification | Yes |
| Confidence | Where applicable |
| Materiality | Yes |
| Alert / Escalation Reference | Where applicable |
| Reopening Reference | Where applicable |
| Evidence References | Yes |
| Decision / Disposition | Yes |

## Regression Confidence Model
```text
LOW CONFIDENCE
→ INVESTIGATE / CONTINUE MONITORING
MEDIUM CONFIDENCE
→ INCREASE OBSERVATION / CORRELATE / REVIEW
HIGH CONFIDENCE
→ CLASSIFY / ALERT / ESCALATE AS MATERIALITY REQUIRES
CONFIRMED MATERIAL REGRESSION
→ REOPEN / REASSESS / REVALIDATE
```

## Regression Reopening Interface
```text
CONFIRMED MATERIAL REGRESSION
↓
REOPEN CLOSED CONDITION
↓
REASSESS CURRENT STATE
↓
REVALIDATE BASIS
↓
REMEDIATE
↓
VERIFY
↓
RE-CLOSE
↓
POST-CLOSURE MONITOR AGAIN
```

## Regression Detection Anti-Gaming Control
Regression detection shall not be weakened, delayed, rebaselined or reclassified solely to preserve closure performance, avoid reopening or reduce reported findings. Material changes to detection logic shall be governed and traceable.

## Regression Detection Change Control
Changes to regression modes, indicators, baselines, sensitivity, rules, classification or action paths shall be governed, approved, versioned and effective-dated.

```text
CURRENT DETECTION MODEL
↓
CHANGE PROPOSAL
↓
IMPACT / RISK ASSESSMENT
↓
AUTHORITY APPROVAL
↓
NEW VERSION
↓
EFFECTIVE DATE
```

Historical detections, false positives, false negatives, rule versions and reopening events shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-regression-detection layer beneath mandatory post-closure monitoring. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, monitoring, alerting, escalation, resolution, closure or post-closure monitoring layers.

## Governance-to-Regression-Detection Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → ESCALATION → RESOLUTION → CLOSURE → POST-CLOSURE MONITORING → MANDATORY REGRESSION DETECTION → REOPEN / REASSESS / REVALIDATE
```

## Complete Regression Chain
```text
MANDATORY STATE → VERIFY → EVIDENCE → MEASURE → THRESHOLD → CLASSIFY → CONSEQUENCE → RESPOND → EFFECTIVENESS → REASSESS → REVALIDATE → ACCEPT → RELY → MONITOR → ALERT → ESCALATE → RESOLVE → VERIFY → CLOSE → POST-CLOSURE MONITOR → DETECT REGRESSION → CLASSIFY → REOPEN / REASSESS
```

## Next Document
`EA-IMETA-PC-RG-024` — Mandatory Regression Classification

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL CLOSED STATES TO BE SUBJECT TO GOVERNED REGRESSION DETECTION THAT COMPARES CURRENT POST-CLOSURE OBSERVATIONS AGAINST VALID BASELINES, RELEVANT REGRESSION MODES AND MATERIALITY CRITERIA, WITH SUFFICIENT SENSITIVITY, EVIDENCE AND TRACEABILITY TO DISTINGUISH NORMAL VARIATION FROM REGRESSION AND TO TRIGGER REOPENING, ESCALATION OR REASSESSMENT WHEN REQUIRED.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-CLOSURE-MANDATORY-POST-CLOSURE-MONITORING-MANDATORY-REGRESSION-DETECTION-01
