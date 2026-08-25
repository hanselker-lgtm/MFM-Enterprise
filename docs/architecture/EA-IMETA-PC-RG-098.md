# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-098`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-098` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Comparison and Deviation Determination |
| Parent | EA-IMETA-PC-RG-097 — Mandatory Post-Closure Observation and Measurement Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory comparison and deviation-determination layer that evaluates qualified post-closure observations and measurements against the approved baseline, required state and applicable criteria, and determines whether a material deviation exists.

## Core Principle
Comparison is the controlled act of evaluating a qualified current state against an approved reference. Deviation determination is the governed conclusion that the difference is absent, immaterial, material, uncertain or otherwise requires further assessment. A raw difference shall not automatically be treated as a material deviation.

```text
QUALIFIED OBSERVATION / MEASUREMENT
      ↓
REFERENCE VALID?
├── NO → REFERENCE GAP / RECONSTRUCT / ESCALATE
└── YES
     ↓
COMPARISON METHOD VALID?
├── NO → CORRECT / REPEAT
└── YES
     ↓
CURRENT STATE vs REQUIRED / BASELINE STATE
     ↓
DIFFERENCE DETECTED?
├── NO → NO DEVIATION DETERMINED
└── YES
     ↓
DIFFERENCE VALID + MATERIAL?
├── NO → IMMATERIAL / MONITOR
├── UNCERTAIN → ASSESS / GATHER EVIDENCE
└── YES → MATERIAL DEVIATION
     ↓
CLASSIFY / DETERMINE CONSEQUENCE / ALERT
```

## Comparison and Deviation Quality Test
```text
QUALIFIED CURRENT OBSERVATION
+
VALID REFERENCE
+
VALID COMPARISON METHOD
+
COMMON SEMANTICS / UNITS
+
DEFINED TOLERANCE / CRITERIA
+
TIME CONTEXT
+
UNCERTAINTY CONSIDERED
+
TRACEABLE RESULT
=
VALID GOVERNED DEVIATION DETERMINATION
```

## Observation vs Measurement vs Comparison vs Deviation
```text
OBSERVATION
→ WHAT IS OBSERVED?

MEASUREMENT
→ WHAT VALUE / STATE DOES THE EVIDENCE SUPPORT?

COMPARISON
→ HOW DOES CURRENT STATE DIFFER FROM REFERENCE?

DEVIATION DETERMINATION
→ IS THAT DIFFERENCE GOVERNED AS A DEVIATION?
```

## Comparison and Deviation State Model
```text
PENDING
REFERENCE INVALID
READY
COMPARING
NO DIFFERENCE
IMMATERIAL DIFFERENCE
POTENTIAL DEVIATION
UNCERTAIN
MATERIAL DEVIATION
DETERMINATION ACCEPTED
REQUIRES CLASSIFICATION
REQUIRES ESCALATION
REASSESSMENT REQUIRED
```

## Comparison and Deviation Invariants

```text
COMPARISON SHALL USE AN APPROVED AND IDENTIFIABLE REFERENCE
```

```text
REFERENCE AND CURRENT STATE SHALL USE COMPATIBLE SEMANTICS, UNITS AND SCOPE
```

```text
COMPARISON METHOD SHALL BE APPROPRIATE TO THE GOVERNED CONDITION
```

```text
TOLERANCES AND ACCEPTANCE CRITERIA SHALL BE EXPLICIT
```

```text
TIME CONTEXT SHALL BE CONSIDERED WHERE CHANGE OVER TIME MATTERS
```

```text
UNCERTAINTY SHALL BE CONSIDERED BEFORE DECLARING A MATERIAL DEVIATION
```

```text
A DIFFERENCE SHALL NOT AUTOMATICALLY CONSTITUTE A MATERIAL DEVIATION
```

```text
ABSENCE OF A DETECTED DIFFERENCE SHALL NOT OVERRIDE KNOWN OBSERVABILITY GAPS
```

