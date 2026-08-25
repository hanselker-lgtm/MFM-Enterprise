# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01

## Physical File ID
`EA-IMETA-PC-RG-020`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-020` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Resolution |
| Parent | EA-IMETA-PC-RG-019 — Mandatory Escalation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-resolution layer defining how an escalated or otherwise material condition is brought to a controlled and evidenced outcome, with explicit criteria, authority, accountability, verification and disposition before the matter may proceed to closure or governed follow-on activity.

## Core Principle
Resolution is not the same as action completion. A condition is resolved only when the defined resolution criteria are satisfied, the required state is restored or otherwise governed, sufficient evidence exists, verification is complete and the authorized authority accepts the disposition.

```text
ESCALATED / MATERIAL CONDITION
      ↓
RESOLUTION OBJECTIVE
      ↓
CONTAIN / REMEDIATE / RESTORE
      ↓
RESOLUTION EVIDENCE
      ↓
VERIFY AGAINST CRITERIA
      ↓
RESOLVED / PARTIALLY RESOLVED / UNRESOLVED / UNDETERMINED
      ↓
ACCEPT / REASSESS / REOPEN / ESCALATE
```

## Resolution Quality Test
```text
DEFINED CONDITION
+
DEFINED RESOLUTION OBJECTIVE
+
EXPLICIT RESOLUTION CRITERIA
+
SUFFICIENT EVIDENCE
+
VERIFICATION
+
AUTHORIZED DECISION
+
ACCOUNTABILITY
+
TRACEABLE DISPOSITION
=
VALID GOVERNED RESOLUTION
```

## Resolution Status Model
```text
OPEN
TRIGGERED
CONTAINED
IN REMEDIATION
RESTORING
READY FOR VERIFICATION
VERIFIED
RESOLVED
PARTIALLY RESOLVED
UNRESOLVED
UNDETERMINED
REOPENED
ESCALATED
ACCEPTED
CLOSED
SUPERSEDED
UNDER REVIEW
```

## Resolution Invariants

```text
EVERY MATERIAL CONDITION SHALL HAVE EXPLICIT RESOLUTION CRITERIA
```

```text
RESOLUTION SHALL ADDRESS THE GOVERNED CONDITION, NOT ONLY THE ASSOCIATED TASK
```

```text
CONTAINMENT SHALL NOT AUTOMATICALLY CONSTITUTE RESOLUTION
```

```text
REMEDIATION SHALL NOT AUTOMATICALLY CONSTITUTE RESOLUTION
```

```text
RESOLUTION SHALL REQUIRE SUFFICIENT AND TRACEABLE EVIDENCE
```

```text
RESOLUTION SHALL BE VERIFIED AGAINST CURRENT CRITERIA
```

```text
THE RESOLUTION DECISION SHALL HAVE IDENTIFIABLE AUTHORITY AND ACCOUNTABILITY
```

```text
PARTIAL RESOLUTION SHALL NOT BE RECORDED AS FULL RESOLUTION
```

```text
UNDETERMINED SHALL NOT BE TREATED AS RESOLVED
```

```text
UNRESOLVED CONDITIONS SHALL REMAIN GOVERNED AND SHALL BE ESCALATED WHEN REQUIRED
```

```text
RESOLUTION SHALL PRESERVE THE ORIGINAL TRIGGER, IMPACT, RESPONSE AND ESCALATION HISTORY
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RESOLUTIONS SHALL RECEIVE APPROPRIATE VERIFICATION
```

```text
AI AND AGENT RESOLUTION SHALL CONFIRM THAT THE GOVERNED AUTHORITY AND BEHAVIOURAL BOUNDARIES ARE RESTORED OR CONTROLLED
```

```text
RESOLUTION SHALL NOT BE USED TO HIDE REGRESSION OR PREMATURELY CLOSE A CONDITION
```

```text
REOPENING SHALL BE POSSIBLE WHEN SUBSEQUENT EVIDENCE INVALIDATES THE RESOLUTION
```

## 1. Resolution Domain — Resolution Governance

**Control family:** `PCRMR-001`

The Resolution Governance domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-001-01` — Establish and maintain the resolution governance control.
- `PCRMR-001-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-02` — Establish and maintain the resolution governance control.
- `PCRMR-001-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-03` — Establish and maintain the resolution governance control.
- `PCRMR-001-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-04` — Establish and maintain the resolution governance control.
- `PCRMR-001-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-05` — Establish and maintain the resolution governance control.
- `PCRMR-001-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-06` — Establish and maintain the resolution governance control.
- `PCRMR-001-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-001-07` — Establish and maintain the resolution governance control.
- `PCRMR-001-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 2. Resolution Domain — Resolution Objective

**Control family:** `PCRMR-002`

The Resolution Objective domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-002-01` — Establish and maintain the resolution objective control.
- `PCRMR-002-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-02` — Establish and maintain the resolution objective control.
- `PCRMR-002-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-03` — Establish and maintain the resolution objective control.
- `PCRMR-002-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-04` — Establish and maintain the resolution objective control.
- `PCRMR-002-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-05` — Establish and maintain the resolution objective control.
- `PCRMR-002-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-06` — Establish and maintain the resolution objective control.
- `PCRMR-002-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-002-07` — Establish and maintain the resolution objective control.
- `PCRMR-002-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 3. Resolution Domain — Resolution Definition

**Control family:** `PCRMR-003`

The Resolution Definition domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-003-01` — Establish and maintain the resolution definition control.
- `PCRMR-003-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-02` — Establish and maintain the resolution definition control.
- `PCRMR-003-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-03` — Establish and maintain the resolution definition control.
- `PCRMR-003-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-04` — Establish and maintain the resolution definition control.
- `PCRMR-003-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-05` — Establish and maintain the resolution definition control.
- `PCRMR-003-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-06` — Establish and maintain the resolution definition control.
- `PCRMR-003-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-003-07` — Establish and maintain the resolution definition control.
- `PCRMR-003-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 4. Resolution Domain — Resolution Scope

**Control family:** `PCRMR-004`

The Resolution Scope domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-004-01` — Establish and maintain the resolution scope control.
- `PCRMR-004-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-02` — Establish and maintain the resolution scope control.
- `PCRMR-004-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-03` — Establish and maintain the resolution scope control.
- `PCRMR-004-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-04` — Establish and maintain the resolution scope control.
- `PCRMR-004-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-05` — Establish and maintain the resolution scope control.
- `PCRMR-004-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-06` — Establish and maintain the resolution scope control.
- `PCRMR-004-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-004-07` — Establish and maintain the resolution scope control.
- `PCRMR-004-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 5. Resolution Domain — Resolution Authority

**Control family:** `PCRMR-005`

The Resolution Authority domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-005-01` — Establish and maintain the resolution authority control.
- `PCRMR-005-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-02` — Establish and maintain the resolution authority control.
- `PCRMR-005-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-03` — Establish and maintain the resolution authority control.
- `PCRMR-005-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-04` — Establish and maintain the resolution authority control.
- `PCRMR-005-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-05` — Establish and maintain the resolution authority control.
- `PCRMR-005-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-06` — Establish and maintain the resolution authority control.
- `PCRMR-005-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-005-07` — Establish and maintain the resolution authority control.
- `PCRMR-005-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 6. Resolution Domain — Resolution Criteria

**Control family:** `PCRMR-006`

The Resolution Criteria domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-006-01` — Establish and maintain the resolution criteria control.
- `PCRMR-006-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-02` — Establish and maintain the resolution criteria control.
- `PCRMR-006-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-03` — Establish and maintain the resolution criteria control.
- `PCRMR-006-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-04` — Establish and maintain the resolution criteria control.
- `PCRMR-006-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-05` — Establish and maintain the resolution criteria control.
- `PCRMR-006-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-06` — Establish and maintain the resolution criteria control.
- `PCRMR-006-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-006-07` — Establish and maintain the resolution criteria control.
- `PCRMR-006-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 7. Resolution Domain — Resolution Evidence

**Control family:** `PCRMR-007`

The Resolution Evidence domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-007-01` — Establish and maintain the resolution evidence control.
- `PCRMR-007-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-02` — Establish and maintain the resolution evidence control.
- `PCRMR-007-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-03` — Establish and maintain the resolution evidence control.
- `PCRMR-007-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-04` — Establish and maintain the resolution evidence control.
- `PCRMR-007-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-05` — Establish and maintain the resolution evidence control.
- `PCRMR-007-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-06` — Establish and maintain the resolution evidence control.
- `PCRMR-007-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-007-07` — Establish and maintain the resolution evidence control.
- `PCRMR-007-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 8. Resolution Domain — Resolution Accountability

**Control family:** `PCRMR-008`

The Resolution Accountability domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-008-01` — Establish and maintain the resolution accountability control.
- `PCRMR-008-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-02` — Establish and maintain the resolution accountability control.
- `PCRMR-008-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-03` — Establish and maintain the resolution accountability control.
- `PCRMR-008-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-04` — Establish and maintain the resolution accountability control.
- `PCRMR-008-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-05` — Establish and maintain the resolution accountability control.
- `PCRMR-008-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-06` — Establish and maintain the resolution accountability control.
- `PCRMR-008-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-008-07` — Establish and maintain the resolution accountability control.
- `PCRMR-008-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 9. Resolution Domain — Resolution Timing

**Control family:** `PCRMR-009`

The Resolution Timing domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-009-01` — Establish and maintain the resolution timing control.
- `PCRMR-009-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-02` — Establish and maintain the resolution timing control.
- `PCRMR-009-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-03` — Establish and maintain the resolution timing control.
- `PCRMR-009-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-04` — Establish and maintain the resolution timing control.
- `PCRMR-009-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-05` — Establish and maintain the resolution timing control.
- `PCRMR-009-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-06` — Establish and maintain the resolution timing control.
- `PCRMR-009-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-009-07` — Establish and maintain the resolution timing control.
- `PCRMR-009-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 10. Resolution Domain — Resolution Verification

**Control family:** `PCRMR-010`

The Resolution Verification domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-010-01` — Establish and maintain the resolution verification control.
- `PCRMR-010-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-02` — Establish and maintain the resolution verification control.
- `PCRMR-010-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-03` — Establish and maintain the resolution verification control.
- `PCRMR-010-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-04` — Establish and maintain the resolution verification control.
- `PCRMR-010-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-05` — Establish and maintain the resolution verification control.
- `PCRMR-010-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-06` — Establish and maintain the resolution verification control.
- `PCRMR-010-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-010-07` — Establish and maintain the resolution verification control.
- `PCRMR-010-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 11. Resolution Domain — Resolution Decision

**Control family:** `PCRMR-011`

The Resolution Decision domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-011-01` — Establish and maintain the resolution decision control.
- `PCRMR-011-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-02` — Establish and maintain the resolution decision control.
- `PCRMR-011-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-03` — Establish and maintain the resolution decision control.
- `PCRMR-011-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-04` — Establish and maintain the resolution decision control.
- `PCRMR-011-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-05` — Establish and maintain the resolution decision control.
- `PCRMR-011-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-06` — Establish and maintain the resolution decision control.
- `PCRMR-011-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-011-07` — Establish and maintain the resolution decision control.
- `PCRMR-011-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 12. Resolution Domain — Resolution Closure

**Control family:** `PCRMR-012`

The Resolution Closure domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-012-01` — Establish and maintain the resolution closure control.
- `PCRMR-012-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-02` — Establish and maintain the resolution closure control.
- `PCRMR-012-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-03` — Establish and maintain the resolution closure control.
- `PCRMR-012-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-04` — Establish and maintain the resolution closure control.
- `PCRMR-012-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-05` — Establish and maintain the resolution closure control.
- `PCRMR-012-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-06` — Establish and maintain the resolution closure control.
- `PCRMR-012-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-012-07` — Establish and maintain the resolution closure control.
- `PCRMR-012-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 13. Resolution Domain — Security Resolution

**Control family:** `PCRMR-013`

The Security Resolution domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-013-01` — Establish and maintain the security resolution control.
- `PCRMR-013-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-02` — Establish and maintain the security resolution control.
- `PCRMR-013-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-03` — Establish and maintain the security resolution control.
- `PCRMR-013-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-04` — Establish and maintain the security resolution control.
- `PCRMR-013-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-05` — Establish and maintain the security resolution control.
- `PCRMR-013-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-06` — Establish and maintain the security resolution control.
- `PCRMR-013-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-013-07` — Establish and maintain the security resolution control.
- `PCRMR-013-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 14. Resolution Domain — Resilience Resolution

**Control family:** `PCRMR-014`

The Resilience Resolution domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-014-01` — Establish and maintain the resilience resolution control.
- `PCRMR-014-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-02` — Establish and maintain the resilience resolution control.
- `PCRMR-014-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-03` — Establish and maintain the resilience resolution control.
- `PCRMR-014-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-04` — Establish and maintain the resilience resolution control.
- `PCRMR-014-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-05` — Establish and maintain the resilience resolution control.
- `PCRMR-014-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-06` — Establish and maintain the resilience resolution control.
- `PCRMR-014-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-014-07` — Establish and maintain the resilience resolution control.
- `PCRMR-014-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 15. Resolution Domain — Compliance Resolution

**Control family:** `PCRMR-015`

The Compliance Resolution domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-015-01` — Establish and maintain the compliance resolution control.
- `PCRMR-015-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-02` — Establish and maintain the compliance resolution control.
- `PCRMR-015-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-03` — Establish and maintain the compliance resolution control.
- `PCRMR-015-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-04` — Establish and maintain the compliance resolution control.
- `PCRMR-015-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-05` — Establish and maintain the compliance resolution control.
- `PCRMR-015-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-06` — Establish and maintain the compliance resolution control.
- `PCRMR-015-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-015-07` — Establish and maintain the compliance resolution control.
- `PCRMR-015-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 16. Resolution Domain — Data Resolution

**Control family:** `PCRMR-016`

The Data Resolution domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-016-01` — Establish and maintain the data resolution control.
- `PCRMR-016-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-02` — Establish and maintain the data resolution control.
- `PCRMR-016-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-03` — Establish and maintain the data resolution control.
- `PCRMR-016-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-04` — Establish and maintain the data resolution control.
- `PCRMR-016-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-05` — Establish and maintain the data resolution control.
- `PCRMR-016-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-06` — Establish and maintain the data resolution control.
- `PCRMR-016-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-016-07` — Establish and maintain the data resolution control.
- `PCRMR-016-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 17. Resolution Domain — AI and Agent Resolution

**Control family:** `PCRMR-017`

The AI and Agent Resolution domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-017-01` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-02` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-03` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-04` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-05` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-06` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-017-07` — Establish and maintain the ai and agent resolution control.
- `PCRMR-017-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 18. Resolution Domain — Resolution Failure

**Control family:** `PCRMR-018`

The Resolution Failure domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-018-01` — Establish and maintain the resolution failure control.
- `PCRMR-018-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-02` — Establish and maintain the resolution failure control.
- `PCRMR-018-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-03` — Establish and maintain the resolution failure control.
- `PCRMR-018-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-04` — Establish and maintain the resolution failure control.
- `PCRMR-018-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-05` — Establish and maintain the resolution failure control.
- `PCRMR-018-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-06` — Establish and maintain the resolution failure control.
- `PCRMR-018-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-018-07` — Establish and maintain the resolution failure control.
- `PCRMR-018-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 19. Resolution Domain — Resolution Escalation

**Control family:** `PCRMR-019`

The Resolution Escalation domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-019-01` — Establish and maintain the resolution escalation control.
- `PCRMR-019-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-02` — Establish and maintain the resolution escalation control.
- `PCRMR-019-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-03` — Establish and maintain the resolution escalation control.
- `PCRMR-019-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-04` — Establish and maintain the resolution escalation control.
- `PCRMR-019-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-05` — Establish and maintain the resolution escalation control.
- `PCRMR-019-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-06` — Establish and maintain the resolution escalation control.
- `PCRMR-019-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-019-07` — Establish and maintain the resolution escalation control.
- `PCRMR-019-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## 20. Resolution Domain — Resolution Review and Learning

**Control family:** `PCRMR-020`

The Resolution Review and Learning domain establishes governed mandatory-resolution requirements for post-closure regression.

### Required controls
- `PCRMR-020-01` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-01-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-02` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-02-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-03` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-03-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-04` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-04-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-05` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-05-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-06` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-06-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.
- `PCRMR-020-07` — Establish and maintain the resolution review and learning control.
- `PCRMR-020-07-E` — Preserve trigger, objective, criteria, evidence, verification, authority, accountability, decision and disposition traceability.

