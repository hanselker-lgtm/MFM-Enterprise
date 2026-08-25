# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MEASUREMENT-AND-OBSERVATION-01

## Physical File ID
`EA-IMETA-PC-RG-073`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-073` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MEASUREMENT-AND-OBSERVATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Monitoring Measurement and Observation |
| Parent | EA-IMETA-PC-RG-072 — Mandatory Monitoring Baseline Establishment |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory measurement and observation layer that produces reliable, comparable and traceable current-state information against the active monitoring baseline.

## Core Principle
Monitoring requires trustworthy observations. Measurement converts an observable property into a defined value or result; observation establishes what is actually occurring. Neither measurement nor observation shall be treated as meaningful without context, method, timing, quality and traceability.

```text
ACTIVE BASELINE
      ↓
DEFINE WHAT MUST BE OBSERVED / MEASURED
      ↓
SELECT METHOD + SOURCE + FREQUENCY
      ↓
CAPTURE CURRENT OBSERVATION
      ↓
VALIDATE MEASUREMENT QUALITY
      ↓
COMPARE WITH BASELINE
      ↓
CURRENT STATE RESULT
├── NORMAL → CONTINUE
├── DEVIATION → CLASSIFY / ALERT
└── UNKNOWN → INVESTIGATE / CORRECT
```

## Measurement Quality Test
```text
DEFINED PROPERTY
+
APPROPRIATE METHOD
+
KNOWN SOURCE
+
VALID TIME CONTEXT
+
KNOWN UNIT / SCALE
+
QUALITY CHECK
+
TRACEABLE RECORD
+
COMPARABLE BASELINE
=
VALID GOVERNED MEASUREMENT
```

## Observation Quality Test
```text
OBSERVATION OBJECT
+
CURRENT CONTEXT
+
OBSERVATION METHOD
+
OBSERVER / SOURCE
+
TIMESTAMP
+
SUFFICIENT EVIDENCE
+
TRACEABILITY
=
VALID GOVERNED OBSERVATION
```

## Measurement / Observation Status Model
```text
NOT DUE
SCHEDULED
IN PROGRESS
CAPTURED
VALIDATED
COMPARABLE
DEVIATING
INVALID
UNKNOWN
MISSING
SUPERSEDED
```

## Measurement and Observation Invariants

```text
MEASUREMENT AND OBSERVATION OBJECTS SHALL BE EXPLICIT
```

```text
METHODS SHALL BE APPROPRIATE TO THE PROPERTY BEING MEASURED OR OBSERVED
```

```text
TIME, CONTEXT AND SOURCE SHALL BE TRACEABLE
```

```text
UNITS, SCALES AND TRANSFORMATIONS SHALL BE KNOWN WHERE APPLICABLE
```

```text
MEASUREMENT QUALITY SHALL BE ASSESSED WHERE MATERIAL
```

```text
OBSERVATION SHALL REMAIN DISTINCT FROM INTERPRETATION
```

```text
MEASUREMENT SHALL REMAIN DISTINCT FROM DECISION
```

```text
MISSING OR INVALID MEASUREMENTS SHALL NOT BE TREATED AS NORMAL
```

```text
UNKNOWN SHALL REMAIN DISTINCT FROM NO DEVIATION
```

```text
BASELINE COMPARISON SHALL USE COMPATIBLE MEASUREMENT CONTEXT
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE MEASUREMENTS SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT MEASUREMENT SHALL COVER MATERIAL AUTHORITY, POLICY, TOOL, DATA, AUTONOMY AND BEHAVIOURAL PROPERTIES
```

```text
MEASUREMENT METHODS SHALL NOT BE CHANGED SILENTLY
```

```text
MEASUREMENT HISTORY SHALL REMAIN PRESERVED FOR TREND AND REGRESSION ANALYSIS
```

```text
MEASUREMENT GAPS THAT COULD HIDE MATERIAL REGRESSION SHALL BE GOVERNED AS CONDITIONS
```

## 1. Measurement Domain — Monitoring Measurement Observation Governance

**Control family:** `PCRMO-001`

The Monitoring Measurement Observation Governance domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-001-01` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-02` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-03` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-04` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-05` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-06` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-001-07` — Establish and maintain the monitoring measurement observation governance control.
- `PCRMO-001-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 2. Measurement Domain — Monitoring Measurement Observation Objective

**Control family:** `PCRMO-002`

The Monitoring Measurement Observation Objective domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-002-01` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-02` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-03` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-04` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-05` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-06` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-002-07` — Establish and maintain the monitoring measurement observation objective control.
- `PCRMO-002-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 3. Measurement Domain — Monitoring Measurement Observation Definition

**Control family:** `PCRMO-003`

The Monitoring Measurement Observation Definition domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-003-01` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-02` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-03` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-04` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-05` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-06` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-003-07` — Establish and maintain the monitoring measurement observation definition control.
- `PCRMO-003-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 4. Measurement Domain — Monitoring Measurement Observation Scope

**Control family:** `PCRMO-004`

The Monitoring Measurement Observation Scope domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-004-01` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-02` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-03` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-04` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-05` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-06` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-004-07` — Establish and maintain the monitoring measurement observation scope control.
- `PCRMO-004-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 5. Measurement Domain — Monitoring Measurement Observation Authority

**Control family:** `PCRMO-005`

The Monitoring Measurement Observation Authority domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-005-01` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-02` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-03` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-04` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-05` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-06` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-005-07` — Establish and maintain the monitoring measurement observation authority control.
- `PCRMO-005-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 6. Measurement Domain — Monitoring Measurement Observation Criteria

**Control family:** `PCRMO-006`

The Monitoring Measurement Observation Criteria domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-006-01` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-02` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-03` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-04` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-05` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-06` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-006-07` — Establish and maintain the monitoring measurement observation criteria control.
- `PCRMO-006-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 7. Measurement Domain — Monitoring Measurement Observation Preconditions

**Control family:** `PCRMO-007`

The Monitoring Measurement Observation Preconditions domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-007-01` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-02` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-03` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-04` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-05` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-06` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-007-07` — Establish and maintain the monitoring measurement observation preconditions control.
- `PCRMO-007-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 8. Measurement Domain — Monitoring Measurement Observation Evidence

**Control family:** `PCRMO-008`

The Monitoring Measurement Observation Evidence domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-008-01` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-02` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-03` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-04` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-05` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-06` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-008-07` — Establish and maintain the monitoring measurement observation evidence control.
- `PCRMO-008-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 9. Measurement Domain — Monitoring Measurement Observation Method

**Control family:** `PCRMO-009`

The Monitoring Measurement Observation Method domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-009-01` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-02` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-03` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-04` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-05` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-06` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-009-07` — Establish and maintain the monitoring measurement observation method control.
- `PCRMO-009-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 10. Measurement Domain — Monitoring Measurement Observation Decision

**Control family:** `PCRMO-010`

The Monitoring Measurement Observation Decision domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-010-01` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-02` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-03` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-04` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-05` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-06` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-010-07` — Establish and maintain the monitoring measurement observation decision control.
- `PCRMO-010-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 11. Measurement Domain — Monitoring Measurement Observation Accountability

**Control family:** `PCRMO-011`

The Monitoring Measurement Observation Accountability domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-011-01` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-02` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-03` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-04` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-05` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-06` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-011-07` — Establish and maintain the monitoring measurement observation accountability control.
- `PCRMO-011-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 12. Measurement Domain — Monitoring Measurement Observation Timing

**Control family:** `PCRMO-012`

The Monitoring Measurement Observation Timing domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-012-01` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-02` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-03` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-04` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-05` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-06` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-012-07` — Establish and maintain the monitoring measurement observation timing control.
- `PCRMO-012-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 13. Measurement Domain — Security Monitoring Measurement Observation

**Control family:** `PCRMO-013`

The Security Monitoring Measurement Observation domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-013-01` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-02` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-03` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-04` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-05` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-06` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-013-07` — Establish and maintain the security monitoring measurement observation control.
- `PCRMO-013-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 14. Measurement Domain — Resilience Monitoring Measurement Observation

**Control family:** `PCRMO-014`

The Resilience Monitoring Measurement Observation domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-014-01` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-02` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-03` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-04` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-05` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-06` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-014-07` — Establish and maintain the resilience monitoring measurement observation control.
- `PCRMO-014-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 15. Measurement Domain — Compliance Monitoring Measurement Observation

**Control family:** `PCRMO-015`

The Compliance Monitoring Measurement Observation domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-015-01` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-02` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-03` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-04` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-05` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-06` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-015-07` — Establish and maintain the compliance monitoring measurement observation control.
- `PCRMO-015-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 16. Measurement Domain — Data Monitoring Measurement Observation

**Control family:** `PCRMO-016`

The Data Monitoring Measurement Observation domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-016-01` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-02` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-03` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-04` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-05` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-06` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-016-07` — Establish and maintain the data monitoring measurement observation control.
- `PCRMO-016-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 17. Measurement Domain — AI and Agent Monitoring Measurement Observation

**Control family:** `PCRMO-017`

The AI and Agent Monitoring Measurement Observation domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-017-01` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-02` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-03` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-04` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-05` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-06` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-017-07` — Establish and maintain the ai and agent monitoring measurement observation control.
- `PCRMO-017-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 18. Measurement Domain — Monitoring Measurement Observation Failure

**Control family:** `PCRMO-018`

The Monitoring Measurement Observation Failure domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-018-01` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-02` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-03` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-04` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-05` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-06` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-018-07` — Establish and maintain the monitoring measurement observation failure control.
- `PCRMO-018-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 19. Measurement Domain — Monitoring Measurement Observation Independence

**Control family:** `PCRMO-019`

The Monitoring Measurement Observation Independence domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-019-01` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-02` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-03` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-04` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-05` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-06` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-019-07` — Establish and maintain the monitoring measurement observation independence control.
- `PCRMO-019-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## 20. Measurement Domain — Monitoring Measurement Observation Review and Learning

**Control family:** `PCRMO-020`

The Monitoring Measurement Observation Review and Learning domain establishes governed mandatory measurement and observation requirements.

### Required controls
- `PCRMO-020-01` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-01-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-02` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-02-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-03` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-03-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-04` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-04-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-05` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-05-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-06` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-06-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.
- `PCRMO-020-07` — Establish and maintain the monitoring measurement observation review and learning control.
- `PCRMO-020-07-E` — Preserve object, method, source, timestamp, context, value/result, quality, baseline version and interpretation traceability.

