# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-DETECTION-CONTROL-01

## Physical File ID
`EA-IMETA-PC-RG-110`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-110` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-DETECTION-CONTROL-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Detection Control |
| Parent | EA-IMETA-PC-RG-109 — Mandatory Post-Closure Reliance Restoration Monitoring Continuity Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory regression-detection layer that determines whether a previously restored, accepted and monitored state has materially deteriorated, deviated from its approved baseline, lost required control characteristics, or otherwise requires alerting, restriction, response, reassessment or reopening.

## Core Principle
Regression is a governed state transition, not merely a measurement anomaly. A material regression exists when current evidence demonstrates that a previously accepted or restored state no longer satisfies the applicable baseline, criteria, control state, threshold, reliability or reliance conditions.

```text
RESTORED / ACCEPTED STATE
        ↓
CURRENT OBSERVATION
        ↓
MEASURE / QUALIFY
        ↓
COMPARE WITH APPROVED BASELINE
        ↓
DEVIATION DETECTED?
├── NO → CONTINUE MONITORING
└── YES
     ↓
MATERIAL REGRESSION?
├── NO → RECORD / CONTINUE
└── YES
     ↓
CLASSIFY CONSEQUENCE
     ↓
ALERT / NOTIFY
     ↓
RESTRICT / RESPOND / REASSESS
     ↓
REOPEN IF REQUIRED
```

## Regression Detection Quality Test
```text
CURRENT STATE
+
VALID OBSERVATION
+
VALID MEASUREMENT
+
CURRENT BASELINE
+
EXPLICIT DEVIATION LOGIC
+
MATERIALITY CRITERIA
+
CONSEQUENCE CLASSIFICATION
+
TRACEABLE EVIDENCE
+
ACTION PATH
=
VALID GOVERNED REGRESSION DETECTION
```

## Deviation vs Regression
```text
DEVIATION
→ CURRENT STATE DIFFERS FROM EXPECTED STATE

REGRESSION
→ DEVIATION IS MATERIAL OR OTHERWISE RELEVANT
  BECAUSE A PREVIOUSLY RESTORED / ACCEPTED CONDITION
  HAS DETERIORATED OR LOST REQUIRED CHARACTERISTICS
