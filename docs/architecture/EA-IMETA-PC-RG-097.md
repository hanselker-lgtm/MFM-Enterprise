# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-OBSERVATION-AND-MEASUREMENT-CONTROL-01

## Physical File ID
`EA-IMETA-PC-RG-097`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-097` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-OBSERVATION-AND-MEASUREMENT-CONTROL-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Observation and Measurement Control |
| Parent | EA-IMETA-PC-RG-096 — Mandatory Post-Closure Monitoring Activation and Baseline Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory observation and measurement layer that converts an active post-closure monitoring model into trustworthy observations and measurements suitable for comparison, deviation detection, revalidation, reliance restoration and regression determination.

## Core Principle
Observation is the act of obtaining information about the current state. Measurement is the governed act of determining a value, condition or status from defined evidence. Neither observation nor measurement shall be treated as reliable merely because data exists. Quality, provenance, timing, method, uncertainty, completeness and fitness for purpose shall be controlled.

```text
MONITORING ACTIVE
      ↓
OBSERVATION REQUIRED
      ↓
DATA / SIGNAL ACQUIRED
      ↓
PROVENANCE + QUALITY VALIDATED?
├── NO → INVALID / DEGRADED / CORRECT
└── YES
     ↓
MEASUREMENT METHOD VALID?
├── NO → CORRECT / REPEAT
└── YES
     ↓
MEASUREMENT PRODUCED
     ↓
UNCERTAINTY / CONFIDENCE ASSESSED
     ↓
STORE + TRACE
     ↓
COMPARE AGAINST BASELINE / CRITERIA
```

## Observation and Measurement Quality Test
```text
DEFINED OBSERVATION OBJECTIVE
+
VALID DATA SOURCE
+
KNOWN PROVENANCE
+
VALID MEASUREMENT METHOD
+
TIMELY OBSERVATION
+
QUALITY CONTROL
+
UNCERTAINTY / CONFIDENCE
+
TRACEABLE RESULT
=
VALID GOVERNED OBSERVATION / MEASUREMENT
```

## Observation vs Measurement vs Comparison
```text
OBSERVATION
→ WHAT IS CURRENTLY SEEN / DETECTED?

MEASUREMENT
→ WHAT VALUE / STATE DOES THE EVIDENCE SUPPORT?

