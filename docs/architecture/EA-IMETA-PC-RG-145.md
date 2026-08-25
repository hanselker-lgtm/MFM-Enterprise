# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-DEVIATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-145`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-145` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-DEVIATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Monitoring Deviation Determination |
| Parent | EA-IMETA-PC-RG-144 — Mandatory Post-Closure Regression Monitoring Result Comparison Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory deviation-determination layer that determines whether a material or otherwise governed difference identified through post-closure monitoring constitutes a formal deviation from an approved baseline, required state, control condition, acceptance criterion, policy, obligation or other authorized reference condition.

## Core Principle
A difference is not automatically a deviation. Deviation determination establishes whether the difference crosses an applicable governed boundary, violates a requirement, exceeds an approved tolerance, or otherwise meets the formal criteria for deviation. The determination shall remain evidence-based, contextual, traceable and distinct from regression determination.

```text
QUALIFIED COMPARISON RESULT
        ↓
DIFFERENCE CONFIRMED?
├── NO → NO DEVIATION
└── YES
     ↓
GOVERNED DEVIATION CRITERIA APPLICABLE?
├── NO → HOLD / DEFINE / ESCALATE
└── YES
     ↓
BOUNDARY / REQUIREMENT / TOLERANCE BREACHED?
├── NO → CONTROLLED DIFFERENCE
└── YES
     ↓
DEVIATION CONFIRMED?
├── NO → INCONCLUSIVE / REVIEW
└── YES
     ↓
CLASSIFY DEVIATION
     ↓
ASSESS CONSEQUENCE / REGRESSION / RESPONSE NEED
```
## Deviation Quality Test
```text
VALID COMPARISON
+
APPLICABLE DEVIATION CRITERIA
+
IDENTIFIED GOVERNED BOUNDARY
+
EVIDENCE OF BREACH / NON-CONFORMANCE
+
CONTEXTUAL ASSESSMENT
+
MATERIALITY / CONSEQUENCE
+
ACCOUNTABLE DETERMINATION
=
VALID GOVERNED DEVIATION
```
## Comparison vs Deviation vs Regression
```text
COMPARISON
→ WHAT DIFFERENCE EXISTS?

DEVIATION
→ DOES THE DIFFERENCE VIOLATE A GOVERNED CONDITION?

REGRESSION
→ DOES THE DEVIATION REPRESENT A RETURN OF THE PREVIOUSLY GOVERNED REGRESSION CONDITION?

CONSEQUENCE
→ WHAT EFFECT DOES THE DEVIATION HAVE?

RESPONSE
→ WHAT ACTION IS GOVERNED BY THE DEVIATION?
```
## Deviation States
```text
DV0 — DEVIATION NOT REQUIRED
DV1 — DEVIATION PENDING
DV2 — DEVIATION ASSESSMENT IN PROGRESS
DV3 — CRITERIA CONFIRMED
DV4 — NO DEVIATION
DV5 — CONTROLLED DIFFERENCE
DV6 — BORDERLINE / WATCH
DV7 — DEVIATION INDICATED
DV8 — DEVIATION CONFIRMED
DV9 — MATERIAL DEVIATION
DV10 — CRITICAL DEVIATION
DV11 — DEVIATION INCONCLUSIVE
DV12 — EVIDENCE REQUIRED
DV13 — CONTEXT / CRITERIA INVALID
DV14 — ESCALATION REQUIRED
DV15 — REGRESSION ASSESSMENT READY
DV16 — CONSEQUENCE ASSESSMENT READY
DV17 — RESPONSE ASSESSMENT READY
DV18 — REVALIDATION REQUIRED
DV19 — REOPENING ASSESSMENT REQUIRED
DVX — UNKNOWN / INSUFFICIENT BASIS
DVS — DEVIATION ASSESSMENT SUSPENDED

## Deviation Dimensions
| Dimension | Required determination |
|---|---|
| Comparison | Valid comparison input |
| Criteria | Applicable deviation criteria |
| Boundary | Governing boundary / requirement |
| Breach | Breach condition |
| Tolerance | Approved tolerance |
| Materiality | Significance |
| Severity | Deviation severity |
| Persistence | Duration / recurrence |
| Context | Operating conditions |
| Evidence | Supporting proof |
| Cause | Where required |
| Regression | Regression indication |
| Consequence | Consequence input |
| Response | Response input |
| Decision | Deviation outcome |

## Deviation Invariants

```text
ONLY VALID COMPARISONS SHALL BE USED AS THE PRIMARY INPUT TO MATERIAL DEVIATION DETERMINATION
```

```text
DEVIATION CRITERIA SHALL BE EXPLICIT AND APPLICABLE TO THE DECISION
```

```text
THE GOVERNED BOUNDARY OR REQUIREMENT SHALL BE IDENTIFIABLE
```

```text
CONTROLLED DIFFERENCE SHALL REMAIN DISTINCT FROM FORMAL DEVIATION
```

```text
BORDERLINE CONDITIONS SHALL REMAIN DISTINCT FROM CONFIRMED DEVIATIONS
```

```text
MATERIAL DEVIATIONS SHALL NOT BE DOWNGRADED TO PRESERVE A CLOSED STATE
```

```text
TOLERANCES SHALL NOT BE ALTERED WITHOUT GOVERNED AUTHORITY
```

```text
CONTEXT SHALL BE CONSIDERED WHERE IT CHANGES THE MEANING OR MATERIALITY OF THE DIFFERENCE
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE RELEVANT
```

```text
SECURITY, RESILIENCE, SAFETY, COMPLIANCE AND DATA DEVIATIONS SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT DEVIATIONS SHALL CONSIDER POLICY, AUTHORITY, BEHAVIOR, TOOL, DATA AND CONSEQUENCE CONDITIONS
```

```text
INCONCLUSIVE DEVIATION ASSESSMENTS SHALL NOT BE RECORDED AS NO DEVIATION
```

```text
DEVIATION DETERMINATION SHALL REMAIN DISTINCT FROM REGRESSION DETERMINATION
```

```text
MATERIAL DEVIATIONS SHALL BE AVAILABLE AS INPUT TO CONSEQUENCE, RESPONSE, REVALIDATION AND REOPENING GOVERNANCE
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
DEVIATION RECORDS SHALL PRESERVE THE BASIS FOR AUDIT, REVALIDATION AND FUTURE REGRESSION ANALYSIS
```

## 1. Deviation Domain — Post-Closure Regression Monitoring Deviation Governance

**Control family:** `PCRD-001`

The Post-Closure Regression Monitoring Deviation Governance domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-001-01` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-02` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-03` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-04` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-05` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-06` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-001-07` — Establish and maintain the post-closure regression monitoring deviation governance control.
- `PCRD-001-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 2. Deviation Domain — Post-Closure Regression Monitoring Deviation Objective

**Control family:** `PCRD-002`

The Post-Closure Regression Monitoring Deviation Objective domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-002-01` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-02` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-03` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-04` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-05` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-06` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-002-07` — Establish and maintain the post-closure regression monitoring deviation objective control.
- `PCRD-002-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 3. Deviation Domain — Post-Closure Regression Monitoring Deviation Definition

**Control family:** `PCRD-003`

The Post-Closure Regression Monitoring Deviation Definition domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-003-01` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-02` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-03` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-04` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-05` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-06` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-003-07` — Establish and maintain the post-closure regression monitoring deviation definition control.
- `PCRD-003-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 4. Deviation Domain — Post-Closure Regression Monitoring Deviation Scope

**Control family:** `PCRD-004`

The Post-Closure Regression Monitoring Deviation Scope domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-004-01` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-02` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-03` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-04` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-05` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-06` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-004-07` — Establish and maintain the post-closure regression monitoring deviation scope control.
- `PCRD-004-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 5. Deviation Domain — Post-Closure Regression Monitoring Deviation Authority

**Control family:** `PCRD-005`

The Post-Closure Regression Monitoring Deviation Authority domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-005-01` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-02` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-03` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-04` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-05` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-06` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-005-07` — Establish and maintain the post-closure regression monitoring deviation authority control.
- `PCRD-005-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 6. Deviation Domain — Post-Closure Regression Monitoring Deviation Criteria

**Control family:** `PCRD-006`

The Post-Closure Regression Monitoring Deviation Criteria domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-006-01` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-02` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-03` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-04` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-05` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-06` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-006-07` — Establish and maintain the post-closure regression monitoring deviation criteria control.
- `PCRD-006-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 7. Deviation Domain — Post-Closure Regression Monitoring Deviation Preconditions

**Control family:** `PCRD-007`

The Post-Closure Regression Monitoring Deviation Preconditions domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-007-01` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-02` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-03` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-04` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-05` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-06` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-007-07` — Establish and maintain the post-closure regression monitoring deviation preconditions control.
- `PCRD-007-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 8. Deviation Domain — Post-Closure Regression Monitoring Deviation Evidence

**Control family:** `PCRD-008`

The Post-Closure Regression Monitoring Deviation Evidence domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-008-01` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-02` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-03` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-04` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-05` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-06` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-008-07` — Establish and maintain the post-closure regression monitoring deviation evidence control.
- `PCRD-008-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 9. Deviation Domain — Post-Closure Regression Monitoring Deviation Method

**Control family:** `PCRD-009`

The Post-Closure Regression Monitoring Deviation Method domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-009-01` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-02` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-03` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-04` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-05` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-06` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-009-07` — Establish and maintain the post-closure regression monitoring deviation method control.
- `PCRD-009-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 10. Deviation Domain — Post-Closure Regression Monitoring Deviation Decision

**Control family:** `PCRD-010`

The Post-Closure Regression Monitoring Deviation Decision domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-010-01` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-02` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-03` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-04` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-05` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-06` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-010-07` — Establish and maintain the post-closure regression monitoring deviation decision control.
- `PCRD-010-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 11. Deviation Domain — Post-Closure Regression Monitoring Deviation Accountability

**Control family:** `PCRD-011`

The Post-Closure Regression Monitoring Deviation Accountability domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-011-01` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-02` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-03` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-04` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-05` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-06` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-011-07` — Establish and maintain the post-closure regression monitoring deviation accountability control.
- `PCRD-011-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 12. Deviation Domain — Post-Closure Regression Monitoring Deviation Timing

**Control family:** `PCRD-012`

The Post-Closure Regression Monitoring Deviation Timing domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-012-01` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-02` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-03` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-04` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-05` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-06` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-012-07` — Establish and maintain the post-closure regression monitoring deviation timing control.
- `PCRD-012-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 13. Deviation Domain — Security Post-Closure Regression Monitoring Deviation

**Control family:** `PCRD-013`

The Security Post-Closure Regression Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-013-01` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-02` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-03` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-04` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-05` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-06` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-013-07` — Establish and maintain the security post-closure regression monitoring deviation control.
- `PCRD-013-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 14. Deviation Domain — Resilience Post-Closure Regression Monitoring Deviation

**Control family:** `PCRD-014`

The Resilience Post-Closure Regression Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-014-01` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-02` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-03` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-04` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-05` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-06` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-014-07` — Establish and maintain the resilience post-closure regression monitoring deviation control.
- `PCRD-014-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 15. Deviation Domain — Compliance Post-Closure Regression Monitoring Deviation

**Control family:** `PCRD-015`

The Compliance Post-Closure Regression Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-015-01` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-02` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-03` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-04` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-05` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-06` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-015-07` — Establish and maintain the compliance post-closure regression monitoring deviation control.
- `PCRD-015-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 16. Deviation Domain — Data Post-Closure Regression Monitoring Deviation

**Control family:** `PCRD-016`

The Data Post-Closure Regression Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-016-01` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-02` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-03` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-04` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-05` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-06` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-016-07` — Establish and maintain the data post-closure regression monitoring deviation control.
- `PCRD-016-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 17. Deviation Domain — AI and Agent Post-Closure Regression Monitoring Deviation

**Control family:** `PCRD-017`

The AI and Agent Post-Closure Regression Monitoring Deviation domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-017-01` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-02` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-03` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-04` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-05` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-06` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-017-07` — Establish and maintain the ai and agent post-closure regression monitoring deviation control.
- `PCRD-017-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 18. Deviation Domain — Post-Closure Regression Monitoring Deviation Failure

**Control family:** `PCRD-018`

The Post-Closure Regression Monitoring Deviation Failure domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-018-01` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-02` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-03` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-04` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-05` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-06` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-018-07` — Establish and maintain the post-closure regression monitoring deviation failure control.
- `PCRD-018-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 19. Deviation Domain — Post-Closure Regression Monitoring Deviation Independence

**Control family:** `PCRD-019`

The Post-Closure Regression Monitoring Deviation Independence domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-019-01` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-02` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-03` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-04` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-05` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-06` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-019-07` — Establish and maintain the post-closure regression monitoring deviation independence control.
- `PCRD-019-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## 20. Deviation Domain — Post-Closure Regression Monitoring Deviation Review and Learning

**Control family:** `PCRD-020`

The Post-Closure Regression Monitoring Deviation Review and Learning domain establishes governed mandatory deviation-determination requirements.

### Required controls
- `PCRD-020-01` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-01-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-02` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-02-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-03` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-03-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-04` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-04-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-05` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-05-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-06` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-06-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.
- `PCRD-020-07` — Establish and maintain the post-closure regression monitoring deviation review and learning control.
- `PCRD-020-07-E` — Preserve comparison, criteria, boundary, breach, tolerance, materiality, severity, persistence, context, evidence, cause, regression, consequence, response, decision and handover traceability.

