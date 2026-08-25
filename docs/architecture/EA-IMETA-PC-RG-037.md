# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-01

## Physical File ID
`EA-IMETA-PC-RG-037`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-037` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Resolution Verification Revalidation |
| Parent | EA-IMETA-PC-RG-036 — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-resolution-verification-revalidation layer defining how a verified resolution is re-examined against the current required state, changed circumstances, evidence, residual risk and applicable dependencies before the resolution is considered sufficiently current for renewed acceptance, reliance restoration or closure.

## Core Principle
Verification establishes that a resolution is supported at a point in time. Revalidation establishes that the verified resolution remains valid when time, context, evidence, dependencies, threats, requirements or operating conditions have changed.

```text
VERIFIED RESOLUTION
      ↓
REVALIDATION TRIGGER / REVIEW POINT
      ↓
CURRENT STATE + CRITERIA + CONTEXT
      ↓
RECHECK EVIDENCE + CONTROLS + OUTCOMES + BOUNDARIES
      ↓
VALID / CONDITIONAL / STALE / INVALID
      ↓
REACCEPT / RESTRICT / REOPEN / REVALIDATE AGAIN
```

## Revalidation Quality Test
```text
VALID VERIFICATION
+
CURRENT CONTEXT
+
CURRENT CRITERIA
+
CURRENT EVIDENCE
+
NO MATERIAL UNASSESSED CHANGE
+
RESIDUAL RISK WITHIN AUTHORITY
+
AUTHORIZED REVALIDATION DECISION
=
VALID GOVERNED REVALIDATION
```

## Revalidation Status Model
```text
NOT DUE
SCHEDULED
TRIGGERED
IN REVIEW
IN REVALIDATION
VALID
CONDITIONALLY VALID
STALE
INVALID
REOPENED
RESTRICTED
REVALIDATION FAILED
REVALIDATED
SUPERSEDED
```

## Revalidation Invariants

```text
EVERY MATERIAL VERIFIED RESOLUTION SHALL BE REVALIDATED WHEN REQUIRED BY TIME, CHANGE, RISK OR GOVERNANCE
```

```text
REVALIDATION SHALL CONSIDER CHANGES SINCE THE ORIGINAL VERIFICATION
```

```text
REVALIDATION SHALL NOT SIMPLY REPEAT THE ORIGINAL VERIFICATION WITHOUT ASSESSING CURRENT CONTEXT
```

```text
CURRENT CRITERIA SHALL BE USED
```

```text
STALE OR INVALID EVIDENCE SHALL NOT SUPPORT UNCONDITIONAL REVALIDATION
```

```text
MATERIAL CHANGES SHALL BE TRACEABLE TO THE REVALIDATION DECISION
```

```text
CONDITIONAL VALIDITY SHALL HAVE EXPLICIT CONDITIONS, OWNERS AND REVIEW POINTS
```

```text
FAILED REVALIDATION SHALL PREVENT UNCONTROLLED RESTORATION OF RELIANCE
```

```text
REVALIDATION SHALL CONSIDER DOWNSTREAM AND DEPENDENCY CHANGES
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE REVALIDATION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT REVALIDATION SHALL RECHECK AUTHORITY, POLICY, TOOLS, DATA, AUTONOMY AND BEHAVIOURAL CONDITIONS
```

```text
REVALIDATION SHALL REMAIN DISTINCT FROM INITIAL VERIFICATION
```

```text
REVALIDATION RESULTS SHALL BE HISTORICALLY TRACEABLE
```

```text
REVALIDATION SHALL SUPPORT REOPENING WHEN THE RESOLUTION BASIS IS NO LONGER VALID
```

```text
REPEATED REVALIDATION FAILURE SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Revalidation Domain — Resolution Revalidation Governance

**Control family:** `PCRR-001`

The Resolution Revalidation Governance domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-001-01` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-02` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-03` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-04` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-05` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-06` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-001-07` — Establish and maintain the resolution revalidation governance control.
- `PCRR-001-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 2. Revalidation Domain — Resolution Revalidation Objective

**Control family:** `PCRR-002`

The Resolution Revalidation Objective domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-002-01` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-02` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-03` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-04` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-05` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-06` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-002-07` — Establish and maintain the resolution revalidation objective control.
- `PCRR-002-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 3. Revalidation Domain — Resolution Revalidation Definition

**Control family:** `PCRR-003`

The Resolution Revalidation Definition domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-003-01` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-02` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-03` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-04` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-05` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-06` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-003-07` — Establish and maintain the resolution revalidation definition control.
- `PCRR-003-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 4. Revalidation Domain — Resolution Revalidation Scope

