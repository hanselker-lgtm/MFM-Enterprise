# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01

## Physical File ID
`EA-IMETA-PC-RG-036`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-036` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Escalation Resolution Verification |
| Parent | EA-IMETA-PC-RG-035 — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-resolution-verification layer defining how a claimed resolution is independently and sufficiently verified against the current required state, approved criteria, evidence requirements and relevant boundaries before resolution is accepted as valid and before downstream revalidation, acceptance, reliance restoration or closure may proceed.

## Core Principle
Resolution is a claim; verification establishes whether that claim is supported. Verification shall test the actual restored state rather than merely confirming that remediation activity was completed.

```text
RESOLUTION CLAIM
      ↓
DEFINE CURRENT REQUIRED STATE + CRITERIA
      ↓
VERIFY CONTROLS + OUTCOMES + BOUNDARIES
      ↓
REVIEW EVIDENCE + MEASUREMENTS
      ↓
VALID / PARTIAL / INVALID / UNKNOWN
      ↓
ACCEPT RESOLUTION / REMEDIATE / REOPEN / ESCALATE
```

## Verification Quality Test
```text
DEFINED RESOLUTION CLAIM
+
CURRENT CRITERIA
+
APPROPRIATE TEST / VERIFICATION METHOD
+
SUFFICIENT EVIDENCE
+
CONTROL + OUTCOME + BOUNDARY VERIFICATION
+
AUTHORIZED DECISION
=
VALID GOVERNED RESOLUTION VERIFICATION
```

## Verification Status Model
```text
NOT READY
PLANNED
READY
IN PROGRESS
UNDER REVIEW
VERIFIED
PARTIALLY VERIFIED
FAILED
UNKNOWN
REOPENED
ESCALATED
SUPERSEDED
```

## Verification Invariants

```text
EVERY MATERIAL RESOLUTION SHALL BE VERIFIED BEFORE IT IS TREATED AS FULLY RESOLVED
```

```text
VERIFICATION SHALL TEST THE CURRENT REQUIRED STATE, NOT ONLY REMEDIATION COMPLETION
```

```text
VERIFICATION CRITERIA SHALL BE CURRENT, APPROVED AND TRACEABLE
```

```text
CONTROL CONDITIONS AND INTENDED OUTCOMES SHALL BOTH BE VERIFIED WHERE MATERIAL
```

```text
BOUNDARIES, DEPENDENCIES AND ASSUMPTIONS SHALL BE VERIFIED WHERE MATERIAL
```

```text
PARTIAL VERIFICATION SHALL REMAIN DISTINCT FROM FULL VERIFICATION
```

```text
UNKNOWN SHALL NOT BE TREATED AS VERIFIED
```

```text
FAILED VERIFICATION SHALL PREVENT PREMATURE RESOLUTION ACCEPTANCE
```

```text
VERIFICATION EVIDENCE SHALL BE TRACEABLE TO THE RESOLUTION CLAIM
```

```text
INDEPENDENCE SHALL BE APPLIED WHERE MATERIALITY OR GOVERNANCE REQUIRES IT
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE VERIFICATION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT VERIFICATION SHALL CONFIRM AUTHORITY, POLICY, TOOL, DATA, AUTONOMY AND BEHAVIOURAL BOUNDARIES
```

```text
VERIFICATION SHALL CONSIDER SUSTAINABILITY AND REGRESSION RISK WHERE REQUIRED
```

```text
VERIFICATION RESULTS SHALL REMAIN HISTORICALLY TRACEABLE
```

```text
REPEATED VERIFICATION FAILURE SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Verification Domain — Resolution Verification Governance

**Control family:** `PCRVFY-001`

The Resolution Verification Governance domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-001-01` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-02` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-03` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-04` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-05` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-06` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-001-07` — Establish and maintain the resolution verification governance control.
- `PCRVFY-001-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 2. Verification Domain — Resolution Verification Objective

**Control family:** `PCRVFY-002`

The Resolution Verification Objective domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-002-01` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-02` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-03` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-04` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-05` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-06` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-002-07` — Establish and maintain the resolution verification objective control.
- `PCRVFY-002-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 3. Verification Domain — Resolution Verification Definition

**Control family:** `PCRVFY-003`

The Resolution Verification Definition domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-003-01` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-02` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-03` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-04` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-05` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-06` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-003-07` — Establish and maintain the resolution verification definition control.
- `PCRVFY-003-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 4. Verification Domain — Resolution Verification Scope