```text
CONDITION → RESOLVE → VERIFY → ACCEPT / REOPEN / ESCALATE
```

## Resolution Structure

| Element | Required definition |
|---|---|
| Condition | Material state being resolved |
| Objective | Intended resolution outcome |
| Criteria | Conditions for resolution |
| Action | Containment, remediation or restoration |
| Evidence | Proof of achieved result |
| Verification | Confirmation against criteria |
| Authority | Authorized resolution decision maker |
| Accountability | Accountable role |
| Disposition | Resolved / partial / unresolved / undetermined |
| Reopening | Conditions invalidating resolution |

## Resolution Objective

The objective is to restore, contain or otherwise establish the required governed state so that the original material condition no longer creates unmanaged exposure within the approved scope.

## Resolution Definition

Resolution is the verified achievement of the defined resolution criteria. It requires more than task completion, acknowledgement or administrative closure.

## Resolution Scope

Scope shall identify the affected systems, services, controls, processes, data, environments, users, dependencies and boundaries covered by the resolution.

## Resolution Authority

Authority shall define who may determine that resolution criteria are met, who may accept the result and who may reopen or escalate the condition.

## Resolution Criteria

Criteria shall be explicit, measurable where appropriate and aligned to the original condition and required state.

```text
CONDITION
↓
RESOLUTION CRITERIA
├── SATISFIED → RESOLUTION ELIGIBLE
└── NOT SATISFIED → CONTINUE / ESCALATE
```