```text
REFERENCE CHANGES SHALL NOT SILENTLY ERASE HISTORICAL COMPARABILITY
```

```text
COMPARISON RESULTS SHALL BE TRACEABLE TO SOURCE OBSERVATIONS AND MEASUREMENTS
```

```text
MATERIAL DEVIATIONS SHALL ENTER THE APPLICABLE CLASSIFICATION AND CONSEQUENCE PATH
```

```text
UNCERTAIN DEVIATIONS SHALL REMAIN UNCERTAIN UNTIL SUFFICIENT EVIDENCE EXISTS
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE DEVIATIONS SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT COMPARISON SHALL CONSIDER OUTCOME AND CONTROL-STATE DIFFERENCES
```

```text
COMPARISON LOGIC SHALL BE PROTECTED AGAINST MANIPULATION OR METRIC GAMING
```

```text
DEVIATION HISTORY SHALL BE PRESERVED FOR REGRESSION, REVALIDATION AND LEARNING
```

## 1. Comparison Domain — Post-Closure Comparison Deviation Governance

**Control family:** `PCCD-001`

The Post-Closure Comparison Deviation Governance domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-001-01` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-02` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-03` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-04` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-05` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-06` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-001-07` — Establish and maintain the post-closure comparison deviation governance control.
- `PCCD-001-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 2. Comparison Domain — Post-Closure Comparison Deviation Objective

**Control family:** `PCCD-002`

The Post-Closure Comparison Deviation Objective domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-002-01` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-02` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-03` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-04` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-05` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-06` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-002-07` — Establish and maintain the post-closure comparison deviation objective control.
- `PCCD-002-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 3. Comparison Domain — Post-Closure Comparison Deviation Definition

**Control family:** `PCCD-003`

The Post-Closure Comparison Deviation Definition domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-003-01` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-02` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-03` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-04` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-05` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-06` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-003-07` — Establish and maintain the post-closure comparison deviation definition control.
- `PCCD-003-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 4. Comparison Domain — Post-Closure Comparison Deviation Scope

**Control family:** `PCCD-004`

The Post-Closure Comparison Deviation Scope domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-004-01` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-02` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-03` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-04` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-05` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-06` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-004-07` — Establish and maintain the post-closure comparison deviation scope control.
- `PCCD-004-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 5. Comparison Domain — Post-Closure Comparison Deviation Authority

**Control family:** `PCCD-005`

The Post-Closure Comparison Deviation Authority domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-005-01` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-02` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-03` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-04` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-05` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-06` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-005-07` — Establish and maintain the post-closure comparison deviation authority control.
- `PCCD-005-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 6. Comparison Domain — Post-Closure Comparison Deviation Criteria

**Control family:** `PCCD-006`

The Post-Closure Comparison Deviation Criteria domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-006-01` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-02` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-03` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-04` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-05` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-06` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-006-07` — Establish and maintain the post-closure comparison deviation criteria control.
- `PCCD-006-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 7. Comparison Domain — Post-Closure Comparison Deviation Preconditions

**Control family:** `PCCD-007`

The Post-Closure Comparison Deviation Preconditions domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-007-01` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-02` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-03` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-04` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-05` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-06` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-007-07` — Establish and maintain the post-closure comparison deviation preconditions control.
- `PCCD-007-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 8. Comparison Domain — Post-Closure Comparison Deviation Evidence

**Control family:** `PCCD-008`

The Post-Closure Comparison Deviation Evidence domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-008-01` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-02` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-03` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-04` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-05` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-06` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-008-07` — Establish and maintain the post-closure comparison deviation evidence control.
- `PCCD-008-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 9. Comparison Domain — Post-Closure Comparison Deviation Method

**Control family:** `PCCD-009`

The Post-Closure Comparison Deviation Method domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-009-01` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-02` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-03` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-04` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-05` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-06` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-009-07` — Establish and maintain the post-closure comparison deviation method control.
- `PCCD-009-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 10. Comparison Domain — Post-Closure Comparison Deviation Decision