**Control family:** `PCRVFY-004`

The Resolution Verification Scope domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-004-01` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-02` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-03` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-04` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-05` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-06` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-004-07` — Establish and maintain the resolution verification scope control.
- `PCRVFY-004-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 5. Verification Domain — Resolution Verification Authority

**Control family:** `PCRVFY-005`

The Resolution Verification Authority domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-005-01` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-02` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-03` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-04` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-05` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-06` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-005-07` — Establish and maintain the resolution verification authority control.
- `PCRVFY-005-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 6. Verification Domain — Resolution Verification Criteria

**Control family:** `PCRVFY-006`

The Resolution Verification Criteria domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-006-01` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-02` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-03` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-04` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-05` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-06` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-006-07` — Establish and maintain the resolution verification criteria control.
- `PCRVFY-006-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 7. Verification Domain — Resolution Verification Preconditions

**Control family:** `PCRVFY-007`

The Resolution Verification Preconditions domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-007-01` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-02` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-03` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-04` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-05` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-06` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-007-07` — Establish and maintain the resolution verification preconditions control.
- `PCRVFY-007-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 8. Verification Domain — Resolution Verification Evidence

**Control family:** `PCRVFY-008`

The Resolution Verification Evidence domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-008-01` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-02` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-03` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-04` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-05` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-06` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-008-07` — Establish and maintain the resolution verification evidence control.
- `PCRVFY-008-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 9. Verification Domain — Resolution Verification Method

**Control family:** `PCRVFY-009`

The Resolution Verification Method domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-009-01` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-02` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-03` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-04` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-05` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-06` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-009-07` — Establish and maintain the resolution verification method control.
- `PCRVFY-009-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 10. Verification Domain — Resolution Verification Decision

**Control family:** `PCRVFY-010`

The Resolution Verification Decision domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-010-01` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-02` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-03` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-04` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-05` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-06` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-010-07` — Establish and maintain the resolution verification decision control.
- `PCRVFY-010-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 11. Verification Domain — Resolution Verification Accountability

**Control family:** `PCRVFY-011`

The Resolution Verification Accountability domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-011-01` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-02` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-03` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-04` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-05` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-06` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-011-07` — Establish and maintain the resolution verification accountability control.
- `PCRVFY-011-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 12. Verification Domain — Resolution Verification Timing

**Control family:** `PCRVFY-012`

The Resolution Verification Timing domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-012-01` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-02` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-03` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-04` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-05` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-06` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-012-07` — Establish and maintain the resolution verification timing control.
- `PCRVFY-012-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 13. Verification Domain — Security Resolution Verification

**Control family:** `PCRVFY-013`

The Security Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-013-01` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-02` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-03` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-04` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-05` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-06` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-013-07` — Establish and maintain the security resolution verification control.
- `PCRVFY-013-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 14. Verification Domain — Resilience Resolution Verification

**Control family:** `PCRVFY-014`

The Resilience Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-014-01` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-02` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-03` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-04` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-05` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-06` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-014-07` — Establish and maintain the resilience resolution verification control.
- `PCRVFY-014-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 15. Verification Domain — Compliance Resolution Verification

**Control family:** `PCRVFY-015`

The Compliance Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-015-01` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-02` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-03` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-04` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-05` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-06` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-015-07` — Establish and maintain the compliance resolution verification control.
- `PCRVFY-015-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 16. Verification Domain — Data Resolution Verification

**Control family:** `PCRVFY-016`

The Data Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-016-01` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-02` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-03` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-04` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-05` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-06` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-016-07` — Establish and maintain the data resolution verification control.
- `PCRVFY-016-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 17. Verification Domain — AI and Agent Resolution Verification

**Control family:** `PCRVFY-017`

The AI and Agent Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-017-01` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-02` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-03` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-04` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-05` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-06` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-017-07` — Establish and maintain the ai and agent resolution verification control.
- `PCRVFY-017-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 18. Verification Domain — Resolution Verification Failure

**Control family:** `PCRVFY-018`

The Resolution Verification Failure domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-018-01` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-02` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-03` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-04` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-05` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-06` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-018-07` — Establish and maintain the resolution verification failure control.
- `PCRVFY-018-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 19. Verification Domain — Resolution Verification Independence

**Control family:** `PCRVFY-019`

