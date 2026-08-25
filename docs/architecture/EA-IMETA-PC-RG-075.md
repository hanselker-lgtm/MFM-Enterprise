# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-DEVIATION-CLASSIFICATION-AND-THRESHOLD-GOVERNANCE-01

## Physical File ID
`EA-IMETA-PC-RG-075`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-075` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-DEVIATION-CLASSIFICATION-AND-THRESHOLD-GOVERNANCE-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Deviation Classification and Threshold Governance |
| Parent | EA-IMETA-PC-RG-074 — Mandatory Monitoring Comparison and Deviation Detection |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory classification and threshold-governance layer that determines the materiality, severity, persistence, confidence and required governance treatment of detected deviations.

## Core Principle
A deviation is not governed merely because it exists; it becomes actionable when its significance is classified against explicit, authorized and versioned thresholds and criteria. Thresholds shall define decision boundaries without being manipulated to conceal deterioration.

```text
DETECTED DEVIATION
      ↓
VALIDATE CLASSIFICATION INPUTS
      ↓
APPLY CURRENT THRESHOLDS + TOLERANCES
      ↓
ASSESS MAGNITUDE + DURATION + FREQUENCY + CONTEXT
      ↓
CLASSIFY MATERIALITY
├── INFORMATIONAL → CONTINUE / RECORD
├── MINOR → MONITOR / AGGREGATE
├── SIGNIFICANT → ALERT
├── MATERIAL → ALERT / ESCALATE
└── CRITICAL → IMMEDIATE GOVERNED RESPONSE
```

## Classification Quality Test
```text
VALID DEVIATION
+
CURRENT CRITERIA
+
CURRENT THRESHOLD VERSION
+
MAGNITUDE
+
PERSISTENCE
+
FREQUENCY
+
CONTEXT
+
UNCERTAINTY
+
CONSEQUENCE
=
VALID GOVERNED CLASSIFICATION
```

## Threshold Quality Test
```text
DEFINED PURPOSE
+
VALID BASELINE
+
MEASURABLE PROPERTY
+
AUTHORIZED LIMIT
+
MATERIALITY RATIONALE
+
CONTEXT
+
VERSION
+
REVIEW DATE / TRIGGER
=
VALID GOVERNED THRESHOLD
```

## Classification Status Model
```text
UNCLASSIFIED
INFORMATIONAL
MINOR
SIGNIFICANT
MATERIAL
CRITICAL
UNCERTAIN
INVALID
RECLASSIFIED
SUPERSEDED
```

## Classification and Threshold Invariants

```text
CLASSIFICATION CRITERIA SHALL BE EXPLICIT
```

```text
THRESHOLDS SHALL BE AUTHORIZED AND VERSIONED
```

```text
THRESHOLDS SHALL BE TRACEABLE TO THEIR MATERIALITY RATIONALE
```

```text
CLASSIFICATION SHALL CONSIDER MAGNITUDE, PERSISTENCE, FREQUENCY AND CONTEXT WHERE MATERIAL
```

```text
UNCERTAINTY SHALL BE VISIBLE
```

```text
CONSEQUENCE SHALL INFORM MATERIALITY WHERE REQUIRED
```

```text
THRESHOLDS SHALL NOT BE CHANGED RETROACTIVELY TO ERASE HISTORICAL REGRESSION
```

```text
CLASSIFICATION SHALL REMAIN DISTINCT FROM RESPONSE
```

```text
CRITICAL CONDITIONS SHALL HAVE DEFINED IMMEDIATE GOVERNANCE PATHS
```

```text
REPEATED LOWER-LEVEL EVENTS SHALL BE CAPABLE OF CUMULATIVE CLASSIFICATION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE THRESHOLDS SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT THRESHOLDS SHALL COVER MATERIAL AUTHORITY, POLICY, DATA, TOOL, AUTONOMY AND BEHAVIOURAL LIMITS
```

```text
THRESHOLD CHANGES SHALL CONSIDER FALSE-POSITIVE AND FALSE-NEGATIVE IMPACT
```

```text
THRESHOLD EXCEPTIONS SHALL BE EXPLICIT AND GOVERNED
```

```text
CLASSIFICATION HISTORY SHALL REMAIN TRACEABLE
```

## 1. Classification Domain — Deviation Classification Threshold Governance

**Control family:** `PCRCT-001`

The Deviation Classification Threshold Governance domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-001-01` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-02` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-03` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-04` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-05` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-06` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-001-07` — Establish and maintain the deviation classification threshold governance control.
- `PCRCT-001-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 2. Classification Domain — Deviation Classification Threshold Objective

**Control family:** `PCRCT-002`

The Deviation Classification Threshold Objective domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-002-01` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-02` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-03` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-04` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-05` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-06` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-002-07` — Establish and maintain the deviation classification threshold objective control.
- `PCRCT-002-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 3. Classification Domain — Deviation Classification Threshold Definition

**Control family:** `PCRCT-003`

The Deviation Classification Threshold Definition domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-003-01` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-02` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-03` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-04` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-05` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-06` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-003-07` — Establish and maintain the deviation classification threshold definition control.
- `PCRCT-003-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 4. Classification Domain — Deviation Classification Threshold Scope

**Control family:** `PCRCT-004`

The Deviation Classification Threshold Scope domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-004-01` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-02` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-03` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-04` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-05` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-06` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-004-07` — Establish and maintain the deviation classification threshold scope control.
- `PCRCT-004-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 5. Classification Domain — Deviation Classification Threshold Authority

**Control family:** `PCRCT-005`

The Deviation Classification Threshold Authority domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-005-01` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-02` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-03` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-04` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-05` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-06` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-005-07` — Establish and maintain the deviation classification threshold authority control.
- `PCRCT-005-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 6. Classification Domain — Deviation Classification Threshold Criteria

**Control family:** `PCRCT-006`

The Deviation Classification Threshold Criteria domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-006-01` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-02` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-03` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-04` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-05` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-06` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-006-07` — Establish and maintain the deviation classification threshold criteria control.
- `PCRCT-006-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 7. Classification Domain — Deviation Classification Threshold Preconditions

**Control family:** `PCRCT-007`

The Deviation Classification Threshold Preconditions domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-007-01` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-02` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-03` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-04` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-05` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-06` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-007-07` — Establish and maintain the deviation classification threshold preconditions control.
- `PCRCT-007-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 8. Classification Domain — Deviation Classification Threshold Evidence

**Control family:** `PCRCT-008`

The Deviation Classification Threshold Evidence domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-008-01` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-02` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-03` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-04` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-05` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-06` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-008-07` — Establish and maintain the deviation classification threshold evidence control.
- `PCRCT-008-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 9. Classification Domain — Deviation Classification Threshold Method

**Control family:** `PCRCT-009`

The Deviation Classification Threshold Method domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-009-01` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-02` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-03` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-04` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-05` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-06` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-009-07` — Establish and maintain the deviation classification threshold method control.
- `PCRCT-009-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 10. Classification Domain — Deviation Classification Threshold Decision

**Control family:** `PCRCT-010`

The Deviation Classification Threshold Decision domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-010-01` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-02` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-03` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-04` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-05` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-06` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-010-07` — Establish and maintain the deviation classification threshold decision control.
- `PCRCT-010-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 11. Classification Domain — Deviation Classification Threshold Accountability

**Control family:** `PCRCT-011`

The Deviation Classification Threshold Accountability domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-011-01` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-02` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-03` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-04` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-05` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-06` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-011-07` — Establish and maintain the deviation classification threshold accountability control.
- `PCRCT-011-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 12. Classification Domain — Deviation Classification Threshold Timing

**Control family:** `PCRCT-012`

The Deviation Classification Threshold Timing domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-012-01` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-02` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-03` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-04` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-05` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-06` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-012-07` — Establish and maintain the deviation classification threshold timing control.
- `PCRCT-012-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 13. Classification Domain — Security Deviation Classification Threshold

**Control family:** `PCRCT-013`

The Security Deviation Classification Threshold domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-013-01` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-02` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-03` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-04` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-05` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-06` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-013-07` — Establish and maintain the security deviation classification threshold control.
- `PCRCT-013-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 14. Classification Domain — Resilience Deviation Classification Threshold

**Control family:** `PCRCT-014`

The Resilience Deviation Classification Threshold domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-014-01` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-02` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-03` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-04` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-05` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-06` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-014-07` — Establish and maintain the resilience deviation classification threshold control.
- `PCRCT-014-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 15. Classification Domain — Compliance Deviation Classification Threshold

**Control family:** `PCRCT-015`

The Compliance Deviation Classification Threshold domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-015-01` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-02` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-03` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-04` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-05` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-06` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-015-07` — Establish and maintain the compliance deviation classification threshold control.
- `PCRCT-015-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 16. Classification Domain — Data Deviation Classification Threshold

**Control family:** `PCRCT-016`

The Data Deviation Classification Threshold domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-016-01` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-02` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-03` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-04` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-05` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-06` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-016-07` — Establish and maintain the data deviation classification threshold control.
- `PCRCT-016-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 17. Classification Domain — AI and Agent Deviation Classification Threshold

**Control family:** `PCRCT-017`

The AI and Agent Deviation Classification Threshold domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-017-01` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-02` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-03` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-04` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-05` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-06` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-017-07` — Establish and maintain the ai and agent deviation classification threshold control.
- `PCRCT-017-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 18. Classification Domain — Deviation Classification Threshold Failure

**Control family:** `PCRCT-018`

The Deviation Classification Threshold Failure domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-018-01` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-02` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-03` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-04` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-05` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-06` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-018-07` — Establish and maintain the deviation classification threshold failure control.
- `PCRCT-018-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 19. Classification Domain — Deviation Classification Threshold Independence

**Control family:** `PCRCT-019`

The Deviation Classification Threshold Independence domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-019-01` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-02` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-03` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-04` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-05` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-06` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-019-07` — Establish and maintain the deviation classification threshold independence control.
- `PCRCT-019-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## 20. Classification Domain — Deviation Classification Threshold Review and Learning

**Control family:** `PCRCT-020`

The Deviation Classification Threshold Review and Learning domain establishes governed mandatory classification and threshold requirements.

### Required controls
- `PCRCT-020-01` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-01-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-02` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-02-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-03` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-03-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-04` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-04-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-05` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-05-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-06` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-06-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.
- `PCRCT-020-07` — Establish and maintain the deviation classification threshold review and learning control.
- `PCRCT-020-07-E` — Preserve deviation input, threshold version, classification logic, materiality rationale, uncertainty, consequence and decision traceability.

