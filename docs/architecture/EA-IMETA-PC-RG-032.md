# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-01

## Physical File ID
`EA-IMETA-PC-RG-032`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-032` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Regression Reliance Monitoring |
| Parent | EA-IMETA-PC-RG-031 — Mandatory Regression Reliance |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-regression-reliance-monitoring layer defining how an accepted and relied-upon state is continuously or periodically observed to ensure that its acceptance basis, reliance conditions, evidence validity, required state and risk boundaries remain valid.

## Core Principle
Reliance creates an ongoing obligation to observe the conditions that make reliance legitimate. Monitoring shall detect material change, degradation, stale evidence, scope expansion, control failure and emerging regression before reliance becomes unjustified.

```text
AUTHORIZED RELIANCE
      ↓
DEFINE MONITORING CONDITIONS
      ↓
OBSERVE / MEASURE / TEST
      ↓
COMPARE WITH REQUIRED STATE + RELIANCE CONDITIONS
      ↓
NORMAL / WARNING / BREACH / REGRESSION
      ↓
CONTINUE / RESTRICT / SUSPEND / REASSESS / REVALIDATE / REVOKE
```

## Monitoring Quality Test
```text
VALID RELIANCE
+
DEFINED MONITORING OBJECTIVE
+
RELEVANT SIGNALS
+
MEASURABLE THRESHOLDS
+
CURRENT EVIDENCE
+
ASSIGNED OWNER
+
ESCALATION PATH
+
REVOCATION / REASSESSMENT TRIGGERS
=
VALID GOVERNED RELIANCE MONITORING
```

## Monitoring Status Model
```text
NOT REQUIRED
DEFINED
ACTIVE
HEALTHY
WARNING
BREACH
DEGRADED
STALE
UNKNOWN
ESCALATED
SUSPENDED
REASSESSMENT REQUIRED
REVALIDATION REQUIRED
RELIANCE RESTRICTED
RELIANCE REVOKED
```

## Monitoring Invariants

```text
EVERY MATERIAL RELIANCE SHALL HAVE DEFINED MONITORING REQUIREMENTS WHERE REQUIRED BY RISK OR GOVERNANCE
```

```text
MONITORING SHALL MEASURE CONDITIONS RELEVANT TO THE BASIS FOR RELIANCE
```

```text
MONITORING SHALL INCLUDE APPROPRIATE THRESHOLDS AND RESPONSE TRIGGERS
```

```text
STALE OR MISSING EVIDENCE SHALL NOT BE TREATED AS HEALTHY RELIANCE
```

```text
MONITORING SHALL DETECT MATERIAL SCOPE EXPANSION
```

```text
MONITORING SHALL DETECT LOSS OF ACCEPTANCE OR REVALIDATION BASIS
```

```text
MONITORING SHALL SUPPORT TIMELY REASSESSMENT, REVALIDATION, RESTRICTION OR REVOCATION
```

```text
MONITORING RESULTS SHALL BE TRACEABLE
```

```text
UNKNOWN SHALL REMAIN DISTINCT FROM NORMAL
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RELIANCE MONITORING SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT RELIANCE MONITORING SHALL OBSERVE AUTHORITY, POLICY, TOOLS, DATA, AUTONOMY AND BEHAVIOURAL BOUNDARIES
```

```text
MONITORING SHALL NOT BE DESIGNED TO HIDE OR DELAY REGRESSION DETECTION
```

```text
FAILED MONITORING SHALL ITSELF BE GOVERNED
```

```text
MONITORING SHALL PRESERVE HISTORICAL SIGNALS, EVENTS AND DECISIONS
```

```text
REPEATED MONITORING BREACHES SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Monitoring Domain — Reliance Monitoring Governance

**Control family:** `PCRM-001`

The Reliance Monitoring Governance domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-001-01` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-02` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-03` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-04` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-05` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-06` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-001-07` — Establish and maintain the reliance monitoring governance control.
- `PCRM-001-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 2. Monitoring Domain — Reliance Monitoring Objective

**Control family:** `PCRM-002`

The Reliance Monitoring Objective domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-002-01` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-02` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-03` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-04` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-05` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-06` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-002-07` — Establish and maintain the reliance monitoring objective control.
- `PCRM-002-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 3. Monitoring Domain — Reliance Monitoring Definition

**Control family:** `PCRM-003`

The Reliance Monitoring Definition domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-003-01` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-02` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-03` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-04` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-05` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-06` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-003-07` — Establish and maintain the reliance monitoring definition control.
- `PCRM-003-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 4. Monitoring Domain — Reliance Monitoring Scope

**Control family:** `PCRM-004`

