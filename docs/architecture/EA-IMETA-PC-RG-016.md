# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01

## Physical File ID
`EA-IMETA-PC-RG-016`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-016` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Reliance |
| Parent | EA-IMETA-PC-RG-015 — Mandatory Acceptance |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-reliance layer defining when, how and to what extent an accepted mandatory state may be relied upon for operational, governance, security, resilience, compliance, data and AI/agent decisions.

## Core Principle
Acceptance establishes permission to rely within a defined scope; reliance is the controlled use of that accepted state. Reliance shall remain bounded by evidence, conditions, validity, monitoring, materiality and current governance status.

```text
ACCEPTED STATE
      ↓
RELIANCE BASIS
      ↓
SCOPE / CONDITIONS / LIMITS
      ↓
AUTHORIZED RELIANCE
      ↓
MONITOR CURRENT VALIDITY
      ↓
CONTINUE / LIMIT / SUSPEND / REVOKE
      ↓
REASSESS / REVALIDATE / RE-ACCEPT WHEN REQUIRED
```

## Reliance Quality Test
```text
VALID ACCEPTANCE
+
DEFINED RELIANCE SCOPE
+
CURRENT EVIDENCE
+
KNOWN CONDITIONS
+
AUTHORIZED USE
+
MONITORING
+
LIMITATION / SUSPENSION RULES
+
TRACEABLE DECISION
=
VALID GOVERNED RELIANCE
```

## Reliance Status Model
```text
NOT PERMITTED
ELIGIBLE
AUTHORIZED
ACTIVE
LIMITED
CONDITIONAL
UNDER MONITORING
SUSPENDED
REVOKED
EXPIRED
SUPERSEDED
UNDER REASSESSMENT
```

## Reliance Invariants

```text
RELIANCE SHALL ONLY BE BASED ON A VALID ACCEPTANCE OR OTHER EXPLICIT GOVERNANCE BASIS
```

```text
RELIANCE SCOPE SHALL BE EXPLICIT
```

```text
RELIANCE CONDITIONS AND LIMITATIONS SHALL BE KNOWN TO USERS AND DECISION MAKERS
```

```text
RELIANCE SHALL NOT EXCEED THE SCOPE OF THE ACCEPTANCE
```

```text
CURRENT VALIDITY SHALL BE MONITORED WHERE MATERIAL
```

```text
LOSS OF ACCEPTANCE VALIDITY SHALL LIMIT, SUSPEND OR REVOKE RELIANCE AS REQUIRED
```

```text
UNDETERMINED CURRENT STATE SHALL NOT SUPPORT UNQUALIFIED RELIANCE
```

```text
RELIANCE SHALL BE TRACEABLE TO THE ACCEPTANCE, EVIDENCE AND GOVERNANCE VERSIONS USED
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RELIANCE SHALL RECEIVE APPROPRIATE CONTROLS
```

```text
AI AND AGENT RELIANCE SHALL RESPECT CURRENT AUTHORITY, POLICY, TOOL, DATA AND AUTONOMY BOUNDARIES
```

```text
CONDITIONAL RELIANCE SHALL HAVE EXPLICIT LIMITS AND MONITORING
```

```text
RELIANCE SHALL NOT CREATE AN UNAUTHORIZED EXCEPTION TO A MANDATORY REQUIREMENT
```

```text
HISTORICAL RELIANCE DECISIONS SHALL REMAIN PRESERVED
```

```text
RELIANCE SHALL BE SUSPENDED WHEN MATERIAL EVIDENCE INVALIDATES ITS BASIS
```

```text
REPEATED RELIANCE FAILURE SHALL TRIGGER GOVERNANCE LEARNING
```

## 1. Reliance Domain — Reliance Governance

**Control family:** `PCRMRL-001`

The Reliance Governance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-001-01` — Establish and maintain the reliance governance control.
- `PCRMRL-001-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-02` — Establish and maintain the reliance governance control.
- `PCRMRL-001-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-03` — Establish and maintain the reliance governance control.
- `PCRMRL-001-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-04` — Establish and maintain the reliance governance control.
- `PCRMRL-001-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-05` — Establish and maintain the reliance governance control.
- `PCRMRL-001-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-06` — Establish and maintain the reliance governance control.
- `PCRMRL-001-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-001-07` — Establish and maintain the reliance governance control.
- `PCRMRL-001-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 2. Reliance Domain — Reliance Objective

**Control family:** `PCRMRL-002`

The Reliance Objective domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-002-01` — Establish and maintain the reliance objective control.
- `PCRMRL-002-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-02` — Establish and maintain the reliance objective control.
- `PCRMRL-002-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-03` — Establish and maintain the reliance objective control.
- `PCRMRL-002-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-04` — Establish and maintain the reliance objective control.
- `PCRMRL-002-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-05` — Establish and maintain the reliance objective control.
- `PCRMRL-002-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-06` — Establish and maintain the reliance objective control.
- `PCRMRL-002-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-002-07` — Establish and maintain the reliance objective control.
- `PCRMRL-002-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 3. Reliance Domain — Reliance Definition

**Control family:** `PCRMRL-003`

The Reliance Definition domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-003-01` — Establish and maintain the reliance definition control.
- `PCRMRL-003-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-02` — Establish and maintain the reliance definition control.
- `PCRMRL-003-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-03` — Establish and maintain the reliance definition control.
- `PCRMRL-003-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-04` — Establish and maintain the reliance definition control.
- `PCRMRL-003-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-05` — Establish and maintain the reliance definition control.
- `PCRMRL-003-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-06` — Establish and maintain the reliance definition control.
- `PCRMRL-003-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-003-07` — Establish and maintain the reliance definition control.
- `PCRMRL-003-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 4. Reliance Domain — Reliance Scope

**Control family:** `PCRMRL-004`

The Reliance Scope domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-004-01` — Establish and maintain the reliance scope control.
- `PCRMRL-004-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-02` — Establish and maintain the reliance scope control.
- `PCRMRL-004-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-03` — Establish and maintain the reliance scope control.
- `PCRMRL-004-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-04` — Establish and maintain the reliance scope control.
- `PCRMRL-004-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-05` — Establish and maintain the reliance scope control.
- `PCRMRL-004-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-06` — Establish and maintain the reliance scope control.
- `PCRMRL-004-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-004-07` — Establish and maintain the reliance scope control.
- `PCRMRL-004-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 5. Reliance Domain — Reliance Authority

**Control family:** `PCRMRL-005`

The Reliance Authority domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-005-01` — Establish and maintain the reliance authority control.
- `PCRMRL-005-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-02` — Establish and maintain the reliance authority control.
- `PCRMRL-005-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-03` — Establish and maintain the reliance authority control.
- `PCRMRL-005-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-04` — Establish and maintain the reliance authority control.
- `PCRMRL-005-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-05` — Establish and maintain the reliance authority control.
- `PCRMRL-005-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-06` — Establish and maintain the reliance authority control.
- `PCRMRL-005-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-005-07` — Establish and maintain the reliance authority control.
- `PCRMRL-005-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 6. Reliance Domain — Reliance Basis

**Control family:** `PCRMRL-006`

The Reliance Basis domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-006-01` — Establish and maintain the reliance basis control.
- `PCRMRL-006-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-02` — Establish and maintain the reliance basis control.
- `PCRMRL-006-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-03` — Establish and maintain the reliance basis control.
- `PCRMRL-006-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-04` — Establish and maintain the reliance basis control.
- `PCRMRL-006-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-05` — Establish and maintain the reliance basis control.
- `PCRMRL-006-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-06` — Establish and maintain the reliance basis control.
- `PCRMRL-006-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-006-07` — Establish and maintain the reliance basis control.
- `PCRMRL-006-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 7. Reliance Domain — Reliance Conditions

**Control family:** `PCRMRL-007`

The Reliance Conditions domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-007-01` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-02` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-03` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-04` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-05` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-06` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-007-07` — Establish and maintain the reliance conditions control.
- `PCRMRL-007-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 8. Reliance Domain — Reliance Level

**Control family:** `PCRMRL-008`

The Reliance Level domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-008-01` — Establish and maintain the reliance level control.
- `PCRMRL-008-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-02` — Establish and maintain the reliance level control.
- `PCRMRL-008-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-03` — Establish and maintain the reliance level control.
- `PCRMRL-008-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-04` — Establish and maintain the reliance level control.
- `PCRMRL-008-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-05` — Establish and maintain the reliance level control.
- `PCRMRL-008-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-06` — Establish and maintain the reliance level control.
- `PCRMRL-008-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-008-07` — Establish and maintain the reliance level control.
- `PCRMRL-008-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 9. Reliance Domain — Reliance Timing

**Control family:** `PCRMRL-009`

The Reliance Timing domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-009-01` — Establish and maintain the reliance timing control.
- `PCRMRL-009-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-02` — Establish and maintain the reliance timing control.
- `PCRMRL-009-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-03` — Establish and maintain the reliance timing control.
- `PCRMRL-009-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-04` — Establish and maintain the reliance timing control.
- `PCRMRL-009-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-05` — Establish and maintain the reliance timing control.
- `PCRMRL-009-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-06` — Establish and maintain the reliance timing control.
- `PCRMRL-009-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-009-07` — Establish and maintain the reliance timing control.
- `PCRMRL-009-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 10. Reliance Domain — Reliance Evidence

**Control family:** `PCRMRL-010`

The Reliance Evidence domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-010-01` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-02` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-03` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-04` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-05` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-06` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-010-07` — Establish and maintain the reliance evidence control.
- `PCRMRL-010-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 11. Reliance Domain — Reliance Monitoring

**Control family:** `PCRMRL-011`

The Reliance Monitoring domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-011-01` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-02` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-03` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-04` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-05` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-06` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-011-07` — Establish and maintain the reliance monitoring control.
- `PCRMRL-011-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 12. Reliance Domain — Reliance Limitation

**Control family:** `PCRMRL-012`

The Reliance Limitation domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-012-01` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-02` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-03` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-04` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-05` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-06` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-012-07` — Establish and maintain the reliance limitation control.
- `PCRMRL-012-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 13. Reliance Domain — Security Reliance

**Control family:** `PCRMRL-013`

The Security Reliance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-013-01` — Establish and maintain the security reliance control.
- `PCRMRL-013-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-02` — Establish and maintain the security reliance control.
- `PCRMRL-013-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-03` — Establish and maintain the security reliance control.
- `PCRMRL-013-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-04` — Establish and maintain the security reliance control.
- `PCRMRL-013-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-05` — Establish and maintain the security reliance control.
- `PCRMRL-013-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-06` — Establish and maintain the security reliance control.
- `PCRMRL-013-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-013-07` — Establish and maintain the security reliance control.
- `PCRMRL-013-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 14. Reliance Domain — Resilience Reliance

**Control family:** `PCRMRL-014`

The Resilience Reliance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-014-01` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-02` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-03` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-04` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-05` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-06` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-014-07` — Establish and maintain the resilience reliance control.
- `PCRMRL-014-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 15. Reliance Domain — Compliance Reliance

**Control family:** `PCRMRL-015`

The Compliance Reliance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-015-01` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-02` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-03` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-04` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-05` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-06` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-015-07` — Establish and maintain the compliance reliance control.
- `PCRMRL-015-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 16. Reliance Domain — Data Reliance

**Control family:** `PCRMRL-016`

The Data Reliance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-016-01` — Establish and maintain the data reliance control.
- `PCRMRL-016-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-02` — Establish and maintain the data reliance control.
- `PCRMRL-016-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-03` — Establish and maintain the data reliance control.
- `PCRMRL-016-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-04` — Establish and maintain the data reliance control.
- `PCRMRL-016-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-05` — Establish and maintain the data reliance control.
- `PCRMRL-016-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-06` — Establish and maintain the data reliance control.
- `PCRMRL-016-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-016-07` — Establish and maintain the data reliance control.
- `PCRMRL-016-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 17. Reliance Domain — AI and Agent Reliance

**Control family:** `PCRMRL-017`

The AI and Agent Reliance domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-017-01` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-02` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-03` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-04` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-05` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-06` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-017-07` — Establish and maintain the ai and agent reliance control.
- `PCRMRL-017-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 18. Reliance Domain — Reliance Failure

**Control family:** `PCRMRL-018`

The Reliance Failure domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-018-01` — Establish and maintain the reliance failure control.
- `PCRMRL-018-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-02` — Establish and maintain the reliance failure control.
- `PCRMRL-018-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-03` — Establish and maintain the reliance failure control.
- `PCRMRL-018-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-04` — Establish and maintain the reliance failure control.
- `PCRMRL-018-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-05` — Establish and maintain the reliance failure control.
- `PCRMRL-018-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-06` — Establish and maintain the reliance failure control.
- `PCRMRL-018-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-018-07` — Establish and maintain the reliance failure control.
- `PCRMRL-018-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 19. Reliance Domain — Reliance Escalation

**Control family:** `PCRMRL-019`

The Reliance Escalation domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-019-01` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-02` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-03` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-04` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-05` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-06` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-019-07` — Establish and maintain the reliance escalation control.
- `PCRMRL-019-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## 20. Reliance Domain — Reliance Review and Learning

**Control family:** `PCRMRL-020`

The Reliance Review and Learning domain establishes governed mandatory-reliance requirements for post-closure regression.

### Required controls
- `PCRMRL-020-01` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-01-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-02` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-02-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-03` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-03-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-04` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-04-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-05` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-05-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-06` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-06-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.
- `PCRMRL-020-07` — Establish and maintain the reliance review and learning control.
- `PCRMRL-020-07-E` — Preserve acceptance basis, scope, conditions, authority, monitoring, reliance decision and disposition traceability.