```text
DEVIATION → CLASSIFY → ALERT / ESCALATE
```

## Deviation Classification Threshold Governance Structure

| Element | Required definition |
|---|---|
| Deviation | Detected departure from expected state |
| Threshold | Governed boundary |
| Tolerance | Permitted variation |
| Materiality | Significance of deviation |
| Classification | Assigned severity/category |
| Context | Conditions affecting classification |
| Consequence | Relevant impact |
| Version | Current rule identity |

## Deviation Classification Threshold Objective

Provide consistent, defensible and timely classification of detected deviations so that governance treatment is proportionate to actual materiality.

## Deviation Classification Threshold Definition

Classification is the governed determination of deviation significance. Threshold governance is the controlled establishment, approval, versioning and review of the boundaries used for that determination.

## Deviation Classification Threshold Scope

Scope shall identify systems, services, users, data, decisions, dependencies, environments, consumers and boundaries covered by classification rules.

## Deviation Classification Threshold Authority

Authority shall define who may create, approve, modify, suspend, challenge or retire thresholds and classification rules.

## Deviation Classification Threshold Criteria

Criteria shall distinguish informational, minor, significant, material, critical, uncertain and invalid conditions.

```text
DEVIATION
↓
VALID INPUT?
├── NO → INVALID / UNKNOWN
└── YES
     ↓
APPLY CURRENT THRESHOLD
     ↓
ASSESS MAGNITUDE + PERSISTENCE + CONTEXT
     ↓
CLASSIFY
```