COMPARISON
→ HOW DOES THE MEASURED STATE DIFFER FROM THE REQUIRED REFERENCE?
```

## Observation and Measurement State Model
```text
EXPECTED
SCHEDULED
ACQUIRING
OBSERVED
VALIDATING
VALID
DEGRADED
INVALID
MISSING
STALE
MEASURED
UNCERTAIN
REJECTED
REPEATED
ACCEPTED
```

## Observation and Measurement Invariants

```text
OBSERVATION OBJECTIVES SHALL BE EXPLICIT
```

```text
MEASUREMENT METHODS SHALL BE DEFINED AND APPROPRIATE TO THE DECISION
```

```text
DATA PROVENANCE SHALL BE PRESERVED WHERE MATERIAL
```

```text
OBSERVATION TIME SHALL BE TRACEABLE WHERE TIMING AFFECTS INTERPRETATION
```

```text
DATA QUALITY SHALL BE ASSESSED BEFORE MATERIAL GOVERNANCE USE
```

```text
MEASUREMENT UNITS, SCALE AND SEMANTICS SHALL BE UNAMBIGUOUS
```

```text
UNCERTAINTY OR CONFIDENCE SHALL BE CONSIDERED WHERE MATERIAL
```

```text
MISSING OR STALE OBSERVATIONS SHALL NOT BE TREATED AS HEALTHY STATES
```

```text
INVALID MEASUREMENTS SHALL NOT ENTER GOVERNED COMPARISON AS VALID EVIDENCE
```

```text
REPEATED MEASUREMENTS SHALL PRESERVE THEIR INDIVIDUAL HISTORY
```

```text
MANUAL AND AUTOMATED MEASUREMENTS SHALL REMAIN ATTRIBUTABLE
```

```text
MEASUREMENT METHOD CHANGES SHALL BE GOVERNED AND TRACEABLE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE MEASUREMENTS SHALL HAVE APPROPRIATE RIGOR
```

```text
AI AND AGENT OBSERVATIONS SHALL CONSIDER BOTH OUTPUT AND CONTROL CONDITIONS
```

```text
OBSERVATION AND MEASUREMENT DATA SHALL REMAIN TRACEABLE TO THE POST-CLOSURE CONDITION
```

```text
MEASUREMENT RESULTS SHALL NOT BE ALTERED TO HIDE DEVIATION
```

## 1. Observation Domain — Post-Closure Observation Measurement Governance

**Control family:** `PCOM-001`

The Post-Closure Observation Measurement Governance domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-001-01` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-02` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-03` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-04` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-05` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-06` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-001-07` — Establish and maintain the post-closure observation measurement governance control.
- `PCOM-001-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 2. Observation Domain — Post-Closure Observation Measurement Objective

**Control family:** `PCOM-002`

The Post-Closure Observation Measurement Objective domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-002-01` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-02` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-03` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-04` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-05` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-06` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-002-07` — Establish and maintain the post-closure observation measurement objective control.
- `PCOM-002-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 3. Observation Domain — Post-Closure Observation Measurement Definition

**Control family:** `PCOM-003`

The Post-Closure Observation Measurement Definition domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-003-01` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-02` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-03` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-04` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-05` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-06` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-003-07` — Establish and maintain the post-closure observation measurement definition control.
- `PCOM-003-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 4. Observation Domain — Post-Closure Observation Measurement Scope

**Control family:** `PCOM-004`

The Post-Closure Observation Measurement Scope domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-004-01` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-02` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-03` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-04` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-05` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-06` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-004-07` — Establish and maintain the post-closure observation measurement scope control.
- `PCOM-004-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 5. Observation Domain — Post-Closure Observation Measurement Authority

**Control family:** `PCOM-005`

The Post-Closure Observation Measurement Authority domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-005-01` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-02` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-03` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-04` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-05` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-06` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-005-07` — Establish and maintain the post-closure observation measurement authority control.
- `PCOM-005-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 6. Observation Domain — Post-Closure Observation Measurement Criteria

**Control family:** `PCOM-006`

The Post-Closure Observation Measurement Criteria domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-006-01` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-02` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-03` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-04` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-05` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-06` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-006-07` — Establish and maintain the post-closure observation measurement criteria control.
- `PCOM-006-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 7. Observation Domain — Post-Closure Observation Measurement Preconditions

**Control family:** `PCOM-007`

The Post-Closure Observation Measurement Preconditions domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-007-01` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-02` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-03` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-04` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-05` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-06` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-007-07` — Establish and maintain the post-closure observation measurement preconditions control.
- `PCOM-007-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 8. Observation Domain — Post-Closure Observation Measurement Evidence

**Control family:** `PCOM-008`

The Post-Closure Observation Measurement Evidence domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-008-01` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-02` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-03` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-04` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-05` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-06` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-008-07` — Establish and maintain the post-closure observation measurement evidence control.
- `PCOM-008-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 9. Observation Domain — Post-Closure Observation Measurement Method

**Control family:** `PCOM-009`

The Post-Closure Observation Measurement Method domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-009-01` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-02` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-03` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-04` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-05` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-06` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-009-07` — Establish and maintain the post-closure observation measurement method control.
- `PCOM-009-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 10. Observation Domain — Post-Closure Observation Measurement Decision

**Control family:** `PCOM-010`

The Post-Closure Observation Measurement Decision domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-010-01` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-02` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-03` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-04` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-05` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-06` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-010-07` — Establish and maintain the post-closure observation measurement decision control.
- `PCOM-010-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 11. Observation Domain — Post-Closure Observation Measurement Accountability

**Control family:** `PCOM-011`

The Post-Closure Observation Measurement Accountability domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-011-01` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-02` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-03` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-04` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-05` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-06` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-011-07` — Establish and maintain the post-closure observation measurement accountability control.
- `PCOM-011-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 12. Observation Domain — Post-Closure Observation Measurement Timing

**Control family:** `PCOM-012`

The Post-Closure Observation Measurement Timing domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-012-01` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-02` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-03` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-04` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-05` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-06` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-012-07` — Establish and maintain the post-closure observation measurement timing control.
- `PCOM-012-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 13. Observation Domain — Security Post-Closure Observation Measurement

**Control family:** `PCOM-013`

The Security Post-Closure Observation Measurement domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-013-01` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-02` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-03` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-04` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-05` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-06` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-013-07` — Establish and maintain the security post-closure observation measurement control.
- `PCOM-013-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 14. Observation Domain — Resilience Post-Closure Observation Measurement

**Control family:** `PCOM-014`

The Resilience Post-Closure Observation Measurement domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-014-01` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-02` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-03` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-04` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-05` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-06` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-014-07` — Establish and maintain the resilience post-closure observation measurement control.
- `PCOM-014-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 15. Observation Domain — Compliance Post-Closure Observation Measurement

**Control family:** `PCOM-015`

The Compliance Post-Closure Observation Measurement domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-015-01` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-02` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-03` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-04` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-05` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-06` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-015-07` — Establish and maintain the compliance post-closure observation measurement control.
- `PCOM-015-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 16. Observation Domain — Data Post-Closure Observation Measurement

**Control family:** `PCOM-016`

The Data Post-Closure Observation Measurement domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-016-01` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-02` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-03` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-04` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-05` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-06` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-016-07` — Establish and maintain the data post-closure observation measurement control.
- `PCOM-016-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 17. Observation Domain — AI and Agent Post-Closure Observation Measurement

**Control family:** `PCOM-017`

The AI and Agent Post-Closure Observation Measurement domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-017-01` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-02` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-03` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-04` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-05` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-06` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-017-07` — Establish and maintain the ai and agent post-closure observation measurement control.
- `PCOM-017-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 18. Observation Domain — Post-Closure Observation Measurement Failure

**Control family:** `PCOM-018`

The Post-Closure Observation Measurement Failure domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-018-01` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-02` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-03` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-04` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-05` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-06` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-018-07` — Establish and maintain the post-closure observation measurement failure control.
- `PCOM-018-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 19. Observation Domain — Post-Closure Observation Measurement Independence

**Control family:** `PCOM-019`

The Post-Closure Observation Measurement Independence domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-019-01` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-02` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-03` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-04` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-05` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-06` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-019-07` — Establish and maintain the post-closure observation measurement independence control.
- `PCOM-019-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## 20. Observation Domain — Post-Closure Observation Measurement Review and Learning

**Control family:** `PCOM-020`

The Post-Closure Observation Measurement Review and Learning domain establishes governed mandatory observation and measurement requirements.

### Required controls
- `PCOM-020-01` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-01-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-02` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-02-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-03` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-03-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-04` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-04-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-05` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-05-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-06` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-06-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.
- `PCOM-020-07` — Establish and maintain the post-closure observation measurement review and learning control.
- `PCOM-020-07-E` — Preserve objective, source, provenance, timestamp, method, quality, uncertainty, result, reviewer and downstream-use traceability.