The Resolution Verification Independence domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-019-01` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-02` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-03` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-04` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-05` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-06` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-019-07` — Establish and maintain the resolution verification independence control.
- `PCRVFY-019-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## 20. Verification Domain — Resolution Verification Review and Learning

**Control family:** `PCRVFY-020`

The Resolution Verification Review and Learning domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRVFY-020-01` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-01-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-02` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-02-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-03` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-03-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-04` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-04-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-05` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-05-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-06` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-06-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.
- `PCRVFY-020-07` — Establish and maintain the resolution verification review and learning control.
- `PCRVFY-020-07-E` — Preserve resolution claim, criteria, method, evidence, result, authority and follow-on traceability.

```text
RESOLVE → VERIFY → ACCEPT / FAIL / REOPEN
```

## Resolution Verification Structure

| Element | Required definition |
|---|---|
| Resolution Claim | State claimed to be restored |
| Required State | State that must be demonstrated |
| Criteria | Current verification conditions |
| Method | Test / observation / measurement |
| Evidence | Supporting proof |
| Result | Verification determination |
| Authority | Authorized reviewer / approver |
| Follow-on | Acceptance / remediation / reopening |

## Resolution Verification Objective

Determine whether the claimed resolution has actually restored the required governed state sufficiently to support the next authorized lifecycle decision.

## Resolution Verification Definition

Resolution verification is the controlled examination of a resolved condition to establish, using sufficient evidence, whether required controls, outcomes and boundaries have been restored.

## Resolution Verification Scope

Scope shall include the original escalated condition, remediation, affected controls, outcomes, dependencies, boundaries, downstream effects and any conditions identified during resolution.

## Resolution Verification Authority

Authority shall define who may perform, witness, challenge, approve and reject verification and who may authorize progression after verification.

## Resolution Verification Criteria

Criteria shall define what constitutes verified, partially verified, failed or unknown.

```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA SATISFIED?
├── NO → FAIL / REMEDIATE
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → UNKNOWN / COMPLETE EVIDENCE
└── YES
     ↓
CONTROL + OUTCOME + BOUNDARY VERIFIED?
├── NO → PARTIAL / FAIL
└── YES → VERIFIED
```

## Resolution Verification Preconditions

Preconditions include completed remediation or an approved alternative, current criteria, defined scope, available evidence, test readiness and appropriate authority.

## Resolution Verification Evidence

Evidence shall be current, attributable, traceable, reproducible where applicable and sufficient to support the verification determination.

## Resolution Verification Method

Verification methods may include testing, inspection, observation, measurement, simulation, independent review, evidence review and controlled operational confirmation as appropriate.

```text
CLAIM
↓
METHOD
↓
TEST / OBSERVE / MEASURE
↓
COMPARE WITH CRITERIA
↓
DETERMINE RESULT
```

## Resolution Verification Decision

The verification decision shall explicitly state verified, partially verified, failed or unknown.

```text
VERIFIED → PROCEED TO REQUIRED NEXT STATE
PARTIAL → COMPLETE GAPS
FAILED → REMEDIATE / REOPEN
UNKNOWN → RESTORE EVIDENCE / INVESTIGATE
```

## Resolution Verification Accountability

Verification accountability shall remain explicit. The person performing a test, the reviewer and the resolution authority may be separate roles.

## Resolution Verification Timing

Verification shall occur within the validity period of the evidence and before resolution is used as a basis for acceptance, reliance restoration or closure.

## Security Resolution Verification

Verify that security controls, access boundaries, exposure, detection and protective measures meet current criteria after resolution.

## Resilience Resolution Verification

Verify availability, recovery, continuity, capacity and dependency conditions and demonstrate that resilience objectives are restored where applicable.

## Compliance Resolution Verification

Verify applicable obligations, controls, evidence and formal disposition requirements are satisfied.

## Data Resolution Verification

Verify integrity, quality, lineage, access, retention, authorized use and relevant downstream data effects.

## AI and Agent Resolution Verification

Verify restoration of AI/agent authority, policy adherence, tool permissions, data boundaries, autonomy limits and behavioural controls.

```text
RESOLVED AI / AGENT STATE
↓
VERIFY AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY + BEHAVIOUR
↓
ALL REQUIRED BOUNDARIES VALID?
├── YES → VERIFIED
└── NO → FAIL / LIMIT / REOPEN
```

## Resolution Verification Failure

Failure to verify the required state shall prevent full resolution acceptance and shall trigger remediation, further evidence, reopening or escalation as appropriate.

