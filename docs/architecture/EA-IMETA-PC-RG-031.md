# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01

## Physical File ID
`EA-IMETA-PC-RG-031`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-031` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Regression Reliance |
| Parent | EA-IMETA-PC-RG-030 — Mandatory Regression Revalidation Acceptance |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-regression-reliance layer defining when an accepted and revalidated state may be relied upon for operational, governance, security, compliance, data, service and decision-making purposes, and how that reliance remains bounded, monitored and revocable.

## Core Principle
Acceptance establishes that a state may be accepted; reliance determines whether and to what extent that accepted state may be used as a basis for action, operation, decision or further governance. Reliance shall be bounded by scope, authority, evidence validity, residual risk and continuing conditions.

```text
ACCEPTED STATE
      ↓
RELIANCE PRECONDITIONS
      ↓
SCOPE + AUTHORITY + EVIDENCE VALIDITY
      ↓
RESIDUAL RISK + CONDITIONS
      ↓
RELIANCE DECISION
      ↓
USE / OPERATE / DECIDE / GOVERN
      ↓
CONTINUOUS MONITORING + REVOCATION TRIGGERS
```

## Reliance Quality Test
```text
VALID ACCEPTANCE
+
VALID RELIANCE SCOPE
+
AUTHORIZED USE
+
CURRENT EVIDENCE
+
KNOWN CONDITIONS
+
RESIDUAL RISK WITHIN AUTHORITY
+
REVOCATION CONDITIONS
=
VALID GOVERNED RELIANCE
```

## Reliance Status Model
```text
NOT PERMITTED
READY FOR RELIANCE
AUTHORIZED
ACTIVE
CONDITIONAL
RESTRICTED
MONITORED
CHALLENGED
SUSPENDED
REVOKED
EXPIRED
SUPERSEDED
```

## Reliance Invariants

```text
RELIANCE SHALL REQUIRE VALID ACCEPTANCE WHERE ACCEPTANCE IS REQUIRED
```

```text
RELIANCE SHALL HAVE AN EXPLICIT SCOPE
```

```text
RELIANCE SHALL HAVE AN IDENTIFIABLE AUTHORITY BASIS
```

```text
RELIANCE SHALL CONSIDER THE VALIDITY PERIOD OF EVIDENCE AND ACCEPTANCE
```

```text
CONDITIONAL RELIANCE SHALL HAVE EXPLICIT CONDITIONS, OWNERS AND REVIEW POINTS
```

```text
RELIANCE SHALL NOT EXCEED THE SCOPE OF ACCEPTANCE
```

```text
RESIDUAL RISK SHALL REMAIN WITHIN THE AUTHORITY PERMITTED FOR RELIANCE
```

```text
RELIANCE SHALL BE REVOCABLE WHEN ITS BASIS CEASES TO BE VALID
```

```text
UNKNOWN OR STALE EVIDENCE SHALL NOT BE TREATED AS VALID BASIS FOR UNBOUNDED RELIANCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RELIANCE SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT RELIANCE SHALL BE LIMITED BY AUTHORITY, POLICY, TOOL, DATA, AUTONOMY AND BEHAVIOURAL BOUNDARIES
```

```text
RELIANCE SHALL NOT CREATE AUTHORITY THAT WAS NOT PRESENT IN THE ACCEPTED STATE
```

```text
MATERIAL CHANGES SHALL TRIGGER REASSESSMENT OF RELIANCE
```

```text
RELIANCE DECISIONS SHALL REMAIN TRACEABLE
```

```text
REPEATED RELIANCE CHALLENGES SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Reliance Domain — Regression Reliance Governance

**Control family:** `PCRL-001`

The Regression Reliance Governance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-001-01` — Establish and maintain the regression reliance governance control.
- `PCRL-001-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-02` — Establish and maintain the regression reliance governance control.
- `PCRL-001-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-03` — Establish and maintain the regression reliance governance control.
- `PCRL-001-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-04` — Establish and maintain the regression reliance governance control.
- `PCRL-001-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-05` — Establish and maintain the regression reliance governance control.
- `PCRL-001-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-06` — Establish and maintain the regression reliance governance control.
- `PCRL-001-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-001-07` — Establish and maintain the regression reliance governance control.
- `PCRL-001-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 2. Reliance Domain — Regression Reliance Objective

**Control family:** `PCRL-002`