```text
COMPARISON → APPLY DEVIATION CRITERIA → DETERMINE BREACH → CONFIRM / REJECT DEVIATION → HANDOVER
```

## Post-Closure Regression Monitoring Deviation Structure

| Element | Required definition |
|---|---|
| Comparison | Valid comparison input |
| Criteria | Deviation rules |
| Boundary | Requirement / control boundary |
| Breach | Breach condition |
| Tolerance | Approved tolerance |
| Materiality | Significance |
| Severity | Impact level |
| Persistence | Duration / recurrence |
| Context | Operating conditions |
| Evidence | Supporting proof |
| Cause | Where required |
| Regression | Regression indication |
| Consequence | Consequence input |
| Response | Response input |
| Decision | Deviation outcome |

## Post-Closure Regression Monitoring Deviation Objective

Determine whether a governed difference constitutes a formal deviation, including its materiality and severity, so that downstream regression, consequence, response, revalidation and reopening decisions are based on an explicit deviation state.

## Post-Closure Regression Monitoring Deviation Definition

Deviation determination is the governed decision that a valid comparison difference crosses an applicable requirement, boundary, tolerance, acceptance criterion or other authorized condition.

## Post-Closure Regression Monitoring Deviation Scope

Scope includes criteria, boundaries, breaches, tolerance, materiality, severity, persistence, context, evidence, cause, regression indication, consequence and response implications.