**Control family:** `PCRR-004`

The Resolution Revalidation Scope domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-004-01` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-02` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-03` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-04` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-05` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-06` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-004-07` — Establish and maintain the resolution revalidation scope control.
- `PCRR-004-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 5. Revalidation Domain — Resolution Revalidation Authority

**Control family:** `PCRR-005`

The Resolution Revalidation Authority domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-005-01` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-02` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-03` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-04` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-05` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-06` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-005-07` — Establish and maintain the resolution revalidation authority control.
- `PCRR-005-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 6. Revalidation Domain — Resolution Revalidation Criteria

**Control family:** `PCRR-006`

The Resolution Revalidation Criteria domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-006-01` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-02` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-03` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-04` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-05` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-06` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-006-07` — Establish and maintain the resolution revalidation criteria control.
- `PCRR-006-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 7. Revalidation Domain — Resolution Revalidation Preconditions

**Control family:** `PCRR-007`

The Resolution Revalidation Preconditions domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-007-01` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-02` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-03` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-04` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-05` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-06` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-007-07` — Establish and maintain the resolution revalidation preconditions control.
- `PCRR-007-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 8. Revalidation Domain — Resolution Revalidation Evidence

**Control family:** `PCRR-008`

The Resolution Revalidation Evidence domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-008-01` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-02` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-03` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-04` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-05` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-06` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-008-07` — Establish and maintain the resolution revalidation evidence control.
- `PCRR-008-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 9. Revalidation Domain — Resolution Revalidation Method

**Control family:** `PCRR-009`

The Resolution Revalidation Method domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-009-01` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-02` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-03` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-04` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-05` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-06` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-009-07` — Establish and maintain the resolution revalidation method control.
- `PCRR-009-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 10. Revalidation Domain — Resolution Revalidation Decision

**Control family:** `PCRR-010`

The Resolution Revalidation Decision domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-010-01` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-02` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-03` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-04` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-05` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-06` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-010-07` — Establish and maintain the resolution revalidation decision control.
- `PCRR-010-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 11. Revalidation Domain — Resolution Revalidation Accountability

**Control family:** `PCRR-011`

The Resolution Revalidation Accountability domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-011-01` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-02` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-03` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-04` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-05` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-06` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-011-07` — Establish and maintain the resolution revalidation accountability control.
- `PCRR-011-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 12. Revalidation Domain — Resolution Revalidation Timing

**Control family:** `PCRR-012`

The Resolution Revalidation Timing domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-012-01` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-02` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-03` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-04` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-05` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-06` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-012-07` — Establish and maintain the resolution revalidation timing control.
- `PCRR-012-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 13. Revalidation Domain — Security Resolution Revalidation

**Control family:** `PCRR-013`

The Security Resolution Revalidation domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-013-01` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-02` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-03` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-04` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-05` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-06` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-013-07` — Establish and maintain the security resolution revalidation control.
- `PCRR-013-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 14. Revalidation Domain — Resilience Resolution Revalidation

**Control family:** `PCRR-014`

The Resilience Resolution Revalidation domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-014-01` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-02` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-03` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-04` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-05` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-06` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-014-07` — Establish and maintain the resilience resolution revalidation control.
- `PCRR-014-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 15. Revalidation Domain — Compliance Resolution Revalidation

**Control family:** `PCRR-015`

The Compliance Resolution Revalidation domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-015-01` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-02` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-03` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-04` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-05` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-06` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-015-07` — Establish and maintain the compliance resolution revalidation control.
- `PCRR-015-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 16. Revalidation Domain — Data Resolution Revalidation

**Control family:** `PCRR-016`

The Data Resolution Revalidation domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-016-01` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-02` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-03` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-04` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-05` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-06` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-016-07` — Establish and maintain the data resolution revalidation control.
- `PCRR-016-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 17. Revalidation Domain — AI and Agent Resolution Revalidation

**Control family:** `PCRR-017`

The AI and Agent Resolution Revalidation domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-017-01` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-02` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-03` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-04` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-05` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-06` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-017-07` — Establish and maintain the ai and agent resolution revalidation control.
- `PCRR-017-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 18. Revalidation Domain — Resolution Revalidation Failure

**Control family:** `PCRR-018`

The Resolution Revalidation Failure domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-018-01` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-02` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-03` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-04` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-05` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-06` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-018-07` — Establish and maintain the resolution revalidation failure control.
- `PCRR-018-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 19. Revalidation Domain — Resolution Revalidation Independence

**Control family:** `PCRR-019`

