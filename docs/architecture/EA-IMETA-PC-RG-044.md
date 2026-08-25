# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01

## Physical File ID
`EA-IMETA-PC-RG-044`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-044` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Resolution Verification |
| Parent | EA-IMETA-PC-RG-043 — Mandatory Restoration Monitoring Alerting Escalation Resolution |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-resolution-verification layer defining how a declared resolution is independently or systematically checked against the required current state before it may progress to revalidation, reacceptance or restoration of reliance.

## Core Principle
Resolution is a claim about a controlled state. Verification determines whether that claim is supported by current, sufficient and traceable evidence. A completed action is not equivalent to a verified outcome.

```text
RESOLUTION CLAIM
      ↓
DEFINE CURRENT REQUIRED STATE + CRITERIA
      ↓
CHECK CONTROLS + OUTCOMES + BOUNDARIES
      ↓
REVIEW EVIDENCE + MEASUREMENTS
      ↓
VERIFIED / PARTIAL / FAILED / UNKNOWN
      ↓
REVALIDATE / REOPEN / RESTRICT / PROCEED
```

## Verification Quality Test
```text
RESOLUTION CLAIM
+
CURRENT CRITERIA
+
APPROPRIATE METHOD
+
SUFFICIENT EVIDENCE
+
CURRENT STATE OBSERVED
+
BOUNDARIES CHECKED
+
AUTHORIZED REVIEW
=
VALID GOVERNED VERIFICATION
```

## Verification Status Model
```text
NOT READY
PLANNED
IN VERIFICATION
VERIFIED
PARTIALLY VERIFIED
FAILED
UNKNOWN
REOPENED
SUPERSEDED
```

## Verification Invariants

```text
EVERY MATERIAL RESOLUTION SHALL BE VERIFIED WHERE REQUIRED BEFORE REVALIDATION OR REACCEPTANCE
```

```text
VERIFICATION SHALL TEST THE CURRENT STATE, NOT MERELY THE ACTION COMPLETION
```

```text
VERIFICATION SHALL USE CURRENT CRITERIA
```

```text
VERIFICATION SHALL CONSIDER CONTROLS, OUTCOMES AND BOUNDARIES
```

```text
EVIDENCE SHALL BE SUFFICIENT, CURRENT, ATTRIBUTABLE AND TRACEABLE
```

```text
VERIFICATION METHODS SHALL BE APPROPRIATE TO MATERIALITY
```

```text
PARTIAL VERIFICATION SHALL NOT BE PRESENTED AS FULL VERIFICATION
```

```text
UNKNOWN SHALL REMAIN DISTINCT FROM VERIFIED
```

```text
FAILED VERIFICATION SHALL PREVENT UNCONTROLLED PROGRESSION
```

```text
VERIFICATION SHALL REMAIN DISTINCT FROM REVALIDATION AND REACCEPTANCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE VERIFICATION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT VERIFICATION SHALL CHECK AUTHORITY, POLICY, TOOLS, DATA, AUTONOMY AND BEHAVIOURAL CONDITIONS
```

```text
INDEPENDENT REVIEW SHALL BE USED WHERE MATERIALITY REQUIRES IT
```

```text
VERIFICATION RESULTS SHALL BE HISTORICALLY TRACEABLE
```

```text
REPEATED VERIFICATION FAILURE SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Verification Domain — Resolution Verification Governance

**Control family:** `PCRV-001`

The Resolution Verification Governance domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-001-01` — Establish and maintain the resolution verification governance control.
- `PCRV-001-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-02` — Establish and maintain the resolution verification governance control.
- `PCRV-001-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-03` — Establish and maintain the resolution verification governance control.
- `PCRV-001-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-04` — Establish and maintain the resolution verification governance control.
- `PCRV-001-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-05` — Establish and maintain the resolution verification governance control.
- `PCRV-001-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-06` — Establish and maintain the resolution verification governance control.
- `PCRV-001-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-001-07` — Establish and maintain the resolution verification governance control.
- `PCRV-001-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 2. Verification Domain — Resolution Verification Objective

**Control family:** `PCRV-002`