## Resolution Evidence

Evidence shall demonstrate that the condition has been controlled or resolved. It shall be current, traceable and linked to the relevant action and criteria.

## Resolution Accountability

Accountability shall remain explicit throughout resolution. Operational execution may be delegated, but the accountable role shall remain identifiable until authorized disposition.

## Resolution Timing

Resolution timing shall reflect the required risk treatment and response deadlines. Overdue resolution shall trigger escalation rather than silent extension.

## Resolution Verification

Verification shall independently or appropriately confirm that resolution criteria are met and that the result is stable enough for the intended disposition.

```text
ACTION COMPLETED
↓
VERIFY CURRENT STATE
↓
CRITERIA SATISFIED?
├── YES → RESOLVED
└── NO → PARTIAL / UNRESOLVED / REOPEN
```

## Resolution Decision

The resolution decision shall explicitly classify the outcome and identify the authority.

```text
VERIFIED RESULT
├── RESOLVED
├── PARTIALLY RESOLVED
├── UNRESOLVED
└── UNDETERMINED
```

## Resolution Closure

Closure shall occur only after resolution evidence, verification, authority and disposition requirements are satisfied. Administrative closure shall not override unresolved material conditions.

## Security Resolution

Security resolution shall confirm restoration or adequate control of the affected security state, including relevant access, exposure, vulnerability or boundary conditions.