The Resolution Revalidation Independence domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-019-01` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-02` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-03` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-04` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-05` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-06` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-019-07` — Establish and maintain the resolution revalidation independence control.
- `PCRR-019-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## 20. Revalidation Domain — Resolution Revalidation Review and Learning

**Control family:** `PCRR-020`

The Resolution Revalidation Review and Learning domain establishes governed mandatory-revalidation requirements.

### Required controls
- `PCRR-020-01` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-01-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-02` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-02-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-03` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-03-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-04` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-04-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-05` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-05-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-06` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-06-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.
- `PCRR-020-07` — Establish and maintain the resolution revalidation review and learning control.
- `PCRR-020-07-E` — Preserve verification basis, change context, criteria, evidence, result, authority and follow-on traceability.

```text
VERIFY → REVALIDATE → REACCEPT / RESTRICT / REOPEN
```

## Resolution Revalidation Structure

| Element | Required definition |
|---|---|
| Verified Resolution | Previously verified state |
| Trigger | Reason revalidation is required |
| Current Context | Present operating conditions |
| Current Criteria | Applicable requirements |
| Evidence | Current supporting basis |
| Result | Revalidation determination |
| Authority | Authorized decision role |
| Follow-on | Acceptance / reliance / reopening |

## Resolution Revalidation Objective

Determine whether a previously verified resolution remains valid and sufficiently current to support the next authorized lifecycle state.

## Resolution Revalidation Definition

Revalidation is the controlled reassessment of a verified resolution against current conditions to determine whether its validity persists, requires conditions, or has ceased.

## Resolution Revalidation Scope

Scope shall include the original resolution, verification basis, changes since verification, affected systems, controls, dependencies, outcomes, boundaries and residual risk.

## Resolution Revalidation Authority

Authority shall define who may initiate, perform, challenge, approve, conditionally accept or reject revalidation.

## Resolution Revalidation Criteria

Criteria shall define when a verified resolution remains valid, becomes conditional, becomes stale or is invalid.

```text
VERIFIED RESOLUTION
↓
MATERIAL CHANGE SINCE VERIFICATION?
├── NO → CURRENT EVIDENCE CHECK
└── YES → IMPACT ASSESSMENT
     ↓
CURRENT CRITERIA SATISFIED?
├── NO → REOPEN / RESTRICT
└── YES → REVALIDATED
```

## Resolution Revalidation Preconditions

Preconditions include current criteria, identified changes, available evidence, defined scope, valid verification history and appropriate decision authority.

## Resolution Revalidation Evidence

Evidence shall demonstrate both continuity and current validity, including relevant changes, new measurements, updated dependencies and changed risk conditions.

## Resolution Revalidation Method

Methods may include targeted retesting, evidence review, change-impact analysis, control reassessment, outcome confirmation and independent review.

```text
ORIGINAL VERIFICATION
↓
CHANGE ANALYSIS
↓
TARGETED RECHECK
↓
CURRENT EVIDENCE
↓
REVALIDATION RESULT
```

## Resolution Revalidation Decision

Decisions shall distinguish revalidated, conditionally revalidated, stale, invalid, restricted and reopened states.

```text
REVALIDATED → PROCEED
CONDITIONAL → PROCEED WITH CONTROLS
STALE → REFRESH / REVERIFY
INVALID → REOPEN / REMEDIATE
RESTRICTED → LIMIT RELIANCE
```

## Resolution Revalidation Accountability

Accountability shall remain explicit for the revalidation determination and any conditions attached to continued validity.

## Resolution Revalidation Timing

Revalidation timing shall be driven by scheduled review points, evidence expiry, material changes, incidents, regression signals, threat changes, requirement changes or other defined triggers.

## Security Resolution Revalidation

Revalidate security resolution against current threats, vulnerabilities, access conditions, controls, exposure and monitoring evidence.

## Resilience Resolution Revalidation

Revalidate resilience resolution against current availability, capacity, dependencies, recovery capability and continuity conditions.

## Compliance Resolution Revalidation

Revalidate compliance resolution against current obligations, policies, controls, evidence and reporting requirements.

## Data Resolution Revalidation

Revalidate data resolution against current integrity, quality, lineage, access, retention, authorized-use and downstream conditions.

## AI and Agent Resolution Revalidation

Revalidate AI/agent resolution against current authority, policy, tools, data access, autonomy limits, behavioural patterns and operating context.

```text
VERIFIED AI / AGENT RESOLUTION
↓
CURRENT AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY + BEHAVIOUR
↓
STILL VALID?
├── YES → REVALIDATED
└── NO → RESTRICT / REOPEN / REVERIFY
```

## Resolution Revalidation Failure

Failure to revalidate shall prevent uncontrolled continuation of the previous resolution status where revalidation is mandatory.

```text
REVALIDATION FAILURE
↓
PROTECT / RESTRICT
↓
IDENTIFY CHANGE OR GAP
↓
REVERIFY / REMEDIATE
↓
REOPEN / ESCALATE IF REQUIRED
```

## Resolution Revalidation Independence

Where materiality requires it, revalidation shall include independent review or testing distinct from the original remediation and verification roles.

## Resolution Revalidation Review and Learning

Reviews shall identify recurring stale resolutions, weak triggers, inadequate change detection, excessive conditionality and opportunities to improve verification and monitoring.

## Revalidation Determination Model
```text
VERIFIED RESOLUTION
↓
REVALIDATION DUE OR TRIGGERED?
├── NO → CONTINUE MONITORING
└── YES
     ↓