## Post-Closure Regression Monitoring Deviation Authority

Authority shall define who may confirm, reject, override, classify, escalate or reopen assessment of a deviation.

## Post-Closure Regression Monitoring Deviation Criteria

Criteria shall define when a difference constitutes no deviation, controlled difference, borderline condition, deviation, material deviation or critical deviation.
```text
COMPARISON
↓
CRITERIA APPLICABLE?
├── NO → HOLD / DEFINE / ESCALATE
└── YES
     ↓
BOUNDARY / REQUIREMENT BREACHED?
├── NO → NO DEVIATION / CONTROLLED DIFFERENCE
└── YES
     ↓
MATERIALITY / SEVERITY
↓
DEVIATION CONFIRMED?
├── NO → INCONCLUSIVE / REVIEW
└── YES
     ↓
CLASSIFY
     ↓
REGRESSION / CONSEQUENCE / RESPONSE ASSESSMENT
```

## Post-Closure Regression Monitoring Deviation Preconditions

Preconditions include valid comparison, applicable criteria, identified boundary, sufficient evidence and authorized decision authority.

## Post-Closure Regression Monitoring Deviation Evidence

Evidence shall preserve the comparison result, criteria version, governing boundary, breach evidence, tolerance, materiality, severity, context, decision and accountable authority.