```text
ACCEPT → RELY → MONITOR → LIMIT / SUSPEND / REVOKE
```

## Reliance Structure

| Element | Required definition |
|---|---|
| Acceptance | Approved basis for reliance |
| Scope | What may be relied upon |
| Conditions | Restrictions or obligations |
| Authority | Authority permitting reliance |
| Level | Degree of permitted reliance |
| Evidence | Supporting current evidence |
| Monitoring | Controls confirming continued validity |
| Limitations | Known boundaries |
| Suspension | Conditions preventing continued reliance |
| Review | Required reassessment or renewal |

## Reliance Objective

The objective is to ensure that accepted states are used only within their valid governance boundaries and that reliance decreases or stops when the basis becomes uncertain or invalid.

## Reliance Definition

Reliance is the controlled use of an accepted mandatory state as a basis for decisions, operation, control execution, risk treatment or governance conclusions.

## Reliance Scope

Scope shall identify services, systems, controls, processes, data, environments, users, decisions and dependencies for which reliance is permitted.

## Reliance Authority

Authority shall identify who may authorize, consume, restrict, suspend or revoke reliance. Operational use shall not silently expand the approved scope.

## Reliance Basis

Every material reliance decision shall be traceable to the acceptance, revalidation, evidence, criteria and versions that establish its basis.