```text
ACQUIRE → VALIDATE → MEASURE → QUALIFY → TRACE → COMPARE
```

## Post-Closure Observation Measurement Structure

| Element | Required definition |
|---|---|
| Observation Objective | What must be observed |
| Data Source | Source of observation |
| Provenance | Origin and transformation history |
| Timestamp | Observation time |
| Method | Measurement method |
| Quality | Data quality assessment |
| Uncertainty | Known measurement uncertainty |
| Result | Measurement outcome |
| Attribution | Responsible source / actor |

## Post-Closure Observation Measurement Objective

Produce trustworthy, timely and traceable observations and measurements that can support material post-closure governance decisions.

## Post-Closure Observation Measurement Definition

Observation is the controlled acquisition of information about a state. Measurement is the controlled determination of a value, status or condition from that information.

## Post-Closure Observation Measurement Scope

Scope shall identify the monitored condition, observation channels, metrics, events, samples, data sources, time windows and decision uses.

## Post-Closure Observation Measurement Authority

Authority shall define who approves measurement methods, accepts quality exceptions, changes observation parameters and authorizes use of uncertain or degraded measurements.

## Post-Closure Observation Measurement Criteria

Criteria shall define data quality, timeliness, completeness, provenance, measurement method, tolerance, uncertainty, repeatability and fitness for purpose.

```text
DATA ACQUIRED
↓
SOURCE VALID?
├── NO → REJECT / INVESTIGATE
└── YES
     ↓
TIMELY + COMPLETE?
├── NO → STALE / DEGRADED / COMPENSATE
└── YES
     ↓
METHOD VALID?
├── NO → REPEAT / CORRECT
└── YES
     ↓
MEASUREMENT + UNCERTAINTY
↓
ACCEPT FOR GOVERNED USE
```

## Post-Closure Observation Measurement Preconditions