## Post-Closure Regression Monitoring Deviation Method

Methods may include rule evaluation, threshold breach analysis, requirement mapping, tolerance assessment, materiality analysis, severity classification and independent review.
```text
COMPARISON → REQUIREMENT / BOUNDARY → BREACH TEST → MATERIALITY → SEVERITY → DEVIATION DECISION
```

## Post-Closure Regression Monitoring Deviation Decision

Decision shall determine DV0, DV1, DV2, DV3, DV4, DV5, DV6, DV7, DV8, DV9, DV10, DV11, DV12, DV13, DV14, DV15, DV16, DV17, DV18, DV19, DVX or DVS.

## Post-Closure Regression Monitoring Deviation Accountability

Accountability shall remain explicit for criteria selection, boundary interpretation, materiality, severity, confirmation and downstream handover.

## Post-Closure Regression Monitoring Deviation Timing

Deviation determination shall occur before material downstream decisions rely upon the difference, and within the required response window where consequence warrants urgency.

## Security Post-Closure Regression Monitoring Deviation

Security deviations shall consider unauthorized access, policy breach, control failure, exposure, integrity loss, persistence and consequence.

## Resilience Post-Closure Regression Monitoring Deviation

Resilience deviations shall consider service degradation, dependency failure, recovery breach, continuity loss and duration.