## Reliance Conditions

Conditions attached to acceptance shall automatically constrain reliance. Conditions shall be visible, assigned and monitored.
```text
ACCEPTANCE CONDITIONS
↓
RELIANCE LIMITS
↓
MONITOR CONDITIONS
↓
CONDITION BREACH?
├── NO → CONTINUE
└── YES → LIMIT / SUSPEND / ESCALATE
```

## Reliance Level

Reliance may be classified according to confidence, materiality and permitted use.
```text
FULL → NORMAL GOVERNED RELIANCE
LIMITED → RESTRICTED USE / ADDITIONAL CONTROLS
CONDITIONAL → USE ONLY WITH SPECIFIED CONDITIONS
SUSPENDED → DO NOT RELY
REVOKED → BASIS NO LONGER VALID
```

## Reliance Timing

Reliance shall respect acceptance effective dates, review dates, expiry conditions and known change windows. Expired acceptance shall not support unqualified reliance.

## Reliance Evidence

Current evidence shall be available where required to demonstrate that the reliance basis remains valid. Historical evidence supports traceability but does not automatically establish current validity.

## Reliance Monitoring

Material reliance shall be monitored for changes in state, evidence, thresholds, conditions, incidents, risks and dependencies.
```text
ACTIVE RELIANCE
↓
MONITOR
↓
MATERIAL CHANGE?
├── NO → CONTINUE
└── YES → REASSESS / REVALIDATE
```