```

## Regression Detection State Model
```text
NORMAL
OBSERVATION PENDING
DEVIATION DETECTED
DEVIATION QUALIFICATION REQUIRED
REGRESSION SUSPECTED
REGRESSION CONFIRMED
MATERIAL REGRESSION
ALERTED
RESTRICTED
RESPONSE INITIATED
REASSESSMENT REQUIRED
REOPENING REQUIRED
RECOVERY MONITORING
STABLE AFTER REGRESSION
```

## Regression Detection Invariants

```text
REGRESSION SHALL BE DETERMINED AGAINST A VALID CURRENT BASELINE OR EXPLICIT ACCEPTANCE CRITERIA
```

```text
A SINGLE NOISY OBSERVATION SHALL NOT AUTOMATICALLY BECOME MATERIAL REGRESSION WITHOUT APPLICABLE QUALIFICATION
```

```text
ABSENCE OF DATA SHALL NOT BE TREATED AS EVIDENCE OF NO REGRESSION
```

```text
MATERIALITY SHALL BE BASED ON CONSEQUENCE, CONTROL STATE, RELIANCE AND APPLICABLE CRITERIA
```

```text
REGRESSION DETECTION SHALL REMAIN LINKED TO THE RESTORED RELIANCE STATE
```

```text
DETECTION LOGIC SHALL BE VERSIONED AND TRACEABLE
```

```text
THRESHOLDS SHALL NOT BE MODIFIED TO SUPPRESS A KNOWN REGRESSION
```

```text
REGRESSION DETECTION SHALL SUPPORT FALSE-POSITIVE AND FALSE-NEGATIVE ANALYSIS
```

```text
CRITICAL REGRESSION SHALL HAVE A DIRECT ESCALATION AND RESTRICTION PATH
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE REGRESSION SHALL RECEIVE APPROPRIATE DETECTION RIGOR
```

```text
AI AND AGENT REGRESSION SHALL INCLUDE BEHAVIORAL AND CONTROL-STATE REGRESSION
```

```text
DEPENDENCY REGRESSION SHALL BE CONSIDERED WHERE A DOWNSTREAM CHANGE CAN INVALIDATE THE RESTORED STATE
```

```text
REGRESSION DETECTION SHALL PRESERVE FIRST-DETECTED TIME AND EVIDENCE
```

```text
A CONFIRMED REGRESSION SHALL REMAIN GOVERNED UNTIL RESOLVED OR EXPLICITLY ACCEPTED UNDER AUTHORITY
```

```text
REGRESSION SHALL BE CAPABLE OF TRIGGERING RESTRICTION BEFORE FULL FAILURE WHERE PRECURSOR CONDITIONS ARE MATERIAL
```

```text
REGRESSION HISTORY SHALL REMAIN TRACEABLE THROUGH RESPONSE, resolution, closure and later restoration
```

## 1. Regression Domain — Post-Closure Regression Detection Governance

**Control family:** `PCRD-001`

The Post-Closure Regression Detection Governance domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-001-01` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-02` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-03` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-04` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-05` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-06` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-001-07` — Establish and maintain the post-closure regression detection governance control.
- `PCRD-001-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 2. Regression Domain — Post-Closure Regression Detection Objective

**Control family:** `PCRD-002`

The Post-Closure Regression Detection Objective domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-002-01` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-02` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-03` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-04` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-05` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-06` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-002-07` — Establish and maintain the post-closure regression detection objective control.
- `PCRD-002-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 3. Regression Domain — Post-Closure Regression Detection Definition

**Control family:** `PCRD-003`

The Post-Closure Regression Detection Definition domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-003-01` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-02` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-03` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-04` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-05` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-06` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-003-07` — Establish and maintain the post-closure regression detection definition control.
- `PCRD-003-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 4. Regression Domain — Post-Closure Regression Detection Scope

**Control family:** `PCRD-004`

The Post-Closure Regression Detection Scope domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-004-01` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-02` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-03` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-04` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-05` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-06` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-004-07` — Establish and maintain the post-closure regression detection scope control.
- `PCRD-004-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 5. Regression Domain — Post-Closure Regression Detection Authority

**Control family:** `PCRD-005`

The Post-Closure Regression Detection Authority domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-005-01` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-02` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-03` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-04` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-05` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-06` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-005-07` — Establish and maintain the post-closure regression detection authority control.
- `PCRD-005-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 6. Regression Domain — Post-Closure Regression Detection Criteria

**Control family:** `PCRD-006`

The Post-Closure Regression Detection Criteria domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-006-01` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-02` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-03` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-04` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-05` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-06` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-006-07` — Establish and maintain the post-closure regression detection criteria control.
- `PCRD-006-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 7. Regression Domain — Post-Closure Regression Detection Preconditions

**Control family:** `PCRD-007`

The Post-Closure Regression Detection Preconditions domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-007-01` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-02` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-03` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-04` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-05` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-06` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-007-07` — Establish and maintain the post-closure regression detection preconditions control.
- `PCRD-007-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 8. Regression Domain — Post-Closure Regression Detection Evidence

**Control family:** `PCRD-008`

The Post-Closure Regression Detection Evidence domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-008-01` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-02` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-03` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-04` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-05` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-06` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-008-07` — Establish and maintain the post-closure regression detection evidence control.
- `PCRD-008-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 9. Regression Domain — Post-Closure Regression Detection Method

**Control family:** `PCRD-009`

The Post-Closure Regression Detection Method domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-009-01` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-02` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-03` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-04` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-05` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-06` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-009-07` — Establish and maintain the post-closure regression detection method control.
- `PCRD-009-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 10. Regression Domain — Post-Closure Regression Detection Decision

**Control family:** `PCRD-010`

The Post-Closure Regression Detection Decision domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-010-01` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-02` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-03` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-04` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-05` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-06` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-010-07` — Establish and maintain the post-closure regression detection decision control.
- `PCRD-010-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 11. Regression Domain — Post-Closure Regression Detection Accountability

**Control family:** `PCRD-011`

The Post-Closure Regression Detection Accountability domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-011-01` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-02` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-03` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-04` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-05` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-06` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-011-07` — Establish and maintain the post-closure regression detection accountability control.
- `PCRD-011-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 12. Regression Domain — Post-Closure Regression Detection Timing

**Control family:** `PCRD-012`

The Post-Closure Regression Detection Timing domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-012-01` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-02` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-03` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-04` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-05` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-06` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-012-07` — Establish and maintain the post-closure regression detection timing control.
- `PCRD-012-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 13. Regression Domain — Security Post-Closure Regression Detection

**Control family:** `PCRD-013`

The Security Post-Closure Regression Detection domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-013-01` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-02` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-03` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-04` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-05` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-06` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-013-07` — Establish and maintain the security post-closure regression detection control.
- `PCRD-013-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 14. Regression Domain — Resilience Post-Closure Regression Detection

**Control family:** `PCRD-014`

The Resilience Post-Closure Regression Detection domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-014-01` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-02` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-03` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-04` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-05` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-06` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-014-07` — Establish and maintain the resilience post-closure regression detection control.
- `PCRD-014-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 15. Regression Domain — Compliance Post-Closure Regression Detection

**Control family:** `PCRD-015`

The Compliance Post-Closure Regression Detection domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-015-01` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-02` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-03` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-04` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-05` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-06` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-015-07` — Establish and maintain the compliance post-closure regression detection control.
- `PCRD-015-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 16. Regression Domain — Data Post-Closure Regression Detection

**Control family:** `PCRD-016`

The Data Post-Closure Regression Detection domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-016-01` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-02` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-03` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-04` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-05` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-06` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-016-07` — Establish and maintain the data post-closure regression detection control.
- `PCRD-016-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 17. Regression Domain — AI and Agent Post-Closure Regression Detection

**Control family:** `PCRD-017`

The AI and Agent Post-Closure Regression Detection domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-017-01` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-02` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-03` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-04` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-05` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-06` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-017-07` — Establish and maintain the ai and agent post-closure regression detection control.
- `PCRD-017-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 18. Regression Domain — Post-Closure Regression Detection Failure

**Control family:** `PCRD-018`

The Post-Closure Regression Detection Failure domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-018-01` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-02` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-03` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-04` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-05` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-06` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-018-07` — Establish and maintain the post-closure regression detection failure control.
- `PCRD-018-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 19. Regression Domain — Post-Closure Regression Detection Independence

**Control family:** `PCRD-019`

The Post-Closure Regression Detection Independence domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-019-01` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-02` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-03` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-04` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-05` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-06` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-019-07` — Establish and maintain the post-closure regression detection independence control.
- `PCRD-019-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## 20. Regression Domain — Post-Closure Regression Detection Review and Learning

**Control family:** `PCRD-020`

The Post-Closure Regression Detection Review and Learning domain establishes governed mandatory regression-detection requirements.

### Required controls
- `PCRD-020-01` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-01-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-02` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-02-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-03` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-03-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-04` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-04-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-05` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-05-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-06` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-06-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.
- `PCRD-020-07` — Establish and maintain the post-closure regression detection review and learning control.
- `PCRD-020-07-E` — Preserve baseline, observation, measurement, deviation, qualification, materiality, consequence, alert, restriction, response and reopening traceability.