## Compliance Post-Closure Regression Monitoring Deviation

Compliance deviations shall consider breach of applicable obligations, control requirements, evidence requirements and authorized exceptions.

## Data Post-Closure Regression Monitoring Deviation

Data deviations shall consider integrity, completeness, lineage, consistency, access, corruption, loss and unauthorized alteration.

## AI and Agent Post-Closure Regression Monitoring Deviation

AI/agent deviations shall consider policy violation, authority overreach, unsafe behavior, unauthorized tool use, data misuse, model drift and consequential outcomes.
```text
VALID COMPARISON
↓
POLICY / AUTHORITY / BEHAVIOR / TOOL / DATA CRITERIA
↓
BREACH?
├── NO → NO DEVIATION
└── YES → CLASSIFY DEVIATION
```

## Post-Closure Regression Monitoring Deviation Failure

Failure includes incorrect criteria, invalid boundary, insufficient evidence, hidden breach, unsupported severity or unjustified rejection of a material deviation.
```text
DEVIATION ASSESSMENT FAILURE
↓
MATERIAL?
├── YES → HOLD / ESCALATE / REVALIDATE / REOPEN AS GOVERNED
└── NO → CORRECT / RECORD
```

## Post-Closure Regression Monitoring Deviation Independence

Independent deviation determination shall be used where consequence, conflict of interest, classification bias or governance requirements make independence necessary.

## Post-Closure Regression Monitoring Deviation Review and Learning

Reviews shall examine missed deviations, tolerance manipulation, boundary ambiguity, inconsistent severity, false negatives and deviations later confirmed through regression or reopening.

## Deviation Decision Model
```text
VALID COMPARISON
↓
CONFIRM APPLICABLE REQUIREMENT / BOUNDARY
↓
BREACH / TOLERANCE TEST
├── NO → NO DEVIATION / CONTROLLED DIFFERENCE
└── YES
     ↓
ASSESS MATERIALITY + SEVERITY + PERSISTENCE + CONTEXT
     ↓
DEVIATION CONFIRMED?
├── NO → INCONCLUSIVE / REVIEW
└── YES
     ↓
CLASSIFY
├── DEVIATION
├── MATERIAL DEVIATION
└── CRITICAL DEVIATION
     ↓
REGRESSION / CONSEQUENCE / RESPONSE / REVALIDATION
```

## Deviation Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| DV0 | Not required | Record basis |
| DV1 | Pending | Prepare assessment |
| DV2 | In progress | Assess |
| DV3 | Criteria confirmed | Continue |
| DV4 | No deviation | Continue monitoring |
| DV5 | Controlled difference | Monitor / record |
| DV6 | Borderline / watch | Review / increase monitoring |
| DV7 | Deviation indicated | Confirm / investigate |
| DV8 | Deviation confirmed | Govern deviation |
| DV9 | Material deviation | Consequence / response assessment |
| DV10 | Critical deviation | Immediate governed escalation |
| DV11 | Inconclusive | Gather evidence / escalate |
| DV12 | Evidence required | Supplement |
| DV13 | Criteria / context invalid | Correct / reassess |
| DV14 | Escalation required | Escalate |
| DV15 | Regression ready | Determine regression |
| DV16 | Consequence ready | Determine consequence |
| DV17 | Response ready | Determine response |
| DV18 | Revalidation required | Revalidate |
| DV19 | Reopening assessment | Assess reopening |
| DVX | Unknown | Do not assume no deviation |
| DVS | Suspended | Restore assessment |

## Deviation Record
| Field | Required |
|---|---|
| Deviation ID | Yes |
| Comparison ID | Yes |
| Criteria Version | Yes |
| Governing Boundary | Yes |
| Breach Evidence | Yes |
| Tolerance | Where applicable |
| Materiality | Yes |
| Severity | Yes |
| Persistence | Where applicable |
| Context | Yes |
| Cause | Where required |
| Regression Indication | Where applicable |
| Consequence Input | Where applicable |
| Response Input | Where applicable |
| Deviation State | Yes |
| Decision | Yes |
| Authority | Yes |
| Evidence | Yes |
| Audit Trail | Yes |

## Deviation Is Not Difference
A comparison can identify a difference without establishing a formal deviation.
```text
DIFFERENCE
≠
DEVIATION
```