CURRENT CONTEXT IDENTIFIED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
MATERIAL CHANGE IDENTIFIED?
├── YES → IMPACT ASSESSMENT
└── NO
     ↓
CURRENT CRITERIA + EVIDENCE VALID?
├── NO → STALE / INVALID / REOPEN
└── YES
     ↓
RESIDUAL RISK WITHIN AUTHORITY?
├── NO → RESTRICT / ESCALATE
└── YES → REVALIDATED
```

## Revalidation Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Revalidated | Previous resolution remains valid | Proceed |
| Conditionally Revalidated | Valid with explicit conditions | Monitor conditions |
| Stale | Basis too old | Refresh / reverify |
| Invalid | Basis no longer valid | Reopen / remediate |
| Restricted | Continued validity limited | Limit reliance |
| Revalidation Failed | Current validity not demonstrated | Reverify / escalate |

## Revalidation Record
| Field | Required |
|---|---|
| Revalidation ID | Yes |
| Resolution ID | Yes |
| Verification ID | Yes |
| Trigger | Yes |
| Change Analysis | Yes |
| Current Criteria Version | Yes |
| Current Evidence | Yes |
| Result | Yes |
| Conditions | Where applicable |
| Residual Risk | Yes |
| Authority | Yes |
| Follow-on Decision | Yes |

## Revalidation Triggers
Typical triggers include scheduled review, evidence expiry, material change, security event, resilience degradation, compliance change, data change, AI/agent behaviour change, regression detection, authority change or significant dependency change.

```text
TRIGGER
↓
IS PREVIOUS RESOLUTION STILL VALID?
├── YES → REVALIDATE / CONTINUE
└── NO → REOPEN / REMEDIATE / REVERIFY
```

## Revalidation Change Analysis
The revalidation process shall distinguish changes that are immaterial from changes that could alter the resolution basis. Material change shall trigger deeper revalidation or reopening as appropriate.

## Revalidation Scope Creep Control
Revalidation shall not silently expand the original resolution into new environments, users, systems, data, dependencies or operating conditions. Such expansion requires appropriate assessment and governance.

## Revalidation Change Control
Changes to revalidation triggers, criteria, methods, evidence requirements, frequency or authorities shall be governed, approved, versioned and effective-dated.

```text
CURRENT REVALIDATION MODEL
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

## Revalidation Anti-Gaming Control
Revalidation shall not be reduced to a procedural renewal. It shall test whether the resolution remains valid under present conditions and shall reopen the resolution where the basis has materially changed.

Historical revalidation records, change assessments, evidence, conditions, decisions, restrictions, failures and reopenings shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-resolution-verification-revalidation layer beneath mandatory resolution verification. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, acceptance, reliance, monitoring, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Revalidation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → ESCALATION → RESOLUTION → VERIFICATION → MANDATORY REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING
```

## Complete Revalidation Chain
```text
RESOLVE → VERIFY → MONITOR VALIDITY → TRIGGER REVALIDATION → ASSESS CHANGE → RECHECK CURRENT CRITERIA + EVIDENCE → REVALIDATE / CONDITION / RESTRICT / REOPEN → ACCEPT → RESTORE RELIANCE → MONITOR
```

## Next Document
`EA-IMETA-PC-RG-038` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification Revalidation Reacceptance

## Final Principle
EA-IMETA SHALL REQUIRE VERIFIED RESOLUTIONS TO REMAIN SUBJECT TO REVALIDATION WHEN TIME, CHANGE, RISK, EVIDENCE, REQUIREMENTS OR OPERATING CONDITIONS COULD AFFECT THEIR VALIDITY, WITH CURRENT CRITERIA, CHANGE ANALYSIS, SUFFICIENT EVIDENCE AND AUTHORIZED DECISION REQUIRED BEFORE UNCONDITIONAL ACCEPTANCE OR RELIANCE RESTORATION.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-01