**Control family:** `PCCD-010`

The Post-Closure Comparison Deviation Decision domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-010-01` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-02` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-03` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-04` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-05` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-06` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-010-07` — Establish and maintain the post-closure comparison deviation decision control.
- `PCCD-010-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 11. Comparison Domain — Post-Closure Comparison Deviation Accountability

**Control family:** `PCCD-011`

The Post-Closure Comparison Deviation Accountability domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-011-01` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-02` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-03` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-04` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-05` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-06` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-011-07` — Establish and maintain the post-closure comparison deviation accountability control.
- `PCCD-011-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 12. Comparison Domain — Post-Closure Comparison Deviation Timing

**Control family:** `PCCD-012`

The Post-Closure Comparison Deviation Timing domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-012-01` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-02` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-03` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-04` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-05` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-06` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-012-07` — Establish and maintain the post-closure comparison deviation timing control.
- `PCCD-012-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 13. Comparison Domain — Security Post-Closure Comparison Deviation

**Control family:** `PCCD-013`

The Security Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-013-01` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-02` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-03` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-04` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-05` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-06` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-013-07` — Establish and maintain the security post-closure comparison deviation control.
- `PCCD-013-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 14. Comparison Domain — Resilience Post-Closure Comparison Deviation

**Control family:** `PCCD-014`

The Resilience Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-014-01` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-02` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-03` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-04` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-05` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-06` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-014-07` — Establish and maintain the resilience post-closure comparison deviation control.
- `PCCD-014-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 15. Comparison Domain — Compliance Post-Closure Comparison Deviation

**Control family:** `PCCD-015`

The Compliance Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-015-01` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-02` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-03` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-04` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-05` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-06` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-015-07` — Establish and maintain the compliance post-closure comparison deviation control.
- `PCCD-015-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 16. Comparison Domain — Data Post-Closure Comparison Deviation

**Control family:** `PCCD-016`

The Data Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-016-01` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-02` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-03` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-04` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-05` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-06` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-016-07` — Establish and maintain the data post-closure comparison deviation control.
- `PCCD-016-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 17. Comparison Domain — AI and Agent Post-Closure Comparison Deviation

**Control family:** `PCCD-017`

The AI and Agent Post-Closure Comparison Deviation domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-017-01` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-02` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-03` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-04` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-05` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-06` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-017-07` — Establish and maintain the ai and agent post-closure comparison deviation control.
- `PCCD-017-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 18. Comparison Domain — Post-Closure Comparison Deviation Failure

**Control family:** `PCCD-018`

The Post-Closure Comparison Deviation Failure domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-018-01` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-02` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-03` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-04` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-05` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-06` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-018-07` — Establish and maintain the post-closure comparison deviation failure control.
- `PCCD-018-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 19. Comparison Domain — Post-Closure Comparison Deviation Independence

**Control family:** `PCCD-019`

The Post-Closure Comparison Deviation Independence domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-019-01` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-02` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-03` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-04` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-05` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-06` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-019-07` — Establish and maintain the post-closure comparison deviation independence control.
- `PCCD-019-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## 20. Comparison Domain — Post-Closure Comparison Deviation Review and Learning

**Control family:** `PCCD-020`

The Post-Closure Comparison Deviation Review and Learning domain establishes governed mandatory comparison and deviation-determination requirements.