## Deviation Classification Threshold Preconditions

Preconditions include validated deviation input, active threshold version, defined materiality criteria, consequence context, uncertainty treatment and authority.

## Deviation Classification Threshold Evidence

Evidence shall preserve the deviation, baseline, threshold version, values, context, classification logic, rationale and resulting classification.

## Deviation Classification Threshold Method

Methods may include deterministic thresholds, tolerance bands, weighted scoring, risk matrices, persistence rules, aggregation rules and statistical classification.

```text
INPUT
↓
NORMALIZE
↓
APPLY RULES
↓
ASSESS CONTEXT
↓
CLASSIFY
```

## Deviation Classification Threshold Decision

Classification shall determine the governance severity; subsequent response, alerting and escalation shall remain separate controlled decisions.

```text
CLASSIFICATION
├── INFORMATIONAL → RECORD
├── MINOR → MONITOR
├── SIGNIFICANT → ALERT
├── MATERIAL → ALERT / ESCALATE
└── CRITICAL → IMMEDIATE GOVERNED RESPONSE
```

## Deviation Classification Threshold Accountability

Accountability shall remain explicit for threshold ownership, classification integrity, exceptions, changes and historical traceability.

## Deviation Classification Threshold Timing

Threshold evaluation shall occur promptly enough to meet the required detection and response latency for the classified condition.