The Regression Reliance Objective domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-002-01` — Establish and maintain the regression reliance objective control.
- `PCRL-002-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-02` — Establish and maintain the regression reliance objective control.
- `PCRL-002-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-03` — Establish and maintain the regression reliance objective control.
- `PCRL-002-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-04` — Establish and maintain the regression reliance objective control.
- `PCRL-002-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-05` — Establish and maintain the regression reliance objective control.
- `PCRL-002-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-06` — Establish and maintain the regression reliance objective control.
- `PCRL-002-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-002-07` — Establish and maintain the regression reliance objective control.
- `PCRL-002-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 3. Reliance Domain — Regression Reliance Definition

**Control family:** `PCRL-003`

The Regression Reliance Definition domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-003-01` — Establish and maintain the regression reliance definition control.
- `PCRL-003-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-02` — Establish and maintain the regression reliance definition control.
- `PCRL-003-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-03` — Establish and maintain the regression reliance definition control.
- `PCRL-003-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-04` — Establish and maintain the regression reliance definition control.
- `PCRL-003-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-05` — Establish and maintain the regression reliance definition control.
- `PCRL-003-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-06` — Establish and maintain the regression reliance definition control.
- `PCRL-003-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-003-07` — Establish and maintain the regression reliance definition control.
- `PCRL-003-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 4. Reliance Domain — Regression Reliance Scope

**Control family:** `PCRL-004`

The Regression Reliance Scope domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-004-01` — Establish and maintain the regression reliance scope control.
- `PCRL-004-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-02` — Establish and maintain the regression reliance scope control.
- `PCRL-004-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-03` — Establish and maintain the regression reliance scope control.
- `PCRL-004-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-04` — Establish and maintain the regression reliance scope control.
- `PCRL-004-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-05` — Establish and maintain the regression reliance scope control.
- `PCRL-004-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-06` — Establish and maintain the regression reliance scope control.
- `PCRL-004-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-004-07` — Establish and maintain the regression reliance scope control.
- `PCRL-004-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 5. Reliance Domain — Regression Reliance Authority

**Control family:** `PCRL-005`

The Regression Reliance Authority domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-005-01` — Establish and maintain the regression reliance authority control.
- `PCRL-005-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-02` — Establish and maintain the regression reliance authority control.
- `PCRL-005-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-03` — Establish and maintain the regression reliance authority control.
- `PCRL-005-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-04` — Establish and maintain the regression reliance authority control.
- `PCRL-005-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-05` — Establish and maintain the regression reliance authority control.
- `PCRL-005-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-06` — Establish and maintain the regression reliance authority control.
- `PCRL-005-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-005-07` — Establish and maintain the regression reliance authority control.
- `PCRL-005-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 6. Reliance Domain — Regression Reliance Criteria

**Control family:** `PCRL-006`

The Regression Reliance Criteria domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-006-01` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-02` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-03` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-04` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-05` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-06` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-006-07` — Establish and maintain the regression reliance criteria control.
- `PCRL-006-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 7. Reliance Domain — Regression Reliance Preconditions

**Control family:** `PCRL-007`

The Regression Reliance Preconditions domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-007-01` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-02` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-03` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-04` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-05` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-06` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-007-07` — Establish and maintain the regression reliance preconditions control.
- `PCRL-007-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 8. Reliance Domain — Regression Reliance Evidence

**Control family:** `PCRL-008`

The Regression Reliance Evidence domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-008-01` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-02` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-03` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-04` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-05` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-06` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-008-07` — Establish and maintain the regression reliance evidence control.
- `PCRL-008-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 9. Reliance Domain — Regression Reliance Decision

**Control family:** `PCRL-009`

The Regression Reliance Decision domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-009-01` — Establish and maintain the regression reliance decision control.
- `PCRL-009-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-02` — Establish and maintain the regression reliance decision control.
- `PCRL-009-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-03` — Establish and maintain the regression reliance decision control.
- `PCRL-009-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-04` — Establish and maintain the regression reliance decision control.
- `PCRL-009-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-05` — Establish and maintain the regression reliance decision control.
- `PCRL-009-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-06` — Establish and maintain the regression reliance decision control.
- `PCRL-009-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-009-07` — Establish and maintain the regression reliance decision control.
- `PCRL-009-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 10. Reliance Domain — Regression Reliance Accountability

**Control family:** `PCRL-010`

The Regression Reliance Accountability domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-010-01` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-02` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-03` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-04` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-05` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-06` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-010-07` — Establish and maintain the regression reliance accountability control.
- `PCRL-010-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 11. Reliance Domain — Regression Reliance Residual Risk

**Control family:** `PCRL-011`