```text
BASELINE → MEASURE / OBSERVE → COMPARE → CLASSIFY
```

## Monitoring Measurement Observation Structure

| Element | Required definition |
|---|---|
| Object | Property or condition measured/observed |
| Method | Defined acquisition method |
| Source | Instrument, system, person or data source |
| Timestamp | When observation occurred |
| Context | Conditions affecting interpretation |
| Value / Result | Recorded output |
| Quality | Confidence / validity information |
| Baseline | Reference version used |

## Monitoring Measurement Observation Objective

Produce reliable current-state evidence that can be compared with the active baseline and support governed detection of deviation, regression and uncertainty.

## Monitoring Measurement Observation Definition

Measurement is the controlled quantification or determination of a defined property; observation is the controlled recording of an actual condition, event or behaviour.

## Monitoring Measurement Observation Scope

Scope shall identify systems, services, users, data, decisions, dependencies, environments, consumers and boundaries subject to measurement or observation.

## Monitoring Measurement Observation Authority

Authority shall define who may establish methods, approve sources, validate results, interpret exceptions and change measurement controls.

## Monitoring Measurement Observation Criteria

Criteria shall distinguish valid, invalid, missing, unknown, comparable and deviating observations.

```text
CAPTURE
↓
QUALITY VALID?
├── NO → INVALID / INVESTIGATE
└── YES
     ↓
COMPARABLE WITH BASELINE?
├── NO → UNKNOWN / RECONTEXTUALIZE
└── YES
     ↓
WITHIN EXPECTED RANGE?
├── YES → NORMAL
└── NO → DEVIATION
```