The Reliance Monitoring Scope domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-004-01` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-02` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-03` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-04` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-05` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-06` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-004-07` — Establish and maintain the reliance monitoring scope control.
- `PCRM-004-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 5. Monitoring Domain — Reliance Monitoring Authority

**Control family:** `PCRM-005`

The Reliance Monitoring Authority domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-005-01` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-02` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-03` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-04` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-05` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-06` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-005-07` — Establish and maintain the reliance monitoring authority control.
- `PCRM-005-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 6. Monitoring Domain — Reliance Monitoring Criteria

**Control family:** `PCRM-006`

The Reliance Monitoring Criteria domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-006-01` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-02` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-03` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-04` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-05` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-06` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-006-07` — Establish and maintain the reliance monitoring criteria control.
- `PCRM-006-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 7. Monitoring Domain — Reliance Monitoring Preconditions

**Control family:** `PCRM-007`

The Reliance Monitoring Preconditions domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-007-01` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-02` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-03` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-04` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-05` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-06` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-007-07` — Establish and maintain the reliance monitoring preconditions control.
- `PCRM-007-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 8. Monitoring Domain — Reliance Monitoring Evidence

**Control family:** `PCRM-008`

The Reliance Monitoring Evidence domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-008-01` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-02` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-03` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-04` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-05` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-06` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-008-07` — Establish and maintain the reliance monitoring evidence control.
- `PCRM-008-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 9. Monitoring Domain — Reliance Monitoring Measurement

**Control family:** `PCRM-009`

The Reliance Monitoring Measurement domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-009-01` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-02` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-03` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-04` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-05` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-06` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-009-07` — Establish and maintain the reliance monitoring measurement control.
- `PCRM-009-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 10. Monitoring Domain — Reliance Monitoring Decision

**Control family:** `PCRM-010`

The Reliance Monitoring Decision domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-010-01` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-02` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-03` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-04` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-05` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-06` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-010-07` — Establish and maintain the reliance monitoring decision control.
- `PCRM-010-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 11. Monitoring Domain — Reliance Monitoring Accountability

**Control family:** `PCRM-011`

The Reliance Monitoring Accountability domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-011-01` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-02` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-03` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-04` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-05` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-06` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-011-07` — Establish and maintain the reliance monitoring accountability control.
- `PCRM-011-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 12. Monitoring Domain — Reliance Monitoring Timing

**Control family:** `PCRM-012`

The Reliance Monitoring Timing domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-012-01` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-02` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-03` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-04` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-05` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-06` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-012-07` — Establish and maintain the reliance monitoring timing control.
- `PCRM-012-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 13. Monitoring Domain — Security Reliance Monitoring

**Control family:** `PCRM-013`

The Security Reliance Monitoring domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-013-01` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-02` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-03` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-04` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-05` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-06` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-013-07` — Establish and maintain the security reliance monitoring control.
- `PCRM-013-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 14. Monitoring Domain — Resilience Reliance Monitoring

**Control family:** `PCRM-014`

The Resilience Reliance Monitoring domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-014-01` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-02` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-03` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-04` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-05` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-06` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-014-07` — Establish and maintain the resilience reliance monitoring control.
- `PCRM-014-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 15. Monitoring Domain — Compliance Reliance Monitoring

**Control family:** `PCRM-015`

The Compliance Reliance Monitoring domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-015-01` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-02` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-03` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-04` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-05` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-06` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-015-07` — Establish and maintain the compliance reliance monitoring control.
- `PCRM-015-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 16. Monitoring Domain — Data Reliance Monitoring

**Control family:** `PCRM-016`

The Data Reliance Monitoring domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-016-01` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-02` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-03` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-04` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-05` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-06` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-016-07` — Establish and maintain the data reliance monitoring control.
- `PCRM-016-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 17. Monitoring Domain — AI and Agent Reliance Monitoring

**Control family:** `PCRM-017`

The AI and Agent Reliance Monitoring domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-017-01` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-02` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-03` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-04` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-05` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-06` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-017-07` — Establish and maintain the ai and agent reliance monitoring control.
- `PCRM-017-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 18. Monitoring Domain — Reliance Monitoring Failure

**Control family:** `PCRM-018`

The Reliance Monitoring Failure domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-018-01` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-02` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-03` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-04` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-05` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-06` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-018-07` — Establish and maintain the reliance monitoring failure control.
- `PCRM-018-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 19. Monitoring Domain — Reliance Monitoring Escalation

**Control family:** `PCRM-019`

The Reliance Monitoring Escalation domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-019-01` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-02` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-03` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-04` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-05` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-06` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-019-07` — Establish and maintain the reliance monitoring escalation control.
- `PCRM-019-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## 20. Monitoring Domain — Reliance Monitoring Review and Learning