The Regression Reliance Residual Risk domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-011-01` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-02` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-03` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-04` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-05` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-06` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-011-07` — Establish and maintain the regression reliance residual risk control.
- `PCRL-011-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 12. Reliance Domain — Regression Reliance Timing

**Control family:** `PCRL-012`

The Regression Reliance Timing domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-012-01` — Establish and maintain the regression reliance timing control.
- `PCRL-012-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-02` — Establish and maintain the regression reliance timing control.
- `PCRL-012-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-03` — Establish and maintain the regression reliance timing control.
- `PCRL-012-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-04` — Establish and maintain the regression reliance timing control.
- `PCRL-012-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-05` — Establish and maintain the regression reliance timing control.
- `PCRL-012-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-06` — Establish and maintain the regression reliance timing control.
- `PCRL-012-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-012-07` — Establish and maintain the regression reliance timing control.
- `PCRL-012-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 13. Reliance Domain — Security Regression Reliance

**Control family:** `PCRL-013`

The Security Regression Reliance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-013-01` — Establish and maintain the security regression reliance control.
- `PCRL-013-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-02` — Establish and maintain the security regression reliance control.
- `PCRL-013-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-03` — Establish and maintain the security regression reliance control.
- `PCRL-013-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-04` — Establish and maintain the security regression reliance control.
- `PCRL-013-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-05` — Establish and maintain the security regression reliance control.
- `PCRL-013-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-06` — Establish and maintain the security regression reliance control.
- `PCRL-013-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-013-07` — Establish and maintain the security regression reliance control.
- `PCRL-013-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 14. Reliance Domain — Resilience Regression Reliance

**Control family:** `PCRL-014`

The Resilience Regression Reliance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-014-01` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-02` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-03` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-04` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-05` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-06` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-014-07` — Establish and maintain the resilience regression reliance control.
- `PCRL-014-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 15. Reliance Domain — Compliance Regression Reliance

**Control family:** `PCRL-015`

The Compliance Regression Reliance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-015-01` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-02` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-03` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-04` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-05` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-06` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-015-07` — Establish and maintain the compliance regression reliance control.
- `PCRL-015-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 16. Reliance Domain — Data Regression Reliance

**Control family:** `PCRL-016`

The Data Regression Reliance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-016-01` — Establish and maintain the data regression reliance control.
- `PCRL-016-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-02` — Establish and maintain the data regression reliance control.
- `PCRL-016-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-03` — Establish and maintain the data regression reliance control.
- `PCRL-016-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-04` — Establish and maintain the data regression reliance control.
- `PCRL-016-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-05` — Establish and maintain the data regression reliance control.
- `PCRL-016-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-06` — Establish and maintain the data regression reliance control.
- `PCRL-016-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-016-07` — Establish and maintain the data regression reliance control.
- `PCRL-016-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 17. Reliance Domain — AI and Agent Regression Reliance

**Control family:** `PCRL-017`

The AI and Agent Regression Reliance domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-017-01` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-02` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-03` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-04` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-05` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-06` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-017-07` — Establish and maintain the ai and agent regression reliance control.
- `PCRL-017-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 18. Reliance Domain — Regression Reliance Failure

**Control family:** `PCRL-018`

The Regression Reliance Failure domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-018-01` — Establish and maintain the regression reliance failure control.
- `PCRL-018-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-02` — Establish and maintain the regression reliance failure control.
- `PCRL-018-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-03` — Establish and maintain the regression reliance failure control.
- `PCRL-018-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-04` — Establish and maintain the regression reliance failure control.
- `PCRL-018-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-05` — Establish and maintain the regression reliance failure control.
- `PCRL-018-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-06` — Establish and maintain the regression reliance failure control.
- `PCRL-018-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-018-07` — Establish and maintain the regression reliance failure control.
- `PCRL-018-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 19. Reliance Domain — Regression Reliance Escalation

**Control family:** `PCRL-019`

The Regression Reliance Escalation domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-019-01` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-02` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-03` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-04` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-05` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-06` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-019-07` — Establish and maintain the regression reliance escalation control.
- `PCRL-019-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## 20. Reliance Domain — Regression Reliance Review and Learning

**Control family:** `PCRL-020`

The Regression Reliance Review and Learning domain establishes governed mandatory-reliance requirements.