### Required controls
- `PCCD-020-01` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-01-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-02` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-02-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-03` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-03-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-04` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-04-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-05` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-05-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-06` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-06-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.
- `PCCD-020-07` — Establish and maintain the post-closure comparison deviation review and learning control.
- `PCCD-020-07-E` — Preserve current observation, reference, method, tolerance, timing, uncertainty, difference, determination and downstream-action traceability.

```text
CURRENT STATE → REFERENCE → COMPARE → QUALIFY → DETERMINE
```

## Post-Closure Comparison Deviation Structure

| Element | Required definition |
|---|---|
| Current State | Qualified current observation / measurement |
| Reference | Approved baseline / required state |
| Scope | Comparable population / condition |
| Method | Comparison logic |
| Criteria | Tolerance / threshold |
| Time Context | Relevant observation period |
| Uncertainty | Measurement / comparison uncertainty |
| Difference | Calculated or assessed variance |
| Determination | Governed deviation result |

## Post-Closure Comparison Deviation Objective

Determine whether the current post-closure state remains within the required and approved reference condition or has developed a material deviation requiring further governance.

## Post-Closure Comparison Deviation Definition

Comparison is the controlled evaluation of current state against a valid reference. Deviation determination is the authorized conclusion about the significance and governance treatment of the observed difference.

## Post-Closure Comparison Deviation Scope

Scope shall identify the condition, dimensions, systems, services, controls, data, populations, time windows and dependencies included in the comparison.

## Post-Closure Comparison Deviation Authority

Authority shall define who approves comparison logic, resolves ambiguous differences, accepts immaterial deviation, determines material deviation and triggers escalation.

## Post-Closure Comparison Deviation Criteria

Criteria shall define reference, tolerance, threshold, materiality, timing, uncertainty, persistence and consequence relevance.

```text
CURRENT STATE
↓
VALID REFERENCE?
├── NO → REFERENCE GAP
└── YES
     ↓
COMPARISON VALID?
├── NO → CORRECT / REPEAT
└── YES
     ↓
DIFFERENCE?
├── NO → NO DEVIATION
└── YES
     ↓
WITHIN TOLERANCE?
├── YES → IMMATERIAL / MONITOR
└── NO
     ↓
UNCERTAINTY RESOLVED?
├── NO → UNCERTAIN / ASSESS
└── YES → MATERIAL DEVIATION
```

## Post-Closure Comparison Deviation Preconditions

Preconditions include valid observations, valid reference, compatible units and semantics, approved comparison method, criteria, time context and sufficient data quality.

## Post-Closure Comparison Deviation Evidence

Evidence shall preserve source observations, measurements, reference version, comparison method, calculation or reasoning, tolerance, uncertainty, result and determination.

## Post-Closure Comparison Deviation Method

Methods may include threshold comparison, baseline comparison, trend comparison, control-state comparison, statistical comparison, rule-based comparison and expert assessment.

```text
CURRENT
↓
REFERENCE
↓
NORMALIZE IF REQUIRED
↓
COMPARE
↓
APPLY TOLERANCE / UNCERTAINTY
↓
DETERMINE DEVIATION
```

## Post-Closure Comparison Deviation Decision

Decision shall determine no deviation, immaterial difference, potential deviation, uncertain deviation or material deviation and identify the required downstream path.

```text
COMPARISON RESULT
├── NO DIFFERENCE → CONTINUE MONITORING
├── IMMATERIAL → MONITOR / RECORD
├── UNCERTAIN → ASSESS / REPEAT
└── MATERIAL → CLASSIFY / ESCALATE / RESPOND
```

## Post-Closure Comparison Deviation Accountability

Accountability shall remain explicit for reference validity, comparison logic, materiality interpretation and the resulting deviation determination.

## Post-Closure Comparison Deviation Timing

Comparison timing shall reflect how quickly the condition can change and how long a material deviation may remain undetected before consequence increases.

## Security Post-Closure Comparison Deviation

Security comparison shall evaluate current exposure, access, control integrity, anomalous activity and relevant security-state measures against approved reference conditions.

## Resilience Post-Closure Comparison Deviation

Resilience comparison shall evaluate current availability, recovery capability, capacity, dependency health and continuity against required and baseline conditions.

## Compliance Post-Closure Comparison Deviation

Compliance comparison shall evaluate current control and obligation state against applicable requirements, approved controls and accepted compliance criteria.

## Data Post-Closure Comparison Deviation

Data comparison shall evaluate integrity, quality, lineage, access, confidentiality, retention and authorized-use conditions against the required reference state.

## AI and Agent Post-Closure Comparison Deviation

AI/agent comparison shall evaluate both outcome and control-state differences, including authority, policy, tool use, data access, autonomy and behavioural conditions.

```text
AI / AGENT CURRENT STATE
vs
APPROVED BASELINE / REQUIRED STATE
↓
OUTCOME DIFFERENCE?
+
CONTROL DIFFERENCE?
↓
DEVIATION DETERMINATION
```

## Post-Closure Comparison Deviation Failure

Failure includes invalid reference, incompatible semantics, incorrect comparison logic, hidden tolerance changes, insufficient evidence, uncertainty ignored or material differences suppressed.

```text
COMPARISON FAILURE
↓
DEVIATION RESULT TRUSTWORTHY?
├── YES → RETAIN WITH QUALIFICATION
└── NO → REPEAT / CORRECT / ESCALATE
```

## Post-Closure Comparison Deviation Independence

Independent validation may be required where comparison logic materially affects reliance, acceptance, compliance, security posture or high-consequence decisions.

## Post-Closure Comparison Deviation Review and Learning

Reviews shall identify recurring comparison errors, baseline drift, threshold weaknesses, false positives, false negatives, hidden tolerance changes and systemic regression patterns.

## Comparison and Deviation Determination Model
```text
QUALIFIED CURRENT STATE
↓
VALID REFERENCE?
├── NO → REFERENCE GAP / RECONSTRUCT / ESCALATE
└── YES
     ↓