## Deviation Is Not Regression
A deviation may indicate regression, but formal regression determination remains a separate governed decision.
```text
DEVIATION
≠
REGRESSION DETERMINED
```

## Deviation Is Not Consequence
Deviation identifies the condition; consequence determination establishes its governed effect.
```text
DEVIATION
≠
CONSEQUENCE
```

## Deviation Is Not Response
A confirmed deviation may require response, but response remains a separate governed layer.
```text
DEVIATION
≠
RESPONSE EXECUTED
```

## Boundary Integrity
The requirement, acceptance criterion, control boundary or tolerance used to determine deviation shall be authoritative and traceable.

## Materiality
Materiality shall consider magnitude, consequence, persistence, recurrence, exposure and decision purpose where relevant.

## Severity
Severity shall be determined using approved domain-specific criteria and shall not be inferred solely from the numerical size of the difference.

## Persistence and Recurrence
Persistent or recurring deviations shall be treated distinctly from isolated deviations where governance criteria require it.

## Exceptions
Authorized exceptions shall remain explicitly distinguishable from deviations. An exception shall not silently convert a material breach into a normal state.

## AI and Agent Deviation
AI/agent deviation assessment shall preserve policy, authority, behavior, tool and data context and shall account for consequential outcomes.

## Relationship to Regression
RG-145 supplies confirmed deviation states to the subsequent regression-determination layer.
```text
COMPARISON → DEVIATION → REGRESSION DETERMINATION
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression monitoring deviation-determination layer beneath comparison and above regression determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, qualification, comparison, regression determination, regression classification, consequence determination, alert determination, notification determination, acknowledgement determination, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, monitoring execution, result validation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Deviation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → MANDATORY DEVIATION DETERMINATION → REGRESSION DETERMINATION → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REOPENING
```

## Complete Deviation Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ISSUE ALERT → DETERMINE NOTIFICATION → ISSUE NOTIFICATION → DELIVER → DETERMINE ACKNOWLEDGEMENT → VALIDATE ACTOR / TIMING / COMPLETENESS → ACKNOWLEDGE → ACCEPT / ASSIGN → DETERMINE RESPONSE INITIATION → AUTHORIZE → ASSIGN → ACTIVATE → VERIFY → DETERMINE AUTHORITY TRANSFER → IDENTIFY RECEIVER → PACKAGE STATE → ACCEPT → VERIFY → ACTIVATE RECEIVING AUTHORITY → DETERMINE EXECUTION → AUTHORIZE ACTION → EXECUTE → OBSERVE → VERIFY → ADJUST / ESCALATE / ROLLBACK / STOP → COMPLETE → DETERMINE EFFECTIVENESS → VERIFY → DETERMINE RESOLUTION → RESTORE / CONTROL CONDITION → VERIFY → DETERMINE CLOSURE → COMPLETE OBLIGATIONS → CONFIRM EVIDENCE / RISK / HANDOVER → AUTHORIZE → VERIFY → CLOSE → DETERMINE MONITORING REQUIREMENT → DEFINE OBJECTIVE / SCOPE / OWNER / AUTHORITY / SIGNALS / THRESHOLDS / CADENCE / DURATION / EVIDENCE / ESCALATION → AUTHORIZE → ACTIVATE → VERIFY → EXECUTE MONITORING → OBSERVE → MEASURE → VALIDATE EXECUTION DATA → DETERMINE RESULT → VALIDATE RESULT → QUALIFY RESULT → COMPARE RESULT WITH AUTHORIZED TARGET → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-146` — Mandatory Post-Closure Regression Determination

## Final Principle
EA-IMETA SHALL REQUIRE ALL MATERIAL POST-CLOSURE MONITORING DIFFERENCES TO BE ASSESSED AGAINST EXPLICIT AND AUTHORITATIVE DEVIATION CRITERIA, GOVERNED BOUNDARIES, REQUIREMENTS AND TOLERANCES BEFORE A FORMAL DEVIATION IS CONFIRMED, WITH CONTROLLED DIFFERENCES, BORDERLINE CONDITIONS, DEVIATIONS, MATERIAL DEVIATIONS AND CRITICAL DEVIATIONS KEPT DISTINCT, AND WITH CONFIRMED DEVIATIONS AVAILABLE AS TRACEABLE INPUTS TO REGRESSION, CONSEQUENCE, RESPONSE, REVALIDATION AND REOPENING GOVERNANCE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-DEVIATION-DETERMINATION-01