**Control family:** `PCRM-020`

The Reliance Monitoring Review and Learning domain establishes governed mandatory-monitoring requirements.

### Required controls
- `PCRM-020-01` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-01-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-02` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-02-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-03` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-03-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-04` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-04-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-05` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-05-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-06` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-06-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.
- `PCRM-020-07` — Establish and maintain the reliance monitoring review and learning control.
- `PCRM-020-07-E` — Preserve reliance scope, monitored condition, signal, threshold, evidence, owner, response and escalation traceability.

```text
RELY → MONITOR → DETECT CHANGE → ACT
```

## Reliance Monitoring Structure

| Element | Required definition |
|---|---|
| Reliance | Authorized use basis |
| Monitoring Objective | What must remain valid |
| Signal | Observable indicator |
| Threshold | Trigger condition |
| Evidence | Monitoring record |
| Owner | Accountable monitoring role |
| Response | Action on change |
| Escalation | Higher governance path |
| Revocation | Condition ending reliance |

## Reliance Monitoring Objective

Detect material changes or deterioration that could invalidate the basis for reliance and initiate the appropriate controlled response before reliance becomes unsafe, unauthorized or unjustified.

## Reliance Monitoring Definition

Reliance monitoring is the governed observation and measurement of the conditions, evidence, controls, outcomes and boundaries that support continued reliance.

## Reliance Monitoring Scope

Scope shall cover the accepted and relied-upon state, its relevant dependencies, boundaries, users, data, services, controls, evidence and operating conditions.

## Reliance Monitoring Authority

Authority shall define who owns monitoring, who may declare a breach, who may restrict reliance and who may trigger reassessment, revalidation or revocation.

## Reliance Monitoring Criteria

Criteria shall define normal, warning, breach, degraded, stale and unknown conditions.

```text
MONITORED STATE
↓
WITHIN THRESHOLD?
├── YES → NORMAL / CONTINUE
└── NO
     ↓
MATERIAL?
├── NO → WARNING / MONITOR
└── YES → BREACH / RESPONSE
```

## Reliance Monitoring Preconditions

Preconditions include defined scope, valid signals, approved thresholds, evidence retention, monitoring ownership, alerting and response paths.

## Reliance Monitoring Evidence

Monitoring evidence shall preserve observations, timestamps, source, measurement context, threshold version, detected condition and resulting action.

## Reliance Monitoring Measurement

Measurements shall be relevant, sufficiently sensitive, timely and resistant to manipulation. Where possible, monitoring shall combine multiple signals to reduce false confidence.

## Reliance Monitoring Decision

Monitoring outcomes shall drive explicit decisions such as continue, investigate, restrict, suspend, reassess, revalidate or revoke.

```text
NORMAL → CONTINUE
WARNING → INVESTIGATE / INCREASE MONITORING
BREACH → RESTRICT / REASSESS
CRITICAL BREACH → SUSPEND / REVOKE / ESCALATE
```

## Reliance Monitoring Accountability

Monitoring accountability shall remain explicit even where monitoring is automated or delegated. Automated detection does not eliminate governance accountability.

## Reliance Monitoring Timing

Monitoring frequency shall reflect materiality, volatility, dependency and time-to-impact. High-risk reliance may require continuous or near-real-time monitoring.

## Security Reliance Monitoring

Monitor security controls, access, exposure, threat indicators, policy compliance and evidence freshness relevant to continued reliance.

## Resilience Reliance Monitoring

Monitor availability, capacity, recovery capability, continuity, dependency health and degradation relevant to reliance.

## Compliance Reliance Monitoring

Monitor control status, applicable requirements, evidence validity and material compliance changes affecting reliance.

## Data Reliance Monitoring

Monitor data integrity, quality, lineage, access, retention, authorized use and material changes affecting data reliance.

## AI and Agent Reliance Monitoring

Monitor AI/agent authority, policy adherence, tool use, data access, autonomy, behavioural drift, abnormal outputs and boundary violations.

```text
AI / AGENT RELIANCE
↓
MONITOR AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY + BEHAVIOUR
↓
BOUNDARY BREACH?
├── NO → CONTINUE
└── YES → LIMIT / SUSPEND / REASSESS / REVOKE
```

## Reliance Monitoring Failure

Failure of monitoring coverage, sensors, evidence, thresholds, alerts or ownership shall be treated as a governance condition and may require restriction or suspension of reliance.

```text
MONITORING FAILURE
↓
LOSS OF OBSERVABILITY?
├── YES → LIMIT / SUSPEND RELIANCE
└── NO → RESTORE MONITORING
     ↓