## Resilience Resolution

Resilience resolution shall confirm restoration or controlled operation of required service, recovery, continuity, capacity and dependency conditions.

## Compliance Resolution

Compliance resolution shall confirm that the applicable non-conformance or exposure has been addressed to the required standard and that evidence supports the determination.

## Data Resolution

Data resolution shall confirm restoration or control of required integrity, quality, lineage, access, retention and authorized-use conditions.

## AI and Agent Resolution

AI and agent resolution shall confirm that authority, policy, data, tool, autonomy and behavioural boundaries are restored or appropriately constrained.

```text
AI / AGENT CONDITION
↓
CONTAIN / REMEDIATE / LIMIT
↓
VERIFY GOVERNED BEHAVIOUR
↓
BOUNDARIES RESTORED?
├── YES → RESOLVED / ACCEPT
└── NO → REOPEN / SUSPEND / ESCALATE
```

## Resolution Failure

Failure to achieve resolution criteria, inability to verify, recurrence of the condition or discovery of residual material exposure shall prevent normal closure.

```text
RESOLUTION FAILURE
↓
PROTECT REQUIRED STATE
↓
CLASSIFY RESIDUAL RISK
↓
REMEDIATE / REOPEN / ESCALATE
↓
REVERIFY
```

## Resolution Escalation