### Required controls
- `PCRL-020-01` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-01-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-02` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-02-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-03` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-03-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-04` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-04-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-05` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-05-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-06` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-06-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.
- `PCRL-020-07` — Establish and maintain the regression reliance review and learning control.
- `PCRL-020-07-E` — Preserve acceptance, scope, authority, evidence validity, conditions, reliance decision and revocation traceability.

```text
ACCEPT → AUTHORIZE RELIANCE → USE → MONITOR → REVOKE IF REQUIRED
```

## Regression Reliance Structure

| Element | Required definition |
|---|---|
| Acceptance | Authorized state approval |
| Reliance Scope | What may be relied upon |
| Authority | Who may authorize use |
| Evidence Validity | Current basis for reliance |
| Conditions | Constraints on reliance |
| Residual Risk | Remaining exposure |
| Reliance Decision | Authorized use determination |
| Monitoring | Continuing validity checks |
| Revocation | Conditions that end reliance |

## Regression Reliance Objective

Ensure that reliance on a revalidated and accepted state is proportionate, authorized, bounded and continuously subject to the conditions that made reliance legitimate.

## Regression Reliance Definition

Reliance is the governed use of an accepted state, control, outcome or evidence base as a basis for operation, decision, action or further governance.

## Regression Reliance Scope

Scope shall identify exactly what is relied upon, where it applies, for whom, for which decisions or operations, and what remains outside the reliance boundary.

## Regression Reliance Authority

Authority shall define who may authorize reliance, expand or restrict its scope, suspend it and revoke it.

## Regression Reliance Criteria

Criteria shall define when reliance is permitted and when it must be restricted or stopped.

```text
ACCEPTED STATE
↓
WITHIN ACCEPTED SCOPE?
├── NO → NOT PERMITTED
└── YES
     ↓
EVIDENCE / ACCEPTANCE CURRENT?
├── NO → SUSPEND / REVALIDATE
└── YES
     ↓
CONDITIONS SATISFIED?
├── NO → RESTRICT / REVOKE
└── YES → RELY
```

## Regression Reliance Preconditions

Preconditions include valid acceptance, defined scope, current evidence, known conditions, appropriate authority, residual-risk treatment and required monitoring.

## Regression Reliance Evidence

Evidence supporting reliance shall remain accessible, current, versioned and traceable to the acceptance and revalidation basis.

## Regression Reliance Decision

Reliance shall be explicitly authorized as permitted, conditional, restricted, suspended or revoked.

```text
AUTHORIZED → USE WITHIN SCOPE
CONDITIONAL → USE WITH CONDITIONS
RESTRICTED → LIMITED USE
SUSPENDED → NO RELIANCE
REVOKED → BASIS INVALID
```

## Regression Reliance Accountability

Accountability for reliance decisions shall remain explicit, including where downstream users or systems consume an accepted state.

## Regression Reliance Residual Risk

Residual risk shall be considered in determining whether reliance is permitted, restricted or requires additional controls.

## Regression Reliance Timing

Reliance shall respect acceptance validity, evidence freshness, review points and expiry conditions. Changed circumstances may require immediate reassessment.

## Security Regression Reliance

Security reliance shall be bounded by current controls, threat conditions, exposure, access authority and evidence validity.

## Resilience Regression Reliance

Resilience reliance shall be bounded by current availability, recovery, capacity, continuity and dependency conditions.

## Compliance Regression Reliance

Compliance reliance shall be limited to the requirements and evidence actually demonstrated and accepted.

## Data Regression Reliance

Data reliance shall be bounded by validated integrity, quality, lineage, access, retention and authorized-use conditions.

## AI and Agent Regression Reliance

AI/agent reliance shall explicitly define what outputs, actions, authority and autonomy may be relied upon and under which controls.

```text
ACCEPTED AI / AGENT STATE
↓
RELIANCE SCOPE
↓
AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY
↓
CONDITIONS VALID?
├── YES → CONTROLLED RELIANCE
└── NO → LIMIT / SUSPEND / REVOKE
```

## Regression Reliance Failure

Failure of reliance controls, stale evidence, unauthorized use or reliance outside scope shall trigger immediate restriction, suspension, reassessment or escalation as appropriate.

```text
RELIANCE FAILURE
↓
STOP / LIMIT UNAUTHORIZED RELIANCE
↓
ASSESS IMPACT
↓
REASSESS ACCEPTANCE / REVALIDATE
↓
RESTORE OR REVOKE RELIANCE
```

## Regression Reliance Escalation

Escalation shall occur when reliance is outside authority, residual risk exceeds limits, evidence validity is disputed, downstream impact is material or revocation affects critical operations.

## Regression Reliance Review and Learning

Reviews shall examine reliance failures, scope creep, stale evidence, hidden dependencies, downstream effects and repeated challenges to the accepted state.

## Reliance Determination Model
```text
ACCEPTANCE VALID?
├── NO → NOT PERMITTED / RETURN TO ACCEPTANCE
└── YES
     ↓