## Monitoring Measurement Observation Preconditions

Preconditions include active baseline, defined property, approved method, source, frequency, context, units or scale where applicable and quality criteria.

## Monitoring Measurement Observation Evidence

Evidence shall preserve raw or authoritative source data where required, derived values, transformation logic, timestamps, context and quality information.

## Monitoring Measurement Observation Method

Methods may include direct measurement, telemetry, sampling, inspection, event capture, human observation, automated observation, statistical observation and controlled testing.

```text
OBJECT
↓
SOURCE
↓
METHOD
↓
CAPTURE
↓
QUALITY CHECK
↓
STORE
↓
COMPARE
```

## Monitoring Measurement Observation Decision

Measurement results shall support a distinction between normal, deviation, invalid, missing and unknown states without prematurely converting observations into conclusions.

```text
RESULT
├── VALID + NORMAL → CONTINUE
├── VALID + DEVIATING → CLASSIFY / ALERT
├── INVALID → CORRECT SOURCE / METHOD
├── MISSING → GOVERN GAP
└── UNKNOWN → INVESTIGATE
```

## Monitoring Measurement Observation Accountability

Accountability shall remain explicit for method integrity, source quality, data capture, validation, interpretation boundaries and record preservation.

## Monitoring Measurement Observation Timing

Frequency and timing shall reflect volatility, materiality, time-to-impact, baseline sensitivity and required detection latency.