```text
OBSERVE → MEASURE → COMPARE → QUALIFY → DETECT → CLASSIFY → ACT
```

## Post-Closure Regression Detection Structure

| Element | Required definition |
|---|---|
| Restored State | Previously accepted/reliance-restored state |
| Baseline | Approved expected state |
| Observation | Evidence of current condition |
| Measurement | Quantified or qualified condition |
| Deviation | Difference from baseline |
| Materiality | Significance of deviation |
| Regression | Material deterioration or loss of required state |
| Consequence | Impact classification |
| Action | Alert, restrict, respond, reassess or reopen |

## Post-Closure Regression Detection Objective

Detect material deterioration early enough to prevent unjustified continued reliance, enabling timely restriction, response, reassessment or reopening.

## Post-Closure Regression Detection Definition

Regression detection is the governed determination that a previously accepted or restored state has materially departed from its approved baseline, control state, acceptance criteria or reliance conditions.

## Post-Closure Regression Detection Scope

Scope shall cover the restored reliance object, relevant controls, dependencies, data, operating conditions, thresholds, leading indicators, lagging indicators and consequence dimensions.

## Post-Closure Regression Detection Authority

Authority shall define who may classify regression, trigger restriction, escalate, suspend reliance, require reassessment or authorize continued operation under conditions.

## Post-Closure Regression Detection Criteria

Criteria shall define baseline, comparison method, tolerance, persistence, materiality, consequence and action thresholds.
```text
CURRENT STATE
↓
COMPARE
├── WITHIN BASELINE → CONTINUE
└── OUTSIDE BASELINE
     ↓
QUALIFY
     ↓
MATERIAL?
├── NO → RECORD / WATCH
└── YES → REGRESSION
     ↓
CLASSIFY → ALERT → ACT
```