```text
VERIFICATION FAILURE
↓
MAINTAIN PROTECTION
↓
IDENTIFY GAP
↓
REMEDIATE / REVERIFY
↓
REOPEN / ESCALATE IF REQUIRED
```

## Resolution Verification Independence

Where materiality warrants it, verification shall be performed or reviewed independently from the role responsible for remediation to reduce confirmation bias and conflicts of interest.

## Resolution Verification Review and Learning

Reviews shall identify weak verification methods, inadequate criteria, recurring failures, false confidence, evidence gaps and opportunities to improve resolution controls.

## Verification Determination Model
```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
METHOD APPROPRIATE?
├── NO → REDESIGN / APPROVE METHOD
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → UNKNOWN / COMPLETE EVIDENCE
└── YES
     ↓
CONTROL + OUTCOME + BOUNDARY VERIFIED?
├── NO → PARTIAL / FAIL
└── YES
     ↓
RESULT REVIEWED BY AUTHORIZED ROLE?
├── NO → REVIEW / ESCALATE
└── YES → VERIFIED
```

## Verification Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Verified | Required state demonstrated | Proceed to acceptance / reliance path |
| Partially Verified | Some requirements demonstrated | Complete gaps / reverify |
| Failed | Required state not demonstrated | Remediate / reopen |
| Unknown | Evidence insufficient | Restore evidence / investigate |

## Verification Record
| Field | Required |
|---|---|
| Verification ID | Yes |
| Resolution ID | Yes |
| Resolution Claim | Yes |
| Required State | Yes |
| Criteria Version | Yes |
| Method | Yes |
| Test / Observation References | Yes |
| Evidence References | Yes |
| Result | Yes |
| Reviewer | Yes |
| Authority | Yes |
| Follow-on Decision | Yes |

## Verification Coverage
Verification coverage shall be sufficient to detect material residual defects, boundary failures, dependency failures and unintended consequences that could invalidate the resolution claim.

```text
RESOLUTION CLAIM
↓
WHAT COULD MAKE IT INVALID?
↓
WHAT VERIFICATION WOULD DETECT THAT?
↓
IS THAT VERIFICATION PERFORMED?
├── NO → COVERAGE GAP
└── YES → VALIDATE
```

## Verification Blind Spots
Known blind spots shall be documented and assessed. Material blind spots may require compensating controls, additional testing, restricted reliance or reopening of the resolution.

## Verification Change Control
Changes to verification criteria, methods, sampling, evidence standards, independence requirements or authority shall be governed, approved, versioned and effective-dated.

```text
CURRENT VERIFICATION MODEL
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

## Verification Anti-Gaming Control
Verification shall not be narrowed merely to produce a successful result. The verification scope shall remain aligned with the actual required state and material ways the resolution could fail.

Historical verification plans, tests, observations, measurements, failures, reviews, approvals and results shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-resolution-verification layer beneath mandatory escalation resolution. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, monitoring, alerting, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Verification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → ESCALATION → RESOLUTION → MANDATORY VERIFICATION → CLOSURE → POST-CLOSURE MONITORING → REGRESSION DETECTION → REGRESSION CLASSIFICATION → REGRESSION CONSEQUENCE → REGRESSION RESPONSE → RESPONSE EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → ESCALATION → RESOLUTION → VERIFICATION
```

## Complete Verification Chain
```text
RESOLVE → DEFINE REQUIRED STATE → DEFINE CRITERIA → SELECT METHOD → TEST / OBSERVE / MEASURE → COLLECT EVIDENCE → VERIFY CONTROLS + OUTCOMES + BOUNDARIES → REVIEW → VERIFIED / PARTIAL / FAILED / UNKNOWN → ACCEPT / REMEDIATE / REOPEN → REVALIDATE → RESTORE RELIANCE → MONITOR
```

## Next Document
`EA-IMETA-PC-RG-037` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification Revalidation

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL RESOLUTION CLAIMS TO BE VERIFIED AGAINST THE CURRENT REQUIRED STATE, APPROVED CRITERIA AND SUFFICIENT EVIDENCE BEFORE RESOLUTION IS TREATED AS VALID, WITH CONTROL, OUTCOME AND BOUNDARY VERIFICATION, APPROPRIATE INDEPENDENCE, TRACEABILITY AND EXPLICIT HANDLING OF PARTIAL, FAILED OR UNKNOWN RESULTS.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01