The Resolution Verification Objective domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-002-01` — Establish and maintain the resolution verification objective control.
- `PCRV-002-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-02` — Establish and maintain the resolution verification objective control.
- `PCRV-002-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-03` — Establish and maintain the resolution verification objective control.
- `PCRV-002-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-04` — Establish and maintain the resolution verification objective control.
- `PCRV-002-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-05` — Establish and maintain the resolution verification objective control.
- `PCRV-002-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-06` — Establish and maintain the resolution verification objective control.
- `PCRV-002-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-002-07` — Establish and maintain the resolution verification objective control.
- `PCRV-002-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 3. Verification Domain — Resolution Verification Definition

**Control family:** `PCRV-003`

The Resolution Verification Definition domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-003-01` — Establish and maintain the resolution verification definition control.
- `PCRV-003-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-02` — Establish and maintain the resolution verification definition control.
- `PCRV-003-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-03` — Establish and maintain the resolution verification definition control.
- `PCRV-003-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-04` — Establish and maintain the resolution verification definition control.
- `PCRV-003-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-05` — Establish and maintain the resolution verification definition control.
- `PCRV-003-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-06` — Establish and maintain the resolution verification definition control.
- `PCRV-003-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-003-07` — Establish and maintain the resolution verification definition control.
- `PCRV-003-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 4. Verification Domain — Resolution Verification Scope

**Control family:** `PCRV-004`

The Resolution Verification Scope domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-004-01` — Establish and maintain the resolution verification scope control.
- `PCRV-004-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-02` — Establish and maintain the resolution verification scope control.
- `PCRV-004-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-03` — Establish and maintain the resolution verification scope control.
- `PCRV-004-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-04` — Establish and maintain the resolution verification scope control.
- `PCRV-004-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-05` — Establish and maintain the resolution verification scope control.
- `PCRV-004-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-06` — Establish and maintain the resolution verification scope control.
- `PCRV-004-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-004-07` — Establish and maintain the resolution verification scope control.
- `PCRV-004-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 5. Verification Domain — Resolution Verification Authority

**Control family:** `PCRV-005`

The Resolution Verification Authority domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-005-01` — Establish and maintain the resolution verification authority control.
- `PCRV-005-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-02` — Establish and maintain the resolution verification authority control.
- `PCRV-005-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-03` — Establish and maintain the resolution verification authority control.
- `PCRV-005-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-04` — Establish and maintain the resolution verification authority control.
- `PCRV-005-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-05` — Establish and maintain the resolution verification authority control.
- `PCRV-005-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-06` — Establish and maintain the resolution verification authority control.
- `PCRV-005-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-005-07` — Establish and maintain the resolution verification authority control.
- `PCRV-005-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 6. Verification Domain — Resolution Verification Criteria

**Control family:** `PCRV-006`

The Resolution Verification Criteria domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-006-01` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-02` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-03` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-04` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-05` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-06` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-006-07` — Establish and maintain the resolution verification criteria control.
- `PCRV-006-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 7. Verification Domain — Resolution Verification Preconditions

**Control family:** `PCRV-007`

The Resolution Verification Preconditions domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-007-01` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-02` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-03` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-04` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-05` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-06` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-007-07` — Establish and maintain the resolution verification preconditions control.
- `PCRV-007-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 8. Verification Domain — Resolution Verification Evidence

**Control family:** `PCRV-008`

The Resolution Verification Evidence domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-008-01` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-02` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-03` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-04` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-05` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-06` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-008-07` — Establish and maintain the resolution verification evidence control.
- `PCRV-008-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 9. Verification Domain — Resolution Verification Method

**Control family:** `PCRV-009`

The Resolution Verification Method domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-009-01` — Establish and maintain the resolution verification method control.
- `PCRV-009-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-02` — Establish and maintain the resolution verification method control.
- `PCRV-009-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-03` — Establish and maintain the resolution verification method control.
- `PCRV-009-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-04` — Establish and maintain the resolution verification method control.
- `PCRV-009-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-05` — Establish and maintain the resolution verification method control.
- `PCRV-009-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-06` — Establish and maintain the resolution verification method control.
- `PCRV-009-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-009-07` — Establish and maintain the resolution verification method control.
- `PCRV-009-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 10. Verification Domain — Resolution Verification Decision