## Security Monitoring Measurement Observation

Measure or observe material access, authentication, authorization, exposure, boundary, control and anomalous activity conditions.

## Resilience Monitoring Measurement Observation

Measure or observe availability, latency, capacity, recovery readiness, continuity, dependency health and degradation conditions.

## Compliance Monitoring Measurement Observation

Measure or observe compliance control performance, obligation status, evidence completeness, reporting conditions and policy deviations.

## Data Monitoring Measurement Observation

Measure or observe integrity, quality, completeness, timeliness, lineage, access, retention, authorized use and downstream data effects.

## AI and Agent Monitoring Measurement Observation

Measure or observe authority use, policy adherence, tool invocation, data access, autonomy, behaviour, model/configuration changes and material outcomes.

```text
AI / AGENT
↓
OBSERVE AUTHORITY + POLICY + TOOLS + DATA
↓
MEASURE AUTONOMY + BEHAVIOUR + OUTCOMES
↓
COMPARE WITH BASELINE
```

## Monitoring Measurement Observation Failure

Failure includes missing data, invalid source, stale observation, broken telemetry, incompatible method, unknown context or quality below required limits.

```text
MEASUREMENT FAILURE
↓
CAN REGRESSION STILL BE DETECTED?
├── YES → RESTRICT CONFIDENCE / CONTINUE WITH CONTROL
└── NO → GOVERN GAP / ALERT / ESCALATE AS REQUIRED
```

## Monitoring Measurement Observation Independence

Where materiality requires it, critical measurements or observations shall receive independent validation or corroboration.

## Monitoring Measurement Observation Review and Learning

Reviews shall identify sensor drift, sampling bias, blind spots, method weakness, stale data, false signals and recurring measurement gaps.

## Measurement Determination Model
```text
ACTIVE BASELINE
↓
PROPERTY DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
METHOD + SOURCE VALID?
├── NO → CORRECT
└── YES
     ↓
CURRENT OBSERVATION CAPTURED?
├── NO → MISSING / GOVERN GAP
└── YES
     ↓
QUALITY + CONTEXT VALID?
├── NO → INVALID / UNKNOWN
└── YES
     ↓
COMPARABLE WITH BASELINE?
├── NO → RECONTEXTUALIZE / UNKNOWN
└── YES → COMPARE
```

## Measurement Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Normal | Valid observation within expected state | Continue monitoring |
| Deviating | Valid observation outside expected state | Classify / alert |
| Invalid | Measurement quality inadequate | Correct / repeat |
| Missing | Expected measurement unavailable | Govern gap |
| Unknown | Current state cannot be established | Investigate |
| Superseded | New valid observation/version replaces prior record | Preserve history |

## Measurement Record
| Field | Required |
|---|---|
| Measurement ID | Yes |
| Baseline ID / Version | Yes |
| Object | Yes |
| Method | Yes |
| Source | Yes |
| Timestamp | Yes |
| Context | Yes |
| Value / Result | Yes |
| Unit / Scale | Where applicable |
| Quality | Yes |
| Transformation | Where applicable |
| Interpretation | Separate from raw result |