## Post-Closure Regression Detection Preconditions

Preconditions include current baseline, valid data sources, measurement definitions, thresholds, materiality logic, ownership and response pathways.

## Post-Closure Regression Detection Evidence

Evidence shall preserve first observation, source, timestamp, baseline version, measurement, comparison, qualification, materiality decision, consequence and resulting action.

## Post-Closure Regression Detection Method

Methods may include threshold detection, trend analysis, statistical comparison, rule-based detection, control-state verification, scenario detection and independent assurance.
```text
OBSERVE
↓
MEASURE
↓
COMPARE
↓
QUALIFY
↓
DETECT
↓
CLASSIFY
↓
ACT
```

## Post-Closure Regression Detection Decision

Decision shall determine normal, deviation detected, regression suspected, regression confirmed, material regression, restriction, response, reassessment or reopening.

## Post-Closure Regression Detection Accountability

Accountability shall remain explicit for detection logic, materiality interpretation, classification, escalation and resulting reliance-state action.

## Post-Closure Regression Detection Timing

Detection latency shall be proportionate to consequence and the maximum tolerable period during which regression may remain undetected.

## Security Post-Closure Regression Detection

Security detection shall identify deterioration in access control, exposure, authentication, monitoring, configuration, threat posture and other material security conditions.

## Resilience Post-Closure Regression Detection

Resilience detection shall identify deterioration in availability, capacity, recovery readiness, dependencies, redundancy and fallback capability.

## Compliance Post-Closure Regression Detection

Compliance detection shall identify loss of required controls, approvals, segregation, reporting or other mandatory obligations.

## Data Post-Closure Regression Detection

Data detection shall identify deterioration in integrity, quality, freshness, lineage, confidentiality, availability or recoverability relevant to reliance.

## AI and Agent Post-Closure Regression Detection

AI/agent regression detection shall include output behavior, policy adherence, authority boundaries, tool use, data access, autonomy and human-oversight conditions.
```text
AI / AGENT
↓
OUTPUT / BEHAVIOR CHANGE
+
CONTROL-STATE CHANGE
+
AUTHORITY / TOOL / DATA CHANGE
↓
QUALIFY
↓
REGRESSION?
├── NO → CONTINUE
└── YES → RESTRICT / RESPOND / REASSESS
```

## Post-Closure Regression Detection Failure

Failure includes missed regression, false negative, stale baseline, invalid measurement, threshold suppression, delayed detection, broken alert path or incorrect materiality classification.
```text
DETECTION FAILURE
↓
REGRESSION MAY BE MATERIAL?
├── NO → CORRECT DETECTION CONTROL
└── YES → RESTRICT / ESCALATE / REASSESS
```

## Post-Closure Regression Detection Independence

Independent detection or assurance may be required where the monitored party benefits from continued reliance, where detection is contested, or where missed regression has high consequence.

## Post-Closure Regression Detection Review and Learning

Reviews shall examine missed detections, false positives, false negatives, stale baselines, weak thresholds, delayed escalation and recurring regression patterns.

## Regression Detection Determination Model
```text
RESTORED / ACCEPTED STATE
↓
CURRENT OBSERVATION
↓
MEASURE / QUALIFY
↓
BASELINE VALID?
├── NO → CORRECT / REASSESS
└── YES
     ↓
DEVIATION?
├── NO → CONTINUE MONITORING
└── YES
     ↓
MATERIAL REGRESSION?
├── NO → RECORD / WATCH
└── YES
     ↓
CLASSIFY CONSEQUENCE
     ↓
ALERT / NOTIFY
     ↓
RESTRICT / RESPOND / REASSESS
     ↓
REOPEN IF REQUIRED
```

## Regression Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Normal | State remains within accepted baseline | Continue monitoring |
| Observation Pending | Current state not yet sufficiently observed | Obtain evidence |
| Deviation Detected | State differs from baseline | Qualify |
| Deviation Qualification Required | Materiality not yet established | Assess |
| Regression Suspected | Evidence indicates possible deterioration | Investigate / control |
| Regression Confirmed | Deterioration established | Govern response |
| Material Regression | Consequence exceeds required tolerance | Alert / restrict / respond |
| Restricted | Reliance or operation limited | Maintain restrictions |
| Response Initiated | Corrective response active | Execute / verify |
| Reassessment Required | Acceptance basis changed | Reassess |
| Reopening Required | Closed lifecycle no longer valid | Reopen |
| Recovery Monitoring | Restored state under heightened observation | Monitor |
| Stable After Regression | Recovery sustained | Continue governed monitoring |