REASSESS IF MATERIAL
```

## Reliance Monitoring Escalation

Escalation shall occur when thresholds are breached, monitoring is blind, impact is material, scope changes, authority is exceeded or repeated warnings indicate emerging regression.

## Reliance Monitoring Review and Learning

Reviews shall analyze trends, false positives, false negatives, stale signals, monitoring gaps, threshold quality and recurring reliance degradation.

## Monitoring Determination Model
```text
RELIANCE ACTIVE
↓
MONITORING AVAILABLE?
├── NO → LIMIT / SUSPEND / RESTORE OBSERVABILITY
└── YES
     ↓
SIGNALS CURRENT?
├── NO → STALE / INVESTIGATE
└── YES
     ↓
THRESHOLDS WITHIN LIMIT?
├── YES → CONTINUE
└── NO
     ↓
MATERIAL CHANGE / BREACH?
├── NO → WARNING / INCREASE MONITORING
└── YES
     ↓
RELIANCE BASIS STILL VALID?
├── NO → REASSESS / REVALIDATE / REVOKE
└── YES → CONTROLLED CONTINUATION
```

## Monitoring Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Healthy | Conditions within limits | Continue reliance |
| Warning | Early deviation | Investigate / increase monitoring |
| Breach | Threshold materially exceeded | Restrict / reassess |
| Degraded | Reliability of basis reduced | Limit / remediate |
| Stale | Evidence or signal too old | Restore / revalidate |
| Unknown | Observability insufficient | Protect / investigate |
| Critical | Immediate material concern | Suspend / revoke / escalate |

## Monitoring Record
| Field | Required |
|---|---|
| Monitoring ID | Yes |
| Reliance ID | Yes |
| Scope | Yes |
| Signal / Metric | Yes |
| Threshold Version | Yes |
| Observation | Yes |
| Timestamp | Yes |
| Evidence Reference | Yes |
| Owner | Yes |
| Result | Yes |
| Action | Yes |
| Escalation | Where applicable |
| Reassessment Trigger | Where applicable |

## Monitoring Coverage
Monitoring coverage shall be sufficient to detect the material conditions that could invalidate reliance. Absence of monitoring shall not be interpreted as absence of risk.

```text
RELIANCE BASIS
↓
WHAT COULD INVALIDATE IT?
↓
WHAT SIGNAL WOULD DETECT THAT?
↓
IS THE SIGNAL AVAILABLE AND TIMELY?
├── NO → COVERAGE GAP
└── YES → MONITOR
```

## Monitoring Blind Spots
Known blind spots shall be documented and assessed. Where a blind spot creates material uncertainty, reliance shall be restricted, suspended or subjected to compensating controls as appropriate.

## Monitoring Change Control
Changes to monitoring scope, signals, thresholds, frequency, retention, alerting or response paths shall be governed, approved, versioned and effective-dated.

```text
CURRENT MONITORING MODEL
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

## Monitoring Anti-Gaming Control
Monitoring shall not be optimized merely to avoid alerts or produce favorable reporting. Thresholds and signals shall reflect the real conditions necessary to maintain valid reliance.

Historical monitoring signals, alerts, breaches, investigations, threshold changes and resulting decisions shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-regression-reliance-monitoring layer beneath mandatory regression reliance. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Monitoring Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MANDATORY MONITORING → ALERTING → ESCALATION → RESOLUTION → CLOSURE → POST-CLOSURE MONITORING → REGRESSION DETECTION → REGRESSION CLASSIFICATION → REGRESSION CONSEQUENCE → REGRESSION RESPONSE → RESPONSE EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING
```

## Complete Monitoring Chain
```text
ACCEPT → AUTHORIZE RELIANCE → DEFINE MONITORING → OBSERVE → MEASURE → COMPARE → DETECT DEVIATION → ALERT → INVESTIGATE → REASSESS / REVALIDATE / RESTRICT / SUSPEND / REVOKE → RESOLVE → RE-CLOSE
```

## Next Document
`EA-IMETA-PC-RG-033` — Mandatory Regression Reliance Monitoring Alerting

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL RELIANCE TO REMAIN SUBJECT TO GOVERNED MONITORING OF THE CONDITIONS, EVIDENCE, CONTROLS, OUTCOMES AND BOUNDARIES THAT JUSTIFY RELIANCE, WITH TIMELY DETECTION, TRACEABLE EVIDENCE AND CONTROLLED RESTRICTION, SUSPENSION, REASSESSMENT, REVALIDATION OR REVOCATION WHEN THE BASIS FOR RELIANCE CHANGES.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-01