**Control family:** `PCRV-010`

The Resolution Verification Decision domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-010-01` — Establish and maintain the resolution verification decision control.
- `PCRV-010-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-02` — Establish and maintain the resolution verification decision control.
- `PCRV-010-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-03` — Establish and maintain the resolution verification decision control.
- `PCRV-010-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-04` — Establish and maintain the resolution verification decision control.
- `PCRV-010-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-05` — Establish and maintain the resolution verification decision control.
- `PCRV-010-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-06` — Establish and maintain the resolution verification decision control.
- `PCRV-010-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-010-07` — Establish and maintain the resolution verification decision control.
- `PCRV-010-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 11. Verification Domain — Resolution Verification Accountability

**Control family:** `PCRV-011`

The Resolution Verification Accountability domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-011-01` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-02` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-03` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-04` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-05` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-06` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-011-07` — Establish and maintain the resolution verification accountability control.
- `PCRV-011-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 12. Verification Domain — Resolution Verification Timing

**Control family:** `PCRV-012`

The Resolution Verification Timing domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-012-01` — Establish and maintain the resolution verification timing control.
- `PCRV-012-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-02` — Establish and maintain the resolution verification timing control.
- `PCRV-012-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-03` — Establish and maintain the resolution verification timing control.
- `PCRV-012-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-04` — Establish and maintain the resolution verification timing control.
- `PCRV-012-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-05` — Establish and maintain the resolution verification timing control.
- `PCRV-012-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-06` — Establish and maintain the resolution verification timing control.
- `PCRV-012-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-012-07` — Establish and maintain the resolution verification timing control.
- `PCRV-012-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 13. Verification Domain — Security Resolution Verification

**Control family:** `PCRV-013`

The Security Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-013-01` — Establish and maintain the security resolution verification control.
- `PCRV-013-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-02` — Establish and maintain the security resolution verification control.
- `PCRV-013-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-03` — Establish and maintain the security resolution verification control.
- `PCRV-013-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-04` — Establish and maintain the security resolution verification control.
- `PCRV-013-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-05` — Establish and maintain the security resolution verification control.
- `PCRV-013-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-06` — Establish and maintain the security resolution verification control.
- `PCRV-013-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-013-07` — Establish and maintain the security resolution verification control.
- `PCRV-013-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 14. Verification Domain — Resilience Resolution Verification

**Control family:** `PCRV-014`

The Resilience Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-014-01` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-02` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-03` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-04` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-05` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-06` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-014-07` — Establish and maintain the resilience resolution verification control.
- `PCRV-014-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 15. Verification Domain — Compliance Resolution Verification

**Control family:** `PCRV-015`

The Compliance Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-015-01` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-02` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-03` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-04` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-05` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-06` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-015-07` — Establish and maintain the compliance resolution verification control.
- `PCRV-015-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 16. Verification Domain — Data Resolution Verification

**Control family:** `PCRV-016`

The Data Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-016-01` — Establish and maintain the data resolution verification control.
- `PCRV-016-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-02` — Establish and maintain the data resolution verification control.
- `PCRV-016-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-03` — Establish and maintain the data resolution verification control.
- `PCRV-016-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-04` — Establish and maintain the data resolution verification control.
- `PCRV-016-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-05` — Establish and maintain the data resolution verification control.
- `PCRV-016-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-06` — Establish and maintain the data resolution verification control.
- `PCRV-016-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-016-07` — Establish and maintain the data resolution verification control.
- `PCRV-016-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 17. Verification Domain — AI and Agent Resolution Verification

**Control family:** `PCRV-017`

The AI and Agent Resolution Verification domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-017-01` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-02` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-03` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-04` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-05` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-06` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-017-07` — Establish and maintain the ai and agent resolution verification control.
- `PCRV-017-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 18. Verification Domain — Resolution Verification Failure

**Control family:** `PCRV-018`