RELIANCE SCOPE DEFINED?
├── NO → DEFINE / ESCALATE
└── YES
     ↓
USE WITHIN SCOPE?
├── NO → STOP / RESTRICT
└── YES
     ↓
EVIDENCE CURRENT AND VALID?
├── NO → SUSPEND / REVALIDATE
└── YES
     ↓
CONDITIONS SATISFIED?
├── NO → RESTRICT / REVOKE
└── YES
     ↓
RESIDUAL RISK WITHIN AUTHORITY?
├── NO → ESCALATE / SUSPEND
└── YES → RELIANCE PERMITTED
```

## Reliance Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Authorized | Reliance permitted within defined scope | Monitor |
| Conditional | Reliance permitted subject to conditions | Track conditions |
| Restricted | Limited reliance | Apply boundaries |
| Suspended | Reliance temporarily prohibited | Reassess / revalidate |
| Revoked | Reliance basis no longer valid | Stop reliance / reopen |
| Expired | Validity period ended | Renew / revalidate |

## Reliance Record
| Field | Required |
|---|---|
| Reliance ID | Yes |
| Acceptance ID | Yes |
| Revalidation ID | Yes |
| Reliance Scope | Yes |
| Authorized Users / Consumers | Where applicable |
| Evidence Version | Yes |
| Conditions | Where applicable |
| Residual Risk | Yes |
| Authority | Yes |
| Decision | Yes |
| Validity Period | Yes |
| Monitoring Requirements | Yes |
| Revocation Triggers | Yes |

## Conditional Reliance
Conditional reliance shall define each condition, owner, deadline or review point, monitoring requirement and consequence of breach.

```text
CONDITIONAL RELIANCE
↓
CONDITIONS + OWNER + REVIEW POINT
↓
MONITOR
↓
CONDITIONS SATISFIED?
├── YES → CONTINUE RELIANCE
└── NO → RESTRICT / SUSPEND / REVOKE
```

## Reliance Revocation
Reliance shall be revoked or suspended when acceptance is revoked, evidence becomes materially invalid, required conditions fail, the scope is exceeded, material regression occurs or authority is withdrawn.

## Reliance Scope Creep Control
Reliance shall not silently expand from the accepted scope into new systems, decisions, users, environments, data or operating conditions. Any material expansion shall require appropriate reassessment and acceptance.

## Reliance Change Control
Changes to reliance scope, authority, evidence validity, conditions, residual-risk limits, monitoring or revocation criteria shall be governed, approved, versioned and effective-dated.

```text
CURRENT RELIANCE MODEL
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

## Reliance Anti-Gaming Control
Reliance shall not be treated as proof that a state is permanently valid. It is a bounded governance permission that remains dependent on the conditions and evidence supporting acceptance.

Historical reliance decisions, restrictions, suspensions, revocations, scope changes and downstream challenges shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-regression-reliance layer beneath mandatory regression revalidation acceptance. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, monitoring, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Reliance Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → MANDATORY RELIANCE → MONITORING → ALERTING → ESCALATION → RESOLUTION → CLOSURE → POST-CLOSURE MONITORING → REGRESSION DETECTION → REGRESSION CLASSIFICATION → REGRESSION CONSEQUENCE → REGRESSION RESPONSE → RESPONSE EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE
```

## Complete Reliance Chain
```text
REVALIDATE → ACCEPT → DEFINE RELIANCE SCOPE → AUTHORIZE → RELY WITHIN BOUNDARIES → MONITOR CONDITIONS + EVIDENCE → DETECT CHANGE → REASSESS / REVALIDATE → RESTRICT / SUSPEND / REVOKE IF REQUIRED → RESOLVE → RE-CLOSE
```

## Next Document
`EA-IMETA-PC-RG-032` — Mandatory Regression Reliance Monitoring

## Final Principle
EA-IMETA SHALL REQUIRE RELIANCE ON AN ACCEPTED REGRESSION STATE TO BE EXPLICITLY BOUNDED BY SCOPE, AUTHORITY, EVIDENCE VALIDITY, CONDITIONS AND RESIDUAL RISK, WITH CONTINUOUS GOVERNANCE CONTROLS THAT PREVENT UNAUTHORIZED SCOPE EXPANSION AND ENABLE TIMELY RESTRICTION, SUSPENSION OR REVOCATION WHEN THE BASIS FOR RELIANCE CEASES TO BE VALID.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01