## Reliance Limitation

Reliance shall be limited when evidence is incomplete, conditions are partially met, risk increases or the accepted state is only conditionally valid.

## Security Reliance

Security decisions shall not rely beyond the currently accepted security state. Material security change shall trigger appropriate limitation, reassessment or suspension.

## Resilience Reliance

Resilience decisions shall account for current capacity, dependencies, recovery evidence and changed operating conditions. Prior recovery success shall not guarantee future reliance.

## Compliance Reliance

Compliance reliance shall remain within the scope of current evidence and applicable requirements. Acceptance shall not be interpreted as an unauthorized legal or regulatory exemption.

## Data Reliance

Data consumers shall rely only within approved quality, lineage, integrity, access and authorized-use boundaries.

## AI and Agent Reliance

AI and agent reliance shall be explicitly bounded by current authority, policy, data, tool, autonomy and behavioural acceptance.
```text
ACCEPTED AI / AGENT STATE
↓
RELIANCE BOUNDARY
├── AUTHORITY
├── DATA
├── TOOLS
├── POLICY
└── AUTONOMY
↓
MATERIAL CHANGE?
├── NO → CONTINUE WITH MONITORING
└── YES → LIMIT / SUSPEND / REASSESS
```

## Reliance Failure

Reliance failure occurs when a decision or operation materially depends on a state that was invalid, out of scope, expired, insufficiently evidenced or subject to breached conditions.
```text
RELIANCE FAILURE
↓
PROTECT REQUIRED STATE
↓
LIMIT / SUSPEND
↓
CLASSIFY IMPACT
↓
RESPOND / REMEDIATE
↓
REASSESS / REVALIDATE
```