The Resolution Verification Failure domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-018-01` — Establish and maintain the resolution verification failure control.
- `PCRV-018-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-02` — Establish and maintain the resolution verification failure control.
- `PCRV-018-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-03` — Establish and maintain the resolution verification failure control.
- `PCRV-018-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-04` — Establish and maintain the resolution verification failure control.
- `PCRV-018-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-05` — Establish and maintain the resolution verification failure control.
- `PCRV-018-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-06` — Establish and maintain the resolution verification failure control.
- `PCRV-018-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-018-07` — Establish and maintain the resolution verification failure control.
- `PCRV-018-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 19. Verification Domain — Resolution Verification Independence

**Control family:** `PCRV-019`

The Resolution Verification Independence domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-019-01` — Establish and maintain the resolution verification independence control.
- `PCRV-019-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-02` — Establish and maintain the resolution verification independence control.
- `PCRV-019-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-03` — Establish and maintain the resolution verification independence control.
- `PCRV-019-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-04` — Establish and maintain the resolution verification independence control.
- `PCRV-019-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-05` — Establish and maintain the resolution verification independence control.
- `PCRV-019-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-06` — Establish and maintain the resolution verification independence control.
- `PCRV-019-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-019-07` — Establish and maintain the resolution verification independence control.
- `PCRV-019-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 20. Verification Domain — Resolution Verification Review and Learning

**Control family:** `PCRV-020`

The Resolution Verification Review and Learning domain establishes governed mandatory-verification requirements.

### Required controls
- `PCRV-020-01` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-02` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-03` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-04` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-05` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-06` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.
- `PCRV-020-07` — Establish and maintain the resolution verification review and learning control.
- `PCRV-020-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination, reviewer and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## Resolution Verification Structure

| Element | Required definition |
|---|---|
| Resolution Claim | State claimed to be restored |
| Required State | Current target state |
| Criteria | Acceptance/verification requirements |
| Method | Verification approach |
| Evidence | Supporting basis |
| Observation | Actual current state |
| Determination | Verification result |
| Follow-on | Revalidation / reopening / restriction |

## Resolution Verification Objective

Determine whether the resolved condition has actually been brought to the required current state and whether the evidence is sufficient to support progression to the next governed lifecycle stage.

## Resolution Verification Definition

Verification is the controlled examination of a resolution claim against current requirements, evidence, observations and boundaries to determine whether the claimed state is demonstrated.

## Resolution Verification Scope

Scope shall identify affected systems, services, users, data, decisions, dependencies, environments and boundaries included in the resolution claim.

## Resolution Verification Authority

Authority shall define who may perform, review, challenge, approve or reject verification and who may require additional testing.

## Resolution Verification Criteria

Criteria shall distinguish verified, partially verified, failed and unknown states.