## Observation vs Interpretation
Observation records what is detected. Interpretation explains what the observation may mean. Interpretation shall not overwrite the underlying observation.

```text
OBSERVATION
→ WHAT WAS SEEN / MEASURED?

INTERPRETATION
→ WHAT MAY IT MEAN?

DECISION
→ WHAT SHALL BE DONE?
```

## Raw vs Derived Measurement
Where material, raw source evidence shall be retained alongside derived values so that transformations and calculations remain auditable.

## Measurement Context Integrity
A measurement shall retain the context needed to determine comparability, including time window, environment, configuration, sampling conditions and relevant dependencies.

```text
VALUE
+
UNIT
+
TIME
+
METHOD
+
CONTEXT
=
INTERPRETABLE MEASUREMENT
```

## Measurement Frequency
Frequency shall be governed by detection needs. A low-frequency measurement shall not be presented as continuous monitoring.

## Sampling
Sampling methods shall define population, sample selection, frequency, confidence or coverage rationale where material, and known limitations.

## Sensor / Source Quality
Material automated measurements shall consider source availability, freshness, integrity, calibration or equivalent quality controls where applicable.

## Measurement Drift
Changes in measurement method, source behaviour or instrument characteristics can create apparent regression. Such drift shall be detected and governed before conclusions are made.

```text
OBSERVED CHANGE
↓
SYSTEM CHANGE OR MEASUREMENT CHANGE?
├── SYSTEM → POSSIBLE REGRESSION
└── MEASUREMENT → SOURCE / METHOD INVESTIGATION
```

## Measurement Change Control
Changes to methods, sources, frequency, transformations, units, sampling, quality rules or context requirements shall be governed, approved, versioned and effective-dated.

```text
CURRENT METHOD
↓
CHANGE PROPOSAL
↓
COMPARABILITY IMPACT
↓
APPROVAL
↓
NEW METHOD VERSION
↓
TRANSITION CONTROL
```

## Measurement Anti-Gaming
Measurements shall not be selected, filtered, timed or transformed solely to reduce apparent regression, alerts or escalation.

## Measurement Gaps
A measurement gap that could conceal material regression shall itself become a governed monitoring condition and may require alerting or escalation.

## Relationship to Baseline and Alerting
Measurements and observations provide the evidence layer between baseline and deviation classification.

```text
BASELINE
↓
MEASURE / OBSERVE
↓
QUALITY CHECK
↓
COMPARE
↓
DEVIATION
↓
CLASSIFY
↓
ALERT
```

## Relationship to Existing Architecture
This document specializes the mandatory monitoring measurement-and-observation layer beneath baseline establishment and above comparison, deviation classification and alerting. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, reacceptance, reliance restoration, baseline establishment, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Measurement Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → BASELINE → MANDATORY MEASUREMENT / OBSERVATION → COMPARISON → ALERTING → ESCALATION → RESOLUTION
```

## Complete Measurement Chain
```text
REACCEPT → RESTORE RELIANCE → BASELINE → MEASURE / OBSERVE → COMPARE → DETECT → CLASSIFY → ALERT → ESCALATE → RESOLVE → VERIFY → REVALIDATE
```

## Next Document
`EA-IMETA-PC-RG-074` — Mandatory Regression Reliance Restoration Monitoring Comparison and Deviation Detection

## Final Principle
EA-IMETA SHALL REQUIRE POST-RESTORATION MONITORING TO PRODUCE CURRENT, CONTEXTUAL, TRACEABLE AND COMPARABLE MEASUREMENTS AND OBSERVATIONS AGAINST THE ACTIVE BASELINE, WITH METHOD, SOURCE, TIMING, QUALITY, UNITS, TRANSFORMATIONS AND LIMITATIONS GOVERNED, SO THAT INVALID, MISSING OR UNKNOWN INFORMATION CANNOT BE SILENTLY TREATED AS NORMAL AND MATERIAL REGRESSION CAN BE DETECTED BEFORE IT ESCAPES GOVERNANCE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MEASUREMENT-AND-OBSERVATION-01