Preconditions include active monitoring, defined observation objective, valid data source, approved method, required instrumentation or collection process and quality rules.

## Post-Closure Observation Measurement Evidence

Evidence shall preserve raw or source observations where required, transformed values, timestamps, provenance, method version, quality checks, uncertainty and accepted result.

## Post-Closure Observation Measurement Method

Methods may include direct measurement, telemetry, sampling, inspection, automated evaluation, manual observation, statistical estimation and controlled inference.

```text
SOURCE
↓
OBSERVE
↓
VALIDATE
↓
MEASURE
↓
QUALIFY
↓
STORE
↓
COMPARE
```

## Post-Closure Observation Measurement Decision

Decision shall determine whether an observation or measurement is valid, degraded, uncertain, rejected, repeated or accepted for downstream comparison.

```text
RESULT
├── VALID → USE
├── UNCERTAIN → QUALIFY / GOVERN
├── DEGRADED → COMPENSATE / LIMIT USE
├── STALE → REACQUIRE
└── INVALID → REJECT / INVESTIGATE
```

## Post-Closure Observation Measurement Accountability

Accountability shall remain explicit for collection, validation, method integrity, data quality, acceptance and material downstream use.

## Post-Closure Observation Measurement Timing

Observation timing shall reflect the rate at which the monitored condition can change and the time available to detect and respond to material deviation.

## Security Post-Closure Observation Measurement

Security observations shall support reliable measurement of relevant exposure, access, control integrity, anomalous activity and security-state indicators.

## Resilience Post-Closure Observation Measurement

Resilience observations shall support measurement of availability, recovery, capacity, dependency health, continuity and degradation.

## Compliance Post-Closure Observation Measurement

Compliance observations shall support measurement of required controls, obligations, evidence completeness and applicable compliance state.

## Data Post-Closure Observation Measurement

Data observations shall support measurement of integrity, quality, lineage, access, confidentiality, retention and authorized-use conditions.

## AI and Agent Post-Closure Observation Measurement

AI/agent observations shall support measurement of outcome quality and relevant control conditions, including authority use, policy compliance, tool use, data access, autonomy and behavioural signals.

```text
AI / AGENT OBSERVE
↓
OUTPUT + CONTROL SIGNALS
↓
VALIDATE
↓
MEASURE / QUALIFY
```

## Post-Closure Observation Measurement Failure

Failure includes missing data, invalid source, stale values, broken instrumentation, method drift, transformation error, unbounded uncertainty or measurement results that cannot support the intended decision.

```text
MEASUREMENT FAILURE
↓
DECISION STILL SAFE?
├── YES → LIMIT / QUALIFY / COMPENSATE
└── NO → STOP USE / ESCALATE / REACQUIRE
```

## Post-Closure Observation Measurement Independence

Independent validation may be required where measurements are high consequence, disputed, easily manipulated or controlled by an interested party.

## Post-Closure Observation Measurement Review and Learning

Reviews shall identify recurring data-quality defects, method drift, measurement bias, false positives, false negatives, blind spots, stale observations and ineffective collection methods.

## Observation and Measurement Determination Model
```text
MONITORING ACTIVE
↓
OBSERVATION DUE
↓
DATA ACQUIRED
↓
PROVENANCE VALID?
├── NO → REJECT / INVESTIGATE
└── YES
     ↓
QUALITY ACCEPTABLE?
├── NO → DEGRADED / COMPENSATE
└── YES
     ↓
MEASUREMENT METHOD VALID?
├── NO → REPEAT / CORRECT
└── YES
     ↓
RESULT PRODUCED
↓
UNCERTAINTY / CONFIDENCE ASSESSED
↓
RESULT ACCEPTED
↓
COMPARE AGAINST BASELINE / CRITERIA
```

## Observation Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Expected | Observation is due | Acquire |
| Scheduled | Observation scheduled | Acquire |
| Acquiring | Data collection underway | Complete |
| Observed | Raw observation obtained | Validate |
| Validating | Quality checks underway | Complete validation |
| Valid | Suitable for intended use | Measure / compare |
| Degraded | Quality limitation exists | Qualify / compensate |
| Invalid | Evidence cannot support use | Reject / investigate |
| Missing | No observation obtained | Reacquire / escalate |
| Stale | Observation too old | Reacquire / qualify |
| Measured | Value / state determined | Compare |
| Uncertain | Material uncertainty remains | Qualify / govern |
| Rejected | Result not accepted | Investigate / repeat |
| Repeated | New observation obtained | Reassess |
| Accepted | Result approved for downstream use | Compare / act |