```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA MET?
├── NO → FAIL / REOPEN
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

Preconditions include defined required state, current criteria, verification method, evidence availability, scope, authority and independence requirements.

## Resolution Verification Evidence

Evidence shall be current, attributable, reproducible where applicable, traceable to the resolution and sufficient to support the verification determination.

## Resolution Verification Method

Methods may include inspection, testing, sampling, observation, measurement, replay, comparison, control testing, outcome validation and independent assurance.

```text
RESOLUTION
↓
SELECT METHOD
↓
OBSERVE / TEST / MEASURE
↓
COMPARE WITH CRITERIA
↓
DETERMINE
```

## Resolution Verification Decision

Verification decisions shall distinguish verified, partial, failed and unknown outcomes.

```text
VERIFIED → REVALIDATION PATH
PARTIAL → COMPLETE GAPS
FAILED → REOPEN / REMEDIATE
UNKNOWN → COMPLETE EVIDENCE / INVESTIGATE
```

## Resolution Verification Accountability

Accountability shall remain explicit for method selection, evidence sufficiency, determination and recommendation for follow-on action.

## Resolution Verification Timing

Verification shall occur before a resolution is treated as fully effective where required. Delay shall not be used to imply validity.

## Security Resolution Verification

Verify security controls, access, exposure, threat conditions, containment and required security outcomes against current criteria.

## Resilience Resolution Verification

Verify availability, recovery, continuity, capacity, dependency stability and service outcomes against current criteria.

## Compliance Resolution Verification

Verify obligations, controls, evidence, reporting and policy conditions against current criteria.

## Data Resolution Verification

Verify integrity, quality, lineage, access, retention, authorized use and downstream effects against current criteria.

## AI and Agent Resolution Verification

Verify AI/agent authority, policy, tool access, data boundaries, autonomy and behavioural outcomes against current criteria.

```text
AI / AGENT RESOLUTION
↓
AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY + BEHAVIOUR
↓
CURRENTLY VALID?
├── YES → VERIFIED
└── NO → FAIL / REOPEN / RESTRICT
```

## Resolution Verification Failure

Verification failure includes insufficient evidence, failed tests, unexpected outcomes, boundary breaches, invalid criteria or inability to establish the current state.

```text
VERIFICATION FAILURE
↓
NO UNCONTROLLED PROGRESSION
↓
IDENTIFY GAP
↓
REMEDIATE / COMPLETE EVIDENCE
↓
VERIFY AGAIN
```

## Resolution Verification Independence

Where materiality requires it, verification shall be performed or reviewed independently of the remediation role to reduce confirmation bias.

## Resolution Verification Review and Learning

Reviews shall identify recurring verification failures, weak methods, insufficient evidence, blind spots and opportunities to improve resolution quality.

## Verification Determination Model
```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
METHOD APPROPRIATE?
├── NO → REDESIGN / APPROVE
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
AUTHORIZED REVIEW COMPLETE?
├── NO → REVIEW
└── YES → VERIFIED
```

## Verification Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Verified | Required state demonstrated | Proceed to revalidation |
| Partially Verified | Some requirements demonstrated | Complete gaps |
| Failed | Required state not demonstrated | Reopen / remediate |
| Unknown | Evidence insufficient | Investigate / complete evidence |

## Verification Record
| Field | Required |
|---|---|
| Verification ID | Yes |
| Resolution ID | Yes |
| Scope | Yes |
| Criteria Version | Yes |
| Method | Yes |
| Evidence References | Yes |
| Observations | Yes |
| Result | Yes |
| Reviewer | Yes |
| Residual Risk | Yes |
| Follow-on Decision | Yes |

## Verification Blind Spots
Known blind spots shall be documented. Material blind spots may require additional testing, compensating controls, restricted progression or reopening.

```text
KNOWN BLIND SPOT
↓
MATERIAL?
├── NO → DOCUMENT / MONITOR
└── YES → ADD TEST / CONTROL / RESTRICT
```

## Verification Scope Control
Verification shall not silently expand or contract the resolution claim. Any material scope change shall be governed and reflected in the criteria and verification record.

## Verification Change Control
Changes to criteria, methods, evidence requirements, reviewer independence or decision thresholds shall be governed, approved, versioned and effective-dated.

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
Verification shall not be reduced to checking that remediation tasks were completed. It shall establish whether the resulting current state meets the required criteria.

Historical verification records, methods, evidence, observations, failures, blind spots, reviewer decisions and follow-on determinations shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-resolution-verification layer beneath mandatory resolution. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, monitoring, alerting, escalation, closure, post-closure monitoring or regression detection layers.

## Governance-to-Verification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → REACCEPTANCE → RELIANCE RESTORATION → MONITORING → ALERTING → ESCALATION → RESOLUTION → MANDATORY VERIFICATION → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION
```

## Complete Verification Chain
```text
RESOLVE → DEFINE CURRENT STATE → VERIFY → DETERMINE → REVALIDATE → REACCEPT → RESTORE RELIANCE → MONITOR → ALERT → ESCALATE → RESOLVE
```

## Next Document
`EA-IMETA-PC-RG-045` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification Revalidation

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL RESOLUTION CLAIMS TO BE VERIFIED AGAINST CURRENT REQUIREMENTS, SUFFICIENT EVIDENCE, OBSERVED OUTCOMES AND APPLICABLE BOUNDARIES BEFORE THEY MAY PROGRESS TO REVALIDATION, REACCEPTANCE OR RELIANCE RESTORATION, WITH UNKNOWN, PARTIAL AND FAILED RESULTS REMAINING DISTINCT FROM VERIFIED STATE.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-MANDATORY-VERIFICATION-01