COMPARISON METHOD VALID?
├── NO → CORRECT / REPEAT
└── YES
     ↓
COMMON SCOPE / UNITS / SEMANTICS?
├── NO → NORMALIZE / CORRECT
└── YES
     ↓
DIFFERENCE DETECTED?
├── NO → NO DEVIATION DETERMINED
└── YES
     ↓
WITHIN ACCEPTED TOLERANCE?
├── YES → IMMATERIAL / MONITOR
└── NO
     ↓
UNCERTAINTY MATERIAL?
├── YES → UNCERTAIN / ASSESS
└── NO → MATERIAL DEVIATION
     ↓
CLASSIFY / DETERMINE CONSEQUENCE / ALERT
```

## Deviation Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Pending | Comparison not complete | Complete comparison |
| Reference Invalid | Reference cannot support comparison | Revalidate / reconstruct |
| Ready | Preconditions satisfied | Compare |
| Comparing | Comparison underway | Complete |
| No Difference | Current state within required condition | Continue monitoring |
| Immaterial Difference | Difference below materiality | Record / monitor |
| Potential Deviation | Difference detected but not yet qualified | Assess |
| Uncertain | Evidence / uncertainty prevents determination | Gather / repeat |
| Material Deviation | Governed deviation confirmed | Classify / escalate |
| Determination Accepted | Result authorized | Proceed |
| Requires Classification | Material deviation awaits consequence classification | Classify |
| Requires Escalation | Decision exceeds current authority | Escalate |
| Reassessment Required | New evidence invalidates comparison | Reassess |

## Comparison Record
| Field | Required |
|---|---|
| Comparison ID | Yes |
| Condition ID | Yes |
| Monitoring ID | Yes |
| Current Observation Reference | Yes |
| Measurement Reference | Where applicable |
| Baseline ID / Version | Yes |
| Required State | Where applicable |
| Comparison Method Version | Yes |
| Scope | Yes |
| Time Window | Yes |
| Tolerance / Threshold | Yes |
| Uncertainty | Where material |
| Difference | Yes |
| Determination | Yes |
| Authority | Yes |
| Downstream Action | Where applicable |

## Reference Integrity
A comparison is only as valid as its reference. The reference shall be identifiable, approved, versioned and appropriate to the current condition.

## Required State vs Historical Baseline
Where a historical baseline differs from the current required state, both shall be preserved. Comparison shall use the applicable governed reference without erasing the historical baseline.

```text
HISTORICAL BASELINE
+
CURRENT REQUIRED STATE
+
CURRENT OBSERVATION
↓
GOVERNED COMPARISON
```

## Tolerance
Tolerance defines the permitted difference before a condition becomes material. Tolerance shall not be silently widened to avoid deviation classification.

## Materiality
Materiality shall consider consequence, persistence, scope, uncertainty, affected controls and applicable mandatory requirements rather than relying solely on numerical magnitude.

## Persistence
A small difference that persists or accumulates may become material. Comparison logic shall therefore consider time where relevant.

```text
SMALL DEVIATION
↓
PERSISTING / ACCUMULATING?
├── NO → MAY REMAIN IMMATERIAL
└── YES → REASSESS MATERIALITY
```

## Trend Comparison
Where trend matters, current state shall be evaluated against expected trajectory as well as a static baseline.

## Difference vs Deviation
A numerical or categorical difference is not automatically a governed deviation. The architecture shall distinguish the observed difference from the authorized determination of its significance.

## Uncertain Deviation
Where uncertainty prevents reliable classification, the result shall remain uncertain until sufficient evidence exists.

## Observability Limitation
A comparison showing no difference does not prove stability when monitoring coverage or observation quality is insufficient.

```text
NO DETECTED DIFFERENCE
+
OBSERVABILITY GAP
=
NO CONCLUSIVE STABILITY DETERMINATION
```

## Baseline Drift
Baseline drift shall be detected and governed. A moving reference shall not be allowed to conceal gradual deterioration.

## Comparison Method Changes
Changes to comparison logic, normalization, tolerances or classification rules shall be versioned so that historical determinations remain reproducible.

## AI and Agent Comparison
AI/agent comparison shall not be limited to output similarity. A materially changed authority, policy, tool, data or autonomy condition can constitute a deviation even where output remains acceptable.

## Comparison Anti-Gaming
Comparison logic shall not be manipulated through hidden filtering, selective sampling, denominator changes, tolerance widening or reference substitution to suppress deviation.

## Relationship to Deviation Classification
RG-098 determines whether a governed deviation exists. The next applicable layer classifies the confirmed deviation and determines its consequence.

```text
OBSERVE → MEASURE → QUALIFY → COMPARE → DEVIATION DETERMINATION → CLASSIFY → CONSEQUENCE → ALERT / RESPONSE
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure comparison and deviation-determination layer beneath observation and measurement and above deviation classification, consequence determination, alerting, revalidation, reacceptance, reliance restoration and regression determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, classification, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Deviation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → ASSESSMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → TRANSITION → MONITORING ACTIVATION → BASELINE → OBSERVATION → MEASUREMENT → MANDATORY COMPARISON → DEVIATION DETERMINATION → CLASSIFICATION → CONSEQUENCE → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REGRESSION → REOPENING
```

## Complete Comparison Chain
```text
BASELINE → ACTIVATE MONITORING → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → RESPOND → ESCALATE → EXECUTE → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → REVALIDATE → REACCEPT → RESTORE RELIANCE → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-099` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Deviation Classification and Consequence Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE COMPARISON TO USE A VALID, VERSIONED AND APPROPRIATE REFERENCE, COMPATIBLE SCOPE AND SEMANTICS, EXPLICIT TOLERANCES, RELEVANT TIME CONTEXT AND MATERIAL UNCERTAINTY CONSIDERATION, SO THAT A RAW DIFFERENCE CANNOT BE MISTAKEN FOR A MATERIAL DEVIATION AND A MOVING BASELINE OR MANIPULATED COMPARISON CANNOT HIDE REGRESSION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-COMPARISON-AND-DEVIATION-DETERMINATION-01