Escalation shall occur when resolution is overdue, disputed, materially incomplete, repeatedly unsuccessful, blocked by authority or resources, or unable to establish an acceptable governed state.

## Resolution Review and Learning

Resolution outcomes shall be reviewed for recurring causes, ineffective remediation, weak criteria, premature closure, repeated reopening and systemic governance deficiencies.

## Resolution Determination Model
```text
MATERIAL CONDITION
↓
RESOLUTION ACTION PERFORMED?
├── NO → CONTINUE / ESCALATE
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → UNDETERMINED / CONTINUE
└── YES
     ↓
VERIFICATION PASSED?
├── NO → PARTIAL / UNRESOLVED / REOPEN
└── YES
     ↓
RESOLUTION CRITERIA SATISFIED?
├── NO → CONTINUE / ESCALATE
└── YES → RESOLVED / ACCEPT FOR CLOSURE
```

## Resolution Record
| Field | Required |
|---|---|
| Resolution ID | Yes |
| Original Trigger / Alert / Escalation ID | Yes |
| Resolution Objective | Yes |
| Scope | Yes |
| Criteria Version | Yes |
| Actions | Yes |
| Evidence References | Yes |
| Verification Reference | Yes |
| Authority | Yes |
| Accountability | Yes |
| Result | Yes |
| Residual Risk | Where applicable |
| Reopening Conditions | Yes |
| Closure Decision | Yes |