## Security Deviation Classification Threshold

Classify security deviations using material exposure, authorization impact, boundary breach, control degradation and threat context.

## Resilience Deviation Classification Threshold

Classify resilience deviations using availability, recovery, capacity, continuity, dependency and degradation context.

## Compliance Deviation Classification Threshold

Classify compliance deviations using obligation materiality, control failure, evidence deficiency, reporting impact and policy context.

## Data Deviation Classification Threshold

Classify data deviations using integrity, quality, completeness, timeliness, access, lineage, retention and downstream impact.

## AI and Agent Deviation Classification Threshold

Classify AI/agent deviations using authority breach, policy deviation, unsafe tool use, data-boundary violation, autonomy drift, behavioural drift and material outcome impact.

```text
AI / AGENT DEVIATION
↓
AUTHORITY + POLICY + DATA + TOOLS
↓
AUTONOMY + BEHAVIOUR + OUTCOME
↓
CLASSIFY MATERIALITY
```

## Deviation Classification Threshold Failure

Failure includes stale threshold, ambiguous criteria, missing context, excessive uncertainty, incompatible scale, threshold conflict or inability to classify reliably.

```text
CLASSIFICATION FAILURE
↓
RELIABLE SEVERITY?
├── YES → CONTROLLED UNCERTAINTY
└── NO → UNKNOWN / ESCALATE GOVERNANCE GAP
```

## Deviation Classification Threshold Independence

Material threshold design and critical classifications shall receive independent challenge where required to reduce bias and normalization of deviance.

## Deviation Classification Threshold Review and Learning

Reviews shall examine false positives, false negatives, threshold drift, classification inconsistency, recurring exceptions and evidence that thresholds no longer represent materiality.

## Classification Determination Model
```text
DETECTED DEVIATION
↓
CURRENT THRESHOLD VERSION?
├── NO → HOLD / GOVERNANCE GAP
└── YES
     ↓
INPUT VALID + CONTEXT SUFFICIENT?
├── NO → UNKNOWN / INVALID
└── YES
     ↓
MAGNITUDE + PERSISTENCE + FREQUENCY + CONSEQUENCE
↓
CLASSIFY MATERIALITY
↓
TRIGGER GOVERNED NEXT STEP
```

## Classification Outcome Matrix
| Classification | Meaning | Required treatment |
|---|---|---|
| Informational | No material concern | Record / continue |
| Minor | Limited deviation | Monitor / aggregate |
| Significant | Material concern requiring attention | Alert |
| Material | Material regression or control concern | Alert / escalate |
| Critical | Immediate high-consequence condition | Immediate governed response |
| Uncertain | Insufficient confidence | Investigate / govern uncertainty |
| Invalid | Classification input not trustworthy | Correct / repeat |

## Threshold Record
| Field | Required |
|---|---|
| Threshold ID | Yes |
| Version | Yes |
| Property | Yes |
| Unit / Scale | Where applicable |
| Boundary | Yes |
| Tolerance | Where applicable |
| Materiality Rationale | Yes |
| Context | Yes |
| Owner | Yes |
| Authority | Yes |
| Effective Time | Yes |
| Review Trigger | Yes |

## Classification Record
| Field | Required |
|---|---|
| Classification ID | Yes |
| Deviation ID | Yes |
| Threshold Version | Yes |
| Classification Method | Yes |
| Inputs | Yes |
| Context | Yes |
| Uncertainty | Where applicable |
| Consequence | Where applicable |
| Result | Yes |
| Rationale | Yes |
| Timestamp | Yes |