## Observation and Measurement Record
| Field | Required |
|---|---|
| Observation ID | Yes |
| Condition ID | Yes |
| Monitoring ID | Yes |
| Baseline ID | Yes |
| Source | Yes |
| Provenance | Where material |
| Timestamp | Yes |
| Method Version | Yes |
| Quality Result | Yes |
| Measurement Unit / Scale | Where applicable |
| Result | Yes |
| Uncertainty / Confidence | Where material |
| Attribution | Yes |
| Acceptance | Yes |
| Downstream Use | Where material |

## Raw Observation vs Derived Measurement
Where a measurement is derived from raw observations, the relationship shall remain traceable.

```text
RAW OBSERVATION
↓
TRANSFORMATION
↓
DERIVED MEASUREMENT
↓
DECISION
```

## Provenance
Material observations and measurements shall retain sufficient provenance to establish where the information originated and what transformations occurred before use.

## Timestamp Integrity
Where timing affects interpretation, observation time shall not be replaced by processing time without preserving both.

## Data Quality
Data quality shall consider, as relevant, completeness, accuracy, consistency, validity, timeliness, availability and provenance.

## Measurement Uncertainty
Where uncertainty can materially affect a decision, the uncertainty shall be represented and considered rather than hidden.

```text
MEASURED VALUE
+
UNCERTAINTY / CONFIDENCE
↓
GOVERNED INTERPRETATION
```

## Stale Measurements
A previously valid measurement may become invalid for the current decision if it is older than the allowed observation window.

## Missing Measurements
Missing observations shall be explicitly represented. A missing measurement shall never silently become zero, normal, unchanged or healthy unless that mapping is explicitly governed and valid.

## Method Changes
Changes to measurement method, instrumentation, calculation logic or data transformation can change comparability. Such changes shall be versioned and governed.

## Repeatability
Where repeated measurements are used, the architecture shall preserve individual observations and not retain only the preferred result.

## Manual Measurements
Manual observations remain governed evidence and shall be attributable to the person, role or process performing them.

## Automated Measurements
Automated measurement shall preserve sufficient provenance to identify the source system, algorithm or process where material.

## AI-Derived Measurements
AI-generated or AI-assisted measurements shall be identified as such where material, including the model or method version and relevant uncertainty or confidence limitations.

## Measurement Anti-Gaming
Measurements shall not be altered, filtered, sampled or transformed solely to hide deviation or improve apparent post-closure performance.

## Relationship to Comparison
RG-097 produces qualified observations and measurements. The next architecture layer uses those results to perform controlled comparison against baseline and required state.

```text
OBSERVE
↓
MEASURE
↓
QUALIFY
↓
COMPARE
↓
DEVIATION DETERMINATION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure observation and measurement layer beneath monitoring activation and baseline control and above comparison, deviation detection, revalidation, reacceptance, reliance restoration and regression determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Observation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → ASSESSMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → TRANSITION → MONITORING ACTIVATION → BASELINE → MANDATORY OBSERVATION AND MEASUREMENT → COMPARISON → DEVIATION DETECTION → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REGRESSION → REOPENING
```

## Complete Observation Chain
```text
BASELINE → ACTIVATE MONITORING → OBSERVE → ACQUIRE DATA → VALIDATE PROVENANCE → MEASURE → QUALIFY UNCERTAINTY → ACCEPT RESULT → COMPARE → DETECT DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → RESPOND → ESCALATE → EXECUTE → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → REVALIDATE → REACCEPT → RESTORE RELIANCE → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-098` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Comparison and Deviation Determination

## Final Principle
EA-IMETA SHALL REQUIRE POST-CLOSURE OBSERVATIONS AND MEASUREMENTS TO BE VALIDATED FOR PROVENANCE, QUALITY, TIMING, METHOD, UNCERTAINTY AND FITNESS FOR PURPOSE BEFORE THEY ARE USED FOR MATERIAL GOVERNANCE DECISIONS, SO THAT MISSING, STALE, INVALID OR MANIPULATED MEASUREMENTS CANNOT BE MISTAKEN FOR EVIDENCE OF A HEALTHY OR STABLE POST-CLOSURE STATE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-OBSERVATION-AND-MEASUREMENT-CONTROL-01