## Regression Detection Record
| Field | Required |
|---|---|
| Regression ID | Yes |
| Reliance ID | Yes |
| Monitoring ID | Yes |
| First Detection Time | Yes |
| Observation Source | Yes |
| Baseline Version | Yes |
| Measurement | Yes |
| Deviation | Yes |
| Materiality | Yes |
| Consequence | Yes |
| Classification | Yes |
| Alert | Where applicable |
| Restriction | Where applicable |
| Response | Where applicable |
| Evidence | Yes |
| Decision Authority | Yes |
| Reassessment / Reopening | Where applicable |

## Deviation Is Not Automatically Regression
A deviation is a factual difference from the expected state. Regression requires qualification against materiality, consequence, control requirements or reliance conditions.
```text
DEVIATION
≠
AUTOMATIC REGRESSION
```

## Absence of Evidence
Absence of valid observation shall not be treated as evidence that the restored state remains normal.
```text
NO DATA
≠
NO REGRESSION
```

## Baseline Validity
Regression detection depends on a valid baseline. If the baseline is obsolete, corrupted, incomplete or no longer applicable, the detection decision shall be qualified and the reliance state reassessed where necessary.

## Threshold Integrity
Thresholds shall be governed and versioned. Threshold changes shall require explicit authority and shall never be used retrospectively to erase a previously detected material regression.

## Leading Indicators
Where feasible, detection shall include leading indicators capable of identifying deterioration before full failure occurs.

## Lagging Indicators
Lagging indicators may confirm realized deterioration but shall not be the sole detection mechanism where earlier warning is reasonably achievable and material consequence warrants it.

## Persistence and Hysteresis
Where measurement noise could create unstable decisions, persistence rules or hysteresis may be used, provided they do not delay action beyond acceptable consequence limits.

## False Positives and False Negatives
Detection controls shall evaluate both false positives and false negatives. A low alert volume does not prove effective detection.

## Critical Regression
Critical regression shall have a direct path from detection to authority, alerting and restriction without unnecessary intermediate delay.

## Dependency Regression
Regression may originate outside the directly monitored component. Material dependency changes shall therefore be capable of invalidating the restored state.

## AI and Agent Regression
AI/agent regression shall consider drift in behavior, policy, authority, tool permissions, data boundaries, autonomy and human oversight—not merely output accuracy.

## Regression Anti-Gaming
Detection logic, baselines, thresholds and monitoring sources shall not be manipulated to suppress known regression.

## Relationship to Response
Confirmed material regression feeds the existing alert, notification, acknowledgement, response initiation and authority-transfer chain.
```text
REGRESSION
↓
CLASSIFY
↓
CONSEQUENCE
↓
ALERT
↓
NOTIFY
↓
ACKNOWLEDGE
↓
RESPONSE
```

## Relationship to Reopening
Where regression invalidates a prior resolution, closure or reacceptance basis, the governed lifecycle shall support reopening rather than silently continuing under an invalid state.
```text
REGRESSION
↓
REASSESS
↓
REOPEN IF REQUIRED
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure regression-detection layer beneath monitoring continuity and above alerting, response, reassessment and reopening. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Regression Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REACCEPTANCE → RELIANCE RESTORATION → MONITORING CONTINUITY → MANDATORY REGRESSION DETECTION → REOPENING
```

## Complete Regression Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → REACCEPT → RESTORE RELIANCE → MAINTAIN MONITORING → DETECT REGRESSION → RESTRICT / RESPOND → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-111` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Classification Control

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL RESTORED-RELIANCE STATE TO BE CONTINUOUSLY ASSESSED AGAINST A VALID CURRENT BASELINE, WITH EXPLICIT DEVIATION AND MATERIALITY LOGIC, CONSEQUENCE CLASSIFICATION, TRACEABLE EVIDENCE AND DIRECT ACTION PATHS, SO THAT REGRESSION IS DETECTED EARLY, FALSE CONFIDENCE FROM MISSING DATA IS PREVENTED, AND MATERIAL DETERIORATION CAN TRIGGER RESTRICTION, RESPONSE, REASSESSMENT OR REOPENING.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-DETECTION-CONTROL-01