## Resolution Outcome Model
```text
RESOLVED
    → REQUIRED STATE RESTORED / CONTROLLED
PARTIALLY RESOLVED
    → MATERIAL REMNANT REMAINS / GOVERNED FOLLOW-ON REQUIRED
UNRESOLVED
    → CONDITION REMAINS / ACTIVE RESPONSE REQUIRED
UNDETERMINED
    → EVIDENCE OR VERIFICATION INSUFFICIENT
```

## Resolution Reopening
A resolution shall be reopened when new evidence demonstrates that the condition persisted, recurred, was incorrectly classified, exceeded the original scope, or the resolution basis is no longer valid.

```text
RESOLVED
↓
NEW MATERIAL EVIDENCE / REGRESSION
↓
REOPEN
↓
REASSESS
↓
REVALIDATE
↓
RESOLVE AGAIN / ESCALATE
```

## Resolution Anti-Gaming Control
Resolution shall not be declared merely because a ticket is completed, a remediation task is marked done, an alert is acknowledged or stakeholders require closure. The governed condition and resolution criteria remain controlling.

## Resolution Change Control
Changes to resolution criteria, verification methods, authority, closure rules, residual-risk treatment or reopening conditions shall be governed, approved, versioned and effective-dated.

```text
CURRENT RESOLUTION MODEL
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

Historical resolution decisions, evidence, verification results and reopening events shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-resolution layer beneath mandatory escalation. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, monitoring, alerting or escalation layers.

## Governance-to-Resolution Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → ESCALATION → MANDATORY RESOLUTION → VERIFICATION → ACCEPT / REOPEN / REASSESS
```

## Complete Resolution Chain
```text
MANDATORY STATE → VERIFY → EVIDENCE → MEASURE → THRESHOLD → CLASSIFY → CONSEQUENCE → RESPOND → EFFECTIVENESS → REASSESS → REVALIDATE → ACCEPT → RELY → MONITOR → ALERT → ESCALATE → RESOLVE → VERIFY → ACCEPT / REOPEN
```

## Next Document
`EA-IMETA-PC-RG-021` — Mandatory Closure

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL ESCALATED CONDITION TO ACHIEVE AN EXPLICIT, EVIDENCE-BASED AND VERIFIED RESOLUTION BEFORE NORMAL CLOSURE, WITH PARTIAL, UNRESOLVED OR UNDETERMINED CONDITIONS REMAINING GOVERNED, AND WITH REOPENING, REASSESSMENT OR FURTHER ESCALATION AVAILABLE WHEN THE RESOLUTION BASIS FAILS.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01