## Threshold vs Tolerance
A threshold defines a decision boundary. A tolerance defines permitted variation around expected behaviour. The two shall not be conflated.

```text
EXPECTED STATE
   ↕
TOLERANCE BAND
   ↕
THRESHOLD / MATERIALITY BOUNDARY
```

## Absolute vs Relative Thresholds
Where appropriate, thresholds may be absolute, relative, rate-based, percentage-based, trend-based or composite. The selected form shall remain explicit and justified.

## Persistence and Hysteresis
Where conditions fluctuate around a boundary, persistence or hysteresis rules may prevent unstable classification. Such rules shall be explicit and shall not delay required action where consequence warrants immediate response.

```text
THRESHOLD CROSS
↓
PERSISTENCE RULE
├── NOT MET → CONTINUE OBSERVATION
└── MET → CLASSIFY / ALERT
```

## Aggregation Rules
Repeated events shall be capable of cumulative classification where frequency, duration, combined impact or pattern makes the total condition material.

## Consequence-Aware Classification
Materiality may depend not only on measured deviation but also on consequence, affected population, dependency criticality, reversibility and time-to-impact.

## Uncertainty-Aware Classification
Where evidence uncertainty overlaps a threshold, the classification shall preserve uncertainty and may require additional observation rather than falsely selecting normal or material.

```text
RESULT + UNCERTAINTY
↓
CLEARLY NORMAL → NORMAL
CLEARLY MATERIAL → MATERIAL
OVERLAPPING BOUNDARY → UNCERTAIN / INVESTIGATE
```

## Threshold Change Control
Changes to thresholds, tolerances, classification logic, persistence, aggregation or consequence weighting shall be governed, approved, versioned and effective-dated.

```text
CURRENT THRESHOLD
↓
CHANGE PROPOSAL
↓
MATERIALITY + FALSE POSITIVE / NEGATIVE REVIEW
↓
APPROVAL
↓
NEW VERSION
```

## No Retroactive Reclassification Without Governance
Historical classifications shall not be silently rewritten because thresholds changed later. Any retrospective reclassification shall be explicit, authorized and traceable.

## Threshold Exceptions
Exceptions shall identify scope, reason, authority, duration, compensating controls and review or expiry. Permanent exceptions shall not be hidden as temporary exceptions.

## Classification Anti-Gaming
Thresholds and classification rules shall not be tuned solely to reduce alerts, avoid escalation, improve reported performance or normalize deteriorating behaviour.

## Handoff to Alerting
The classification output shall provide the alerting layer with severity, evidence, threshold version, context, persistence and materiality rationale.

```text
CLASSIFY
↓
SEVERITY + EVIDENCE + CONTEXT + THRESHOLD VERSION
↓
ALERTING
```

## Relationship to Existing Architecture
This document specializes the mandatory deviation-classification and threshold-governance layer beneath comparison and deviation detection and above alerting. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, comparison, consequence, response, effectiveness, reassessment, revalidation, reacceptance, reliance restoration, baseline establishment, monitoring, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Classification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → BASELINE → MEASUREMENT / OBSERVATION → COMPARISON → DEVIATION DETECTION → MANDATORY CLASSIFICATION → ALERTING → ESCALATION → RESOLUTION
```

## Complete Classification Chain
```text
REACCEPT → RESTORE RELIANCE → BASELINE → MEASURE / OBSERVE → COMPARE → DETECT → CLASSIFY → ALERT → ESCALATE → RESOLVE → VERIFY → REVALIDATE
```

## Next Document
`EA-IMETA-PC-RG-076` — Mandatory Regression Reliance Restoration Monitoring Alerting Trigger and Notification

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL DEVIATION TO BE CLASSIFIED AGAINST CURRENT, AUTHORIZED AND VERSIONED THRESHOLDS AND CRITERIA WITH MAGNITUDE, PERSISTENCE, FREQUENCY, CONTEXT, UNCERTAINTY AND CONSEQUENCE CONSIDERED WHERE MATERIAL, WHILE PRESERVING EXPLICIT UNKNOWN AND INVALID STATES AND PREVENTING THRESHOLD MANIPULATION FROM HIDING REGRESSION OR AVOIDING GOVERNED ALERTING AND ESCALATION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-DEVIATION-CLASSIFICATION-AND-THRESHOLD-GOVERNANCE-01