## Reliance Escalation

Escalation shall occur when reliance is materially disputed, unsupported, out of scope, conditionally breached, based on stale evidence or otherwise unsafe to continue.

## Reliance Review and Learning

Reliance patterns shall be reviewed for excessive confidence, recurring scope breaches, stale evidence, weak monitoring, inappropriate acceptance criteria and systemic governance gaps.

## Reliance Determination Model
```text
ACCEPTANCE VALID?
├── NO → RELIANCE NOT PERMITTED
└── YES
     ↓
WITHIN APPROVED SCOPE?
├── NO → BLOCK / ESCALATE
└── YES
     ↓
CONDITIONS SATISFIED?
├── NO → LIMIT / SUSPEND / ESCALATE
└── YES
     ↓
CURRENT EVIDENCE / VALIDITY SUFFICIENT?
├── NO → LIMIT / REASSESS
└── YES → AUTHORIZED RELIANCE
```

## Reliance Record
| Field | Required |
|---|---|
| Reliance ID | Yes |
| Acceptance ID | Yes |
| Revalidation ID | Yes |
| Scope | Yes |
| Reliance Level | Yes |
| Conditions | Where applicable |
| Authority | Yes |
| Evidence References | Yes |
| Monitoring Controls | Yes |
| Effective Date | Yes |
| Review / Expiry | Where applicable |
| Suspension / Revocation Rule | Yes |
| Reliance Decision | Yes |

## Reliance Suspension and Revocation
Reliance shall be suspended or revoked when acceptance is suspended or revoked, conditions are breached, material evidence invalidates the basis, scope is exceeded or a material change makes continued reliance unsafe.

```text
ACCEPTED / RELIED-UPON STATE
↓
MATERIAL CHANGE / BREACH / INVALIDATION
↓
LIMIT / SUSPEND / REVOKE
↓
REASSESS
↓
REVALIDATE
↓
RE-ACCEPT
↓
RESTORE RELIANCE
```

## Reliance Anti-Gaming Control
Reliance shall not be treated as valid merely because a decision was previously accepted, operational processes depend upon it, or stakeholders expect continuity. Current scope, evidence, conditions and governance status remain controlling.

## Reliance Change Control
Changes to reliance scope, levels, conditions, authorities, monitoring, suspension rules or permitted use shall be governed, approved, versioned and effective-dated.

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

Historical reliance decisions shall remain preserved and shall remain linked to the acceptance and governance versions applicable at the time.

## Relationship to Existing Architecture
This document specializes the mandatory-reliance layer beneath mandatory acceptance. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation or acceptance layers.

## Governance-to-Reliance Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → MANDATORY RELIANCE → MONITORING → LIMIT / SUSPEND / REVOKE
```

## Complete Reliance Chain
```text
MANDATORY STATE → VERIFY → EVIDENCE → MEASURE → THRESHOLD → CLASSIFY → CONSEQUENCE → RESPOND → EFFECTIVENESS → REASSESS → REVALIDATE → ACCEPT → RELY → MONITOR → REASSESS WHEN TRIGGERED
```

## Next Document
`EA-IMETA-PC-RG-017` — Mandatory Monitoring

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL RELIANCE ON AN ACCEPTED MANDATORY STATE TO REMAIN WITHIN EXPLICIT SCOPE, CONDITIONS, AUTHORITY AND CURRENT EVIDENCE, WITH MATERIAL LOSS OF VALIDITY, SCOPE, CONDITIONS OR ACCEPTANCE BASIS TRIGGERING LIMITATION, SUSPENSION, REVOCATION, REASSESSMENT OR ESCALATION AS REQUIRED.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-01
